---
id: cli-specs-data-and-storage
domain: cli
type: schema-reference
version: "0.15"
tags: [project, secret, artifact, dataitem, table, croissant, model, sklearn, mlflow, huggingface, yaml, schema]
schemas:
  - project/project.json
  - secret/secret.json
  - artifact/artifact.json
  - dataitem/dataitem.json
  - dataitem/table.json
  - dataitem/croissant.json
  - model/model.json
  - model/sklearn.json
  - model/mlflow.json
  - model/huggingface.json
summary: Core JSON Schema-backed YAML specifications for Projects, Secrets, Artifacts, Dataitems (generic, table, croissant), and ML Models (generic, sklearn, mlflow, huggingface).
---

# YAML Specifications: Data, Models, Projects & Secrets

This reference defines the exact YAML schemas validated by DigitalHub Core when executing `dhcli create -f <file.yaml>`, `dhcli register -f <file.yaml>`, or `dhcli update -f <file.yaml>`.

---

## 1. Project Specification (`kind: project`)

Source Schema: `digitalhub-core/schemas/specs/project/project.json`

A Project is the top-level namespace and organizational boundary for all DigitalHub entities, default file stores, and credentials.

### Schema Properties (`spec`)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `source` | `string` | No | Default remote storage root URI (`s3://bucket/path` or `file:///path`) for project entities. |
| `context` | `string` | No | Local filesystem working directory context. |
| `config` | `object` | No | Project-level configuration overrides (`default_files_store`, environment defaults). |
| `functions` | `array<object>` | No | Embedded list of function specifications belonging to the project. |
| `workflows` | `array<object>` | No | Embedded list of workflow specifications belonging to the project. |
| `dataitems` | `array<object>` | No | Embedded list of dataitem specifications belonging to the project. |
| `artifacts` | `array<object>` | No | Embedded list of artifact specifications belonging to the project. |
| `models` | `array<object>` | No | Embedded list of model specifications belonging to the project. |

### Canonical YAML (`dhcli create -f project.yaml`)
```yaml
kind: project
name: fraud-detection
metadata:
  name: fraud-detection
  description: "End-to-end fraud detection ML pipeline project"
  labels:
    - production
    - finance
spec:
  config:
    default_files_store: "s3://datalake/projects/fraud-detection"
```

---

## 2. Secret Specification (`kind: secret`)

Source Schema: `digitalhub-core/schemas/specs/secret/secret.json`

Secrets store sensitive configuration values (API keys, database passwords, tokens) backed by Kubernetes Secrets inside the project namespace.

### Schema Properties (`spec`)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `path` | `string` | No | Secret storage path (`secret://<secret-name>`). Managed automatically by Core. |
| `provider` | `string` | No | Secret provider identifier (defaults to `kubernetes`). |

### Creating & Referencing Secrets
Secrets are created in the project and mounted into Function Runs via `spec.secrets`:
```yaml
# Inside a Function Run YAML (e.g., python+job:run)
spec:
  function: "python://fraud-detection/ingest-fn:v1"
  secrets:
    - DB_PASSWORD
    - HF_TOKEN
```
Inside the container, DigitalHub injects the secret values as environment variables matching the secret names (`DB_PASSWORD`, `HF_TOKEN`).

---

## 3. Artifact Specification (`kind: artifact`)

Source Schema: `digitalhub-core/schemas/specs/artifact/artifact.json`

Artifacts represent unstructured files, archives, reports, plots, or binaries stored in object storage (`s3://`), shared volumes, or git repositories.

### Schema Properties (`spec`)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `path` | `string` | **Yes** | Target storage URI (`s3://bucket/project/artifact/name/id/file.ext`) or source URI. |

### Canonical YAML (`dhcli upload artifact` or `dhcli register -f artifact.yaml`)
```yaml
project: fraud-detection
kind: artifact
name: training-config-archive
metadata:
  description: "Hyperparameter configuration bundle"
  labels:
    - config
spec:
  path: "s3://datalake/fraud-detection/artifact/training-config-archive/v1/config.tar.gz"
```
> **CLI Best Practice**: Instead of manually writing `spec.path` and uploading to S3 separately, use `dhcli upload artifact training-config-archive -p fraud-detection -i ./config.tar.gz`. `dhcli` creates the entity and streams the file to S3 automatically.

---

## 4. Dataitem Specifications (`kind: dataitem`, `table`, `croissant`)

Source Schemas:
- `digitalhub-core/schemas/specs/dataitem/dataitem.json`
- `digitalhub-core/schemas/specs/dataitem/table.json`
- `digitalhub-core/schemas/specs/dataitem/croissant.json`

Dataitems represent structured, semi-structured, or unstructured datasets.

### 4.1 Generic Dataitem (`kind: dataitem`)
Used for raw files (JSON, XML, images, audio, text corpora).
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `path` | `string` | **Yes** | Storage URI (`s3://...`, `http://...`, `https://...`). |

### 4.2 Tabular Dataitem (`kind: table`)
Used for structured tabular datasets (`.parquet`, `.csv`, SQL tables) and supports inline Frictionless Table Schema validation and preview rows.
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `path` | `string` | **Yes** | Storage URI (`s3://.../*.parquet`, `s3://.../*.csv`, `sql://db/schema/table`). |
| `schema` | `object` | No | Frictionless Table Schema definition (`{"fields": [{"name": "col", "type": "number"}]}`). |
| `preview` | `object` | No | Columnar preview sample (`{"columns": [...], "data": [...]}`). |

