---
render_macros: true
---

# Use a function

The `Function` object can execute code and manage its related tasks and triggers.

## Persist and refresh

{{ member_doc("save", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("export", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("refresh", "digitalhub.entities.function._base.entity.Function") }}

## Run

Use `run()` to execute a function. Its keyword arguments are passed to the run builder, including inputs, parameters, and runtime-specific options.

{{ member_doc("run", "digitalhub.entities.function._base.entity.Function") }}

## Manage tasks

The Function object exposes methods to create, retrieve, list, update, and delete its tasks.

{{ member_doc("new_task", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("get_task", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("list_task", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("import_tasks", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("update_task", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("set_task", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("delete_task", "digitalhub.entities.function._base.entity.Function") }}

## Manage triggers

The Function object exposes methods to create, retrieve, and list its triggers.

{{ member_doc("trigger", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("get_trigger", "digitalhub.entities.function._base.entity.Function") }}

{{ member_doc("list_triggers", "digitalhub.entities.function._base.entity.Function") }}

## Kind-specific methods

Methods specific to a function kind are documented in the reference documentation for the corresponding runtime.

[Back to Function](./entity.md)
