# CRUD

The CRUD methods are used to create, read, update and delete functions. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage functions from the project, you can use the `Project` object and avoid to specify the `project` parameter. In this last case, you need to specify every parameter as keyword argument.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# Use CRUD method on project

function = project.new_function(name="my-function",
                                kind="python",
                                code_src="function.py",
                                handler="function-handler")

# Use CRUD method from SDK

function = dh.new_function(project="my-project",
                           name="my-function",
                           kind="python",
                           code_src="function.py",
                           handler="function-handler")
```

A `function` entity can be managed with the following methods.

Create:

- [**`new_function`**](#new)

Read:

- [**`get_function`**](#get)
- [**`get_function_versions`**](#get-versions)
- [**`import_function`**](#import)
- [**`list_functions`**](#list)

Update:

- [**`update_function`**](#update)

Delete:

- [**`delete_function`**](#delete)

## Create

You can create a function with the `new_function()`.
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
            - new_function

## Read

To read functions you can use the `get_function()`, `get_function_versions()`, `list_functions()` or `import_function()` functions.

### Get

This function searches for a single function into the backend.
If you want to collect a function from the backend using `get_function()`, you have two options:

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
            - get_function

### Get versions

This function returns all the versions of a function from the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_function_versions

### List

This function returns all the latest functions from the backend related to a project.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_functions

### Import

This function load the function from a local yaml file descriptor.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_function

## Update

To update a function you can use the `update_function()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_function

## Delete

To delete a function you can use the `delete_function()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_function
