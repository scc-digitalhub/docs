# ModelServe vllmserve-pooling Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a vLLM pooling Function.

- [**Task**](#task){ .list-card-link } - Configure the vLLM pooling Task.

- [**Run**](#run){ .list-card-link } - Serve the vLLM pooling model.

</div>

## Overview

The `serve` action deploys vLLM pooling models as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

The vllmserve-pooling function kind supports serving pooling models with vLLM. Pooling models can be used for tasks such as embedding and reranking.

## Function

??? example "Create a function"

    Define the Function with the model path and serving image.

    === "Parameters"

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
        | [adapters](#adapters) | list[dict] | Adapters. |

        #### Adapters

        Adapters is a list of dictionaries with the following keys:

        ```python
        adapters = [{
            "name": "adapter-name",
            "url": "adapter-url"
        }]
        ```

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-vllm-pooling-service",
            kind="vllmserve-pooling",
            url="s3://my-bucket/path-to-model"
        )
        ```

### Function methods

The vLLM pooling Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [replicas](../../../configuration/kubernetes.md#replicas) | int | Number of replicas. |
        | [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Service type. |
        | service_name | str | Service name. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            replicas=1
        )
        ```

### Task methods

The vLLM pooling Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | url | str | URL of the vLLM service. |
        | args | list[str] | Arguments for the vLLM server. |
        | enable_telemetry | bool | Enable or disable telemetry. |
        | use_cpu_image | bool | Use a CPU image for serving. |
        | storage_space | str | Storage space for model artifacts. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            args=["--pooling", "last"]
        )
        ```

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

??? example "invoke"

    Invoke the vLLM pooling model serving run with input data.

    ::: digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.entity.RunVllmservepoolingRun.invoke
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "list_endpoints"

    List all available endpoints for the served model.

    ::: digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.entity.RunVllmservepoolingRun.list_endpoints
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
