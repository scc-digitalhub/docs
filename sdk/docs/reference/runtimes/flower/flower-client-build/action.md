---
render_macros: true
---

# Flower Client Build

Use the `build` action to package Flower client code and its dependencies into a deployable container image.

## What the action does

The resulting image can be used to deploy a Flower client to a federation.

{{ overview_cards([
    ("Create", "create.md", "Configure the Flower client source and image build."),
    ("Run", "run.md", "Build the client image and configure the build task."),
    ("Use", "use.md", "Retrieve the image produced by the build."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
