# Model kinds

At the moment, we support the following kinds:

- **`model`**: represents a generic ML model
- **`mlflow`**: represents a MLflow model
- **`sklearn`**: represents a scikit-learn model
- **`huggingface`**: represents a HuggingFace model

For each different kind, the `Model` object has its own subclass with different `spec` and `status` attributes.

## Model

The `model` kind indicates that the model is a generic ML model. It's usefull to represent a generic ML model as a `Model` object.

### Model spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, can be a local path or a remote path, a single filepath or a directory/partition. | *required* |
| `framework` | *str* | Model framework (e.g. 'pytorch'). | `None` |
| `algorithm` | *str* | Model algorithm (e.g. 'resnet'). | `None` |
| `base_model` | *str* | Base model. | `None` |
| `parameters` | *dict* | Model parameters. | `None` |
| `metrics` | *dict* | Model metrics. | `None` |

### Model methods

The `model` kind has no additional methods.

## Mlflow

The `mlflow` kind indicates that the model is an MLflow model. It's usefull to represent an MLflow model as a `Model` object.

### Mlflow spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, can be a local path or a remote path, a single filepath or a directory/partition. | *required* |
| `framework` | *str* | Model framework (e.g. 'pytorch'). | `None` |
| `algorithm` | *str* | Model algorithm (e.g. 'resnet'). | `None` |
| `base_model` | *str* | Base model. | `None` |
| `parameters` | *dict* | Model parameters. | `None` |
| `metrics` | *dict* | Model metrics. | `None` |
| `flavor` | *str* | Mlflow model flavor. | `None` |
| `model_config` | *dict* | Mlflow model config. | `None` |
| `input_datasets` | *list[Dataset]* | Mlflow input datasets (see below). | `None` |
| `signature` | *Signature* | Mlflow model signature (see below). | `None` |

#### Dataset

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | *str* | Dataset name. | `None` |
| `digest` | *str* | Dataset digest. | `None` |
| `profile` | *str* | Dataset profile. | `None` |
| `schema` | *str* | Dataset schema. | `None` |
| `source` | *str* | Dataset source. | `None` |
| `source_type` | *str* | Dataset source type. | `None` |

#### Signature

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `inputs` | *str* | Signature inputs. | `None` |
| `outputs` | *str* | Signature outputs. | `None` |
| `parameters` | *str* | Signature parameters. | `None` |

### Mlflow methods

The `mlflow` kind has no additional methods.

## Sklearn

The `sklearn` kind indicates that the model is an Sklearn model. It's usefull to represent an Sklearn model as a `Model` object.

### Sklearn spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, can be a local path or a remote path, a single filepath or a directory/partition. | *required* |
| `framework` | *str* | Model framework (e.g. 'pytorch'). | `None` |
| `algorithm` | *str* | Model algorithm (e.g. 'resnet'). | `None` |
| `base_model` | *str* | Base model. | `None` |
| `parameters` | *dict* | Model parameters. | `None` |
| `metrics` | *dict* | Model metrics. | `None` |

### Sklearn methods

The `sklearn` kind has no additional methods.

## Huggingface

The `huggingface` kind indicates that the model is an Huggingface model. It's usefull to represent an Huggingface model as a `Model` object.

### Huggingface spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, can be a local path or a remote path, a single filepath or a directory/partition. | *required* |
| `framework` | *str* | Model framework (e.g. 'pytorch'). | `None` |
| `algorithm` | *str* | Model algorithm (e.g. 'resnet'). | `None` |
| `base_model` | *str* | Base model. | `None` |
| `parameters` | *dict* | Model parameters. | `None` |
| `metrics` | *dict* | Model metrics. | `None` |
| `model_id` | *str* | Huggingface model id. If not specified, the model is loaded from the model path | `None` |
| `model_revision` | *str* | Huggingface model revision. | `None` |

### Huggingface methods

The `huggingface` kind has no additional methods.
