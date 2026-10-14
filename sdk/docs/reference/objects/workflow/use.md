---
render_macros: true
---

# Use a workflow

The `Workflow` object can execute workflow pipelines and manage their related tasks and triggers.

## Persist and refresh

{{ member_doc("save", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("export", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("refresh", "digitalhub.entities.workflow._base.entity.Workflow") }}

## Run

Use `run()` to execute a workflow. Its keyword arguments are passed to the run builder, including inputs, parameters, and runtime-specific options.

{{ member_doc("run", "digitalhub.entities.workflow._base.entity.Workflow") }}

## Manage tasks

The Workflow object exposes methods to create, retrieve, list, update, and delete its tasks.

{{ member_doc("new_task", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("get_task", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("list_task", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("import_tasks", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("update_task", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("set_task", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("delete_task", "digitalhub.entities.workflow._base.entity.Workflow") }}

## Manage triggers

The Workflow object exposes methods to create, retrieve, and list its triggers.

{{ member_doc("trigger", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("get_trigger", "digitalhub.entities.workflow._base.entity.Workflow") }}

{{ member_doc("list_triggers", "digitalhub.entities.workflow._base.entity.Workflow") }}

## Kind-specific methods

Methods specific to a workflow kind are documented in the reference documentation for the corresponding runtime.

[Back to Workflow](./entity.md)
