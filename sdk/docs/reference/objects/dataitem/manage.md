---
render_macros: true
---

# Manage dataitems

The CRUD methods are used to read, update, and delete dataitems. They can be called through the SDK or through the `Project` object. When managing dataitems from a project, omit the `project` parameter and pass every other parameter as a keyword argument. For dataitem creation functions, see the [Create a dataitem guide](./create.md).

## Read

Use the read methods to retrieve dataitems from the backend or load them from a YAML descriptor.

{{ function_doc("get_dataitem", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("get_dataitem_versions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_dataitems", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_dataitem", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("load_dataitem", "digitalhub.entities", separate_examples=True) }}

## Update

Update a dataitem after changing its mutable metadata.

{{ function_doc("update_dataitem", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one dataitem version or all versions of a dataitem.

{{ function_doc("delete_dataitem", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
