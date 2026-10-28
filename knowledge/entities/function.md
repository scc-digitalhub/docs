---
title: Function Entity
description: Executable template entity across 16 runtimes (python, container, dbt, serving, flower, guardrail) created via dhcli create functions and executed via dhcli run.
---

# Function Entity (`functions`)

A **Function** defines an executable template—source code, container image, model reference, or transformation query—configured for a specific DigitalHub runtime `kind`.

- **Function reference URI**: `<kind>://<project>/<name>:<uuid>` (e.g., `python://my-project/train-fn:a1b2c3d4-...`)
- **Versioning**: Functions are versioned. `spec` is immutable on an existing version; running `dhcli create functions -p <project> -f function.yaml` with the same `name` creates a new version UUID.

## 1. Supported Function Kinds & Runtimes

| Runtime Page | Function `kind`(s) | `dhcli run <task>` Actions | Purpose |
| :--- | :--- | :--- | :--- |
| [**python**](../runtimes/python.md) | `python` | `python+build`, `python+job`, `python+serve` | Python batch jobs and Nuclio HTTP serverless endpoints. |
| [**container**](../runtimes/container.md) | `container` | `container+build`, `container+job`, `container+serve`, `container+deploy` | Custom Docker/OCI container batch jobs, services, and deployments. |
| [**dbt**](../runtimes/dbt.md) | `dbt` | `dbt+transform` | SQL transformations over `table` Dataitems in PostgreSQL/Dremio. |
| [**sklearnserve**](../runtimes/sklearnserve.md) | `sklearnserve` | `sklearnserve+serve` | Serve Scikit-Learn models via KServe OpenInference v2. |
| [**mlflowserve**](../runtimes/mlflowserve.md) | `mlflowserve` | `mlflowserve+build`, `mlflowserve+serve` | Serve MLflow models via KServe OpenInference v2. |
| [**huggingfaceserve**](../runtimes/huggingfaceserve.md) | `huggingfaceserve` | `huggingfaceserve+serve` | Serve HuggingFace models via KServe. |
| [**vllmserve**](../runtimes/vllmserve.md) | `vllmserve-text`, `vllmserve-speech`, `vllmserve-pooling` | `vllmserve-text+serve`, `vllmserve-speech+serve`, `vllmserve-pooling+serve` | High-throughput LLM, speech, and embedding serving on vLLM. |
| [**kubeai**](../runtimes/kubeai.md) | `kubeai-text`, `kubeai-speech` | `kubeai-text+serve`, `kubeai-speech+serve` | Autoscaled OpenAI-compatible LLM and Whisper serving on KubeAI. |
| [**openinference**](../runtimes/openinference.md) | `openinference` | `openinference+build`, `openinference+serve` | Custom Python inference handler using OpenInference v2 protocol. |
| [**guardrail**](../runtimes/guardrail.md) | `guardrail` | `guardrail+build`, `guardrail+serve` | LLM input/output safety guardrail validation service. |
| [**flower**](../runtimes/flower.md) | `flower-app`, `flower-server`, `flower-client` | `flower-app+train`, `flower-server+build`, `flower-server+deploy`, `flower-client+build`, `flower-client+deploy` | Federated learning training apps, SuperLink servers, and SuperNode clients. |

## 2. CLI Lifecycle (`dhcli`)

```bash
# 1. Create a function (or a new version of an existing function name)
dhcli create functions -p my-project -f function.yaml

# 2. Get the latest version of a function by name
dhcli get functions -p my-project -n my-fn -o json

# 3. List all functions in a project (or all versions of one function with -n)
dhcli list functions -p my-project
dhcli list functions -p my-project -n my-fn -o json

# 4. Execute the function (auto-resolves the function and task, and creates a Run)
dhcli run python+job -p my-project -n my-fn -f run.yaml

# 5. Delete a specific version by UUID, or all versions by name (-n)
dhcli delete functions <uuid> -p my-project -y
dhcli delete functions -p my-project -n my-fn -y
```

## 3. Source Code Rules for Code-Backed Functions (`python`, `dbt`, `openinference`, `guardrail`, `flower-*`)

When creating code-backed functions via `dhcli create functions -f function.yaml`:
- Source fields (`lang`, `handler`, `base64`, `source`, `init_function`) **MUST be nested inside `spec.source`**.
- `dhcli create` sends the YAML directly to Core without reading local `.py` or `.sql` files from disk. Always Base64-encode local single-file scripts (`base64 -i handler.py | tr -d '\n'`) into `spec.source.base64`, or reference a remote `git+https://...` or `s3://...` URI in `spec.source.source`.
