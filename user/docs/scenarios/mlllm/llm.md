# Managing LLM Models

With the platform it is possible to create and serve LLM HuggingFace-compatible-models. Specifically, it is possible to serve directly the LLM models from the HuggingFace catalogue provided the id of the model or to serve the fine-tuned model from the specified path, such as S3.

LLM implementation relies on the [KServe LLM runtime](https://kserve.github.io/website/latest/modelserving/v1beta1/llm/huggingface/) and therefore supports one of the corresponding LLM tasks:

- Text Generation
- Text2Text Generation
- Fill Mask
- Text (Sequence) Classification
- Token Classification

Based on the type of the task the API of the exposed service may differ. Generative models (text generation and text2text generation) use OpenAI's [Completion](https://platform.openai.com/docs/api-reference/completions) and [Chat Completion](https://platform.openai.com/docs/api-reference/chat) API.

The other types of tasks like token classification, sequence classification, fill mask are served using KServe's Open Inference Protocol v2 API.

## Exposing Predefined Text Classification Models

In case of predefined HuggingFace non-generative model it is possible to use ``huggingfaceserve`` runtime to expose the corresponding inference  API. For this purpose it is necessary to define the ``huggingfaceserve`` function definition (via UI or SDK) providing the name of the exposed model and the URI of the model in the following form

``huggingface://<id of the huggingface model>``

For example ``huggingface://distilbert/distilbert-base-uncased-finetuned-sst-2-english``.

When using SDK, this may be accomplished as follows.

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("llm")
```

Create the serving function definition:

```python
llm_function = project.new_function("llm_classification",
                                    kind="huggingfaceserve",
                                    model_name="mymodel",
                                    path="huggingface://distilbert/ distilbert-base-uncased-finetuned-sst-2-english")
```

Serve the model:

```python
llm_run = llm_function.run(action="serve", profile="template-a100")
```

Please note the use of the ``profile`` parameter. As the LLM models require specific hardware (GPU in particular), it is necessary
to specify the HW requirements as described in the  [Configuring Kubernetes executions](../../tasks/kubernetes-resources.md) section. In particular, it is possible to rely on the predefined resource templates of the platform deployment.

As in other scenarios, you need to wait a bit for the service to become available.
Once the service becomes available, it is possible to make the calls:

```python
model_name = "mymodel"
json = {
    "inputs": [
        {
            "name": "input-0",
            "shape": [2],
            "datatype": "BYTES",
            "data": ["Hello, my dog is cute", "I am feeling sad"],
        },
    ]
}

llm_run.invoke(model_name=model_name, json=json).json()
```

Here the classification LLM service API follows the Open Inference protocol API and the expected result should have the following form:

```python
{
    "model_name": "mymodel",
    "model_version": None,
    "id": "cab30aa5-c10f-4233-94e2-14e4bc8fbf6f",
    "parameters": None,
    "outputs": [
        {
            "name": "output-0",
            "shape": [2],
            "datatype": "INT64",
            "parameters": None,
            "data": [1, 0],
        },
    ],
}
```

As in case of other services (ML model services or Serverless functions), it is possible to expose the service using the KRM API gateway functionality.

## Exposing Predefined Text Generation Models

In case of predefined HuggingFace ngenerative model it is possible to use ``huggingfaceserve`` runtime to expose the OpenAI compatible API. For this purpose it is necessary to define the ``huggingfaceserve`` function definition (via UI or SDK) providing the name of the exposed model and the URI of the model in the following form

``huggingface://<id of the huggingface model>``

For example ``huggingface://meta-llama/meta-llama-3-8b-instruct``.

When using SDK, this may be accomplished as follows.

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("llm")
```

Create the serving function definition:

```python
llm_function = project.new_function("llm_generation",
                                    kind="huggingfaceserve",
                                    model_name="mymodel",
                                    path="huggingface://meta-llama/meta-llama-3-8b-instruct")
```

Serve the model:

```python
llm_run = llm_function.run(action="serve", profile="template-a100")
```

Please note that in case of protected models (like, e.g., llama models) it is necessary to path the HuggingFace token. For example,

```python
hf_token = "<HUGGINGFACE TOKEN>"
llm_run = llm_function.run(action="serve",
                           profile="template-a100",
                           envs = [{"name": "HF_TOKEN", "value": hf_token}])
```

As in case of classification models, the LLM models require specific hardware (GPU in particular), it is necessary
to specify the HW requirements as described in the [Configuring Kubernetes executions](../../tasks/kubernetes-resources.md) section. In particular, it is possible to rely on the predefined resource templates of the platform deployment.

Once the service becomes available, it is possible to make the calls. For example, for the completion requests:

```python
service_url = llm_run.refresh().status.to_dict()["service"]["url"]
url = f"http://{service_url}/openai/v1/completions"
model_name = "mymodel"
json = {
    "model": model_name,
    "prompt": "Hello! How are you?",
    "stream": False,
    "max_tokens": 30
}

llm_run.invoke(url=url, json=json).json()
```

Here the expected output should have the following form:

``` json
{
  "id": "cmpl-625a9240f25e463487a9b6c53cbed080",
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": " and how they make you feel\nColors, oh colors, so vibrant and bright\nA world of emotions, a kaleidoscope in sight\nRed"
    }
  ],
  "created": 1718620153,
  "model": "mymodel",
  "system_fingerprint": null,
  "object": "text_completion",
  "usage": {
    "completion_tokens": 30,
    "prompt_tokens": 6,
    "total_tokens": 36
  }
}
```

In case of chat requests:

```python
service_url = llm_run.refresh().status.to_dict()["service"]["url"]
url = f'http://{service_url}/openai/v1/chat/completions'

model_name = "mymodel"

json = {
    "model": model_name,
    "messages": [
        {"role": "system", "content": "You are an assistant that speaks like Shakespeare."},
        {"role": "user", "content": "Write a poem about colors"}
    ],
    "max_tokens": 30,
    "stream": False
}

llm_run.invoke(url=url, json=json).json()
```

Expected output:

``` json
{
  "id": "cmpl-9aad539128294069bf1e406a5cba03d3",
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "message": {
        "content": "  O, fair and vibrant colors, how ye doth delight\nIn the world around us, with thy hues so bright!\n",
        "tool_calls": null,
        "role": "assistant",
        "function_call": null
      },
      "logprobs": null
    }
  ],
  "created": 1718638005,
  "model": "mymodel",
  "system_fingerprint": null,
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 30,
    "prompt_tokens": 37,
    "total_tokens": 67
  }
}
```

As in case of other services (ML model services or Serverless functions), it is possible to expose the service using the KRM API gateway functionality.

## Fine-tuned LLM model

when it comes to custom LLM model, it is possible to create HuggingFace-based fine tuned model, log it and then serve it from the model path.

When using SDK, this may be accomplished as follows.

First, import necessary libraries

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("llm")
```

Create the training procedure that logs model to the platform:

```python
%%writefile "src/train_model.py"

import os

import evaluate
import numpy as np
from datasets import load_dataset
from digitalhub_runtime_python import handler
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments


@handler()
def train(project):
    tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
    metric = evaluate.load("accuracy")

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)

    dataset = load_dataset("yelp_review_full")
    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained("google-bert/bert-base-cased", num_labels=5)

    training_args = TrainingArguments(output_dir="test_trainer")

    small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
    small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))

    training_args = TrainingArguments(output_dir="test_trainer", eval_strategy="epoch")

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=small_train_dataset,
        eval_dataset=small_eval_dataset,
        compute_metrics=compute_metrics,
    )

    trainer.train()

    save_model = "model"
    if not os.path.exists(save_model):
        os.makedirs(save_model)

    save_dir = "model"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    trainer.save_model(save_dir)
    tokenizer.save_pretrained(save_dir)

    project.log_model(
        name="test_llm_model",
        kind="huggingface",
        base_model="google-bert/bert-base-cased",
        source=save_dir,
    )
