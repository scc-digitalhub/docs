---
render_macros: true
---

# Deploy a Flower Client

Call `function.run(action="deploy", ...)` to deploy the client to its federation.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `deploy`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes for deployment. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| superlink | str | | Flower SuperLink service endpoint. |
| node_config | dict | | Flower client node configuration. |
| root_certificates | str | | Root certificate content for secure communication. |
| private_key_secret | str | | [Secret](../../../objects/secret/entity.md) containing the private key for secure communication. |
| public_key_secret | str | | [Secret](../../../objects/secret/entity.md) containing the public key for secure communication. |
| isolation | str | | Isolation mode: `process` or `subprocess`. |

## Example

```python
run = function.run(
    action="deploy",
    superlink="superlink-service",
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
