# Tasks

A `Task` represents one executable action associated with a Function or Workflow. Tasks contain the action-specific configuration, such as runtime parameters, Kubernetes resources, volumes, environment variables and referenced secrets.

Tasks are normally created automatically by `Function.run()` or `Workflow.run()`, but they can also be managed as entities with the SDK CRUD methods.

Task kinds are derived from the executable kind and action provided by a runtime. See the [runtime documentation](../../runtimes/index.md) to create and configure a task.

## Task operations

<div class="grid cards" markdown>

- [**Task CRUD**](./crud.md){ .card-link }

	---

	Create, read, update, or delete tasks.

- [**Use the Task entity**](./methods.md){ .card-link }

	---

	Execute tasks and manage their runs.

</div>

[Back to Entities](../index.md)
