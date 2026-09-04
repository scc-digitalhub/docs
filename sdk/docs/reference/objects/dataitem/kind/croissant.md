# Croissant

The `croissant` kind stores an ML Croissant dataset defined by a `metadata.json` file and its referenced local files. Use this kind to load the dataset through the `mlcroissant` library.

When logging a Croissant dataitem, ensure the metadata file is named `metadata.json`. If you set an explicit `path`, it must be an S3 partition path ending with `/`.

## Croissant spec

The `croissant` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths.md#entity-paths) | *str* | Path to the Croissant dataset location, a directory or partition containing `metadata.json`. | *required* |

## Croissant methods

The `croissant` kind has the following additional methods.

??? example "as_dataset"

    Load the Croissant dataitem as a dataset.

    ::: digitalhub.entities.dataitem.croissant.entity.DataitemCroissant.as_dataset
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
