---
title: Python Runtime
description: Execute Python batch jobs (python+job), Nuclio serverless HTTP services (python+serve), and Kaniko container image builds (python+build) via dhcli.
---

# Python Runtime (`kind: python`)

The **Python runtime** (`digitalhub-runtime-python`) executes Python handler functions as one-off Kubernetes Jobs (`python+job`), long-lived Nuclio HTTP microservices (`python+serve`), or Kaniko container builds (`python+build`).

## 1. Critical Rules for `dhcli`

1. **Nested `spec.source`**: In `function.yaml`, handler code metadata (`lang`, `handler`, `base64`, `source`, `init_function`) **MUST** be nested under `spec.source`.
2. **Base64-Encode Local `.py` Scripts**: `dhcli create` sends YAML directly to Core without reading local `.py` files on disk. Always encode local scripts via `base64 -i handler.py | tr -d '\n'` and place the string in `spec.source.base64`.
3. **Bake Dependencies with `python+build`**: When `spec.requirements` includes packages not in the base image, run `dhcli run python+build -p <project> -n <fn-name>` and wait for `COMPLETED` before running `python+job` or `python+serve`.

## 2. End-to-End Batch Job Recipe (`python+job`)

### Step 1: Write and Base64-encode `handler.py`
```python
def process_data(project, run, raw_data, threshold: float = 0.5):
    df = raw_data.as_df()
    filtered = df[df["score"] >= threshold]
    project.log_dataitem(name="filtered-data", kind="table", data=filtered)
    run.log_metric("rows_kept", len(filtered))
```
```bash
base64 -i handler.py | tr -d '\n'
```

### Step 2: Create `function.yaml`
```yaml
kind: python
name: filter-scores-fn
project: my-project
metadata:
  description: "Filter dataset rows by score threshold"
spec:
  python_version: PYTHON3_10
  requirements:
    - "pandas>=2.0.0"
  source:
    lang: python
    handler: process_data
    base64: "<single-line-base64-string>"
```
```bash
dhcli create functions -p my-project -f function.yaml
```

### Step 3: Build Custom Dependencies (If Needed) & Run `python+job`
```bash
# Optional: build image with spec.requirements
dhcli run python+build -p my-project -n filter-scores-fn
```

Create `run.yaml` (remember: `dhcli run` automatically sets `spec.function` and `spec.task`):
```yaml
spec:
  inputs:
    raw_data: "store://my-project/dataitem/table/raw-scores:<uuid>"
  parameters:
    threshold: 0.75
  resources:
    cpu: "1"
    mem: "2Gi"
```
```bash
dhcli run python+job -p my-project -n filter-scores-fn -f run.yaml
dhcli list runs -p my-project -o json
dhcli log <run-id> -p my-project
```

## 3. Serverless HTTP Endpoint Recipe (`python+serve`)

For `python+serve`, provide an optional `init_function` (called once on pod startup to load models into `context`) and a `handler` (called on every HTTP request with `(context, event)`):

```python
def init_context(context, model_key: str):
    model = context.project.get_model(key=model_key)
    context.user_data.clf = model.as_custom()

def serve(context, event):
    payload = event.body
    pred = context.user_data.clf.predict([payload["features"]])
    return {"prediction": int(pred[0])}
```

In `function.yaml`, set `spec.source.init_function: init_context` and `spec.source.handler: serve`. Then execute with `dhcli run python+serve -p my-project -n <fn-name> -f serve-run.yaml`, passing `spec.init_parameters: {model_key: "store://..."}`.

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `python`

Schema: `schemas/specs/function/python.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.base_image` | string |  | Image used as base for building tasks |
| `spec.image` | string |  | Container image used for tasks |
| `spec.python_version` | enum: `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` | **yes** | Major version of language |
| `spec.requirements` | array<string> |  | List of requirements (formatted as requirements.txt) |
| `spec.source` | object (PythonSourceCode) | **yes** | Source code |
| `spec.source.base64` | string |  | Source code |
| `spec.source.handler` | string |  | Name of the handler function |
| `spec.source.init_function` | string |  | Name of the initializing function (optional) |
| `spec.source.lang` | enum: `python` |  | Language used for source code; default `"python"` |
| `spec.source.source` | string |  | Reference to source (path or URI) |

#### Task `python+build` → run kind `python+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.init_parameters` | map<string, serializable> |  |  |
| `spec.inputs` | map<string, string> |  | Input elements |
| `spec.instructions` | array<string> |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `python+job` → run kind `python+job:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.init_parameters` | map<string, serializable> |  |  |
| `spec.inputs` | map<string, string> |  | Input elements |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `python+serve` → run kind `python+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.init_parameters` | map<string, serializable> |  |  |
| `spec.inputs` | map<string, string> |  | Input elements |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.replicas` | integer |  | Number of replicas for the current task |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.service_name` | string |  | Name of the service exposed |
| `spec.service_type` | enum: `ExternalName`, `ClusterIP`, `NodePort`, `LoadBalancer` |  | Select the type used for service definition; default `"ClusterIP"` |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
