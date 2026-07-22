# Python Job

The `job` action executes a Python function as a one-off task on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The job action executes a Python function as a one-off task. This is suitable for batch processing, data transformation, and other tasks that run to completion.

## Quick example

```python
function = dh.new_function(
    name="my-python-function",
    kind="python",
    code_src="handler.py",
    handler="main",
    python_version="PYTHON3_10"
)

run = function.run(
    action="job",
    inputs={"data": dataitem.key},
    parameters={"threshold": 0.5}
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `python`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code_src/overview.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. |
| [init_function](#init-function) | str | Init function name for remote (Nuclio) execution. |
| [python_version](#python-versions) | str | Python version to use. **Required.** |
| lang | str | Source code language (informational). |
| image | str | Container image used to execute the function. |
| [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
| [requirements](#requirements) | list | List of pip requirements to install into the execution image. |

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

!!! warning
    Deploying jobs built from certain base images may be restricted by cluster security policies. Confirm allowed base images with your cluster administrator.

#### Requirements

Requirements are a list of strings representing packages to be installed by `pip` in the image where the function will be executed.

```python
requirements = ["numpy", "pandas>1,<3", "scikit-learn==1.2.0"]
```

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `job`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| local_execution | bool | Execute the run locally instead of remotely. |
| inputs | dict | Mapping of function argument names to entity keys. |
| parameters | dict | Extra parameters passed to the function. |
| init_parameters | dict | Parameters supplied to the init function. |

## Entity methods

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

::: digitalhub_runtime_python.entities.run._base.entity.RunPythonRun.output
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub_runtime_python.entities.run._base.entity.RunPythonRun.outputs
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub_runtime_python.entities.run._base.entity.RunPythonRun.result
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub_runtime_python.entities.run._base.entity.RunPythonRun.results
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
