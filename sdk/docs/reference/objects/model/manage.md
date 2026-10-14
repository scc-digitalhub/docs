---
render_macros: true
---

# Manage a model

The CRUD methods are used to read, update, and delete models. They can be called through the SDK or through the `Project` object. When managing models from a project, omit the `project` parameter and pass every other parameter as a keyword argument. For model creation functions, see the [Create a model guide](./create.md).

## Read

Use the read methods to retrieve models from the backend or load them from a YAML descriptor.

{% call function_doc("get_model", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        model = dh.get_model(
            identifier="my-model",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("get_model_versions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        models = dh.get_model_versions(
            identifier="my-model",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_models", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        models = dh.list_models(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_model", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        model = dh.import_model("my-model.yaml")
        ```
{% endcall %}

## Update

Update a model after changing its mutable metadata.

{% call function_doc("update_model", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        model = dh.get_model(
            identifier="my-model",
            project="my-project",
        )
        model.set_description("Updated model")
        model = dh.update_model(model)
        ```
{% endcall %}

## Delete

Delete one model version or all versions of a model.

{% call function_doc("delete_model", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_model(
            identifier="my-model",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}
