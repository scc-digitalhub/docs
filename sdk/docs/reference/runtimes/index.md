# Runtimes

Functions are the logical description of something that the platform may execute and track for you. A function may represent code to run as a job, an ML model inference to be used as batch procedure or as a service, a data validation, etc.

In the platform we perform actions over functions (also referred to as "tasks"), such as job execution, deploy, container image build. A single action execution is called run, and the platform keeps track of these runs, with metadata about function version, operation parameters, and runtime parameters for a single execution.

They are associated with a given runtime, which implements the actual execution and determines which actions are available. Examples are DBT, Container, Python, etc. Runtimes are highly specialized components that translate the representation of a given execution (as expressed in the run) into an actual operation performed via libraries, code, or external tools.

Runtimes define the key point of extension of the platform: new runtimes may be added to implement the low-level logic of "translating" the high-level operation definition into an executable run. For example, the DBT runtime allows defining a transformation as a task that, given an input table reference, produces a dataset applying the SQL-defined function. In this case the runtime converts the specification and references into a Kubernetes Job that runs the DBT transformation and stores the resulting dataset.

## Supported runtimes

- [Python](python/python/overview.md) — Python-based functions, including `python`, `guardrail`, and `openinference` kinds.
- [Container](container/overview.md) — run arbitrary container images as jobs or services.
- [DBT](dbt/overview.md) — run DBT transformations for data modeling.
- [Hera](hera/overview.md) — Hera pipelines runtime (DAG/steps orchestration).
- [ModelServe](modelserve/overview.md) — model serving and inference workloads.
- [Flower](flower/overview.md) — federated learning with Flower framework.
