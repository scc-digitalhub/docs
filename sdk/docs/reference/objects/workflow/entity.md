---
render_macros: true
---

# Workflow

Workflows allow for organizing the single operations in a advanced management pipelines, to perform a series operation of data processing, ML model training and serving, etc. Workflows represent long-running procedures defined as Directed Acyclic Graphs (DAGs) where each node is a single unit of work performed by the platform (e.g., as a Kubernetes Job).

## Choose a workflow kind

Choose the runtime that matches the workflow you want to create. The `kind` to use is shown at the end of the card description.

<div class="list-cards" markdown>

- [**Hera**](../../runtimes/hera/overview.md){ .list-card-link } - Build workflows with Hera pipelines - `hera`

</div>

{{ entity_overview_cards("workflow") }}

[Back to Entities](../index.md)
