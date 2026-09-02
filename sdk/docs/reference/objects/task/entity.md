# Tasks

A `Task` represents one executable action associated with a Function or Workflow. Tasks contain the action-specific configuration, such as runtime parameters, Kubernetes resources, volumes, environment variables and referenced secrets.

Tasks are normally created automatically by `Function.run()` or `Workflow.run()`, but they can also be managed as entities with the SDK CRUD methods.

1. In the [CRUD section](./crud.md), see how to create, read, update and delete tasks.
2. In the [methods section](./methods.md), see how to execute a task and manage its runs.
3. In the [kinds section](./kinds.md), see how task kinds are derived from executable actions.
