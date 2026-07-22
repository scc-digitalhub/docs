# Guardrail Serve

The `serve` action deploys a `guardrail` function as a request/response processor on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

Guardrail functions are specialized Python handlers that process inbound requests, outbound responses, or both. They are intended for validation, filtering, enrichment, or policy enforcement around an upstream service.

## Quick example

```python
function = dh.new_function(
    name="my-guardrail-function",
    kind="guardrail",
    code_src="guardrail.py",
    handler="process",
    python_version="PYTHON3_10",
    processing_mode="preprocessor"
)

run = function.run(
    action="serve",
    replicas=1,
    service_type="ClusterIP"
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `guardrail`. **Required.** |
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
| [processing_mode](#processing-mode) | str | Guardrail processing mode. **Required.** |

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

#### Processing Mode

The processing mode determines where the guardrail is applied in the request/response lifecycle:

- `preprocessor`: modifies or validates incoming traffic before forwarding it upstream
- `postprocessor`: modifies or validates outgoing traffic before returning it to the client
- `wrapprocessor`: can inspect both request and response and can short-circuit the flow when needed

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `serve`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |
| [replicas](../../../configuration/kubernetes/overview.md#replicas) | int | Number of replicas. |
| service_type | str | Kubernetes service type. |
| service_name | str | Name assigned to the created service. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| init_parameters | dict | Parameters supplied to the init function. |
