---
render_macros: true
---

# Create a KubeAI Speech Function

Define the Function with the KubeAI speech model URL and adapters.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `kubeai-speech`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| model_name | str | Name of the model. |
| image | str | Docker image used to serve the model. |
| [url](#model-url) | str | Model URL. |
| [adapters](#adapters) | list[dict] | Model adapters. |

## Model URL

The SDK stores the model URL as a string and does not validate its format locally. Provide a URL supported by KubeAI, such as an `hf://` source.

## Adapters

Adapters are a list of dictionaries with `name` and `url` keys:

```python
adapters = [{"name": "adapter-name", "url": "adapter-url"}]
```

## Example

```python
function = dh.new_function(
    name="my-kubeai-speech-service",
    kind="kubeai-speech",
    url="hf://openai/whisper-tiny",
    adapters=[{"name": "whisper-adapter", "url": "hf://adapter-url"}]
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
