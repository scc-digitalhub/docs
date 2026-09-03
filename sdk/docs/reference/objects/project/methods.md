# Project methods

The `Project` object is the working context for project state, related entities, and project-level operations. Choose an area below to find the relevant methods.

<div class="grid cards" markdown>

- [**Manage project state**](#manage-project-state){ .card-link }

    ---

    Persist the project, export it locally, or refresh it from the backend.

- [**Manage related entities**](#manage-related-entities){ .card-link }

    ---

    Create, retrieve, list, import, update, and delete entities in the project.

- [**Run project operations**](#run-project-operations){ .card-link }

    ---

    Manage project access, search entities, and run workflows.

</div>

## Manage project state

Use these methods to persist or synchronize a `Project` object.

??? example "save"

    Save or update the project in the backend.

    ::: digitalhub.entities.project._base.entity.Project.save
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

    Export the project locally as a YAML file.

    ::: digitalhub.entities.project._base.entity.Project.export
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

    Refresh the project from the backend.

    ::: digitalhub.entities.project._base.entity.Project.refresh
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Manage related entities

The `Project` object exposes the CRUD methods for the entities it contains. The project name is inferred from the object. See [Entities](../index.md) for the available entity types and their documentation.

## Run project operations

Use these methods to execute workflows, search project entities, and manage access:

??? example "share"

    Share the project with a user.

    ::: digitalhub.entities.project._base.entity.Project.share
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "unshare"

    Remove project access for a user.

    ::: digitalhub.entities.project._base.entity.Project.unshare
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "search_entity"

    Search entities related to the project.

    ::: digitalhub.entities.project._base.entity.Project.search_entity
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "run"

    Execute a workflow from the project.

    ::: digitalhub.entities.project._base.entity.Project.run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

[Back to Project](./entity.md)
