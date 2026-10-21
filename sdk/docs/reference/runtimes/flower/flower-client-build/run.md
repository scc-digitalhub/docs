---
render_macros: true
---

# Build a Flower Client Image

Call `function.run(action="build", ...)` to build the Flower client image.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `build`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes for the build. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests for the build. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| instructions | list[str] | | Custom instructions to execute during the container build. |
| superlink | str | | Flower SuperLink service endpoint. |
| node_config | dict | | Flower client node configuration. |
| root_certificates | str | | Root certificate content for secure communication. |
| private_key_secret | str | | Secret containing the private key for secure communication. |
| public_key_secret | str | | Secret containing the public key for secure communication. |
| isolation | str | | Isolation mode: `process` or `subprocess`. |

## Example

```python
run = function.run(
    action="build",
    instructions=["pip install -r requirements.txt"],
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
