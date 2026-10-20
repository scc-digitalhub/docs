---
render_macros: true
---

# Python Build

Use the `build` action to create a container image for a Python function and its dependencies.

## What the action does

Build instructions are added as `RUN` instructions to the generated Dockerfile. The resulting image can be used by Job or Serve runs.

{{ overview_cards([
    ("Create", "create.md", "Define the Python function source, handler and dependencies."),
    ("Run", "run.md", "Build the image and customize Dockerfile instructions."),
    ("Use", "use.md", "Retrieve the generated image and build run outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
