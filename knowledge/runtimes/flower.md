---
title: Flower Federated Learning Runtime
description: Deploy Flower SuperLink servers (flower-server), SuperNode clients (flower-client), and federated training applications (flower-app).
---

# Flower Federated Learning Runtime (`flower-server`, `flower-client`, `flower-app`)

The **Flower runtime** (`digitalhub-runtime-flower`) orchestrates federated learning across distributed data silos on Kubernetes using three cooperating Function kinds:

1. **`flower-server`**: Deploys the central Flower SuperLink aggregation server (`flower-server+build`, `flower-server+deploy`).
2. **`flower-client`**: Deploys a Flower SuperNode participant connected to a SuperLink (`flower-client+build`, `flower-client+deploy`).
3. **`flower-app`**: Submits a federated training job (`ClientApp` + `ServerApp` fabs) to an active SuperLink (`flower-app+train`).

## Workflow via `dhcli`

1. Create and deploy the `flower-server` function (`dhcli run flower-server+deploy -p my-project -n fl-server`).
2. Create and deploy one or more `flower-client` functions pointing `spec.superlink` to the server's internal service address (`dhcli run flower-client+deploy -p my-project -n fl-client-1 -f client-run.yaml`).
3. Create the `flower-app` function and launch federated training (`dhcli run flower-app+train -p my-project -n fl-train-app -f train-run.yaml`).

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `flower-app`

Schema: `schemas/specs/function/flower-app.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.base_image` | string |  |  |
| `spec.fab_source` | object (FlowerSourceCode) |  | Source code |
| `spec.fab_source.clientapp` | string |  |  |
| `spec.fab_source.clientbase64` | string |  | Client Source Code |
| `spec.fab_source.serverapp` | string |  |  |
| `spec.fab_source.serverbase64` | string |  | Server Source Code |
| `spec.fab_source.source` | string |  |  |
| `spec.image` | string |  |  |
| `spec.requirements` | array<string> |  | List of requirements (formatted as requirements.txt) |

#### Task `flower-app+train` → run kind `flower-app+train:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.federation` | string |  |  |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.root_certificates` | string |  |  |
| `spec.secrets` | array<string> |  |  |
| `spec.superlink` | string |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

### Function kind `flower-server`

Schema: `schemas/specs/function/flower-server.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.base_image` | string |  |  |
| `spec.image` | string |  |  |
| `spec.requirements` | array<string> |  | List of requirements (formatted as requirements.txt) |

#### Task `flower-server+build` → run kind `flower-server+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.auth_public_keys` | array<string> |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.insecure` | boolean |  |  |
| `spec.instructions` | array<string> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `flower-server+deploy` → run kind `flower-server+deploy:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.auth_public_keys` | array<string> |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.insecure` | boolean |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

### Function kind `flower-client`

Schema: `schemas/specs/function/flower-client.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.base_image` | string |  |  |
| `spec.image` | string |  |  |
| `spec.requirements` | array<string> |  | List of requirements (formatted as requirements.txt) |

#### Task `flower-client+build` → run kind `flower-client+build:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.instructions` | array<string> |  |  |
| `spec.isolation` | enum: `process`, `subprocess` |  | default `"subprocess"` |
| `spec.node_config` | map<string, serializable> |  |  |
| `spec.private_key_secret` | string |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.public_key_secret` | string |  |  |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.root_certificates` | string |  |  |
| `spec.secrets` | array<string> |  |  |
| `spec.superlink` | string |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

#### Task `flower-client+deploy` → run kind `flower-client+deploy:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.isolation` | enum: `process`, `subprocess` |  | default `"subprocess"` |
| `spec.node_config` | map<string, serializable> |  |  |
| `spec.private_key_secret` | string |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.public_key_secret` | string |  |  |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.root_certificates` | string |  |  |
| `spec.secrets` | array<string> |  |  |
| `spec.superlink` | string |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
