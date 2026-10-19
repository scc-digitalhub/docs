---
render_macros: true
---

# Flower Application Train

Use the `train` action to execute a Flower application that defines both client and server components.

## What the action does

The action runs the Flower application with `flwr run`. It supports execution on a remote platform or local Flower simulation. The application can be sourced from a Git repository or assembled from client and server source code.

{{ overview_cards([
    ("Create", "create.md", "Configure a Flower application and its client and server components."),
    ("Run", "run.md", "Configure federation, simulation and training parameters."),
    ("Use", "use.md", "Check whether the training run used local execution."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
