# CRUD

The CRUD methods are used to create, read, update and delete projects.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")
```

A `project` entity can be managed with the following methods.

Create:

- [**`new_project`**](#new)

Read:

- [**`get_project`**](#get)
- [**`import_project`**](#import)
- [**`load_project`**](#load)

Read or create:

- [**`get_or_create_project`**](#read-or-create)

Update:

- [**`update_project`**](#update)

Delete:

- [**`delete_project`**](#delete)

For project configuration options, please refer to the [Config](config.md) section, and the [Setup](setup.md) section.

## Create

You can create a project with the `new_project()` method.

### New

This function create a new entity and saves it into the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - new_project

## Read

To read projects you can use the `get_project()`, `import_project()` or `load_project()`.

### Get

This function searches for a single project into the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_project

### Import

This function load the project from a local yaml file descriptor.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_project

### Load

This function loads the project from a local YAML file and updates the existing object into the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - load_project

## Read or create

You can read or create a project with the `get_or_create_project()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_or_create_project

## Update

To update a project you can use the `update_project()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_project

## Delete

To delete a project you can use the `delete_project()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_project
