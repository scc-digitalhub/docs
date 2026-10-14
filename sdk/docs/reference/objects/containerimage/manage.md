---
render_macros: true
---

# Manage container images

The CRUD methods are used to read, update, and delete container images. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument. For image creation, see [Create a container image](./create.md).

## Read

Use the read methods to retrieve container images from the backend or load them from a YAML descriptor.

{% call function_doc("get_containerimage", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        image = dh.get_containerimage(
            identifier="my-image",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("get_containerimage_versions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        images = dh.get_containerimage_versions(
            identifier="my-image",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_containerimages", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        images = dh.list_containerimages(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_containerimage", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        image = dh.import_containerimage("my-image.yaml")
        ```
{% endcall %}

{% call function_doc("load_containerimage", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        image = dh.load_containerimage("my-image.yaml")
        ```
{% endcall %}

## Update

Update a container image after changing its mutable metadata.

{% call function_doc("update_containerimage", "digitalhub.entities") %}
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
{% endcall %}

## Delete

Delete one container image version or all versions of an image.

{% call function_doc("delete_containerimage", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_containerimage(
            identifier="my-image",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}
