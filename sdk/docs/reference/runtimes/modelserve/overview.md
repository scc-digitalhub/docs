# ModelServe Runtime

The ModelServe runtime enables deploying ML models as services on Kubernetes. It registers multiple Function kinds for different model formats and supports the `serve` action for model deployment. The `mlflowserve` kind also supports `build`.

- **`sklearnserve`**: Serve scikit-learn models
- **`mlflowserve`**: Build or serve MLflow models
- **`huggingfaceserve`**: Serve HuggingFace models
- **`kubeai-text`**: Serve text generation models via KubeAI
- **`kubeai-speech`**: Serve speech to text models via KubeAI
- **`vllmserve-text`**: Serve vLLM text generation models
- **`vllmserve-speech`**: Serve vLLM speech models
- **`vllmserve-pooling`**: Serve vLLM models with pooling support

## Prerequisites

**Supported Python versions:**

- Python ≥ 3.10, < 3.15

**Required packages:**

- `digitalhub-runtime-modelserve`

Install from PyPI:

```bash
pip install digitalhub-runtime-modelserve
```

## Usage overview

To deploy ML models as services on the platform:

1. Prepare your trained model in the supported format.
2. Create a `Function` resource that references your model.
3. Call `function.run()` to deploy the model as a service.
4. Use the run's `invoke()` method to send inference requests.

!!! warning "Service responsiveness"
    It may take some time for the service to become ready. Use `run.refresh()` and inspect `run.status`. When ready, the `status` will include a `service` attribute.

```python
run.refresh()
run.status
```

After the service is ready, call the inference endpoint with `run.invoke()`. By default the `url` is taken from the `run` object; override it with an explicit `url` parameter if needed.

!!! note
    If you set `model_name` in the function spec and run remotely, pass `model_name` to `invoke()` so the runtime can target the model with the MLServer V2 endpoint ("http://{url-from-k8s}/v2/models/{model_name}/infer").

```python
data = [[...]]  # some array
json = {
    "inputs": [
        {
            "name": "input-0",
            "shape": [x, y],
            "datatype": "FP32",
            "data": data
        }
    ]
}

run.invoke(json=json)
```

See [how to](how-to.md) for detailed instructions on deploying different types of models.
See [Examples](examples.md) for code samples.
