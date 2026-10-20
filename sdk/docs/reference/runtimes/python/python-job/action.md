---
render_macros: true
---

# Python Job

Use the `job` action to execute a Python handler as a one-off task.

## What the action does

The handler runs to completion. A job can execute locally or remotely; remote execution uses the configured function image and dependencies.

!!! warning "Build remote requirements first"
    For remote execution, if the Function has `requirements`, run the [Python Build action](../python-build/action.md) first so the dependencies are installed in its image. For local execution, install the dependencies locally.

{{ overview_cards([
    ("Create", "create.md", "Define the Python function source, handler and dependencies."),
    ("Run", "run.md", "Configure local or remote execution and pass handler inputs."),
    ("Use", "use.md", "Read entity outputs and primitive results from the run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
