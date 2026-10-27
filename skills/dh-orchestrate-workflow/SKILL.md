---
name: dh-orchestrate-workflow
description: Author, build, execute, and schedule multi-step DAG pipelines (Hera / Argo Workflows and KFP) and automated Triggers (scheduler cron and lifecycle event-driven) using dhcli.
---

# Skill: Orchestrating Multi-Step Workflows & Automated Triggers

Use this procedural workflow when chaining multiple DigitalHub Functions into an automated Directed Acyclic Graph (DAG) pipeline using `kind: hera` (Argo Workflows) and optionally attaching a cron `scheduler` or event-driven `lifecycle` Trigger.

## Reference Knowledge
- [workflow-pipelines-dsl.md](../../knowledge/sdk/workflow-pipelines-dsl.md)
- [specs-workflows-and-triggers.md](../../knowledge/cli/specs-workflows-and-triggers.md)
- [keys-and-lifecycle.md](../../knowledge/management/keys-and-lifecycle.md)

---

## Step-by-Step Procedure

### Step 1: Verify All Component Functions Exist in the Project
Every step in a DigitalHub workflow calls a registered Function in the same project. Verify that all required functions are registered and built (`status.state: READY`):
```bash
dhcli list functions -p <project-name>
```

### Step 2: Write the Python Hera Pipeline Script (`pipeline.py`)
Author `pipeline.py` using `digitalhub_runtime_hera.dsl.step` and `hera.workflows.Workflow`:
```python
from digitalhub_runtime_hera.dsl import step
from hera.workflows import Workflow, DAG, Parameter


def pipeline():
    with Workflow(
        entrypoint="dag",
        arguments=[Parameter(name="raw_dataset_key")],
    ) as w:
        with DAG(name="dag"):
            s1 = step(
                name="s1-prep",
                function="prep-data-fn",
                template={
                    "action": "job",
                    "inputs": {"raw_data": "{{workflow.parameters.raw_dataset_key}}"},
                },
                outputs=["cleaned_data"],
            )
            s2 = step(
                name="s2-train",
                function="train-model-fn",
                template={
                    "action": "job",
                    "inputs": {"train_data": "{{inputs.parameters.cleaned_data}}"},
                },
                arguments={"cleaned_data": s1.get_parameter("cleaned_data")},
            )
            s1 >> s2
    return w
```

### Step 3: Base64-Encode `pipeline.py` and Create the `kind: hera` Workflow
1. Base64-encode the script without line breaks:
   ```bash
   base64 -i pipeline.py | tr -d '\n'
   ```
2. Create `workflow.yaml` with `spec.source.base64`:
   ```yaml
   project: <project-name>
   kind: hera
   name: <workflow-name>
   metadata:
     description: "Automated training DAG pipeline"
   spec:
     source:
       lang: python
       handler: pipeline
       base64: "<BASE64_STRING>"
   ```
3. Register the workflow and capture its `id` (`<wf-uuid>`):
   ```bash
   dhcli create -f workflow.yaml -p <project-name>
   dhcli get workflow <workflow-name> -p <project-name> -o yaml
   ```

### Step 4: Phase 1 — Build the Workflow Template (`kind: hera+build:run`)
Before executing a Hera pipeline, compile its Python DSL into an Argo Workflow YAML specification (`spec.workflow`):
```yaml
project: <project-name>
kind: hera+build:run
spec:
  workflow: "hera://<project-name>/<workflow-name>:<wf-uuid>"
```
```bash
dhcli execute -f wf-build-run.yaml -p <project-name>
```
Poll `dhcli get run <build-run-uuid> -p <project-name> -o yaml` until `status.state` is `COMPLETED`.

### Step 5: Phase 2 — Execute the Pipeline (`kind: hera+pipeline:run`)
Create `wf-pipeline-run.yaml` passing the workflow-level parameters:
```yaml
project: <project-name>
kind: hera+pipeline:run
spec:
  workflow: "hera://<project-name>/<workflow-name>:<wf-uuid>"
  parameters:
    raw_dataset_key: "store://<project-name>/dataitem/table/<dataset-name>:<dataset-uuid>"
```
```bash
dhcli execute -f wf-pipeline-run.yaml -p <project-name>
```
Monitor the pipeline run via `dhcli get run <pipeline-run-uuid> -p <project-name> -o yaml`.

### Step 6 (Optional): Attach an Automated Cron or Lifecycle Trigger
To schedule the pipeline on a recurring Quartz cron schedule (`kind: scheduler`), create `trigger.yaml` and apply via `dhcli create -f trigger.yaml -p <project-name>` (see [specs-workflows-and-triggers.md](../../knowledge/cli/specs-workflows-and-triggers.md)).

