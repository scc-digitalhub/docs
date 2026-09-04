# Container Build

## Build reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the build action does.

- [**Function**](#function){ .list-card-link } - Create a container Function.

- [**Task**](#task){ .list-card-link } - Configure the container build Task.

- [**Run**](#run){ .list-card-link } - Execute the container build.

</div>

## Overview

The build action generates a Dockerfile with your custom instructions and builds a container image.

## Function

??? example "Create a function"

    Define the Function with the container image and build settings.

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
            name="my-build",
            kind="container",
            base_image="python:3.9"
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
        | action | str | Task action. **Required. Must be `build`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. Example: `{"cpu": "1", "mem": "512Mi"}`. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [instructions](#instructions) | list[str] | Build instructions executed as RUN lines in the generated Dockerfile. |
        | base_image | str | Optional override for the base image used by this build run. |
        | image | str | Optional target image name:tag to build/push. |

        #### Instructions

        Instructions are executed as `RUN` instructions in the generated Dockerfile. Example:

        ```python
        instructions = ["apt-get install -y git"]
        ```

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            instructions=["pip install numpy", "pip install pandas"]
        )
        ```

### Task methods

The container build Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | args | list[str] | Command-line arguments to pass to the container command. |

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            args=["--help"]
        )
        ```

### Run methods

The container run does not add runtime-specific methods.
