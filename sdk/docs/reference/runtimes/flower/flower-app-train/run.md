---
render_macros: true
---

# Run a Flower Application

Call `function.run(action="train", ...)` to execute the federated-learning application.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `train`.** |
| schedule | str | Quartz cron expression for scheduling the task. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| local_execution | bool | Run a local Flower simulation instead of submitting the run remotely. Defaults to `False`. |
| [parameters](#training-parameters) | dict | Flower application and training configuration. |
| federation | str | Federation name. Required for remote execution. |
| superlink | str | SuperLink service endpoint. Required for remote execution. |
| root_certificates | str | Root certificate content for secure remote communication. |

## Training parameters

Parameters configure the Flower application. For Git-based applications, they override configuration in `pyproject.toml`; for source-based applications, they are used to generate that configuration.

Reserved parameter names include:

| Name | Type | Description |
| --- | --- | --- |
| name | str | Application name. Defaults to `flower-app`. |
| version | str | Application version. Defaults to `0.1.0`. |
| description | str | Application description. Defaults to `Flower Application`. |
| publisher | str | Publisher. Defaults to `digitalhub-runtime-flower`. |
| dependencies | list[str] | Python package dependencies. |
| packages | list[str] | Python packages to include. Defaults to `["."]`. |

Other parameters beginning with `option.` are added to `[tool.flwr.federations.local-simulation]`; other keys are added to `[tool.flwr.app.config]`. The `serverapp` and `clientapp` components come from the Function parameters.

Local simulation requires the `digitalhub-runtime-flower[local]` extra and the application dependencies. Remote execution runs on a platform-managed server or cluster.

## Example

```python
run = function.run(
    action="train",
    local_execution=False,
    federation="my-federation",
    superlink="superlink-service",
    parameters={"num_rounds": 10},
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
