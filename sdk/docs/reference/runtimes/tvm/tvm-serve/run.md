---
render_macros: true
---

# Serve a TVM Model

Call `function.run(action="serve", ...)` with the compiled model path and service settings.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| model_path | str | | Compiled `model.so` path or store key. |
| served_name | str | | Name used by the served model. |
| image | str | | TVM execution image. |
| replicas | int | | Number of service replicas. |
| workers | int | | Number of workers per replica. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | Kubernetes service type. |
| service_name | str | | Kubernetes service name. |
| model | str | | Source model path or store key. |
| format | str | | Source model format: `auto`, `onnx`, or `tflite`. |
| ir_model | str | | Store key of the Relax IR model. |
| so_model | str | | Store key of the compiled `model.so`. |
| local_execution | bool | | Execute the run locally instead of remotely. |

## Example

```python
run = function.run(
    action="serve",
    model_path="store://my-project/model/model-so:version",
    served_name="my-model",
    replicas=1,
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
