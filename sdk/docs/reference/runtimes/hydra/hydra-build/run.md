---
render_macros: true
---

# Build a Hydra Execution Image

Call `function.run(action="build", ...)` to build the function's execution image.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `build`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [instructions](#instructions) | list[str] | | Build instructions executed as `RUN` lines in the generated Dockerfile. |
| parameters | dict | | Extra parameters passed to the function. |
| init_parameters | dict | | Parameters supplied to the init function. |

## Instructions

Instructions are executed as `RUN` lines in the generated Dockerfile:

```python
instructions = ["apt-get install -y git"]
```

## Example

```python
run = function.run(
    action="build",
    instructions=["apt-get install -y git"],
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
