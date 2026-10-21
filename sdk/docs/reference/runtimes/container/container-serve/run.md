---
render_macros: true
---

# Run a Container Service

Call `function.run(action="serve", ...)` to deploy the container as a service. Pass service and execution parameters as keyword arguments to the same call.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve` |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. Example: `{"cpu": "1", "mem": "512Mi"}`. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [replicas](../../../configuration/kubernetes.md#replicas) | int | | Number of replicas. Must be non-negative. |
| [service_ports](../../../configuration/kubernetes.md#service-port-and-type) | list[dict] | | Ports to expose for the service. Each port and target port must be an integer. Example: `[{"port": 80, "target_port": 8080}]`. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | Service type: `ClusterIP`, `LoadBalancer`, `NodePort` or `ExternalName`. |
| service_name | str | | Service name. |
| [run_as_user](../../../configuration/kubernetes.md#security-context) | int | | User ID to run the container. Must be non-negative. |
| [run_as_group](../../../configuration/kubernetes.md#security-context) | int | | Group ID to run the container. Must be non-negative. |
| [fs_group](../../../configuration/kubernetes.md#security-context) | int | | File system group ID. Must be positive. |
| args | list[str] | | Command-line arguments to pass to the container command. |

## Example

```python
run = function.run(
    action="serve",
    replicas=3,
    service_ports=[{"port": 80, "target_port": 8080}]
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
