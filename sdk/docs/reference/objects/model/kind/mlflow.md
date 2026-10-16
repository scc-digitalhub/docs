---
render_macros: true
---

# MLflow

The `mlflow` kind stores an MLflow model together with its flavor, configuration, input datasets, and signature metadata. Kind-specific fields are documented with the creation functions.

## Create

### Log

{{ function_doc("log_mlflow", "digitalhub_runtime_modelserve.entities.model.mlflow.crud", separate_examples=True) }}

### Register

{{ function_doc("register_mlflow", "digitalhub_runtime_modelserve.entities.model.mlflow.crud", separate_examples=True) }}

### New

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="fraud-detector",
            kind="mlflow",
            path="s3://my-bucket/models/fraud-detector",
            flavor="sklearn",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete an MLflow Model.

## Related runtime

See the [ModelServe runtime](../../../runtimes/modelserve/overview.md) and its [MLflow serving action](../../../runtimes/modelserve/actions/mlflowserve-serve.md).
