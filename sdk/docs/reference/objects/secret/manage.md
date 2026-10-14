---
render_macros: true
---

# Manage secrets

The CRUD methods create, read, update, and delete secrets. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument. For creation, see [Create a secret](./create.md) and the [secret kind](./kind/secret.md).

## Read

Use the read methods to retrieve secrets from the backend or load them from a YAML descriptor.

{% call function_doc("get_secret", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        secret = dh.get_secret(
            identifier="my-secret",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_secrets", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        secrets = dh.list_secrets(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_secret", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        secret = dh.import_secret("my-secret.yaml")
        ```
{% endcall %}

## Update

Update a secret after changing its mutable metadata.

{% call function_doc("update_secret", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        secret = dh.get_secret(
            identifier="my-secret",
            project="my-project",
        )
        secret.set_description("Updated secret")
        secret = dh.update_secret(secret)
        ```
{% endcall %}

## Delete

Delete one secret version or all versions of a secret.

{% call function_doc("delete_secret", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_secret(
            identifier="my-secret",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}

[Back to Secrets](./entity.md)
