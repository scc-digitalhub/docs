# Project methods

The `Project` object comes with three sets of methods: CRUD methods, entity specific CRUD methods and project specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

- `save()`: Save or update the entity into the backend.
- `export()`: Export the entity locally as yaml file.
- `refresh()`: Refresh (read) the entity from the backend.

::: digitalhub.entities.project._base.entity.Project.save
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.project._base.entity.Project.export
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.project._base.entity.Project.refresh
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Entity CRUD

The project acts as context for other entities as mentioned in the introduction. With a `Project` object, you can create, read, update and delete these entities. The methods exposed are basically the same as the standalone CRUD functions; the only difference is that on the project object you omit the project name parameter. The available methods are:

- **`new`**: create a new entity
- **`log`**: create and upload an entity
- **`get`**: get an entity from backend
- **`get_versions`**: get all version for a named entity
- **`list`**: list entities related to the project
- **`import`**: import an entity
- **`update`**: update an entity
- **`delete`**: delete an entity

For more information about the entity methods, see the related entity documentation:

- [**`artifacts`**](../artifact/crud.md)
- [**`dataitems`**](../dataitem/crud.md)
- [**`models`**](../model/crud.md)
- [**`functions`**](../function/crud.md)
- [**`workflows`**](../workflow/crud.md)
- [**`runs`**](../run/crud.md)
- [**`secrets`**](../secret/crud.md)

## Project specific methods

The project object exposes the following methods:

- **`run`**: execute a workflow from the project
- **`search_entity`**: search entities related to the project
- **`share`**: share the project with a user
- **`unshare`**: remove project access for a user

::: digitalhub.entities.project._base.entity.Project.run
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.project._base.entity.Project.search_entity
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.project._base.entity.Project.share
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.project._base.entity.Project.unshare
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
