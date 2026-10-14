---
render_macros: true
---

# Container image

The `container-image` kind represents an existing container image reference in a project. Its required `image` field is the image URI or registry reference. The backend may populate metadata such as the digest, media type, size, tags, and manifest information.

Creating a Containerimage entity records the reference; it does not build or push the image.

## Create

### New

{% call function_doc("new_containerimage", "digitalhub.entities") %}
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
{% endcall %}

## Methods

The `container-image` kind adds no instance methods. See [Use a container image](../use.md) for the common methods.

[Back to container image kind selection](../create.md)
