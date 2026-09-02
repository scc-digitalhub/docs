# Flower Server Build

The `build` action creates a container image for a Flower server that orchestrates federated learning. This action packages the server code along with its dependencies into a deployable container image.

## Overview

The runtime builds a Docker container image containing the Flower server code.
The resulting container image can be deployed to orchestrate federated learning tasks. See how to [deploy the server](flower-server-deploy.md).

## Quick example with bare minimum parameters

```python
import digitalhub as dh

# Create Flower server function
f = dh.new_function(
    name="my-flower-server",
    kind="flower-server",
    base_image="some-base-image"
)

# Build the server
run = f.run(action="build", instructions=["... bash instructions ..."])
```

You can also call `f.build()` to create a server build run directly.

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. **Required. MUST BE `flower-server`** |
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
| auth_public_keys | list[str] | List of public keys for authentication. |
| insecure | bool | Disable TLS verification. |
| auto_build | bool | Whether to build the function automatically when no image is configured. Defaults to `True`. |

### Requirements

`requirements` accepts a list of requirement strings or a path to a supported requirements file. The SDK parses the requirements when the function is saved. For an unversioned package found in the local environment, it adds the installed version and logs a warning; use an explicit version or constraint to avoid this inference.

## Entity methods

### Run methods

Once the build run is complete, the generated image reference is available through the `run.image` property.
