---
render_macros: true
---

# TVM SO

The `tvm-so` kind stores a compiled TVM shared-object model. Kind-specific fields, including target, optimization level, manifest, and tensor signatures, are documented with the creation functions.

## Create

### Log

{% call function_doc("log_tvm_so", "digitalhub_runtime_tvm.entities.model.tvm_so.crud") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_tvm_so(
            project="my-project",
            name="resnet18-tvm",
            source="./build/resnet18.so",
            target="llvm -mcpu=x86-64-v2",
            opt_level=3,
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_tvm_so", "digitalhub_runtime_tvm.entities.model.tvm_so.crud") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_tvm_so(
            project="my-project",
            name="registered-resnet18-tvm",
            source="s3://my-bucket/models/resnet18.so",
            target="llvm -mcpu=x86-64-v2",
            opt_level=3,
        )
        ```
{% endcall %}

### New

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="resnet18-tvm",
            kind="tvm-so",
            path="s3://my-bucket/models/resnet18.so",
            target="llvm -mcpu=x86-64-v2",
            opt_level=3,
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a TVM SO Model.

## Related runtime

See the [TVM runtime](../../../runtimes/tvm/overview.md), including its [compile](../../../runtimes/tvm/actions/tvm-compile.md) and [serve](../../../runtimes/tvm/actions/tvm-serve.md) workflows.
