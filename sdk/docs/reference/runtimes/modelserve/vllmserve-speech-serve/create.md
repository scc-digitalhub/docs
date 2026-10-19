---
render_macros: true
---

# Create a vLLM Speech Function

Define the Function with the speech model source URL.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `vllmserve-speech`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| model_name | str | Name of the model. |
| image | str | Docker image used to serve the model. |
| url | str | Model source URL. |
| [adapters](#adapters) | list[dict] | List of model adapters. |

## Adapters

Adapters are a list of dictionaries with `name` and `url` keys:

```python
adapters = [{"name": "adapter-name", "url": "adapter-url"}]
```

## Example

```python
function = dh.new_function(
    name="my-vllm-speech-service",
    kind="vllmserve-speech",
    url="s3://my-bucket/path-to-model"
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
