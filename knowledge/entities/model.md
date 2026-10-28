---
title: Model Entity
description: Versioned ML and DL model artifacts (sklearn, mlflow, huggingface, model) with lineage, metrics, and direct deployment to serving runtimes.
---

# Model Entity (`kind: model`, `sklearn`, `mlflow`, `huggingface`)

A **Model** entity represents trained machine learning or deep learning weights, tokenizer files, and model signatures stored in S3 (`s3://`) and ready to be deployed by DigitalHub serving runtimes.

- **Supported kinds**:
  - `sklearn`: Scikit-Learn `.pkl` / `.joblib` model served by [`sklearnserve`](../runtimes/sklearnserve.md).
  - `mlflow`: MLflow model directory (`MLmodel` + flavor artifacts) served by [`mlflowserve`](../runtimes/mlflowserve.md).
  - `huggingface`: HuggingFace Transformer/PyTorch checkpoint directory served by [`huggingfaceserve`](../runtimes/huggingfaceserve.md), [`vllmserve`](../runtimes/vllmserve.md), or [`kubeai`](../runtimes/kubeai.md).
  - `model`: Generic model weights or custom archive (e.g. ONNX, PyTorch `.pt`).
- **Store URI format**: `store://<project>/model/<kind>/<name>:<uuid>`

## 1. Uploading Local Model Weights (`dhcli upload`)

### Generic Model (`kind: model`)
> **CRITICAL RULE**: Pass the singular `model` resource argument so `dhcli upload` sets `kind: model`.

```bash
dhcli upload model -p my-project -n custom-weights -f ./weights.pt -v
```

### Typed Model (`kind: sklearn`, `mlflow`, `huggingface`)
To upload local files into a typed model kind (`sklearn`, `mlflow`, `huggingface`):
1. Register the manifest via `dhcli create models -p my-project -f model.yaml`:
   ```yaml
   kind: sklearn
   name: fraud-rf
   project: my-project
   metadata:
     description: "RandomForest fraud classifier"
   spec:
     path: "s3://datalake/my-project/model/fraud-rf/model.joblib"
     framework: scikit-learn
     algorithm: RandomForestClassifier
   ```
2. Retrieve the `<uuid>` via `dhcli get models -p my-project -n fraud-rf -o json`.
3. Upload the file or directory into that `<uuid>`:
   ```bash
   dhcli upload model <uuid> -p my-project -f ./model.joblib
   ```

## 2. Logging Models from a Python Training Job

The most common way to produce a `Model` entity is inside a `python+job` training handler using the injected `project` object:

```python
import joblib
from sklearn.ensemble import RandomForestClassifier

def train(project, train_data):
    df = train_data.as_df()
    X, y = df.drop(columns=["target"]), df["target"]
    clf = RandomForestClassifier(n_estimators=100).fit(X, y)
    joblib.dump(clf, "model.joblib")

    model = project.log_sklearn(
        name="fraud-rf",
        source="model.joblib",
        algorithm="RandomForestClassifier",
    )
    model.log_metrics({"accuracy": 0.96})
```

## 3. Deploying a Model to a Serving Runtime

Pass the Model's `store://` URI (or `s3://` path) to the corresponding serving function or run:
- `sklearn` → [`sklearnserve`](../runtimes/sklearnserve.md) (`spec.path: "store://<project>/model/sklearn/<name>:<uuid>"`)
- `mlflow` → [`mlflowserve`](../runtimes/mlflowserve.md) (`spec.path: "store://<project>/model/mlflow/<name>:<uuid>"`)
- `huggingface` → [`huggingfaceserve`](../runtimes/huggingfaceserve.md) or [`vllmserve`](../runtimes/vllmserve.md) / [`kubeai`](../runtimes/kubeai.md)

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Kind `huggingface`

Schema: `schemas/specs/model/huggingface.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.algorithm` | string |  |  |
| `spec.base_model` | string |  |  |
| `spec.framework` | string |  |  |
| `spec.model_id` | string |  |  |
| `spec.model_revision` | string |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |

### Kind `mlflow`

Schema: `schemas/specs/model/mlflow.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.algorithm` | string |  |  |
| `spec.flavor` | string |  |  |
| `spec.framework` | string |  |  |
| `spec.input_datasets` | array<object (Dataset)> |  |  |
| `spec.model_config` | map<string, string> |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |
| `spec.signature` | object (Signature) |  |  |
| `spec.signature.inputs` | string |  |  |
| `spec.signature.outputs` | string |  |  |
| `spec.signature.params` | string |  |  |

### Kind `model`

Schema: `schemas/specs/model/model.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.algorithm` | string |  |  |
| `spec.framework` | string |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |

### Kind `sklearn`

Schema: `schemas/specs/model/sklearn.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.algorithm` | string |  |  |
| `spec.framework` | string |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |

<!-- END GENERATED: spec-reference -->
