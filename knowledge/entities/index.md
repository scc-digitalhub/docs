---
title: Entities Overview
description: Core reference index for all DigitalHub Platform entities, their URI schemes, versioning semantics, and dhcli CRUD support.
---

# DigitalHub Platform Entities

Every resource in DigitalHub is represented as a typed **Entity** inside a **Project** workspace. Entities hold structured configuration in `spec`, user labels and descriptions in `metadata`, and runtime state in `status`.

## 1. Entity Kinds & CLI Support Matrix

| Entity | Plural (`dhcli`) | Versioned? | `dhcli` CRUD Support | URI / Key Format |
| :--- | :--- | :---: | :---: | :--- |
| [**Project**](project.md) | `projects` (`project`) | No | `create`, `get`, `list`, `update`, `delete` | `store://<project>` (or `<project>`) |
| [**Function**](function.md) | `functions` (`function`, `fn`) | **Yes** | `create`, `get`, `list`, `update`, `delete`, `run` | `<kind>://<project>/<name>:<uuid>` |
| [**Workflow**](workflow.md) | `workflows` (`workflow`) | **Yes** | `create`, `get`, `list`, `update`, `delete` | `<kind>://<project>/<name>:<uuid>` |
| [**Artifact**](artifact.md) | `artifacts` (`artifact`) | **Yes** | `create`, `get`, `list`, `update`, `delete`, `upload`, `download` | `store://<project>/artifact/<kind>/<name>:<uuid>` |
| [**Dataitem**](dataitem.md) | `dataitems` (`dataitem`) | **Yes** | `create`, `get`, `list`, `update`, `delete`, `upload`, `download` | `store://<project>/dataitem/<kind>/<name>:<uuid>` |
| [**Model**](model.md) | `models` (`model`) | **Yes** | `create`, `get`, `list`, `update`, `delete`, `upload`, `download` | `store://<project>/model/<kind>/<name>:<uuid>` |
| [**Run**](run.md) | `runs` (`run`) | No (UUID) | `get`, `list`, `delete`, `log`, `stop`, `metrics` *(created via `dhcli run`)* | `store://<project>/run/<kind>/<uuid>` |
| [**Task**](task.md) | *(auto-managed)* | No (UUID) | Auto-created by `dhcli run` | `<task-kind>://<project>/<task-uuid>` |
| [**Secret**](secret.md) | *(SDK / Console)* | No (UUID) | Referenced in runs via `spec.secrets`; managed via Python SDK or Console | `store://<project>/secret/secret/<name>:<uuid>` |
| [**Trigger**](trigger.md) | *(SDK / Console)* | No (UUID) | Managed via Python SDK or Console | `store://<project>/trigger/<kind>/<name>:<uuid>` |

## 2. Universal YAML Manifest Structure

All entities created with `dhcli create <resource> -p <project> -f <file.yaml>` follow the same top-level envelope:

```yaml
kind: <entity-kind>
name: <rfc1123-entity-name>
project: <project-name>
metadata:
  name: <display-or-logical-name>
  description: "<human-readable description>"
  labels:
    - "<label-1>"
spec:
  # Kind-specific fields validated against Core JSON Schemas
```

- **RFC-1123 Naming**: `name` and `project` must match `^[a-z0-9-]+$` (lowercase alphanumeric and hyphens, max 63 characters).
- **Version Immutability**: For versioned entities (`function`, `workflow`, `artifact`, `dataitem`, `model`), `spec` is **immutable** once created. To modify `spec` (e.g., updating function handler code or dataset path), run `dhcli create <resource> -p <project> -f <file.yaml>` with the **same `name`**—Core automatically mints a new version UUID under that lineage. `dhcli update` only modifies mutable `metadata` or `status` on an existing `<id>`.

<!-- BEGIN GENERATED: entity-kinds -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

| Entity | Kinds |
| :--- | :--- |
| [project](project.md) | `project` |
| [artifact](artifact.md) | `artifact` |
| [dataitem](dataitem.md) | `croissant`, `dataitem`, `table` |
| [model](model.md) | `huggingface`, `mlflow`, `model`, `sklearn` |
| [function](function.md) | `container`, `dbt`, `flower-app`, `flower-client`, `flower-server`, `guardrail`, `huggingfaceserve`, `kubeai-speech`, `kubeai-text`, `mlflowserve`, `openinference`, `python`, `sklearnserve`, `vllmserve-pooling`, `vllmserve-speech`, `vllmserve-text` |
| [workflow](workflow.md) | `hera`, `kfp` |
| [secret](secret.md) | `secret` |
| [trigger](trigger.md) | `lifecycle`, `scheduler` |
| [run](run.md) | `<task>:run` — see [runtimes](../runtimes/index.md) |
| [task](task.md) | `<function-kind>+<action>` — see [runtimes](../runtimes/index.md) |

<!-- END GENERATED: entity-kinds -->
