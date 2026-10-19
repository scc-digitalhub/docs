---
render_macros: true
---

# Hydra runtime

Use Hydra to configure Python applications and run them as jobs or build an execution image with their dependencies.

{{ runtime_prerequisites("digitalhub-runtime-hydra") }}

Hydra execution supports Python versions `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, and `PYTHON3_13`.

{{ runtime_actions([
    ("Job", "hydra-job/action.md", "Execute a Hydra function as a one-off multirun job."),
    ("Build", "hydra-build/action.md", "Build an execution image for a Hydra function."),
]) }}

{{ runtime_examples("Explore complete examples for Hydra jobs and builds.") }}
