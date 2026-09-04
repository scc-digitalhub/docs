# Function

Functions are the logical description of something that the platform may execute and track for you. A function may represent code to run as a job, an ML function inference to be used as batch procedure or as a service, a data validation, etc.

## Choose a function kind

Choose the runtime that matches the function you want to create. The `kind` to use is shown at the end of each card description.

<div class="list-cards" markdown>

- [**Python**](../../runtimes/python/python/overview.md){ .list-card-link } - Create functions with the Python runtime - `python`

- [**Container**](../../runtimes/container/overview.md){ .list-card-link } - Run functions packaged in a container image - `container`

- [**Model serving**](../../runtimes/modelserve/overview.md){ .list-card-link } - Serve trained models through a model serving runtime - `modelserve`

- [**DBT**](../../runtimes/dbt/overview.md){ .list-card-link } - Run dbt projects as functions - `dbt`

- [**Federated learning**](../../runtimes/flower/overview.md){ .list-card-link } - Build federated learning functions with Flower - `flower`

- [**Guardrail**](../../runtimes/python/guardrail/overview.md){ .list-card-link } - Define guardrail functions with the Python runtime - `guardrail`

- [**OpenInference**](../../runtimes/python/openinference/overview.md){ .list-card-link } - Use OpenInference with the Python runtime - `openinference`

</div>

## Managing functions with SDK

Functions can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.

<div class="grid cards" markdown>

- [**Function CRUD**](./crud.md){ .card-link }

	---

	Create, read, update, or delete functions.

- [**Use the Function entity**](./methods.md){ .card-link }

	---

	Run functions and manage their tasks and triggers.

</div>

[Back to Entities](../index.md)
