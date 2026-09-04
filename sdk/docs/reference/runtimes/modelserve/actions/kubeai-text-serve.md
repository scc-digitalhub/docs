# ModelServe kubeai-text Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a KubeAI text Function.

- [**Task**](#task){ .list-card-link } - Configure the KubeAI text Task.

- [**Run**](#run){ .list-card-link } - Serve the KubeAI text model.

</div>

## Overview

The `serve` action deploys text generation models via KubeAI as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

The kubeai-text function kind supports deploying text generation and processing models via KubeAI. It supports various features including text generation, text embedding, and can work with different engines like Ollama, VLLM, etc.

## Function

??? example "Create a function"

    Define the Function with the KubeAI text model URL, features and engine.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. Must be `kubeai-text`. **Required.** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | model_name | str | Name of the model. |
        | image | str | Docker image where to serve the model. |
        | [url](#model-url) | str | Model url. |
        | [adapters](#adapters) | list[dict] | Adapters. |
        | [features](#features) | list[str] | Features. |
        | [engine](#engine) | KubeaiEngine | Engine. |

        #### Adapters

        Adapters is a list of dictionaries with the following keys:

        ```python
        adapters = [{
            "name": "adapter-name",
            "url": "adapter-url"
        }]
        ```

        #### Features

        Features is a list of strings. It accepts the following values:

        - `TextGeneration`
        - `TextEmbedding`
        - `SpeechToText`

        #### Engine

        The engine is a `KubeaiEngine` object that represents the engine to use for the function. The engine can be one of the following:

        - `OLlama`
        - `VLLM`
        - `FasterWhisper`
        - `Infinity`

        #### Model URL

        The SDK stores the model URL as a string and does not validate its format locally. Provide a URL supported by KubeAI, such as an `hf://` source.

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-kubeai-text-service",
            kind="kubeai-text",
            url="hf://microsoft/DialoGPT-medium",
            features=["TextGeneration"],
            engine="VLLM"
        )
        ```

### Function methods

The KubeAI text Function does not add runtime-specific methods.

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

The KubeAI text Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        #### Run Function Kind-Specific Parameters

        ##### KubeAI Text

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

    Invoke the KubeAI text model serving run with input data.

    ::: digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.entity.RunKubeaiserveTextRun.invoke
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

    ::: digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.entity.RunKubeaiserveTextRun.list_endpoints
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
