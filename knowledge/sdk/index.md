---
id: sdk-index
domain: sdk
type: index
version: "0.15"
tags: [sdk, python, index, handler, hera, kfp, notebook]
summary: Domain router for the DigitalHub Python SDK, separating in-container Python handler authoring and pipeline DSLs from host-side CLI management.
---

# DigitalHub Python SDK Knowledge Domain

## Architectural Role of the Python SDK vs. `dhcli`

In the DigitalHub Platform architecture:
1. **Host-Side Operations (`dhcli`)**: Creating projects, registering YAML manifests, triggering jobs, uploading local datasets, checking run states, and reading pod logs from an agent or CI/CD runner should be executed via **`dhcli` (`digitalhub-cli`)** (see [CLI Index](../cli/index.md)).
2. **In-Container Execution (`digitalhub` Python SDK)**: The Python code that executes **inside** Kubernetes pods (`python+job`, `python+serve`, `hera`, `kfp`) or inside interactive Jupyter notebooks uses the `digitalhub` Python SDK to:
   - Receive typed `Dataitem`, `Model`, and `Artifact` objects in function handlers (`def handler(project, run, ...):`).
   - Read Dataitems as Pandas/Polars DataFrames (`di.as_df()`) or local files (`di.as_file()`).
   - Log output datasets (`project.log_dataitem(...)`), trained models (`project.log_model(...)`, `project.log_sklearn(...)`, `project.log_mlflow(...)`), artifacts (`project.log_artifact(...)`), and evaluation metrics (`run.log_metric(...)`).
   - Author multi-step DAG pipelines using `digitalhub_runtime_hera.dsl` or `digitalhub_runtime_kfp.dsl`.

---

## SDK Knowledge Map

| Document | Topic & Scope | When to Read |
| :--- | :--- | :--- |
| [handler-authoring.md](handler-authoring.md) | **In-Container Handler Authoring**: `job`, `serve` (`init_context` + `serve`), and `expose` handler signatures, context injection (`project`, `run`, `context`), and return contracts. | Before writing any `.py` script for a `python` function. |
| [data-models-and-metrics.md](data-models-and-metrics.md) | **In-Container Data, Model & Metric Logging**: Reading inputs (`as_df`, `as_file`, `download`) and logging outputs (`log_dataitem`, `log_artifact`, `log_sklearn`, `log_mlflow`, `log_huggingface`, `log_metric`). | When a handler reads datasets or produces artifacts, models, or metrics. |
| [workflow-pipelines-dsl.md](workflow-pipelines-dsl.md) | **Pipeline DSL Authoring (Hera & KFP)**: Writing multi-step DAG pipelines in Python using `digitalhub_runtime_hera.dsl.step` and `hera.workflows.Workflow`. | When writing the `.py` source for a `kind: hera` or `kind: kfp` workflow. |
| [interactive-sdk-reference.md](interactive-sdk-reference.md) | **Interactive Notebook SDK Reference**: Top-level `import digitalhub as dh` CRUD and execution functions (`get_or_create_project`, `new_function`, `func.run()`) for Jupyter users. | Only when assisting a user inside an interactive Python notebook. |

---

## Python Package Installation & Extras

Inside DigitalHub runtime containers, `digitalhub` is pre-installed. When installing locally for development or IDE type-checking, match the minor version (`0.15.x`) of DigitalHub Core:

```bash
# Core SDK + Dataitem/Model/Artifact support (Pandas, PyArrow, S3, SQL)
pip install digitalhub[full]

# Runtime-specific extras for local testing or authoring
pip install digitalhub-runtime-python
pip install digitalhub-runtime-hera
pip install digitalhub-runtime-kfp
pip install digitalhub-runtime-modelserve
```

### Automatic Environment Detection Inside Pods
When a Run executes inside a Kubernetes pod launched by DigitalHub Core, the platform automatically injects `DHCORE_ENDPOINT`, `DHCORE_ACCESS_TOKEN`, and project context variables into the container environment. Your handler code **never** needs to configure credentials or endpoints manually—simply use the injected `project` or `run` arguments directly.

