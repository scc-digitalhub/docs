---
type: knowledge_catalog
name: digitalhub_knowledge_catalog
version: "0.16"
description: "Master Open Knowledge Format (OKF) catalog for the DigitalHub platform, divided into CLI (host execution & YAML specs), SDK (in-container handlers & pipelines), and Management (architecture, K8s resources, governance & troubleshooting)."
domains:
  - id: "cli"
    title: "DigitalHub CLI & YAML Specification Knowledge Base"
    path: "cli/index.md"
    description: "Host-side resource management, authentication, execution, service exposure, storage transfer, and JSON Schema-backed YAML specifications via `dhcli`."
  - id: "sdk"
    title: "DigitalHub Python SDK & Handler Authoring Knowledge Base"
    path: "sdk/index.md"
    description: "In-container Python handler authoring (`def handler(project, run, ...):`), DataItem/Artifact/Model I/O, metric logging, and Hera/KFP pipeline DSL."
  - id: "management"
    title: "DigitalHub Platform Architecture, Governance & Troubleshooting"
    path: "management/index.md"
    description: "Platform architecture, `store://` URI semantics, entity lifecycle and versioning, Kubernetes resource/volume profiles, governance standards, and error troubleshooting."
topics:
  # --- PILLAR 1: CLI (Host Execution & Resource Management) ---
  - id: "cli"
    domain: "cli"
    type: "domain_index"
    title: "DigitalHub CLI (`dhcli`) Command Reference & Overview"
    path: "cli/index.md"
    tags: [cli, dhcli, commands, flags, resources, overview]
    summary: "Master index of `dhcli` commands, global flags, supported resource types, and CLI execution patterns."
  - id: "cli-auth-and-env"
    domain: "cli"
    type: "operational_guide"
    title: "CLI Environment Registration, Authentication & Configuration"
    path: "cli/auth-and-env.md"
    tags: [cli, dhcli, register, login, pat, use, list-env, refresh, config, credentials, init, dhcore.ini]
    summary: "Registering DigitalHub Core endpoints, OAuth2/PAT login, managing multiple environments in `.dhcore.ini`, inspecting credentials, and bootstrapping workspaces with `dhcli init`."
  - id: "cli-crud-and-yaml"
    domain: "cli"
    type: "operational_guide"
    title: "CLI Resource CRUD Operations & YAML Manifest Anatomy"
    path: "cli/crud-and-yaml-anatomy.md"
    tags: [cli, dhcli, create, get, list, update, delete, yaml, json, metadata, spec]
    summary: "Universal YAML manifest structure (`kind`, `name`, `project`, `metadata`, `spec`) and executing `create`, `get`, `list`, `update`, and `delete` via `dhcli`."
  - id: "cli-execution-and-runs"
    domain: "cli"
    type: "operational_guide"
    title: "CLI Task Execution, Run Monitoring, Logs & Metrics"
    path: "cli/execution-and-runs.md"
    tags: [cli, dhcli, run, log, metrics, stop, task, job, build, serve]
    summary: "Triggering function executions with `dhcli run <kind>+<action>`, passing run configuration YAML, streaming container logs (`dhcli log`), reading pod metrics (`dhcli metrics`), and stopping runs."
  - id: "cli-storage-and-services"
    domain: "cli"
    type: "operational_guide"
    title: "CLI File Upload/Download & Service Networking (Port-Forward & Proxy)"
    path: "cli/storage-and-services.md"
    tags: [cli, dhcli, upload, download, s3, services, port-forward, proxy]
    summary: "Uploading and downloading artifacts/models/dataitems to S3 via `dhcli upload`/`download`, listing active services (`dhcli services`), and tunneling traffic via `port-forward` and `proxy`."
  - id: "cli-specs-data-and-storage"
    domain: "cli"
    type: "entity_specification"
    title: "CLI YAML Specifications: Project, Secret, Artifact, DataItem & Model"
    path: "cli/specs-data-and-storage.md"
    tags: [cli, yaml, schema, project, secret, artifact, dataitem, table, croissant, model, sklearn, mlflow, huggingface]
    summary: "Core JSON Schema-aligned YAML specifications and `dhcli` recipes for Projects, Secrets, Artifacts, DataItems (`table`, `dataitem`, `croissant`), and Models (`model`, `sklearn`, `mlflow`, `huggingface`)."
  - id: "cli-specs-functions-and-runtimes"
    domain: "cli"
    type: "runtime_specification"
    title: "CLI YAML Specifications: Functions & Runtimes (Python, Container, ModelServe, DBT, Flower)"
    path: "cli/specs-functions-and-runtimes.md"
    tags: [cli, yaml, schema, function, python, container, modelserve, vllmserve, kubeai, sklearnserve, mlflowserve, huggingfaceserve, dbt, guardrail, openinference, flower]
    summary: "Core JSON Schema-aligned YAML specifications for creating and running Functions across all supported platform runtimes."
  - id: "cli-specs-workflows-and-triggers"
    domain: "cli"
    type: "entity_specification"
    title: "CLI YAML Specifications: Workflows (Hera, KFP) & Triggers (Scheduler, Lifecycle)"
    path: "cli/specs-workflows-and-triggers.md"
    tags: [cli, yaml, schema, workflow, hera, kfp, trigger, scheduler, lifecycle, cron]
    summary: "Core JSON Schema-aligned YAML specifications for DAG Workflows (`hera`, `kfp`) and automated Triggers (`scheduler`, `lifecycle`)."

  # --- PILLAR 2: SDK (In-Container Handlers, Pipelines & Interactive Notebooks) ---
  - id: "sdk"
    domain: "sdk"
    type: "domain_index"
    title: "DigitalHub Python SDK Overview & Usage Contexts"
    path: "sdk/index.md"
    tags: [sdk, python, overview, handler, notebook, pipeline]
    summary: "When and how to use the `digitalhub` Python SDK: writing in-container function handlers, authoring Hera/KFP workflow DAGs, and running interactive notebook experiments."
  - id: "sdk-handler-authoring"
    domain: "sdk"
    type: "runtime_specification"
    title: "Authoring Python Handlers (`def handler`, Inputs, Parameters & Outputs)"
    path: "sdk/handler-authoring.md"
    tags: [sdk, python, handler, project, run, context, event, inputs, parameters, outputs, init]
    summary: "How to write Python handler functions executed by the platform: injected reserved arguments (`project`, `run`, `context`, `event`), mapping `inputs` vs `parameters`, optional `@handler` output decorators, and `init` functions."
  - id: "sdk-data-models-and-metrics"
    domain: "sdk"
    type: "operational_guide"
    title: "In-Handler SDK Operations: Reading DataItems & Logging Artifacts, Models, and Metrics"
    path: "sdk/data-models-and-metrics.md"
    tags: [sdk, dataitem, as_df, as_file, log_artifact, log_dataitem, log_model, log_sklearn, log_mlflow, log_metric]
    summary: "Using injected `project`, `run`, and `Dataitem` objects inside handler code to read tabular/file data, log produced artifacts and trained ML models, and track experiment metrics."
  - id: "sdk-workflow-pipelines-dsl"
    domain: "sdk"
    type: "runtime_specification"
    title: "Authoring Workflow Pipelines in Python (Hera & KFP DSL)"
    path: "sdk/workflow-pipelines-dsl.md"
    tags: [sdk, workflow, pipeline, dag, hera, kfp, dsl, step]
    summary: "Writing Python pipeline functions with `digitalhub_runtime_hera.dsl` (`Workflow`, `step`, DAG dependencies `A >> B`) and Kubeflow Pipelines (`kfp`)."
  - id: "sdk-interactive-reference"
    domain: "sdk"
    type: "entity_specification"
    title: "Interactive Python SDK Reference (Notebooks & Local Scripts)"
    path: "sdk/interactive-sdk-reference.md"
    tags: [sdk, jupyter, notebook, crud, get_or_create_project, new_function, local_execution]
    summary: "Quick reference for top-level `import digitalhub as dh` CRUD and execution methods when developing inside Jupyter notebooks."

  # --- PILLAR 3: MANAGEMENT (Architecture, K8s Resources, Governance & Troubleshooting) ---
  - id: "management"
    domain: "management"
    type: "domain_index"
    title: "DigitalHub Platform Architecture & Entity Model"
    path: "management/index.md"
    tags: [management, architecture, entities, console, urls, storage, compute]
    summary: "Platform architecture (Core, Kubernetes, MinIO S3, PostgreSQL, Dremio, Coder), entity relationship graph, and Console UI route conventions."
  - id: "management-keys-and-lifecycle"
    domain: "management"
    type: "operational_guide"
    title: "Entity Keys (`store://`), Source URIs, Versioning & State Machines"
    path: "management/keys-and-lifecycle.md"
    tags: [management, store, key, uri, s3, git, versioning, immutability, state, lifecycle]
    summary: "Structure of `store://` entity keys, supported `code_src` URI schemes (`git+https://`, `zip+s3://`), spec immutability rules, and Run lifecycle states."
  - id: "management-kubernetes-resources"
    domain: "management"
    type: "operational_guide"
    title: "Kubernetes Compute Resources, Hardware Profiles, Volumes & Networking"
    path: "management/kubernetes-resources.md"
    tags: [management, kubernetes, resources, cpu, mem, gpu, profile, volumes, pvc, empty_dir, shared_volume, envs, secrets, service_type, replicas]
    summary: "Configuring `CoreResource` (`cpu`, `mem`, `gpu`, `disk`), hardware `profile` templates, `CoreVolume` mounts, `envs`, `secrets`, and Kubernetes service exposure."
  - id: "management-governance-and-security"
    domain: "management"
    type: "governance_standard"
    title: "Platform Governance, Naming Conventions, Labeling & Security Standards"
    path: "management/governance-and-security.md"
    tags: [management, governance, naming, labels, security, rbac, share, secrets]
    summary: "Mandatory RFC-1123 naming conventions, metadata labeling standards, project sharing/RBAC, secret handling, and container image security policies."
  - id: "management-troubleshooting"
    domain: "management"
    type: "troubleshooting_guide"
    title: "Platform, CLI & Run Troubleshooting Guide"
    path: "management/troubleshooting.md"
    tags: [management, troubleshooting, errors, debugging, logs, build, kaniko, oom, auth]
    summary: "Diagnostic runbooks and self-correction protocols for CLI authentication/API-level errors, failed Kaniko builds, Python handler tracebacks, `entity_key` mismatches, and Kubernetes pod failures."
