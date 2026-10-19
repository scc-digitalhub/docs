---
render_macros: true
---

# Hera runtime

Use Hera to define workflows and run them on the platform. A pipeline function returns a Hera `Workflow`; see the [pipeline definition guide](define-pipeline.md) for the DSL helpers and handler requirements.

{{ runtime_prerequisites("digitalhub-runtime-hera") }}

{{ runtime_actions([
    ("Build", "hera-build/action.md", "Compile a Hera Workflow into Argo Workflows YAML."),
    ("Pipeline", "hera-pipeline/action.md", "Execute a Hera workflow, optionally building it first."),
]) }}

{{ runtime_examples("Explore examples for defining, building and running Hera workflows.") }}
