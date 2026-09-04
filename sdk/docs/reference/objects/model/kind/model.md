# Model

The `model` kind stores a generic machine learning model in an addressable repository. Use it when the model does not require the metadata or behavior of a specialized kind.

## Model spec

The `model` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths.md#scheme-specific-paths) | *str* | Path of the model, either on the local filesystem or in remote storage. | *required* |
| `framework` | *str \| None* | Model framework, for example `pytorch`. | `None` |
| `algorithm` | *str \| None* | Model algorithm, for example `resnet`. | `None` |
| `parameters` | *dict \| None* | Model parameters. | `None` |

## Model methods

The `model` kind has no additional methods.
