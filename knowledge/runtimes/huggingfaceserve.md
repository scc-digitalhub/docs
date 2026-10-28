---
title: HuggingFace Serve Runtime
description: Deploy HuggingFace Transformer and PyTorch models via KServe HuggingFace serving runtime (huggingfaceserve+serve).
---

# HuggingFace Serve Runtime (`kind: huggingfaceserve`)

The **HuggingFace Serve runtime** deploys a HuggingFace Hub model (`hf://org/model-id`) or a project `kind: huggingface` Model (`store://...`) using the KServe HuggingFace server for sequence classification, token classification, fill-mask, or text generation.

- **Supported task**: `huggingfaceserve+serve` → `huggingfaceserve+serve:run`

## Creating & Running via `dhcli`

```yaml
# function.yaml
kind: huggingfaceserve
name: sentiment-hf-service
project: my-project
metadata:
  description: "DistilBERT sentiment classifier"
spec:
  model_name: sentiment
  path: "hf://distilbert/distilbert-base-uncased-finetuned-sst-2-english"
```

```yaml
# run.yaml
spec:
  huggingface_task: text_classification
  resources:
    cpu: "2"
    mem: "4Gi"
```

```bash
dhcli create functions -p my-project -f function.yaml
dhcli run huggingfaceserve+serve -p my-project -n sentiment-hf-service -f run.yaml
dhcli services -p my-project -o json
dhcli port-forward -p my-project -f sentiment-hf-service -l 8080
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `huggingfaceserve`

Schema: `schemas/specs/function/huggingfaceserve.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.image` | string |  | Container image used for tasks; pattern `^(kserve\/huggingfaceserver?:).*` |
| `spec.model_name` | string |  | default `"model"` |
| `spec.path` | string | **yes** | URI pointing to the content; pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |

#### Task `huggingfaceserve+serve` → run kind `huggingfaceserve+serve:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.args` | array<string> |  |  |
| `spec.backend` | enum: `AUTO`, `VLLM`, `HUGGINGFACE` |  |  |
| `spec.disable_log_requests` | boolean |  |  |
| `spec.disable_lower_case` | boolean |  |  |
| `spec.disable_special_tokens` | boolean |  |  |
| `spec.dtype` | enum: `AUTO`, `FLOAT16`, `FLOAT32`, `BFLOAT16`, `FLOAT`, `HALF` |  |  |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.huggingface_task` | enum: `sequence_classification`, `token_classification`, `fill_mask`, `text_generation`, `text2text_generation`, `text_embedding` |  |  |
| `spec.max_length` | integer |  |  |
| `spec.max_log_len` | integer |  |  |
| `spec.path` | string |  | URI pointing to the content; pattern `^(store://([^/]+)/model/huggingface/.*)|.*/$|.*\.zip$|^huggingface?://.*$|^hf?://.*$` |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.replicas` | integer |  | Number of replicas for the current task |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.return_probabilities` | boolean |  |  |
| `spec.return_token_type_ids` | boolean |  |  |
| `spec.secrets` | array<string> |  |  |
| `spec.service_name` | string |  | Name of the service exposed |
| `spec.service_type` | enum: `ExternalName`, `ClusterIP`, `NodePort`, `LoadBalancer` |  | Select the type used for service definition; default `"ClusterIP"` |
| `spec.tensor_input_names` | array<string> |  |  |
| `spec.tokenizer_revision` | string |  |  |
| `spec.trust_remote_code` | boolean |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
