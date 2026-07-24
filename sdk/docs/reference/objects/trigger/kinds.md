# Trigger kinds

At the moment, we support the following kinds:

- **`scheduler`** - Time-based trigger that uses cron expressions to schedule task execution
- **`lifecycle`** - Event-based trigger that responds to entity state changes

For each different kind, the `Trigger` object has its own subclass with different `spec` and `status` attributes.

## Scheduler Trigger

The scheduler trigger allows you to execute tasks on a schedule using cron expressions.

Required parameters:

- `task` - The task to execute
- `schedule` - Quartz cron expression
- One of:
  - `function` - The function to execute
  - `workflow` - The workflow to execute

Example:

```python
trigger = dh.new_trigger(
    project="my-project",
    name="daily-run",
    kind="scheduler",
    task="my-task",
    function="my-function",
    schedule="0 0 * * *"  # Run daily at midnight
)
```

## Lifecycle Trigger

The lifecycle trigger executes tasks in response to entity state changes.

Required parameters:

- `task` - The task to execute
- `key` - The entity key to monitor
- `states` - List of states to trigger on
- One of:
  - `function` - The function to execute
  - `workflow` - The workflow to execute

Example:

```python
trigger = dh.new_trigger(
    project="my-project",
    name="model-complete",
    kind="lifecycle",
    task="my-task",
    function="my-function",
    key="store://project/model/kind/name",
    states=["completed"]
)
```

Please see the [trigger entities](./entity.md) documentation for more details on creating and managing triggers.
