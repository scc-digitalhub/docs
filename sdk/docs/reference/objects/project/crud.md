# CRUD

The CRUD methods create, read, update and delete projects.

## Create

`new_project()` creates and saves a project. For project configuration options, see the [Config](config.md) and [Setup](setup.md) sections.

??? example "new_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_project

    === "Creation example"

        ```python
        import digitalhub as dh

        project = dh.new_project(name="my-project")
        ```

## Read

Use the read methods to retrieve projects from the backend or load them from a YAML descriptor.

??? example "get_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_project

    === "Example"

        ```python
        import digitalhub as dh

        project = dh.get_project("my-project")
        ```

??? example "import_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_project

    === "Example"

        ```python
        import digitalhub as dh

        project = dh.import_project("my-project.yaml")
        ```

??? example "load_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - load_project

    === "Example"

        ```python
        import digitalhub as dh

        project = dh.load_project("my-project.yaml")
        ```

## Read or create

Use `get_or_create_project()` to retrieve a project or create it when it does not exist.

??? example "get_or_create_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_or_create_project

    === "Example"

        ```python
        import digitalhub as dh

        project = dh.get_or_create_project("my-project")
        ```

## Update

Update a project after changing its mutable metadata.

??? example "update_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_project

    === "Example"

        ```python
        import digitalhub as dh

        project = dh.get_project("my-project")
        project.set_description("Updated project")
        project = dh.update_project(project)
        ```

## Delete

Delete a project from the backend.

??? example "delete_project"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_project

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_project("my-project")
        ```

[Back to Project](./entity.md)
