---
render_macros: true
---

# Create a workflow

Choose the runtime guide for instructions on creating, configuring, and executing that kind of workflow.

## Choose a workflow kind

{{ kind_cards([
    ("Hera", "../../runtimes/hera/overview.md", "Build workflows with Hera pipelines", "hera"),
]) }}

## Create a workflow

Use `new_workflow()` to create and save a workflow. See the [Hera runtime documentation](../../runtimes/hera/overview.md) for runtime-specific requirements.

{{ function_doc("new_workflow", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
