---
id: cli-specs-workflows-and-triggers
domain: cli
type: schema-reference
version: "0.15"
tags: [workflow, hera, kfp, argo, pipeline, build, trigger, scheduler, cron, lifecycle, yaml, schema]
schemas:
  - workflow/hera.json
  - workflow/kfp.json
  - run/hera+build:run.json
  - run/hera+pipeline:run.json
  - trigger/scheduler.json
  - trigger/lifecycle.json
summary: Core JSON Schema-backed YAML specifications for Workflows (hera, kfp), Workflow Runs (build, pipeline), and Triggers (scheduler cron, lifecycle event-driven).
---

# YAML Specifications: Workflows (`hera`, `kfp`) & Triggers (`scheduler`, `lifecycle`)

This reference documents the exact YAML schemas required by `dhcli create -f` and `dhcli execute -f` for multi-step DAG pipelines and automated triggers.

---

## 1. Hera Workflow Specification (`kind: hera`)

Source Schema: `digitalhub-core/schemas/specs/workflow/hera.json`

The `hera` runtime allows you to write Argo Workflows DAGs in pure Python using the `digitalhub_runtime_hera.dsl` (`step`) and `hera.workflows` (`Workflow`, `DAG`, `Steps`) SDKs.

### Schema Properties (`spec`)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `source` | `object` | **Yes** | Nested `WorkflowSourceCode` object (`handler`, `base64`, `source`, `lang`). |
| `source.handler` | `string` | **Yes** | Name of the Python pipeline function (e.g., `pipeline`). |
| `source.base64` | `string` | **Yes*** | Base64-encoded string of the Python workflow script (required when creating local files via `dhcli`). |
| `source.source` | `string` | No | Remote code source URI (`git://...`, `http://...`) if not using inline `base64`. |
| `source.lang` | `string` | No | Must be `"python"`. |
| `image` | `string` | No | Custom container image for building the workflow template. |
| `tag` | `string` | No | Image tag override. |
| `workflow` | `string` | No | Compiled Argo Workflow YAML string (populated automatically after running `hera+build:run`). |

### Two-Phase Workflow Lifecycle in `dhcli`
A `hera` (or `kfp`) workflow requires **two steps** before it executes on Argo:
1. **Build Phase (`hera+build:run`)**: Compiles the Python `spec.source` function into an Argo Workflow YAML template and saves it into the workflow's `spec.workflow` field.
2. **Execution Phase (`hera+pipeline:run`)**: Submits the compiled Argo Workflow YAML template to the cluster's Argo controller with runtime `parameters`.

### Canonical `kind: hera` Workflow YAML
Encode your pipeline script (`base64 -i pipeline.py | tr -d '\n'`) and create the workflow:
```yaml
project: fraud-detection
kind: hera
name: training-pipeline
metadata:
  description: "End-to-end data prep, training, and evaluation DAG"
spec:
  source:
    lang: python
    handler: pipeline
    base64: "ZGVmIHBpcGVsaW5lKCk6CiAgICBwYXNzCg=="
```

---

## 2. Hera Workflow Build & Pipeline Run YAMLs

Source Schemas:
- `digitalhub-core/schemas/specs/run/hera+build:run.json`
- `digitalhub-core/schemas/specs/run/hera+pipeline:run.json`

> **Critical Reference Format**: Inside any workflow run YAML, `spec.workflow` MUST be formatted as:
> `<workflow-kind>://<project-name>/<workflow-name>:<workflow-uuid>`
> Example: `hera://fraud-detection/training-pipeline:d4e5f6a7-1111-4222-8333-999988887777`

### 2.1 Step 1: Build the Workflow (`kind: hera+build:run`)
```yaml
project: fraud-detection
kind: hera+build:run
spec:
  task: "hera+build://fraud-detection/build-task-uuid"
  workflow: "hera://fraud-detection/training-pipeline:d4e5f6a7-1111-4222-8333-999988887777"
```
Run with `dhcli execute -f build-run.yaml -p fraud-detection` and wait until `status.state` reaches `COMPLETED`.

