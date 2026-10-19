---
render_macros: true
---

# DBT

Use DBT to run SQL transformations against project data. The `transform` action maps input Dataitems to dbt `ref()` calls and publishes the result as a table Dataitem.

{{ runtime_prerequisites("digitalhub-runtime-dbt") }}

{{ runtime_actions([
    ("Transform", "dbt-transform/action.md", "Run a dbt transformation and create a table Dataitem."),
]) }}

{{ runtime_examples("Explore complete examples for DBT runtime.") }}
