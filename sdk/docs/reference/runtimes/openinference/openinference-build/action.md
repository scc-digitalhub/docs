---
render_macros: true
---

# OpenInference Build

Use the `build` action to create an image containing the OpenInference handler and its dependencies.

## What the action does

The function's model metadata and tensor schemas remain part of its specification; the build packages the handler for execution.

{{ overview_cards([
    ("Create", "create.md", "Define the inference handler, model name and tensor schemas."),
    ("Run", "run.md", "Build the image and customize Dockerfile instructions."),
    ("Use", "use.md", "Retrieve the generated image and build run outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
