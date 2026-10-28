---
title: Run Entity
description: Immutable execution instance of a Function or Workflow task, its lifecycle state machine, run.yaml anatomy, logs, metrics, and stopping runs via dhcli.
---

# Run Entity (`<task>:run`)

A **Run** represents a single execution instance of a Function or Workflow task on the Kubernetes cluster (for example, `python+job:run`, `python+serve:run`, `container+serve:run`, `hera+pipeline:run`).

- **Addressing**: Runs are **unversioned** and addressed solely by their `<run-id>` UUID.
- **Run kind format**: `<function-kind>+<action>:run` (e.g. `python+build:run`, `python+job:run`, `vllmserve-text+serve:run`).

## 1. Triggering a Run via `dhcli run`

```bash
# Run the latest version of function <fn-name> with task <kind>+<action>
dhcli run <kind>+<action> -p <project> -n <fn-name> [-f run.yaml]

# Run a specific function version by UUID (-i)
dhcli run <kind>+<action> -p <project> -i <fn-uuid> [-f run.yaml]
```

### Anatomy of `run.yaml` for `dhcli run`
When you pass `-f run.yaml` to `dhcli run`, `dhcli` extracts **only the `spec:` map** and automatically populates `kind`, `project`, `spec.task`, `spec.function`, and `spec.local_execution: false`.

```yaml
# run.yaml — only `spec:` is required by `dhcli run`
spec:
  inputs:
    # Handler arg -> store://<project>/<entity-type>/<kind>/<name>:<uuid>
    raw_data: "store://my-project/dataitem/table/sales:9d249ef7..."
  parameters:
    # Handler arg -> JSON serializable primitive/dict/list
    learning_rate: 0.01
    max_depth: 6
  init_parameters:
    # Passed to init_context (for serve tasks)
    model_name: "fraud-rf"
  envs:
    - name: LOG_LEVEL
      value: "INFO"
  secrets:
    - DB_PASSWORD
  resources:
    cpu: "2"
    mem: "4Gi"
```

## 2. Discovering `<run-id>`, Polling State & Inspecting Logs

`dhcli run` prints `Created successfully.` without echoing the new `<run-id>`. Always retrieve the `<run-id>` immediately via `dhcli list runs`:

```bash
# 1. List runs in JSON (newest runs appear first)
dhcli list runs -p my-project -o json

# Filter runs by state (-s) (Note: do not pass kind with '+' like -k python+job:run due to URL query decoding; filter kinds with jq instead)
dhcli list runs -p my-project -s RUNNING -o json

# 2. Inspect full Run status, outputs, or error messages (exclude heavy k8s block to avoid truncation)
dhcli get runs <run-id> -p my-project -o json | jq 'del(.status.k8s)'

# 3. Fetch container logs (live container) or persisted logs (terminated pod)
dhcli log <run-id> -p my-project
# If returns "container not found":
dhcli list logs -p my-project -o json | jq -r '.[] | select(.run == "<run-id>") | .content | @base64d'

# 4. Read CPU/memory metrics for a run
dhcli metrics run <run-id> -p my-project -o json

# 5. Stop a running job or service
dhcli stop <run-id> -p my-project

# 6. Delete a run record
dhcli delete runs <run-id> -p my-project -y
```

## 3. Run State Machine (`status.state`)

```text
CREATED ──► READY ──► RUNNING ──┬──► COMPLETED   (batch job / build / pipeline succeeded)
                                ├──► ERROR       (build/container failed — check `dhcli log`)
                                └──► STOPPED     (terminated via `dhcli stop`)
```

- **Batch tasks (`+job`, `+build`, `+transform`, `+pipeline`, `+train`)**: Poll `dhcli get runs <run-id> -p <project> -o json` until `status.state` reaches **`COMPLETED`** (or **`ERROR`**).
- **Long-lived services (`+serve`, `+deploy`)**: Remain in **`RUNNING`** indefinitely and expose their endpoint in `status.service` (viewable with `dhcli services -p <project> -o json`).
