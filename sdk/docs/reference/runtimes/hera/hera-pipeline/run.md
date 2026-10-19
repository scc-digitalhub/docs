---
render_macros: true
---

# Run a Hera Pipeline

Call `workflow.run(action="pipeline", ...)` to execute the workflow on the platform. Set `auto_build=True` to build it first when its compiled definition is missing.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `pipeline`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| auto_build | bool | Build automatically when the compiled workflow is missing. Defaults to `False`. Set to `True` to build automatically, or leave it `False` after calling `workflow.build()`. |
| parameters | dict | Values for Hera workflow parameters declared in the pipeline source. |

## Example

```python
run = workflow.run(
    action="pipeline",
    auto_build=True,
    parameters={"url": "https://example.com"},
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