---

# DigitalHub Knowledge Catalog (OKF v0.16)

Welcome to the authoritative **DigitalHub Open Knowledge Format (OKF)** Knowledge Base. This catalog is structured into three specialized pillars so AI agents and developers can retrieve exact specifications with minimal context overhead:

1. **[`cli/` — CLI & YAML Specification Knowledge Base](cli/index.md)**:
   **Primary execution layer for agents.** Covers `dhcli` commands, authentication, resource CRUD, task execution (`dhcli run`), log/metric inspection, file transfer, and Core JSON Schema-aligned YAML manifests.
2. **[`sdk/` — Python SDK & Handler Authoring Knowledge Base](sdk/index.md)**:
   **Code authoring layer.** Covers how to write the Python source code (`handler.py`, `pipeline.py`, or notebooks) that runs *inside* DigitalHub functions and workflows (`project.log_artifact`, `di.as_df()`, `run.log_metric()`, Hera DSL).
3. **[`management/` — Platform Architecture, Governance & Troubleshooting](management/index.md)**:
   **Platform foundation & operations layer.** Covers the entity model, `store://` URI keys, Kubernetes compute/volume configurations, governance standards, Console URLs, and error recovery runbooks.

---

## Topic Directory by Domain

### 1. CLI & YAML Specifications (`cli/`)

