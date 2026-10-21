---
render_macros: true
---

# Compile a TVM Model

Call `function.run(action="compile", ...)` with the Relax IR path and target settings.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `compile`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| model_path | str | | Relax IR model path or store key. |
| target_architecture | str | | Target CPU profile. See [target architectures](action.md#target-architecture). |
| opt_level | int | | TVM optimization level. |
| cross_cc | str | | Cross-compiler command. |
| exec_mode | str | | TVM execution mode. |
| relax_pipeline | str | | Relax compilation pipeline. |
| tir_pipeline | str | | TIR compilation pipeline. |
| system_lib | bool | | Build a system library. |
| params_path | str | | Model parameters path or store key. |
| tag | str | | Tag for the compiled model. |
| image | str | | TVM execution image. |
| model | str | | Source model path or store key. |
| format | str | | Source model format: `auto`, `onnx`, or `tflite`. |
| ir_model | str | | Store key for the Relax IR model. |
| so_model | str | | Store key for the compiled `model.so`. |
| inputs | dict[str, str] | | Mapping of input names to Dataitem or store keys. |
| local_execution | bool | | Execute the run locally instead of remotely. |

## Example

```python
run = function.run(
    action="compile",
    model_path="store://my-project/model/model-relax:version",
    target_architecture="auto",
    opt_level=3,
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
