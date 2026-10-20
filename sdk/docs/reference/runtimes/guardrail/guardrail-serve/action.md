---
render_macros: true
---

# Guardrail Serve

Use the `serve` action to deploy a Guardrail function as a request/response processor.

## What the action does

The Guardrail service processes traffic according to its configured `processing_mode`. See the [Guardrail handler definition](../handler.md) for ExtProc processing phases and response behavior.

!!! warning "Build requirements first"
    If the Function has `requirements`, run the [Guardrail Build action](../guardrail-build/action.md) before deploying it so the dependencies are installed in its image.

{{ overview_cards([
    ("Create", "create.md", "Define the Guardrail handler and its processing mode."),
    ("Run", "run.md", "Deploy the processor and configure its service."),
    ("Use", "use.md", "Inspect the deployed service and its run outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
