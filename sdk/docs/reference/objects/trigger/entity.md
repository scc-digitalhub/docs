# Trigger

Triggers are the logical description of how and when jobs should be executed on the platform. A trigger controls the scheduling and execution of tasks, defining when and under what conditions they should run. This can include time-based scheduling, event-driven execution, or other triggering mechanisms.

## Choose a trigger kind

Choose the kind that matches when the trigger should run. The `kind` to use is shown at the end of the card description.

<div class="list-cards" markdown>

- [**Scheduler**](./kind/scheduler.md){ .list-card-link } - Run a task on a cron schedule - `scheduler`

- [**Lifecycle**](./kind/lifecycle.md){ .list-card-link } - Run a task when an entity reaches selected states - `lifecycle`

</div>

## Trigger operations

<div class="grid cards" markdown>

- [**Trigger CRUD**](./crud.md){ .card-link }

	---

	Create, read, update, or delete triggers.

- [**Use the Trigger entity**](./methods.md){ .card-link }

	---

	Save, stop, export, and refresh trigger entities.

</div>

## Creating Triggers from Functions and Workflows

Triggers can be created directly from Function and Workflow objects using their `trigger()` method. This provides a convenient way to set up triggers for specific functions or workflows.

Example using a Function:

```python
function = project.get_function("my-function")

# Create a scheduler trigger
trigger = function.trigger(
    action="job",
    kind="scheduler",
    name="daily-function-run",
    schedule="0 0 * * * ?"  # Run daily at midnight
)

# Create a lifecycle trigger when an artifact is uploaded
trigger = function.trigger(
    action="job",
    kind="lifecycle",
    name="validate-on-upload",
    key="store://project/artifact/*",
    states=["READY"],
    template={"inputs": {"my-param": "{{input.key}}"}},
)
```

Example using a Workflow:

```python
workflow = project.get_workflow("my-workflow")

# Create a scheduler trigger
trigger = workflow.trigger(
    action="pipeline",
    kind="scheduler",
    name="weekly-workflow-run",
    schedule="0 0 * * 0 ?"  # Run weekly on Sunday
)

# Create a lifecycle trigger
trigger = workflow.trigger(
    action="pipeline",
    kind="lifecycle",
    name="validation-pipeline-on-upload",
    key="store://project/artifact/*",
    states=["READY"],
    template={"parameters": {"param-name": "{{input.key}}"}},
)
```

[Back to Entities](../index.md)
