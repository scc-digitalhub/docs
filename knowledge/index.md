---
type: knowledge_catalog
name: digitalhub_knowledge_catalog
version: "0.16"
description: "Master Open Knowledge Format (OKF) catalog for the DigitalHub platform, centered on Entities (Core Domain), Runtimes (Execution Engines), CLI (dhcli), Python SDK (In-Container Handlers & Fallback), and Management (Architecture, K8s Resources, Governance & Troubleshooting)."
domains:
  - id: "entities"
    title: "DigitalHub Entities (Core Domain Model)"
    path: "entities/index.md"
    description: "Schema-generated specifications, URI keys, versioning rules, and dhcli recipes for all 10 DigitalHub entities (project, function, workflow, task, run, artifact, dataitem, model, secret, trigger)."
  - id: "runtimes"
    title: "DigitalHub Runtimes (Execution Engines)"
    path: "runtimes/index.md"
    description: "Schema-generated specifications, task mappings (`<kind>+<action>`), and end-to-end recipes for all 13 runtime families (python, container, dbt, hera, kfp, sklearnserve, mlflowserve, huggingfaceserve, vllmserve, kubeai, openinference, guardrail, flower)."
  - id: "cli"
    title: "DigitalHub CLI (dhcli) Command Reference"
    path: "cli/index.md"
    description: "Verified dhcli command reference, flags, authentication, CRUD operations, run monitoring, S3 transfers, and service tunneling."
  - id: "sdk"
    title: "DigitalHub Python SDK & Handler Authoring"
    path: "sdk/index.md"
    description: "In-container Python handler authoring (`def handler(project, run, ...):`), Dataitem/Artifact/Model I/O, metric logging, Hera/KFP pipeline DSL, and SDK fallback for CLI gaps."
  - id: "management"
    title: "DigitalHub Platform Architecture, Governance & Troubleshooting"
    path: "management/index.md"
    description: "Platform architecture, `store://` URI semantics, entity lifecycle and versioning, Kubernetes resource/volume profiles, governance standards, and error troubleshooting."
