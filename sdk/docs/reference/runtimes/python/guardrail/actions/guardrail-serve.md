# Guardrail Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a Guardrail Function.

- [**Task**](#task){ .list-card-link } - Configure the Guardrail serve Task.

- [**Run**](#run){ .list-card-link } - Deploy the Guardrail function as a service.

</div>

## Overview

Guardrail functions are specialized Python handlers that process inbound requests, outbound responses, or both. The `serve` action deploys a `guardrail` function as a request/response processor on Kubernetes.

## Function

??? example "Create a function"

    Define the Function with the Guardrail source, handler, processing mode and dependencies.

    === "Parameters"

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
        | [code_src](../../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
        | [code](../../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
        | base64 | str | Source code encoded as base64. |
        | [handler](../../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
        | [init_function](#init-function) | str | Init function name for remote execution. |
        | [python_version](#python-versions) | str | Python version to use. **Required.** |
        | lang | str | Source code language (informational). |
        | image | str | Container image used to execute the function. |
        | [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
        | [requirements](#requirements) | list[str] \| str | List of pip requirements or a path to a supported requirements file. |
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

        Requirements can be a list of strings or a path to an existing file named `requirements.txt`, `setup.py`, `pyproject.toml`, `conda.yml` or `conda.yaml`. The SDK parses and normalizes them when the function is saved. `requirements.txt` and `setup.py` are parsed as pip requirements, `pyproject.toml` reads `project.dependencies`, and Conda files read pip dependencies from `dependencies.pip`. If a package is specified without a version, the SDK looks for it in the active local virtual environment, adds the installed version when available, and logs a warning. A build is required to install requirements before remote execution. See [Requirements and automatic builds](../../python/overview.md#requirements-and-automatic-builds) for details.

        #### Processing Mode

        The processing mode determines where the guardrail is applied in the request/response lifecycle:

        - `preprocessor`: modifies or validates incoming traffic before forwarding it upstream
        - `postprocessor`: modifies or validates outgoing traffic before returning it to the client
        - `wrapprocessor`: can inspect both request and response and can short-circuit the flow when needed

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-guardrail-function",
            kind="guardrail",
            code_src="guardrail.py",
            handler="process",
            python_version="PYTHON3_10",
            processing_mode="preprocessor"
        )
        ```

### Function methods

??? example "build"

    Build the Guardrail function image.

    ::: digitalhub_runtime_python.entities.function._base.entity.FunctionBaseFunction.build
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Task

??? example "Create a task"

    A Task for the `serve` action is created when `function.run()` is called.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`** |
        | [volumes](../../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [replicas](../../../../configuration/kubernetes.md#replicas) | int | Number of replicas. |
        | service_type | str | Kubernetes service type. |
        | service_name | str | Name assigned to the created service. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            replicas=1,
            service_type="ClusterIP"
        )
        ```

### Task methods

The Guardrail serve Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    Deploy the Guardrail function as a request/response service and return the resulting `Run` entity.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | auto_build | bool | Build the function automatically when `spec.image` is `None`. Defaults to `False`. If requirements are present, an existing image is not rebuilt automatically. |
        | init_parameters | dict | Parameters supplied to the init function. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            replicas=1,
            service_type="ClusterIP"
        )
        ```

### Run methods

??? example "inputs"

    Get inputs passed in the run specification.

    ::: digitalhub_runtime_python.entities.run._base.entity.RunBaseRun.inputs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "output"

    Get run's output by name.

    ::: digitalhub_runtime_python.entities.run._base.entity.RunBaseRun.output
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "outputs"

    Get run's outputs.

    ::: digitalhub_runtime_python.entities.run._base.entity.RunBaseRun.outputs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "result"

    Get result by name.

    ::: digitalhub_runtime_python.entities.run._base.entity.RunBaseRun.result
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "results"

    Get results.

    ::: digitalhub_runtime_python.entities.run._base.entity.RunBaseRun.results
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
