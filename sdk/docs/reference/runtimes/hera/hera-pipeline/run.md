---
render_macros: true
---

# Run a Hera Pipeline

Call `workflow.run(action="pipeline", ...)` to execute a compiled workflow on the platform. If its compiled definition is missing, call `workflow.build()` first.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `pipeline`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| parameters | dict | Values for Hera workflow parameters declared in the pipeline source. |

## Example

```python
build_run = workflow.build(wait=True)

run = workflow.run(
    action="pipeline",
    parameters={"url": "https://example.com"},
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
