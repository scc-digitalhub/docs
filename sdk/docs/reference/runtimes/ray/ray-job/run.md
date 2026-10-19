---
render_macros: true
---

# Run a Ray Job

Call `function.run(action="job", ...)` to execute a Ray function on a dynamically created cluster.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `job`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits and requests for each worker task. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template for each worker task. |
| replicas | int | Initial number of worker replicas. |
| min_replicas | int | Minimum number of worker replicas. |
| max_replicas | int | Maximum number of worker replicas. |
| auto_build | bool | Build when the Function has no image. Defaults to `False`. An existing image is not rebuilt automatically when requirements change. |
| parameters | dict | Parameters passed to the Ray application. |

## Example

```python
run = function.run(
    action="job",
    replicas=2,
    min_replicas=2,
    max_replicas=4,
    parameters={"epochs": 10},
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
