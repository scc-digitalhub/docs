# Trigger object

The `Trigger` object comes with CRUD methods and trigger-specific methods.

## CRUD methods

CRUD methods are used to interact with the entity object in the backend or locally:

- `save()`: Save or update the entity into the backend
- `export()`: Export the entity locally as yaml file
- `refresh()`: Refresh (read) the entity from the backend

::: digitalhub.entities.trigger._base.entity.Trigger.save
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.trigger._base.entity.Trigger.export
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub.entities.trigger._base.entity.Trigger.refresh
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Trigger methods

The trigger object exposes the following method:

- `stop()`: Stop the trigger.

::: digitalhub.entities.trigger._base.entity.Trigger.stop
    options:
        heading_level: 3
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Trigger Specifications

The trigger object has specific attributes based on its kind:

### Base Trigger

All triggers have these base specifications:

- `template`: Configuration template for the run (dict with parameters/inputs, resources, etc.)
- `task`: The task to execute
- `function` or `workflow`: The target process to execute (either a function or workflow)

### Scheduler Trigger

Additional specifications:

- `schedule`: Quartz cron expression

### Lifecycle Trigger

Additional specifications:

- `key`: Entity key to monitor (format: `store://<project>/<entity-type>/<entity-kind>/<name>`, can include wildcards `*`)
- `states`: List of states of the monitored entity that will trigger execution

For more details about trigger kinds and their specific configurations, see the [kinds section](kinds.md).

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
    schedule="0 0 * * *"  # Run daily at midnight
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
    schedule="0 0 * * 0"  # Run weekly on Sunday
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
