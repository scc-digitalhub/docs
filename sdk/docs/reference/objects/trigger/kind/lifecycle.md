---
render_macros: true
---

# Lifecycle

The `lifecycle` kind runs a task when a monitored entity reaches one of the configured states.

## Lifecycle spec

The `lifecycle` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `task` | *str* | Task to execute. | *required* |
| `template` | *dict* | Configuration template for the run. | `{}` |
| `function` | *str \| None* | Function to execute. Provide this or `workflow`. | `None` |
| `workflow` | *str \| None* | Workflow to execute. Provide this or `function`. | `None` |
| `key` | *str* | Entity key to monitor. It can include wildcards such as `*`. | *required* |
| `states` | *list[str]* | States of the monitored entity that trigger execution. | *required* |

## Create

### New

{% call function_doc("new_trigger", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        trigger = dh.new_trigger(
            project="my-project",
            name="model-complete",
            kind="lifecycle",
            task="store://my-project/task/my-task:latest",
            function="store://my-project/function/my-function:latest",
            key="store://my-project/model/*",
            states=["COMPLETED"],
        )
        ```
{% endcall %}

## Methods

The `lifecycle` kind adds no instance methods. See [Use a trigger](../use.md) for common methods.

[Back to trigger kind selection](../create.md)
