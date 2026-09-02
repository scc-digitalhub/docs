# CRUD

The CRUD methods create, read, update and delete tasks. Tasks are unversioned and belong to a project.

Example:

```python
import digitalhub as dh

# Create a task directly for an executable

task = dh.new_task(
    project="my-project",
    kind="python+job",
    function="python://my-project/my-function:latest",
)
```

A `task` entity can be managed with the following methods.

Create:

- [**`new_task`**](#new)

Read:

- [**`get_task`**](#get)
- [**`import_task`**](#import)
- [**`load_task`**](#load)
- [**`list_tasks`**](#list)

Update:

- [**`update_task`**](#update)

Delete:

- [**`delete_task`**](#delete)

## Create

### New

This function creates a task and saves it into the backend. The task `kind` combines an executable kind and an action, for example `python+job`.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - new_task

## Read

### Get

Get a task by its storage key or ID. When using an ID, provide the project name.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_task

### List

List tasks in a project. Use `function` or `workflow` filters to restrict the results to an executable.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_tasks

### Import

Import a task from a local YAML descriptor or a storage key.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_task

### Load

Load a task from a local YAML descriptor and update the existing backend object.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - load_task

## Update

Update a task. Its specification is immutable where required by the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_task

## Delete

Delete a task from the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_task
