# Working with Agents

DigitalHub provides first-class support for AI coding assistants (such as **Claude Code**, **GitHub Copilot**, **Cursor**, **Windsurf**, **Codex**, and **Antigravity**) and autonomous platform agents through the DigitalHub CLI (`dhcli`).

With a single command (`dhcli init --agent`), you can bootstrap any project repository with:

- **`AGENTS.md`**: The single source of truth router and operating manual for AI agents working with DigitalHub.
- **`CLAUDE.md`**: An entry-point pointer directing Claude Code to read and follow `AGENTS.md`.
- **`.agents/skills/dh-*/SKILL.md`**: 10 self-contained, step-by-step procedural runbooks covering every core platform workflow (environment setup, Python functions, S3 data/artifacts, dbt SQL transformations, containers, ML/LLM serving, guardrails, Hera/KFP workflows, secrets, and run troubleshooting).
- **Version-Pinned Remote Knowledge Base**: All documentation links inside `AGENTS.md` and `.agents/skills/` are automatically pinned to the `major.minor` release branch of your connected DigitalHub Core instance (for example, Core `0.16.2` pins to `0.16`).

---

## Architecture Overview: Router, Local Skills & Version-Pinned Knowledge

DigitalHub separates agent instructions into two layers so that your local repository stays lightweight while always matching the exact API and schema version of your connected platform:

```text
digitalhub-cli (embedded templates)       Your Project Workspace (after dhcli init --agent)
  templates/AGENTS.md          ───────►     AGENTS.md
  templates/CLAUDE.md          ───────►     CLAUDE.md
  templates/skills/dh-*/       ───────►     .agents/skills/dh-*/SKILL.md
                                                      │
                                                      ▼ (fetched on demand, pinned to Core major.minor)
                                            https://raw.githubusercontent.com/scc-digitalhub/docs/<major.minor>/knowledge/
                                              ├── llms.txt & index.md
                                              ├── entities/     (project, function, workflow, task, run, ...)
                                              ├── runtimes/     (python, container, dbt, hera, kfp, vllmserve, ...)
                                              ├── cli/          (index, auth-and-env, crud-and-yaml-anatomy, ...)
                                              ├── sdk/          (handler-authoring, data-models-and-metrics, ...)
                                              └── management/   (keys-and-lifecycle, kubernetes-resources, ...)
```

1. **Embedded Agent Router & Procedural Skills (Local)**:
   `AGENTS.md`, `CLAUDE.md`, and `.agents/skills/dh-*/SKILL.md` are embedded directly inside the `dhcli` binary (`templates/`). Running `dhcli init --agent` renders them into your current working directory without requiring Python or downloading files from GitHub.
2. **Version-Pinned Knowledge Base (Remote, On-Demand)**:
   During `dhcli init --agent`, the CLI queries the active Core endpoint's `/.well-known/configuration`, reads `dhcore_version` (for example, `0.16.2`), and substitutes every `<%DOCS%>` template placeholder with `https://raw.githubusercontent.com/scc-digitalhub/docs/0.16`. When an AI agent needs an entity schema or runtime specification, it fetches only the relevant Markdown page from that release branch's `knowledge/` directory.

!!! info "Strict Version Pinning"
Agents are instructed never to fall back to `main`, `latest`, or a different release branch if a knowledge URL is unreachable. Relative links inside fetched knowledge pages resolve against the fetched page's URL, keeping the agent on the exact same `major.minor` release.

---

## Prerequisites

Before initializing an agent workspace, make sure `dhcli` is installed and connected to a DigitalHub Core environment:

1. **Register your DigitalHub Core endpoint** (if not already registered):
   ```sh
   dhcli register -e my-env https://core.digitalhub.example.com
   dhcli use my-env
   ```
2. **Authenticate**:
   - **Interactive workstation (OAuth2 PKCE browser login)**:
     ```sh
     dhcli login
     ```
   - **Headless / Agent / CI environment ([Personal Access Token](pat.md))**:
     ```sh
     dhcli login --pat "<your-personal-access-token>"
     # Or via environment variable:
     export DHCORE_PERSONAL_ACCESS_TOKEN="<your-personal-access-token>"
     dhcli login
     ```

---

## Step 1: Bootstrap an Agent Workspace (`dhcli init --agent`)

