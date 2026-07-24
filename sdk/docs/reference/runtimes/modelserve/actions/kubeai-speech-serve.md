# ModelServe kubeai-speech Serve

The `serve` action deploys speech processing models via KubeAI as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The kubeai-speech function kind supports deploying speech processing models via KubeAI. It supports speech-to-text functionality and can work with different engines for speech processing.

## Quick example

```python
function = dh.new_function(
    name="my-kubeai-speech-service",
    kind="kubeai-speech",
    url="hf://openai/whisper-tiny",
    adapters=[{"name": "whisper-adapter", "url": "hf://adapter-url"}]
)

run = function.run(
    action="serve"
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `kubeai-speech`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| model_name | str | Name of the model. |
| image | str | Docker image where to serve the model. |
| [url](#model-url) | str | Model url. |
| [adapters](#adapters) | list[dict] | Adapters. |

#### Model URL

The model url must follow the pattern:

```python
regexp = (
    r"^(store://([^/]+)/model/huggingface/.*)"
    + r"|"
    + r"^pvc?://.*$"
    + r"|"
    + r"^s3?://.*$"
    + r"|"
    + r"^ollama?://.*$"
    + r"|"
    + r"^hf?://.*$"
)
```

#### Adapters

Adapters is a list of dictionaries with the following keys:

```python
adapters = [{
    "name": "adapter-name",
    "url": "adapter-url"
}]
```

### Task Parameters

Can only be specified when calling `function.run()`.

#### Shared Parameters

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `serve`** |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `function.run()`.

#### Run Function Kind-Specific Parameters

##### KubeAI Speech

| Name | Type | Description |
| --- | --- | --- |
| env | dict | Environment variables. |
| args | list[str] | Arguments. |
| cache_profile | str | Cache profile. |
| [files](#files) | list[KubeaiFile] | Files. |
| [scaling](#scaling) | Scaling | Scaling parameters. |
| processors | int | Number of processors. |

#### Files

Files is a list of dict with the following keys:

```python
files = [
    {
        "path": "file-path"
        "content": "file-content"
    }
]
```

#### Scaling

Scaling is a `Scaling` object that represents the scaling parameters for the run. Its structure is as follows:

```python
scaling = {
    "replicas": int,
    "min_replicas": int,
    "max_replicas": int,
    "autoscaling_disabled": bool,
    "target_request": int,
    "scale_down_delay_seconds": int,
    "load_balancing": {
        "strategy": str,  # "LeastLoad" or "PrefixHash"
        "prefix_hash": {
            "mean_load_factor": int,
            "replication": int,
            "prefix_char_length": int
        }
    }
}
```

## Entity methods

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

::: digitalhub_runtime_modelserve.entities.run.kubeaiservespeechtotext_run.entity.RunKubeaiserveSpeechtotextRun.invoke
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
