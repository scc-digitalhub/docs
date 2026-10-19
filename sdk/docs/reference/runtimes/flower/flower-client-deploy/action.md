---
render_macros: true
---

# Flower Client Deploy

Use the `deploy` action to deploy a Flower client that joins a federation and participates in training.

## What the action does

If the Function has no image and `auto_build=True`, the runtime builds the image before deployment.

{{ overview_cards([
    ("Create", "create.md", "Configure the Flower client image and dependencies."),
    ("Run", "run.md", "Deploy the client and configure its federation connection."),
    ("Use", "use.md", "Inspect the client deployment run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
