---
render_macros: true
---

# Deploy a Flower Server

Call `function.run(action="deploy", ...)` to deploy the server and coordinate federated-learning clients.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `deploy`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes for deployment. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| auth_public_keys | list[str] | | Public keys for client authentication. |
| insecure | bool | | Disable TLS verification. Defaults to `False`. |

## Example

```python
run = function.run(
    action="deploy",
    auth_public_keys=["client-public-key"],
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
