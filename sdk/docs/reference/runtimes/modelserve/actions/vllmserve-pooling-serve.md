# ModelServe vllmserve-pooling Serve

The `serve` action deploys vLLM models with pooling support as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The vllmserve-pooling function kind uses the same parameters as `vllmserve`, with a pooling-based serving flow.

## Quick example

```python
function = dh.new_function(
    name="my-vllm-pooling-service",
    kind="vllmserve-pooling",
    url="hf://mistralai/Mistral-7B-v0.1",
)

run = function.run(
    action="serve",
    replicas=1,
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `vllmserve-pooling`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| model_name | str | Name of the model. |
| image | str | Docker image where to serve the model. |
| url | str | Model source URL. |
| [adapters](#adapters) | list[dict] | List of adapters. |

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

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `serve`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| [replicas](../../../configuration/kubernetes/overview.md#replicas) | int | Number of replicas. |
| [service_type](../../../configuration/kubernetes/overview.md#service-port-type) | str | Service type. |
| service_name | str | Service name. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| url | str | URL of the vLLM service. |
| args | list[str] | Extra arguments passed to the vLLM server. |
| enable_telemetry | bool | Enable or disable telemetry. |
| use_cpu_image | bool | Use a CPU image for serving. |
| storage_space | str | Storage space for model artifacts. |

## Entity methods

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

::: digitalhub_runtime_modelserve.entities.run.vllmserve_run.entity.RunVllmserveRun.invoke
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
