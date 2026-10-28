---
title: DBT Runtime
description: Run SQL data transformations over tabular Dataitems in PostgreSQL/Dremio using dbt (dbt+transform).
---

# DBT Runtime (`kind: dbt`)

The **DBT runtime** (`digitalhub-runtime-dbt`) executes SQL transformation queries (`SELECT ...`) against `table` Dataitems stored in the platform's SQL database (`sql://` PostgreSQL) and logs the materialized result as a new versioned `table` Dataitem.

- **Supported task**: `dbt+transform` → `dbt+transform:run`

## 1. Authoring & Registering a DBT Function

Write a SQL transformation query that references input tables via standard dbt `ref('<input_name>')` syntax. Because `dhcli create` sends YAML directly to Core, Base64-encode the `.sql` query into `spec.source.base64` (with `spec.source.lang: sql`):

```sql
-- transform.sql
SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_spent
FROM {{ ref('raw_orders') }}
WHERE status = 'COMPLETED'
GROUP BY customer_id
```

```bash
base64 -i transform.sql | tr -d '\n'
```

```yaml
# function.yaml
kind: dbt
name: customer-spend-summary
project: my-project
metadata:
  description: "Aggregate completed order spend per customer"
spec:
  source:
    lang: sql
    base64: "<single-line-base64-encoded-sql>"
```

```bash
dhcli create functions -p my-project -f function.yaml
```

## 2. Running the Transformation (`dbt+transform`)

Map each `ref('<input_name>')` table in `spec.inputs` to a `store://<project>/dataitem/table/<name>:<uuid>` URI, and specify the output table name in `spec.outputs`:

```yaml
# run.yaml
spec:
  inputs:
    raw_orders: "store://my-project/dataitem/table/raw-orders:<uuid>"
  outputs:
    output_table: "customer-spend-gold"
```

```bash
dhcli run dbt+transform -p my-project -n customer-spend-summary -f run.yaml
dhcli list runs -p my-project -o json
dhcli log <run-id> -p my-project
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Function kind `dbt`

Schema: `schemas/specs/function/dbt.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.source` | object (SourceCode_DbtSourceCodeLanguages_) | **yes** | Source code |
| `spec.source.base64` | string |  | Source code |
| `spec.source.handler` | string |  | Name of the handler function |
| `spec.source.lang` | enum: `sql`, `python` |  | Language used for source code |
| `spec.source.source` | string |  | Reference to source (path or URI) |

#### Task `dbt+transform` → run kind `dbt+transform:run`

Fields accepted under `spec:` of a run manifest (task-level and run-level). `task`, `function` and `local_execution` are set automatically and are omitted.

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.envs` | array<object (CoreEnv)> |  |  |
| `spec.inputs` | map<string, string> |  | Input elements |
| `spec.outputs` | map<string, string> |  | Output elements |
| `spec.parameters` | map<string, serializable> |  |  |
| `spec.profile` | string |  | Select a profile to leverage a pre-configured template |
| `spec.resources` | object (CoreResource) |  |  |
| `spec.resources.cpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.disk` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.gpu` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.resources.mem` | string |  | pattern `^\d+([a-zA-Z]+)?$` |
| `spec.secrets` | array<string> |  |  |
| `spec.volumes` | array<object (CoreVolume)> |  |  |

<!-- END GENERATED: spec-reference -->
