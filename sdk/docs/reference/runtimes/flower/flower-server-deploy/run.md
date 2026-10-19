---
render_macros: true
---

# Deploy a Flower Server

Call `function.run(action="deploy", ...)` to deploy the server and coordinate federated-learning clients.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `deploy`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes for deployment. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| auth_public_keys | list[str] | Public keys for client authentication. |
| insecure | bool | Disable TLS verification. Defaults to `False`. |
| auto_build | bool | Build automatically when no image is configured. Defaults to `True`. |

## Example

```python
run = function.run(
    action="deploy",
    auth_public_keys=["client-public-key"],
    auto_build=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
