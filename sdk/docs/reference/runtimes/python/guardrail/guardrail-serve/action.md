---
render_macros: true
---

# Guardrail Serve

Use the `serve` action to deploy a Guardrail function as a request/response processor.

## What the action does

The Guardrail service processes traffic according to its configured `processing_mode`. See the [shared handler guide](../../define-function.md#guardrail) for ExtProc processing phases and response behavior.

{{ overview_cards([
    ("Create", "create.md", "Define the Guardrail handler and its processing mode."),
    ("Run", "run.md", "Deploy the processor and configure its service."),
    ("Use", "use.md", "Inspect the deployed service and its run outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
