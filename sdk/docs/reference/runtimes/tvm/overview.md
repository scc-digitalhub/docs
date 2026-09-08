# TVM runtime

The TVM runtime builds, compiles, and serves machine learning models with Apache TVM. It accepts models in ONNX or TFLite format and stores the intermediate Relax IR model and compiled `model.so` as runtime outputs.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-tvm` |

## Supported kinds and actions

| Function kind | Supported actions | Purpose |
| --- | --- | --- |
| `tvm` | `build` | Convert a source model to Relax IR. |
| `tvm` | `compile` | Compile a Relax IR model for a target architecture. |
| `tvm` | `serve` | Deploy a compiled TVM model as a service. |

## Usage pattern

Use a TVM Function to describe the source model, then run the actions in order:

1. Create a `tvm` Function with the model path and optional format.
2. Run `build` to produce the Relax IR model.
3. Run `compile` to produce the compiled `model.so`.
4. Run `serve` with the compiled model path to deploy the model as a service.

??? example "Create and build a TVM function"

    ```python
    import digitalhub as dh

    function = dh.new_function(
        name="mobilenet",
        kind="tvm",
        model="s3://my-bucket/models/mobilenet.onnx",
        format="onnx",
    )

    build = function.run(
        action="build",
        wait=True,
    )
    ```

The `format` field accepts `auto`, `onnx`, or `tflite`. The function spec also supports `ir_model` and `so_model` store keys when referring to artifacts produced by previous actions.

## Local and remote execution

TVM actions can be submitted to a remote Kubernetes runtime. Use the action-specific `image`, `resources`, `volumes`, `envs`, `secrets`, and `profile` parameters to configure the execution environment.

The source model can be a local path, a store key, or a supported repository/archive URI. See the [code source](../../configuration/code-sources.md) reference for URI formats.

## Action documentation

<div class="list-cards" markdown>

- [**TVM build**](actions/tvm-build.md){ .list-card-link }

    Convert an ONNX or TFLite model to Relax IR.

- [**TVM compile**](actions/tvm-compile.md){ .list-card-link }

    Compile a Relax IR model to `model.so` for a target architecture.

- [**TVM serve**](actions/tvm-serve.md){ .list-card-link }

    Deploy a compiled TVM model as a service.

</div>

## Examples

<div class="list-cards" markdown>

- [**TVM examples**](examples.md){ .list-card-link }

    Create, build, compile, and serve a TVM model.

</div>
