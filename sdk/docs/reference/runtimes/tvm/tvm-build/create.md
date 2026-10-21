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
| ir_model | str | | Store key for the Relax IR model produced by `build`. |
| so_model | str | | Store key for the compiled `model.so` produced by `compile`. |

The source model can be a local path, store key, or supported repository/archive URI. See the [code source reference](../../../configuration/code-sources.md) for URI formats.

## Example

```python
function = dh.new_function(
    name="my-tvm-model",
    kind="tvm",
    model="s3://my-bucket/models/model.onnx",
    format="onnx",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
