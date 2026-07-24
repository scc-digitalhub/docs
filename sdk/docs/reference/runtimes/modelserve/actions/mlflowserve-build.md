# ModelServe mlflowserve Build

The `build` action builds an MLflow model-serving container image. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The mlflowserve function kind supports building MLflow models for serving. The model must be saved in MLflow format with an MLmodel file.

## Quick example

```python
function = dh.new_function(
    name="my-mlflow-build-function",
    kind="mlflowserve",
    path=model.key
)

build_run = function.run(
    action="build",
    instructions=["pip install -r requirements.txt"]
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `mlflowserve`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [path](#model-path) | str | Model path. |
| model_name | str | Name of the model. |
| [image](#model-image) | str | Docker image where to serve the model. |

#### Model Path

The model path must consists of the model key or the s3 path partition where the model files are or a zip containing the model files.

#### Model Image

Model image must follow the pattern:

```python
image_regex = r"^seldonio\\/mlserver?:.*-mlflow$"
```

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `build`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| [replicas](../../../configuration/kubernetes/overview.md#replicas) | int | Number of replicas. |
| [service_type](../../../configuration/kubernetes/overview.md#service-port-type) | str | Service type. |
| service_name | str | Service name. |
| [instructions](#instructions) | list[str] | Build instructions executed as RUN lines in the generated Dockerfile. |

### Run Parameters

Can only be specified when calling `function.run()`.

No specific parameters for run of this action.

## Instructions

Instructions are executed as `RUN` instructions in the generated Dockerfile. Example:

```python
instructions = ["apt-get install -y git"]
```

## Entity methods

### Run methods

No runtime-specific helper methods are available for this action.
