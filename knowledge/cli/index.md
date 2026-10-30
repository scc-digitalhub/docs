---
id: cli
domain: cli
type: domain_index
version: "0.16"
tags: [cli, dhcli, commands, flags, resources, overview, schema]
commands:
  - dhcli register
  - dhcli login
  - dhcli refresh
  - dhcli use
  - dhcli list-env
  - dhcli remove
  - dhcli config
  - dhcli credentials
  - dhcli init
  - dhcli create
  - dhcli get
  - dhcli list
  - dhcli update
  - dhcli delete
  - dhcli run
  - dhcli log
  - dhcli metrics
  - dhcli stop
  - dhcli upload
  - dhcli download
  - dhcli services
  - dhcli port-forward
  - dhcli proxy
summary: "Master reference and operational guide for the DigitalHub CLI (`dhcli`): global flags, supported resource types, command cheatsheet, and non-interactive automation rules."
---

# DigitalHub CLI (`dhcli`) Command Reference & Overview

The **DigitalHub Command-Line Interface (`dhcli`)** is the primary operational tool for managing platform environments, performing CRUD operations on entities, triggering and monitoring executions (`runs`), transferring files to/from S3 storage, and exposing cluster services locally.

---

## 1. Global Flags & Environment Variables

Every `dhcli` command accepts the following global flags and respects standard environment variables:

| Flag / Env Variable | Type | Description |
| :--- | :--- | :--- |
| `-e, --env <name>` | Flag (`string`) | Target environment section in `.dhcore.ini`. If omitted, uses `current_environment`. |
| `-p, --project <name>` | Flag (`string`) | Target project name. Falls back to the `PROJECT_NAME` environment variable if omitted. |
| `-o, --output <format>` | Flag (`string`) | Output format for inspection commands: `short` (default human summary), `json`, or `yaml`. |
| `-v, --verbose` | Flag (`bool`) | Enable verbose operational logging. |
| `--debug` | Flag (`bool`) | Enable full HTTP request/response debug logging (implies `--verbose`). |
| `--version` | Flag (`bool`) | Print `dhcli` version and exit. |
| `DH_CONFIG` | Env Var | Override path to `.dhcore.ini` (defaults to `./.dhcore.ini` if present in CWD, else `~/.dhcore.ini`). |
| `PROJECT_NAME` | Env Var | Default project used whenever `-p` is omitted on project-scoped commands. |
| `DHCORE_PERSONAL_ACCESS_TOKEN` | Env Var | Personal Access Token used by `dhcli login` for non-interactive authentication (alias: `DHCORE_PAT`). |

---

## 2. Supported Resource Identifiers

Commands that operate on platform entities (`create`, `get`, `list`, `update`, `delete`, `upload`, `download`, `metrics`) take a `<resource>` positional argument. Both plural and singular forms are accepted:

| Canonical Plural | Accepted Aliases | Project Scoped (`-p` required)? | Versioned? | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`projects`** | `project` | No (top-level) | No | Workspace container for all project entities, runs, and shares. |
| **`functions`** | `function`, `fn` | Yes | Yes (UUID) | Executable definitions (`python`, `container`, `modelserve`, `dbt`, `flower`, ...). |
| **`workflows`** | `workflow` | Yes | Yes (UUID) | Multi-step pipeline DAG definitions (`hera`, `kfp`). |
| **`runs`** | `run` | Yes | No (UUID) | Concrete executions produced by running a function or workflow task. |
| **`dataitems`** | `dataitem` | Yes | Yes (UUID) | Structured/tabular (`table`), `croissant`, or unstructured dataset entities. |
| **`artifacts`** | `artifact` | Yes | Yes (UUID) | General files, source archives, or binary objects stored in the datalake. |
| **`models`** | `model` | Yes | Yes (UUID) | Trained ML/AI model entities (`model`, `sklearn`, `mlflow`, `huggingface`, ...). |
| **`logs`** | `log` | Yes | No (UUID) | Persisted container log records associated with runs. |

