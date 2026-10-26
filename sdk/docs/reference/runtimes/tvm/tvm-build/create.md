---
render_macros: true
---

# Create a TVM Function

Define a `tvm` Function with the source model and optional artifact store keys.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `tvm`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether to embed the object in the project. |
| model | str | ✓ | Source model path or store key. |
| format | str | | Source model format: `auto`, `onnx`, or `tflite`. |
| ir_model | str | | Relax IR model reference; CORE updates it after a successful `build`. |
| so_model | str | | Compiled model reference; CORE updates it after a successful `compile`. |

Use a `store://` Model reference or an `s3://`/`https://` source reachable by the
CORE Job. A path on your laptop is not a remote Job input: upload it with
`project.log_onnx(source="model.onnx", name="my-model")` (or `log_tflite`) and pass
the returned Model's `.key`. Compilation and serving require the produced bundles,
not the original ONNX/TFLite file.

## Example

```python
import digitalhub as dh

function = dh.new_function(
    project="my-project",
    name="my-tvm-model",
    kind="tvm",
    model="s3://my-bucket/models/model.onnx",
    format="onnx",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
