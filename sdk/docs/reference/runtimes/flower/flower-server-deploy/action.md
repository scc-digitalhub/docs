---
render_macros: true
---

# Flower Server Deploy

Use the `deploy` action to deploy a Flower server that coordinates federated-learning clients.

## What the action does

The server manages client communications and training rounds using the image configured on the Function.

!!! warning "Build requirements first"
    If the Function has `requirements`, run the [Flower Server Build action](../flower-server-build/action.md) before deploying it so the dependencies are installed in its image.

{{ overview_cards([
    ("Create", "create.md", "Configure the Flower server image and dependencies."),
    ("Run", "run.md", "Deploy the server and configure authentication."),
    ("Use", "use.md", "Inspect the server deployment run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
