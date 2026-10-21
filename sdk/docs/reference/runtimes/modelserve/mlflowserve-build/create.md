---
render_macros: true
---

# Create an MLflow Serving Function

Define the Function with the MLflow model path and serving image.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `mlflowserve`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether to embed the object in the project. |
| [path](#model-path) | str | | Model path. |
| model_name | str | | Name of the model. |
| [image](#model-image) | str | | Docker image used to serve the model. |

## Model path

The SDK stores the model path as a string and does not validate its format locally. Provide a model key, an S3 path partition, or a zip archive supported by the platform.

## Model image

The SDK stores the image as a string and does not validate its format locally. Provide an image compatible with the MLflow serving runtime.

## Example

```python
function = dh.new_function(
    name="my-mlflow-build-function",
    kind="mlflowserve",
    path=model.key
)
```

## Function methods

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
