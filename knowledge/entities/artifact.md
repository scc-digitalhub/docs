---
title: Artifact Entity
description: Unstructured files, archives, plots, and bundles stored in S3 object storage and managed via dhcli upload, download, and CRUD commands.
---

# Artifact Entity (`kind: artifact`)

An **Artifact** represents any unstructured file or directory ( archives, configurations, PDF reports, plots, raw binaries) stored in the project's object store (`s3://`) and tracked with versioned lineage in DigitalHub Core.

- **Store URI format**: `store://<project>/artifact/artifact/<name>:<uuid>`

## 1. Uploading & Downloading Files (`dhcli upload` / `download`)

The primary way to create an Artifact from local files is `dhcli upload`. It automatically generates a version UUID, uploads the file or folder to `s3://datalake/<project>/artifact/<name>/<uuid>/...`, and transitions the entity state from `CREATED` to `READY`.

> **CRITICAL RULE**: Always pass the **singular** resource name `artifact` to `dhcli upload` (not `artifacts`), because `dhcli upload` sets the entity `kind` equal to the resource argument.

```bash
# Upload a local file or directory as a new artifact version
dhcli upload artifact -p my-project -n training-config -f ./config.yaml -v

# Inspect the latest version (retrieves UUID and store:// key)
dhcli get artifacts -p my-project -n training-config -o json

# List all versions of an artifact
dhcli list artifacts -p my-project -n training-config -o json

# Download the latest version by name to a local folder
dhcli download artifact -p my-project -n training-config -d ./downloads

# Download a specific version by UUID
dhcli download artifact <uuid> -p my-project -d ./downloads
```

## 2. Registering an Existing S3 Path via YAML

If the file already exists in S3, register its metadata directly with `dhcli create`:

```yaml
kind: artifact
name: training-config
project: my-project
metadata:
  description: "Hyperparameter configuration archive"
  labels:
    - config
spec:
  path: "s3://datalake/my-project/artifact/training-config/v1/config.yaml"
```

```bash
dhcli create artifacts -p my-project -f artifact.yaml
```

## 3. Passing an Artifact into a Function Run

Reference the Artifact's `store://` URI inside `spec.inputs` of your `run.yaml`:

```yaml
spec:
  inputs:
    config_file: "store://my-project/artifact/artifact/training-config:<uuid>"
```

Inside a Python handler (`def my_handler(config_file):`), call `local_path = config_file.download()` to download the file into the container's working directory.

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Kind `artifact`

Schema: `schemas/specs/artifact/artifact.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |
| `spec.src_path` | string |  | URI pointing to the source |

<!-- END GENERATED: spec-reference -->
