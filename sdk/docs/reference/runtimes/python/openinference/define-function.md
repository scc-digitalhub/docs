# Define an OpenInference v2 Function

OpenInference functions use the shared handler contract documented in [Define a Python Function](../define-function.md). See the [Open Inference Protocol](https://github.com/open-inference/open-inference-protocol) for the protocol details.

## OpenInference-specific details

In addition to the common `project`, `run`, `context`, and `event` arguments, an OpenInference handler receives `request`, an OpenInference `InferRequest` object.

The handler returns a response object containing the protocol outputs:

```python
def func(project, run, context, event, request):
    run.log_metric("my-metric", -14.6)
    image_bytes = request.inputs[0].data

    return {
        "outputs": [
            {
                "name": "caption",
                "datatype": "BYTES",
                "data": [caption],
                "shape": [1, len(caption)],
            }
        ]
    }
```
