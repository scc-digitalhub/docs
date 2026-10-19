---
render_macros: true
---

# OpenInference runtime

OpenInference functions are Python handlers for inference services. Their function specification declares a model name and the tensor schemas accepted by the endpoint. Handler behavior is described in the shared [Python function guide](../define-function.md).

{{ runtime_prerequisites("digitalhub-runtime-python", "../../../../how-to/installation.md") }}

{{ runtime_actions([
    ("Serve", "openinference-serve/action.md", "Deploy an OpenInference function as an inference service."),
    ("Build", "openinference-build/action.md", "Build a container image for an OpenInference function."),
]) }}

{{ runtime_examples("Explore examples for OpenInference builds and inference services.") }}
