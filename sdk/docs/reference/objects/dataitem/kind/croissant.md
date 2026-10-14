---
render_macros: true
---

# Croissant

The `croissant` kind stores an ML Croissant dataset defined by a `metadata.json` file and its referenced local files. Use this kind to load the dataset through the `mlcroissant` library, which is available through the `digitalhub[mlcroissant]` extra in the [SDK installation guide](../../../../how-to/installation.md).

When logging a Croissant dataitem, the metadata file must be named `metadata.json`; its referenced local files are uploaded with it. An explicit destination `path` must be an S3 partition path ending with `/`. See [supported paths](../../../configuration/paths.md#scheme-specific-paths).

## Create

### Log

{% call function_doc("log_croissant", "digitalhub.entities") %}
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
{% endcall %}

### Register

{% call function_doc("register_croissant", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_croissant(
            project="my-project",
            name="registered-catalog",
            source="s3://my-bucket/data/croissant/metadata.json",
        )
        ```
{% endcall %}

### New

{% call function_doc("new_dataitem", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.new_dataitem(
            project="my-project",
            name="catalog",
            kind="croissant",
            path="s3://my-bucket/data/croissant/catalog/",
        )
        ```
{% endcall %}

## Methods

The `croissant` kind adds dataset loading to the [common Dataitem methods](../use.md).

{{ member_doc("as_dataset", "digitalhub.entities.dataitem.croissant.entity.DataitemCroissant") }}

[Back to dataitem kind selection](../create.md)
