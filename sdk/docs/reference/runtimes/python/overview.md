---
render_macros: true
---

# Python runtime

The Python runtime executes user-defined Python functions for general-purpose jobs and services.

{{ runtime_prerequisites("digitalhub-runtime-python") }}

{{ runtime_actions([
    ("Job", "python-job/action.md", "Execute a Python function as a one-off task."),
    ("Serve", "python-serve/action.md", "Deploy a Python function as an HTTP service."),
    ("Build", "python-build/action.md", "Build a container image for a Python function."),
]) }}

{{ runtime_examples("Explore examples for Python jobs, services and builds.") }}
