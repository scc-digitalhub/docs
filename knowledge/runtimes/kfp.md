---
title: KFP Workflow Runtime (Kubeflow Pipelines)
description: Author and execute multi-step Kubeflow Pipelines DAGs using the digitalhub_runtime_kfp Python DSL.
---

# KFP Workflow Runtime (`kind: kfp`)

The **KFP runtime** (`digitalhub-runtime-kfp`) compiles Python pipeline functions written with the Kubeflow Pipelines DSL and `digitalhub_runtime_kfp.dsl.step` into Kubeflow Pipeline specifications and executes them on the cluster.

- **Entity type**: `workflow` (`dhcli create workflows`)
- **Tasks**:
  - `kfp+build`: Compile the Python pipeline into a KFP YAML package.
  - `kfp+pipeline`: Execute the compiled KFP pipeline.

## 1. Writing & Registering a KFP Workflow

```python
from digitalhub_runtime_kfp.dsl import pipeline_context, step

def my_kfp_pipeline(threshold: float = 0.5):
    with pipeline_context() as pc:
        s1 = step(name="ingest", function="ingest-fn", action="job")
        s2 = step(
            name="filter",
            function="filter-scores-fn",
            action="job",
            inputs={"raw_data": s1.outputs["raw_table"]},
            parameters={"threshold": threshold},
        )
```

Encode `pipeline.py` with `base64 -i pipeline.py | tr -d '\n'` and register via `dhcli create workflows -p my-project -f workflow.yaml`:

```yaml
kind: kfp
name: kfp-score-pipeline
project: my-project
spec:
  source:
    lang: python
    handler: my_kfp_pipeline
    base64: "<single-line-base64-of-pipeline.py>"
```

## 2. Building & Executing

Trigger `build` and `pipeline` via the Python SDK fallback (`dhcli init` — see [`sdk/sdk-fallback.md`](../sdk/sdk-fallback.md)), then inspect runs with `dhcli`:

```bash
python3 -c '
import digitalhub as dh
wf = dh.get_project("my-project").get_workflow("kfp-score-pipeline")
wf.run("build", wait=True)
run = wf.run("pipeline", parameters={"threshold": 0.75})
print("Run ID:", run.id)
'
dhcli get runs <run-id> -p my-project -o yaml
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Workflow kind `kfp`

Schema: `schemas/specs/workflow/kfp.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.image` | string |  | Container image used for tasks |
| `spec.source` | object (SourceCode_KFPSourceCodeLanguages_) | **yes** | Source code |
| `spec.source.base64` | string |  | Source code |
| `spec.source.handler` | string |  | Name of the handler function |
| `spec.source.lang` | enum: `python` |  | Language used for source code; default `"python"` |
| `spec.source.source` | string |  | Reference to source (path or URI) |
| `spec.tag` | string |  |  |

#### Task `kfp+build` → run kind `kfp+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `workflow` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.inputs` | map<string, string> |  | Input elements |
| `spec.outputs` | map<string, string> |  | Output elements |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `kfp+pipeline` → run kind `kfp+pipeline:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `workflow` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.inputs` | map<string, string> |  | Input elements |
| `spec.outputs` | map<string, string> |  | Output elements |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