> **Entities managed via SDK fallback (`secret`, `trigger`, and running `workflow` pipelines)**:
> `dhcli` `keys.Resources` supports the 8 resource types above (`projects`, `functions`, `workflows`, `runs`, `dataitems`, `artifacts`, `models`, `logs`). To create a `Secret`, attach a `Trigger`, or run a `Workflow` (`hera`/`kfp` `build` + `pipeline`), use a one-liner Python SDK call inside the workspace venv created by `dhcli init` (see [`../sdk/interactive-sdk-reference.md`](../sdk/interactive-sdk-reference.md)).

---

## 3. Complete Command Cheatsheet

### 3.1 Environment & Authentication Commands
*(Detailed in [`cli/auth-and-env.md`](auth-and-env.md))*

| Command | Syntax | Purpose |
| :--- | :--- | :--- |
| **`register`** | `dhcli register [-e <env>] [-f] <endpoint_url>` | Fetch `.well-known/configuration` from Core and register environment in `.dhcore.ini`. |
| **`login`** | `dhcli login [-e <env>] [--pat <token>]` | Authenticate via OAuth2 PKCE (browser) or non-interactively via `--pat` / `DHCORE_PERSONAL_ACCESS_TOKEN`. |
| **`refresh`** | `dhcli refresh [-e <env>]` | Refresh expired OAuth2 `access_token` using the stored `refresh_token`. |
| **`use`** | `dhcli use <env>` | Set the active default environment in `.dhcore.ini`. |
| **`list-env`** | `dhcli list-env` | List all registered environments in `.dhcore.ini`. |
| **`remove`** | `dhcli remove <env>` | Remove an environment section from `.dhcore.ini`. |
| **`config`** | `dhcli config [-e <env>] [-o short\|json\|yaml]` | Print non-secret environment configuration (endpoints, S3 bucket, API level/version). |
| **`credentials`**| `dhcli credentials [-e <env>] [-o short\|json\|yaml]` | Print active short-lived credentials (AWS S3 keys, DB password, Core access/refresh tokens). |
| **`init`** | `dhcli init [-e\|--environment <env>] (--agent \| --env \| [--pre] [venv_path])` | With `--agent`, install version-pinned agent templates (`AGENTS.md`, `CLAUDE.md`, `.agents/skills/`) in CWD; with `--env`, export config and refreshed credentials to `./.env`; otherwise create/activate a Python venv and install matching `digitalhub[full]` + `digitalhub-runtime-python`. |

### 3.2 Resource CRUD Commands
*(Detailed in [`cli/crud-and-yaml-anatomy.md`](crud-and-yaml-anatomy.md))*

| Command | Syntax | Purpose |
| :--- | :--- | :--- |
| **`create`** | `dhcli create [-p <proj>] [-f <file.yaml>] [-n <name>] [-r] <resource>` | Create a new entity from a YAML file (or create a project by name with `-n <name> projects`). `-r` resets the ID. |
| **`list`** | `dhcli list [-p <proj>] [-n <name>] [-k <kind>] [-s <state>] [-o short\|json\|yaml] <resource>` | List latest versions of resources (or all versions of `<name>` when `-n` is passed). |
| **`get`** | `dhcli get [-p <proj>] [-n <name>] [-o short\|json\|yaml] <resource> [id]` | Retrieve a single resource by `id` (specific version) or `-n <name>` (latest version). |
| **`update`** | `dhcli update [-p <proj>] -f <file.yaml> <resource> <id>` | Update an existing resource's mutable metadata/status from a YAML definition. |
| **`delete`** | `dhcli delete [-p <proj>] [-n <name>] [-y] [-c] <resource> [id]` | Delete a specific version (`id`) or all versions (`-n <name>`). Use `-y` to skip confirmation, `-c` to cascade-delete a project. |

### 3.3 Execution & Monitoring Commands
*(Detailed in [`cli/execution-and-runs.md`](execution-and-runs.md))*

