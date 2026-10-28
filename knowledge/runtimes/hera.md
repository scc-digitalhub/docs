---
title: Hera Workflow Runtime (Argo)
description: Author and execute multi-step Argo Workflows DAG pipelines using the digitalhub_runtime_hera Python DSL.
---

# Hera Workflow Runtime (`kind: hera`)

The **Hera runtime** (`digitalhub-runtime-hera`) compiles Python pipeline functions written with `@pipeline` and `step(...)` into Kubernetes **Argo Workflows** DAGs.

- **Entity type**: `workflow` (`dhcli create workflows`)
- **Tasks**:
  - `hera+build`: Compile the Python pipeline handler into an Argo Workflow template.
  - `hera+pipeline`: Execute the compiled DAG on Argo Workflows.

## 1. Writing a Hera Pipeline (`pipeline.py`)

Each step in the pipeline calls an existing registered Function in the project:

```python
from digitalhub_runtime_hera.dsl import step
from hera.workflows import DAG, Workflow, Parameter

def pipeline():
    with Workflow(entrypoint="dag", arguments=[Parameter(name="threshold", default="0.5")]) as w:
        with DAG(name="dag"):
            s1 = step(
                template={"action": "job", "function": "ingest-fn"},
                name="ingest",
                outputs=["raw_table"],
            )
            s2 = step(
                template={
                    "action": "job",
                    "function": "filter-scores-fn",
                    "inputs": {"raw_data": "{{tasks.ingest.outputs.parameters.raw_table}}"},
                    "parameters": {"threshold": "{{workflow.parameters.threshold}}"},
                },
                name="filter",
                outputs=["filtered_data"],
            )
            s1 >> s2
    return w
```

## 2. Registering the Workflow via `dhcli`

Base64-encode `pipeline.py` and register the Workflow entity:

```bash
base64 -i pipeline.py | tr -d '\n'
```

```yaml
# workflow.yaml
kind: hera
name: score-filter-pipeline
project: my-project
metadata:
  description: "Ingest and filter scores on Argo Workflows"
spec:
  source:
    lang: python
    handler: pipeline
    base64: "<single-line-base64-of-pipeline.py>"
```

```bash
dhcli create workflows -p my-project -f workflow.yaml
```

## 3. Building & Running the Pipeline

Because `dhcli run` targets `/functions` rather than `/workflows`, trigger `build` and `pipeline` using a one-line Python SDK call inside the workspace venv (`dhcli init` — see [`sdk/sdk-fallback.md`](../sdk/sdk-fallback.md)), then monitor with `dhcli`:

```bash
python3 -c '
import digitalhub as dh
wf = dh.get_project("my-project").get_workflow("score-filter-pipeline")
wf.run("build", wait=True)
run = wf.run("pipeline", parameters={"threshold": 0.75})
print("Run ID:", run.id)
'

dhcli get runs <run-id> -p my-project -o yaml
dhcli log <run-id> -p my-project
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Workflow kind `hera`

Schema: `schemas/specs/workflow/hera.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.image` | string |  | Container image used for tasks |
| `spec.source` | object (SourceCode_HeraSourceCodeLanguages_) | **yes** | Source code |
| `spec.source.base64` | string |  | Source code |
| `spec.source.handler` | string |  | Name of the handler function |
| `spec.source.lang` | enum: `python` |  | Language used for source code; default `"python"` |
| `spec.source.source` | string |  | Reference to source (path or URI) |
| `spec.tag` | string |  |  |

#### Task `hera+build` → run kind `hera+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `workflow` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `hera+pipeline` → run kind `hera+pipeline:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `workflow` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
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
