---
title: MLflow Serve Runtime
description: Build and deploy MLflow Model entities as KServe OpenInference v2 HTTP services (mlflowserve+build, mlflowserve+serve).
---

# MLflow Serve Runtime (`kind: mlflowserve`)

The **MLflow Serve runtime** (`digitalhub-runtime-modelserve`) deploys a `kind: mlflow` Model entity via MLServer/KServe exposing the OpenInference v2 REST protocol.

- **Supported tasks**:
  - `mlflowserve+build`: Optional Kaniko image build when custom Python dependencies are needed.
  - `mlflowserve+serve`: Deploy the MLflow model as an HTTP service.

## Creating & Deploying via `dhcli`

```yaml
# function.yaml
kind: mlflowserve
name: churn-mlflow-service
project: my-project
metadata:
  description: "MLflow churn model endpoint"
spec:
  model_name: churn-model
  path: "store://my-project/model/mlflow/churn-model:<model-uuid>"
```

```bash
dhcli create functions -p my-project -f function.yaml
dhcli run mlflowserve+serve -p my-project -n churn-mlflow-service
dhcli services -p my-project -o json
dhcli port-forward -p my-project -f churn-mlflow-service -l 8080
```

Query `POST http://localhost:8080/v2/models/churn-model/infer` using the OpenInference v2 JSON payload.

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `mlflowserve`

Schema: `schemas/specs/function/mlflowserve.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.image` | string |  | Container image used for tasks; pattern `^seldonio\/mlserver?:.*-mlflow$` |
| `spec.model_name` | string |  | default `"model"` |
| `spec.path` | string | **yes** | URI pointing to the content; pattern `^(store://([^/]+)/model/mlflow/.*)|.*/$|.*\.zip$` |

#### Task `mlflowserve+build` → run kind `mlflowserve+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.instructions` | array<string> |  |  |
| `spec.path` | string |  | URI pointing to the content; pattern `^(store://([^/]+)/model/mlflow/.*)|.*/$|.*\.zip$` |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `mlflowserve+serve` → run kind `mlflowserve+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.path` | string |  | URI pointing to the content; pattern `^(store://([^/]+)/model/mlflow/.*)|.*/$|.*\.zip$` |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.replicas` | integer |  | Number of replicas for the current task |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.service_name` | string |  | Name of the service exposed |
| `spec.service_type` | enum: `ExternalName`, `ClusterIP`, `NodePort`, `LoadBalancer` |  | Select the type used for service definition; default `"ClusterIP"` |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
