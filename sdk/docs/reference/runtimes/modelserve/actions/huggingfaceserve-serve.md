# ModelServe huggingfaceserve Serve

## Serve reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the serve action does.

- [**Function**](#function){ .list-card-link } - Create a HuggingFace serving Function.

- [**Task**](#task){ .list-card-link } - Configure the HuggingFace serving Task.

- [**Run**](#run){ .list-card-link } - Serve the HuggingFace model.

</div>

## Overview

The `serve` action deploys HuggingFace ML models as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

The huggingfaceserve function kind supports deploying HuggingFace models as REST API services. It supports various model formats and tasks including text generation, classification, and embedding.

## Function

??? example "Create a function"

    Define the Function with the HuggingFace model path and serving image.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. Must be `huggingfaceserve`. **Required.** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | [path](#model-path) | str | Path to the model files. |
        | model_name | str | Name of the model. |
        | [image](#model-image) | str | Docker image where to serve the model. |

        #### Model Path

        The SDK stores the model path as a string and does not validate its format locally. Provide a path supported by the platform and the Hugging Face serving runtime.

        #### Model Image

        The SDK stores the image as a string and does not validate its format locally. Provide an image compatible with the Hugging Face serving runtime.

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-huggingface-service",
            kind="huggingfaceserve",
            path="s3://my-bucket/path-to-model"
        )
        ```

### Function methods

The HuggingFace serving Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `serve`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | [replicas](../../../configuration/kubernetes.md#replicas) | int | Number of replicas. |
        | [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | Service type. |
        | service_name | str | Service name. |
        | [huggingface_task](#huggingface-task) | str | Huggingface task type. |
        | [backend](#backend) | str | Backend type. |
        | tokenizer_revision | str | Tokenizer revision. |
        | max_length | int | Huggingface max sequence length for the tokenizer. |
        | disable_lower_case | bool | Do not use lower case for the tokenizer. |
        | disable_special_tokens | bool | The sequences will not be encoded with the special tokens relative to their model. |
        | [dtype](#dtype) | str | Data type to load the weights in. |
        | trust_remote_code | bool | Allow loading of models and tokenizers with custom code. |
        | tensor_input_names | list[str] | The tensor input names passed to the model. |
        | return_token_type_ids | bool | Return token type ids. |
        | return_probabilities | bool | Return all probabilities. |
        | disable_log_requests | bool | Disable log requests. |
        | max_log_len | int | Max number of prompt characters or prompt. |

        #### HuggingFace Task

        You can specify the task type for the Huggingface model. The task type must be one of the following:

        - `sequence_classification`
        - `token_classification`
        - `fill_mask`
        - `text_generation`
        - `text2text_generation`
        - `text_embedding`

        #### Backend

        You can specify the backend type for the Huggingface model. The backend type must be one of the following:

        - `AUTO`
        - `VLLM`
        - `HUGGINGFACE`

        #### Dtype

        You can specify the data type to load the weights in. The data type must be one of the following:

        - `AUTO`
        - `FLOAT32`
        - `FLOAT16`
        - `BFLOAT16`
        - `FLOAT`
        - `HALF`

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            replicas=1,
            huggingface_task="text_generation"
        )
        ```

### Task methods

The HuggingFace serving Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | args | list[str] | Arguments for the HuggingFace serve command. |

    === "Creation example"

        ```python
        run = function.run(
            action="serve",
            args=["--help"]
        )
        ```

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

??? example "invoke"

    Invoke the HuggingFace model serving run with input data.

    ::: digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.entity.RunHuggingfaceserveRun.invoke
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