```

Register the function and execute it:

```python
train_func = project.new_function(name="train_model",
                                  kind="python",
                                  python_version="PYTHON3_9",
                                  code_src="src/train_model.py",
                                  handler="train",
                                  requirements=["evaluate", "transformers[torch]", "torch", "torchvision", "accelerate"])

train_run=train_func.run(action="job", profile="template-a100")
```

Create the serving function definition:

```python
llm_function = project.new_function("llm_classification",
                                    kind="huggingfaceserve",
                                    model_name="mymodel",
                                    path="s3://datalake/llm/model/test_llm_model/f8026820-2471-4497-97f5-8e6d49baac5f/")
```

Serve the model:

```python
llm_run = llm_function.run(action="serve", profile="template-a100")
```

Please note the use of the ``profile`` parameter. As the LLM models require specific hardware (GPU in particular), it is necessary
to specify the HW requirements as described in the  [Configuring Kubernetes executions](../../tasks/kubernetes-resources.md) section. In particular, it is possible to rely on the predefined resource templates of the platform deployment.

Once the service becomes available, it is possible to make the calls:

```python
model_name = "mymodel"
json = {
    "inputs": [
        {
            "name": "input-0",
            "shape": [2],
            "datatype": "BYTES",
            "data": ["Hello, my dog is cute", "I am feeling sad"],
        }
    ]
}

llm_run.invoke(model_name=model_name, json=json).json()
```

Here the classification LLM service API follows the Open Inference protocol API and the expected result should have the following form:

```python
{
    "model_name": "mymodel",
    "model_version": None,
    "id": "cab30aa5-c10f-4233-94e2-14e4bc8fbf6f",
    "parameters": None,
    "outputs": [
        {
            "name": "output-0",
            "shape": [2],
            "datatype": "INT64",
            "parameters": None,
            "data": [4, 0],
        }
    ],
}
```

As in case of other services (ML model services or Serverless functions), it is possible to expose the service using the KRM API gateway functionality.
