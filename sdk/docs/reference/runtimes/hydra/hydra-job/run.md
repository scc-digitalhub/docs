---
render_macros: true
---

# Run a Hydra Job

Call `function.run(action="job", ...)` to execute a Hydra function as a one-off job.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Action to execute. **Required. Must be `job`.** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits and requests. Applied to a single subtask, not the orchestrating launcher. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. Applied to a single subtask, not the orchestrating launcher. |
| local_execution | bool | Execute locally instead of remotely. Defaults to `False`. Local dependencies must already be installed. |
| parameters | dict | Hydra configuration overrides passed to the function. |
| init_parameters | dict | Parameters supplied to the init function. |
| workers | int | Number of workers available for parallel execution. |

## Example

```python
run = function.run(
    action="job",
    parameters={
        "trainer.max_epochs": 1,
        "hydra.sweeper.storage": "sqlite:///hpo.db",
    },
    workers=5,
    local_execution=False,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
