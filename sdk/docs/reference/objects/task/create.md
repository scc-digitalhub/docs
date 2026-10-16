---
render_macros: true
---

# Create a task

Tasks are normally created automatically when a Function or Workflow runs. Use `new_task()` for direct task creation. The `kind` combines an executable kind and an action, such as `python+job`. See the [runtime documentation](../../runtimes/index.md) for runtime-specific configuration.

{{ function_doc("new_task", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
