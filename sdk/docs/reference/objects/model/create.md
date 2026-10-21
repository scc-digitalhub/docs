---
render_macros: true
---

# Create a model

Choose the creation method based on where the model source is and whether you want to upload it.

!!! note "Install the model runtime"
    Kind-specific `new_model(kind=...)`, `log_<kind>()`, and `register_<kind>()` operations depend on runtime packages. Install the matching package in the same Python environment as the SDK before using them:

    - `mlflow`, `sklearn`, and `huggingface`: `digitalhub-runtime-modelserve`
    - `onnx`, `tflite`, `tvm-ir`, and `tvm-so`: `digitalhub-runtime-tvm`

    The generic `model` kind is provided by the SDK and does not require an additional runtime. See the [installation guide](../../../how-to/installation.md) for install commands.

## Choose a creation method

- **Log with `log_<kind>()`** creates a model from a local source and uploads its files to an artifact store. Choose the matching kind below.
- **Register with `register_<kind>()`** creates a model entity for a source that already exists in a store. Choose the matching kind below.
- **Create with `new_model()`** creates an entity from an explicit kind and path without uploading a source. Each kind page below includes an example with its corresponding kind.

## Choose a model kind

Creation methods vary by kind. Each kind page documents the available functions, parameters, and examples.

{{ kind_cards([
    ("Model", "./kind/model.md", "Store a generic machine-learning model", "model"),
    ("MLflow", "./kind/mlflow.md", "Store an MLflow model with its metadata", "mlflow"),
    ("Scikit-learn", "./kind/sklearn.md", "Store a scikit-learn model", "sklearn"),
    ("Hugging Face", "./kind/huggingface.md", "Register or reference a Hugging Face model", "huggingface"),
    ("ONNX", "./kind/onnx.md", "Store an ONNX model", "onnx"),
    ("TFLite", "./kind/tflite.md", "Store a TensorFlow Lite model", "tflite"),
    ("TVM IR", "./kind/tvm-ir.md", "Store a Relax IR model produced by TVM", "tvm-ir"),
    ("TVM SO", "./kind/tvm-so.md", "Store a compiled TVM shared-object model", "tvm-so"),
]) }}

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
