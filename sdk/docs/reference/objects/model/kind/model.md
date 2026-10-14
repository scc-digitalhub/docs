---
render_macros: true
---

# Model

The `model` kind stores a generic machine-learning model when no specialized kind metadata is needed. The `log_model()` and `register_model()` functions are provided by the SDK.

## Create

### Log

{% call function_doc("log_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_model(
            project="my-project",
            name="image-classifier",
            source="./models/image-classifier",
            framework="pytorch",
            algorithm="resnet18",
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_model(
            project="my-project",
            name="registered-image-classifier",
            source="s3://my-bucket/models/image-classifier",
            framework="pytorch",
            algorithm="resnet18",
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
            kind="model",
            path="s3://my-bucket/models/image-classifier",
            framework="pytorch",
            algorithm="resnet18",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a Model.
