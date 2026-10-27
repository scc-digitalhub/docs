---
id: sdk-workflow-pipelines-dsl
domain: sdk
type: reference
version: "0.15"
tags: [sdk, workflow, hera, kfp, argo, pipeline, dag, step, dsl]
summary: Authoring multi-step DAG pipelines in Python using digitalhub_runtime_hera.dsl (Argo Workflows) and digitalhub_runtime_kfp.dsl (Kubeflow Pipelines).
---

# Authoring Workflow Pipelines in Python (`hera` & `kfp` DSL)

In DigitalHub, multi-step workflows orchestrate existing **Functions** (`python`, `container`, `sklearnserve`, etc.) as nodes in a Directed Acyclic Graph (DAG). You write the pipeline logic in Python using either the **Hera DSL** (`kind: hera`, recommended for Argo Workflows) or the **KFP DSL** (`kind: kfp`).

---

## 1. Hera Pipeline DSL (`kind: hera`)

The `digitalhub_runtime_hera.dsl` package bridges DigitalHub Functions with Argo Workflows (`hera.workflows`).

### Core Imports
```python
from digitalhub_runtime_hera.dsl import step
from hera.workflows import Workflow, DAG, Parameter
```

### How `step(...)` Works
The `step(...)` function wraps a DigitalHub Function execution inside an Argo DAG task:
| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `template` | `dict` | **Yes** | Dictionary defining the Task action (`{"action": "job", "inputs": {...}, "parameters": {...}, "outputs": [...]}`). |
| `function` | `str` | **Yes** | Name of the registered Function in the same project (e.g., `"prep-data-fn"`). |
| `version` | `str` | No | Optional UUID of a specific Function version. Defaults to the latest version. |
| `name` | `str` | No | Step node name inside the Argo DAG (must be RFC-1123 lowercase alphanumeric + hyphens, e.g., `"s1-prep"`). |
| ` arguments` | `dict` | No | Upstream step output references passed into this step. |
| `outputs` | `list[str]` | No | Names of return keys produced by the Function's `outputs` contract that downstream steps will consume. |

---

## 2. Complete End-to-End Hera Pipeline Pattern

Suppose our project `fraud-detection` has two registered `python` functions:
1. `prep-data-fn`: Takes `inputs={"raw_data": ...}` and `parameters={"test_size": ...}`, and returns `{"train_set": Dataitem, "test_set": Dataitem}` (matching `outputs={"train_set": "train-data", "test_set": "test-data"}`).
2. `train-model-fn`: Takes `inputs={"train_data": ..., "test_data": ...}` and `parameters={"n_estimators": ...}`, and logs a trained model.

Here is the canonical `pipeline.py` script:

```python
from digitalhub_runtime_hera.dsl import step
from hera.workflows import Workflow, DAG, Parameter


def pipeline():
    # Define an Argo Workflow using the Hera context manager
    with Workflow(
        entrypoint="dag",
        arguments=[
            Parameter(name="raw_dataset_key"),
            Parameter(name="n_estimators", default=200),
        ],
    ) as w:
        with DAG(name="dag"):
            # Step 1: Data preparation function
            s1 = step(
                name="s1-prep-data",
                function="prep-data-fn",
                template={
                    "action": "job",
                    "inputs": {
                        "raw_data": "{{workflow.parameters.raw_dataset_key}}"
                    },
                    "parameters": {
                        "test_size": 0.2
                    },
                },
                outputs=["train_set", "test_set"],
            )

            # Step 2: Model training function consuming Step 1 outputs
            s2 = step(
                name="s2-train-model",
                function="train-model-fn",
                template={
                    "action": "job",
                    "inputs": {
                        "train_data": "{{inputs.parameters.train_set}}",
                        "test_data": "{{inputs.parameters.test_set}}",
                    },
                    "parameters": {
                        "n_estimators": "{{workflow.parameters.n_estimators}}"
                    },
                    "resources": {
                        "cpu": {"requests": "1", "limits": "2"},
                        "mem": {"requests": "2Gi", "limits": "4Gi"},
                    },
                },
                arguments={
                    "train_set": s1.get_parameter("train_set"),
                    "test_set": s1.get_parameter("test_set"),
                },
            )

            # Define DAG execution dependency (Step 1 -> Step 2)
            s1 >> s2

    return w
```

### Critical Rules for Hera Pipelines
1. **Handler Signature**: The entry function (`def pipeline():`) takes **no required positional arguments** when using `Workflow(arguments=[Parameter(...)])` and **must return the `Workflow` object `w`**.
2. **Passing Outputs Between Steps**:
   - In the upstream step (`s1`), declare `outputs=["train_set", "test_set"]` matching the dictionary keys returned by `prep-data-fn`.
   - In the downstream step (`s2`), wire `arguments={"train_set": s1.get_parameter("train_set")}` and reference it inside `template["inputs"]` as `"{{inputs.parameters.train_set}}"`.
3. **Passing Workflow-Level Parameters**:
   - Declare `arguments=[Parameter(name="raw_dataset_key")]` on `Workflow(...)`.
   - Reference them inside `template["inputs"]` or `template["parameters"]` using `"{{workflow.parameters.raw_dataset_key}}"`.
   - When executing `kind: hera+pipeline:run` via `dhcli execute -f`, pass `spec.parameters.raw_dataset_key: "store://..."`.

---

## 3. Kubeflow Pipelines DSL (`kind: kfp`)

For environments running Kubeflow Pipelines instead of Argo Workflows, use `digitalhub_runtime_kfp.dsl`:

```python
from digitalhub_runtime_kfp.dsl import step, pipeline_context
from kfp import dsl


@dsl.pipeline(name="fraud-kfp-pipeline")
def kfp_pipeline(raw_dataset_key: str, n_estimators: int = 200):
    with pipeline_context() as pc:
        s1 = step(
            name="prep-data",
            function="prep-data-fn",
            action="job",
            inputs={"raw_data": raw_dataset_key},
            outputs={"train_set": "train-data", "test_set": "test-data"},
        )

        s2 = step(
            name="train-model",
            function="train-model-fn",
            action="job",
            inputs={
                "train_data": s1.outputs["train_set"],
                "test_data": s1.outputs["test_set"],
            },
            parameters={"n_estimators": n_estimators},
        )
```

---

## 4. Registering & Running Your Pipeline via `dhcli`

Once `pipeline.py` is authored:
1. **Base64-encode `pipeline.py`**:
   ```bash
   base64 -i pipeline.py | tr -d '\n'
   ```
2. **Create the `kind: hera` Workflow (`dhcli create -f workflow.yaml -p <project>`)** with `spec.source.handler: "pipeline"` and `spec.source.base64: "<encoded>"`.
3. **Run `kind: hera+build:run`** (`dhcli execute -f build-run.yaml -p <project>`) to compile the Python code into `spec.workflow`.
4. **Run `kind: hera+pipeline:run`** (`dhcli execute -f pipeline-run.yaml -p <project>`) to execute the DAG on the cluster.
*(See [specs-workflows-and-triggers.md](../cli/specs-workflows-and-triggers.md) for the exact YAML manifests).*

