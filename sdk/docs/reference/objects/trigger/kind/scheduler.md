---
render_macros: true
---

# Scheduler

The `scheduler` kind runs a task on a recurring schedule defined by a Quartz cron expression.

## Scheduler spec

The `scheduler` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `task` | *str* | Task to execute. | *required* |
| `template` | *dict* | Configuration template for the run. | `{}` |
| `function` | *str \| None* | Function to execute. Provide this or `workflow`. | `None` |
| `workflow` | *str \| None* | Workflow to execute. Provide this or `function`. | `None` |
| `schedule` | *str* | Quartz cron expression. | *required* |

## Create

### New

{% call function_doc("new_trigger", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        trigger = dh.new_trigger(
            project="my-project",
            name="daily-run",
            kind="scheduler",
            task="store://my-project/task/my-task:latest",
            function="store://my-project/function/my-function:latest",
            schedule="0 0 * * * ?",
        )
        ```
{% endcall %}

## Methods

The `scheduler` kind adds no instance methods. See [Use a trigger](../use.md) for common methods.

[Back to trigger kind selection](../create.md)
