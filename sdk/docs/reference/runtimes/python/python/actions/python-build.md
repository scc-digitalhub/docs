# Python Build

## Build reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the build action does.

- [**Function**](#function){ .list-card-link } - Create a Python Function.

- [**Task**](#task){ .list-card-link } - Configure the Python build Task.

- [**Run**](#run){ .list-card-link } - Build the Python function image.

</div>

## Overview

The `build` action creates a container image containing the Python function and its dependencies. This image can then be used for deployment or distribution.

## Function

??? example "Create a function"

    Define the Function with the Python source, handler and dependencies.

    === "Parameters"

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
        | [code_src](../../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
        | [code](../../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
        | base64 | str | Source code encoded as base64. |
        | [handler](../../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
        | [init_function](#init-function) | str | Init function name for remote (Nuclio) execution. |
        | [python_version](#python-versions) | str | Python version to use. **Required.** |
        | lang | str | Source code language (informational). |
        | image | str | Container image used to execute the function. |
        | [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
        | [requirements](#requirements) | list[str] \| str | List of pip requirements or a path to a supported requirements file. |

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

        Requirements can be a list of strings or a path to an existing file named `requirements.txt`, `setup.py`, `pyproject.toml`, `conda.yml` or `conda.yaml`. The SDK parses and normalizes them when the function is saved. `requirements.txt` and `setup.py` are parsed as pip requirements, `pyproject.toml` reads `project.dependencies`, and Conda files read pip dependencies from `dependencies.pip`. If a package is specified without a version, the SDK looks for it in the active local virtual environment, adds the installed version when available, and logs a warning. See [Requirements and automatic builds](../overview.md#requirements-and-automatic-builds) for details and the build requirement for remote execution.

        ```python
        requirements = ["numpy", "pandas>1,<3", "scikit-learn==1.2.0"]
        ```

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-python-function",
            kind="python",
            code_src="handler.py",
            handler="main",
            python_version="PYTHON3_10"
        )
        ```

### Function methods

??? example "build"

    Build the Python function image.

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

    A Task for the `build` action is created when `function.run()` is called.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        #### Shared Parameters

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `build`** |
        | [volumes](../../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [instructions](#instructions) | list[str] | Build instructions executed as RUN lines in the generated Dockerfile. |

        #### Instructions

        Instructions are executed as `RUN` instructions in the generated Dockerfile. Example:

        ```python
        instructions = ["apt-get install -y git"]
        ```

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            instructions=["apt-get install -y git", "apt-get install -y curl"]
        )
        ```

### Task methods

The Python build Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    Build the Python function image and return the resulting `Run` entity.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | inputs | dict | Mapping of function argument names to entity keys. |
        | parameters | dict | Extra parameters passed to the function. |
        | init_parameters | dict | Parameters supplied to the init function. |

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            instructions=["apt-get install -y git", "apt-get install -y curl"]
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
