---
render_macros: true
---

# Manage tasks

Tasks are unversioned and belong to a project. Use these methods to retrieve, import, load, update, or delete tasks.

## Read

{{ function_doc("get_task", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_tasks", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_task", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("load_task", "digitalhub.entities", separate_examples=True) }}

## Update

Update a task after changing its mutable metadata. Its specification is immutable where required by the backend.

{{ function_doc("update_task", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete a task from the backend.

{{ function_doc("delete_task", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
