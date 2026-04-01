# Exposing Open Inference v2 Services

The Open Inference protocol v2 is a protocol used by various inference providers (e.g., NVIDIA Triton, KServe) to expose models that can be used for ML inference.
It defines a standard interfaces, defined by input and output tensor definitions to define how the interaction should be performed in a platform-agnostic manner.

In this tutorial we  demonstrate how to deploy a Visual Question Answering (VQA) service using the [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) model from Salesforce and serve it via the **OpenInference** runtime on the platform.

The workflow covers:
1. Setting up the project and source directory
2. Writing the inference service code
3. Registering and deploying the function
4. Sending inference requests to the running service

## 1. Initialize the DigitalHub Project

Import the `digitalhub` SDK and create (or retrieve) a project named `demo`. The project acts as a namespace for all functions, artifacts, and runs in DigitalHub.

```python
import digitalhub as dh

project = dh.get_or_create_project("demo")
```

## 2. Write the Inference Service Code

Prepare the source directory

```python
from pathlib import Path

Path("src").mkdir(exist_ok=True)
```

Use the `%%writefile` magic to write `src/openinference_service.py` to disk. This file contains:

- **`VQAModel`** — a wrapper around the `Salesforce/blip-image-captioning-base` model that loads the BLIP processor and model onto the available device (GPU or CPU) and exposes a `generate_caption` method for both image captioning and visual question answering.
- **`init_context(context)`** — called once at server startup; loads the `VQAModel` and attaches it to the server context.
- **`handler(context, request)`** — the per-request inference function; decodes the incoming raw image bytes, optionally reads a `question` parameter, calls `generate_caption`, and returns the result as a `BYTES` output tensor.
```python
%%writefile "src/openinference_service.py"

"""
Visual Question Answering Service using BLIP model and PyTriton.

This microservice serves a BLIP model for visual question answering tasks.
It accepts images (JPEG/PNG) and returns text descriptions.
"""

import base64

from io import BytesIO
from PIL import Image
import json

# Import transformers for BLIP model
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Configure logging
import time


class VQAModel:
    """Visual Question Answering model wrapper for BLIP."""
    
    def __init__(self, model_name: str = "Salesforce/blip-image-captioning-base"):
        """
        Initialize the BLIP model and processor.
        
        Args:
            model_name: HuggingFace model identifier
        """
        print(f"Loading BLIP model: {model_name}")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name).to(self.device)
        print("Model loaded successfully")
    
    def generate_caption(self, image: Image.Image, question: str = None) -> str:
        """
        Generate a caption or answer for the given image.
        
        Args:
            image: PIL Image
            question: Optional question text for VQA
            
        Returns:
            Generated text description
        """
        if question:
            # Visual question answering
            inputs = self.processor(image, question, return_tensors="pt").to(self.device)
        else:
            # Image captioning
            inputs = self.processor(image, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            output = self.model.generate(**inputs, max_new_tokens=50)
        
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption


def init_context(context):
    """Initialize the VQA model at server startup."""
    vqa_model = VQAModel()
    setattr(context, "model", vqa_model)

def handler(context, request):
    """
    Inference function for the VQA model.
    
    Args:
        request: Inference Request object
        
    Returns:
        List inference response
    """
    vqa_model = getattr(context, 'model', None)
    if vqa_model is None:
        init_context(context)
        vqa_model = getattr(context, 'model', None)
    
    vqa_model = context.model
    image_bytes = request.inputs[0].data

    caption = ""
    try:
        # Convert bytes to PIL Image
        image_bytes_clean = bytes(image_bytes)
        image = Image.open(BytesIO(image_bytes_clean)).convert('RGB')
        # time.sleep(2)  # Simulate processing time
        # Generate caption

        if request.parameters and "question" in request.parameters:
            question = request.parameters["question"]
            caption = vqa_model.generate_caption(image, question)
        else:
            caption = vqa_model.generate_caption(image)
        
        context.logger.info(f"Generated caption: {caption}")
        
    except Exception as e:
        context.logger.error(f"Error processing image: {e}")
        # caption = f"Error: {str(e)}"
    

    # Convert results to numpy array with object dtype for variable-length strings
    return {
        "outputs": 
            [
                {"name": "caption", "datatype": "BYTES", "data": [caption], "shape": [1, len(caption)]}
            ]
        
    }

```

## 3. Register the Function in DigitalHub

Create a new **OpenInference** function in the project that points to the service file written above. Key parameters:

| Parameter | Value | Description |
|---|---|---|
| `kind` | `openinference` | Runtime type used by DigitalHub |
| `handler` | `handler` | Per-request inference entry point |
| `init_function` | `init_context` | Called once at startup to load the model |
| `model_name` | `vqa_blip` | Model name exposed by the inference server |
| `inputs` | `image (UINT8)` | Raw image bytes accepted by the model |
| `outputs` | `caption (BYTES)` | Text caption/answer returned by the model |
| `requirements` | torch, transformers, pillow | Python packages installed in the serving environment |


```python
func = project.new_function(name="vqa-oi",
                            kind="openinference",
                            python_version="PYTHON3_10",
                            code_src="src/openinference_service.py",
                            handler="handler",
                            init_function="init_context",
                            model_name="vqa_blip",
                            inputs=[{
                                "name": "image",
                                "datatype": "UINT8",
                                "shape": [-1,-1]
                            }],
                            outputs=[{
                                "name": "caption",
                                "datatype": "BYTES",
                                "shape": [-1,-1]
                            }],
                            requirements=["torch>=2.0.0", "transformers>=4.30.0", "pillow>=10.0.0"]
                           )
```

## 4. Deploy the Function as a Serving Endpoint

Run the registered function with the `serve` action to start an inference server. The resource requests ensure the BLIP model weights can be downloaded and held in memory.

> **Note:** This cell is kept as a raw cell to prevent accidental re-deployment. Convert it to a code cell and run it when you want to (re)deploy the service.

```python
run = func.run(action="serve", resources={"mem": "4Gi", "disk": "30Gi"})
```

## 5. Prepare an Inference Request

Configure the client with the service URL and model name, then download a sample parrot image from HuggingFace. The image bytes are wrapped into a KServe v2 inference request payload with a single `UINT8` input tensor.

```python
import requests
import urllib.request

BASE_URL = run.refresh().status.service['url']
MODEL_NAME = 'vqa_blip'

img_url = 'https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png'
with urllib.request.urlopen(img_url) as response:
    image_bytes = response.read()

    request = {
        "inputs": [
                {
                    "name": "input",
                    "datatype": "UINT8",
                    "shape": [1, len(image_bytes)],
                    "data": list(image_bytes)
                }
            ]    
    }
```

## 6. Send the Inference Request

POST the prepared payload to the KServe v2 inference endpoint (`/v2/models/{model_name}/infer`) and print the HTTP status code to confirm the request was received successfully.

```python
response = requests.post(
        f"http://{BASE_URL}/v2/models/{MODEL_NAME}/infer",
        json=request,
        headers={"Content-Type": "application/json"}
    )
    
print(f"Status Code: {response.status_code}")
data = response.json()

```

## 7. Inspect the Response

Display the full JSON response returned by the inference server. The response follows the Open Inference v2 format and includes an `outputs` array with the model's generated caption for the image.

```python
print(data)
``` 