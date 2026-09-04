# DBT Transform

## Transform reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the transform action does.

- [**Function**](#function){ .list-card-link } - Create a DBT Function.

- [**Task**](#task){ .list-card-link } - Configure the DBT Transform Task.

- [**Run**](#run){ .list-card-link } - Execute the DBT transformation.

</div>

## Overview

The `transform` action executes a dbt transformation using the DBT runtime. At a high level:

1. Collects input material entities and materializes them as versioned tables in the configured PostgreSQL database
2. Collects the SQL source and generates the dbt project files and configuration
3. Runs `dbt run --select <output_table>`
4. Creates one table Dataitem for the resulting table

## Function

??? example "Create a function"

    Define the Function with dbt SQL or a source reference.

    === "Parameters"

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
        | [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
        | [code](../../../configuration/code-sources.md#plain-text-source) | str | SQL source provided as plain text. |
        | base64 | str | SQL source encoded as base64. |
        | [handler](../../../configuration/code-sources.md#handler) | str | Source file path used with repository or archive sources. |
        | lang | str | Source language hint. Defaults to `sql`; dbt transformations use SQL. |

    === "Creation example"

        ```python
        import digitalhub as dh

        function = dh.new_function(
            name="my-function",
            kind="dbt",
            code="SELECT * FROM {{ ref('my_table_ref') }}"
        )
        ```

### Function methods

The DBT Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `transform`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |

    === "Creation example"

        ```python
        run = function.run(
            action="transform",
            resources={"cpu": 2, "mem": "4Gi"},
            inputs={"my_table_ref": dataitem.key},
            outputs={"output_table": "mapped-name"},
        )
        ```

### Task methods

The DBT Transform Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | local_execution | bool | Execute the run locally instead of remotely. (Default: False) |
        | inputs | dict | Mapping of names used by dbt `ref()` calls to material entity keys. Pass `{}` when the SQL has no input references. |
        | outputs | dict | Required mapping containing `output_table`, whose value is the name of the resulting table Dataitem. Example: `{"output_table": "your-table-output-name"}`. |
        | parameters | dict | Additional parameters stored in the run specification. They are not consumed by the dbt runtime. |

    === "Creation example"

        ```python
        run = function.run(
            action="transform",
            local_execution=False,
            inputs={"my_table_ref": dataitem.key},
            outputs={"output_table": "mapped-name"},
        )
        ```

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

??? example "inputs"

    Get the inputs passed to the run.

    ::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.inputs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
??? example "output"

    Get a run output by name.

    ::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.output
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
??? example "outputs"

    Get the outputs produced by the run.

    ::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.outputs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
