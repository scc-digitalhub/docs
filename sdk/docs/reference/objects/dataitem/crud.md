# CRUD

The CRUD methods are used to create, read, update and delete dataitems. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage dataitems from the project, you can use the `Project` object and avoid specifying the `project` parameter. In this case, specify every parameter as a keyword argument.

## Create

Creation methods differ in how they handle the source:

- `new_dataitem()` creates and saves an entity.
- `log_<kind>()` creates an entity and uploads the source to a dataitem store.
- `register_<kind>()` creates an entity for an existing source; `name` is optional and can be inferred from the source.

For specification parameters, see the documentation for the relevant [dataitem kind](kind/dataitem.md), [table kind](kind/table.md), or [croissant kind](kind/croissant.md). Use the generic methods only for a kind supported by DigitalHub Core but not by the SDK.

??? example "new_dataitem"

    This function creates a new entity and saves it into the backend.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.new_dataitem(
            project="my-project",
            name="my-table",
            kind="table",
            path="s3://my-bucket/my-table.parquet",
        )
        ```

??? example "log_dataitem"

    This function creates a dataitem and uploads a local source to a dataitem store.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_dataitem(
            project="my-project",
            name="my-dataitem",
            source="./local-dataitem",
        )
        ```

??? example "log_generic_dataitem"

    This function creates a dataitem of a custom kind and uploads a local source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_generic_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_generic_dataitem(
            project="my-project",
            kind="custom-dataitem",
            source="./local-dataitem",
            name="my-dataitem",
        )
        ```

??? example "log_table"

    This function logs a table dataitem from a dataframe, SQL query, or file source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_table

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_table(
            project="my-project",
            name="my-table",
            source="./my-table.csv",
        )

        dataitem = dh.log_table(
            project="my-project",
            name="my-table-2",
            data=pandas-dataframe,
        )
        ```

??? example "log_croissant"

    This function creates a Croissant dataitem by uploading a `metadata.json` file and its referenced local files.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_croissant

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_croissant(
            project="my-project",
            name="my-croissant",
            source="./metadata.json",
        )
        ```

??? example "register_dataitem"

    Register a dataitem whose source already exists in a supported store. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_dataitem(
            project="my-project",
            source="s3://my-bucket/my-dataitem",
        )
        ```

??? example "register_generic_dataitem"

    Register an existing source with a custom dataitem kind.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_generic_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_generic_dataitem(
            project="my-project",
            kind="custom-dataitem",
            source="s3://my-bucket/my-dataitem",
        )
        ```

??? example "register_table"

    Register an existing table source. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_table

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_table(
            project="my-project",
            source="s3://my-bucket/my-table.parquet",
        )
        ```

??? example "register_croissant"

    Register an existing Croissant dataset. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_croissant

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_croissant(
            project="my-project",
            source="s3://my-bucket/my-croissant/",
        )
        ```

## Read

Use the read methods to retrieve dataitems from the backend or load them from a YAML descriptor.

??? example "get_dataitem"

    Get one dataitem by name and project. Omitting `entity_id` returns the latest version. You can also pass a `store://` entity key as `identifier`.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_dataitem

    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.get_dataitem(
            identifier="my-dataitem",
            project="my-project",
        )
        ```

??? example "get_dataitem_versions"

    Get all versions of a dataitem by name and project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_dataitem_versions

    === "Example"

        ```python
        import digitalhub as dh

        dataitems = dh.get_dataitem_versions(
            identifier="my-dataitem",
            project="my-project",
        )
        ```

??? example "list_dataitems"

    List the latest dataitems in a project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_dataitems

    === "Example"

        ```python
        import digitalhub as dh

        dataitems = dh.list_dataitems(project="my-project")
        ```

??? example "import_dataitem"

    Import a dataitem from a local YAML descriptor or a storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_dataitem

    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.import_dataitem("my-dataitem.yaml")
        ```

??? example "load_dataitem"

    Load a dataitem from a local YAML descriptor and update the existing backend entity.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - load_dataitem

    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.load_dataitem("my-dataitem.yaml")
        ```

## Update

Update a dataitem after changing its mutable metadata.

??? example "update_dataitem"

    Update an existing dataitem. The dataitem specification is immutable.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_dataitem

    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.get_dataitem(
            identifier="my-dataitem",
            project="my-project",
        )
        dataitem.set_description("Updated dataitem")
        dataitem = dh.update_dataitem(dataitem)
        ```

## Delete

Delete one dataitem version or all versions of a dataitem.

??? example "delete_dataitem"

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
                    - delete_dataitem

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_dataitem(
            identifier="my-dataitem",
            project="my-project",
            delete_all_versions=True,
        )
        ```
