---
render_macros: true
---

# Guardrail runtime

Guardrail functions are Python handlers for request and response processing using the [Envoy Proxy ExtProc protocol](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/ext_proc/v3/ext_proc.proto). The required `processing_mode` selects which request or response stages the handler processes. Handler behavior is described in the shared [Python function guide](../define-function.md#guardrail).

{{ runtime_prerequisites("digitalhub-runtime-python", "../../../../how-to/installation.md") }}

{{ runtime_actions([
    ("Serve", "guardrail-serve/action.md", "Deploy a Guardrail function as a request/response processor."),
    ("Build", "guardrail-build/action.md", "Build a container image for a Guardrail function."),
]) }}

{{ runtime_examples("Explore examples for Guardrail builds and request/response processing.") }}
