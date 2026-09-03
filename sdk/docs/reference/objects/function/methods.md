# Function object

The `Function` object comes with CRUD methods, a run method, task methods, trigger methods, and kind specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

??? example "save"

    Save or update the function in the backend.

    ::: digitalhub.entities.function._base.entity.Function.save
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

    Export the function locally as a YAML file.

    ::: digitalhub.entities.function._base.entity.Function.export
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

    Refresh the function from the backend.

    ::: digitalhub.entities.function._base.entity.Function.refresh
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

The `run()` method is used to execute the function. Its `extensions` parameter
adds extension dictionaries to the resulting `Run` object. Other keyword
arguments are passed to the run builder, including `inputs`, `parameters` and
runtime-specific options.

??? example "run"

    Execute the function.

    ::: digitalhub.entities.function._base.entity.Function.run
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

The function object exposes the following methods to manage tasks.

??? example "new_task"

    Create a task for an action.

    ::: digitalhub.entities.function._base.entity.Function.new_task
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

    ::: digitalhub.entities.function._base.entity.Function.get_task
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

    List the tasks related to the function.

    ::: digitalhub.entities.function._base.entity.Function.list_task
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

    Import serialized tasks and associate matching tasks with the function.

    ::: digitalhub.entities.function._base.entity.Function.import_tasks
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

    ::: digitalhub.entities.function._base.entity.Function.update_task
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

    ::: digitalhub.entities.function._base.entity.Function.set_task
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

    ::: digitalhub.entities.function._base.entity.Function.delete_task
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

The function object exposes the following methods to manage triggers.

??? example "trigger"

    Create a trigger for the function.

    ::: digitalhub.entities.function._base.entity.Function.trigger
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

    ::: digitalhub.entities.function._base.entity.Function.get_trigger
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

    List the triggers related to the function.

    ::: digitalhub.entities.function._base.entity.Function.list_triggers
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

Methods specific to a function kind are documented in the reference documentation of the corresponding runtime.
