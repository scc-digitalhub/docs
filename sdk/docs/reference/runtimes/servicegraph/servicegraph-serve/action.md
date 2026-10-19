---
render_macros: true
---

# ServiceGraph Serve

Use the `serve` action to deploy a declarative ServiceGraph pipeline as a service on Kubernetes.

## What the action does

The pipeline can expose synchronous HTTP inputs or connect streaming sources and outputs. The action configures the service ports and other Kubernetes resources.

{{ overview_cards([
    ("Create", "create.md", "Provide a ServiceGraph pipeline definition."),
    ("Run", "run.md", "Configure service ports, resources and pipeline parameters."),
    ("Use", "use.md", "Check readiness and invoke or connect to the deployed pipeline."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
