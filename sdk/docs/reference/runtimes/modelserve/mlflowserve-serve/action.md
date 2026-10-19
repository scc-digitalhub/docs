---
render_macros: true
---

# MLflow Serve

Use the `serve` action to deploy MLflow models as REST API services on Kubernetes. The model must be saved in MLflow format with an `MLmodel` file.

{{ overview_cards([
    ("Create", "create.md", "Configure a Function with the MLflow model path."),
    ("Run", "run.md", "Deploy the model as a service."),
    ("Use", "use.md", "Send inference requests to the service."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
