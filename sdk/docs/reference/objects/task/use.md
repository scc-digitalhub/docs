---
render_macros: true
---

# Use a task

The `Task` object provides CRUD methods and methods for managing its runs.

## Persist and refresh

{{ member_doc("save", "digitalhub.entities.task._base.entity.Task") }}

{{ member_doc("export", "digitalhub.entities.task._base.entity.Task") }}

{{ member_doc("refresh", "digitalhub.entities.task._base.entity.Task") }}

## Manage runs

{{ member_doc("run", "digitalhub.entities.task._base.entity.Task") }}

{{ member_doc("new_run", "digitalhub.entities.task._base.entity.Task") }}

{{ member_doc("get_run", "digitalhub.entities.task._base.entity.Task") }}

{{ member_doc("delete_run", "digitalhub.entities.task._base.entity.Task") }}

## Task kinds

Task kinds are provided by runtimes. See the [runtime documentation](../../runtimes/index.md) for the corresponding runtime behavior.

{{ page_navigation(("Manage", "manage.md"), ("Entity", "entity.md")) }}
