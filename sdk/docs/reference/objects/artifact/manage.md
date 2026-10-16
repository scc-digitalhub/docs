---
render_macros: true
---

# Manage an artifact

The CRUD methods are used to read, update, and delete artifacts. They can be called through the SDK or through the `Project` object. When managing artifacts from a project, omit the `project` parameter and pass every other parameter as a keyword argument. For artifact creation functions, see the [Create an artifact guide](./create.md).

## Read

Use the read methods to retrieve artifacts from the backend or load them from a YAML descriptor.

{{ function_doc("get_artifact", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("get_artifact_versions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_artifacts", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_artifact", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("load_artifact", "digitalhub.entities", separate_examples=True) }}

## Update

Update an artifact after changing its mutable metadata.

{{ function_doc("update_artifact", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one artifact version or all versions of an artifact.

{{ function_doc("delete_artifact", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
