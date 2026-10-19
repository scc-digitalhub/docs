---
render_macros: true
---

# Container runtime

The Container runtime executes custom container images as jobs or long-lived services on Kubernetes. It can also build images with custom instructions.

{{ runtime_prerequisites("digitalhub-runtime-container") }}

{{ runtime_actions([
    ("Job", "container-job/action.md", "Execute a container to completion as a one-off job."),
    ("Serve", "container-serve/action.md", "Deploy a container as a long-lived service."),
    ("Build", "container-build/action.md", "Build a container image with custom instructions."),
]) }}

{{ runtime_examples("Explore complete examples for container jobs, builds and services.") }}
