---
title: KubeAI Serve Runtime (Text & Speech)
description: Autoscaled LLM, embedding, and Whisper speech serving on KubeAI using VLLM or OLlama engines (kubeai-text+serve, kubeai-speech+serve).
---

# KubeAI Serve Runtime (`kubeai-text`, `kubeai-speech`)

The **KubeAI runtime** deploys OpenAI-compatible text generation, embedding, reranking (`kubeai-text`), and speech-to-text (`kubeai-speech`) models managed by KubeAI with scale-to-zero and LoRA adapter support.

- **Supported function kinds & tasks**:
  - `kubeai-text` → `kubeai-text+serve` (`features`: `TextGeneration`, `TextEmbedding`, `Reranking`)
  - `kubeai-speech` → `kubeai-speech+serve` (`features`: `SpeechToText`)
- **Supported engines**: `OLlama`, `VLLM`

## 1. Deploying an LLM on KubeAI (`kubeai-text`)

```yaml
# function.yaml
kind: kubeai-text
name: llama3-kubeai
project: my-project
metadata:
  description: "Llama 3.2 3B Instruct via KubeAI"
spec:
  model_name: llama3
  url: "hf://meta-llama/Llama-3.2-3B-Instruct"
  engine: VLLM
  features:
    - TextGeneration
```

```yaml
# run.yaml
spec:
  profile: "gpu-a100-1x"
  scaling:
    min_replicas: 1
    max_replicas: 2
  secrets:
    - HF_TOKEN
```

```bash
dhcli create functions -p my-project -f function.yaml
dhcli run kubeai-text+serve -p my-project -n llama3-kubeai -f run.yaml
dhcli services -p my-project -o json
dhcli port-forward -p my-project -f llama3-kubeai -l 8000
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `kubeai-text`

Schema: `schemas/specs/function/kubeai-text.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.adapters` | array<object (KubeAIAdapter)> |  |  |
| `spec.engine` | enum: `OLlama`, `VLLM`, `Infinity` | **yes** |  |
| `spec.features` | array<enum: `TextGeneration`, `TextEmbedding`> | **yes** |  |
| `spec.image` | string |  |  |
| `spec.model_name` | string |  | default `"model"` |
| `spec.url` | string | **yes** | URL to the model (s3://, hf://, store://, ollama://); pattern `^(store://([^/]+)/model/huggingface/.*)|^pvc?://.*$|^s3?://.*$|^ollama?://.*$|^hf?://.*$` |

#### Task `kubeai-text+serve` → run kind `kubeai-text+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.cache_profile` | string |  |  |
| `spec.env` | map<string, string> |  |  |
| `spec.files` | array<object (KubeAIFile)> |  | Files to be mounted in the model Pods |
| `spec.processors` | integer |  |  |
| `spec.profile` | string |  |  |
| `spec.scaling` | object (KubeAIScaling) |  | Scaling configuration |
| `spec.scaling.autoscaling_disabled` | boolean |  | will stop the controller from managing the replicas for the Model |
| `spec.scaling.load_balancing` | object (KubeAILoadBalancing) |  |  |
| `spec.scaling.max_replicas` | integer |  | maximum number of Pod replicas that the model can scale up to. |
| `spec.scaling.min_replicas` | integer |  | minimum number of Pod replicas that the model can scale down to. |
| `spec.scaling.replicas` | integer |  | number of Pod replicas that should be actively serving the model |
| `spec.scaling.scale_down_delay_seconds` | integer |  | minimum time before a deployment is scaled down after the autoscaling algorithm determines that it should be scaled down |
| `spec.scaling.target_requests` | integer |  | average number of active requests that the autoscaler will try to maintain on model server Pods. |
| `spec.secrets` | array<string> |  |  |
| `spec.url` | string |  | URL to the model (s3://, hf://, store://, ollama://); pattern `^(store://([^/]+)/model/huggingface/.*)|^pvc?://.*$|^s3?://.*$|^ollama?://.*$|^hf?://.*$` |

### Function kind `kubeai-speech`

Schema: `schemas/specs/function/kubeai-speech.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.adapters` | array<object (KubeAIAdapter)> |  |  |
| `spec.image` | string |  |  |
| `spec.model_name` | string |  | default `"model"` |
| `spec.url` | string | **yes** | URL to the model (s3://, hf://, store://, ollama://); pattern `^(store://([^/]+)/model/huggingface/.*)|^pvc?://.*$|^s3?://.*$|^ollama?://.*$|^hf?://.*$` |

#### Task `kubeai-speech+serve` → run kind `kubeai-speech+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.cache_profile` | string |  |  |
| `spec.env` | map<string, string> |  |  |
| `spec.files` | array<object (KubeAIFile)> |  | Files to be mounted in the model Pods |
| `spec.processors` | integer |  |  |
| `spec.profile` | string |  |  |
| `spec.scaling` | object (KubeAIScaling) |  | Scaling configuration |
| `spec.scaling.autoscaling_disabled` | boolean |  | will stop the controller from managing the replicas for the Model |
| `spec.scaling.load_balancing` | object (KubeAILoadBalancing) |  |  |
| `spec.scaling.max_replicas` | integer |  | maximum number of Pod replicas that the model can scale up to. |
| `spec.scaling.min_replicas` | integer |  | minimum number of Pod replicas that the model can scale down to. |
| `spec.scaling.replicas` | integer |  | number of Pod replicas that should be actively serving the model |
| `spec.scaling.scale_down_delay_seconds` | integer |  | minimum time before a deployment is scaled down after the autoscaling algorithm determines that it should be scaled down |
| `spec.scaling.target_requests` | integer |  | average number of active requests that the autoscaler will try to maintain on model server Pods. |
| `spec.secrets` | array<string> |  |  |
| `spec.url` | string |  | URL to the model (s3://, hf://, store://, ollama://); pattern `^(store://([^/]+)/model/huggingface/.*)|^pvc?://.*$|^s3?://.*$|^ollama?://.*$|^hf?://.*$` |

<!-- END GENERATED: spec-reference -->
