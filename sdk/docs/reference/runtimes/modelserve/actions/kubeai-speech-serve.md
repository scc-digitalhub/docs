# ModelServe kubeai-speech Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a KubeAI speech Function.

- [**Task**](#task){ .list-card-link } - Configure the KubeAI speech Task.

- [**Run**](#run){ .list-card-link } - Serve the KubeAI speech model.

</div>

## Overview

The `serve` action deploys speech processing models via KubeAI as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

The kubeai-speech function kind supports deploying speech processing models via KubeAI. It supports speech-to-text functionality and can work with different engines for speech processing.

## Function

??? example "Create a function"

    Define the Function with the KubeAI speech model URL and adapters.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. Must be `kubeai-speech`. **Required.** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | model_name | str | Name of the model. |
        | image | str | Docker image where to serve the model. |
        | [url](#model-url) | str | Model url. |
        | [adapters](#adapters) | list[dict] | Adapters. |

        #### Model URL

        The SDK stores the model URL as a string and does not validate its format locally. Provide a URL supported by KubeAI, such as an `hf://` source.

        #### Adapters

        Adapters is a list of dictionaries with the following keys:

        ```python
        adapters = [{
            "name": "adapter-name",
            "url": "adapter-url"
        }]
        ```

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-kubeai-speech-service",
            kind="kubeai-speech",
            url="hf://openai/whisper-tiny",
            adapters=[{"name": "whisper-adapter", "url": "hf://adapter-url"}]
        )
        ```

### Function methods

The KubeAI speech Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        #### Shared Parameters

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`** |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |

    === "Creation example"

        ```python
        run = function.run(action="serve")
        ```

### Task methods

The KubeAI speech Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        #### Run Function Kind-Specific Parameters

        ##### KubeAI Speech

        | Name | Type | Description |
        | --- | --- | --- |
        | env | dict | Environment variables. |
        | args | list[str] | Arguments. |
        | cache_profile | str | Cache profile. |
        | [files](#files) | list[KubeaiFile] | Files. |
        | [scaling](#scaling) | Scaling | Scaling parameters. |
        | processors | int | Number of processors. |

        #### Files

        Files is a list of dict with the following keys:

        ```python
        files = [
            {
                "path": "file-path"
                "content": "file-content"
            }
        ]
        ```

        #### Scaling

        Scaling is a `Scaling` object that represents the scaling parameters for the run. Its structure is as follows:

        ```python
        scaling = {
            "replicas": int,
            "min_replicas": int,
            "max_replicas": int,
            "autoscaling_disabled": bool,
            "target_request": int,
            "scale_down_delay_seconds": int,
            "load_balancing": {
                "strategy": str,  # "LeastLoad" or "PrefixHash"
                "prefix_hash": {
                    "mean_load_factor": int,
                    "replication": int,
                    "prefix_char_length": int
                }
            }
        }
        ```

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            processors=1
        )
        ```

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

??? example "invoke"

    Invoke the KubeAI speech model serving run with input data.

    ::: digitalhub_runtime_modelserve.entities.run.kubeaiservespeechtotext_run.entity.RunKubeaiserveSpeechtotextRun.invoke
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "list_endpoints"

    List all available endpoints for the served model.

    ::: digitalhub_runtime_modelserve.entities.run.kubeaiservespeechtotext_run.entity.RunKubeaiserveSpeechtotextRun.list_endpoints
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
