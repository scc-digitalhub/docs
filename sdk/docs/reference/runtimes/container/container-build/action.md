---
render_macros: true
---

# Container Build

Use the `build` action to generate a Dockerfile with custom instructions and build a container image.

## What the action does

The build action creates an execution image. When a job or service needs additional dependencies, build the image first, then use the same Function for the `job` or `serve` run.

{{ overview_cards([
    ("Create", "create.md", "Configure the Function with a base image and target image."),
    ("Run", "run.md", "Build an image with custom instructions."),
    ("Use", "use.md", "Continue using the built image with the same Function."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
