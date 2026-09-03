# MLflow

The `mlflow` kind stores an MLflow model together with its flavor, configuration, input datasets, and signature metadata.

## MLflow spec

The `mlflow` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, either on the local filesystem or in remote storage. | *required* |
| `framework` | *str \| None* | Model framework, for example `pytorch`. | `None` |
| `algorithm` | *str \| None* | Model algorithm, for example `resnet`. | `None` |
| `parameters` | *dict \| None* | Model parameters. | `None` |
| `flavor` | *str \| None* | MLflow model flavor. | `None` |
| `model_config` | *dict \| None* | MLflow model configuration. | `None` |
| `input_datasets` | *list[Dataset] \| None* | Datasets used as model inputs. | `None` |
| `signature` | *Signature \| None* | MLflow model signature. | `None` |

### Dataset

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | *str \| None* | Dataset name. | `None` |
| `digest` | *str \| None* | Dataset digest. | `None` |
| `profile` | *str \| None* | Dataset profile. | `None` |
| `dataset_schema` | *str \| None* | Dataset schema. | `None` |
| `source` | *str \| None* | Dataset source. | `None` |
| `source_type` | *str \| None* | Dataset source type. | `None` |

### Signature

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `inputs` | *str \| None* | Signature inputs. | `None` |
| `outputs` | *str \| None* | Signature outputs. | `None` |
| `params` | *str \| None* | Signature parameters. | `None` |

## MLflow methods

The `mlflow` kind has no additional methods.
