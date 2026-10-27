---
id: cli-execution-and-runs
domain: cli
type: operational_guide
version: "0.16"
tags: [cli, dhcli, run, log, metrics, stop, task, job, build, serve, pipeline]
commands:
  - dhcli run
  - dhcli log
  - dhcli metrics
  - dhcli stop
  - dhcli get
  - dhcli list
schemas:
  - run/python+job:run.json
  - run/python+build:run.json
  - run/python+serve:run.json
  - run/container+job:run.json
  - run/container+serve:run.json
  - log/log.json
summary: "Triggering function executions with `dhcli run <kind>+<action>`, passing run configuration YAML, streaming container logs (`dhcli log`), reading pod metrics (`dhcli metrics`), and stopping runs."
---

# CLI Task Execution, Run Monitoring, Logs & Metrics

In DigitalHub, executing an action on a **Function** creates a **Run** entity tracked by the platform. Through `dhcli`, you can launch runs (`dhcli run`), inspect their state (`dhcli get`/`list`), fetch container stdout/stderr logs (`dhcli log`), monitor CPU/Memory/GPU metrics (`dhcli metrics`), and terminate active runs (`dhcli stop`).

---

## 1. Launching a Function Run (`dhcli run`)

### 1.1 Command Syntax
```bash
dhcli run -p <project> (-n <function_name> | -i <function_id>) [-f <run_spec.yaml>] <task>
```

| Parameter / Flag | Required | Description |
| :--- | :---: | :--- |
| `-p, --project <project>` | Yes | Project name (or set via `PROJECT_NAME` env var). |
| `-n, --fn-name <name>` | Cond. | Name of the function to run (uses the `latest` version). Mandatory if `-i` is omitted. |
| `-i, --fn-id <uuid>` | Cond. | Specific version UUID of the function to run. Alternative to `-n`. |
| `-f, --file <run.yaml>` | No | Optional YAML file containing `spec` parameters (`inputs`, `parameters`, `resources`, `envs`, `secrets`, `volumes`). |
| `<task>` | Yes | Positional task identifier formatted as **`<kind>+<action>`** (e.g. `python+build`, `python+job`, `python+serve`, `container+job`, `container+serve`, `sklearnserve+serve`, `vllmserve-text+serve`, `dbt+transform`). |

### 1.2 How `dhcli run` Works Under the Hood
When you invoke `dhcli run -p my-proj -n my-fn -f run.yaml python+job`:
1. `dhcli` fetches the function `my-fn` (or version `-i <id>`) from Core.
2. `dhcli` checks if a `Task` entity for `python+job` already exists on that function; if not, it automatically creates one.
3. `dhcli` merges the `spec` block from `run.yaml` with the resolved `task` URI and `function` URI and posts a new `Run` entity to `/api/v1/-/<project>/runs`.

### 1.3 Anatomy of `<run_spec.yaml>` Passed to `dhcli run -f`
You do **not** need to hardcode `spec.task` or `spec.function` inside `run.yaml`—`dhcli run` populates those automatically! Only include the runtime and Kubernetes execution fields inside `spec`:

```yaml
kind: python+job:run
project: my-project
spec:
  # 1. Runtime execution inputs & parameters
  inputs:
    dataset: "store://my-project/dataitem/table/customers:latest"
  parameters:
    learning_rate: 0.01
    max_epochs: 20
  init_parameters: {}

  # 2. Kubernetes hardware & environment overrides
  resources:
    cpu: "2"
    mem: "4Gi"
    gpu: "1"
  envs:
    - name: LOG_LEVEL
      value: INFO
  secrets:
    - db-credentials
  volumes:
    - volume_type: empty_dir
      name: scratch-vol
      mount_path: /tmp/scratch
      spec:
        size_limit: "2Gi"
```

---

## 2. Finding the Created `<run_id>` & Polling Run State

Because `dhcli run` executes asynchronously on the Kubernetes cluster and prints `Created successfully.`, follow this pattern to get the `<run_id>` and check its `status.state`:

```bash
# 1. List runs in JSON (newest runs appear first or check metadata.created)
dhcli list -p my-project runs -o json

# 2. Inspect a specific run's status, outputs, and results
dhcli get -p my-project runs <run_id> -o json
```

Key fields in the `dhcli get -p <proj> runs <run_id> -o json` response:
- **`status.state`**: `CREATED` $\rightarrow$ `READY` $\rightarrow$ `RUNNING` $\rightarrow$ `COMPLETED` (or `ERROR` / `STOPPED`).
- **`status.outputs`**: Dictionary of platform entity keys (`store://...`) logged or returned by the run.
- **`status.results`**: Dictionary of primitive values returned by the handler.
- **`status.service`**: (For `+serve` runs) Contains `"url"` and `"urls"` for the internal cluster HTTP service.

---

## 3. Fetching Container Execution Logs (`dhcli log`)

To retrieve stdout and stderr captured from the Kubernetes pod executing the run:

```bash
# Fetch current logs of the main execution container (Recommended for Agents)
dhcli log -p my-project <run_id>

# Specify a specific container name inside the pod (-c)
dhcli log -p my-project -c <container_name> <run_id>
```

> **WARNING FOR AI AGENTS**:
> Never pass the `-f` (`--follow`) flag when calling `dhcli log` from an automated tool call! `dhcli log -f` polls in an infinite 5-second loop until the process is killed. Always run `dhcli log -p <project> <run_id>` without `-f`.

---

## 4. Inspecting Container Resource Metrics (`dhcli metrics`)

To check CPU, RAM, GPU utilization, GPU memory, and network I/O of a running or completed run:

```bash
# Human-readable summary (avg, sum, max, min for cpu, memory, gpu, gpu-memory)
dhcli metrics -p my-project run <run_id>

# Full time-series metrics in JSON format
dhcli metrics -p my-project run <run_id> -o json
```

---

## 5. Stopping an Active Run (`dhcli stop`)

To terminate a running batch job, build, or long-lived service deployment:

```bash
dhcli stop -p my-project <run_id>
```
This transitions the run's `status.state` to `STOPPED` and tears down the associated Kubernetes Job or Deployment/Service pods.

