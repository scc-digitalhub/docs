---
render_macros: true
---

# Run a Python Job

Call `function.run(action="job", ...)` to execute the handler as a one-off task.

## Task and run parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `job`.** |
| [volumes](../../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../../configuration/kubernetes.md#profile) | str | Profile template. |
| local_execution | bool | Execute the handler locally instead of remotely. Defaults to `False`; local dependencies must already be installed. |
| auto_build | bool | Build when no image is configured. Defaults to `False`; an existing image is not rebuilt when requirements change. |
| inputs | dict | Mapping of handler argument names to platform entity keys. |
| parameters | dict | Extra values passed to handler arguments. |
| init_parameters | dict | Values supplied to the init function. |

For remote execution with requirements, set `auto_build=True` when no image is configured, or build the function explicitly.

## Example

```python
run = function.run(
    action="job",
    inputs={"data": dataitem.key},
    parameters={"threshold": 0.5},
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
