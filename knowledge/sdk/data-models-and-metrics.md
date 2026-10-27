---
id: sdk-data-models-and-metrics
domain: sdk
type: reference
version: "0.15"
tags: [sdk, dataitem, as_df, as_file, log_dataitem, log_artifact, log_model, log_sklearn, log_mlflow, log_huggingface, log_metric, mlflow]
summary: Complete reference for reading Dataitems, Models, and Artifacts inside Python handlers and logging output datasets, models, artifacts, and evaluation metrics back to DigitalHub Core.
---

# Reading & Logging Dataitems, Models, Artifacts & Metrics in Python

Inside a Python handler (`def handler(project, run, ...):`), DigitalHub automatically resolves every `store://` key declared in `spec.inputs` into a rich SDK object (`Dataitem`, `Artifact`, or `Model`) and injects the active `project` and `run` objects.

---

## 1. Consuming Input Dataitems (`Dataitem` Object)

When a `Dataitem` (`kind: table` or `kind: dataitem`) is passed into your handler as an argument, use these methods to read its underlying data from S3, HTTP, or SQL:

### 1.1 Read as a DataFrame (`di.as_df()`)
Reads tabular data (`.parquet`, `.csv`, `.json`, or `sql://` tables) directly into a `pandas.DataFrame` (default) or `polars.DataFrame`.

```python
import pandas as pd

def process_table(project, raw_table):
    # Read Parquet/CSV/SQL directly from S3/DB into a Pandas DataFrame
    df: pd.DataFrame = raw_table.as_df()

    # Pass file-format specific kwargs (e.g., CSV separator or column selection)
    # df = raw_table.as_df( file_format="csv", sep=";" )
    return df
```

### 1.2 Download to Local Container Filesystem (`di.download()`)
Downloads the remote file or folder from S3 into the container's local disk and returns the local filesystem path.

```python
def process_raw_file(raw_dataitem):
    # Downloads to a temporary local path or specified destination
    local_path: str = raw_dataitem.download(destination="/tmp/input_data", overwrite=True)
    with open(local_path, "r") as f:
        content = f.read()
```

### 1.3 Stream as File-Like Buffer (`di.as_file()`)
Opens the remote object as a binary file-like object (`io.BytesIO` / stream) without writing to disk.

---

## 2. Consuming Input Artifacts & Models

When an `Artifact` or `Model` is passed to your handler (or fetched in `init_context` via `project.get_model("my-model")`), use `.download()` to pull the files into the container:

```python
import joblib
import os

def init_context(context):
    # Fetch the latest READY version of the model from the project
    model_entity = context.project.get_model("fraud-rf-classifier")
    
    # Download model files to /tmp/model (returns local path)
    local_path = model_entity.download(destination="/tmp/model", overwrite=True)
    
    # If local_path is a directory, locate the file; if a file path, load directly
    if os.path.isdir(local_path):
        local_path = os.path.join(local_path, "model.joblib")
        
    context.model = joblib.load(local_path)
```

---

## 3. Logging Output Dataitems (`project.log_dataitem`)

To persist a processed dataset to the project's default S3 store and register it in DigitalHub Core, call `project.log_dataitem(...)`:

### 3.1 Logging a Pandas DataFrame (`kind="table"`)
When passing `data=df`, DigitalHub automatically converts the DataFrame to Parquet, extracts the Frictionless Table Schema (`spec.schema`), computes a data preview (`spec.preview`), and uploads it to S3.

```python
def create_features(project, raw_data):
    df = raw_data.as_df()
    features_df = df.dropna().reset_index(drop=True)

    # Logs as kind='table', uploads Parquet to S3, and registers schema
    logged_di = project.log_dataitem(
        name="cleaned-features",
        kind="table",
        data=features_df,
        description="Cleaned feature matrix without nulls",
        labels=["features", "gold-tier"]
    )
    return logged_di
```

### 3.2 Logging Local Files as a Dataitem (`source=...`)
```python
logged_raw = project.log_dataitem(
    name="raw-json-dump",
    kind="dataitem",
    source="/tmp/events.json"
)
```

---

## 4. Logging Output Artifacts (`project.log_artifact`)

