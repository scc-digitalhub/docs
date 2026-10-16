---
render_macros: true
---

# Run a DBT Transformation

Call `function.run(action="transform", ...)` to execute the DBT transformation. Pass parameters as keyword arguments to the same call.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `transform`** |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
| local_execution | bool | Execute the Run locally instead of remotely (default: `False`). Local execution requires `digitalhub-runtime-dbt[local]` and a configured, reachable PostgreSQL connection in DigitalHub. See the [DBT installation instructions](../../../../how-to/installation.md#dbt). |
| inputs | dict | Mapping of names used by dbt `ref()` calls to material entity keys. Pass `{}` when the SQL has no input references. |
| outputs | dict | Required mapping containing `output_table`, whose value is the name of the resulting table Dataitem. Example: `{"output_table": "your-table-output-name"}`. |
| parameters | dict | Additional parameters stored in the run specification. They are not consumed by the dbt runtime. |

## Example

```python
run = function.run(
    action="transform",
    resources={"cpu": 2, "mem": "4Gi"},
    inputs={"my_table_ref": dataitem.key},
    outputs={"output_table": "mapped-name"},
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
