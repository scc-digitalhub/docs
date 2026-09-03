# CRUD

The CRUD methods create, read, update and delete models. They can be called directly from the SDK or through a `Project` object.
The syntax is the same for all CRUD methods. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument.

## Create

Creation methods differ in how they handle the source:

- `new_model()` creates and saves an entity.
- `log_<kind>()` creates an entity and uploads the source to a model store.
- `register_<kind>()` creates an entity for an existing source; `name` is optional and can be inferred from the source.

For specification parameters, see the documentation for the relevant [model kind](kind/model.md), [MLflow kind](kind/mlflow.md), [scikit-learn kind](kind/sklearn.md), [Hugging Face kind](kind/huggingface.md), [TVM IR kind](kind/tvm-ir.md), or [TVM SO kind](kind/tvm-so.md). Use the generic methods only for a kind supported by DigitalHub Core but not by the SDK.

??? example "new_model"

    Create and save a model entity.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - new_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.new_model(
            project="my-project",
            name="my-model",
            kind="model",
            path="s3://my-bucket/my-model",
        )
        ```

??? example "log_model"

    Create a model entity and upload a local source to the model store.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_model(
            project="my-project",
            name="my-model",
            source="./local-model",
        )
        ```

??? example "log_generic_model"

    Create a model of a custom kind and upload a local source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_generic_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_generic_model(
            project="my-project",
            kind="custom-model",
            source="./local-model",
            name="my-model",
        )
        ```

??? example "log_mlflow"

    Log an MLflow model from a local MLflow directory.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_mlflow

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_mlflow(
            project="my-project",
            name="my-mlflow-model",
            source="./mlruns/model",
        )
        ```

??? example "log_sklearn"

    Log a scikit-learn model from a local file or directory.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_sklearn

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_sklearn(
            project="my-project",
            name="my-sklearn-model",
            source="./model.pkl",
        )
        ```

??? example "log_huggingface"

    Log a Hugging Face model from a local repository or directory.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_huggingface

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_huggingface(
            project="my-project",
            name="my-huggingface-model",
            source="./model-repository",
        )
        ```

??? example "log_tvm_ir"

    Log a TVM Relax IR model from a local source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_tvm_ir

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_tvm_ir(
            project="my-project",
            name="my-tvm-ir-model",
            source="./out",
            source_format="onnx",
        )
        ```

??? example "log_tvm_so"

    Log a TVM compiled shared-object model from a local source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_tvm_so

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_tvm_so(
            project="my-project",
            name="my-tvm-so-model",
            source="./out",
            target="llvm -mcpu=x86-64-v2",
        )
        ```

??? example "register_model"

    Register a model whose source already exists in a supported store. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_model(
            project="my-project",
            source="s3://my-bucket/my-model",
        )
        ```

??? example "register_generic_model"

    Register an existing source with a custom model kind.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_generic_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_generic_model(
            project="my-project",
            kind="custom-model",
            source="s3://my-bucket/my-model",
        )
        ```

??? example "register_mlflow"

    Register an existing MLflow model. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_mlflow

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_mlflow(
            project="my-project",
            source="s3://my-bucket/my-mlflow-model",
        )
        ```

??? example "register_sklearn"

    Register an existing scikit-learn model. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_sklearn

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_sklearn(
            project="my-project",
            source="s3://my-bucket/my-sklearn-model",
        )
        ```

??? example "register_huggingface"

    Register an existing Hugging Face model. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_huggingface

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_huggingface(
            project="my-project",
            source="s3://my-bucket/my-huggingface-model",
        )
        ```

??? example "register_tvm_ir"

    Register an existing TVM Relax IR model. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_tvm_ir

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_tvm_ir(
            project="my-project",
            source="s3://my-bucket/my-tvm-ir-model",
        )
        ```

??? example "register_tvm_so"

    Register an existing TVM compiled model. The `name` can be inferred from the source.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_tvm_so

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_tvm_so(
            project="my-project",
            source="s3://my-bucket/my-tvm-so-model",
        )
        ```

## Read

Use the read methods to retrieve models from the backend or load them from a YAML descriptor.

??? example "get_model"

    Get one model by name and project. Omitting `entity_id` returns the latest version.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_model

    === "Example"

        ```python
        import digitalhub as dh

        model = dh.get_model(
            identifier="my-model",
            project="my-project",
        )
        ```

??? example "get_model_versions"

    Get all versions of a model by name and project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - get_model_versions

    === "Example"

        ```python
        import digitalhub as dh

        models = dh.get_model_versions(
            identifier="my-model",
            project="my-project",
        )
        ```

??? example "list_models"

    List the latest models in a project.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - list_models

    === "Example"

        ```python
        import digitalhub as dh

        models = dh.list_models(project="my-project")
        ```

??? example "import_model"

    Import a model from a local YAML descriptor or a storage key.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - import_model

    === "Example"

        ```python
        import digitalhub as dh

        model = dh.import_model("my-model.yaml")
        ```

## Update

Update a model after changing its mutable metadata.

??? example "update_model"

    Update an existing model. Its specification is immutable.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - update_model

    === "Example"

        ```python
        import digitalhub as dh

        model = dh.get_model(
            identifier="my-model",
            project="my-project",
        )
        model.set_description("Updated model")
        model = dh.update_model(model)
        ```

## Delete

Delete one model version or all versions of a model.

??? example "delete_model"

    Set `delete_all_versions=True` to delete all versions by entity name.

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - delete_model

    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_model(
            identifier="my-model",
            project="my-project",
            delete_all_versions=True,
        )
        ```
