---
render_macros: true
---

# Run a Python Service

Call `function.run(action="serve", ...)` to deploy the Python function as an HTTP service.

## Task and run parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [replicas](../../../configuration/kubernetes.md#replicas) | int | | Number of service replicas. |
| service_type | str | | Kubernetes service type. |
| service_name | str | | Name assigned to the created service. |
| inputs | dict | | Mapping of handler argument names to platform entity keys. |
| parameters | dict | | Extra values passed to handler arguments. |
| init_parameters | dict | | Values supplied to the init function. |

Serving functions run remotely. Ensure the configured image contains the required dependencies; run the [Python Build action](../python-build/action.md) first when requirements need to be installed.

## Example

```python
run = function.run(
    action="serve",
    replicas=2,
    service_type="NodePort",
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
