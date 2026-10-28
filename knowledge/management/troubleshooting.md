---
id: mgmt-troubleshooting
domain: management
type: runbook
version: "0.16"
tags: [troubleshooting, errors, debugging, logs, status, oomkilled, kaniko, build, schema-error, auth-error]
summary: Diagnostic runbook and error resolution catalog for dhcli authentication, YAML schema validation errors, Kaniko image build failures, Python handler exceptions, and Kubernetes pod crashes.
---

# Diagnostic & Troubleshooting Runbook

When a `dhcli` command fails or a Run enters `status.state: ERROR`, follow the systematic diagnostic workflow below to pinpoint and resolve the root cause.

---

## 1. Systematic 3-Step Triage Protocol for Failed Runs

Whenever a Run (`python+job:run`, `python+build:run`, `hera+pipeline:run`, `*+serve:run`) fails or stalls:

```bash
# Step 1: Inspect the Run status (exclude heavy k8s block to avoid truncation)
dhcli get runs <run-uuid> -p <project-name> -o json | jq 'del(.status.k8s)'

# Step 2: Fetch container logs (live pod) or persisted logs (terminated pod)
dhcli log <run-uuid> -p <project-name>
# If returns "Failed: container not found":
dhcli list logs -p <project-name> -o json | jq -r '.[] | select(.run == "<run-uuid>") | .content | @base64d'

# Step 3: Verify the referenced Function/Workflow and Input entities exist and are READY
dhcli get functions -p <project-name> -n <fn-name> -o json
```

---

## 2. CLI & Authentication Errors

| Error / Symptom | Root Cause | Exact Resolution |
| :--- | :--- | :--- |
| `401 Unauthorized` or `invalid_grant` / `token expired` | The `access_token` in `~/.dhcore.ini` has expired and no `refresh_token` or PAT is configured. | Run `dhcli login <profile>` to refresh OAuth2 tokens, or configure `DHCORE_PERSONAL_ACCESS_TOKEN` in your environment. |
| `connection refused` or `no such host` on `dhcli` command | `DHCORE_ENDPOINT` is missing, points to `localhost` instead of the cluster URL, or the wrong profile is active. | Run `dhcli list-env` and `dhcli config` to inspect profiles, then switch profile via `dhcli use <profile>` or register with `dhcli register -e <profile> https://<dhcore-host>`. |
| `resource not supported` on `dhcli list secrets` or `dhcli list triggers` | `digitalhub-cli` v0.15 `keys.Resources` map only supports `projects`, `artifacts`, `dataitems`, `models`, `functions`, `workflows`, `runs`, and `logs` for positional resource lookup. | Manage `secret`, `trigger`, and `task` entities via file-driven `dhcli create -f <file.yaml> -p <project>` and `dhcli update -f <file.yaml> -p <project>`. |

---

## 3. Core JSON Schema & YAML Validation Errors (`400 Bad Request`)

| Error / Symptom | Root Cause | Exact Resolution |
| :--- | :--- | :--- |
| `spec.source: is required` when creating a `python` function or `hera` workflow | Used Python SDK flattened kwargs (`code_src`, `code`, `handler` at top level of `spec`) instead of the Core JSON Schema `spec.source` object. | Nest `lang`, `handler`, and `base64` (or `source`) inside `spec.source:` (see [function.md](../entities/function.md) and [runtimes/index.md](../runtimes/index.md)). |
| `spec.function` or `spec.workflow` invalid format in `:run` YAML | Passed a `store://` URI or omitted the `:uuid` suffix in `spec.function` / `spec.workflow`. | Format `spec.function` as `<func-kind>://<project>/<func-name>:<func-uuid>` (e.g., `python://my-proj/my-fn:uuid`). |
| `spec.envs[0].value: must be string` | Passed an unquoted integer or boolean in `spec.envs` (`value: 8080` or `value: true`). | Quote all environment variable values as strings (`value: "8080"`, `value: "true"`). |
| `invalid entity name` / regex validation failure | Entity `name` contains uppercase letters, underscores (`_`), spaces, or exceeds 63 characters. | Rename entity using RFC-1123 lowercase alphanumeric + hyphens (`my-clean-name`). |

