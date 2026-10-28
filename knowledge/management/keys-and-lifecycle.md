---
id: management-keys-and-lifecycle
domain: management
type: operational_guide
version: "0.16"
tags:
  [
    management,
    store,
    key,
    uri,
    s3,
    git,
    versioning,
    immutability,
    state,
    lifecycle,
    console,
  ]
summary: "Platform reference for `store://` entity keys, source code URI schemes (`git+https://`, `zip+s3://`), entity versioning and spec immutability rules, Run state transitions, and Console UI URL routing."
---

# Entity Keys (`store://`), Source URIs, Versioning & State Machines

Every resource managed by DigitalHub Core follows strict addressing, versioning, and lifecycle rules. Understanding these rules prevents broken references across `dhcli` manifests and handler inputs.

---

## 1. Entity Keys (`store://` URI Format)

Every entity persisted in DigitalHub Core is uniquely identified across the platform by its **`key`**, which uses the `store://` URI scheme:

```text
store://<project>/<entity_type>/<kind>/<name>:<id>
```

| Segment | Description | Examples |
| :--- | :--- | :--- |
| `<project>` | Project name that owns the entity. | `my-project`, `fraud-detection` |
| `<entity_type>` | Singular entity category. | `dataitem`, `artifact`, `model`, `function`, `workflow`, `run`, `task`, `trigger`, `secret` |
| `<kind>` | Specific entity or runtime kind. | `table`, `artifact`, `sklearn`, `python`, `python+job:run` |
| `<name>` | Logical name of the entity (for `run` and `task`, this is equal to `<id>`). | `customer-churn`, `clean-data` |
| `<id>` | Version UUID (or `:latest` when referencing the newest version in inputs). | `eab4f45fb93f49288780024ce17a344c`, `latest` |

### Examples of Valid Entity Keys
- **Tabular DataItem**: `store://analytics/dataitem/table/customers:9d249ef7762349e2a532e883ac4c378e`
- **Function Reference**: `python://analytics/clean-data:eab4f45fb93f49288780024ce17a344c` *(Note: inside `Run.spec.function`, the shorthand `<kind>://<project>/<name>:<id>` is also used by Core)*
- **Task Reference**: `python+job://analytics/9d249ef7762349e2a532e883ac4c378e`

> **How to Obtain an Entity's Exact Key via `dhcli`**:
> ```bash
> dhcli get -p <project> -n <name> <resource> -o json
> ```
> Read the top-level `"key"` and `"id"` fields from the returned JSON.

---

## 2. Versioning vs. Unversioned Entities & Immutability

DigitalHub entities are divided into **Versioned** and **Unversioned** resources:

| Category | Entities | Addressing & Mutation Rules |
| :--- | :--- | :--- |
| **Versioned Entities** | `function`, `workflow`, `dataitem`, `artifact`, `model` | • Addressed by **`name`** (logical lineage) + **`id`** (version UUID).<br>• **`spec` is IMMUTABLE** on existing versions. To change `spec` (e.g., updating function code, requirements, or dataset path), run **`dhcli create -p <proj> -f <updated.yaml> <resource>`** with the same `name`—Core automatically creates a new version UUID under that `name`.<br>• `dhcli update` only modifies mutable `metadata` (`description`, `labels`) or `status` on a specific version `id`. |
| **Unversioned Entities**| `project`, `run`, `task`, `trigger`, `secret`, `log` | • Single instance addressed by `name` (for `project`) or `id` (UUID for `run`, `task`, `trigger`, `secret`).<br>• Calling `dhcli delete -p <proj> -n <name> <resource>` on a versioned entity deletes **all versions** of `<name>`; passing `<id>` deletes only that specific version. |

---

## 3. Code Source URIs (`spec.source.source`)

When defining a `function` or `workflow` YAML manifest for `dhcli create`, you must provide executable source code inside `spec.source` using either inline `base64` or a remote `source` URI:

