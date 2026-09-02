# ModelServe mlflowserve Serve

The `serve` action deploys MLflow ML models as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The mlflowserve function kind supports deploying MLflow models as REST API services. The model must be saved in MLflow format with an MLmodel file.

## Quick example

```python
function = dh.new_function(
    name="my-mlflow-service",
    kind="mlflowserve",
    path=model.key
)

run = function.run(
    action="serve",
    replicas=1
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

The SDK stores the model path as a string and does not validate its format locally. Provide a model key, an S3 path partition, or a zip archive supported by the platform.

#### Model Image

The SDK stores the image as a string and does not validate its format locally. Provide an image compatible with the MLflow serving runtime.

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `serve`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| [replicas](../../../configuration/kubernetes/overview.md#replicas) | int | Number of replicas. |
| [service_type](../../../configuration/kubernetes/overview.md#service-port-and-type) | str | Service type. |
| service_name | str | Service name. |

### Run Parameters

Can only be specified when calling `function.run()`.

No specific parameters for run of this action.

## Entity methods

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

::: digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.entity.RunMlflowserveServeRun.invoke
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
