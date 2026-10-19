---
render_macros: true
---

# Scikit-learn Serve

Use the `serve` action to deploy scikit-learn models as REST API services on Kubernetes. The model must be saved in pickle format (`.pkl`).

{{ overview_cards([
    ("Create", "create.md", "Configure a Function with a pickled scikit-learn model."),
    ("Run", "run.md", "Deploy the model as a service."),
    ("Use", "use.md", "Send inference requests to the service."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
