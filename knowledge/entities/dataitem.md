---
title: Dataitem Entity
description: Structured tabular datasets (table), generic datasets (dataitem), and Croissant ML metadata datasets (croissant) backed by S3 or SQL stores.
---

# Dataitem Entity (`kind: dataitem`, `table`, `croissant`)

A **Dataitem** represents a structured or semi-structured dataset (CSV, Parquet, JSON, SQL table, or Croissant ML dataset) tracked in DigitalHub Core.

- **Supported kinds**:
  - `dataitem`: Generic file-backed dataset in S3 (`s3://...`).
  - `table`: Structured tabular dataset in S3 (`.parquet`, `.csv`) or an analytical SQL database (`sql://<db>/<schema>/<table>`) with a typed column `schema`.
  - `croissant`: Dataset described with MLCommons Croissant JSON-LD metadata.
- **Store URI format**: `store://<project>/dataitem/<kind>/<name>:<uuid>`

## 1. Uploading Local Datasets to S3 (`dhcli upload`)

To upload a local CSV or Parquet file as a `kind: dataitem`:

> **CRITICAL RULE**: Always pass the **singular** resource name `dataitem` to `dhcli upload` when creating a new entity so its `kind` is set to `dataitem`.

```bash
# Upload a local Parquet or CSV file as a new dataitem
dhcli upload dataitem -p my-project -n raw-customers -f ./customers.parquet -v

# Retrieve its store:// key and UUID
dhcli get dataitems -p my-project -n raw-customers -o json

# Download the latest version locally
dhcli download dataitem -p my-project -n raw-customers -d ./data
```

### Creating a `kind: table` Dataitem with a Local File
Because `dhcli upload` without an `<id>` sets `kind: dataitem`, to upload a local file into a `kind: table` entity:
1. Create the `kind: table` manifest first (`dhcli create dataitems -p my-project -f table.yaml`) with `spec.path: "s3://datalake/my-project/dataitem/sales-table/customers.parquet"`.
2. Retrieve the created `<uuid>` (`dhcli get dataitems -p my-project -n sales-table -o json`).
3. Upload the file into that specific `<uuid>`:
   ```bash
   dhcli upload dataitem <uuid> -p my-project -f ./customers.parquet
   ```

## 2. Registering External S3 or SQL Tables (`dhcli create`)

When data already lives in S3 or PostgreSQL/Dremio/Trino (`sql://`), register it with `dhcli create dataitems -p my-project -f dataitem.yaml`:

```yaml
kind: table
name: transactions-clean
project: my-project
metadata:
  description: "Cleaned transaction records with schema"
  labels:
    - silver
spec:
  path: "s3://datalake/my-project/dataitem/transactions-clean/part-0.parquet"
  schema:
    fields:
      - name: transaction_id
        type: string
      - name: amount
        type: number
      - name: is_fraud
        type: integer
```

For a database table, set `spec.path: "sql://postgres/public/transactions"`.

## 3. Consuming & Logging Dataitems in Python Handlers

Pass the Dataitem's `store://` URI under `spec.inputs` in `run.yaml`:

```yaml
spec:
  inputs:
    dataset: "store://my-project/dataitem/table/transactions-clean:<uuid>"
```

Inside the Python handler:
```python
def process(project, dataset):
    df = dataset.as_df()  # Loads CSV/Parquet/SQL table as a Pandas DataFrame
    clean_df = df.dropna()
    project.log_dataitem(name="transactions-gold", kind="table", data=clean_df)
```

<!-- BEGIN GENERATED: spec-reference -->
<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->

## Spec reference (from Core JSON Schemas)

### Kind `croissant`

Schema: `schemas/specs/dataitem/croissant.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |

### Kind `dataitem`

Schema: `schemas/specs/dataitem/dataitem.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |

### Kind `table`

Schema: `schemas/specs/dataitem/table.json`

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `spec.path` | string | **yes** | URI pointing to the content; minLength 1 |
| `spec.schema` | object (TableSchema) |  |  |
| `spec.schema.fields` | array<object (Field)> |  |  |

<!-- END GENERATED: spec-reference -->
