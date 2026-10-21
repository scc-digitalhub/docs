---
render_macros: true
---

# TVM Serve

Use the `serve` action to deploy a compiled TVM `model.so` as a service on Kubernetes.

## What the action does

The Run uses `function.so_model` unless it supplies `model_path`. Configure the
served model name, replicas and workers on the Run; reusable Tasks contain common
infrastructure settings.

{{ overview_cards([
    ("Create", "create.md", "Use the TVM Function created for the build action."),
    ("Run", "run.md", "Deploy a compiled model and configure the service."),
    ("Use", "use.md", "Check readiness and inspect the service endpoint."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
