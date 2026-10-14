# TVM Compile

## Compile reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Compile a Relax IR model to `model.so`.

- [**Function**](#function){ .list-card-link } - Use a TVM Function as the model source.

- [**Task**](#task){ .list-card-link } - Configure the TVM compile Task.

- [**Run**](#run){ .list-card-link } - Execute the TVM compilation.

</div>

## Overview

The `compile` action compiles a Relax IR model for a target architecture and produces a deployable `model.so` artifact.

`amd64` means Intel/AMD 64-bit (x86-64-v2); `arm64` means ARM 64-bit (AArch64);
`arm32` requires ARMv7 hard-float with NEON. `auto` uses the compile node's architecture.
Older names remain accepted aliases: `cpu`/`llvm`, `x86`, `x86_v3`, `x86_native` and
`armv7l` map to `auto`, `amd64`, `amd64_v3`, `amd64_native` and `arm32`, respectively.

## Function

??? example "Create a function"

    The compile action uses the same `tvm` Function specification as the [build action](tvm-build.md#function).

    === "Creation example"

        ```python
        function = dh.new_function(
            name="my-tvm-model",
            kind="tvm",
            model="s3://my-bucket/models/model.onnx",
            format="onnx",
        )
        ```

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `compile`.** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |
        | model_path | str | Relax IR model path or store key. |
        | target_architecture | str | Target CPU profile: `auto` (default), `amd64`, `amd64_v3`, `amd64_native`, `arm64`, `arm64_pi5`, or `arm32`. |
        | opt_level | int | TVM optimization level. |
        | cross_cc | str | Cross-compiler command. |
        | exec_mode | str | TVM execution mode. |
        | relax_pipeline | str | Relax compilation pipeline. |
        | tir_pipeline | str | TIR compilation pipeline. |
        | system_lib | bool | Build a system library. |
        | params_path | str | Model parameters path or store key. |
        | tag | str | Tag for the compiled model. |
        | image | str | TVM execution image. |

    === "Creation example"

        ```python
        run = function.run(
            action="compile",
            model_path="store://my-project/model/model-relax:version",
            target_architecture="auto",
            opt_level=3,
        )
        ```

### Task methods

The TVM compile Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | model | str | Source model path or store key. **Required.** |
        | format | str | Source model format: `auto`, `onnx`, or `tflite`. |
        | ir_model | str | Store key of the Relax IR model. |
        | so_model | str | Store key for the compiled `model.so` output. |
        | model_path | str | Relax IR model path or store key. |
        | target_architecture | str | Target CPU profile: `auto` (default), `amd64`, `amd64_v3`, `amd64_native`, `arm64`, `arm64_pi5`, or `arm32`. |
        | opt_level | int | TVM optimization level. |
        | cross_cc | str | Cross-compiler command. |
        | exec_mode | str | TVM execution mode. |
        | relax_pipeline | str | Relax compilation pipeline. |
        | tir_pipeline | str | TIR compilation pipeline. |
        | system_lib | bool | Build a system library. |
        | params_path | str | Model parameters path or store key. |
        | tag | str | Tag for the compiled model. |
        | image | str | TVM execution image. |
        | local_execution | bool | Execute the run locally instead of remotely. |

    === "Creation example"

        ```python
        run = function.run(
            action="compile",
            model_path="store://my-project/model/model-relax:version",
            target_architecture="auto",
            wait=True,
        )
        ```

### Run methods

The TVM compile Run does not add runtime-specific methods.
