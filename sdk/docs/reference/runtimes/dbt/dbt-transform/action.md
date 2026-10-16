---
render_macros: true
---

# DBT Transform

Use this action to run a dbt transformation and publish its output as a table Dataitem.

## What the action does

The `transform` action executes a dbt transformation using the DBT runtime. At a high level:

1. Collects input material entities and materializes them as versioned tables in the configured PostgreSQL database
2. Collects the SQL source and generates the dbt project files and configuration
3. Runs `dbt run --select <output_table>`
4. Creates one table Dataitem for the resulting table

{{ overview_cards([
    ("Create", "create.md", "Create a dbt function."),
    ("Run", "run.md", "Run with method `run()`."),
    ("Use", "use.md", "Inspect the run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
