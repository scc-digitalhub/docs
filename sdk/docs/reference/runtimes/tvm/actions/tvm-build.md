# TVM Build

## Build reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Convert a source model to Relax IR.

- [**Function**](#function){ .list-card-link } - Create a TVM Function.

- [**Task**](#task){ .list-card-link } - Configure the TVM build Task.

- [**Run**](#run){ .list-card-link } - Execute the TVM build.

</div>

## Overview

The `build` action converts an ONNX or TFLite source model into a Relax IR model. The resulting store key can be passed to the `compile` action as `model_path` or recorded in the function's `ir_model` field.

## Function

??? example "Create a function"

    Define the Function with the source model path and format.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. **Required. Must be `tvm`.** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | model | str | Source model path or store key. **Required.** |
        | format | str | Source model format: `auto`, `onnx`, or `tflite`. |
        | ir_model | str | Store key of the Relax IR model produced by `build`. |
        | so_model | str | Store key of the compiled `model.so` produced by `compile`. |

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-tvm-model",
            kind="tvm",
            model="s3://my-bucket/models/model.onnx",
            format="onnx",
        )
        ```

### Function methods

The TVM Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `build`.** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | image | str | TVM execution image. |
        | simplify | bool | Simplify the source model during conversion. |
        | target_opset | int | Target ONNX opset. |
        | opset_override | int | Override the source ONNX opset. |
        | strict_shape_inference | bool | Enable strict shape inference. |
        | data_prop | bool | Enable data propagation. |
        | keep_params_in_input | bool | Keep model parameters as inputs. |
        | sanitize_input_names | bool | Sanitize model input names. |

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            simplify=True,
            resources={"cpu": 2, "mem": "4Gi"},
        )
        ```

### Task methods

The TVM build Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | model | str | Source model path or store key. **Required.** |
        | format | str | Source model format: `auto`, `onnx`, or `tflite`. |
        | ir_model | str | Store key for the Relax IR output. |
        | so_model | str | Store key for the compiled `model.so` output. |
        | inputs | dict[str, str] | Mapping of input names to dataitem or store keys. |
        | local_execution | bool | Execute the run locally instead of remotely. |

    === "Creation example"

        ```python
        run = function.run(
            action="build",
            wait=True,
        )
        ```

### Run methods

The TVM build Run does not add runtime-specific methods.
