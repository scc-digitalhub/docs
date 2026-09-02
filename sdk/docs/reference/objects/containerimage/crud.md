# CRUD

The CRUD methods create, read, update and delete container images. They can be called directly from the SDK or through a `Project` object.

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

image = project.new_containerimage(
    name="my-image",
    image="registry.example.com/my-image:latest",
)
```

A `containerimage` entity can be managed with the following methods.

Create:

- [**`new_containerimage`**](#new)

Read:

- [**`get_containerimage`**](#get)
- [**`get_containerimage_versions`**](#get-versions)
- [**`import_containerimage`**](#import)
- [**`load_containerimage`**](#load)
- [**`list_containerimages`**](#list)

Update:

- [**`update_containerimage`**](#update)

Delete:

- [**`delete_containerimage`**](#delete)

## Create

### New

Create and save a container image reference. The `image` value is the URI or registry reference of the existing image.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - new_containerimage

## Read

### Get

Get a container image by its storage key or name and project.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_containerimage

### Get versions

Return all versions of a named container image.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - get_containerimage_versions

### List

List the latest container images in a project. Use `versions` to request a different version selection.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - list_containerimages

### Import

Import a container image from a local YAML descriptor or a storage key.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - import_containerimage

### Load

Load a container image from a local YAML descriptor and update the existing backend object.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - load_containerimage

## Update

Update a container image entity.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - update_containerimage

## Delete

Delete a container image. Set `delete_all_versions=True` when deleting all versions by name.

::: digitalhub.entities
    options:
        heading_level: 6
        show_signature: false
        show_docstring_description: false
        show_symbol_type_heading: true
        show_source: false
        members:
            - delete_containerimage
