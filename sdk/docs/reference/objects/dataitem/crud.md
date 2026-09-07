# CRUD

The CRUD methods are used to create, read, update and delete dataitems. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage dataitems from the project, you can use the `Project` object and avoid specifying the `project` parameter. In this case, specify every parameter as a keyword argument.

## Create

Creation methods differ in how they handle the source:

- `log_<kind>()` creates an entity and uploads a local source to a dataitem store.
- `register_<kind>()` creates an entity for a source that already exists in a store; `name` is optional and can be inferred from the source.
- `new_dataitem()` creates and saves an entity from its specification and path without uploading a source.

For specification parameters, see the documentation for the relevant [dataitem kind](kind/dataitem.md), [table kind](kind/table.md), or [croissant kind](kind/croissant.md).

### Log

??? example "log_dataitem"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_dataitem(
            project="my-project",
            name="raw-events",
            source="./data/events.jsonl",
            labels=["raw", "events"],
        )
        ```

??? example "log_table"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_table

    === "Creation example"

        ```python
        import digitalhub as dh
        import pandas as pd

        table_from_source = dh.log_table(
            project="my-project",
            name="sales-from-file",
            source="./data/sales.csv",
            file_format="csv",
        )

        table_from_data = dh.log_table(
            project="my-project",
            name="sales-from-dataframe",
            data=pd.DataFrame(
                {
                    "customer_id": [101, 102],
                    "amount": [12.50, 8.75],
                }
            ),
        )
        ```

??? example "log_croissant"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_croissant

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_croissant(
            project="my-project",
            name="catalog",
            source="./data/croissant/metadata.json",
            description="Product catalog described with Croissant metadata.",
        )
        ```

### Register

??? example "register_dataitem"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_dataitem

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_dataitem(
            project="my-project",
            name="registered-events",
            source="s3://my-bucket/data/events.jsonl",
        )
        ```

??? example "register_table"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_table

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_table(
            project="my-project",
            name="registered-sales",
            source="s3://my-bucket/data/sales.parquet",
            schema={
                "fields": [
                    {"name": "customer_id", "type": "integer"},
                    {"name": "amount", "type": "float"},
                ]
            },
        )
        ```

??? example "register_croissant"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_croissant

    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_croissant(
            project="my-project",
            name="registered-catalog",
            source="s3://my-bucket/data/croissant/metadata.json",
        )
        ```

### New

??? example "new_dataitem"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

## Read

Use the read methods to retrieve dataitems from the backend or load them from a YAML descriptor.

??? example "get_dataitem"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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
