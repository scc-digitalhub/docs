---
render_macros: true
---

# Flower Server Deploy

Use the `deploy` action to deploy a Flower server that coordinates federated-learning clients.

## What the action does

The server manages client communications and training rounds. If the Function has no image and `auto_build=True`, the runtime builds the image before deployment.

{{ overview_cards([
    ("Create", "create.md", "Configure the Flower server image and dependencies."),
    ("Run", "run.md", "Deploy the server and configure authentication."),
    ("Use", "use.md", "Inspect the server deployment run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
