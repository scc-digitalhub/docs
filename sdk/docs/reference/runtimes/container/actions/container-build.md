# Container Build

The `build` action creates a Docker image with custom instructions on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The build action generates a Dockerfile with your custom instructions and builds a container image. It's useful for creating custom images with specific dependencies or configurations.

## Quick example

```python
function = dh.new_function(
    name="my-build",
    kind="container",
    base_image="python:3.9"
)

run = function.run(
    action="build",
    instructions=["pip install numpy", "pip install pandas"],
    image="my-custom-image:latest"
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
| base_image | str | Base image used when building the execution image. **Required for `build` action** |
| image_pull_policy | str | Kubernetes image pull policy. |
| command | str | Command to run inside the container. |

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `build`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. Example: `{"limits": {"cpu": "1", "memory": "512Mi"}, "requests": {"cpu": "250m", "memory": "128Mi"}}`. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| [instructions](#instructions) | list[str] | Build instructions executed as RUN lines in the generated Dockerfile. |
| base_image | str | Base image used when building the execution image. Required for `build` unless a full image is provided. |
| image | str | Target image name:tag to build/push. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| args | list[str] | Command-line arguments to pass to the container command. |

## Instructions

Instructions are executed as `RUN` instructions in the generated Dockerfile. Example:

```python
instructions = ["apt-get install -y git"]
```

## Entity methods

### Run methods

There are no runtime-specific helper methods for container runs.
