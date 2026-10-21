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
| image | str | | TVM execution image. |
| simplify | bool | | Simplify the source model during conversion. |
| target_opset | int | | Target ONNX opset. |
| opset_override | int | | Override the source ONNX opset. |
| strict_shape_inference | bool | | Enable strict shape inference. |
| data_prop | bool | | Enable data propagation. |
| keep_params_in_input | bool | | Keep model parameters as inputs. |
| sanitize_input_names | bool | | Sanitize model input names. |
| model | str | | Source model path or store key. Uses the Function's `model` when omitted. |
| format | str | | Source model format: `auto`, `onnx`, or `tflite`. |
| ir_model | str | | Store key for the Relax IR output. |
| so_model | str | | Store key for a compiled model output. |
| inputs | dict[str, str] | | Mapping of input names to Dataitem or store keys. |
| local_execution | bool | | Execute the run locally instead of remotely. |

## Example

```python
run = function.run(
    action="build",
    simplify=True,
    ir_model="store://my-project/model/model-relax:version",
    resources={"cpu": 2, "mem": "4Gi"},
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
