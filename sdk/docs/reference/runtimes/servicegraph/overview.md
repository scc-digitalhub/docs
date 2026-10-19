---
render_macros: true
---

# ServiceGraph runtime

Use [ServiceGraph](https://github.com/scc-digitalhub/digitalhub-servicegraph) YAML pipeline definitions to orchestrate AI services and streaming data processing.

{{ runtime_prerequisites("digitalhub-runtime-servicegraph") }}

{{ runtime_actions([
    ("Serve", "servicegraph-serve/action.md", "Deploy a synchronous or streaming ServiceGraph pipeline."),
]) }}

{{ runtime_examples("Explore YAML pipelines, synchronous requests and streaming services.") }}
