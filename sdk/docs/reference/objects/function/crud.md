# CRUD

The CRUD methods create, read, update and delete functions. They can be called directly from the SDK or through a `Project` object.
The syntax is the same for all CRUD methods. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument.

## Create

`new_function()` creates and saves a function. The `kind` and other specification parameters are determined by the runtime. See the [runtime documentation](../../runtimes/index.md) when creating a function.

??? example "new_function"

    Create and save a function.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_function

    === "Creation example"

        ```python
        import digitalhub as dh

        function = dh.new_function(
            project="my-project",
            name="my-function",
            kind="python",
            code_src="function.py",
            handler="function-handler",
        )
        ```

## Read

Use the read methods to retrieve functions from the backend or load them from a YAML descriptor.

??? example "get_function"

    Get one function by name and project. Omitting `entity_id` returns the latest version.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_function

    === "Example"

        ```python
        import digitalhub as dh

        function = dh.get_function(
            identifier="my-function",
            project="my-project",
        )
        ```

??? example "get_function_versions"

    Get all versions of a function by name and project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_function_versions

    === "Example"

        ```python
        import digitalhub as dh

        functions = dh.get_function_versions(
            identifier="my-function",
            project="my-project",
        )
        ```

??? example "list_functions"

    List the latest functions in a project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_functions

    === "Example"

        ```python
        import digitalhub as dh

        functions = dh.list_functions(project="my-project")
        ```

??? example "import_function"

    Import a function from a local YAML descriptor or a storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_function

    === "Example"

        ```python
        import digitalhub as dh

        function = dh.import_function("my-function.yaml")
        ```

## Update

Update a function after changing its mutable metadata.

??? example "update_function"

    Update an existing function. Its specification is immutable.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_function

    === "Example"

        ```python
        import digitalhub as dh

        function = dh.get_function(
            identifier="my-function",
            project="my-project",
        )
        function.set_description("Updated function")
        function = dh.update_function(function)
        ```

## Delete

Delete one function version or all versions of a function.

??? example "delete_function"

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
                    - delete_function

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_function(
            identifier="my-function",
            project="my-project",
            delete_all_versions=True,
        )
        ```
