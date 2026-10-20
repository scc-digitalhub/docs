---
render_macros: true
---

# Python Serve

Use the `serve` action to deploy a Python handler as an HTTP service.

## What the action does

The function runs remotely as a service and accepts HTTP requests. Serving functions do not support local execution.

!!! warning "Build requirements first"
    If the Function has `requirements`, run the [Python Build action](../python-build/action.md) before deploying it so the dependencies are installed in its image.

{{ overview_cards([
    ("Create", "create.md", "Define the Python function source, handler and dependencies."),
    ("Run", "run.md", "Deploy the service and configure its replicas and inputs."),
    ("Use", "use.md", "Invoke the endpoint and read run outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
