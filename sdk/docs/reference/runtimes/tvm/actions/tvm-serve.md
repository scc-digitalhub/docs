# TVM Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Deploy a compiled TVM model as a service.

- [**Function**](#function){ .list-card-link } - Use a TVM Function as the model source.

- [**Task**](#task){ .list-card-link } - Configure the TVM serve Task.

- [**Run**](#run){ .list-card-link } - Deploy the TVM service.

</div>

## Overview

The `serve` action deploys a compiled TVM `model.so` as a service on Kubernetes. Set `model_path` to the compiled artifact and optionally configure the service name, replicas, workers, and service type.

## Function

??? example "Create a function"

    The serve action uses the same `tvm` Function specification as the [build action](tvm-build.md#function).

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-tvm-model",
            kind="tvm",
            model="s3://my-bucket/models/model.onnx",
            format="onnx",
        )
        ```

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`.** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | model_path | str | Compiled `model.so` path or store key. |
        | served_name | str | Name used by the served model. |
        | image | str | TVM execution image. |
        | replicas | int | Number of service replicas. |
        | workers | int | Number of workers per replica. |
        | [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Kubernetes service type. |
        | service_name | str | Kubernetes service name. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            model_path="store://my-project/model/model-so:version",
            served_name="my-model",
            replicas=1,
        )
        ```

### Task methods

The TVM serve Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | model | str | Source model path or store key. **Required.** |
        | format | str | Source model format: `auto`, `onnx`, or `tflite`. |
        | ir_model | str | Store key of the Relax IR model. |
        | so_model | str | Store key of the compiled `model.so`. |
        | model_path | str | Compiled `model.so` path or store key. |
        | served_name | str | Name used by the served model. |
        | image | str | TVM execution image. |
        | replicas | int | Number of service replicas. |
        | workers | int | Number of workers per replica. |
        | [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Kubernetes service type. |
        | service_name | str | Kubernetes service name. |
        | local_execution | bool | Execute the run locally instead of remotely. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            model_path="store://my-project/model/model-so:version",
            served_name="my-model",
            replicas=1,
            wait=True,
        )
        ```

### Run methods

Once the run is created, inspect `run.status` and wait for the service to become ready before invoking it.

??? example "Wait for readiness"

    ```python
    run.refresh()
    run.status
    ```
