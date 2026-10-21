---
render_macros: true
---

# Create an OpenInference Function

See the [Python handler definition](../../python/define-function.md) for general handler structure and the [OpenInference handler definition](../handler.md) for protocol-specific request and response behavior.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `openinference`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | | Source code provided as plain text. |
| base64 | str | | Source code encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | | Function entrypoint. |
| init_function | str | | Init function name for remote execution. |
| [python_version](../../python/params.md#supported-python-versions) | str | ✓ | Execution Python version. |
| lang | str | | Source code language (informational). |
| image | str | | Container image used to execute the function. |
| base_image | str | | Base image (name:tag) used when building the execution image. |
| [requirements](../../python/params.md#requirements-and-builds) | list[str] \| str | | Pip requirements or a supported requirements file. |
| model_name | str | | Logical model name exposed by the inference function. |
| inputs | list[dict] | | Tensor definitions accepted by inference requests. |
| outputs | list[dict] | | Tensor definitions returned by inference responses. |

Each tensor definition has `name` (str), `shape` (list[int]), and `datatype` (str, defaults to `FP32`). Supported datatypes are `BOOL`, `BYTES`, `UINT8`, `INT8`, `UINT16`, `INT16`, `UINT32`, `INT32`, `UINT64`, `INT64`, `FP16`, `FP32`, and `FP64`.

## Example

```python
function = dh.new_function(
    name="text-inference",
    kind="openinference",
    code_src="inference.py",
    handler="predict",
    python_version="PYTHON3_10",
    model_name="text-classifier",
    inputs=[{"name": "input-0", "shape": [-1], "datatype": "BYTES"}],
    outputs=[{"name": "output-0", "shape": [-1], "datatype": "FP32"}],
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
