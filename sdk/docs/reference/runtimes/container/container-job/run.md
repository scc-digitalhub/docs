---
render_macros: true
---

# Run a Container Job

Call `function.run(action="job", ...)` to execute the container. Pass action and execution parameters as keyword arguments to the same call.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `job` |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. Example: `{"cpu": "1", "mem": "512Mi"}`. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [fs_group](../../../configuration/kubernetes.md#security-context) | int | | File system group ID. Must be positive. |
| [run_as_user](../../../configuration/kubernetes.md#security-context) | int | | User ID to run the container. Must be non-negative. |
| [run_as_group](../../../configuration/kubernetes.md#security-context) | int | | Group ID to run the container. Must be non-negative. |
| args | list[str] | | Command-line arguments to pass to the container command. |

## Example

```python
run = function.run(
    action="job",
    args=["arg1", "arg2"]
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
