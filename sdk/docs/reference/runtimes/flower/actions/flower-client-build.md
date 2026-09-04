# Flower Client Build

## Build reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the build action does.

- [**Function**](#function){ .list-card-link } - Create a Flower client Function.

- [**Task**](#task){ .list-card-link } - Configure the Flower client build Task.

- [**Run**](#run){ .list-card-link } - Execute the Flower client build.

</div>

## Overview

The `build` action creates a container image for a Flower client that can participate in federated learning. This action packages the client code along with its dependencies into a deployable container image.

The runtime builds a Docker container image containing the Flower client code.
The resulting container image can be deployed to participate in federated learning tasks. See how to [deploy the client](flower-client-deploy.md).

## Function

??? example "Create a function"

    Define the Function with the Flower client image and build settings.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. **Required. MUST BE `flower-client`** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | image | str | Custom Docker image name for the built container. |
        | base_image | str | Base Docker image to use for building. |
        | requirements | list[str] \| str | Additional Python package requirements or a supported requirements file path. |

        #### Requirements

        `requirements` accepts a list of requirement strings or a path to a supported requirements file. The SDK parses the requirements when the function is saved. For an unversioned package found in the local environment, it adds the installed version and logs a warning; use an explicit version or constraint to avoid this inference.

    === "Creation example"

        ```python
        import digitalhub as dh

        f = dh.new_function(
            name="my-flower-client",
            kind="flower-client",
            base_image="some-base-image"
        )
        ```

        You can also call `f.build()` to create a client build run directly.

### Function methods

??? example "build"

    Build the Flower client function using the build action.

    ::: digitalhub_runtime_flower.entities.function._base.entity.FunctionFlowerBuild.build
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
        | action | str | Task action. **Required. MUST BE `build`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes for build execution. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests for build execution. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables for build execution. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names for build execution. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template for build execution. |
        | instructions | list[str] | Custom build instructions to execute during container build. |

    === "Creation example"

        ```python
        run = f.run(action="build", instructions=["... bash instructions ..."])
        ```

### Task methods

The Flower client build Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | superlink | str | Flower superlink service endpoint. |
        | node_config | dict | Node configuration parameters for the Flower client. |
        | root_certificates | str | Content of the root certificate as string. |
        | private_key_secret | str | Name of the secret containing the private key for secure communication. |
        | public_key_secret | str | Name of the secret containing the public key for secure communication. |
        | isolation | str | Isolation mode: `process` or `subprocess`. |
        | auto_build | bool | Whether to build the function automatically when no image is configured. Defaults to `True`. |

    === "Creation example"

        ```python
        run = f.run(action="build", instructions=["... bash instructions ..."])
        ```

### Run methods

??? example "image"

    Get the image generated by the build run.

    ::: digitalhub_runtime_flower.entities.run.flower_client_build.entity.RunFlowerClientBuild.image
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
