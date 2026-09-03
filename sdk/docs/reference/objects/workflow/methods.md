# Workflow object

The `Workflow` object comes with CRUD methods, a run method, task methods, trigger methods, and kind specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

??? example "save"

    Save or update the workflow in the backend.

    ::: digitalhub.entities.workflow._base.entity.Workflow.save
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "export"

    Export the workflow locally as a YAML file.

    ::: digitalhub.entities.workflow._base.entity.Workflow.export
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "refresh"

    Refresh the workflow from the backend.

    ::: digitalhub.entities.workflow._base.entity.Workflow.refresh
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Run method

The `run()` method is used to execute the workflow. Its `extensions` parameter
adds extension dictionaries to the resulting `Run` object. Other keyword
arguments are passed to the run builder, including `inputs`, `parameters` and
runtime-specific options.

??? example "run"

    Execute the workflow.

    ::: digitalhub.entities.workflow._base.entity.Workflow.run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Task methods

The workflow object exposes the following methods to manage tasks.

??? example "new_task"

    Create a task for an action.

    ::: digitalhub.entities.workflow._base.entity.Workflow.new_task
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "get_task"

    Get the task for an action.

    ::: digitalhub.entities.workflow._base.entity.Workflow.get_task
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "list_task"

    List the tasks related to the workflow.

    ::: digitalhub.entities.workflow._base.entity.Workflow.list_task
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "import_tasks"

    Import serialized tasks and associate matching tasks with the workflow.

    ::: digitalhub.entities.workflow._base.entity.Workflow.import_tasks
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "update_task"

    Update the task for an action.

    ::: digitalhub.entities.workflow._base.entity.Workflow.update_task
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "set_task"

    Create or replace the task for an action.

    ::: digitalhub.entities.workflow._base.entity.Workflow.set_task
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "delete_task"

    Delete the task for an action.

    ::: digitalhub.entities.workflow._base.entity.Workflow.delete_task
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Trigger methods

The workflow object exposes the following methods to manage triggers.

??? example "trigger"

    Create a trigger for the workflow.

    ::: digitalhub.entities.workflow._base.entity.Workflow.trigger
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "get_trigger"

    Get a trigger by identifier.

    ::: digitalhub.entities.workflow._base.entity.Workflow.get_trigger
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "list_triggers"

    List the triggers related to the workflow.

    ::: digitalhub.entities.workflow._base.entity.Workflow.list_triggers
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Kind specific methods

Methods specific to a workflow kind are documented in the reference documentation of the corresponding runtime.
