---
render_macros: true
---

# Serve a TVM Model

Call `function.run(action="serve", ...)` with the service settings. The Run uses
`function.so_model` unless you set `model_path` explicitly.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| model_path | str | | Optional `store://` reference to a `tvm-so` Model; otherwise uses `function.so_model`. |
| served_name | str | | Model name in `/v2/models/<name>`; defaults to the Function name. |
| image | str | | TVM execution image. |
| replicas | int | | Number of service replicas. |
| workers | int | | Number of workers per replica. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | Kubernetes service type. |
| service_name | str | | Extra Kubernetes service name, `<function>-<service_name>`; distinct from `served_name`. |

Serving options belong to the Run. Reusable Tasks contain only common infrastructure
settings, for example:

```python
task = function.new_task(action="serve", resources={"cpu": "2", "mem": "2Gi"})
```

## Example

```python
run = function.run(
    action="serve",
    served_name="my-model",
    replicas=1,
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
