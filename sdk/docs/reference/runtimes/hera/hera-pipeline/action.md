---
render_macros: true
---

# Hera Pipeline

Use the `pipeline` action to execute a Hera workflow on the platform.

## What the action does

The action executes a compiled workflow. If the workflow does not have a compiled definition, run the [Hera Build action](../hera-build/action.md) first. The `parameters` mapping supplies values for the Hera workflow parameters declared in the pipeline source.

{{ overview_cards([
    ("Create", "create.md", "Define a Workflow source and a handler that returns a Hera Workflow."),
    ("Run", "run.md", "Execute the pipeline and pass workflow parameters."),
    ("Use", "use.md", "Read results returned by the pipeline run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
