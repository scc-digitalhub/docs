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

The project also exposes the following entity-specific operations:

- **Artifacts**: `new_artifact`, `log_artifact`, `register_artifact`, `get_artifact`, `list_artifacts`, `import_artifact`, `load_artifact`, `update_artifact`, `delete_artifact`.
- **Dataitems**: `new_dataitem`, `log_dataitem`, `log_table`, `log_croissant`, `register_dataitem`, `register_table`, `register_croissant`, `get_dataitem`, `list_dataitems`, `import_dataitem`, `load_dataitem`, `update_dataitem`, `delete_dataitem`.
- **Models**: `new_model`, `log_model`, `log_mlflow`, `log_sklearn`, `log_huggingface`, `log_tvm_ir`, `log_tvm_so`, the matching `register_*` methods, `get_model`, `list_models`, `import_model`, `load_model`, `update_model`, `delete_model`.
- **Functions and workflows**: `new`, `get`, `get_versions`, `list`, `import`, `load`, `update`, `delete`.
- **Tasks**: `new_task`, `get_task`, `list_tasks`, `import_task`, `load_task`, `update_task`, `delete_task`.
- **Runs**: `new_run`, `get_run`, `list_runs`, `import_run`, `load_run`, `update_run`, `delete_run`.
- **Triggers**: `new_trigger`, `get_trigger`, `list_triggers`, `import_trigger`, `load_trigger`, `update_trigger`, `delete_trigger`.
- **Secrets**: `new_secret`, `get_secret`, `list_secrets`, `import_secret`, `load_secret`, `update_secret`, `delete_secret`.
- **Container images**: `new_containerimage`, `get_containerimage`, `get_containerimage_versions`, `list_containerimages`, `import_containerimage`, `update_containerimage`, `delete_containerimage`.

For more information about the entity methods, see the related entity documentation:

- [**`artifacts`**](../artifact/crud.md)
- [**`dataitems`**](../dataitem/crud.md)
- [**`models`**](../model/crud.md)
- [**`functions`**](../function/crud.md)
- [**`workflows`**](../workflow/crud.md)
- [**`runs`**](../run/crud.md)
- [**`secrets`**](../secret/crud.md)
- [**`tasks`**](../task/crud.md)
- [**`triggers`**](../trigger/crud.md)
- [**`container images`**](../containerimage/crud.md)

## Extensions

An extension is a dictionary interpreted by the backend or runtime integration.
Pass `extensions` when creating a project or a supported material entity to
persist extension metadata. `Function.run()` and `Workflow.run()` also accept
`extensions` to attach extension data to the created run.

```python
project = dh.new_project(
    "my-project",
    extensions=[{"name": "my-extension", "config": {"enabled": True}}],
)

artifact = project.register_artifact(
    source="s3://bucket/path/file.csv",
    extensions=[{"name": "catalog", "config": {"owner": "team-a"}}],
)
```

The available extension names and configuration fields are defined by the
installed backend and runtime integrations.

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
