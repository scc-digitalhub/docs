---
title: Project Entity
description: Top-level multi-tenant workspace and namespace for all DigitalHub entities, default storage configuration, and project CRUD via dhcli.
---

# Project Entity (`kind: project`)

A **Project** is the top-level organizational boundary, Kubernetes namespace mapping, and security perimeter in DigitalHub. Every Function, Workflow, Dataitem, Artifact, Model, Run, Secret, and Trigger belongs to a single Project.

## 1. CLI Operations (`dhcli`)

```bash
# List all projects on the active DigitalHub environment
dhcli list projects
dhcli list projects -o json

# Create a new project by name alone (fastest)
dhcli create projects -n my-project

# Or create a project from a YAML manifest
dhcli create projects -f project.yaml

# Inspect a project's metadata and configuration
dhcli get projects my-project -o yaml

# Update project description or labels
dhcli update projects my-project -f project.yaml

# Delete a project and cascade-delete all resources inside it (-y skips prompt)
dhcli delete projects my-project -c -y
```

> **Tip**: Export `PROJECT_NAME=my-project` in your shell to avoid passing `-p my-project` on every subsequent `dhcli` command.

## 2. Canonical YAML Manifest

```yaml
kind: project
name: fraud-detection
metadata:
  name: fraud-detection
  description: "End-to-end fraud detection ML pipeline"
  labels:
    - production
    - finance
spec:
  config:
    default_files_store: "s3://datalake/fraud-detection"
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Kind `project`

Schema: `schemas/specs/project/project.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.artifacts` | array<object (Artifact)> |  |  |
| `spec.config` | object (ProjectConfig) |  |  |
| `spec.config.default_files_store` | string |  |  |
| `spec.dataitems` | array<object (DataItem)> |  |  |
| `spec.functions` | array<object (Function)> |  |  |
| `spec.models` | array<object (Model)> |  |  |
| `spec.source` | string |  |  |
| `spec.workflows` | array<object (Workflow)> |  |  |

<!-- END GENERATED: spec-reference -->
