# CRUD

The CRUD methods are used to create, read, update and delete secrets. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage secrets from the project, you can use the `Project` object and avoid to specify the `project` parameter. In this last case, you need to specify every parameter as keyword argument.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# Use CRUD method on project

secret = project.new_secret(name="my-secret",
                            secret_value="some-value")

# Use CRUD method from SDK

secret = dh.new_secret(project="my-project",
                       name="my-secret",
                       secret_value="some-value")
```

A `secret` entity can be managed with the following methods.

Create:

- [**`new_secret`**](#new)

Read:

- [**`get_secret`**](#get)
- [**`get_secret_versions`**](#get-versions)
- [**`import_secret`**](#import)
- [**`list_secrets`**](#list)

Update:

- [**`update_secret`**](#update)

Delete:

- [**`delete_secret`**](#delete)

## Create

You can create a secret with the `new_secret()`.

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
            - new_secret

## Read

To read secrets you can use the `get_secret()`, `get_secret_versions()`, `list_secrets()` or `import_secret()` functions.

### Get

This function searches for a single secret into the backend.
If you want to collect a secret from the backend using `get_secret()`, you have two options:

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
            - get_secret

### Get versions

This function returns all the versions of a secret from the backend.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_secret_versions

### List

This function returns all the latest secrets from the backend related to a project.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_secrets

### Import

This function load the secret from a local yaml file descriptor.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_secret

## Update

To update a secret you can use the `update_secret()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_secret

## Delete

To delete a secret you can use the `delete_secret()` method.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_secret
