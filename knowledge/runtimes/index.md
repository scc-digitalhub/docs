---
title: Runtimes Overview
description: Master decision matrix and task mapping for all DigitalHub Function and Workflow runtimes (Python, Container, DBT, Hera, KFP, ModelServe, vLLM, KubeAI, OpenInference, Guardrail, Flower).
---

# DigitalHub Platform Runtimes

A **Runtime** connects a declarative `Function` or `Workflow` entity to a concrete execution engine on Kubernetes (K8s Jobs, Nuclio serverless functions, KServe inference services, vLLM, KubeAI, Argo Workflows, Kubeflow Pipelines, or Flower federated learning).

## 1. Choosing the Right Runtime

- **Custom Python ETL, data processing, ML training, or REST microservice** → [`python`](python.md) (`python+build`, `python+job`, `python+serve`).
- **Pre-built Docker image, web app (Streamlit/Gradio/FastAPI), or custom binary** → [`container`](container.md) (`container+build`, `container+job`, `container+serve`, `container+deploy`).
- **SQL transformation over `table` Dataitems in PostgreSQL/Dremio** → [`dbt`](dbt.md) (`dbt+transform`).
- **Multi-step DAG pipeline orchestrating several functions** → [`hera`](hera.md) (Argo Workflows) or [`kfp`](kfp.md) (Kubeflow Pipelines).
- **Serving a trained classical ML or MLflow model (`sklearn`, `mlflow`, `huggingface`)** → [`sklearnserve`](sklearnserve.md), [`mlflowserve`](mlflowserve.md), [`huggingfaceserve`](huggingfaceserve.md).
- **Serving LLMs, speech-to-text (Whisper), or embedding models on GPUs** → [`vllmserve`](vllmserve.md) or [`kubeai`](kubeai.md).
- **Custom Python inference logic speaking the OpenInference v2 protocol** → [`openinference`](openinference.md).
- **LLM input/output safety guardrail validation service** → [`guardrail`](guardrail.md).
- **Federated learning across distributed nodes** → [`flower`](flower.md).

## 2. How Runtime Tasks Map to `dhcli run`

Every function runtime exposes one or more **task kinds** formatted as `<function-kind>+<action>`:

```bash
dhcli run <function-kind>+<action> -p <project> -n <function-name> [-f run.yaml]
```

<!-- BEGIN GENERATED: runtime-matrix -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

| Runtime page | Entity | Kind | Tasks (`dhcli run <task>`) | Run kind(s) |
| :--- | :--- | :--- | :--- | :--- |
| [python](python.md) | function | `python` | `python+build`, `python+job`, `python+serve` | `python+build:run`, `python+job:run`, `python+serve:run` |
| [container](container.md) | function | `container` | `container+build`, `container+deploy`, `container+job`, `container+serve` | `container+build:run`, `container+deploy:run`, `container+job:run`, `container+serve:run` |
| [dbt](dbt.md) | function | `dbt` | `dbt+transform` | `dbt+transform:run` |
| [hera](hera.md) | workflow | `hera` | `hera+build`, `hera+pipeline` | `hera+build:run`, `hera+pipeline:run` |
| [kfp](kfp.md) | workflow | `kfp` | `kfp+build`, `kfp+pipeline` | `kfp+build:run`, `kfp+pipeline:run` |
| [sklearnserve](sklearnserve.md) | function | `sklearnserve` | `sklearnserve+serve` | `sklearnserve+serve:run` |
| [mlflowserve](mlflowserve.md) | function | `mlflowserve` | `mlflowserve+build`, `mlflowserve+serve` | `mlflowserve+build:run`, `mlflowserve+serve:run` |
| [huggingfaceserve](huggingfaceserve.md) | function | `huggingfaceserve` | `huggingfaceserve+serve` | `huggingfaceserve+serve:run` |
| [vllmserve](vllmserve.md) | function | `vllmserve-text` | `vllmserve-text+serve` | `vllmserve-text+serve:run` |
| [vllmserve](vllmserve.md) | function | `vllmserve-speech` | `vllmserve-speech+serve` | `vllmserve-speech+serve:run` |
| [vllmserve](vllmserve.md) | function | `vllmserve-pooling` | `vllmserve-pooling+serve` | `vllmserve-pooling+serve:run` |
| [kubeai](kubeai.md) | function | `kubeai-text` | `kubeai-text+serve` | `kubeai-text+serve:run` |
| [kubeai](kubeai.md) | function | `kubeai-speech` | `kubeai-speech+serve` | `kubeai-speech+serve:run` |
| [openinference](openinference.md) | function | `openinference` | `openinference+build`, `openinference+serve` | `openinference+build:run`, `openinference+serve:run` |
| [guardrail](guardrail.md) | function | `guardrail` | `guardrail+build`, `guardrail+serve` | `guardrail+build:run`, `guardrail+serve:run` |
| [flower](flower.md) | function | `flower-app` | `flower-app+train` | `flower-app+train:run` |
| [flower](flower.md) | function | `flower-server` | `flower-server+build`, `flower-server+deploy` | `flower-server+build:run`, `flower-server+deploy:run` |
| [flower](flower.md) | function | `flower-client` | `flower-client+build`, `flower-client+deploy` | `flower-client+build:run`, `flower-client+deploy:run` |

<!-- END GENERATED: runtime-matrix -->
