# ServiceGraph Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a ServiceGraph Function.

- [**Task**](#task){ .list-card-link } - Configure the ServiceGraph serve Task.

- [**Run**](#run){ .list-card-link } - Deploy the ServiceGraph pipeline.

</div>

## Overview

The `serve` action deploys a pipeline as a service on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Function

??? example "Create a function"

    Define the Function with a ServiceGraph pipeline definition.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. Must be `servicegraph`. **Required.** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the YAML of the pipeline. |
        | [code](../../../configuration/code-sources.md#plain-text-source) | str | Pipeline code YAML provided as plain text. |
        | base64 | str | Pipeline definition encoded as base64. |
        | image | str | Docker image where to serve the model. |

        The pipeline code should be defined following the specification defined in the [ServiceGraph](https://github.com/scc-digitalhub/digitalhub-servicegraph) project.

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-servicegraph-service",
            kind="servicegraph",
            code_src="src/flow.yaml"
        )
        ```

### Function methods

The ServiceGraph Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`** |
        | service_ports | list[dict] | List of service ports. |
        | [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Service type. |
        | service_name | str | Service name. |
        | [replicas](../../../configuration/kubernetes.md#replicas) | int | Number of replicas. |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            service_ports=[{"port": 7777, "target_port": 7777}]
        )
        ```

### Task methods

The ServiceGraph serve Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | parameters | dict | Task parameters to customize the flow properties. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            parameters={"input.url": "http://videosource:1984"},
            service_ports=[{"port": 7777, "target_port": 7777}]
        )
        ```

### Run methods

The ServiceGraph serve Run does not add runtime-specific methods.
