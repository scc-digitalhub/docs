# CRUD

The CRUD methods are used to create, read, update and delete dataitems. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage dataitems from the project, you can use the `Project` object and avoid to specify the `project` parameter. In this last case, you need to specify every parameter as keyword argument.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# Use CRUD method on project

dataitem = project.new_dataitem(name="my-dataitem",
                                kind="table",
                                path="path-to-some-data")

# Use CRUD method from SDK

dataitem = dh.new_dataitem(project="my-project",
                           name="my-dataitem",
                           kind="table",
                           path="path-to-some-data")
```

A `dataitem` entity can be managed with the following methods.

Create:

- [**`new_dataitem`**](#new)
- [**`log_dataitem`**](#log)
- [**`log_generic_dataitem`**](#log-generic)
- [**`log_table`**](#log-table)
- [**`log_croissant`**](#log-croissant)

Read:

- [**`get_dataitem`**](#get)
- [**`get_dataitem_versions`**](#get-versions)
- [**`import_dataitem`**](#import)
- [**`list_dataitems`**](#list)

Update:

- [**`update_dataitem`**](#update)

Delete:

- [**`delete_dataitem`**](#delete)

## Create

You can create a dataitem with the `new_dataitem()` or with `log_dataitem()` method. The main difference between the two methods is that `log_dataitem()` also uploads a local file into a dataitem store (eg. *S3*), while `new_dataitem()` only creates a new entity and saves it into the backend.
The `kwargs` parameters are determined by the **kind** of the object, and are described in the [kinds section](kinds.md).
The `kwargs` parameters are the same for both *new* and *log* methods.

### New

This function creates a new entity and saves it into the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - new_dataitem

### Log

This function creates a new entity in the backend and also uploads a local file into a dataitem store (eg. *S3*).

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - log_dataitem

### Log generic

This function creates a generic dataitem by uploading one or more local files.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - log_generic_dataitem

### Log table

This function logs a table dataitem from a dataframe or file source.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - log_table

### Log croissant

This function creates a Croissant dataitem by uploading a `metadata.json` file and its
referenced local files.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - log_croissant

## Read

To read dataitems you can use the `get_dataitem()`, `get_dataitem_versions()`, `list_dataitems()` or `import_dataitem()` functions.

### Get

This function searches for a single dataitem into the backend.
If you want to collect a dataitem from the backend using `get_dataitem()`, you have two options:

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
            - get_dataitem

### Get versions

This function returns all the versions of a dataitem from the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_dataitem_versions

### List

This function returns all the latest dataitems from the backend related to a project.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_dataitems

### Import

This function loads the dataitem from a local yaml file descriptor.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_dataitem

## Update

To update a dataitem you can use the `update_dataitem()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_dataitem

## Delete

To delete a dataitem you can use the `delete_dataitem()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_dataitem
