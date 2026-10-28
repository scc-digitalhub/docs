---
title: vLLM Serve Runtime (Text, Speech, Pooling)
description: High-throughput GPU serving for LLMs (vllmserve-text), ASR speech models (vllmserve-speech), and embeddings/rerankers (vllmserve-pooling) with an OpenAI-compatible API.
---

# vLLM Serve Runtime (`vllmserve-text`, `vllmserve-speech`, `vllmserve-pooling`)

The **vLLM Serve runtime** deploys LLMs, speech-to-text models, and embedding/pooling models on vLLM, exposing an **OpenAI-compatible REST API** (`/v1/chat/completions`, `/v1/completions`, `/v1/audio/transcriptions`, `/v1/embeddings`).

- **Supported function kinds & tasks**:
  - `vllmserve-text` → `vllmserve-text+serve`
  - `vllmserve-speech` → `vllmserve-speech+serve`
  - `vllmserve-pooling` → `vllmserve-pooling+serve`

## 1. Deploying an LLM (`vllmserve-text`)

```yaml
# function.yaml
kind: vllmserve-text
name: qwen-instruct-vllm
project: my-project
metadata:
  description: "Qwen 2.5 Instruct on vLLM"
spec:
  model_name: llm
  url: "hf://Qwen/Qwen2.5-1.5B-Instruct"
```

```yaml
# run.yaml
spec:
  args:
    - "--max-model-len=4096"
  secrets:
    - HF_TOKEN
  resources:
    cpu: "4"
    mem: "16Gi"
    gpu: "1"
```

```bash
dhcli create functions -p my-project -f function.yaml
dhcli run vllmserve-text+serve -p my-project -n qwen-instruct-vllm -f run.yaml

# Wait until status.state is RUNNING, then port-forward locally
dhcli services -p my-project -o json
dhcli port-forward -p my-project -f qwen-instruct-vllm -l 8000
```

## 2. Calling the OpenAI-Compatible Endpoint

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llm",
    "messages": [{"role": "user", "content": "Summarize DigitalHub in one sentence."}]
  }'
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `vllmserve-text`

Schema: `schemas/specs/function/vllmserve-text.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.adapters` | array<object (VLLMAdapter)> |  |  |
| `spec.image` | string |  | Container image used for tasks; pattern `^vllm\/vllm-openai(:.*)?$` |
| `spec.model_name` | string |  | default `"model"` |
| `spec.url` | string | **yes** | URL to the model (s3://, hf://, store://); pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |

#### Task `vllmserve-text+serve` → run kind `vllmserve-text+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.enable_telemetry` | boolean |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
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
| `spec.url` | string |  | URL to the model (s3://, hf://, store://); pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |
| `spec.use_cpu_image` | boolean |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

### Function kind `vllmserve-speech`

Schema: `schemas/specs/function/vllmserve-speech.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.adapters` | array<object (VLLMAdapter)> |  |  |
| `spec.image` | string |  | Container image used for tasks; pattern `^vllm\/vllm-openai(:.*)?$` |
| `spec.model_name` | string |  | default `"model"` |
| `spec.url` | string | **yes** | URL to the model (s3://, hf://, store://); pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |

#### Task `vllmserve-speech+serve` → run kind `vllmserve-speech+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.enable_telemetry` | boolean |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
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
| `spec.url` | string |  | URL to the model (s3://, hf://, store://); pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |
| `spec.use_cpu_image` | boolean |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

### Function kind `vllmserve-pooling`

Schema: `schemas/specs/function/vllmserve-pooling.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.adapters` | array<object (VLLMAdapter)> |  |  |
| `spec.image` | string |  | Container image used for tasks; pattern `^vllm\/vllm-openai(:.*)?$` |
| `spec.model_name` | string |  | default `"model"` |
| `spec.url` | string | **yes** | URL to the model (s3://, hf://, store://); pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |

#### Task `vllmserve-pooling+serve` → run kind `vllmserve-pooling+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.enable_telemetry` | boolean |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
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
| `spec.url` | string |  | URL to the model (s3://, hf://, store://); pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |
| `spec.use_cpu_image` | boolean |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
