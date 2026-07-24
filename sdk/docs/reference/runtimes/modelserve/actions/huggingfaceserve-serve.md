# ModelServe huggingfaceserve Serve

The `serve` action deploys HuggingFace ML models as services on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

The huggingfaceserve function kind supports deploying HuggingFace models as REST API services. It supports various model formats and tasks including text generation, classification, and embedding.

## Quick example

```python
function = dh.new_function(
    name="my-huggingface-service",
    kind="huggingfaceserve",
    path="s3://my-bucket/path-to-model"
)

run = function.run(
    action="serve",
    replicas=1,
    huggingface_task="text_generation"
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

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

The model path must follow the pattern:

```python
path_regex = (
    r"^(store://([^/]+)/model/huggingface/.*)"
    + r"|"
    + r".*\\/$"
    + r"|"
    + r".*\\.zip$"
    + r"|"
    + r"^huggingface?://.*$"
    + r"|"
    + r"^hf?://.*$"
)
```

#### Model Image

Model image must follow the pattern:

```python
image_regex = r"^kserve\\/huggingfaceserver?:"
```

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
| [service_type](../../../configuration/kubernetes/overview.md#service-port-type) | str | Service type. |
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

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| args | list[str] | Arguments for the HuggingFace serve command. |

## Entity methods

### Run methods

Once the run is created, you can access its attributes and methods through the `run` object.

::: digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.entity.RunHuggingfaceserveRun.invoke
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
