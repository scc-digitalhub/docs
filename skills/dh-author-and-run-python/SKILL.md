---
name: dh-author-and-run-python
description: >-
  Use this skill when the user asks to create, build, run, or serve a Python
  function (kind: python) on the DigitalHub platform using dhcli. Covers writing
  the Python handler code, Base64-encoding local scripts into the Core-compliant
  function YAML spec, executing build/job/serve tasks via dhcli, and inspecting run logs.
---

# Author and Run a Python Function on DigitalHub (`dhcli`)

Follow this exact procedural workflow whenever creating, building, running, or serving a Python function (`kind: python`) on DigitalHub.

## Prerequisites & Knowledge References
- **CLI Commands & Flags**: [`../../knowledge/cli/index.md`](../../knowledge/cli/index.md)
- **Python Function & Run YAML Schemas**: [`../../knowledge/cli/specs-functions-and-runtimes.md`](../../knowledge/cli/specs-functions-and-runtimes.md)
- **Writing Python Handler Code**: [`../../knowledge/sdk/handler-authoring.md`](../../knowledge/sdk/handler-authoring.md)
- **Entity Keys & Base64 Source Rules**: [`../../knowledge/management/keys-and-lifecycle.md`](../../knowledge/management/keys-and-lifecycle.md)

---

## Step 1: Resolve Target Project
1. If an active project is provided by the Console context or user prompt, use it as `<project>`.
2. Otherwise, check `PROJECT_NAME` or list existing projects:
   ```bash
   dhcli list projects -o json
   ```
   If the target project does not exist yet, create it:
   ```bash
   dhcli create -n <project> projects
   ```

## Step 2: Author the Python Handler Script
1. Write a clean Python script (e.g. `handler.py`) containing your entrypoint function (e.g. `def my_handler(project, run, ...):`).
   - **Rule 1 (Plain Functions)**: Do **NOT** import or use `@handler` from `digitalhub_runtime_python` unless explicitly needed for tuple output mapping. Instead, use the injected `project` and `run` objects directly (`project.log_dataitem(...)`, `project.log_artifact(...)`, `project.log_model(...)`, `run.log_metric(...)`).
   - **Rule 2 (Inputs vs Parameters)**: Handler arguments mapped through `spec.inputs` arrive as `Dataitem`/`Artifact`/`Model` SDK objects (call `.as_df()` or `.as_file()`). Arguments mapped through `spec.parameters` arrive as plain Python primitives (`str`, `int`, `float`, `bool`, `dict`, `list`).
2. **Base64-encode the script** so it can be embedded directly into `spec.source.base64` of the CLI YAML manifest:
   ```bash
   base64 -i handler.py | tr -d '\n'
   ```

## Step 3: Create the Function Entity via `dhcli`
1. Create a `function.yaml` file conforming to the Core `function/python` JSON Schema (**note that `handler`, `lang`, and `base64` MUST be nested under `spec.source`**):
   ```yaml
   kind: python
   name: <function-name>
   project: <project>
   metadata:
     name: <function-name>
     description: "<brief description>"
   spec:
     python_version: PYTHON3_10
     requirements:
       - "<pip-package-1>"
     source:
       lang: python
       handler: <entrypoint-function-name>
       base64: "<single-line-base64-encoded-code>"
   ```
2. Register the function in DigitalHub Core:
   ```bash
   dhcli create -p <project> -f function.yaml functions
   ```
3. Verify creation and retrieve the function's `id` and `key`:
   ```bash
   dhcli get -p <project> -n <function-name> functions -o json
   ```

## Step 4: Build (Optional) & Execute the Run via `dhcli`
1. **When to run `python+build`**:
   - Executing `python+build` is **optional** for standard runs, but recommended when custom third-party `requirements` or system `instructions` (`apt-get`) need to be baked into a reusable container image:
     ```bash
     dhcli run -p <project> -n <function-name> python+build
     ```
2. **Prepare `run.yaml` for `python+job` or `python+serve`**:
   > ⚠️ **MANDATORY SCHEMA FIELD**:
   > When submitting a Run manifest (via `dhcli create -f run.yaml` or `dhcli execute -f run.yaml`), `spec.function` is **STRICTLY REQUIRED** and MUST specify `<kind>://<project>/<function-name>:<func-uuid>`.
   ```yaml
   kind: python+job:run
   project: <project>
   spec:
     function: "python://<project>/<function-name>:<func-uuid>"
     inputs:
       # Map handler arg name -> store://<project>/<entity>/<kind>/<name>:<id>
     parameters:
       # Map handler arg name -> primitive value
     resources:
       cpu:
         requests: "500m"
         limits: "2"
       mem:
         requests: "1Gi"
         limits: "4Gi"
   ```
3. **Execute the task**:
   - For a batch job:
     ```bash
     dhcli run -p <project> -n <function-name> -f run.yaml python+job
     ```
   - For a long-lived HTTP service (`kind: python+serve:run` in `run.yaml`):
     ```bash
     dhcli run -p <project> -n <function-name> -f run.yaml python+serve
     ```

## Step 5: Monitor Run State, Inspect Logs & Report Console Links
1. Retrieve the newly created run's `<run-id>` and `status.state`:
   ```bash
   dhcli list -p <project> runs -o json
   ```
2. Inspect the container execution logs (never pass `-f` in an automated agent call):
   ```bash
   dhcli log -p <project> <run-id>
   ```
3. **If `status.state` is `ERROR`**:
   - Read the traceback from `dhcli log -p <project> <run-id>`.
   - Fix the handler code or `requirements`, re-encode Base64, create a new function version (`dhcli create -p <project> -f function.yaml functions`), and re-run (maximum **2 retry attempts**).
4. **Report Results**:
   - Provide clickable Console links in your final summary:
     - Function: `[Function: <function-name>](/-/<project>/functions/<function-id>/show)`
     - Run: `[Run #<run-id>](/-/<project>/runs/<run-id>/show)`
