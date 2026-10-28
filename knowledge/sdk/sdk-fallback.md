---
title: Python SDK Fallback for CLI Gaps
description: Minimal one-line Python SDK recipes for operations not exposed as dhcli commands (executing workflows, creating secrets, and attaching triggers).
---

# Python SDK Fallback for `dhcli` Gaps

`dhcli` is the primary host-side interface for DigitalHub, supporting full CRUD on `projects`, `functions`, `workflows`, `runs`, `dataitems`, `artifacts`, `models`, and `logs`, plus `run`, `upload`, `download`, `services`, `port-forward`, `proxy`, `metrics`, `events`, and `stop`.

Three platform operations are not exposed as `dhcli` commands in `0.15`/`0.16`:
1. **Building & running a `Workflow` (`hera` / `kfp`)** — `dhcli run` targets `/functions` only.
2. **Creating a project `Secret` (`kind: secret`)** — `secret` is not in `dhcli`'s `keys.Resources`.
3. **Creating a `Trigger` (`kind: scheduler` / `lifecycle`)** — `trigger` is not in `dhcli`'s `keys.Resources`.

For these three cases, use a one-line `python3 -c` invocation inside the Python virtual environment created by `dhcli init` (which shares `~/.dhcore.ini` credentials with `dhcli` automatically).

## 1. Ensure the SDK Virtual Environment Exists

```bash
# Bootstrap or activate a local venv matching the Core version
echo y | dhcli init ./.venv
source ./.venv/bin/activate
```

## 2. Build & Execute a Workflow (`hera` or `kfp`)

Register the workflow YAML first via `dhcli create workflows -p <project> -f workflow.yaml`, then run `build` and `pipeline`:

```bash
python3 -c '
import digitalhub as dh
wf = dh.get_project("<project>").get_workflow("<workflow-name>")
wf.run("build", wait=True)
run = wf.run("pipeline", parameters={"param1": "value1"})
print("Pipeline run ID:", run.id)
'
```

Monitor the resulting run normally via `dhcli get runs <run-id> -p <project> -o yaml` and `dhcli log <run-id> -p <project>`.

## 3. Create a Project Secret (`kind: secret`)

```bash
python3 -c '
import digitalhub as dh
p = dh.get_project("<project>")
p.new_secret(name="DB_PASSWORD", secret_value="<secret-value>")
'
```

Then mount `DB_PASSWORD` in any `dhcli run` manifest via `spec.secrets: ["DB_PASSWORD"]`.

## 4. Attach a Cron or Lifecycle Trigger (`kind: scheduler`, `lifecycle`)

```bash
python3 -c '
import digitalhub as dh
fn = dh.get_project("<project>").get_function("<function-name>")
fn.trigger(
    action="job",
    name="nightly-job",
    kind="scheduler",
    schedule="0 0 2 * * ?",
    parameters={"window": "1d"},
)
'
```
