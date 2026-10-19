---
render_macros: true
---

# Flower runtime

Use Flower to run federated-learning simulations or build and deploy Flower client and server applications.

{{ runtime_prerequisites("digitalhub-runtime-flower") }}

{{ runtime_actions([
    ("App train", "flower-app-train/action.md", "Run a Flower application as a federated-learning simulation."),
    ("Client build", "flower-client-build/action.md", "Build a deployable Flower client image."),
    ("Client deploy", "flower-client-deploy/action.md", "Deploy a Flower client to a federation."),
    ("Server build", "flower-server-build/action.md", "Build a deployable Flower server image."),
    ("Server deploy", "flower-server-deploy/action.md", "Deploy a Flower server to coordinate clients."),
]) }}

{{ runtime_examples("Explore complete examples for Flower simulations, clients and servers.") }}
