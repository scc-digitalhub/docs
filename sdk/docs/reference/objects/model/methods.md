# Model object

The `Model` object comes with three sets of methods: CRUD methods, I/O methods and kind specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

??? example "save"

    ::: digitalhub.entities.model._base.entity.Model.save
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "export"

    ::: digitalhub.entities.model._base.entity.Model.export
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "refresh"

    ::: digitalhub.entities.model._base.entity.Model.refresh
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## I/O methods

I/O methods are used to handle objects as files.

??? example "as_file"

    ::: digitalhub.entities.model._base.entity.Model.as_file
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "download"

    ::: digitalhub.entities.model._base.entity.Model.download
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "upload"

    ::: digitalhub.entities.model._base.entity.Model.upload
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Model specific methods

There are several generic model methods on the `Model` object.

??? example "log_metric"

    ::: digitalhub.entities.model._base.entity.Model.log_metric
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "log_metrics"

    ::: digitalhub.entities.model._base.entity.Model.log_metrics
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Kind specific methods

Methods specific to a model kind are documented in the corresponding kind reference page: [model](kind/model.md), [mlflow](kind/mlflow.md), [sklearn](kind/sklearn.md), [huggingface](kind/huggingface.md), [tvm-ir](kind/tvm-ir.md), or [tvm-so](kind/tvm-so.md).
