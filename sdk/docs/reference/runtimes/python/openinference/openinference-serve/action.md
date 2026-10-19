---
render_macros: true
---

# OpenInference Serve

Use the `serve` action to deploy an OpenInference function as an inference service.

## What the action does

The inference endpoint uses the model name and tensor schemas declared in the function specification. Requests and responses follow the Open Inference Protocol.

{{ overview_cards([
    ("Create", "create.md", "Define the inference handler, model name and tensor schemas."),
    ("Run", "run.md", "Deploy the service and configure its replicas."),
    ("Use", "use.md", "Invoke the endpoint with a tensor-oriented request payload."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