Use `project.log_artifact` for unstructured files, HTML reports, plots, or zip archives:

```python
def generate_report(project):
    report_path = "/tmp/confusion_matrix.png"
    # ... save matplotlib figure to report_path ...

    artifact = project.log_artifact(
        name="confusion-matrix-plot",
        kind="artifact",
        source=report_path,
        description="Validation confusion matrix plot"
    )
    return artifact
```

---

## 5. Logging Trained Models (`log_sklearn`, `log_mlflow`, `log_huggingface`, `log_model`)

DigitalHub provides specialized logging helpers for each model serving runtime so your logged model can be deployed immediately with zero glue code.

### 5.1 Logging a Scikit-Learn Model (`project.log_sklearn`)
Ready for immediate deployment on the `sklearnserve` runtime (`kserve-sklearnserver`).

```python
import joblib
from sklearn.ensemble import RandomForestClassifier

def train_sklearn(project, run, train_data, n_estimators: int = 200):
    df = train_data.as_df()
    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]

    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    clf.fit(X, y)
    acc = float(clf.score(X, y))

    # Save model locally using joblib
    model_file = "/tmp/model.joblib"
    joblib.dump(clf, model_file)

    # Upload to S3 and register as kind='sklearn'
    model = project.log_sklearn(
        name="fraud-rf-classifier",
        source=model_file,
        algorithm="RandomForestClassifier",
        parameters={"n_estimators": n_estimators, "random_state": 42},
        metrics={"train_accuracy": acc}
    )

    # Also log metric to the current Run for run-level comparison
    run.log_metric("train_accuracy", acc)
    return model
```

### 5.2 Logging an MLflow Model (`project.log_mlflow`)
Ready for immediate deployment on the `mlflowserve` runtime (`seldon-mlserver`). Uses the helper `from digitalhub_runtime_python import get_mlflow_model_metrics` or standard MLflow logging:

```python
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

def train_with_mlflow(project, train_data):
    df = train_data.as_df()
    X, y = df.drop(columns=["target"]), df["target"]

    with mlflow.start_run() as mlflow_run:
        clf = RandomForestClassifier(n_estimators=100).fit(X, y)
        signature = infer_signature(X, clf.predict(X))
        mlflow.sklearn.log_model(clf, artifact_path="model", signature=signature)
        model_uri = mlflow.get_artifact_uri("model")

    # Register MLflow artifacts directory into DigitalHub
    model = project.log_mlflow(
        name="fraud-mlflow-model",
        source=model_uri,
        flavor="sklearn",
        algorithm="RandomForestClassifier",
        parameters={"n_estimators": 100}
    )
    return model
```

### 5.3 Logging a Custom or Fine-Tuned Model (`project.log_model` / `project.log_huggingface`)
For generic models (PyTorch `.pt`, ONNX `.onnx`) or fine-tuned HuggingFace checkpoints saved to a directory:

```python
# Generic model
model = project.log_model(
    name="custom-pytorch-weights",
    kind="model",
    source="/tmp/checkpoints/",
    framework="pytorch",
    algorithm="ResNet50",
    parameters={"epochs": 10, "lr": 0.001}
)

# Fine-tuned HuggingFace model directory
hf_model = project.log_huggingface(
    name="finetuned-finbert",
    source="/tmp/hf_output_dir/",
    model_id="ProsusAI/finbert",
    framework="transformers"
)
```

---

## 6. Logging Evaluation Metrics (`run.log_metric` & `model.log_metrics`)

You can attach scalar or series metrics to both the **Run** (`run`) and the **Model** (`model`):

```python
def evaluate(run, model, test_data):
    # Log single metric to the Run
    run.log_metric(key="f1_score", value=0.942)
    run.log_metric(key="roc_auc", value=0.981)

    # Log dictionary of metrics directly to the Model entity
    model.log_metrics({
        "test_f1_score": 0.942,
        "test_roc_auc": 0.981,
        "false_positive_rate": 0.012
    })
```
> **Best Practice**: Always cast NumPy scalars (`np.float64`, `np.int64`) to native Python `float(...)` or `int(...)` before passing them to `log_metric` or `parameters` to guarantee clean JSON serialization.

