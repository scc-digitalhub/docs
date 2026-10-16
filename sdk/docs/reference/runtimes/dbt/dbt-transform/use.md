---
render_macros: true
---

# Use a DBT Run

Once `function.run()` returns, use the Run object to inspect its inputs and access the produced table Dataitem.

??? example "inputs"

    Get the inputs passed to the Run.

    ::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.inputs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "output"

    Get a Run output by name.

    ::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.output
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "outputs"

    Get the outputs produced by the Run.

    ::: digitalhub_runtime_dbt.entities.run.transform.entity.RunDbtRun.outputs
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
