---
id: mgmt-governance-and-security
domain: management
type: reference
version: "0.16"
tags: [governance, security, naming, rfc-1123, labels, metadata, secrets, rbac, best-practices]
summary: Governance standards, RFC-1123 naming rules, metadata labeling conventions, secret security policies, and resource hygiene for the DigitalHub Platform.
---

# Platform Governance, Naming Standards & Security Rules

All automated agents (`digitalhub-agent`, IDE agents, CI/CD pipelines) and developers operating on the DigitalHub Platform must comply with these governance, naming, and security standards.

---

## 1. Strict Naming Conventions (RFC-1123 Compliance)

Because DigitalHub Core translates entity names (`project`, `function`, `workflow`, `service`, `volume`) into Kubernetes namespaces, Jobs, Deployments, Services, and Argo DAG nodes, **all entity names must obey RFC-1123 DNS label rules**:

| Rule | Requirement | Valid Example | Invalid Example |
| :--- | :--- | :--- | :--- |
| **Character Set** | Lowercase alphanumeric (`a-z`, `0-9`) and hyphens (`-`) only. | `fraud-rf-model-v2` | `Fraud_RF_Model` (uppercase & underscores) |
| **Start & End** | Must start with a lowercase letter (`a-z`) and end with an alphanumeric (`a-z`, `0-9`). | `ingest-transactions-2026` | `-ingest-data-`, `123-model` |
| **Maximum Length** | Maximum **63 characters** (keep Function and Workflow names **<= 40 characters** so K8s pod suffixes `-job-xxxxx` fit within 63 chars). | `train-xgb-classifier` | `very-long-function-name-exceeding-kubernetes-pod-label-limit-63-chars` |
| **Python Handler Names** | Python function/handler identifiers (`spec.source.handler`) must use **snake_case** (`a-z`, `0-9`, `_`). | `train_model`, `serve_request` | `train-model` (invalid Python identifier) |

---

## 2. Metadata & Labeling Standards

Every entity created via `dhcli create` or `dhcli register` should include a descriptive `metadata` block to ensure discoverability in the DigitalHub catalog:

```yaml
metadata:
  name: transactions-cleaned-2026
  description: "Cleaned credit card transactions with engineered rolling window features"
  labels:
    - domain:finance
    - tier:silver
    - managed-by:dhcli
```

### Recommended Label Taxonomy
- **Data Tier (`dataitem`)**: `tier:bronze` (raw ingested data), `tier:silver` (cleaned/validated data), `tier:gold` (feature-engineered/aggregated data).
- **Lifecycle Stage (`model`, `function`)**: `stage:dev`, `stage:staging`, `stage:production`.
- **Origin**: `managed-by:dhcli`, `managed-by:agent`, `managed-by:hera-pipeline`.

---

## 3. Secret & Credential Security Policy

1. **Zero Plaintext Secrets in YAML**:
   - **NEVER** hardcode API keys, database passwords, S3 secret keys, or OAuth tokens inside `spec.envs`, `spec.parameters`, or Python source code (`spec.source.base64`).
   - Always store sensitive values as DigitalHub `secret` entities (`kind: secret`) and inject them via `spec.secrets: ["MY_SECRET_NAME"]`.
2. **CLI Token Hygiene**:
   - Store `dhcli` credentials in `~/.dhcore.ini` (via `dhcli login` or `dhcli config`) rather than passing `--token` inline in shared shell histories.
   - If using `DHCORE_PERSONAL_ACCESS_TOKEN` or `DHCORE_ACCESS_TOKEN` in CI/CD, inject them from masked CI secret stores.
3. **Database Connections (`sql://`)**:
   - When reading from external databases inside Python handlers, construct connection strings dynamically from environment variables injected via `spec.secrets` rather than embedding `user:password@host` in `Dataitem` specs.

---

## 4. Resource Hygiene & Cost Control

1. **Always Set Resource Requests & Limits for Production Runs**:
   - Unbounded jobs can starve shared Kubernetes nodes. Always specify `spec.resources.cpu` and `spec.resources.mem` on heavy training jobs (`python+job:run`) and long-running services (`*+serve:run`).
2. **GPU Discipline**:
   - Only request `spec.resources.gpu` (or GPU `spec.profile` such as `1xa100`) for workloads that actively utilize CUDA (`huggingfaceserve`, `kubeai-text`, PyTorch/TensorFlow training).
   - Never leave idle GPU `serve` deployments running indefinitely in development projects; stop or delete unused `serve` runs via `dhcli delete run <run-id> -p <project>`.
3. **Container Build Optimization (`python+build`)**:
   - If a Python function only uses standard pre-installed packages (`pandas`, `numpy`, `pyarrow`, `requests`), run `python+job` directly without running `python+build`.
   - When custom `spec.requirements` are needed, pin exact package versions (e.g., `scikit-learn==1.5.1`) and run `python+build` **once**; reuse the built image across all subsequent `python+job` and `python+serve` runs.

