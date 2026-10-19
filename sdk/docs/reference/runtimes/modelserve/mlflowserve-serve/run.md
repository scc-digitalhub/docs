---
render_macros: true
---

# Run an MLflow Serving Function

Call `function.run(action="serve", ...)` to deploy the MLflow model as a service. Configure the service with the following parameters.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `serve`** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| [replicas](../../../configuration/kubernetes.md#replicas) | int | Number of replicas. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Service type. |
| service_name | str | Service name. |

## Example

```python
run = function.run(
    action="serve",
    replicas=1
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
