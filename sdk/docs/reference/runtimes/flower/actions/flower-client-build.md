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
| requirements | list[str] | Additional Python package requirements. |

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. MUST BE `build`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes for build execution. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests for build execution. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables for build execution. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names for build execution. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template for build execution. |
| instructions | list[str] | Custom build instructions to execute during container build. |

### Run Parameters

Can only be specified when calling `function.run()`.

No specific parameters for run of this action.

## Entity methods

### Run methods

There are no additional run methods for this action.
