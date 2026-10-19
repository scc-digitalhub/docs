---
render_macros: true
---

# Guardrail Build

Use the `build` action to create an image containing the Guardrail handler and its dependencies.

## What the action does

The built image can be deployed as a request/response processor using the Envoy Proxy ExtProc protocol.

{{ overview_cards([
    ("Create", "create.md", "Define the Guardrail handler and its processing mode."),
    ("Run", "run.md", "Build the image and customize Dockerfile instructions."),
    ("Use", "use.md", "Retrieve the generated image and build run outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
