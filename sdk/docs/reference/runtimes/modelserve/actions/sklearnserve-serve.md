# ModelServe sklearnserve Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a scikit-learn serving Function.

- [**Task**](#task){ .list-card-link } - Configure the scikit-learn serving Task.

- [**Run**](#run){ .list-card-link } - Serve the scikit-learn model.

</div>

## Overview

The `serve` action deploys scikit-learn ML models as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

The sklearnserve function kind supports deploying scikit-learn models as REST API services. The model must be saved in pickle format (.pkl).

## Function

??? example "Create a function"

    Define the Function with the scikit-learn model path and serving image.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. Must be `sklearnserve`. **Required.** |
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

        The SDK stores the image as a string and does not validate its format locally. Provide an image compatible with the scikit-learn serving runtime.

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-sklearn-service",
            kind="sklearnserve",
            path=model.key
        )
        ```

### Function methods

The scikit-learn serving Function does not add runtime-specific methods.

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

The scikit-learn serving Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        No specific parameters for run of this action.

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            replicas=1
        )
        ```

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

??? example "invoke"

    Invoke the scikit-learn model serving run with input data.

    ::: digitalhub_runtime_modelserve.entities.run.sklearnserve_run.entity.RunSklearnserveRun.invoke
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
