---
render_macros: true
---

# Hera Build

Use the `build` action to compile a Hera Workflow definition into Argo Workflows YAML.

## What the action does

The build imports the source, calls the handler without arguments and serializes the returned Hera `Workflow`. It does not execute the generated workflow. An explicit build is optional before a Pipeline run because `auto_build=True` builds when needed.

{{ overview_cards([
    ("Create", "create.md", "Define a Workflow source and a handler that returns a Hera Workflow."),
    ("Run", "run.md", "Build the workflow and configure the build task."),
    ("Use", "use.md", "Retrieve the generated Argo Workflows YAML."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
