---
title: OpenInference Runtime
description: Author custom Python inference handlers that expose a standardized KServe OpenInference v2 REST API (openinference+build, openinference+serve).
---

# OpenInference Runtime (`kind: openinference`)

The **OpenInference runtime** lets you write a custom Python `init_context` + `serve` handler that automatically speaks the KServe **OpenInference v2** protocol (`/v2/models/<name>/infer`) with typed tensor inputs and outputs.

- **Supported tasks**: `openinference+build`, `openinference+serve`

## Creating & Running via `dhcli`

1. Write your Python inference handler (`handler.py`) and Base64-encode it (`base64 -i handler.py | tr -d '\n'`).
2. Create `function.yaml` with `kind: openinference`, `spec.python_version`, and `spec.source` (`lang: python`, `handler`, `init_function`, `base64`).
3. Register and run:
   ```bash
   dhcli create functions -p my-project -f function.yaml
   dhcli run openinference+build -p my-project -n my-oi-fn
   dhcli run openinference+serve -p my-project -n my-oi-fn -f run.yaml
   ```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `openinference`

Schema: `schemas/specs/function/openinference.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.base_image` | string |  | Image used as base for building tasks |
| `spec.image` | string |  | Container image used for tasks |
| `spec.inputs` | array<object (TensorModel)> | **yes** | Open Inference v2 protocol input tensor definition |
| `spec.model_name` | string | **yes** |  |
| `spec.outputs` | array<object (TensorModel)> |  | Open Inference v2 protocol output tensor definition |
| `spec.python_version` | enum: `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` | **yes** | Major version of language |
| `spec.requirements` | array<string> |  | List of requirements (formatted as requirements.txt) |
| `spec.source` | object (PythonSourceCode) | **yes** | Source code |
| `spec.source.base64` | string |  | Source code |
| `spec.source.handler` | string |  | Name of the handler function |
| `spec.source.init_function` | string |  | Name of the initializing function (optional) |
| `spec.source.lang` | enum: `python` |  | Language used for source code; default `"python"` |
| `spec.source.source` | string |  | Reference to source (path or URI) |

#### Task `openinference+build` → run kind `openinference+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.init_parameters` | map<string, serializable> |  |  |
| `spec.instructions` | array<string> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `openinference+serve` → run kind `openinference+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.init_parameters` | map<string, serializable> |  |  |
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
