---
render_macros: true
---

# TVM IR

The `tvm-ir` kind stores a Relax IR model produced by a `tvm+build` Run. Kind-specific fields, including source format, tensor signatures, and input handling, are documented with the creation functions.

The bundle contains `model.relax.json`, `metadata.json` and optional `params.bin`.
Use the build action to convert ONNX/TFLite first; registering a Model does not
convert the source or create an IR.

## Create

### Log

{{ function_doc("log_tvm_ir", "digitalhub_runtime_tvm.entities.model.tvm_ir.crud", separate_examples=True) }}

### Register

{{ function_doc("register_tvm_ir", "digitalhub_runtime_tvm.entities.model.tvm_ir.crud", separate_examples=True) }}

### New

Create a Model reference to an already uploaded bundle; this call does not compile
or upload files.

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="resnet18-relax",
            kind="tvm-ir",
            path="s3://my-bucket/models/resnet18-ir/",
            source_format="onnx",
            entry="main",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a TVM IR Model.

## Related runtime

See the [TVM runtime](../../../runtimes/tvm/overview.md), including its [build](../../../runtimes/tvm/tvm-build/action.md) and [compile](../../../runtimes/tvm/tvm-compile/action.md) workflows.
