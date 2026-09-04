# Python Job

## Job reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the job action does.

- [**Function**](#function){ .list-card-link } - Create a Python Function.

- [**Task**](#task){ .list-card-link } - Configure the Python job Task.

- [**Run**](#run){ .list-card-link } - Execute the Python function as a job.

</div>

## Overview

The `job` action executes a Python function as a one-off task on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

The job action supports Python handlers that run to completion.

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
        | [requirements](#requirements) | list[str] \| str | List of pip requirements or a supported requirements file path. |

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

        Requirements can be a list of strings or a path to a supported requirements file. The SDK parses and normalizes them when the function is saved. See [Requirements and automatic builds](../../../../../explanations/runtimes/python-execution.md#requirements-and-automatic-builds) for supported filenames, local version inference, and the build requirement for remote execution.

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

The Python Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    A Task for the `job` action is created when `function.run()` is called.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `job`** |
        | [volumes](../../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../../configuration/kubernetes.md#profile) | str | Profile template. |

    === "Creation example"

        ```python
        run = function.run(
            action="job",
            inputs={"data": dataitem.key},
            parameters={"threshold": 0.5}
        )
        ```

### Task methods

The Python job Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    Execute the Python function as a one-off job and return the resulting `Run` entity.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | local_execution | bool | Execute the run locally instead of remotely. |
        | auto_build | bool | Build the function automatically when `spec.image` is `None`. Defaults to `True`. If requirements are present, an existing image is not rebuilt automatically. |
        | inputs | dict | Mapping of function argument names to entity keys. |
        | parameters | dict | Extra parameters passed to the function. |
        | init_parameters | dict | Parameters supplied to the init function. |

    === "Creation example"

        ```python
        run = function.run(
            action="job",
            inputs={"data": dataitem.key},
            parameters={"threshold": 0.5}
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
