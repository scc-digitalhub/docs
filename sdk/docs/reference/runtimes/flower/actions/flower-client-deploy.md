# Flower Client Deploy

## Deploy reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the deploy action does.

- [**Function**](#function){ .list-card-link } - Create a Flower client Function.

- [**Task**](#task){ .list-card-link } - Configure the Flower client deploy Task.

- [**Run**](#run){ .list-card-link } - Deploy the Flower client.

</div>

## Overview

The `deploy` action deploys a built Flower client container to participate in federated learning tasks. This action creates and manages the Flower client that communicates with the Flower server.

The runtime deploys the Flower client container image to a Kubernetes cluster or remote execution environment.
The deployed client will automatically join the federated learning federation and participate in training rounds as orchestrated by the Flower server.
If no image is configured, `auto_build=True` builds the image before deployment.

## Function

??? example "Create a function"

    Define the Function with the built Flower client image.

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
        | image | str | Docker image name of the built Flower client container. If omitted, `auto_build=True` builds it before deployment. |
        | base_image | str | Base Docker image used if an automatic build is triggered. |
        | requirements | list[str] \| str | Python package requirements or a supported requirements file path; used if an automatic build is triggered. |

        #### Requirements

        `requirements` accepts a list of requirement strings or a path to a supported requirements file. The SDK parses the requirements when the function is saved. For an unversioned package found in the local environment, it adds the installed version and logs a warning; use an explicit version or constraint to avoid this inference.

    === "Creation example"

        ```python
        import digitalhub as dh

        f = dh.new_function(
            name="my-flower-client",
            kind="flower-client",
            image="my-registry/my-flower-client:latest",
        )
        ```

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
        | action | str | Task action. **Required. MUST BE `deploy`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes for the deployment. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests for the deployment. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables for the deployment. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names for the deployment. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template for the deployment. |

    === "Creation example"

        ```python
        run = f.run(action="deploy")
        ```

### Task methods

The Flower client deploy Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | superlink | str | Flower superlink service endpoint for coordination. |
        | node_config | dict | Node configuration parameters for the Flower client. |
        | root_certificates | str | Content of the root certificate as string. |
        | private_key_secret | str | Name of the [secret](../../../objects/secret/entity.md) containing the private key for secure communication. |
        | public_key_secret | str | Name of the [secret](../../../objects/secret/entity.md) containing the public key for secure communication. |
        | isolation | str | Isolation mode: `process` or `subprocess`. |
        | auto_build | bool | Whether to build the function automatically when no image is configured. Defaults to `True`. |

    === "Creation example"

        ```python
        run = f.run(
            action="deploy",
            auto_build=True,
        )
        ```

### Run methods

There are no additional runtime-specific methods for this action.
