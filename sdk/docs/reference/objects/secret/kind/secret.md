# Secret

The `secret` kind stores a project-level sensitive value through the configured secret provider. Secret values are managed separately from the entity metadata.

## Secret spec

The `secret` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | *str \| None* | Path to the secret. | `None` |
| `provider` | *str \| None* | Secret provider. | `None` |

## Secret methods

The `secret` kind exposes the standard entity methods and methods for managing secret values.

### CRUD methods

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

### Secret value methods

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
