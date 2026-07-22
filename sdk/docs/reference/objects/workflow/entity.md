# Workflow

Workflows allow for organizing the single operations in a advanced management pipelines, to perform a series operation of data processing, ML model training and serving, etc. Workflows represent long-running procedures defined as Directed Acyclic Graphs (DAGs) where each node is a single unit of work performed by the platform (e.g., as a Kubernetes Job).

## Managing workflows with SDK

Workflows can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.

1. In the [CRUD section](./crud.md), we will see how to create, read, update and delete workflows.
2. In the [methods section](./methods.md), we will see what can be done with the `Workflow` object.
3. In the [kinds section](./kinds.md), we will see what kinds are supported.
