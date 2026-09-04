# ModelServe runtime

The ModelServe runtime enables deploying ML models as services on Kubernetes. It registers multiple Function kinds for different model formats and supports `serve`; the `mlflowserve` kind also supports `build`.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-modelserve` |

## Supported kinds and actions

| Function kind | Supported actions | Purpose |
| --- | --- | --- |
| `sklearnserve` | `serve` | Serve scikit-learn models |
| `mlflowserve` | `build`, `serve` | Build or serve MLflow models |
| `huggingfaceserve` | `serve` | Serve HuggingFace models |
| `kubeai-text` | `serve` | Serve text generation models via KubeAI |
| `kubeai-speech` | `serve` | Serve speech processing models via KubeAI |
| `vllmserve-text` | `serve` | Serve vLLM text generation models |
| `vllmserve-speech` | `serve` | Serve vLLM speech models |
| `vllmserve-pooling` | `serve` | Serve vLLM models with pooling support |

## Usage pattern

To deploy a model as a service, follow this pattern:

1. Prepare a trained model in one of the supported formats.
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
3. Call `function.run(action="serve")` with task and run parameters.
4. Wait for the service to become ready and use the run's `invoke()` method to send inference requests.

??? example "Serve an MLflow model"

    ```python
    function = dh.new_function(
        name="my-model",
        kind="mlflowserve",
        path="s3://my-bucket/path-to-model"
    )

    run = function.run(
        action="serve",
        replicas=1,
    )
    ```

ModelServe functions are executed remotely on Kubernetes clusters managed by the platform.

!!! warning "Service responsiveness"
    It may take some time for the service to become ready. Use `run.refresh()` and inspect `run.status`. When ready, the `status` will include a `service` attribute.

??? example "Wait for readiness and invoke"

    ```python
    run.refresh()
    run.status
    ```

After the service is ready, call the inference endpoint with `run.invoke()`. By default the `url` is taken from the `run` object; override it with an explicit `url` parameter if needed.

!!! note
    If you set `model_name` in the function spec and run remotely, pass `model_name` to `invoke()` so the runtime can target the model with the MLServer V2 endpoint ("http://{url-from-k8s}/v2/models/{model_name}/infer").

??? example "Invoke an inference endpoint"

    ```python
    data = [[...]]
    json = {
        "inputs": [{
            "name": "input-0",
            "shape": [x, y],
            "datatype": "FP32",
            "data": data
        }]
    }

    run.invoke(json=json)
    ```

## Action documentation

Review the detailed parameters for each ModelServe action:

<div class="list-cards" markdown>

- [**sklearnserve serve**](actions/sklearnserve-serve.md){ .list-card-link }

    Deploy a scikit-learn model as a service.

- [**mlflowserve build**](actions/mlflowserve-build.md){ .list-card-link }

    Build an MLflow model-serving image.

- [**mlflowserve serve**](actions/mlflowserve-serve.md){ .list-card-link }

    Deploy an MLflow model as a service.

- [**huggingfaceserve serve**](actions/huggingfaceserve-serve.md){ .list-card-link }

    Deploy a HuggingFace model as a service.

- [**kubeai-text serve**](actions/kubeai-text-serve.md){ .list-card-link }

    Deploy a text model through KubeAI.

- [**kubeai-speech serve**](actions/kubeai-speech-serve.md){ .list-card-link }

    Deploy a speech model through KubeAI.

- [**vllmserve-text serve**](actions/vllmserve-text-serve.md){ .list-card-link }

    Deploy a vLLM text-generation model.

- [**vllmserve-speech serve**](actions/vllmserve-speech-serve.md){ .list-card-link }

    Deploy a vLLM speech model.

- [**vllmserve-pooling serve**](actions/vllmserve-pooling-serve.md){ .list-card-link }

    Deploy a vLLM model with pooling support.

</div>

## Examples

<div class="list-cards" markdown>

- [**ModelServe examples**](examples.md){ .list-card-link }

    Explore complete examples for supported model-serving kinds.

</div>
