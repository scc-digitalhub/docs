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

## Scheduler methods

The `scheduler` kind has no additional methods.
