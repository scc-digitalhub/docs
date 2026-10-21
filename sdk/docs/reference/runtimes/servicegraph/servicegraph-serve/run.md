---
render_macros: true
---

# Run a ServiceGraph Pipeline

Call `function.run(action="serve", ...)` to deploy the pipeline.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve`. |
| service_ports | list[dict] | | List of exposed service ports and target ports. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | Kubernetes service type. |
| service_name | str | | Service name. |
| [replicas](../../../configuration/kubernetes.md#replicas) | int | | Number of service replicas. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| parameters | dict | | Parameters to customize ServiceGraph flow properties. |

## Example

```python
run = function.run(
    action="serve",
    parameters={"input.url": "http://videosource:1984"},
    service_ports=[{"port": 7777, "target_port": 7777}],
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
