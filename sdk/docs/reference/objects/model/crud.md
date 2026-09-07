# CRUD

The CRUD methods create, read, update and delete models. They can be called directly from the SDK or through a `Project` object.
The syntax is the same for all CRUD methods. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument.

## Create

Creation methods differ in how they handle the source:

- `log_<kind>()` creates an entity and uploads a local source to a model store.
- `register_<kind>()` creates an entity for a source that already exists in a store; `name` is optional and can be inferred from the source.
- `new_model()` creates and saves an entity from its specification and path without uploading a source.

For specification parameters, see the documentation for the relevant [model kind](kind/model.md), [MLflow kind](kind/mlflow.md), [scikit-learn kind](kind/sklearn.md), [Hugging Face kind](kind/huggingface.md), [TVM IR kind](kind/tvm-ir.md), or [TVM SO kind](kind/tvm-so.md).

### Log

??? example "log_model"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_model(
            project="my-project",
            name="image-classifier",
            source="./models/image-classifier",
            framework="pytorch",
            algorithm="resnet18",
            parameters={"num_classes": 10},
        )
        ```

??? example "log_mlflow"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_mlflow

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_mlflow(
            project="my-project",
            name="fraud-detector",
            source="./mlruns/0/abc123/artifacts/model",
            flavor="sklearn",
            framework="scikit-learn",
            algorithm="RandomForestClassifier",
        )
        ```

??? example "log_sklearn"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_sklearn

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_sklearn(
            project="my-project",
            name="churn-classifier",
            source="./models/churn-classifier.joblib",
            framework="scikit-learn",
            algorithm="RandomForestClassifier",
            parameters={"n_estimators": 100},
        )
        ```

??? example "log_huggingface"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_huggingface

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_huggingface(
            project="my-project",
            name="sentiment-classifier",
            source="./models/sentiment-classifier",
            model_id="distilbert-base-uncased",
            model_revision="main",
        )
        ```

??? example "log_tvm_ir"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_tvm_ir

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_tvm_ir(
            project="my-project",
            name="resnet18-relax",
            source="./models/resnet18.onnx",
            source_format="onnx",
            entry="main",
        )
        ```

??? example "log_tvm_so"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - log_tvm_so

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.log_tvm_so(
            project="my-project",
            name="resnet18-tvm",
            source="./build/resnet18.so",
            target="llvm -mcpu=x86-64-v2",
            opt_level=3,
        )
        ```

### Register

??? example "register_model"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_model

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_model(
            project="my-project",
            name="registered-image-classifier",
            source="s3://my-bucket/models/image-classifier",
            framework="pytorch",
            algorithm="resnet18",
        )
        ```

??? example "register_mlflow"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_mlflow

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_mlflow(
            project="my-project",
            name="registered-fraud-detector",
            source="s3://my-bucket/models/fraud-detector",
            flavor="sklearn",
            framework="scikit-learn",
        )
        ```

??? example "register_sklearn"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_sklearn

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_sklearn(
            project="my-project",
            name="registered-churn-classifier",
            source="s3://my-bucket/models/churn-classifier.joblib",
            framework="scikit-learn",
            algorithm="RandomForestClassifier",
        )
        ```

??? example "register_huggingface"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_huggingface

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_huggingface(
            project="my-project",
            name="registered-sentiment-classifier",
            source="s3://my-bucket/models/sentiment-classifier",
            model_id="distilbert-base-uncased",
            model_revision="main",
        )
        ```

??? example "register_tvm_ir"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_tvm_ir

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_tvm_ir(
            project="my-project",
            name="registered-resnet18-relax",
            source="s3://my-bucket/models/resnet18.onnx",
            source_format="onnx",
            entry="main",
        )
        ```

??? example "register_tvm_so"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_symbol_type_heading: true
                show_source: false
                members:
                    - register_tvm_so

    === "Creation example"

        ```python
        import digitalhub as dh

        model = dh.register_tvm_so(
            project="my-project",
            name="registered-resnet18-tvm",
            source="s3://my-bucket/models/resnet18.so",
            target="llvm -mcpu=x86-64-v2",
            opt_level=3,
        )
        ```

### New

??? example "new_model"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

## Read

Use the read methods to retrieve models from the backend or load them from a YAML descriptor.

??? example "get_model"

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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

    === "Function documentation"

        ::: digitalhub.entities
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
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