| Topic ID | Path | Summary |
| :--- | :--- | :--- |
| **`cli`** | [`cli/index.md`](cli/index.md) | Master index of `dhcli` commands, global flags, resource aliases, and CLI execution rules. |
| **`cli-auth-and-env`** | [`cli/auth-and-env.md`](cli/auth-and-env.md) | Environment registration (`register`), OAuth2/PAT login (`login`), `.dhcore.ini`, and workspace setup (`init`). |
| **`cli-crud-and-yaml`** | [`cli/crud-and-yaml-anatomy.md`](cli/crud-and-yaml-anatomy.md) | Universal YAML manifest anatomy and `create`, `get`, `list`, `update`, `delete` commands. |
| **`cli-execution-and-runs`** | [`cli/execution-and-runs.md`](cli/execution-and-runs.md) | Executing tasks (`dhcli run <kind>+<action>`), run spec YAML, `log`, `metrics`, and `stop`. |
| **`cli-storage-and-services`** | [`cli/storage-and-services.md`](cli/storage-and-services.md) | S3 file transfer (`upload`, `download`) and service access (`services`, `port-forward`, `proxy`). |
| **`cli-specs-data-and-storage`** | [`cli/specs-data-and-storage.md`](cli/specs-data-and-storage.md) | YAML `spec` schemas for `project`, `secret`, `artifact`, `dataitem`, and `model`. |
| **`cli-specs-functions-and-runtimes`** | [`cli/specs-functions-and-runtimes.md`](cli/specs-functions-and-runtimes.md) | YAML `spec` schemas for `function` and `run` across `python`, `container`, `modelserve`, `dbt`, `flower`, `guardrail`, `openinference`. |
| **`cli-specs-workflows-and-triggers`** | [`cli/specs-workflows-and-triggers.md`](cli/specs-workflows-and-triggers.md) | YAML `spec` schemas for `workflow` (`hera`, `kfp`) and `trigger` (`scheduler`, `lifecycle`). |