| Command | Syntax | Purpose |
| :--- | :--- | :--- |
| **`run`** | `dhcli run -p <proj> (-n <fn_name> \| -i <fn_id>) [-f <run.yaml>] <task>` | Execute a function task (e.g. `python+build`, `python+job`, `python+serve`, `container+serve`). |
| **`log`** | `dhcli log -p <proj> [-c <container>] [-f] <run_id>` | Fetch stdout/stderr logs of a run (`-f` follows live output every 5s). |
| **`metrics`** | `dhcli metrics -p <proj> [-c <container>] <resource> <id>` | Fetch container CPU, memory, GPU, and network metrics for a run (`dhcli metrics -p <proj> run <run_id>`). |
| **`stop`** | `dhcli stop -p <proj> <run_id>` | Stop an active job, build, or serve run. |

### 3.4 Storage & Service Exposure Commands
*(Detailed in [`cli/storage-and-services.md`](storage-and-services.md))*

| Command | Syntax | Purpose |
| :--- | :--- | :--- |
| **`upload`** | `dhcli upload -p <proj> -n <name> -f <local_path> <resource> [id]` | Upload a local file or directory to S3 and create/update an `artifact`, `model`, or `dataitem`. |
| **`download`** | `dhcli download -p <proj> (-n <name> \| <id>) [-d <dest_path>] <resource>` | Download payload files of an `artifact`, `model`, or `dataitem` from S3 to local disk. |
| **`services`** | `dhcli services -p <proj> [-n <name>] [-k <kind>] [-s <state>] [-o short\|json\|yaml]` | List active service runs (`action=serve`, defaults to `state=RUNNING`). |
| **`port-forward`**| `dhcli port-forward -p <proj> [-l <local_port>] (-f <fn_name> \| -n <run_name> \| <run_id>)` | Open an authenticated local TCP tunnel (`localhost:<port>`) to a remote cluster service. |
| **`proxy`** | `dhcli proxy -p <proj> (-f <fn_name> \| -n <run_name> \| <run_id>)` | Bootstrap an authenticated browser session to a remote web UI/service exposed by a run. |

---

## 4. Operational Rules for AI Agents Using `dhcli`

1. **Always Use Structured Output (`-o json` or `-o yaml`) for Parsing**:
   - Default `-o short` output is formatted for human terminal reading. When inspecting resources to extract `id`, `key`, `spec`, or `status.state`, always pass `-o json` or `-o yaml`:
     ```bash
     dhcli get -p my-project -n my-function functions -o json
     dhcli list -p my-project runs -o json
     ```
2. **Never Block Indefinitely on Interactive Prompts**:
   - `dhcli delete` prompts for `y/n` confirmation on `stdin` unless `-y` (`--confirm`) is passed. After confirming destructive intent with the user, always invoke `dhcli delete -y ...`.
   - `dhcli log -f` loops infinitely every 5 seconds. Agents must call `dhcli log -p <proj> <run_id>` **without** `-f`.
   - `dhcli port-forward` is a long-running foreground tunnel. Run it as a background daemon task if needed, never as a blocking synchronous command.
3. **Create vs. Upload Distinction**:
   - Use **`dhcli upload`** when you have a local file or folder on disk (e.g. `./data.csv`, `./model.pkl`) and want `dhcli` to both upload it to the S3 datalake (`s3://datalake/...`) and register the entity catalog entry.
   - Use **`dhcli create -f <file.yaml>`** when creating `projects`, `functions`, `workflows`, or registering metadata entities that already point to an existing remote path (`s3://`, `https://`, `sql://`).
4. **Resolving the Created Run ID After `dhcli run`**:
   - Because `dhcli run` outputs `Created successfully.`, immediately query the newest run for that function using:
     ```bash
     dhcli list -p <project> runs -o json
     ```
     Sort/pick the first element (newest `metadata.created`) matching `spec.function` to obtain its `id` and `status.state`.
