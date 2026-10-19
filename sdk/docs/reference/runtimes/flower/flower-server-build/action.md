---
render_macros: true
---

# Flower Server Build

Use the `build` action to package Flower server code and its dependencies into a deployable container image.

## What the action does

The resulting image can be used to deploy a Flower server that coordinates federated-learning clients.

{{ overview_cards([
    ("Create", "create.md", "Configure the Flower server source and image build."),
    ("Run", "run.md", "Build the server image and configure the build task."),
    ("Use", "use.md", "Retrieve the image produced by the build."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
