---
render_macros: true
---

# Ray runtime

Use Ray to execute Python applications on dynamically created Ray clusters.

{{ runtime_prerequisites("digitalhub-runtime-ray") }}

{{ runtime_actions([
    ("Job", "ray-job/action.md", "Execute a Ray function as a one-off job on a Ray cluster."),
    ("Build", "ray-build/action.md", "Build an execution image for a Ray function."),
]) }}

{{ runtime_examples("Explore complete examples for Ray jobs and builds.") }}
