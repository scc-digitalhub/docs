# Container image

The `container-image` kind represents an existing container image reference in a project. The backend may populate image metadata such as its digest, media type, size, tags, and manifest information.

## Container image spec

The `container-image` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `image` | *str* | Image URI or registry reference. | *required* |

## Container image methods

The `container-image` kind has no additional methods.
