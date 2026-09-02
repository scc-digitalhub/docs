# DBT Transform

The `transform` action executes a dbt transformation using the DBT runtime. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The DBT runtime wraps the dbt CLI and executes SQL transformations. At a high level:

1. Collects input material entities and materializes them as versioned tables in the configured PostgreSQL database
2. Collects the SQL source and generates the dbt project files and configuration
3. Runs `dbt run --select <output_table>`
4. Creates one table Dataitem for the resulting table

## Quick example with bare minimum parameters

```python
import digitalhub as dh

# Create function with dbt code
function = dh.new_function(
    name="my-function",
    kind="dbt",
    code="SELECT * FROM {{ ref('my_table_ref') }}"
)

# Execute transformation
run = function.run(
    action="transform",
    inputs={"my_table_ref": dataitem.key},
    outputs={"output_table": "mapped-name"}
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

Provide at least one of `code`, `code_src` or `base64`. The source must contain SQL for a dbt transformation. When `code_src` points to a repository or archive, also provide `handler` with the source file path.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. **Required. Must be `dbt`** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code_src/overview.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | SQL source provided as plain text. |
| base64 | str | SQL source encoded as base64. |
| [handler](../../../configuration/code_src/overview.md#handler) | str | Source file path used with repository or archive sources. |
| lang | str | Source language hint. Defaults to `sql`; dbt transformations use SQL. |

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `transform`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| local_execution | bool | Execute the run locally instead of remotely. (Default: False) |
| inputs | dict | Mapping of names used by dbt `ref()` calls to material entity keys. Pass `{}` when the SQL has no input references. |
| outputs | dict | Required mapping containing `output_table`, whose value is the name of the resulting table Dataitem. Example: `{"output_table": "your-table-output-name"}`. |
| parameters | dict | Additional parameters stored in the run specification. They are not consumed by the dbt runtime. |

## Entity methods

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.output
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.outputs
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