From the root of your project repository, run:

```sh
dhcli init --agent
```

To use a specific registered environment instead of the current default, pass `--environment` (`-e`):

```sh
dhcli init --agent --environment my-env
```

### What `dhcli init --agent` Creates

The command inspects your connected Core version and writes the following structure into the current working directory:

```text
.
├── AGENTS.md
├── CLAUDE.md
└── .agents/
    └── skills/
        ├── dh-author-and-run-python/
        │   └── SKILL.md
        ├── dh-data-and-storage/
        │   └── SKILL.md
        ├── dh-deploy-container-service/
        │   └── SKILL.md
        ├── dh-environment-setup/
        │   └── SKILL.md
        ├── dh-guardrail-and-evaluate-llm/
        │   └── SKILL.md
        ├── dh-orchestrate-workflow/
        │   └── SKILL.md
        ├── dh-secure-and-configure-secrets/
        │   └── SKILL.md
        ├── dh-serve-ml-and-llm/
        │   └── SKILL.md
        ├── dh-transform-with-dbt/
        │   └── SKILL.md
        └── dh-troubleshoot-run/
            └── SKILL.md
```

### Safe File Handling & Idempotency

- **No Python dependency required**: `dhcli init --agent` does **not** create a Python virtual environment or install Python packages.
- **Idempotent re-runs**: If you run `dhcli init --agent` again against the same Core `major.minor` version and the existing files are identical, they are left untouched.
- **Conflict protection**: Existing files with different content (for example, local customizations or templates pinned to another Core version) are **never overwritten**. Move conflicting files aside and reconcile your changes before re-initializing.
- **Symlink rejection & atomic rollback**: Symlinked target paths or directories are rejected, and any failed installation automatically rolls back newly created files and directories.

---

## Step 2: Optional Python SDK Virtual Environment (`dhcli init [path]`)

While AI agents execute nearly all platform operations directly via `dhcli` and declarative YAML manifests, a local Python virtual environment with `digitalhub[full]` is useful in two scenarios:

1. Authoring and running interactive Jupyter notebooks (`.ipynb`).
2. Executing the three SDK gap fallbacks for operations not directly exposed as standalone `dhcli` commands (triggering a `workflow` pipeline run, creating a project `secret`, or attaching a `trigger`).

To create or update a Python virtual environment pinned to your connected Core's `major.minor` release:

```sh
dhcli init ./.venv
```

In non-interactive shells or agent sessions, pipe confirmation to `stdin`:

```sh
echo y | dhcli init ./.venv
```

---

## Included Agent Skills Reference (`.agents/skills/`)

Once `dhcli init --agent` has been executed, AI coding assistants automatically discover `AGENTS.md` and load the appropriate procedural skill from `.agents/skills/`:

| Skill Name                            | Path                                                      | When to Use                                                                                                                                                                                                                                   |
| :------------------------------------ | :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`dh-environment-setup`**            | `.agents/skills/dh-environment-setup/SKILL.md`            | Registering Core endpoints (`dhcli register`), authenticating (`dhcli login`), switching environments (`dhcli use`), bootstrapping `.venv` (`dhcli init`), and creating projects.                                                             |
| **`dh-secure-and-configure-secrets`** | `.agents/skills/dh-secure-and-configure-secrets/SKILL.md` | Creating Kubernetes-backed project secrets via the Python SDK fallback and mounting them into runs via `spec.secrets`.                                                                                                                        |
| **`dh-data-and-storage`**             | `.agents/skills/dh-data-and-storage/SKILL.md`             | Uploading local files, folders, datasets, and models to S3 (`dhcli upload`), registering remote `s3://`, `https://`, or `sql://` tables, and downloading entities (`dhcli download`).                                                         |
| **`dh-author-and-run-python`**        | `.agents/skills/dh-author-and-run-python/SKILL.md`        | Authoring Python `job` and Nuclio `serve` handlers, Base64-encoding scripts into `spec.source.base64`, building custom images (`python+build`), and running via `dhcli run`.                                                                  |
| **`dh-transform-with-dbt`**           | `.agents/skills/dh-transform-with-dbt/SKILL.md`           | Writing SQL data transformations in dbt, Base64-encoding `.sql` queries into `kind: dbt` functions, and executing `dbt+transform` runs over tabular `Dataitem` inputs.                                                                        |
| **`dh-deploy-container-service`**     | `.agents/skills/dh-deploy-container-service/SKILL.md`     | Running custom Docker/OCI images as Kubernetes batch jobs (`container+job`), web UIs or APIs (`container+serve`), persistent deployments (`container+deploy`), or in-cluster image builds (`container+build`).                                |
| **`dh-serve-ml-and-llm`**             | `.agents/skills/dh-serve-ml-and-llm/SKILL.md`             | Deploying Scikit-Learn (`sklearnserve`), MLflow (`mlflowserve`), HuggingFace (`huggingfaceserve`), vLLM (`vllmserve-text`, `vllmserve-speech`, `vllmserve-pooling`), and KubeAI (`kubeai-text`, `kubeai-speech`) inference services.          |
| **`dh-guardrail-and-evaluate-llm`**   | `.agents/skills/dh-guardrail-and-evaluate-llm/SKILL.md`   | Deploying real-time LLM input/output safety guardrails (`guardrail+serve`) and standardized KServe OpenInference v2 Python handlers (`openinference+serve`).                                                                                  |
| **`dh-orchestrate-workflow`**         | `.agents/skills/dh-orchestrate-workflow/SKILL.md`         | Authoring multi-step DAG pipelines in Python using Hera (Argo Workflows) or Kubeflow Pipelines (KFP), registering workflows (`dhcli create workflows`), building/running pipelines, and attaching cron (`scheduler`) or `lifecycle` triggers. |
| **`dh-troubleshoot-run`**             | `.agents/skills/dh-troubleshoot-run/SKILL.md`             | Diagnosing failed (`ERROR`) or stuck (`READY`/`RUNNING`) runs, inspecting live container logs (`dhcli log`) or persisted Base64 `log` entities, and checking pod metrics (`dhcli metrics`).                                                   |

---

## Core Operating Rules for AI Agents

The installed `AGENTS.md` enforces several golden rules that keep agent workflows deterministic and safe:

1. **CLI-First Execution (`dhcli` + Declarative YAML)**:
   All host-side entity CRUD (`projects`, `functions`, `workflows`, `runs`, `dataitems`, `artifacts`, `models`, `logs`), S3 transfers (`upload`, `download`), task execution (`run`), log inspection (`log`), and service exposure (`services`, `port-forward`, `proxy`) use `dhcli` and YAML manifests.
2. **Host CLI vs. In-Container SDK Separation**:
   `dhcli` manages platform entities and runs from the host machine, while the `digitalhub` Python SDK is used inside container handler scripts (`def handler(project, run, ...):`) to read inputs (`di.as_df()`) and log outputs (`project.log_dataitem()`, `project.log_model()`, `run.log_metric()`).
3. **Base64 Source Encoding for Code-Backed Entities**:
   Because `dhcli create` submits YAML manifests directly to the Core REST API without reading external `.py` or `.sql` files from local disk, agents Base64-encode local handler scripts (`base64 -i handler.py | tr -d '\n'`) into `spec.source.base64`.
4. **Non-Blocking Inspection**:
   Agents always request structured output (`-o json` or `-o yaml`) for programmatic inspection and never pass blocking streaming flags like `dhcli log -f` or `dhcli metrics -f` inside automated tool calls.

---

## End-to-End Example: Using an AI Agent on a New Project

```sh
# 1. Authenticate with DigitalHub Core
dhcli register -e dev https://core.digitalhub.example.com
dhcli use dev
dhcli login --pat "<your-pat>"

# 2. Create a project directory and install version-pinned agent instructions & skills
mkdir my-ai-project && cd my-ai-project
dhcli init --agent

# 3. Launch your AI coding assistant (e.g., Claude Code, GitHub Copilot, Cursor)
# Prompt example:
 Create a project called 'iris-ml-project', register the dataset from
 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv',
 write a python function that trains a Scikit-Learn RandomForest classifier
 on it,  and run the job to log the metrics and final model."
```

Your AI assistant will automatically read `AGENTS.md`, follow `.agents/skills/dh-environment-setup/SKILL.md`, `.agents/skills/dh-data-and-storage/SKILL.md`, and `.agents/skills/dh-author-and-run-python/SKILL.md`, and consult the remote `knowledge/` pages matching your Core version.
