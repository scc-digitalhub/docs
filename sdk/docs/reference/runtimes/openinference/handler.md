---
render_macros: true
---

# Define an OpenInference Handler

In addition to the `project`, `run`, `context`, and `event` arguments described in the [Python handler definition](../python/define-function.md), an OpenInference handler receives `request`, an OpenInference `InferRequest` object.

The handler returns a response object containing the protocol outputs.

??? example "Example"

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

See the [Open Inference Protocol](https://github.com/open-inference/open-inference-protocol) for protocol details.

{{ page_navigation(("Overview", "overview.md"), ("Python handler definition", "../python/define-function.md")) }}
