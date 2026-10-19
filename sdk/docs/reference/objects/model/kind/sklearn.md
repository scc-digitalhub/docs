---
render_macros: true
---

# Scikit-learn

The `sklearn` kind stores a scikit-learn model. Kind-specific fields are documented with the creation functions.

## Create

### Log

{{ function_doc("log_sklearn", "digitalhub_runtime_modelserve.entities.model.sklearn.crud", separate_examples=True) }}

### Register

{{ function_doc("register_sklearn", "digitalhub_runtime_modelserve.entities.model.sklearn.crud", separate_examples=True) }}

### New

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="churn-classifier",
            kind="sklearn",
            path="s3://my-bucket/models/churn-classifier.joblib",
            algorithm="RandomForestClassifier",
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a scikit-learn Model.

## Related runtime

See the [ModelServe runtime](../../../runtimes/modelserve/overview.md) and its [scikit-learn serving action](../../../runtimes/modelserve/sklearnserve-serve/action.md).