topics:
  # --- PILLAR 1: ENTITIES (Core Domain) ---
  - id: "entities"
    domain: "entities"
    type: "domain_index"
    title: "Entities Overview"
    path: "entities/index.md"
    tags: [entities, overview, project, function, workflow, artifact, dataitem, model, run, task, secret, trigger]
    summary: "Core reference index for all DigitalHub Platform entities, their URI schemes, versioning semantics, and dhcli CRUD support."
  - id: "project"
    domain: "entities"
    type: "entity_specification"
    title: "Project Entity"
    path: "entities/project.md"
    tags: [project, workspace, namespace, crud, dhcli]
    summary: "Top-level multi-tenant workspace and namespace for all DigitalHub entities, default storage configuration, and project CRUD via dhcli."
  - id: "function"
    domain: "entities"
    type: "entity_specification"
    title: "Function Entity"
    path: "entities/function.md"
    tags: [function, executable, python, container, dbt, serving, flower, guardrail, dhcli]
    summary: "Executable template entity across 16 runtimes created via dhcli create functions and executed via dhcli run."
  - id: "workflow"
    domain: "entities"
    type: "entity_specification"
    title: "Workflow Entity"
    path: "entities/workflow.md"
    tags: [workflow, hera, kfp, argo, pipeline, dag]
    summary: "Multi-step DAG pipelines authored in Hera (Argo Workflows) or KFP (Kubeflow Pipelines), registered via dhcli and executed via the SDK fallback."
  - id: "task"
    domain: "entities"
    type: "entity_specification"
    title: "Task Entity"
    path: "entities/task.md"
    tags: [task, action, build, job, serve, pipeline]
    summary: "Intermediary binding between a Function/Workflow and an execution action (build, job, serve, pipeline) auto-managed by dhcli run."
  - id: "run"
    domain: "entities"
    type: "entity_specification"
    title: "Run Entity"
    path: "entities/run.md"
    tags: [run, execution, state, logs, metrics, stop, dhcli]
    summary: "Immutable execution instance of a Function or Workflow task, its lifecycle state machine, run.yaml anatomy, logs, metrics, and stopping runs via dhcli."
  - id: "artifact"
    domain: "entities"
    type: "entity_specification"
    title: "Artifact Entity"
    path: "entities/artifact.md"
    tags: [artifact, files, s3, upload, download, dhcli]
    summary: "Unstructured files, archives, plots, and bundles stored in S3 object storage and managed via dhcli upload, download, and CRUD commands."
  - id: "dataitem"
    domain: "entities"
    type: "entity_specification"
    title: "Dataitem Entity"
    path: "entities/dataitem.md"
    tags: [dataitem, table, croissant, dataset, parquet, csv, sql, s3, upload, download]
    summary: "Structured tabular datasets (table), generic datasets (dataitem), and Croissant ML metadata datasets (croissant) backed by S3 or SQL stores."
  - id: "model"
    domain: "entities"
    type: "entity_specification"
    title: "Model Entity"
    path: "entities/model.md"
    tags: [model, sklearn, mlflow, huggingface, weights, s3, upload, serving]
    summary: "Versioned ML and DL model artifacts (sklearn, mlflow, huggingface, model) with lineage, metrics, and direct deployment to serving runtimes."
  - id: "secret"
    domain: "entities"
    type: "entity_specification"
    title: "Secret Entity"
    path: "entities/secret.md"
    tags: [secret, kubernetes, credentials, env, security]
    summary: "Project-scoped sensitive credentials backed by Kubernetes Secrets and injected as environment variables into Function and Workflow runs."
  - id: "trigger"
    domain: "entities"
    type: "entity_specification"
    title: "Trigger Entity"
    path: "entities/trigger.md"
    tags: [trigger, scheduler, cron, lifecycle, events]
    summary: "Automated execution triggers (scheduler cron triggers and lifecycle event triggers) that launch Function or Workflow runs."

  # --- PILLAR 2: RUNTIMES (Execution Engines) ---
  - id: "runtimes"
    domain: "runtimes"
    type: "domain_index"
    title: "Runtimes Overview"
    path: "runtimes/index.md"
    tags: [runtimes, matrix, python, container, dbt, hera, kfp, serving, vllm, kubeai, flower]
    summary: "Master decision matrix and task mapping for all DigitalHub Function and Workflow runtimes."
  - id: "python"
    domain: "runtimes"
    type: "runtime_specification"
    title: "Python Runtime"
    path: "runtimes/python.md"
    tags: [runtime, python, job, serve, build, nuclio, base64, handler]
    summary: "Execute Python batch jobs (python+job), Nuclio serverless HTTP services (python+serve), and Kaniko container image builds (python+build) via dhcli."
  - id: "container"
    domain: "runtimes"
    type: "runtime_specification"
    title: "Container Runtime"
    path: "runtimes/container.md"
    tags: [runtime, container, docker, oci, job, serve, deploy, build]
    summary: "Run custom Docker/OCI images as Kubernetes batch jobs (container+job), HTTP services (container+serve), persistent deployments (container+deploy), or Kaniko image builds (container+build)."
  - id: "dbt"
    domain: "runtimes"
    type: "runtime_specification"
    title: "DBT Runtime"
    path: "runtimes/dbt.md"
    tags: [runtime, dbt, sql, transform, table, postgres]
    summary: "Run SQL data transformations over tabular Dataitems in PostgreSQL/Dremio using dbt (dbt+transform)."
  - id: "hera"
    domain: "runtimes"
    type: "runtime_specification"
    title: "Hera Workflow Runtime (Argo)"
    path: "runtimes/hera.md"
    tags: [runtime, hera, argo, workflow, pipeline, dag]
    summary: "Author and execute multi-step Argo Workflows DAG pipelines using the digitalhub_runtime_hera Python DSL."
  - id: "kfp"
    domain: "runtimes"
    type: "runtime_specification"
    title: "KFP Workflow Runtime (Kubeflow Pipelines)"
    path: "runtimes/kfp.md"
    tags: [runtime, kfp, kubeflow, workflow, pipeline, dag]
    summary: "Author and execute multi-step Kubeflow Pipelines DAGs using the digitalhub_runtime_kfp Python DSL."
  - id: "sklearnserve"
    domain: "runtimes"
    type: "runtime_specification"
    title: "Scikit-Learn Serve Runtime"
    path: "runtimes/sklearnserve.md"
    tags: [runtime, sklearnserve, sklearn, kserve, openinference, serve]
    summary: "Deploy Scikit-Learn (.pkl / .joblib) Model entities as KServe OpenInference v2 HTTP endpoints (sklearnserve+serve)."
  - id: "mlflowserve"
    domain: "runtimes"
    type: "runtime_specification"
    title: "MLflow Serve Runtime"
    path: "runtimes/mlflowserve.md"
    tags: [runtime, mlflowserve, mlflow, kserve, openinference, serve, build]
    summary: "Build and deploy MLflow Model entities as KServe OpenInference v2 HTTP services (mlflowserve+build, mlflowserve+serve)."
  - id: "huggingfaceserve"
    domain: "runtimes"
    type: "runtime_specification"
    title: "HuggingFace Serve Runtime"
    path: "runtimes/huggingfaceserve.md"
    tags: [runtime, huggingfaceserve, huggingface, kserve, serve]
    summary: "Deploy HuggingFace Transformer and PyTorch models via KServe HuggingFace serving runtime (huggingfaceserve+serve)."
  - id: "vllmserve"
    domain: "runtimes"
    type: "runtime_specification"
    title: "vLLM Serve Runtime (Text, Speech, Pooling)"
    path: "runtimes/vllmserve.md"
    tags: [runtime, vllmserve, vllm, llm, speech, pooling, embeddings, openai, gpu]
    summary: "High-throughput GPU serving for LLMs (vllmserve-text), ASR speech models (vllmserve-speech), and embeddings/rerankers (vllmserve-pooling) with an OpenAI-compatible API."
  - id: "kubeai"
    domain: "runtimes"
    type: "runtime_specification"
    title: "KubeAI Serve Runtime (Text & Speech)"
    path: "runtimes/kubeai.md"
    tags: [runtime, kubeai, kubeai-text, kubeai-speech, llm, whisper, ollama, vllm, openai]
    summary: "Autoscaled LLM, embedding, and Whisper speech serving on KubeAI using VLLM or OLlama engines (kubeai-text+serve, kubeai-speech+serve)."
  - id: "openinference"
    domain: "runtimes"
    type: "runtime_specification"
    title: "OpenInference Runtime"
    path: "runtimes/openinference.md"
    tags: [runtime, openinference, kserve, python, serve, build]
    summary: "Author custom Python inference handlers that expose a standardized KServe OpenInference v2 REST API (openinference+build, openinference+serve)."
  - id: "guardrail"
    domain: "runtimes"
    type: "runtime_specification"
    title: "Guardrail Runtime"
    path: "runtimes/guardrail.md"
    tags: [runtime, guardrail, safety, llm, serve, build]
    summary: "Deploy Python LLM input/output safety guardrail validation services (guardrail+build, guardrail+serve)."
  - id: "flower"
    domain: "runtimes"
    type: "runtime_specification"
    title: "Flower Federated Learning Runtime"
    path: "runtimes/flower.md"
    tags: [runtime, flower, flower-app, flower-server, flower-client, federated-learning]
    summary: "Deploy Flower SuperLink servers (flower-server), SuperNode clients (flower-client), and federated training applications (flower-app)."

  # --- PILLAR 3: CLI (Host Execution & Resource Management) ---
  - id: "cli"
    domain: "cli"
    type: "domain_index"
    title: "DigitalHub CLI (dhcli) Command Reference & Overview"
    path: "cli/index.md"
    tags: [cli, dhcli, commands, flags, resources, overview]
    summary: "Master index of dhcli commands, global flags, supported resource types, and CLI execution patterns."
  - id: "cli-auth-and-env"
    domain: "cli"
    type: "operational_guide"
    title: "CLI Environment Registration, Authentication & Configuration"
    path: "cli/auth-and-env.md"
    tags: [cli, dhcli, register, login, pat, use, list-env, refresh, config, credentials, init, dhcore.ini]
    summary: "Registering DigitalHub Core endpoints, OAuth2/PAT login, managing multiple environments in .dhcore.ini, inspecting credentials, and bootstrapping workspaces with dhcli init."
  - id: "cli-crud-and-yaml"
    domain: "cli"
    type: "operational_guide"
    title: "CLI Resource CRUD Operations & YAML Manifest Anatomy"
    path: "cli/crud-and-yaml-anatomy.md"
    tags: [cli, dhcli, create, get, list, update, delete, yaml, json, metadata, spec]
    summary: "Universal YAML manifest structure (kind, name, project, metadata, spec) and executing create, get, list, update, and delete via dhcli."
  - id: "cli-execution-and-runs"
    domain: "cli"
    type: "operational_guide"
    title: "CLI Task Execution, Run Monitoring, Logs & Metrics"
    path: "cli/execution-and-runs.md"
    tags: [cli, dhcli, run, log, metrics, stop, task, job, build, serve]
    summary: "Triggering function executions with dhcli run <kind>+<action>, passing run configuration YAML, reading container logs (dhcli log), reading pod metrics (dhcli metrics), and stopping runs."
  - id: "cli-storage-and-services"
    domain: "cli"
    type: "operational_guide"
    title: "CLI File Upload/Download & Service Networking (Port-Forward & Proxy)"
    path: "cli/storage-and-services.md"
    tags: [cli, dhcli, upload, download, s3, services, port-forward, proxy]
    summary: "Uploading and downloading artifacts/models/dataitems to S3 via dhcli upload/download, listing active services (dhcli services), and tunneling traffic via port-forward and proxy."

  # --- PILLAR 4: SDK (In-Container Handler Authoring & Fallback) ---
  - id: "sdk"
    domain: "sdk"
    type: "domain_index"
    title: "DigitalHub Python SDK & Handler Authoring Overview"
    path: "sdk/index.md"
    tags: [sdk, python, handler, overview, container]
    summary: "Overview of when and how to use the digitalhub Python SDK inside container handlers vs. dhcli on the host."
  - id: "sdk-handler-authoring"
    domain: "sdk"
    type: "operational_guide"
    title: "Writing Python Handlers (job, serve, expose)"
    path: "sdk/handler-authoring.md"
    tags: [sdk, python, handler, init_context, serve, job, inputs, parameters, context, event]
    summary: "Authoring Python functions executed by DigitalHub runtimes: injected arguments (project, run, context), input/parameter resolution, and Nuclio serve handlers."
  - id: "sdk-data-models-and-metrics"
    domain: "sdk"
    type: "operational_guide"
    title: "Reading Inputs & Logging DataItems, Models, Artifacts & Metrics"
    path: "sdk/data-models-and-metrics.md"
    tags: [sdk, dataitem, as_df, log_dataitem, log_artifact, log_model, log_sklearn, log_mlflow, log_huggingface, log_metric]
    summary: "In-handler SDK methods for reading tabular/file inputs and logging output datasets, models, artifacts, and evaluation metrics."
  - id: "sdk-workflow-pipelines-dsl"
    domain: "sdk"
    type: "operational_guide"
    title: "Authoring Hera (Argo) & KFP Pipeline DAGs in Python"
    path: "sdk/workflow-pipelines-dsl.md"
    tags: [sdk, workflow, hera, kfp, dsl, step, dag, pipeline]
    summary: "Writing multi-step DAG workflows in Python using digitalhub_runtime_hera.dsl and digitalhub_runtime_kfp.dsl."
  - id: "sdk-fallback"
    domain: "sdk"
    type: "operational_guide"
    title: "Python SDK Fallback for CLI Gaps"
    path: "sdk/sdk-fallback.md"
    tags: [sdk, fallback, workflow, secret, trigger, dhcli]
    summary: "Minimal one-line Python SDK recipes for operations not exposed as dhcli commands (executing workflows, creating secrets, and attaching triggers)."
  - id: "sdk-interactive-reference"
    domain: "sdk"
    type: "reference"
    title: "Interactive Notebook Python SDK Reference (import digitalhub as dh)"
    path: "sdk/interactive-sdk-reference.md"
    tags: [sdk, notebook, jupyter, get_or_create_project, new_function, run, export]
    summary: "Compact reference for interactive Python SDK usage inside Jupyter notebooks."

  # --- PILLAR 5: MANAGEMENT (Architecture, K8s Resources, Governance & Troubleshooting) ---
  - id: "management"
    domain: "management"
    type: "domain_index"
    title: "Platform Architecture & Management Overview"
    path: "management/index.md"
    tags: [management, architecture, overview, control-plane, storage]
    summary: "Three-layer DigitalHub platform architecture, entity relationship graph, and storage backend overview."
  - id: "management-keys-and-lifecycle"
    domain: "management"
    type: "operational_guide"
    title: "Entity Keys (store://), Source URIs, Versioning & State Machines"
    path: "management/keys-and-lifecycle.md"
    tags: [management, store, key, uri, s3, git, versioning, immutability, state, console]
    summary: "Exact store:// URI grammar, source code URI schemes (base64, git+https://, zip+s3://), entity versioning rules, Run state transitions, and Console UI URL routing."
  - id: "management-kubernetes-resources"
    domain: "management"
    type: "reference"
    title: "Kubernetes Resources, Profiles, Volumes, Envs, Secrets & Services"
    path: "management/kubernetes-resources.md"
    tags: [management, kubernetes, k8s, cpu, mem, gpu, profile, volumes, pvc, empty_dir, shared_volume, envs, secrets, service_ports, replicas]
    summary: "Configuring CPU/Memory/GPU requests & limits, hardware profiles, PVC/EmptyDir/Ephemeral volumes, environment variables, secrets, and service exposure in YAML specs."
  - id: "management-governance-and-security"
    domain: "management"
    type: "reference"
    title: "Platform Governance, Naming Conventions & Security Standards"
    path: "management/governance-and-security.md"
    tags: [management, governance, security, naming, rfc1123, labels, secrets, rbac]
    summary: "RFC-1123 naming rules, metadata label taxonomy, zero-plaintext secret policy, and GPU/compute resource hygiene."
  - id: "management-troubleshooting"
    domain: "management"
    type: "runbook"
    title: "Diagnostic & Troubleshooting Runbook"
    path: "management/troubleshooting.md"
    tags: [management, troubleshooting, errors, logs, kaniko, build, oomkilled, pending, schema]
    summary: "Systematic 3-step run triage protocol and error resolution matrix for CLI auth, YAML validation, Kaniko builds, Python tracebacks, and K8s pod crashes."
