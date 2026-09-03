# Task object

The `Task` object provides CRUD methods inherited from its entity base class and methods for managing runs.

## CRUD methods

??? example "save"

    Save or update the task in the backend.

    ::: digitalhub.entities.task._base.entity.Task.save
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

    Export the task locally as a YAML file.

    ::: digitalhub.entities.task._base.entity.Task.export
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

    Refresh the task from the backend.

    ::: digitalhub.entities.task._base.entity.Task.refresh
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Run methods

??? example "run"

    Start a run for the task.

    ::: digitalhub.entities.task._base.entity.Task.run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "new_run"

    Create a run for the task.

    ::: digitalhub.entities.task._base.entity.Task.new_run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "get_run"

    Get the run associated with the task.

    ::: digitalhub.entities.task._base.entity.Task.get_run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "delete_run"

    Delete the run associated with the task.

    ::: digitalhub.entities.task._base.entity.Task.delete_run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Task kinds

Task kinds are provided by runtimes. See the [runtime documentation](../../runtimes/index.md) for the corresponding runtime behavior.
