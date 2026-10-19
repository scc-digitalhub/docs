---
render_macros: true
---

# TVM IR

The `tvm-ir` kind stores a Relax IR model produced by `tvm` or `tvm+build`. Kind-specific fields, including source format, tensor signatures, and input handling, are documented with the creation functions.

## Create

### Log

{{ function_doc("log_tvm_ir", "digitalhub_runtime_tvm.entities.model.tvm_ir.crud", separate_examples=True) }}

### Register

{{ function_doc("register_tvm_ir", "digitalhub_runtime_tvm.entities.model.tvm_ir.crud", separate_examples=True) }}

### New

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="resnet18-relax",
            kind="tvm-ir",
            path="s3://my-bucket/models/resnet18.relax",
            source_format="onnx",
            entry="main",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a TVM IR Model.

## Related runtime

See the [TVM runtime](../../../runtimes/tvm/overview.md), including its [build](../../../runtimes/tvm/tvm-build/action.md) and [compile](../../../runtimes/tvm/tvm-compile/action.md) workflows.
