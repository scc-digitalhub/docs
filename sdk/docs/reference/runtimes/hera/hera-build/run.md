---
render_macros: true
---

# Build a Hera Workflow

Call `workflow.run(action="build", ...)` or `workflow.build()` to compile the workflow definition.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `build`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| auto_build | bool | Invoke `build()` automatically when the workflow definition is missing. Defaults to `False`. This is generally useful for Pipeline runs; it is not normally needed for a Build run. |
| parameters | dict | Stored in the run specification but ignored by the current build executor. |

Hera is used by the remote process that builds and runs the workflow; it is not required in the client environment.

## Example

```python
run = workflow.run(
    action="build",
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
