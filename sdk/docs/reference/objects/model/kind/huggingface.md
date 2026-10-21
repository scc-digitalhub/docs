---
render_macros: true
---

# Hugging Face

The `huggingface` kind stores metadata for a Hugging Face model. Create the model entity by registering a source that already exists in storage or by creating a reference with `new_model()`.

## Create

### Register

{{ function_doc("register_huggingface", "digitalhub_runtime_modelserve.entities.model.huggingface.crud", separate_examples=True) }}

### New

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="text-classifier",
            kind="huggingface",
            path="s3://my-bucket/models/text-classifier",
            base_model="distilbert-base-uncased",
            model_id="my-org/text-classifier",
            model_revision="main",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a Hugging Face Model.
