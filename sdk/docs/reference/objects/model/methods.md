# Model object

The `Model` object comes with three sets of methods: CRUD methods, I/O methods and kind specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

- `save()`: Save or update the entity into the backend.
- `export()`: Export the entity locally as yaml file.
- `refresh()`: Refresh (read) the entity from the backend.

::: digitalhub.entities.model._base.entity.Model.save
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.model._base.entity.Model.export
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.model._base.entity.Model.refresh
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## I/O methods

I/O methods are used to handle objects as files.

- `as_file()`: Downloads the model into a local temporary destination
- `download()`: Downloads the model into a specified path
- `upload()`: Uploads the model to model spec path

::: digitalhub.entities.model._base.entity.Model.as_file
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.model._base.entity.Model.download
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.model._base.entity.Model.upload
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Model specific methods

There are several generic model methods on the `Model` object.

- `log_metric`: Log a metric in the model.
- `log_metrics`: Log multiple metrics in the model.

::: digitalhub.entities.model._base.entity.Model.log_metric
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.model._base.entity.Model.log_metrics
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Kind specific methods

Kind specific methods are used to express potential behaviors of different object kinds.
See the [kinds section](kinds.md) for more information.
