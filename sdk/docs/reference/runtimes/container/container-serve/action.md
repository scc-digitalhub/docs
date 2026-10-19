---
render_macros: true
---

# Container Serve

Use the `serve` action to run a container continuously as a Kubernetes service that can handle incoming requests.

## What the action does

The serve action creates a service from the configured container image.

{{ overview_cards([
    ("Create", "create.md", "Configure the Function with the container image."),
    ("Run", "run.md", "Deploy the container as a long-lived service."),
    ("Use", "use.md", "Invoke the service endpoint exposed by the Run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
