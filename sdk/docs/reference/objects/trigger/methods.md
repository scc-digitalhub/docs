# Trigger object

The `Trigger` object comes with CRUD methods and trigger-specific methods.

## CRUD methods

CRUD methods are used to interact with the entity object in the backend or locally:

??? example "save"

    Save or update the trigger in the backend.

    ::: digitalhub.entities.trigger._base.entity.Trigger.save
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

    Export the trigger locally as a YAML file.

    ::: digitalhub.entities.trigger._base.entity.Trigger.export
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

    Refresh the trigger from the backend.

    ::: digitalhub.entities.trigger._base.entity.Trigger.refresh
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

The trigger object exposes the following method:

??? example "stop"

    Stop the trigger.

    ::: digitalhub.entities.trigger._base.entity.Trigger.stop
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Trigger kinds

Trigger specifications are documented in the [scheduler kind](kind/scheduler.md) and [lifecycle kind](kind/lifecycle.md) references.
