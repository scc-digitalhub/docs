---
render_macros: true
---

# Build a Flower Server Image

Call `function.run(action="build", ...)` to build the Flower server image.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `build`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes for the build. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits and requests for the build. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| instructions | list[str] | Custom instructions to execute during the container build. |
| auth_public_keys | list[str] | Public keys for authentication. |
| insecure | bool | Disable TLS verification. |

## Example

```python
run = function.run(
    action="build",
    instructions=["pip install -r requirements.txt"],
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
