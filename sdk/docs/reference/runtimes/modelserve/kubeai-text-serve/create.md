---
render_macros: true
---

# Create a KubeAI Text Function

Define the Function with the KubeAI text model URL, features and engine.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `kubeai-text`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| model_name | str | Name of the model. |
| image | str | Docker image used to serve the model. |
| [url](#model-url) | str | Model URL. |
| [adapters](#adapters) | list[dict] | Model adapters. |
| [features](#features) | list[str] | Supported model features. |
| [engine](#engine) | KubeaiEngine | Engine used to serve the model. |

## Adapters

Adapters are a list of dictionaries with `name` and `url` keys:

```python
adapters = [{"name": "adapter-name", "url": "adapter-url"}]
```

## Features

Supported feature values are `TextGeneration`, `TextEmbedding`, and `SpeechToText`.

## Engine

The engine is a `KubeaiEngine` object. Supported engines are `OLlama`, `VLLM`, `FasterWhisper`, and `Infinity`.

## Model URL

The SDK stores the model URL as a string and does not validate its format locally. Provide a URL supported by KubeAI, such as an `hf://` source.

## Example

```python
function = dh.new_function(
    name="my-kubeai-text-service",
    kind="kubeai-text",
    url="hf://microsoft/DialoGPT-medium",
    features=["TextGeneration"],
    engine="VLLM"
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
