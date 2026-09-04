# CRUD

The CRUD methods create, read, update and delete secrets. They can be called directly from the SDK or through a `Project` object.
The syntax is the same for all CRUD methods. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument.

## Create

`new_secret()` creates and saves a project-level secret. Secret values are managed separately from the entity metadata. For specification parameters, see the [secret kind](kind/secret.md) reference.

??? example "new_secret"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_secret

    === "Creation example"

        ```python
        import digitalhub as dh

        secret = dh.new_secret(
            project="my-project",
            name="my-secret",
            secret_value="my-secret-value",
        )
        ```

## Read

Use the read methods to retrieve secrets from the backend or load them from a YAML descriptor.

??? example "get_secret"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_secret

    === "Example"

        ```python
        import digitalhub as dh

        secret = dh.get_secret(
            identifier="my-secret",
            project="my-project",
        )
        ```

??? example "list_secrets"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_secrets

    === "Example"

        ```python
        import digitalhub as dh

        secrets = dh.list_secrets(project="my-project")
        ```

??? example "import_secret"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_secret

    === "Example"

        ```python
        import digitalhub as dh

        secret = dh.import_secret("my-secret.yaml")
        ```

## Update

Update a secret after changing its mutable metadata.

??? example "update_secret"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_secret

    === "Example"

        ```python
        import digitalhub as dh

        secret = dh.get_secret(
            identifier="my-secret",
            project="my-project",
        )
        secret.set_description("Updated secret")
        secret = dh.update_secret(secret)
        ```

## Delete

Delete one secret version or all versions of a secret.

??? example "delete_secret"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_secret

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_secret(
            identifier="my-secret",
            project="my-project",
            delete_all_versions=True,
        )
        ```
