# AGENTS.md — DigitalHub Platform Agent Router & Operating Manual

Welcome! This file is the **Single Source of Truth Router** for AI Coding Assistants (GitHub Copilot, Cursor, Windsurf, Claude Code, Antigravity) and the **DigitalHub Platform Agent (`digitalhub-agent`)**.

---

## 1. Golden Architectural Rules (Read Before Taking Any Action)

1. **CLI-First Execution (`dhcli` + Core JSON Schemas)**:
   - All platform management, entity CRUD (`project`, `artifact`, `dataitem`, `model`, `function`, `workflow`, `secret`, `trigger`), file transfers (`upload`, `download`), and task execution (`execute`, `log`, `stop`) **MUST be performed using `dhcli` (`digitalhub-cli`) and declarative YAML manifests**.
   - Do **NOT** use the Python SDK (`import digitalhub as dh`) for host-side orchestration unless the user explicitly asks for an interactive Jupyter Notebook (`.ipynb`).
2. **Strict Separation Between CLI (`dhcli`) and Python SDK (`digitalhub`)**:
   - **Host Side (`dhcli`)**: Creates projects, registers YAML manifests, uploads/downloads files, triggers runs (`python+build:run`, `python+job:run`, `hera+pipeline:run`, `*+serve:run`), and inspects logs.
   - **In-Container Side (`digitalhub` Python SDK)**: Used **inside** the `.py` handler scripts that execute inside Kubernetes pods (`def handler(project, run, ...):` and `def pipeline():`) to read input datasets (`di.as_df()`) and log output datasets (`project.log_dataitem()`), models (`project.log_sklearn()`, `project.log_mlflow()`), artifacts (`project.log_artifact()`), and metrics (`run.log_metric()`).
3. **Critical YAML Schema Rules (`digitalhub-core/schemas/specs/`)**:
   - **Nested `spec.source`**: In `kind: python` Functions and `kind: hera`/`kfp` Workflows, source code **MUST** be nested under `spec.source` (`lang: python`, `handler: <fn_name>`, `base64: <base64_str>`). Never use flattened SDK kwargs (`code_src`, `code`) at the top level of `spec`.
   - **Base64 Encoding for Local `.py` Scripts**: Because `dhcli create -f` sends YAML directly to DigitalHub Core without reading local `.py` files on disk, always Base64-encode local `.py` files (`base64 -i handler.py | tr -d '\n'`) into `spec.source.base64`.
   - **Run Target Format (`spec.function` / `spec.workflow`)**: Inside any `:run` YAML, reference the target Function or Workflow using `<kind>://<project>/<name>:<uuid>` (e.g., `python://my-project/my-fn:a1b2c3d4-...`), **NOT** a `store://` URI.
   - **Input Entity Format (`spec.inputs`)**: Inside any `:run` YAML, reference input Dataitems, Artifacts, and Models using full `store://<project>/<entity-type>/<kind>/<name>:<uuid>` URIs.
   - **RFC-1123 Naming**: All entity `name` fields (`project`, `function`, `workflow`, `dataitem`, `model`, `artifact`) must use lowercase alphanumeric characters and hyphens (`a-z`, `0-9`, `-`) only. Python handler names (`spec.source.handler`) must use `snake_case`.

---

## 2. Procedural Agent Skills (`skills/dh-*/SKILL.md`)

When executing a multi-step platform task, load and follow the corresponding procedural **Skill** runbook first:

