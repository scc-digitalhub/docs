# CRUD

The CRUD methods create, read, update and delete container images. They can be called directly from the SDK or through a `Project` object.
The syntax is the same for all CRUD methods. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument.

## Create

`new_containerimage()` creates and saves a reference to an existing container image. The `image` value is the URI or registry reference. For specification parameters, see the [container-image kind](kind/container-image.md) reference.

??? example "new_containerimage"

    Create and save a container image reference.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_containerimage

    === "Creation example"

        ```python
        import digitalhub as dh

        image = dh.new_containerimage(
            project="my-project",
            name="my-image",
            kind="container-image",
            image="registry.example.com/my-image:latest",
        )
        ```

## Read

Use the read methods to retrieve container images from the backend or load them from a YAML descriptor.

??? example "get_containerimage"

    Get one container image by storage key or name and project. Omitting `entity_id` returns the latest version.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_containerimage

    === "Example"

        ```python
        import digitalhub as dh

        image = dh.get_containerimage(
            identifier="my-image",
            project="my-project",
        )
        ```

??? example "get_containerimage_versions"

    Get all versions of a container image by name and project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_containerimage_versions

    === "Example"

        ```python
        import digitalhub as dh

        images = dh.get_containerimage_versions(
            identifier="my-image",
            project="my-project",
        )
        ```

??? example "list_containerimages"

    List the latest container images in a project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_containerimages

    === "Example"

        ```python
        import digitalhub as dh

        images = dh.list_containerimages(project="my-project")
        ```

??? example "import_containerimage"

    Import a container image from a local YAML descriptor or a storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_containerimage

    === "Example"

        ```python
        import digitalhub as dh

        image = dh.import_containerimage("my-image.yaml")
        ```

??? example "load_containerimage"

    Load a container image from a local YAML descriptor and update the existing backend object.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - load_containerimage

    === "Example"

        ```python
        import digitalhub as dh

        image = dh.load_containerimage("my-image.yaml")
        ```

## Update

Update a container image after changing its mutable metadata.

??? example "update_containerimage"

    Update an existing container image entity.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_containerimage

    === "Example"

        ```python
        import digitalhub as dh

        image = dh.get_containerimage(
            identifier="my-image",
            project="my-project",
        )
        image.set_description("Updated image")
        image = dh.update_containerimage(image)
        ```

## Delete

Delete one container image version or all versions of an image.

??? example "delete_containerimage"

    Set `delete_all_versions=True` to delete all versions by entity name.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_containerimage

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_containerimage(
            identifier="my-image",
            project="my-project",
            delete_all_versions=True,
        )
        ```
