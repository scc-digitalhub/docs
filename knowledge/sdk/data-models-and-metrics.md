---
id: sdk-data-models-and-metrics
domain: sdk
type: operational_guide
version: "0.16"
tags: [sdk, dataitem, as_df, as_file, log_dataitem, log_artifact, log_model, log_sklearn, log_mlflow, log_huggingface, log_metric, metrics]
summary: Reading Dataitems/Artifacts/Models inside Python handlers and logging outputs, models, artifacts, and metrics to DigitalHub Core.
---

# Reading & Logging Data, Models, Artifacts & Metrics in Python

Inside a Python handler (`def handler(project, run, ...):`), DigitalHub resolves `spec.inputs` keys into SDK objects (`Dataitem`, `Artifact`, `Model`) and injects active `project` and `run` objects.

---

## 1. Consuming Input Dataitems (`Dataitem` Object)

```python
import pandas as pd

def process_table(project, raw_table, raw_file):
    # 1.1 Read tabular Parquet/CSV/SQL as Pandas DataFrame
    df: pd.DataFrame = raw_table.as_df()

    # 1.2 Download file from S3 to container local disk
    local_path: str = raw_file.download(destination="/tmp/input_data")

    # 1.3 Or stream as binary file-like object
    buffer = raw_file.as_file()
    return df
```

---

## 2. Consuming Input Artifacts & Models

When passed via `spec.inputs` (or fetched via `project.get_model("my-model")`), use `.download()`:

```python
import joblib, os

def init_context(context):
    model_entity = context.project.get_model("fraud-rf-classifier")
    local_path = model_entity.download(destination="/tmp/model")
    if os.path.isdir(local_path):
        local_path = os.path.join(local_path, "model.joblib")
    context.model = joblib.load(local_path)
```

---

## 3. Logging Output Dataitems (`project.log_dataitem`)

```python
def create_features(project, raw_data):
    df = raw_data.as_df().dropna()
    # Logs as kind='table', converts to Parquet, registers schema in S3
    return project.log_dataitem(name="cleaned-features", kind="table", data=df)
```

---

## 4. Logging Output Artifacts (`project.log_artifact`)

Use for reports, plots, logs, HTML, or zip archives:

```python
def generate_report(project):
    return project.log_artifact(name="report-file", kind="artifact", source="/tmp/report.json")
```

---

## 5. Logging Trained Models (`log_sklearn`, `log_mlflow`, `log_model`)

```python
# 5.1 Scikit-Learn Model (deployed via sklearnserve)
model = project.log_sklearn(
    name="fraud-rf",
    source="/tmp/model.joblib",
    algorithm="RandomForestClassifier",
    parameters={"n_estimators": 100},
)
model.log_metrics({"accuracy": 0.98})

# 5.2 MLflow Model (deployed via mlflowserve)
model = project.log_mlflow(name="fraud-mlflow", source=mlflow_uri, flavor="sklearn")

# 5.3 Generic / HuggingFace Model
model = project.log_model(name="custom-weights", source="/tmp/weights/")
```

---

## 6. Evaluation Metrics: Run vs. Model vs. CLI Inspection

> ⚠️ **CRITICAL METRIC CLARIFICATION FOR AGENTS**:
> - **Custom Handler Metrics (`run.log_metric(k, v)`)**: Writes custom scalars/lists to Core.
> - **Model Metrics (`model.log_metrics(dict)`)**: Saved directly on the `Model` entity status. `project.log_sklearn()`, `log_mlflow()` and `log_model()` do **not** accept a `metrics=` argument (unknown keyword arguments are silently ignored); call `log_metrics()` on the returned model.
> - **`dhcli metrics run <id>`**: Queries **Kubernetes Prometheus/cAdvisor pod CPU/Memory usage**, NOT your custom Python metrics!
> - **Best Practice**: Always call `model.log_metrics(m)` on the logged model AND return `return {"metrics": m}` in the handler so metrics are immediately visible in `dhcli get runs <id> -o json` without spawning verification jobs. Always cast NumPy scalars (`float(v)`, `int(v)`) for JSON compliance.
