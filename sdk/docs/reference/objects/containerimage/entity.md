# Container images

A `Containerimage` represents an existing container image reference in a project. It stores the image URI and backend metadata such as its digest, media type, size, tags and manifest information.

Container images are versioned context entities and can be managed directly with the SDK CRUD methods or through a `Project` object.

## Choose a container image kind

Choose the kind that matches the container image you want to create. The `kind` to use is shown at the end of the card description.

<div class="list-cards" markdown>

- [**Container image**](./kind/container-image.md){ .list-card-link } - Store a container image reference with image metadata - `container-image`

</div>

## Container image operations

<div class="grid cards" markdown>

- [**Container image CRUD**](./crud.md){ .card-link }

	---

	Create, read, update, or delete container images.

- [**Use the Containerimage entity**](./methods.md){ .card-link }

	---

	Save, export, and refresh container image entities.

</div>

[Back to Entities](../index.md)
