---
title: Workflow Entity
description: Multi-step DAG pipelines authored in Hera (Argo Workflows) or KFP (Kubeflow Pipelines), registered via dhcli and executed via the SDK fallback.
---

# Workflow Entity (`kind: hera`, `kfp`)

A **Workflow** defines a multi-step Directed Acyclic Graph (DAG) pipeline that orchestrates multiple DigitalHub Functions (`job`, `build`, `serve`) on Kubernetes.

- **Supported kinds**:
  - `hera`: Argo Workflows pipeline authored with `digitalhub_runtime_hera.dsl` (see [`runtimes/hera.md`](../runtimes/hera.md)).
  - `kfp`: Kubeflow Pipelines DAG authored with `digitalhub_runtime_kfp.dsl` (see [`runtimes/kfp.md`](../runtimes/kfp.md)).
- **Workflow reference URI**: `<kind>://<project>/<name>:<uuid>` (e.g., `hera://my-project/etl-pipeline:6c9d1...`)

## 1. Registering & Inspecting Workflows via `dhcli`

`dhcli` supports full CRUD (`create`, `get`, `list`, `update`, `delete`) on `workflows`:

```yaml
# workflow.yaml
kind: hera
name: etl-train-pipeline
project: my-project
metadata:
  description: "End-to-end ETL and training DAG"
spec:
  source:
    lang: python
    handler: pipeline
    base64: "<single-line-base64-of-pipeline.py>"
```

```bash
# Encode pipeline.py and register the workflow
base64 -i pipeline.py | tr -d '\n'
dhcli create workflows -p my-project -f workflow.yaml

# Inspect workflow metadata and UUID
dhcli get workflows -p my-project -n etl-train-pipeline -o json
dhcli list workflows -p my-project
```

## 2. Building & Executing a Workflow (`build` + `pipeline`)

> **IMPORTANT CLI LIMITATION**:
> `dhcli run` only resolves **Functions** (`/functions`); it cannot execute Workflows (`/workflows`). And `dhcli create runs` requires a pre-existing `Task` UUID that `dhcli` cannot create for a workflow.
> Therefore, to **build and run a Workflow**, use the one-liner Python SDK fallback inside the workspace venv (`dhcli init` — see [`sdk/sdk-fallback.md`](../sdk/sdk-fallback.md)):

```bash
python3 -c '
import digitalhub as dh
p = dh.get_project("my-project")
wf = p.get_workflow("etl-train-pipeline")
wf.run("build", wait=True)
run = wf.run("pipeline", parameters={"n_estimators": 200})
print("Started pipeline run:", run.id)
'
```

Once the workflow run starts, monitor its state and logs normally with `dhcli`:

```bash
dhcli list runs -p my-project -o json
dhcli get runs <run-id> -p my-project -o yaml
dhcli log <run-id> -p my-project
```
