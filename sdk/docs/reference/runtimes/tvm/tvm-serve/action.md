---
render_macros: true
---

# TVM Serve

Use the `serve` action to deploy a compiled TVM `model.so` as a service on Kubernetes.

## What the action does

Set the Run's required `so_model_path` to the versioned Model key from the chosen
Compile Run's `status.outputs.compiled_so`. Configure the served model name,
replicas and workers on the Run; reusable Tasks contain common infrastructure
settings. Serve does not select the latest Compile or use a Function reference.

{{ overview_cards([
    ("Create", "create.md", "Use the TVM Function created for the build action."),
    ("Run", "run.md", "Deploy a compiled model and configure the service."),
    ("Use", "use.md", "Check readiness and inspect the service endpoint."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
