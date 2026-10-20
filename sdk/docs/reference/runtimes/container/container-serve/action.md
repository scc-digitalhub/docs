---
render_macros: true
---

# Container Serve

Use the `serve` action to run a container continuously as a Kubernetes service that can handle incoming requests.

## What the action does

The serve action creates a service from the configured container image.

!!! warning "Build custom images first"
    If the image needs custom Dockerfile instructions, run the [Container Build action](../container-build/action.md) first and use its resulting image for the service.

{{ overview_cards([
    ("Create", "create.md", "Configure the Function with the container image."),
    ("Run", "run.md", "Deploy the container as a long-lived service."),
    ("Use", "use.md", "Invoke the service endpoint exposed by the Run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
