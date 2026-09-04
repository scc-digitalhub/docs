# CRUD

The CRUD methods create, read, update and delete triggers. The syntax is the same for all CRUD methods.

## Create

`new_trigger()` creates and saves a trigger. Its specification depends on the selected kind. See the [scheduler kind](kind/scheduler.md) and [lifecycle kind](kind/lifecycle.md) references for the supported parameters.

??? example "new_trigger"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_trigger

    === "Creation examples"

        **Scheduler**

        ```python
        import digitalhub as dh

        trigger = dh.new_trigger(
            project="my-project",
            name="daily-run",
            kind="scheduler",
            task="store://my-project/task/my-task:latest",
            function="store://my-project/function/my-function:latest",
            schedule="0 0 * * * ?",
        )
        ```

        **Lifecycle**

        ```python
        import digitalhub as dh

        trigger = dh.new_trigger(
            project="my-project",
            name="model-complete",
            kind="lifecycle",
            task="store://my-project/task/my-task:latest",
            function="store://my-project/function/my-function:latest",
            key="store://my-project/model/*",
            states=["COMPLETED"],
        )
        ```

## Read

Use the read methods to retrieve triggers from the backend or load them from a YAML descriptor.

??? example "get_trigger"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_trigger

    === "Example"

        ```python
        import digitalhub as dh

        trigger = dh.get_trigger(
            identifier="daily-run",
            project="my-project",
        )
        ```

??? example "list_triggers"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_triggers

    === "Example"

        ```python
        import digitalhub as dh

        triggers = dh.list_triggers(project="my-project")
        ```

??? example "import_trigger"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_trigger

    === "Example"

        ```python
        import digitalhub as dh

        trigger = dh.import_trigger("my-trigger.yaml")
        ```

## Update

Update a trigger after changing its mutable metadata.

??? example "update_trigger"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_trigger

    === "Example"

        ```python
        import digitalhub as dh

        trigger = dh.get_trigger(
            identifier="daily-run",
            project="my-project",
        )
        trigger.set_description("Updated trigger")
        trigger = dh.update_trigger(trigger)
        ```

## Delete

Delete one trigger version or all versions of a trigger.

??? example "delete_trigger"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_trigger

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_trigger(
            identifier="daily-run",
            project="my-project",
            delete_all_versions=True,
        )
        ```
