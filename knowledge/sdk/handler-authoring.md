---
id: sdk-handler-authoring
domain: sdk
type: runtime_specification
version: "0.16"
tags:
  [
    sdk,
    python,
    handler,
    project,
    run,
    context,
    event,
    inputs,
    parameters,
    outputs,
    init,
    dataitem,
  ]
summary: "How to write Python handler functions that execute inside the DigitalHub Python runtime: reserved injected arguments (`project`, `run`, `context`, `event`), `inputs` vs `parameters`, optional `@handler` output decorators, and `init` functions."
---

# Authoring Python Handlers (`def handler`, Inputs, Parameters & Outputs)

When you register a `kind: python` function via `dhcli create -f function.yaml functions`, the platform executes the Python function specified by `spec.source.handler` inside a Kubernetes pod (or Nuclio container). This guide covers how to write that Python code using the in-container DigitalHub SDK.

---

## 1. Standard Handler Anatomy (Recommended)

A Python handler is a standard Python `def` function. **No decorator or special import is required** for standard batch jobs or HTTP endpoints:

```python
def process_customers(project, run, raw_data, min_spend=100.0):
    """
    - `project` and `run` are automatically injected by the DigitalHub runtime.
    - `raw_data` is passed via `spec.inputs` in run.yaml (resolved to a Dataitem object).
    - `min_spend` is passed via `spec.parameters` in run.yaml (primitive float).
    """
    # 1. Read input DataItem as a Pandas DataFrame
    df = raw_data.as_df()

    # 2. Transform data
    filtered_df = df[df["total_spend"] >= min_spend]

    # 3. Log output DataItem and execution metric back to the platform
    project.log_dataitem(
        name="high-value-customers",
        kind="table",
        data=filtered_df,
    )
    run.log_metric("rows_retained", len(filtered_df))

    return {"status": "completed", "rows": len(filtered_df)}
```

> **Best Practice for Agents**: Always prefer plain Python functions (`def my_handler(...):`) and explicit `project.log_dataitem(...)` / `project.log_artifact(...)` / `project.log_model(...)` calls inside the function body. Plain functions never fail due to missing `digitalhub-runtime-python` decorator imports.

---

## 2. Reserved Arguments Injected by the Runtime

If any of the following 4 parameter names appear in your handler's signature, the runtime automatically injects the corresponding live platform object at invocation time:

| Argument Name | Injected Object Type | Available In | Common Methods Used Inside Handler |
| :--- | :--- | :--- | :--- |
| **`project`** | `Project` | `job` & `serve` | `project.log_dataitem(...)`, `project.log_artifact(...)`, `project.log_model(...)`, `project.log_sklearn(...)`, `project.get_dataitem(...)`, `project.get_secret(...)` |
| **`run`** | `Run` | `job` & `serve` | `run.log_metric(key, val)`, `run.log_metrics(dict)` |
| **`context`** | Nuclio `Context` | Remote `job` & `serve` | `context.logger.info(...)`, `context.user_data.<attr>` (populated by `init_function`) |
| **`event`** | Nuclio `Event` | Remote `job` & `serve` | `event.body` (incoming HTTP request payload in `python+serve`), `event.headers`, `event.path` |

---

## 3. Mapping `inputs` vs. `parameters` from `run.yaml`

When triggering a run via `dhcli run -p <project> -n <fn> -f run.yaml python+job`, any arguments in your Python function signature (other than the 4 reserved arguments above) are matched by name against `spec.inputs` and `spec.parameters`:

| `run.yaml` Section | What Value Goes in `run.yaml` | What the Python Handler Receives |
| :--- | :--- | :--- |
| **`spec.inputs`** | A platform entity key string: `"store://<project>/<entity>/<kind>/<name>:<version>"` | The instantiated SDK **`Dataitem`**, **`Artifact`**, or **`Model`** object! You can immediately call `.as_df()`, `.as_file()`, or `.download()` on it. |
| **`spec.parameters`**| Any JSON primitive (`string`, `number`, `boolean`, `list`, `dict`). | The exact Python primitive value (`str`, `int`, `float`, `bool`, `list`, `dict`). |

### Critical Pitfall: `entity_key` Parsing Error
- **NEVER** pass a plain file path or primitive string inside `spec.inputs`—the runtime attempts to resolve every entry in `spec.inputs` as a `store://` entity key and will crash with `ValueError: Cannot parse entity_key`.
- **NEVER** pass a `store://` key inside `spec.parameters` if your handler expects a `Dataitem` object with `.as_df()`, because `spec.parameters` passes the raw string literal without resolving the entity.

---

## 4. Writing `serve` Handlers (`python+serve`) & Using `init_function`

For long-lived HTTP endpoints (`dhcli run ... python+serve`), use an `init` function to load heavy resources (such as ML models or DB connections) **once** at pod startup rather than on every HTTP request:

```python
import joblib

def init_context(context, model_artifact_key):
    """
    Called ONCE when the serving pod starts.
    - `model_artifact_key` is supplied via `spec.init_parameters` in run.yaml.
    """
    import digitalhub as dh
    model_obj = dh.get_model(model_artifact_key)
    local_path = model_obj.download()
    context.user_data.clf = joblib.load(local_path)
    context.logger.info("Model loaded into memory.")

def predict(context, event):
    """
    Called on every HTTP request to the service endpoint.
    """
    payload = event.body  # dict parsed from incoming JSON request body
    features = payload.get("features", [])
    prediction = context.user_data.clf.predict([features]).tolist()
    return {"prediction": prediction}
```

Corresponding `function.yaml` and `run.yaml`:
```yaml
# function.yaml
kind: python
name: iris-Realtime-api
project: my-project
spec:
  python_version: PYTHON3_10
  requirements: ["scikit-learn", "joblib"]
  source:
    lang: python
    handler: predict
    init_function: init_context
    base64: "<BASE64_CODE>"
```
```yaml
# run.yaml
kind: python+serve:run
project: my-project
spec:
  replicas: 1
  init_parameters:
    model_artifact_key: "store://my-project/model/sklearn/iris-clf:latest"
```

---

## 5. Optional: `@handler(outputs=[...])` Decorator

If you prefer declarative return-value mapping instead of calling `project.log_*` inside the function, you can decorate the entrypoint with `@handler` from `digitalhub_runtime_python`:

```python
from digitalhub_runtime_python import handler
import pandas as pd

@handler(outputs=["cleaned_table", "row_count"])
def clean(raw_di):
    df = raw_di.as_df().dropna()
    return df, len(df)
```

> **MANDATORY REQUIREMENT WHEN USING `@handler`**:
> If your code contains `from digitalhub_runtime_python import handler`, you **MUST** include `"digitalhub-runtime-python"` in `spec.requirements` of your `function.yaml` (or run `python+build`), otherwise the container may fail with `ModuleNotFoundError: No module named 'digitalhub_runtime_python'` if using a custom base image.
