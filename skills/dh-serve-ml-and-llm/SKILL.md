---
name: dh-serve-ml-and-llm
description: Deploy trained Machine Learning models (sklearnserve, mlflowserve, huggingfaceserve) and OpenAI-compatible LLMs/Embeddings/Whisper services (kubeai-text, kubeai-speech) using dhcli.
---

# Skill: Serving ML Models & OpenAI-Compatible LLMs

Use this procedural workflow to deploy trained Scikit-Learn, MLflow, or HuggingFace models via KServe/Seldon V2 (`sklearnserve`, `mlflowserve`, `huggingfaceserve`) or to launch OpenAI-compatible LLM, Embedding, and Speech endpoints via KubeAI (`kubeai-text`, `kubeai-speech`).

## Reference Knowledge
- [specs-functions-and-runtimes.md](../../knowledge/cli/specs-functions-and-runtimes.md)
- [specs-data-and-storage.md](../../knowledge/cli/specs-data-and-storage.md)
- [kubernetes-resources.md](../../knowledge/management/kubernetes-resources.md)
- [keys-and-lifecycle.md](../../knowledge/management/keys-and-lifecycle.md)

---

## Track A: Serving Classical ML & HuggingFace Models (`sklearnserve`, `mlflowserve`, `huggingfaceserve`)

### Step 1: Verify the Model Entity and Capture its `store://` Key
Ensure the model is already logged or registered in the project and is in state `READY`:
```bash
dhcli get model <model-name> -p <project-name> -o yaml
```
Copy the model's `key` (e.g., `store://<project-name>/model/sklearn/<model-name>:<model-uuid>`).

### Step 2: Create the Model Serving Function
Select the runtime `kind` matching your model (`sklearnserve`, `mlflowserve`, or `huggingfaceserve`) and create `serve-fn.yaml`:
```yaml
project: <project-name>
kind: sklearnserve
name: <service-name>
metadata:
  description: "Real-time inference endpoint for <model-name>"
spec:
  model_name: <model-name>
  path: "store://<project-name>/model/sklearn/<model-name>:<model-uuid>"
```
Apply the Function and note its `id` (`<func-uuid>`):
```bash
dhcli create -f serve-fn.yaml -p <project-name>
```

### Step 3: Execute the Serve Run (`<kind>+serve:run`)
Create `serve-run.yaml`:
```yaml
project: <project-name>
kind: sklearnserve+serve:run
spec:
  function: "sklearnserve://<project-name>/<service-name>:<func-uuid>"
  resources:
    cpu:
      requests: "500m"
      limits: "2"
    mem:
      requests: "1Gi"
      limits: "4Gi"
```
Deploy and verify:
```bash
dhcli execute -f serve-run.yaml -p <project-name>
dhcli get run <serve-run-uuid> -p <project-name> -o yaml
```

### Step 4: Invoke the V2 Open Inference Protocol Endpoint
Once `status.state` is `RUNNING`, inspect `status.service.url` or tunnel locally (`dhcli http <serve-run-uuid> -p <project-name> --port 8080`) and send a V2 inference payload:
```bash
curl -X POST http://localhost:8080/v2/models/<model-name>/infer \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": [
      {
        "name": "input-0",
        "shape": [1, 4],
        "datatype": "FP32",
        "data": [[5.1, 3.5, 1.4, 0.2]]
      }
    ]
  }'
```

---

## Track B: Serving LLMs, Embeddings & Speech via KubeAI (`kubeai-text`, `kubeai-speech`)

### Step 1: Create the KubeAI Function (`kubeai-text` or `kubeai-speech`)
Choose `engine` (`VLLM` or `OLlama` for text; `FasterWhisper` for speech) and `features` (`["TextGeneration"]`, `["TextEmbedding"]`, or `["SpeechToText"]`):
```yaml
project: <project-name>
kind: kubeai-text
name: llm-chat-service
spec:
  model_name: llama3-8b-instruct
  url: "hf://meta-llama/Meta-Llama-3-8B-Instruct"
  engine: VLLM
  features:
    - TextGeneration
  args:
    - "--max-model-len=8192"
  secrets:
    - HF_TOKEN
```
```bash
dhcli create -f kubeai-fn.yaml -p <project-name>
```

### Step 2: Execute the KubeAI Serve Run with GPU Profile & Scaling
Create `kubeai-serve-run.yaml`:
```yaml
project: <project-name>
kind: kubeai-text+serve:run
spec:
  function: "kubeai-text://<project-name>/llm-chat-service:<func-uuid>"
  profile: "1xa100"
  scaling:
    replicas: 1
    min_replicas: 0
    max_replicas: 2
```
```bash
dhcli execute -f kubeai-serve-run.yaml -p <project-name>
```

### Step 3: Query the OpenAI-Compatible API
Once `status.state` is `RUNNING`, query `/v1/chat/completions` (or `/v1/embeddings` / `/v1/audio/transcriptions`) using `model: "llama3-8b-instruct"`.

