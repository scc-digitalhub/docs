# Artifact

The `artifact` kind represents a generic artifact stored as a file in an artifact store. Use it when you need to upload, download, or register files without additional kind-specific behavior.

## Artifact spec

The `artifact` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths.md#entity-paths) | *str* | Target path to the artifact, either on the local filesystem or in remote storage. | *required* |
| `src_path` | *str \| None* | Source path of the artifact. | `None` |

## Artifact methods

The `artifact` kind has no additional methods.
