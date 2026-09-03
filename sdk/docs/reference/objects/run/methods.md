# Run object

The `Run` object comes with three sets of methods: CRUD methods, generic run methods and (eventual) kind specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

??? example "save"

    Save or update the run in the backend.

    ::: digitalhub.entities.run._base.entity.Run.save
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

    Export the run locally as a YAML file.

    ::: digitalhub.entities.run._base.entity.Run.export
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

    Refresh the run from the backend.

    ::: digitalhub.entities.run._base.entity.Run.refresh
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

There are several generic run methods on the `Run` object.

??? example "run"

    Start the run.

    ::: digitalhub.entities.run._base.entity.Run.run
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "wait"

    Wait for the run to finish.

    ::: digitalhub.entities.run._base.entity.Run.wait
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "stop"

    Stop the run.

    ::: digitalhub.entities.run._base.entity.Run.stop
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "resume"

    Resume the run.

    ::: digitalhub.entities.run._base.entity.Run.resume
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "logs"

    Get the logs for the run.

    ::: digitalhub.entities.run._base.entity.Run.logs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "log_metric"

    Log a metric in the run.

    ::: digitalhub.entities.run._base.entity.Run.log_metric
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "log_metrics"

    Log multiple metrics in the run.

    ::: digitalhub.entities.run._base.entity.Run.log_metrics
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

Run kinds are provided by runtimes. See the [runtime documentation](../../runtimes/index.md) for the corresponding runtime behavior.