---

## 4. Python Runtime & Handler Execution Errors (`status.state: ERROR`)

Inspect `dhcli log <run-uuid> -p <project-name>` to identify the Python traceback:

| Traceback / Log Error | Root Cause | Exact Resolution |
| :--- | :--- | :--- |
| `FileNotFoundError` or empty code execution inside `python+job:run` | Created the `python` function via `dhcli create -f` using `spec.source.source: "src/main.py"` (a local path on your laptop) instead of Base64-encoding the script into `spec.source.base64`. | Base64-encode the local `.py` file (`base64 -i src/main.py \| tr -d '\n'`), place it in `spec.source.base64`, and update/recreate the function. |
| `TypeError: handler() got an unexpected keyword argument '<key>'` | A key declared in the Run's `spec.inputs` or `spec.parameters` does not match any parameter in `def handler(...):` and `**kwargs` is not present. | Match `spec.inputs` and `spec.parameters` keys 1-to-1 with your Python handler arguments, or add `**kwargs` to the handler signature. |
| `ModuleNotFoundError: No module named '<pkg>'` | The handler imports a third-party package listed in `spec.requirements`, but `python+build` was never executed (or is still `RUNNING`). | Execute `dhcli run python+build -p <project> -n <fn-name>`, wait until `status.state` is `COMPLETED`, and confirm `spec.image` is populated on the function before running `dhcli run python+job`. |
| `TypeError: Object of type float32 / int64 is not JSON serializable` | Handler returned or logged a NumPy scalar (`np.float32`, `np.int64`) in metrics or parameters. | Wrap numeric metrics/parameters in native Python `float(val)` or `int(val)`. |

---

## 5. Kaniko Container Build Failures (`python+build:run` -> `ERROR`)

When `python+build:run` fails, run `dhcli log <build-run-uuid> -p <project>`:

1. **`pip install` Dependency Conflict or Missing Version**:
   - Check `spec.requirements` on the `python` function. Ensure package names are spelled correctly (e.g., `scikit-learn` instead of `sklearn`) and compatible with the chosen `spec.python_version` (`PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`).
2. **System C-Library Missing during Pip Wheel Compilation**:
   - If a Python library requires OS-level system packages (e.g., `libpq-dev`, `gcc`, `ffmpeg`), add them to `spec.build.instructions`:
     ```yaml
     spec:
       build:
         instructions:
           - "RUN apt-get update && apt-get install -y gcc libpq-dev"
     ```

---

## 6. Kubernetes Pod Infrastructure Errors

When `dhcli get run <run-uuid> -p <project> -o yaml` shows pod-level failures before or during execution:

| Kubernetes Status / Reason | Root Cause | Exact Resolution |
| :--- | :--- | :--- |
| `OOMKilled` (Exit Code `137`) | The container exceeded its memory limit (`spec.resources.mem.limits`), commonly when loading a large Parquet file into Pandas or loading a large LLM. | Increase `spec.resources.mem.requests` and `spec.resources.mem.limits` (e.g., from `"2Gi"` to `"8Gi"` or `"16Gi"`), and if running PyTorch/vLLM, mount an in-memory `/dev/shm` `empty_dir` volume. |
| `Pending` (`0/N nodes are available: Insufficient cpu / memory / nvidia.com/gpu`) | The requested `spec.resources` or `spec.profile` exceeds available cluster node capacity, or no GPU node pool is free. | Lower `requests` to fit cluster capacity, verify the GPU `profile` name with cluster admins, or stop idle `serve` deployments consuming GPUs. |
| `ImagePullBackOff` / `ErrImagePull` | The container image in `spec.image` does not exist, has a typo in the tag, or requires private registry credentials (`image_pull_secrets`). | Verify the image tag exists and is accessible from the cluster. |
| `CrashLoopBackOff` on `*+serve:run` | For `python+serve`, `init_context` raised an exception (e.g., model not found) or `spec.source.init_function` was misconfigured; for `sklearnserve`/`mlflowserve`, `spec.path` points to an invalid model file. | Run `dhcli log <serve-run-uuid> -p <project>` to inspect the startup stack trace and verify the model `store://` URI or S3 path. |

