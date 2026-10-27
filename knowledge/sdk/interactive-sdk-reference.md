---
id: sdk-interactive-reference
domain: sdk
type: reference
version: "0.15"
tags: [sdk, python, notebook, jupyter, get_or_create_project, new_function, new_workflow, run]
summary: Compact reference for interactive Python SDK usage inside Jupyter notebooks (import digitalhub as dh).
---

# Interactive Notebook Python SDK Reference (`import digitalhub as dh`)

> **Important Architectural Note**:
> For automated agents, CI/CD pipelines, and workspace operations, **always prefer `dhcli` + YAML manifests** (see [CLI Index](../cli/index.md)). Use the top-level `import digitalhub as dh` CRUD and execution functions below **only** when assisting a user inside an interactive Jupyter Notebook (`.ipynb`) or when writing an explicit Python automation script requested by the user.

---

## 1. Project Management

```python
import digitalhub as dh

# Get an existing project or create a new one if it doesn't exist
project = dh.get_or_create_project("fraud-detection")

# Fetch an existing project (raises EntityError if not found)
project = dh.get_project("fraud-detection")

# Delete a project (cascade=True deletes all entities inside the project)
dh.delete_project("fraud-detection", cascade=True)
```

---

## 2. Creating & Running Functions Interactively

When creating a `python` function via `project.new_function(...)` in the Python SDK, the SDK reads your local `code_src="src/handler.py"` file from disk and Base64-encodes it into `spec.source.base64` automatically:

```python
# 1. Create a Python function from a local script
fn = project.new_function(
    name="train-rf-fn",
    kind="python",
    python_version="PYTHON3_10",
    code_src="src/train.py",
    handler="train_sklearn",
    requirements=["scikit-learn==1.5.1", "joblib==1.4.2"],
)

# 2. Execute the function as a batch job
#    Pass local=True only if testing locally in the notebook kernel;
#    leave local=False (default) to execute as a Kubernetes Job on the cluster.
job_run = fn.run(
    action="job",
    inputs={"train_data": dataset.key},
    parameters={"n_estimators": 200},
    resources={"cpu": {"requests": "1", "limits": "2"}, "mem": {"requests": "2Gi", "limits": "4Gi"}},
    wait=True,  # Blocks until run reaches COMPLETED or ERROR
)

# 3. Inspect run status, logs, and outputs
print(job_run.refresh().status.state)
print(job_run.logs())
print(job_run.outputs())
```

---

## 3. Deploying Interactive Services (`action="serve"`)

```python
# Deploy a Python API endpoint
serve_run = api_fn.run(
    action="serve",
    init_parameters={"model_name": "fraud-rf-classifier"},
    service_ports=[{"port": 8000, "target_port": 8080}],
    wait=True,
)

# Invoke the deployed service directly via the Run object
response = serve_run.invoke(method="POST", json={"features": [120.5, 0, 1, 4]})
print(response.json())
```

---

## 4. Creating & Running Workflows Interactively

```python
# 1. Define workflow from local pipeline.py
wf = project.new_workflow(
    name="training-pipeline",
    kind="hera",
    code_src="src/pipeline.py",
    handler="pipeline",
)

# 2. Build the Argo workflow template
build_run = wf.run(action="build", wait=True)

# 3. Execute the compiled pipeline on Argo
pipeline_run = wf.run(
    action="pipeline",
    parameters={"raw_dataset_key": dataset.key, "n_estimators": 300},
    wait=True,
)
```

---

## 5. Exporting & Importing YAML from the SDK

Every entity object in the Python SDK supports `.export()` to serialize its Core JSON Schema-compliant YAML to disk:

```python
# Export any entity (Project, Function, Workflow, Dataitem, Model, Run) to YAML
fn.export("functions/train-rf-fn.yaml")
project.export("project-bundle.yaml")

# Load or import an entity from YAML
loaded_fn = project.import_function("functions/train-rf-fn.yaml")
```

