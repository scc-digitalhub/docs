# Flower Client Deploy

The `deploy` action deploys a built Flower client container to participate in federated learning tasks. This action creates and manages the Flower client that communicates with the Flower server.

## Overview

The runtime deploys the Flower client container image to a Kubernetes cluster or remote execution environment.
The deployed client will automatically join the federated learning federation and participate in training rounds as orchestrated by the Flower server.

## Quick example with bare minimum parameters

```python
import digitalhub as dh

# Create Flower client function
f = dh.new_function(
    name="my-flower-client",
    kind="flower-client",
    image="my-registry/my-flower-client:latest",
)

# Deploy the client
run = f.run(action="deploy")
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
| image | str | Docker image name of the built Flower client container. **Required for deploy.** |
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
| superlink | str | Flower superlink service endpoint for coordination. |
| node_config | dict | Node configuration parameters for the Flower client. |
| root_certificates | str | Content of the root certificate as string. |
| private_key_secret | str | Name of the [secret](../../../objects/secret/entity.md) containing the private key for secure communication. |
| public_key_secret | str | Name of the [secret](../../../objects/secret/entity.md) containing the public key for secure communication. |
| isolation | str | Isolation mode: `process` or `subprocess`. |

## Entity methods

### Run methods

There are no additional run methods for this action.