| Skill Name | Path | When to Trigger |
| :--- | :--- | :--- |
| **`dh-environment-setup`** | [`skills/dh-environment-setup/SKILL.md`](skills/dh-environment-setup/SKILL.md) | Configuring `dhcli` profiles (`~/.dhcore.ini`), logging in, refreshing tokens, or creating/initializing a DigitalHub Project. |
| **`dh-data-and-storage`** | [`skills/dh-data-and-storage/SKILL.md`](skills/dh-data-and-storage/SKILL.md) | Uploading local files/datasets to S3 (`dhcli upload`), registering external `s3://`/`sql://` tables (`dhcli register`), or downloading entities (`dhcli download`). |
| **`dh-author-and-run-python`** | [`skills/dh-author-and-run-python/SKILL.md`](skills/dh-author-and-run-python/SKILL.md) | Writing a Python function (`job` or `serve`), Base64-encoding the handler, building custom dependencies (`python+build:run`), and running it via `dhcli execute`. |
| **`dh-deploy-container-service`** | [`skills/dh-deploy-container-service/SKILL.md`](skills/dh-deploy-container-service/SKILL.md) | Running custom Docker/OCI containers as Kubernetes batch jobs (`container+job:run`) or HTTP microservices/web apps (`container+serve:run`). |
| **`dh-serve-ml-and-llm`** | [`skills/dh-serve-ml-and-llm/SKILL.md`](skills/dh-serve-ml-and-llm/SKILL.md) | Deploying Scikit-Learn (`sklearnserve`), MLflow (`mlflowserve`), or HuggingFace (`huggingfaceserve`) models, or launching OpenAI-compatible LLMs/Whisper via KubeAI (`kubeai-text`, `kubeai-speech`). |
| **`dh-orchestrate-workflow`** | [`skills/dh-orchestrate-workflow/SKILL.md`](skills/dh-orchestrate-workflow/SKILL.md) | Authoring multi-step Hera/Argo or KFP DAG pipelines in Python, compiling (`hera+build:run`), executing (`hera+pipeline:run`), and attaching `scheduler`/`lifecycle` Triggers. |
| **`dh-troubleshoot-run`** | [`skills/dh-troubleshoot-run/SKILL.md`](skills/dh-troubleshoot-run/SKILL.md) | Diagnosing and fixing `status.state: ERROR` runs, `400 Bad Request` YAML schema errors, Kaniko build failures, Python tracebacks, or Kubernetes `OOMKilled` pods. |

---

## 3. Declarative Knowledge Base Catalog (`knowledge/`)

Master Index: [`knowledge/index.md`](knowledge/index.md)

### Pillar 1: CLI & Core JSON Schema Specifications (`knowledge/cli/`)
| Document | Scope |
| :--- | :--- |
| [`knowledge/cli/index.md`](knowledge/cli/index.md) | `dhcli` command taxonomy, resource mapping (`keys.go`), and global flags (`-p`, `-k`, `-f`, `-o`). |
| [`knowledge/cli/auth-and-env.md`](knowledge/cli/auth-and-env.md) | `~/.dhcore.ini` profiles, `DHCORE_*` environment variables, OAuth2 `login`, `refresh`, `config`, `use`, `version`, and `install`. |
| [`knowledge/cli/crud-and-yaml-anatomy.md`](knowledge/cli/crud-and-yaml-anatomy.md) | `create`, `register`, `get`, `list`, `update`, `delete`, and the 5-block YAML entity anatomy (`project`, `kind`, `name`, `metadata`, `spec`). |
| [`knowledge/cli/execution-and-runs.md`](knowledge/cli/execution-and-runs.md) | `execute` vs `run`, `log`, `stop`, and canonical `:run` YAML payloads (`python+build:run`, `python+job:run`, `python+serve:run`). |
| [`knowledge/cli/storage-and-services.md`](knowledge/cli/storage-and-services.md) | `upload`, `download`, `s3://` file transfer workflows, and `dhcli http` Kubernetes service port-forwarding. |
| [`knowledge/cli/specs-functions-and-runtimes.md`](knowledge/cli/specs-functions-and-runtimes.md) | Core JSON Schema specs for `python`, `container`, `sklearnserve`, `mlflowserve`, `huggingfaceserve`, `kubeai-text`, and `kubeai-speech`. |
| [`knowledge/cli/specs-data-and-storage.md`](knowledge/cli/specs-data-and-storage.md) | Core JSON Schema specs for `project`, `secret`, `artifact`, `dataitem` (`table`, `croissant`), and `model` (`sklearn`, `mlflow`, `huggingface`). |
| [`knowledge/cli/specs-workflows-and-triggers.md`](knowledge/cli/specs-workflows-and-triggers.md) | Core JSON Schema specs for `workflow` (`hera`, `kfp`), `hera+build:run`, `hera+pipeline:run`, and `trigger` (`scheduler`, `lifecycle`). |

