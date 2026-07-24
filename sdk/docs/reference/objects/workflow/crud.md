# CRUD

The CRUD methods are used to create, read, update and delete workflows. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage workflows from the project, you can use the `Project` object and avoid to specify the `project` parameter. In this last case, you need to specify every parameter as keyword argument.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# Use CRUD method on project

workflow = project.new_workflow(name="my-workflow",
                                kind="hera",
                                code_src="pipeline.py",
                                handler="pipeline-handler")

# Use CRUD method from SDK

workflow = dh.new_workflow(project="my-project",
                           name="my-function",
                           kind="hera",
                           code_src="pipeline.py",
                           handler="pipeline-handler")
```

A `workflow` entity can be managed with the following methods.

Create:

- [**`new_workflow`**](#new)

Read:

- [**`get_workflow`**](#get)
- [**`get_workflow_versions`**](#get-versions)
- [**`import_workflow`**](#import)
- [**`list_workflows`**](#list)

Update:

- [**`update_workflow`**](#update)

Delete:

- [**`delete_workflow`**](#delete)

## Create

You can create a workflow with the `new_workflow()`.
The `kwargs` parameters are determined by the **kind** of the object, and are described in the [kinds section](kinds.md).

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
            - new_workflow

## Read

To read workflows you can use the `get_workflow()`, `get_workflow_versions()`, `list_workflows()` or `import_workflow()` workflows.

### Get

This function searches for a single workflow into the backend.
If you want to collect a workflow from the backend using `get_workflow()`, you have two options:

- The first one is to use the `key` parameter which has the pattern `store://<project-name>/<entity-type>/<entity-kind>/<entity-name>:<entity-id>`.
- The second one is to use the entity name as `identifier`, the project name as `project` and the entity id as `entity_id` parameters. If you do not specify the entity id, you will get the latest version.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_workflow

### Get versions

This function returns all the versions of a workflow from the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_workflow_versions

### List

This function returns all the latest workflows from the backend related to a project.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_workflows

### Import

This function load the workflow from a local yaml file descriptor.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_workflow

## Update

To update a workflow you can use the `update_workflow()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_workflow

## Delete

To delete a workflow you can use the `delete_workflow()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_workflow
