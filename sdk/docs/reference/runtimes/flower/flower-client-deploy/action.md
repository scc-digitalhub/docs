---
render_macros: true
---

# Flower Client Deploy

Use the `deploy` action to deploy a Flower client that joins a federation and participates in training.

## What the action does

The deployment uses the image configured on the Flower client Function.

!!! warning "Build requirements first"
    If the Function has `requirements`, run the [Flower Client Build action](../flower-client-build/action.md) before deploying it so the dependencies are installed in its image.

{{ overview_cards([
    ("Create", "create.md", "Configure the Flower client image and dependencies."),
    ("Run", "run.md", "Deploy the client and configure its federation connection."),
    ("Use", "use.md", "Inspect the client deployment run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
