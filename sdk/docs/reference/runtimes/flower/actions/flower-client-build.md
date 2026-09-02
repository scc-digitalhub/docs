# Flower Client Build

The `build` action creates a container image for a Flower client that can participate in federated learning. This action packages the client code along with its dependencies into a deployable container image.

## Overview

The runtime builds a Docker container image containing the Flower client code.
The resulting container image can be deployed to participate in federated learning tasks. See how to [deploy the client](flower-client-deploy.md).

## Quick example with bare minimum parameters

```python
import digitalhub as dh

# Create Flower client function
f = dh.new_function(
    name="my-flower-client",
    kind="flower-client",
    base_image="some-base-image"
)

# Build the client
run = f.run(action="build", instructions=["... bash instructions ..."])
```

You can also call `f.build()` to create a client build run directly.

## Parameters

### Function Parameters

Must be specified when creating the function.

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

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. MUST BE `build`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes for build execution. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests for build execution. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[dict] | Environment variables for build execution. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[str] | List of secret names for build execution. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template for build execution. |
| instructions | list[str] | Custom build instructions to execute during container build. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| superlink | str | Flower superlink service endpoint. |
| node_config | dict | Node configuration parameters for the Flower client. |
| root_certificates | str | Content of the root certificate as string. |
| private_key_secret | str | Name of the secret containing the private key for secure communication. |
| public_key_secret | str | Name of the secret containing the public key for secure communication. |
| isolation | str | Isolation mode: `process` or `subprocess`. |
| auto_build | bool | Whether to build the function automatically when no image is configured. Defaults to `True`. |

### Requirements

`requirements` accepts a list of requirement strings or a path to a supported requirements file. The SDK parses the requirements when the function is saved. For an unversioned package found in the local environment, it adds the installed version and logs a warning; use an explicit version or constraint to avoid this inference.

## Entity methods

### Run methods

Once the build run is complete, the generated image reference is available through the `run.image` property.
