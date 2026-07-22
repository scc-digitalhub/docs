# CRUD

The CRUD methods are used to create, read, update and delete extensions. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage extensions from the project, you can use the `Project` object and avoid to specify the `project` parameter. In this last case, you need to specify every parameter as keyword argument.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# Use CRUD method on project

extension = project.new_extension(name="my-extension",
                                  kind="extension",
                                  schema='{"name": "string", "kind": "custom", "spec": {}}')

# Use CRUD method from SDK

extension = dh.new_extension(project="my-project",
                             name="my-extension",
                             kind="extension",
                             schema='{"name": "string", "kind": "custom", "spec": {}}')
```

An `extension` entity can be managed with the following methods.

Create:

- [**`new_extension`**](#new)

Read:

- [**`get_extension`**](#get)
- [**`get_extension_versions`**](#get-versions)
- [**`import_extension`**](#import)
- [**`list_extensions`**](#list)

Update:

- [**`update_extension`**](#update)

Delete:

- [**`delete_extension`**](#delete)

## Create

You can create an extension with the `new_extension()` method.
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
            - new_extension

## Read

To read extensions you can use the `get_extension()`, `get_extension_versions()`, `list_extensions()` or `import_extension()` functions.

### Get

This function searches for a single extension into the backend.
If you want to collect an extension from the backend using `get_extension()`, you have two options:

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
            - get_extension

### Get versions

This function returns all the versions of an extension from the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_extension_versions

### List

This function returns all the latest extensions from the backend related to a project.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_extensions

### Import

This function load the extension from a local yaml file descriptor.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_extension

## Update

To update an extension you can use the `update_extension()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_extension

## Delete

To delete an extension you can use the `delete_extension()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_extension
