---
id: cli-crud-and-yaml
domain: cli
type: operational_guide
version: "0.16"
tags: [cli, dhcli, create, get, list, update, delete, yaml, json, metadata, spec]
commands:
  - dhcli create
  - dhcli get
  - dhcli list
  - dhcli update
  - dhcli delete
schemas:
  - metadata/metadata.base.json
  - metadata/metadata.versioning.json
  - metadata/metadata.audit.json
summary: "Universal YAML manifest structure (`kind`, `name`, `project`, `metadata`, `spec`) and executing `create`, `get`, `list`, `update`, and `delete` via `dhcli`."
---

# CLI Resource CRUD Operations & YAML Manifest Anatomy

All DigitalHub resources (`projects`, `functions`, `workflows`, `runs`, `dataitems`, `artifacts`, `models`, `secrets`, `triggers`) share a uniform YAML/JSON resource envelope and are managed through five core `dhcli` commands: `create`, `get`, `list`, `update`, and `delete`.

---

## 1. Universal YAML Manifest Anatomy

Every YAML file passed to `dhcli create -f <file.yaml>` or `dhcli update -f <file.yaml>` follows this top-level structure:

```yaml
kind: <entity_kind>          # REQUIRED: e.g. python, container, table, artifact, sklearn, hera
name: <resource_name>        # REQUIRED: RFC-1123 lowercase kebab-case (e.g. clean-customers)
project: <project_name>      # REQUIRED (except for kind: project)
id: <version_uuid>           # OPTIONAL on create (auto-generated if omitted or if -r is passed)
metadata:
  name: <display_name>       # Optional human-readable title
  description: "<text>"      # Optional description
  project: <project_name>
  labels:                    # Optional list of string tags
    - "env:dev"
    - "stage:etl"
spec:
  # Kind-specific specification fields validated against Core JSON Schemas
  # See cli/specs-data-and-storage.md, cli/specs-functions-and-runtimes.md, cli/specs-workflows-and-triggers.md
```

---

## 2. Creating Resources (`dhcli create`)

### 2.1 Creating a Project
Projects can be created directly by name using `-n` without needing a YAML file:
```bash
dhcli create -n my-project projects
```
Or from a `project.yaml` file:
```bash
dhcli create -f project.yaml projects
```

### 2.2 Creating Project-Scoped Entities (`functions`, `dataitems`, `artifacts`, `models`, `workflows`)
For all resources other than `projects`, both `-p <project>` (or `PROJECT_NAME` env var) and `-f <file.yaml>` are **mandatory**:

```bash
# Create a new entity (or a new version of an existing entity with the same name)
dhcli create -p my-project -f function.yaml functions

# Create from an exported YAML file while forcing a new server-generated UUID (-r / --reset-id)
dhcli create -p my-project -f exported-artifact.yaml -r artifacts
```

> **Versioning Behavior on `create`**:
> For versioned entities (`functions`, `workflows`, `dataitems`, `artifacts`, `models`), running `dhcli create` with an existing `name` (and no `id` or with `-r`) registers a **new version** of that entity and makes it the `latest` version.

---

## 3. Listing & Filtering Resources (`dhcli list`)

`dhcli list` returns the latest version of every matching resource in a project (or all versions of a specific resource when `-n <name>` is supplied).

```bash
# List all projects in JSON format
dhcli list projects -o json

# List latest version of all functions in a project
dhcli list -p my-project functions -o json

# List all historical versions of a specific function named 'clean-data'
dhcli list -p my-project -n clean-data functions -o json

# Filter runs by kind (-k) and state (-s)
dhcli list -p my-project -k "python+job:run" -s RUNNING runs -o json
```

---

## 4. Inspecting a Single Resource (`dhcli get`)

Identify the target resource either by `-n <name>` (fetches the **latest** version) or by positional `<id>` (fetches that exact version UUID).

```bash
# Get a project's full details in JSON
dhcli get projects my-project -o json

# Get the latest version of a function by name (-n)
dhcli get -p my-project -n clean-data functions -o json

# Get a specific version of a dataitem or run by its UUID (<id>)
dhcli get -p my-project runs 7a2f5b50fee5454b98977ee4c19741dd -o yaml

# Export an entity definition to a local YAML file
dhcli get -p my-project -n clean-data functions -o yaml > clean-data.yaml
```

---

## 5. Updating & Deleting Resources (`dhcli update`, `dhcli delete`)

### 5.1 Updating Mutable Metadata (`dhcli update`)
Because `spec` fields on versioned entities are immutable once created, `dhcli update` is used to update mutable `metadata` (`description`, `labels`) on an existing version `<id>`:

```bash
# 1. Export existing entity to YAML
dhcli get -p my-project functions <function-id> -o yaml > fn-update.yaml

# 2. Edit metadata.description or metadata.labels in fn-update.yaml, then apply:
dhcli update -p my-project -f fn-update.yaml functions <function-id>
```
*(To change `spec` fields such as source code, requirements, or image, use `dhcli create -p my-project -f fn-update.yaml -r functions` to create a new version instead).*

### 5.2 Deleting Resources (`dhcli delete`)
- Pass `-y` (`--confirm`) to bypass the interactive `y/n` terminal prompt (only after confirming destructive intent with the user).
- Pass `-n <name>` to delete **all versions** of a resource, or positional `<id>` to delete **only one version**.
- Pass `-c` (`--cascade`) when deleting a project to also delete all entities and runs inside it.

```bash
# Delete a single version of an artifact (non-interactive with -y)
dhcli delete -p my-project -y artifacts <artifact-id>

# Delete ALL versions of a function named 'old-fn'
dhcli delete -p my-project -y -n old-fn functions

# Cascade-delete an entire project and all its resources
dhcli delete -c -y projects my-project
```

