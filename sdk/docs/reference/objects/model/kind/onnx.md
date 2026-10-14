---
render_macros: true
---

# ONNX

The `onnx` kind stores an ONNX model. Kind-specific fields, including tensor signatures and the operator-set version, are documented with the creation functions.

## Create

### Log

{% call function_doc("log_onnx", "digitalhub_runtime_tvm.entities.model.onnx.crud") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_onnx(
            project="my-project",
            name="image-classifier",
            source="./models/image-classifier.onnx",
            opset=17,
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_onnx", "digitalhub_runtime_tvm.entities.model.onnx.crud") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_onnx(
            project="my-project",
            name="registered-image-classifier",
            source="s3://my-bucket/models/image-classifier.onnx",
            opset=17,
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
            name="image-classifier",
            kind="onnx",
            path="s3://my-bucket/models/image-classifier.onnx",
            opset=17,
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete an ONNX Model.

## Related runtime

ONNX models can be used as source models in the [TVM build workflow](../../../runtimes/tvm/actions/tvm-build.md). See the [TVM runtime](../../../runtimes/tvm/overview.md) for the full workflow.
