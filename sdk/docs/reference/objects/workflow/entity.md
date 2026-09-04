# Workflow

Workflows allow for organizing the single operations in a advanced management pipelines, to perform a series operation of data processing, ML model training and serving, etc. Workflows represent long-running procedures defined as Directed Acyclic Graphs (DAGs) where each node is a single unit of work performed by the platform (e.g., as a Kubernetes Job).

## Choose a workflow kind

Choose the runtime that matches the workflow you want to create. The `kind` to use is shown at the end of the card description.

<div class="list-cards" markdown>

- [**Hera**](../../runtimes/hera/overview.md){ .list-card-link } - Build workflows with Hera pipelines - `hera`

</div>

## Managing workflows with SDK

Workflows can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.

<div class="grid cards" markdown>

- [**Workflow CRUD**](./crud.md){ .card-link }

	---

	Create, read, update, or delete workflows.

- [**Use the Workflow entity**](./methods.md){ .card-link }

	---

	Run workflows and manage their tasks and triggers.

</div>

[Back to Entities](../index.md)
