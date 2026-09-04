# Hugging Face

The `huggingface` kind stores a Hugging Face model or repository in an addressable repository.

## Hugging Face spec

The `huggingface` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths.md#scheme-specific-paths) | *str* | Path of the model, either on the local filesystem or in remote storage. | *required* |
| `framework` | *str \| None* | Model framework, for example `pytorch`. | `None` |
| `algorithm` | *str \| None* | Model algorithm, for example `resnet`. | `None` |
| `parameters` | *dict \| None* | Model parameters. | `None` |
| `base_model` | *str \| None* | Base model. | `None` |
| `model_id` | *str \| None* | Hugging Face model ID. If omitted, the model is loaded from the model path. | `None` |
| `model_revision` | *str \| None* | Hugging Face model revision. | `None` |

## Hugging Face methods

The `huggingface` kind has no additional methods.
