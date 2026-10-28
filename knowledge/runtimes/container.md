---
title: Container Runtime
description: Run custom Docker/OCI images as Kubernetes batch jobs (container+job), HTTP services (container+serve), persistent deployments (container+deploy), or Kaniko image builds (container+build).
---

# Container Runtime (`kind: container`)

The **Container runtime** executes any Docker/OCI container image on Kubernetes without requiring Python wrapper handlers.

- **Supported tasks (`dhcli run <task>`)**:
  - `container+build`: Build a container image in-cluster using Kaniko (`spec.base_image` + `spec.instructions` or a Dockerfile in `spec.source`).
  - `container+job`: Run a one-off Kubernetes batch `Job` until completion.
  - `container+serve`: Deploy a Kubernetes `Deployment` + `Service` (HTTP API, Streamlit, Gradio, FastAPI, dashboard).
  - `container+deploy`: Run a persistent background Kubernetes `Deployment` without a `Service` (e.g. queue workers).

## 1. Function YAML Manifest (`function.yaml`)

```yaml
kind: container
name: streamlit-dashboard
project: my-project
metadata:
  description: "Analytics dashboard container"
spec:
  image: "ghcr.io/my-org/streamlit-dashboard:1.0.0"
  image_pull_policy: Always
  command: ["streamlit"]
  args: ["run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
dhcli create functions -p my-project -f function.yaml
```

## 2. Executing as an HTTP Service (`container+serve`)

```yaml
# serve-run.yaml
spec:
  replicas: 1
  service_type: ClusterIP
  service_ports:
    - port: 80
      target_port: 8501
  envs:
    - name: STREAMLIT_SERVER_HEADLESS
      value: "true"
  secrets:
    - DB_PASSWORD
  resources:
    cpu: "1"
    mem: "2Gi"
```

```bash
dhcli run container+serve -p my-project -n streamlit-dashboard -f serve-run.yaml

# Inspect active service endpoint or port-forward locally
dhcli services -p my-project -o json
dhcli port-forward -p my-project -f streamlit-dashboard -l 8501
```

## 3. Executing as a Batch Job (`container+job`)

```yaml
# job-run.yaml
spec:
  args: ["--input", "/data/in.parquet", "--output", "/data/out.parquet"]
  resources:
    cpu: "2"
    mem: "4Gi"
```

```bash
dhcli run container+job -p my-project -n my-batch-container -f job-run.yaml
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `container`

Schema: `schemas/specs/function/container.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.base_image` | string |  | Image used as base for building tasks |
| `spec.command` | string |  | Override command executed in image |
| `spec.image` | string |  | Container image used for tasks |
| `spec.image_pull_policy` | enum: `IfNotPresent`, `Always`, `Never` |  | Policy for image pulling |
| `spec.source` | object (SourceCode_SourceCodeLanguages_) |  | Source code |
| `spec.source.base64` | string |  | Source code |
| `spec.source.handler` | string |  | Name of the handler function |
| `spec.source.lang` | enum: `python`, `java`, `javascript`, `typescript`, `dockerfile`, `markdown`, `html`, `json`, `sql`, `css`, `yaml`, `text`, `sh` |  | Language used for source code |
| `spec.source.source` | string |  | Reference to source (path or URI) |

#### Task `container+build` → run kind `container+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.instructions` | array<string> |  | Instructions executed as RUN during build stage |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `container+deploy` → run kind `container+deploy:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.fs_group` | integer |  | File System group ID |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.replicas` | integer |  | Number of replicas for the current task |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.run_as_group` | integer |  | Group ID for the container |
| `spec.run_as_user` | integer |  | User ID for the container |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `container+job` → run kind `container+job:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.fs_group` | integer |  | File System group ID |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.run_as_group` | integer |  | Group ID for the container |
| `spec.run_as_user` | integer |  | User ID for the container |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `container+serve` → run kind `container+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.fs_group` | integer |  | File System group ID |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.replicas` | integer |  | Number of replicas for the current task |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.run_as_group` | integer |  | Group ID for the container |
| `spec.run_as_user` | integer |  | User ID for the container |
| `spec.secrets` | array<string> |  |  |
| `spec.service_name` | string |  | Name of the service exposed |
| `spec.service_ports` | array<object (CorePort)> |  | Define ports mapping for the service |
| `spec.service_type` | enum: `ExternalName`, `ClusterIP`, `NodePort`, `LoadBalancer` |  | Select the type used for service definition; default `"ClusterIP"` |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