### 2. Python SDK & Handler Authoring (`sdk/`)

| Topic ID | Path | Summary |
| :--- | :--- | :--- |
| **`sdk`** | [`sdk/index.md`](sdk/index.md) | Overview of when to use the Python SDK vs `dhcli`. |
| **`sdk-handler-authoring`** | [`sdk/handler-authoring.md`](sdk/handler-authoring.md) | Writing Python handlers (`def func(project, run, ...)`), `inputs` vs `parameters`, `@handler`, and `init`. |
| **`sdk-data-models-and-metrics`** | [`sdk/data-models-and-metrics.md`](sdk/data-models-and-metrics.md) | Reading `Dataitem` (`as_df`, `as_file`) and logging artifacts, models, and metrics inside handlers. |
| **`sdk-workflow-pipelines-dsl`** | [`sdk/workflow-pipelines-dsl.md`](sdk/workflow-pipelines-dsl.md) | Authoring DAG pipelines using `digitalhub_runtime_hera.dsl` and KFP. |
| **`sdk-interactive-reference`** | [`sdk/interactive-reference.md`](sdk/interactive-sdk-reference.md) | Top-level `import digitalhub as dh` CRUD cheatsheet for Jupyter notebooks. |

### 3. Platform Architecture, Governance & Troubleshooting (`management/`)

| Topic ID | Path | Summary |
| :--- | :--- | :--- |
| **`management`** | [`management/index.md`](management/index.md) | Platform architecture, entity graph, and Console URL routing formats. |
| **`management-keys-and-lifecycle`** | [`management/keys-and-lifecycle.md`](management/keys-and-lifecycle.md) | `store://` URI anatomy, `code_src` schemes, versioning, immutability, and Run states. |
| **`management-kubernetes-resources`** | [`management/kubernetes-resources.md`](management/kubernetes-resources.md) | CPU/Memory/GPU `resources`, hardware `profile` templates, `volumes`, `envs`, `secrets`, and service networking. |
| **`management-governance-and-security`** | [`management/governance-and-security.md`](management/governance-and-security.md) | Naming conventions, mandatory labels, project RBAC sharing, and security rules. |
| **`management-troubleshooting`** | [`management/troubleshooting.md`](management/troubleshooting.md) | Diagnostic protocols for CLI errors, Kaniko build failures, runtime exceptions, and pod errors. |
