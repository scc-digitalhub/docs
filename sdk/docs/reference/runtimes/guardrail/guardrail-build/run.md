---
render_macros: true
---

# Build a Guardrail Function Image

Call `function.run(action="build", ...)` to build the function image.

## Task and run parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `build`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| instructions | list[str] | Additional Dockerfile instructions, each executed as a `RUN` instruction. |
| init_parameters | dict | Values supplied to the init function. |

## Example

```python
run = function.run(
    action="build",
    instructions=["pip install my-guardrail-lib"],
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
