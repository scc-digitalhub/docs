---
name: dh-troubleshoot-run
description: Diagnose and fix failed DigitalHub Runs (ERROR state), YAML schema validation errors, Kaniko container build failures, Python handler exceptions, and Kubernetes pod crashes using dhcli.
---

# Skill: Troubleshooting Failed Runs & CLI Errors

Use this procedural workflow whenever a `dhcli` command returns an error or a DigitalHub Run (`python+job:run`, `python+build:run`, `hera+pipeline:run`, `*+serve:run`) enters `status.state: ERROR` or gets stuck in `PENDING`/`RUNNING`.

## Reference Knowledge
- [troubleshooting.md](../../knowledge/management/troubleshooting.md)
- [execution-and-runs.md](../../knowledge/cli/execution-and-runs.md)
- [kubernetes-resources.md](../../knowledge/management/kubernetes-resources.md)

---

## Step-by-Step Diagnostic Procedure

### Step 1: Inspect the Run Status YAML
Fetch the full Run object to examine `status.state`, `status.message`, and Kubernetes pod status:
```bash
dhcli get run <run-uuid> -p <project-name> -o yaml
```
Check what phase failed:
- Did it fail immediately before pod creation? -> **Schema / Task / Entity Reference Error**.
- Did it fail during container startup (`Pending`, `ImagePullBackOff`, `OOMKilled`)? -> **Kubernetes Resource / Image Error**.
- Did the container execute and exit with a non-zero code? -> **Application / Python Handler / Build Error**.

### Step 2: Retrieve Pod Logs (`dhcli log`)
Fetch the container stdout/stderr logs for the failed Run:
```bash
dhcli log <run-uuid> -p <project-name>
```
*(Optional: Save logs to a file for multi-line stack trace analysis via `dhcli log <run-uuid> -p <project-name> --save ./failed-run.log`).*

### Step 3: Match Symptom to Root Cause & Fix

#### Case A: Python Handler Exception (`TypeError`, `KeyError`, `ModuleNotFoundError`, `FileNotFoundError`)
1. **`ModuleNotFoundError`**:
   - Inspect the parent Function (`dhcli get function <fn-name> --id <fn-uuid> -p <project-name> -o yaml`).
   - Add the missing package to `spec.requirements`, update the function, and run `kind: python+build:run` until `COMPLETED` before re-running `python+job:run`.
2. **`FileNotFoundError` on Handler Script**:
   - The Function was created with `spec.source.source` pointing to a local file path instead of `spec.source.base64`.
   - Base64-encode the local `.py` file (`base64 -i handler.py | tr -d '\n'`), set `spec.source.base64`, update the Function, and re-run.
3. **`TypeError: unexpected keyword argument`**:
   - Align the keys in the Run's `spec.inputs` and `spec.parameters` with the argument names of `def handler(...):`.

#### Case B: Kaniko Image Build Failure (`python+build:run` -> `ERROR`)
1. Inspect `dhcli log <build-run-uuid> -p <project-name>`.
2. Fix invalid package versions in `spec.requirements` or add missing OS apt packages in `spec.build.instructions: ["RUN apt-get update && apt-get install -y <pkg>"]`.

#### Case C: Kubernetes `OOMKilled` (Exit Code 137) or `Pending` Resources
1. If `OOMKilled`: Edit the Run YAML to increase `spec.resources.mem.requests` and `spec.resources.mem.limits` (e.g., to `"8Gi"`), and add a `/dev/shm` `empty_dir` (`medium: "Memory"`) volume if running PyTorch or vLLM.
2. If `Pending` due to insufficient CPU/Memory/GPU: Reduce `spec.resources.*.requests` or verify the cluster hardware `spec.profile`.

### Step 4: Re-Execute & Verify Recovery
Submit a new Run with the corrected YAML and verify it reaches `COMPLETED` (for jobs/builds) or `RUNNING` (for services):
```bash
dhcli execute -f fixed-run.yaml -p <project-name>
dhcli get run <new-run-uuid> -p <project-name> -o yaml
```

