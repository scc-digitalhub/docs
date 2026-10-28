---
title: Secret Entity
description: Project-scoped sensitive credentials backed by Kubernetes Secrets and injected as environment variables into Function and Workflow runs.
---

# Secret Entity (`kind: secret`)

A **Secret** stores sensitive configuration values (API keys, database passwords, S3 tokens, HuggingFace tokens) backed by a Kubernetes Secret in the project's namespace.

- **Store URI format**: `store://<project>/secret/secret/<name>:<uuid>`

## 1. Injecting Secrets into Runs (`spec.secrets`)

In any `run.yaml`, list the secret names under `spec.secrets`. DigitalHub mounts each secret into the container as an environment variable with the same name:

```yaml
# run.yaml
spec:
  secrets:
    - HF_TOKEN
    - DB_PASSWORD
```

Inside your Python handler, read them via `os.environ["HF_TOKEN"]`.

> **Security Rule**: Never place plaintext passwords, tokens, or API keys in `spec.envs` or source code. Always reference them via `spec.secrets`.

## 2. Creating Secrets (SDK Fallback or Console)

`dhcli` does not include `secret` in its CRUD resource list (`keys.Resources`). Create project secrets either from the DigitalHub Web Console (**Project → Secrets**) or via a one-line Python SDK command in the workspace venv (`dhcli init` — see [`sdk/sdk-fallback.md`](../sdk/sdk-fallback.md)):

```bash
python3 -c '
import digitalhub as dh
p = dh.get_project("my-project")
p.new_secret(name="HF_TOKEN", secret_value="<your-token>")
'
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Kind `secret`

Schema: `schemas/specs/secret/secret.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.path` | string | **yes** | URI pointing to the content; pattern `secret://([\w-]+)` |
| `spec.provider` | enum: `kubernetes` | **yes** | Secret provider; default `"kubernetes"` |

<!-- END GENERATED: spec-reference -->
