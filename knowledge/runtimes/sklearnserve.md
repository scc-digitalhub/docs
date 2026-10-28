---
title: Scikit-Learn Serve Runtime
description: Deploy Scikit-Learn (.pkl / .joblib) Model entities as KServe OpenInference v2 HTTP endpoints (sklearnserve+serve).
---

# Scikit-Learn Serve Runtime (`kind: sklearnserve`)

The **Scikit-Learn Serve runtime** (`digitalhub-runtime-modelserve`) deploys a `kind: sklearn` Model entity (`.pkl` or `.joblib`) as a KServe inference service exposing the standard OpenInference v2 REST API.

- **Supported task**: `sklearnserve+serve` → `sklearnserve+serve:run`

## 1. Creating & Deploying the Service via `dhcli`

```yaml
# function.yaml
kind: sklearnserve
name: fraud-rf-service
project: my-project
metadata:
  description: "Serve RandomForest fraud classifier"
spec:
  model_name: fraud-rf
  path: "store://my-project/model/sklearn/fraud-rf:<model-uuid>"
```

```bash
# 1. Register the serving function
dhcli create functions -p my-project -f function.yaml

# 2. Launch the serving run
dhcli run sklearnserve+serve -p my-project -n fraud-rf-service -f run.yaml

# 3. Inspect service status & port-forward locally
dhcli services -p my-project -o json
dhcli port-forward -p my-project -f fraud-rf-service -l 8080
```

## 2. Querying the OpenInference v2 Endpoint

Once port-forwarded to `localhost:8080`, call `/v2/models/<model_name>/infer`:

```bash
curl -X POST http://localhost:8080/v2/models/fraud-rf/infer \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": [
      {"name": "input-0", "shape": [1, 4], "datatype": "FP32", "data": [[5.1, 3.5, 1.4, 0.2]]}
    ]
  }'
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `sklearnserve`

Schema: `schemas/specs/function/sklearnserve.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.image` | string |  | Container image used for tasks; pattern `^seldonio\/mlserver?:.*-sklearn$` |
| `spec.model_name` | string |  | default `"model"` |
| `spec.path` | string | **yes** | URI pointing to the content; pattern `^(store://([^/]+)/model/sklearn/.*)|.*\.pkl$|.*\.joblib$` |

#### Task `sklearnserve+serve` → run kind `sklearnserve+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.path` | string |  | URI pointing to the content; pattern `^(store://([^/]+)/model/sklearn/.*)|.*\.pkl$|.*\.joblib$` |
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
