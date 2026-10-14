---
render_macros: true
---

# Create a container image

A `Containerimage` records a reference to an existing container image. Creating the entity does not build, push, or upload the image.

## Choose a creation method

Containerimage has no `log_<kind>()` or `register_<kind>()` functions.

- **Create with `new_containerimage()`** creates an entity for an existing image reference. Its example is in the Container image kind reference below.

## Choose a container image kind

The `container-image` kind stores the image URI or registry reference.

<div class="list-cards" markdown>

- [**Container image**](./kind/container-image.md){ .list-card-link } - Store an image reference and its backend metadata - `container-image`

</div>

[Back to Container images](./entity.md)