#### Canonical `kind: table` YAML (`dhcli register -f table.yaml`)
```yaml
project: fraud-detection
kind: table
name: transactions-2026
metadata:
  description: "Cleaned credit card transactions dataset"
  labels:
    - dataset
    - silver-tier
spec:
  path: "s3://datalake/fraud-detection/dataitem/transactions-2026/data.parquet"
  schema:
    fields:
      - name: transaction_id
        type: string
      - name: amount
        type: number
      - name: merchant_category
        type: string
      - name: is_fraud
        type: integer
```

### 4.3 Croissant Metadata Dataitem (`kind: croissant`)
Used for MLCommons Croissant JSON-LD dataset descriptors.
```yaml
project: fraud-detection
kind: croissant
name: benchmark-croissant
spec:
  path: "https://huggingface.co/api/datasets/organisation/dataset/croissant"
```

---

## 5. Model Specifications (`kind: model`, `sklearn`, `mlflow`, `huggingface`)

Source Schemas:
- `digitalhub-core/schemas/specs/model/model.json`
- `digitalhub-core/schemas/specs/model/sklearn.json`
- `digitalhub-core/schemas/specs/model/mlflow.json`
- `digitalhub-core/schemas/specs/model/huggingface.json`

Models represent versioned machine learning or deep learning artifacts together with their framework metadata, hyperparameters, and evaluation metrics.

### Common Base Properties (`spec`)
All model kinds share these base properties:
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `path` | `string` | **Yes** | Storage URI pointing to the model file or directory (`s3://...`, `huggingface://...`). |
| `framework` | `string` | No | Framework identifier (e.g., `sklearn`, `pytorch`, `xgboost`, `transformers`). |
| `algorithm` | `string` | No | Algorithm name (e.g., `RandomForestClassifier`, `LlamaForCausalLM`). |
| `parameters` | `object` | No | Key-value dictionary of training hyperparameters (`{"n_estimators": 200, "max_depth": 8}`). |

### Common Status Metrics (`status.metrics`)
Evaluation metrics are stored in `status.metrics` as key-value pairs (scalars or arrays):
```yaml
status:
  state: READY
  metrics:
    f1_score: 0.942
    roc_auc: 0.981
    precision: 0.955
```

### 5.1 Scikit-Learn Model (`kind: sklearn`)
Served directly by the `sklearnserve` runtime (`kserve-sklearnserver`). `spec.path` must point to a `.pkl` or `.joblib` file (or a directory containing `model.joblib` / `model.pkl`).
```yaml
project: fraud-detection
kind: sklearn
name: fraud-rf-classifier
metadata:
  description: "Random Forest classifier trained on 2026 transactions"
spec:
  path: "s3://datalake/fraud-detection/model/fraud-rf-classifier/v1/model.joblib"
  framework: "sklearn"
  algorithm: "RandomForestClassifier"
  parameters:
    n_estimators: 200
    max_depth: 10
    class_weight: "balanced"
```

### 5.2 MLflow Model (`kind: mlflow`)
Served by the `mlflowserve` runtime (`seldon-mlserver`). Includes MLflow flavor and signature schemas.
| Extra Field | Type | Description |
| :--- | :--- | :--- |
| `flavor` | `string` | MLflow flavor (`sklearn`, `pytorch`, `xgboost`, `lightgbm`, `pyfunc`). |
| `input_signature` | `object` | MLflow model input schema (`{"inputs": "[{\"type\": \"double\", \"name\": \"amount\"}]"}`). |
| `output_signature` | `object` | MLflow model output schema (`{"outputs": "[{\"type\": \"long\"}]"}`). |
| `datasets` | `array<string>` | Lineage list of `store://` Dataitem keys used to train the model. |

```yaml
project: fraud-detection
kind: mlflow
name: fraud-mlflow-xgb
spec:
  path: "s3://datalake/fraud-detection/model/fraud-mlflow-xgb/v1/"
  framework: "xgboost"
  flavor: "xgboost"
  parameters:
    learning_rate: 0.05
  datasets:
    - "store://fraud-detection/dataitem/table/transactions-2026:b812a9e0-1111-4222-8333-444455556666"
```

### 5.3 HuggingFace Model (`kind: huggingface`)
Served by the ` huggingfaceserve` runtime (KServe HuggingFace runtime / vLLM backend).
| Extra Field | Type | Description |
| :--- | :--- | :--- |
| `model_id` | `string` | HuggingFace Hub repository ID (e.g., `meta-llama/Llama-3.1-8B-Instruct` or `bert-base-uncased`). |
| `model_revision` | `string` | Optional HuggingFace Git commit hash, tag, or branch. |

```yaml
project: fraud-detection
kind: huggingface
name: finbert-sentiment
spec:
  path: "huggingface://ProsusAI/finbert"
  model_id: "ProsusAI/finbert"
  model_revision: "main"
  framework: "transformers"
  algorithm: "BertForSequenceClassification"
```
*(Note: If you fine-tune a HuggingFace weights folder and upload it to S3, set `spec.path: "s3://datalake/fraud-detection/model/finbert-sentiment/v1/"` instead of `huggingface://...`).*

