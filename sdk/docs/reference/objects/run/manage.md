---
render_macros: true
---

# Manage runs

Use these methods to retrieve, import, update, or delete runs.

## Read

Retrieve runs from the backend or import them from a YAML descriptor.

{{ function_doc("get_run", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_runs", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_run", "digitalhub.entities", separate_examples=True) }}

## Update

Update a run after changing its mutable metadata.

{{ function_doc("update_run", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete a run from the backend.

{{ function_doc("delete_run", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
