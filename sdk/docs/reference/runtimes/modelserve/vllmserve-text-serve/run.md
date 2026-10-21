---
render_macros: true
---

# Run a vLLM Text Function

Call `function.run(action="serve", ...)` to deploy the vLLM text model. Configure the service with the following parameters.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve` |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [replicas](../../../configuration/kubernetes.md#replicas) | int | | Number of replicas. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | Service type. |
| service_name | str | | Service name. |
| url | str | | URL of the vLLM service. |
| args | list[str] | | Arguments for the vLLM server. |
| enable_telemetry | bool | | Enable or disable telemetry. |
| use_cpu_image | bool | | Use a CPU image for serving. |
| storage_space | str | | Storage space for model artifacts. |

## Example

```python
run = function.run(
    action="serve",
    args=["--help"]
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
