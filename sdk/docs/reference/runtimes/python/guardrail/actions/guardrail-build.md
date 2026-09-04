# Guardrail Build

## Build reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the build action does.

- [**Function**](#function){ .list-card-link } - Create a Guardrail Function.

- [**Task**](#task){ .list-card-link } - Configure the Guardrail build Task.

- [**Run**](#run){ .list-card-link } - Build the Guardrail function image.

</div>

## Overview

Guardrail functions are specialized Python handlers used to intercept or transform request and response traffic. The `build` action creates an image containing the guardrail handler and its dependencies.

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
        | [requirements](#requirements) | list[str] | List of pip requirements to install into the execution image. |
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

        Requirements are a list of strings representing packages to be installed by `pip` in the image where the function will be executed. The SDK normalizes them when the function is saved; an unversioned package found in the local environment is replaced with its installed version and a warning is logged. A build is required to install requirements before remote execution. See [Requirements and automatic builds](../../../../../explanations/runtimes/python-execution.md#requirements-and-automatic-builds) for details.

        #### Processing Mode

        The processing mode determines where the guardrail is applied in the request/response lifecycle:

        - `preprocessor`
        - `postprocessor`
        - `wrapprocessor`

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

The Guardrail Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    A Task for the `build` action is created when `function.run()` is called.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `build`** |
        | [volumes](../../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [instructions](#instructions) | list[str] | Additional build instructions. |

        #### Instructions

        Instructions are executed as `RUN` instructions in the generated Dockerfile. Example:

        ```python
        instructions = ["pip install my-guardrail-lib"]
        ```

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            instructions=["pip install my-guardrail-lib"]
        )
        ```

### Task methods

The Guardrail build Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    Build the Guardrail function image and return the resulting `Run` entity.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | init_parameters | dict | Parameters supplied to the init function. |

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            instructions=["pip install my-guardrail-lib"]
        )
        ```

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

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

??? example "image"

    Get the image generated by the build run.

    ::: digitalhub_runtime_python.entities.run._base.entity.RunBaseBuildRun.image
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
