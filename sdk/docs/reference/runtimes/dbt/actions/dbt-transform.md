# DBT Transform

The `transform` action executes a dbt transformation using the DBT runtime. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The DBT runtime wraps the DBT CLI and executes SQL/dbt transformations. At a high level:

1. Downloads input dataitems and loads them into temporary tables in the configured Postgres database
2. Collects the dbt project/code and generates required artifacts (profiles.yml, dbt_project.yml, etc.)
3. Runs the dbt transformation
4. Writes the resulting table back to the database and creates a Dataitem representing the output

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
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. |
| lang | str | Source code language (informational). |

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `transform`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| local_execution | bool | Execute the run locally instead of remotely. (Default: False) |
| inputs | dict | Mapping of function argument names to entity keys. |
| outputs | dict | Mapping of outputs. **MUST BE** in the form: {"output_table": "your-table-output-name"} |
| parameters | dict | Extra parameters passed to the function. |

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
