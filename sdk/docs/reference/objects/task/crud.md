# CRUD

The CRUD methods create, read, update and delete tasks. Tasks are unversioned and belong to a project.

## Create

`new_task()` creates and saves a task. The task `kind` combines an executable kind and an action, for example `python+job`. See the [runtime documentation](../../runtimes/index.md) when creating a task.

??? example "new_task"

    Create and save a task for an executable.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_task

    === "Creation example"

        ```python
        import digitalhub as dh

        task = dh.new_task(
            project="my-project",
            kind="python+job",
            function="python://my-project/my-function:latest",
        )
        ```

## Read

Use the read methods to retrieve tasks from the backend or load them from a YAML descriptor.

??? example "get_task"

    Get a task by its storage key or ID. When using an ID, provide the project name.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_task

    === "Example"

        ```python
        import digitalhub as dh

        task = dh.get_task(
            identifier="my-task-id",
            project="my-project",
        )
        ```

??? example "list_tasks"

    List tasks in a project. Use `function` or `workflow` filters to restrict the results to an executable.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_tasks

    === "Example"

        ```python
        import digitalhub as dh

        tasks = dh.list_tasks(project="my-project")
        ```

??? example "import_task"

    Import a task from a local YAML descriptor or a storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_task

    === "Example"

        ```python
        import digitalhub as dh

        task = dh.import_task("my-task.yaml")
        ```

??? example "load_task"

    Load a task from a local YAML descriptor and update the existing backend object.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - load_task

    === "Example"

        ```python
        import digitalhub as dh

        task = dh.load_task("my-task.yaml")
        ```

## Update

Update a task after changing its mutable metadata. Its specification is immutable where required by the backend.

??? example "update_task"

    Update an existing task.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_task

    === "Example"

        ```python
        import digitalhub as dh

        task = dh.get_task(
            identifier="my-task-id",
            project="my-project",
        )
        task.set_description("Updated task")
        task = dh.update_task(task)
        ```

## Delete

Delete a task from the backend.

??? example "delete_task"

    Delete a task by its entity ID or storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_task

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_task(
            identifier="my-task-id",
            project="my-project",
        )
        ```
