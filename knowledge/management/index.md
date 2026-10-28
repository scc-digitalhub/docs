---
id: mgmt-index
domain: management
type: index
version: "0.16"
tags: [management, architecture, core, kubernetes, storage, s3, store-uri, governance, troubleshooting]
summary: Platform architecture and management index covering the 3-layer DigitalHub architecture, entity dependency graph, storage backends, Kubernetes resource management, governance, and troubleshooting.
---

# DigitalHub Platform Architecture & Management

## 1. Three-Layer Platform Architecture

The DigitalHub Platform is built on a cloud-native, three-layer architecture designed for enterprise data engineering, machine learning, and generative AI operations:

```
+-----------------------------------------------------------------------------------+
| 1. CLIENT & AGENT LAYER                                                           |
|    - dhcli (Go Binary + Core Schemas)   - DigitalHub Web Console & Coder IDEs     |
|    - DigitalHub AI Agent / IDE Agents   - Jupyter Notebooks (digitalhub SDK)      |
+-----------------------------------------+-----------------------------------------+
                                          | REST API (HTTPS + OAuth2 Bearer Token)
                                          v
+-----------------------------------------------------------------------------------+
| 2. CONTROL PLANE (DigitalHub Core)                                                |
|    - Metadata Catalog & Versioning (Projects, Dataitems, Models, Artifacts)       |
|    - JSON Schema Validator (Specs & Status)                                       |
|    - Runtime & Task Dispatcher (Translates Runs into K8s CRDs / Jobs / Services)  |
|    - Trigger Engine (Quartz Cron Scheduler & Lifecycle State Listeners)           |
+-----------------------------------------+-----------------------------------------+
                                          | Kubernetes API & S3 / DB Drivers
                                          v
+-----------------------------------------------------------------------------------+
| 3. EXECUTION & STORAGE PLANE (Kubernetes + Data Lake)                             |
|    - Compute: K8s Jobs, Deployments, KServe / Seldon, Argo Workflows, Kaniko      |
|    - Object Storage: MinIO / AWS S3 (s3://) for Artifacts, Parquet & Models       |
|    - Analytical Databases: PostgreSQL / PostGIS / Trino / Iceberg (sql://)        |
|    - Kubernetes Storage: PersistentVolumeClaims (PVC), Shared Volumes, Secrets    |
+-----------------------------------------------------------------------------------+
```

---

## 2. Entity Relationship & Execution Graph

Understanding how DigitalHub entities connect is essential before creating or executing resources:

1. **`Project`** is the top-level multi-tenant workspace and security perimeter.
2. **Data & Storage Entities** (`Artifact`, `Dataitem`, `Model`, `Secret`) store versioned metadata in Core while their physical payloads reside in `s3://`, `sql://`, or Kubernetes Secrets.
3. **Executable Templates** (`Function`, `Workflow`) define **what** code or container to run (`python`, `container`, `hera`, `sklearnserve`, `mlflowserve`, `huggingfaceserve`, `kubeai-text`), along with default images and environment configs.
4. **Execution Descriptors** (`Task`, `Run`, `Trigger`):
   - A **`Task`** (`<kind>+<action>`, e.g., `python+job`, `python+serve`, `hera+pipeline`) binds a `Function` or `Workflow` to a specific execution mode and resource profile.
   - A **`Run`** (`<kind>+<action>:run`, e.g., `python+job:run`) is a single immutable execution instance of a Task with concrete `inputs` (`store://...`), `parameters`, and runtime `status` (`RUNNING`, `COMPLETED`, `ERROR`).
   - A **`Trigger`** (`scheduler`, `lifecycle`) automatically spawns new `Run` instances on a cron schedule or when an entity reaches a target state.

---

## 3. Management Knowledge Map

| Document | Topic & Scope | When to Read |
| :--- | :--- | :--- |
| [keys-and-lifecycle.md](keys-and-lifecycle.md) | **`store://` Keys, Versioning & State Machines**: Exact grammar of `store://` URIs, function/workflow/task URI formats, immutability vs. mutability, and run state transitions. | Before constructing any entity reference or polling run states. |
| [kubernetes-resources.md](kubernetes-resources.md) | **Kubernetes Compute, Volumes, Env & Services**: `CoreResource` (`cpu`, `mem`, `gpu`, `disk`), hardware `profile` selectors, `CoreVolume` mounts (`persistent_volume_claim`, `empty_dir`, `ephemeral`), `envs`, `secrets`, `service_type`, `service_ports`, and `replicas`. | When configuring CPU/GPU/memory limits, mounting volumes, injecting secrets, or exposing ports. |
| [governance-and-security.md](governance-and-security.md) | **Naming Standards, Labels, RBAC & Secret Security**: RFC-1123 naming rules, mandatory metadata labels, project sharing/RBAC, and secret handling rules. | Before creating new projects, functions, services, or secrets in shared environments. |
| [troubleshooting.md](troubleshooting.md) | **Diagnostic & Troubleshooting Runbook**: Root causes and fixes for CLI auth errors, YAML schema rejections, Kaniko build failures, Python handler exceptions, and Kubernetes pod crashes (`OOMKilled`, `ImagePullBackOff`). | Whenever a command or Run fails (`status.state: ERROR`). |

