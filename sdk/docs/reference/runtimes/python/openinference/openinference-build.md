# OpenInference Build

The `build` action builds a container image for an `openinference` function. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

OpenInference functions are specialized Python handlers for inference workloads. They declare model metadata and tensor schemas as part of the function specification. The build action creates an image containing the inference handler and its dependencies.

## Quick example

```python
function = dh.new_function(
    name="my-openinference-function",
    kind="openinference",
    code_src="inference.py",
    handler="predict",
    python_version="PYTHON3_10",
    model_name="text-classifier",
    inputs=[{"name": "input-0", "shape": [-1], "datatype": "BYTES"}],
    outputs=[{"name": "output-0", "shape": [-1], "datatype": "FP32"}]
)

run = function.run(
    action="build",
    instructions=["pip install transformers"]
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `openinference`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code_src/overview.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. |
| [init_function](#init-function) | str | Init function name for remote execution. |
| [python_version](#python-versions) | str | Python version to use. **Required.** |
| lang | str | Source code language (informational). |
| image | str | Container image used to execute the function. |
| [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
| [requirements](#requirements) | list | List of pip requirements to install into the execution image. |
| model_name | str | Logical model name exposed by the function. |
| [inputs](#tensor-schema) | list[dict] | Tensor definitions for the request payload. |
| [outputs](#tensor-schema) | list[dict] | Tensor definitions for the response payload. |

#### Python Versions

The Python runtime supports versions 3.10, 3.11, 3.12, and 3.13 expressed as:

- `PYTHON3_10`
- `PYTHON3_11`
- `PYTHON3_12`
- `PYTHON3_13`

#### Init Function

The init function is the entrypoint used by the Nuclio init wrapper. Specify the init function name via the `init_function` parameter.

#### Base Image

The base image is the image (name:tag) used as the foundation when building the execution image for the function.

#### Requirements

Requirements are a list of strings representing packages to be installed by `pip` in the image where the function will be executed.

#### Tensor Schema

Each item in `inputs` and `outputs` is a tensor definition with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| name | str | Tensor name. |
| shape | list[int] | Tensor shape. |
| datatype | str | Tensor datatype. Defaults to `FP32`. |

Supported tensor datatypes are: `BOOL`, `BYTES`, `UINT8`, `INT8`, `UINT16`, `INT16`, `UINT32`, `INT32`, `UINT64`, `INT64`, `FP16`, `FP32`, and `FP64`.

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `build`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| instructions | list[str] | Additional build instructions. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| init_parameters | dict | Parameters supplied to the init function. |
