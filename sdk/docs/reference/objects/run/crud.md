# CRUD

The CRUD methods create, read, update and delete runs. The syntax is the same for all CRUD methods.

## Create

`new_run()` creates and saves a run. The `kind` and other specification parameters are determined by the runtime. See the [runtime documentation](../../runtimes/index.md) when creating a run.

??? example "new_run"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_run

    === "Creation example"

        ```python
        import digitalhub as dh

        run = dh.new_run(
            project="my-project",
            kind="python+run",
            task="task-string",
        )
        ```

## Read

Use the read methods to retrieve runs from the backend or load them from a YAML descriptor.

??? example "get_run"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_run

    === "Example"

        ```python
        import digitalhub as dh

        run = dh.get_run(
            identifier="my-run-id",
            project="my-project",
        )
        ```

??? example "list_runs"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_runs

    === "Example"

        ```python
        import digitalhub as dh

        runs = dh.list_runs(project="my-project")
        ```

??? example "import_run"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_run

    === "Example"

        ```python
        import digitalhub as dh

        run = dh.import_run("my-run.yaml")
        ```

## Update

Update a run after changing its mutable metadata.

??? example "update_run"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_run

    === "Example"

        ```python
        import digitalhub as dh

        run = dh.get_run(
            identifier="my-run-id",
            project="my-project",
        )
        run.set_description("Updated run")
        run = dh.update_run(run)
        ```

## Delete

Delete a run from the backend.

??? example "delete_run"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_run

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_run(
            identifier="my-run-id",
            project="my-project",
        )
        ```
