---
render_macros: true
---

# Manage secrets

The CRUD methods create, read, update, and delete secrets. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument. For creation, see [Create a secret](./create.md) and the [secret kind](./kind/secret.md).

## Read

Use the read methods to retrieve secrets from the backend or load them from a YAML descriptor.

{{ function_doc("get_secret", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_secrets", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_secret", "digitalhub.entities", separate_examples=True) }}

## Update

Update a secret after changing its mutable metadata.

{{ function_doc("update_secret", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one secret version or all versions of a secret.

{{ function_doc("delete_secret", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
