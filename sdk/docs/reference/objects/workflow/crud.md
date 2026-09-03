# CRUD

The CRUD methods create, read, update and delete workflows. They can be called directly from the SDK or through a `Project` object.
The syntax is the same for all CRUD methods. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument.

## Create

`new_workflow()` creates and saves a workflow. The `kind` and other specification parameters are determined by the Hera runtime. See the [Hera runtime documentation](../../runtimes/hera/overview.md) when creating a workflow.

??? example "new_workflow"

    Create and save a workflow.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_workflow

    === "Creation example"

        ```python
        import digitalhub as dh

        workflow = dh.new_workflow(
            project="my-project",
            name="my-workflow",
            kind="hera",
            code_src="pipeline.py",
            handler="pipeline-handler",
        )
        ```

## Read

Use the read methods to retrieve workflows from the backend or load them from a YAML descriptor.

??? example "get_workflow"

    Get one workflow by name and project. Omitting `entity_id` returns the latest version.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_workflow

    === "Example"

        ```python
        import digitalhub as dh

        workflow = dh.get_workflow(
            identifier="my-workflow",
            project="my-project",
        )
        ```

??? example "get_workflow_versions"

    Get all versions of a workflow by name and project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_workflow_versions

    === "Example"

        ```python
        import digitalhub as dh

        workflows = dh.get_workflow_versions(
            identifier="my-workflow",
            project="my-project",
        )
        ```

??? example "list_workflows"

    List the latest workflows in a project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_workflows

    === "Example"

        ```python
        import digitalhub as dh

        workflows = dh.list_workflows(project="my-project")
        ```

??? example "import_workflow"

    Import a workflow from a local YAML descriptor or a storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_workflow

    === "Example"

        ```python
        import digitalhub as dh

        workflow = dh.import_workflow("my-workflow.yaml")
        ```

## Update

Update a workflow after changing its mutable metadata.

??? example "update_workflow"

    Update an existing workflow. Its specification is immutable.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_workflow

    === "Example"

        ```python
        import digitalhub as dh

        workflow = dh.get_workflow(
            identifier="my-workflow",
            project="my-project",
        )
        workflow.set_description("Updated workflow")
        workflow = dh.update_workflow(workflow)
        ```

## Delete

Delete one workflow version or all versions of a workflow.

??? example "delete_workflow"

    Set `delete_all_versions=True` to delete all versions by entity name.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_workflow

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_workflow(
            identifier="my-workflow",
            project="my-project",
            delete_all_versions=True,
        )
        ```
