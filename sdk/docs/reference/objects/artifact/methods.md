# Artifact object

The `Artifact` object comes with three sets of methods: CRUD methods, I/O methods and kind specific methods.

## CRUD methods

Crud methods are used to interact with the entity object in the backend or locally.

??? example "save"

    Save or update the artifact in the backend.

    ::: digitalhub.entities.artifact._base.entity.Artifact.save
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

    Export the artifact locally as a YAML file.

    ::: digitalhub.entities.artifact._base.entity.Artifact.export
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

    Refresh the artifact from the backend.

    ::: digitalhub.entities.artifact._base.entity.Artifact.refresh
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

??? example "as_file"

    Download the artifact into a local temporary destination.

    ::: digitalhub.entities.artifact._base.entity.Artifact.as_file
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "download"

    Download the artifact into a specified path.

    ::: digitalhub.entities.artifact._base.entity.Artifact.download
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "upload"

    Upload the artifact to its specification path.

    ::: digitalhub.entities.artifact._base.entity.Artifact.upload
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

Methods specific to an artifact kind are documented in the corresponding kind reference page, such as the [artifact kind reference](kind/artifact.md).
