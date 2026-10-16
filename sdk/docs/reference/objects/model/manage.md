---
render_macros: true
---

# Manage a model

The CRUD methods are used to read, update, and delete models. They can be called through the SDK or through the `Project` object. When managing models from a project, omit the `project` parameter and pass every other parameter as a keyword argument. For model creation functions, see the [Create a model guide](./create.md).

## Read

Use the read methods to retrieve models from the backend or load them from a YAML descriptor.

{{ function_doc("get_model", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("get_model_versions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_models", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_model", "digitalhub.entities", separate_examples=True) }}

## Update

Update a model after changing its mutable metadata.

{{ function_doc("update_model", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one model version or all versions of a model.

{{ function_doc("delete_model", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