| Source Type | `spec.source.source` Value | `spec.source.base64` | Required `spec.source.handler` Syntax |
| :--- | :--- | :--- | :--- |
| **Inline Code (Recommended for single `.py` files)** | *(omit)* | `<base64-encoded string of file>` | `<function_name>` (e.g. `main`, `train`) |
| **Git Repository** | `git+https://github.com/org/repo#branch` | *(omit)* | `path.to.module:function_name` (e.g. `src.train:main`) |
| **S3 ZIP Archive** | `zip+s3://bucket/path/archive.zip` | *(omit)* | `module_name:function_name` (e.g. `app.worker:run`) |
| **HTTP(S) Single File** | `https://host/path/script.py` | *(omit)* | `<function_name>` (e.g. `main`) |
| **HTTP(S) ZIP Archive** | `zip+https://host/path/bundle.zip` | *(omit)* | `pkg.module:function_name` |

> **CRITICAL CLI vs. SDK Difference**:
> When using the Python SDK (`dh.new_function(code_src="local_file.py")`), the Python SDK reads `local_file.py` from disk and converts it into `spec.source.base64` before sending the HTTP request.
> When using **`dhcli create -f function.yaml functions`**, `dhcli` sends the YAML directly to Core without reading local `.py` files referenced in `spec.source.source`. Therefore, for local `.py` files via `dhcli`, **always Base64-encode the file into `spec.source.base64`**, or upload a directory/zip via `dhcli upload` and reference its `s3://` URI!

---

## 4. Run Lifecycle State Machine (`status.state`)

Every `Run` entity (`job`, `build`, `serve`, `pipeline`) transitions through the following backend states in `status.state`:

```text
[ CREATED ] --> [ READY ] --> [ RUNNING ] --+--> [ COMPLETED ]  (Batch Job / Build / Pipeline finished with exit code 0)
                                            |
                                            +--> [ ERROR ]      (Container exited non-zero, build failed, or K8s error)
                                            |
                                            +--> [ STOPPED ]    (Terminated by user via `dhcli stop`)
```

- **For Batch Jobs & Builds (`+job`, `+build`, `+pipeline`, `+transform`)**:
  The target terminal state is **`COMPLETED`**. Once `COMPLETED` (or `ERROR`), inspect logs with `dhcli log -p <proj> <run_id>`.
- **For Long-Lived Services (`+serve`, `+deploy`)**:
  A healthy deployed service stays in the **`RUNNING`** state indefinitely until stopped via `dhcli stop -p <proj> <run_id>` and exposes its endpoint under `status.service` (inspected via `dhcli services -p <proj>`).

---

## 5. DigitalHub Console UI Route Conventions

Whenever presenting created or inspected resources to a user in Markdown, format clickable links using the standard DigitalHub Console routes:

| Resource Type | Console Route Pattern | Markdown Link Example |
| :--- | :--- | :--- |
| **Project** | `/-/{project_name}` | `[Project: demo](/-/demo)` |
| **Run** | `/-/{project_name}/runs/{run_id}/show` | `[Run #7a2f5b](/-/demo/runs/7a2f5b.../show)` |
| **Function** | `/-/{project_name}/functions/{function_id}/show` | `[Function: clean](/-/demo/functions/eab4f.../show)` |
| **DataItem** | `/-/{project_name}/dataitems/{dataitem_id}/show` | `[DataItem: iris](/-/demo/dataitems/9d249.../show)` |
| **Artifact** | `/-/{project_name}/artifacts/{artifact_id}/show` | `[Artifact: report](/-/demo/artifacts/1b3c4.../show)` |
| **Model** | `/-/{project_name}/models/{model_id}/show` | `[Model: clf](/-/demo/models/4f8a2.../show)` |
| **Workflow** | `/-/{project_name}/workflows/{workflow_id}/show` | `[Workflow: etl](/-/demo/workflows/6c9d1.../show)` |
| **Secret** | `/-/{project_name}/secrets/{secret_id}/show` | `[Secret: db-pass](/-/demo/secrets/2a1e9.../show)` |
| **Trigger** | `/-/{project_name}/triggers/{trigger_id}/show` | `[Trigger: nightly](/-/demo/triggers/8f3b5.../show)` |
