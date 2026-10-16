---
render_macros: true
---

# Use a run

The `Run` object provides methods to inspect and control an execution.

## Persist and refresh

{{ member_doc("save", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("export", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("refresh", "digitalhub.entities.run._base.entity.Run") }}

## Control execution

{{ member_doc("run", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("wait", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("stop", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("resume", "digitalhub.entities.run._base.entity.Run") }}

## Inspect logs and metrics

{{ member_doc("logs", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("log_metric", "digitalhub.entities.run._base.entity.Run") }}

{{ member_doc("log_metrics", "digitalhub.entities.run._base.entity.Run") }}

## Kind-specific methods

Run kinds are provided by runtimes. See the [runtime documentation](../../runtimes/index.md) for the corresponding runtime behavior.

{{ page_navigation(("Manage", "manage.md"), ("Entity", "entity.md")) }}
