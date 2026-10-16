---
render_macros: true
---

# Manage projects

The methods below retrieve, import, update, or delete projects. For project creation, see [Create a project](./create.md).

## Read

Use the read methods to retrieve projects from the backend or load them from a YAML descriptor.

{{ function_doc("get_project", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_project", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("load_project", "digitalhub.entities", separate_examples=True) }}

## Update

Update a project after changing its mutable metadata.

{{ function_doc("update_project", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete a project from the backend.

{{ function_doc("delete_project", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
