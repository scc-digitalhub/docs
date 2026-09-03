# Secret object

The `Secret` object comes with two sets of methods: CRUD methods and read/write methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

??? example "save"

    Save or update the secret in the backend.

    ::: digitalhub.entities.secret._base.entity.Secret.save
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

    Export the secret locally as a YAML file.

    ::: digitalhub.entities.secret._base.entity.Secret.export
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

    Refresh the secret from the backend.

    ::: digitalhub.entities.secret._base.entity.Secret.refresh
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## I/O methods

I/O methods are used to handle objects as files.

??? example "set_secret_value"

    Set or update the secret value.

    ::: digitalhub.entities.secret._base.entity.Secret.set_secret_value
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "read_secret_value"

    Read the secret value.

    ::: digitalhub.entities.secret._base.entity.Secret.read_secret_value
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
