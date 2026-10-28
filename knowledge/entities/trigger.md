---
title: Trigger Entity
description: Automated execution triggers (scheduler cron triggers and lifecycle event triggers) that launch Function or Workflow runs.
---

# Trigger Entity (`kind: scheduler`, `lifecycle`)

A **Trigger** automatically launches new `Run` instances of a Function or Workflow either on a recurring cron schedule (`kind: scheduler`) or in response to an entity state change such as a new Dataitem arriving in S3 (`kind: lifecycle`).

- **Supported kinds**:
  - `scheduler`: Fires on a Quartz cron expression (`spec.schedule`, e.g., `"0 0 2 * * ?"` for 02:00 AM daily).
  - `lifecycle`: Fires when a watched entity matching `spec.key` transitions into one of `spec.states` (e.g., `READY`).

## Creating & Managing Triggers (SDK Fallback or Console)

`dhcli` does not include `trigger` in its CRUD resource list (`keys.Resources`). Manage triggers either through the DigitalHub Web Console (**Project → Triggers**) or via the Python SDK inside the workspace venv (`dhcli init` — see [`sdk/sdk-fallback.md`](../sdk/sdk-fallback.md)):

```bash
python3 -c '
import digitalhub as dh
p = dh.get_project("my-project")
fn = p.get_function("daily-etl-fn")
fn.trigger(
    action="job",
    name="nightly-etl-schedule",
    kind="scheduler",
    schedule="0 0 2 * * ?",
    parameters={"batch_window": "24h"},
)
'
```

Once a Trigger fires, the resulting `Run` instances appear normally in `dhcli list runs -p my-project` and can be inspected with `dhcli get runs` and `dhcli log`.

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Kind `lifecycle`

Schema: `schemas/specs/trigger/lifecycle.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.function` | string |  | Static reference to function |
| `spec.key` | string | **yes** | minLength 1; pattern `store://([^/]+)/(.+)` |
| `spec.states` | array<enum: `CREATED`, `DELETED`, `ERROR`, `READY`, `UPLOADING`> |  |  |
| `spec.task` | string | **yes** | minLength 1 |
| `spec.template` | map<string, serializable> | **yes** |  |
| `spec.workflow` | string |  | Static reference to workflow |

### Kind `scheduler`

Schema: `schemas/specs/trigger/scheduler.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.function` | string |  | Static reference to function |
| `spec.schedule` | string | **yes** | Schedule definition as crontab; minLength 1; pattern `((((\d+,)+\d+|(\d+(\/|-|#)\d+)|\d+L?|\*(\/\d+)?|L(-\d+)?|\?|[A-Z]{3}(-[A-Z]{3})?) ?){5,7})|(@(yearly|monthly|weekly|daily|hourly))` |
| `spec.task` | string | **yes** | minLength 1 |
| `spec.template` | map<string, serializable> | **yes** |  |
| `spec.workflow` | string |  | Static reference to workflow |

<!-- END GENERATED: spec-reference -->
