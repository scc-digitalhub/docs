# Container Serve

The `serve` action deploys a container as a long-lived service on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The serve action creates a Kubernetes service that runs continuously and can handle incoming requests. It's ideal for web applications, APIs, or any service that needs to be available over time.

## Quick example

```python
function = dh.new_function(
    name="my-service",
    kind="container",
    image="my-app:latest"
)

run = function.run(
    action="serve",
    replicas=3,
    service_ports=[{"port": 80, "targetPort": 8080}]
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. **Required. Must be `container`** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code_src/overview.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. |
| lang | str | Source code language (informational). |
| image | str | Container image to use for execution (name:tag). |
| base_image | str | Base image used when building the execution image. |
| image_pull_policy | str | Kubernetes image pull policy. |
| command | str | Command to run inside the container. |

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `serve`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. Example: `{"limits": {"cpu": "1", "memory": "512Mi"}, "requests": {"cpu": "250m", "memory": "128Mi"}}`. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| [replicas](../../../configuration/kubernetes/overview.md#replicas) | int | Number of replicas. |
| [service_ports](../../../configuration/kubernetes/overview.md#service-port-type) | list[dict] | Ports to expose for the service. Example: `[{"port": 80, "targetPort": 8080}]`. |
| [service_type](../../../configuration/kubernetes/overview.md#service-port-type) | str | Service type. |
| [run_as_user](../../../configuration/kubernetes/overview.md#security-context) | int | User ID to run the container. |
| [run_as_group](../../../configuration/kubernetes/overview.md#security-context) | int | Group ID to run the container. |
| [fs_group](../../../configuration/kubernetes/overview.md#security-context) | int | File system group ID. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| args | list[str] | Command-line arguments to pass to the container command. |

## Entity methods

### Run methods

There are no runtime-specific helper methods for container runs.
