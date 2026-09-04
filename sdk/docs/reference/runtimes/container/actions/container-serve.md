# Container Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a container Function.

- [**Task**](#task){ .list-card-link } - Configure the container service Task.

- [**Run**](#run){ .list-card-link } - Execute the container service.

</div>

## Overview

The serve action creates a Kubernetes service that runs continuously and can handle incoming requests.

## Function

??? example "Create a function"

    Define the Function with the container image.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. **Required. Must be `container`** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
        | [code](../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
        | base64 | str | Source code encoded as base64. |
        | [handler](../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
        | lang | str | Source code language (informational). |
        | image | str | Container image to use for execution (name:tag). |
        | base_image | str | Base image used when building the execution image. |
        | image_pull_policy | str | Kubernetes image pull policy: `Always`, `IfNotPresent` or `Never`. |
        | command | str | Command to run inside the container. |

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-service",
            kind="container",
            image="my-app:latest"
        )
        ```

### Function methods

??? example "build"

    Create and execute a build run for the function.

    ::: digitalhub_runtime_container.entities.function.container.entity.FunctionContainer.build
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. Example: `{"cpu": "1", "mem": "512Mi"}`. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [replicas](../../../configuration/kubernetes.md#replicas) | int | Number of replicas. Must be non-negative. |
        | [service_ports](../../../configuration/kubernetes.md#service-port-and-type) | list[dict] | Ports to expose for the service. Each port and target port must be an integer. Example: `[{"port": 80, "target_port": 8080}]`. |
        | [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Service type: `ClusterIP`, `LoadBalancer`, `NodePort` or `ExternalName`. |
        | service_name | str | Service name. |
        | [run_as_user](../../../configuration/kubernetes.md#security-context) | int | User ID to run the container. Must be non-negative. |
        | [run_as_group](../../../configuration/kubernetes.md#security-context) | int | Group ID to run the container. Must be non-negative. |
        | [fs_group](../../../configuration/kubernetes.md#security-context) | int | File system group ID. Must be positive. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            replicas=3,
            service_ports=[{"port": 80, "target_port": 8080}]
        )
        ```

### Task methods

The container serve Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | auto_build | bool | Whether to build the function automatically when no image is configured. Defaults to `True`. |
        | args | list[str] | Command-line arguments to pass to the container command. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            auto_build=True,
            args=["--help"]
        )
        ```

### Run methods

??? example "invoke"

    Invoke the service endpoint exposed by the run.

    ::: digitalhub_runtime_container.entities.run.serve.entity.RunContainerRunServe.invoke
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