### 2.2 Step 2: Execute the Pipeline (`kind: hera+pipeline:run`)
```yaml
project: fraud-detection
kind: hera+pipeline:run
spec:
  task: "hera+pipeline://fraud-detection/pipeline-task-uuid"
  workflow: "hera://fraud-detection/training-pipeline:d4e5f6a7-1111-4222-8333-999988887777"
  parameters:
    dataset_key: "store://fraud-detection/dataitem/table/transactions-2026:b812a9e0-1111-4222-8333-444455556666"
    n_estimators: 300
```

---

## 3. Kubeflow Pipelines Specification (`kind: kfp`)

Source Schema: `digitalhub-core/schemas/specs/workflow/kfp.json`

Identical structure to `hera`, except `kind: kfp` uses the `digitalhub_runtime_kfp.dsl` and `@dsl.pipeline` decorator.
- Build Run Kind: `kfp+build:run` (`task: "kfp+build://..."`, `workflow: "kfp://<project>/<name>:<id>"`)
- Pipeline Run Kind: `kfp+pipeline:run` (`task: "kfp+pipeline://..."`, `workflow: "kfp://<project>/<name>:<id>"`)

---

## 4. Trigger Specifications (`kind: scheduler`, `kind: lifecycle`)

Source Schemas:
- `digitalhub-core/schemas/specs/trigger/scheduler.json`
- `digitalhub-core/schemas/specs/trigger/lifecycle.json`

Triggers automate the execution of a Function Task or Workflow Task based on either a time schedule (`scheduler`) or a storage event (`lifecycle`).

### Common Trigger Properties (`spec`)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `task` | `string` | **Yes** | Task string to trigger (e.g., `python+job://fraud-detection/task-uuid` or `hera+pipeline://fraud-detection/task-uuid`). |
| `function` | `string` | Cond. | Function reference (`python://fraud-detection/my-fn:uuid`) if triggering a function. |
| `workflow` | `string` | Cond. | Workflow reference (`hera://fraud-detection/my-wf:uuid`) if triggering a workflow. |
| `template` | `object` | **Yes** | Run specification payload (`inputs`, `parameters`, `resources`, `envs`) passed to every triggered Run. |

### 4.1 Scheduled Cron Trigger (`kind: scheduler`)
Uses **Quartz Cron format** (6 or 7 fields including seconds: ` Seconds Minutes Hours DayOfMonth Month DayOfWeek [Year]`).

```yaml
project: fraud-detection
kind: scheduler
name: nightly-retraining-trigger
metadata:
  description: "Run fraud training pipeline every night at 02:00 UTC"
spec:
  schedule: "0 0 2 * * ?"
  task: "hera+pipeline://fraud-detection/pipeline-task-uuid"
  workflow: "hera://fraud-detection/training-pipeline:d4e5f6a7-1111-4222-8333-999988887777"
  template:
    workflow: "hera://fraud-detection/training-pipeline:d4e5f6a7-1111-4222-8333-999988887777"
    parameters:
      n_estimators: 300
```

> **Quartz Cron Examples**:
> - Every 15 minutes: `0 */15 * * * ?`
> - Every day at midnight: `0 0 0 * * ?`
> - Every Monday at 08:30 AM: `0 30 8 ? * MON`

### 4.2 Event-Driven Lifecycle Trigger (`kind: lifecycle`)
Triggers a task automatically when an entity (such as a `dataitem` or `model`) transitions to a specified `states` value (e.g., `READY`).

```yaml
project: fraud-detection
kind: lifecycle
name: on-new-transactions-trigger
metadata:
  description: "Run validation job whenever transactions-2026 reaches READY"
spec:
  key: "store://fraud-detection/dataitem/table/transactions-2026"
  states:
    - READY
  task: "python+job://fraud-detection/validate-task-uuid"
  function: "python://fraud-detection/validate-fn:a1b2c3d4-1111-4222-8333-444455556666"
  template:
    function: "python://fraud-detection/validate-fn:a1b2c3d4-1111-4222-8333-444455556666"
    parameters:
      strict_mode: true
```

