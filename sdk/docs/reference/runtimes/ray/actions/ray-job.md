# Ray Job

## Job reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the job action does.

- [**Function**](#function){ .list-card-link } - Create a Ray Function.

- [**Task**](#task){ .list-card-link } - Configure the Ray job Task.

- [**Run**](#run){ .list-card-link } - Execute the Ray function as a job.

</div>

## Overview

The `job` action executes a Ray function as a one-off job on a dynamically created Ray cluster. The cluster is defined by the number of the replicas (initial, minimum and maximum) and the resources/profile to be allocated by each worker node. The configuration of the Head node is defined automatically. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Function

??? example "Create a function"

    Define the Function with the Hydra Python source, handler and dependencies.

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
        | image | str | Container image used to execute the function. |
        | [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
        | [requirements](#requirements) | list[str] \| str | List of pip requirements or a path to a supported requirements file. |
        | [ray_version](#ray-versions) | str | Ray version to use. |

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
        func = project.new_function(
            name="ray-training",
            kind="ray",
            requirements=["torch==2.2.2", "torchvision==0.17.2", "numpy==1.24.1"],
            code_src="src/ray_train.py",
            handler="ray_handler"
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

    A Task for the `job` action is created when `function.run()` is called.
	The profile and resource configurations apply to a single subtask, not to the orchestrating launcher. 

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
        | [replicas](#replicas) | num | Number of replicas to start for the task. |
        | [min_replicas](#min-replicas) | num | Minimum number of replicas to allow for the task. |
        | [max_replicas](#max-replicas) | num | Maximum number of replicas to allow for the task. |

    === "Creation example"

        ```python
		run = func.run(
			action="job",
			replicas=2,
            min_replicas=2,
            max_replicas=2,
            parameters={"epochs": 10},
            volumes=[
                {
                    "name": "data",
                    "mount_path": "/data",
                    "volume_type": "persistent_volume_claim",
                    "spec": {"size": "1Gi"} 
                }
            ]
		)
        ```

### Task methods

The Ray job Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    Execute the Hydra function as a one-off job and return the resulting `Run` entity.

    === "Parameters"

        Can only be specified when calling `function.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | auto_build | bool | Build the function automatically when `spec.image` is `None`. Defaults to `False`. If requirements are present, an existing image is not rebuilt automatically. |
        | parameters | dict | Extra parameters as Ray overrides passed to the function execution. |
        | [replicas](#replicas) | num | Number of replicas to start for the task. |
        | [min_replicas](#min-replicas) | num | Minimum number of replicas to allow for the task. |
        | [max_replicas](#max-replicas) | num | Maximum number of replicas to allow for the task. |

    === "Creation example"

        ```python
		run = func.run(
			action="job",
			replicas=2,
            min_replicas=2,
            max_replicas=2,
            parameters={"epochs": 10},
            volumes=[
                {
                    "name": "data",
                    "mount_path": "/data",
                    "volume_type": "persistent_volume_claim",
                    "spec": {"size": "1Gi"} 
                }
            ]
		)
        ```

### Run methods

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
