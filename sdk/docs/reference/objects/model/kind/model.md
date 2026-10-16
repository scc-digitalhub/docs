---
render_macros: true
---

# Model

The `model` kind stores a generic machine-learning model when no specialized kind metadata is needed. The `log_model()` and `register_model()` functions are provided by the SDK.

## Create

### Log

{{ function_doc("log_model", "digitalhub.entities", separate_examples=True) }}

### Register

{{ function_doc("register_model", "digitalhub.entities", separate_examples=True) }}

### New

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="image-classifier",
            kind="model",
            path="s3://my-bucket/models/image-classifier",
            framework="pytorch",
            algorithm="resnet18",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a Model.
