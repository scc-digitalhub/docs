# Flower Server Deploy

The `deploy` action deploys a built Flower server container to orchestrate federated learning tasks. This action creates and manages the Flower server that coordinates clients.

## Overview

The runtime deploys the Flower server container image to a Kubernetes cluster or remote execution environment.
The deployed server will coordinate federated learning rounds and manage client communications.

## Quick example with bare minimum parameters

```python
import digitalhub as dh

# Create Flower server function
f = dh.new_function(
    name="my-flower-server",
    kind="flower-server",
    image="my-registry/my-flower-server:latest",
)

# Deploy the server
run = f.run(action="deploy")
```

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
| image | str | Docker image name of the built Flower server container. **Required for deploy.** |
| base_image | str | Base Docker image used for building (informational only for deploy). |
| requirements | list[str] | Python package requirements (informational only for deploy). |

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. MUST BE `deploy`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes for the deployment. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests for the deployment. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables for the deployment. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names for the deployment. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template for the deployment. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| auth_public_keys | list[str] | List of public keys for client authentication. |
| insecure | bool | Disable TLS verification (default False). |

## Entity methods

### Run methods

There are no additional run methods for this action.
