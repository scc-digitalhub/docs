# Dataitem kinds

At the moment, we support the following kinds:

- **`table`**: represents a table
- **`croissant`**: represents an ML Croissant dataset

For each different kind, the `Dataitem` object has its own subclass with different `spec` and `status` attributes.

## Table

The `table` kind indicates that the dataitem is a generic table. It's usefull if you intend to manipulate the dataitem as a dataframe, in fact it has some methods to do so. The default dataframe framework we use to represent a table as dataframe is `pandas`.

### Table spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../configuration/paths/overview.md#entity-paths) | *str* | Path of the dataitem, can be a local path or a remote path, a single filepath or a directory/partition. | *required* |
| `schema` | [*TableSchema*](https://specs.frictionlessdata.io/table-schema/) | Frictionless table schema | `None` |

### Table methods

The `table` kind has the following additional methods:

::: digitalhub.entities.dataitem.table.entity.DataitemTable.as_df
    options:
        heading_level: 4
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.dataitem.table.entity.DataitemTable.write_df
    options:
        heading_level: 4
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Croissant

The `croissant` kind indicates that the dataitem stores an ML Croissant dataset, defined by a
`metadata.json` file and its referenced local files. Use this kind when you want to load the
dataset through the `mlcroissant` library.

When logging a Croissant dataitem, ensure the metadata file is named `metadata.json`. If you
set an explicit `path`, it must be an S3 partition path ending with `/`.

### Croissant spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../configuration/paths/overview.md#entity-paths) | *str* | Path to the Croissant dataset location (directory/partition containing `metadata.json`). | *required* |

### Croissant methods

The `croissant` kind has the following additional methods:

::: digitalhub.entities.dataitem.croissant.entity.DataitemCroissant.as_dataset
    options:
        heading_level: 4
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
