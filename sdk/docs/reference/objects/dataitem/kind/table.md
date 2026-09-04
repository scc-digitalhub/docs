# Table

The `table` kind represents tabular data that can be read and written as a dataframe. The default dataframe engine is `pandas`.

## Table spec

The `table` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths.md#scheme-specific-paths) | *str* | Path of the dataitem, either on the local filesystem or in remote storage. | *required* |
| `schema` | [*TableSchema*](https://specs.frictionlessdata.io/table-schema/) | Frictionless table schema. | `None` |

## Table methods

The `table` kind has the following additional methods.

??? example "as_df"

    Read the table as a dataframe.

    ::: digitalhub.entities.dataitem.table.entity.DataitemTable.as_df
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "write_df"

    Write a dataframe to the table.

    ::: digitalhub.entities.dataitem.table.entity.DataitemTable.write_df
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "query"

    Query the table.

    ::: digitalhub.entities.dataitem.table.entity.DataitemTable.query
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
