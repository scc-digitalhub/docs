# CRUD

The CRUD methods are used to create, read, update and delete artifacts. There are two ways to use them.
The first is through the SDK and the second is through the `Project` object.
The syntax is the same for all CRUD methods. If you want to manage artifacts from the project, you can use the `Project` object and avoid specifying the `project` parameter. In this case, specify every parameter as a keyword argument.

## Create

Creation methods differ in how they handle the source:

- `new_artifact()` creates and saves an entity.
- `log_<kind>()` creates an entity and uploads the source to an artifact store.
- `register_<kind>()` creates an entity for an existing source; `name` is optional and can be inferred from the source.

For specification parameters, see the documentation for the relevant [artifact kind](kind/artifact.md). Use the generic methods only for a kind supported by DigitalHub Core but not by the SDK.

??? example "new_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_artifact

    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.new_artifact(
            project="my-project",
            name="my-artifact",
            kind="artifact",
            path="s3://my-bucket/my-artifact",
        )
        ```

??? example "log_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_artifact

    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.log_artifact(
            project="my-project",
            name="my-artifact",
            source="./local-artifact",
        )
        ```

??? example "log_generic_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_generic_artifact

    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.log_generic_artifact(
            project="my-project",
            kind="custom-artifact",
            source="./local-artifact",
            name="my-artifact",
        )
        ```

??? example "register_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_artifact

    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.register_artifact(
            project="my-project",
            source="s3://my-bucket/my-artifact",
            name="my-artifact",
        )
        ```

??? example "register_generic_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_generic_artifact

    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.register_generic_artifact(
            project="my-project",
            kind="custom-artifact",
            source="s3://my-bucket/my-artifact",
            name="my-artifact",
        )
        ```

## Read

Use the read methods to retrieve artifacts from the backend or load them from a YAML descriptor.

??? example "get_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_artifact

    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.get_artifact(
            identifier="my-artifact",
            project="my-project",
        )
        ```

??? example "get_artifact_versions"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_artifact_versions

    === "Example"

        ```python
        import digitalhub as dh

        artifacts = dh.get_artifact_versions(
            identifier="my-artifact",
            project="my-project",
        )
        ```

??? example "list_artifacts"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_artifacts

    === "Example"

        ```python
        import digitalhub as dh

        artifacts = dh.list_artifacts(project="my-project")
        ```

??? example "import_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_artifact

    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.import_artifact("my-artifact.yaml")
        ```

??? example "load_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - load_artifact

    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.load_artifact("my-artifact.yaml")
        ```

## Update

Update an artifact after changing its mutable metadata.

??? example "update_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_artifact

    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.get_artifact(
            identifier="my-artifact",
            project="my-project",
        )
        artifact.set_description("Updated artifact")
        artifact = dh.update_artifact(artifact)
        ```

## Delete

Delete one artifact version or all versions of an artifact.

??? example "delete_artifact"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_artifact

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_artifact(
            identifier="my-artifact",
            project="my-project",
            delete_all_versions=True,
        )
        ```
