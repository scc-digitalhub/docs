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

## Lifecycle methods

The `lifecycle` kind has no additional methods.