---

# DigitalHub Platform — Open Knowledge Base (`knowledge/`)

Welcome to the **DigitalHub Open Knowledge Base**. This directory is the versioned reference manual for AI coding assistants (Claude Code, GitHub Copilot, Cursor, Codex, Antigravity) and the **DigitalHub Platform Agent (`digitalhub-agent`)**.

- **Machine-readable index**: [`llms.txt`](llms.txt)
- **Maintainer & schema generation guide**: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Version-pinned navigation

`dhcli init --agent` selects the docs branch from the connected Core's `major.minor` version.
Resolve every relative Markdown link against the full URL of the page containing it.
Resolve catalog `path` values against this file's directory (`knowledge/`) on that same branch.
For example, `../runtimes/sklearnserve.md` in `knowledge/entities/model.md` stays on the selected
branch and resolves to `knowledge/runtimes/sklearnserve.md`. Do not resolve these paths against
the user's workspace or fall back to a different release when a page is unavailable.

---

## 1. Core Domains: Entities & Runtimes First

| Domain | Index | What It Covers |
| :--- | :--- | :--- |
| **1. Entities (Core Domain)** | [`entities/index.md`](entities/index.md) | Schema-generated specifications and `dhcli` recipes for [`project`](entities/project.md), [`function`](entities/function.md), [`workflow`](entities/workflow.md), [`task`](entities/task.md), [`run`](entities/run.md), [`artifact`](entities/artifact.md), [`dataitem`](entities/dataitem.md), [`model`](entities/model.md), [`secret`](entities/secret.md), and [`trigger`](entities/trigger.md). |
| **2. Runtimes (Execution Engines)** | [`runtimes/index.md`](runtimes/index.md) | Schema-generated specifications and `<kind>+<action>` task guides for [`python`](runtimes/python.md), [`container`](runtimes/container.md), [`dbt`](runtimes/dbt.md), [`hera`](runtimes/hera.md), [`kfp`](runtimes/kfp.md), [`sklearnserve`](runtimes/sklearnserve.md), [`mlflowserve`](runtimes/mlflowserve.md), [`huggingfaceserve`](runtimes/huggingfaceserve.md), [`vllmserve`](runtimes/vllmserve.md), [`kubeai`](runtimes/kubeai.md), [`openinference`](runtimes/openinference.md), [`guardrail`](runtimes/guardrail.md), and [`flower`](runtimes/flower.md). |
| **3. CLI Reference (`dhcli`)** | [`cli/index.md`](cli/index.md) | Verified `dhcli` command syntax, flags, [`.dhcore.ini` auth](cli/auth-and-env.md), [YAML CRUD](cli/crud-and-yaml-anatomy.md), [run execution & logs](cli/execution-and-runs.md), and [S3 upload/download & port-forwarding](cli/storage-and-services.md). |
| **4. Python SDK (In-Container & Fallback)** | [`sdk/index.md`](sdk/index.md) | Writing [Python handlers](sdk/handler-authoring.md), [reading/logging data & models](sdk/data-models-and-metrics.md), [Hera/KFP pipeline DSLs](sdk/workflow-pipelines-dsl.md), and the [SDK fallback](sdk/sdk-fallback.md) for running workflows, secrets, and triggers. |
| **5. Architecture, K8s & Troubleshooting** | [`management/index.md`](management/index.md) | [`store://` keys & versioning](management/keys-and-lifecycle.md), [K8s resources & volumes](management/kubernetes-resources.md), [RFC-1123 governance](management/governance-and-security.md), and the [troubleshooting runbook](management/troubleshooting.md). |
