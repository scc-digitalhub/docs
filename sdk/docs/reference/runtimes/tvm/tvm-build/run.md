---
render_macros: true
---

# Build a TVM Model

Call `function.run(action="build", ...)` to convert the source model to Relax IR.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `build`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| image | str | | Optional toolkit image override. |
| simplify | bool | | Simplify the ONNX model before conversion. |
| target_opset | int | | Convert to this ONNX opset. |
| opset_override | int | | Importer opset override, without converting the model. |
| strict_shape_inference | bool | | Enable strict shape inference. |
| data_prop | bool | | Enable shape inference data propagation. |
| keep_params_in_input | bool | | Save weights separately in `params.bin`; compile embeds them again. |
| sanitize_input_names | bool | | Sanitize model input names; default `true`. |
| inputs | dict[str, str] | | Mapping of input names to Dataitem or store keys. |

Conversion settings apply to ONNX. The source `model` and `format` belong to the
Function; CORE records the generated IR reference after success.

Reusable Tasks contain only common infrastructure settings, for example:

```python
task = function.new_task(action="build", resources={"cpu": "2", "mem": "4Gi"})
```

## Example

```python
run = function.run(
    action="build",
    simplify=True,
    resources={"cpu": "2", "mem": "4Gi"},
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
