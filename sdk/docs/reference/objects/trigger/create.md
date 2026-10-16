---
render_macros: true
---

# Create a trigger

Choose a trigger kind based on when it should run. Each kind page documents the corresponding `new_trigger()` example and its specification.

## Choose a trigger kind

{{ kind_cards([
    ("Scheduler", "./kind/scheduler.md", "Run a task on a cron schedule", "scheduler"),
    ("Lifecycle", "./kind/lifecycle.md", "Run a task when an entity reaches selected states", "lifecycle"),
]) }}

## Create from a function or workflow

Functions and workflows also provide a `trigger()` method for creating triggers in their execution context.

??? example "Function.trigger()"

    ```python
    function = project.get_function("my-function")

    trigger = function.trigger(
        action="job",
        kind="scheduler",
        name="daily-function-run",
        schedule="0 0 * * * ?",
    )

    trigger = function.trigger(
        action="job",
        kind="lifecycle",
        name="validate-on-upload",
        key="store://project/artifact/*",
        states=["READY"],
        template={"inputs": {"my-param": "{% raw %}{{input.key}}{% endraw %}"}},
    )
    ```

??? example "Workflow.trigger()"

    ```python
    workflow = project.get_workflow("my-workflow")

    trigger = workflow.trigger(
        action="pipeline",
        kind="scheduler",
        name="weekly-workflow-run",
        schedule="0 0 * * 0 ?",
    )

    trigger = workflow.trigger(
        action="pipeline",
        kind="lifecycle",
        name="validation-pipeline-on-upload",
        key="store://project/artifact/*",
        states=["READY"],
        template={"parameters": {"param-name": "{% raw %}{{input.key}}{% endraw %}"}},
    )
    ```

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
