# Scikit-learn

The `sklearn` kind stores a scikit-learn model in an addressable repository.

## Scikit-learn spec

The `sklearn` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths.md#entity-paths) | *str* | Path of the model, either on the local filesystem or in remote storage. | *required* |
| `framework` | *str \| None* | Model framework, for example `pytorch`. | `None` |
| `algorithm` | *str \| None* | Model algorithm, for example `resnet`. | `None` |
| `parameters` | *dict \| None* | Model parameters. | `None` |

## Scikit-learn methods

The `sklearn` kind has no additional methods.
