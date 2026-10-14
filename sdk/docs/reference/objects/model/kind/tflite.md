---
render_macros: true
---

# TFLite

The `tflite` kind stores a TensorFlow Lite model. Kind-specific fields, including tensor signatures, are documented with the creation functions.

## Create

### Log

{% call function_doc("log_tflite", "digitalhub_runtime_tvm.entities.model.tflite.crud") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_tflite(
            project="my-project",
            name="mobile-classifier",
            source="./models/mobile-classifier.tflite",
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_tflite", "digitalhub_runtime_tvm.entities.model.tflite.crud") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_tflite(
            project="my-project",
            name="registered-mobile-classifier",
            source="s3://my-bucket/models/mobile-classifier.tflite",
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
            name="mobile-classifier",
            kind="tflite",
            path="s3://my-bucket/models/mobile-classifier.tflite",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a TFLite Model.

## Related runtime

TFLite models can be used as source models in the [TVM build workflow](../../../runtimes/tvm/actions/tvm-build.md). See the [TVM runtime](../../../runtimes/tvm/overview.md) for the full workflow.