### Pillar 2: In-Container Python SDK & Pipeline DSL (`knowledge/sdk/`)
| Document | Scope |
| :--- | :--- |
| [`knowledge/sdk/index.md`](knowledge/sdk/index.md) | Architectural separation of `dhcli` vs `digitalhub` Python SDK, package extras, and automatic in-pod credential detection. |
| [`knowledge/sdk/handler-authoring.md`](knowledge/sdk/handler-authoring.md) | Writing `job`, `serve` (`init_context` + `serve`), and `expose` Python handlers, context injection (`project`, `run`, `context`), and return contracts. |
| [`knowledge/sdk/data-models-and-metrics.md`](knowledge/sdk/data-models-and-metrics.md) | Reading `Dataitem` inputs (`as_df`, `as_file`, `download`) and logging outputs (`log_dataitem`, `log_artifact`, `log_sklearn`, `log_mlflow`, `log_huggingface`, `log_metric`). |
| [`knowledge/sdk/workflow-pipelines-dsl.md`](knowledge/sdk/workflow-pipelines-dsl.md) | Writing multi-step Argo (`digitalhub_runtime_hera.dsl.step`) and KFP (`digitalhub_runtime_kfp.dsl.step`) pipelines in Python. |
| [`knowledge/sdk/interactive-sdk-reference.md`](knowledge/sdk/interactive-sdk-reference.md) | Interactive Jupyter Notebook `import digitalhub as dh` reference (`get_or_create_project`, `new_function`, `func.run()`, `.export()`). |

### Pillar 3: Platform Architecture, K8s Resources & Management (`knowledge/management/`)
| Document | Scope |
| :--- | :--- |
| [`knowledge/management/index.md`](knowledge/management/index.md) | 3-layer platform architecture, entity relationship graph, and storage backends (`s3://`, `sql://`, K8s PVCs). |
| [`knowledge/management/keys-and-lifecycle.md`](knowledge/management/keys-and-lifecycle.md) | Exact `store://` URI grammar, `<kind>://` function/workflow reference formats, entity versioning rules, and Run state machines. |
| [`knowledge/management/kubernetes-resources.md`](knowledge/management/kubernetes-resources.md) | `CoreResource` (`cpu`, `mem`, `gpu`), hardware `profile` templates, `CoreVolume` (`persistent_volume_claim`, `empty_dir`, `ephemeral`, `shared_volume`), `envs`, `secrets`, and `service_ports`. |
| [`knowledge/management/governance-and-security.md`](knowledge/management/governance-and-security.md) | RFC-1123 naming rules, metadata label taxonomy, zero-plaintext secret policy, and GPU/compute resource hygiene. |
| [`knowledge/management/troubleshooting.md`](knowledge/management/troubleshooting.md) | Systematic 3-step run triage protocol and error resolution matrix for CLI auth, YAML validation, Kaniko builds, Python tracebacks, and K8s pod crashes. |

---

## 4. Pre-Flight Verification Checklist Before Executing Any YAML

Before running `dhcli create -f <file.yaml>` or `dhcli execute -f <file.yaml>`, verify:
- [ ] `project` and `name` obey RFC-1123 (`^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`, max 63 chars).
- [ ] For `python` / `hera` / `kfp`, code is nested under `spec.source.base64` (single-line Base64) and `spec.source.handler` is a valid Python `snake_case` function name.
- [ ] For `*:run` kinds, `spec.function` or `spec.workflow` uses `<kind>://<project>/<name>:<uuid>` (**MANDATORY**; omission causes immediate `ERROR`).
- [ ] For `*:run` kinds, `spec.inputs` values use `store://<project>/<entity-type>/<kind>/<name>:<uuid>`.
- [ ] All `spec.envs[].value` entries are quoted strings.
