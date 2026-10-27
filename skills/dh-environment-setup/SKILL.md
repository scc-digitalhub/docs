---
name: dh-environment-setup
description: Configure and verify the DigitalHub CLI (dhcli) environment, manage authentication profiles in ~/.dhcore.ini, and initialize or inspect DigitalHub projects.
---

# Skill: DigitalHub Environment Setup & Project Initialization

Use this procedural workflow whenever starting work in a workspace, switching DigitalHub environments, refreshing expired OAuth2 tokens, or initializing a new DigitalHub project.

## Reference Knowledge
- [auth-and-env.md](../../knowledge/cli/auth-and-env.md)
- [specs-data-and-storage.md](../../knowledge/cli/specs-data-and-storage.md)
- [governance-and-security.md](../../knowledge/management/governance-and-security.md)

---

## Step-by-Step Procedure

### Step 1: Verify `dhcli` Installation & Version Compatibility
Check that `dhcli` is installed and verify its version matches the target DigitalHub Core minor version (`0.15.x`):
```bash
dhcli --version
```
*(If `dhcli` is missing, install it using `dhcli install 0.15.0` or verify your `PATH`).*

### Step 2: Inspect Active Configuration Profile (`~/.dhcore.ini`)
List all configured profiles and identify the active endpoint:
```bash
dhcli config list
```
- If the desired profile is already listed but inactive, switch to it:
  ```bash
  dhcli use <profile-name>
  ```
- If no profile exists for the target DigitalHub Core URL, create one:
  ```bash
  dhcli config <profile-name> -e https://<dhcore-endpoint>
  dhcli use <profile-name>
  ```

### Step 3: Verify Connectivity & Authentication
Test authentication by listing projects on the cluster:
```bash
dhcli list projects
```
- If `dhcli list projects` returns `401 Unauthorized` or token expiration errors:
  - In interactive environments, run `dhcli login <profile-name>`.
  - In headless/CI/agent environments, verify that `DHCORE_PERSONAL_ACCESS_TOKEN` or `DHCORE_ACCESS_TOKEN` and `DHCORE_ENDPOINT` are exported in the shell.

### Step 4: Initialize or Verify the Target Project
Check whether the target project (must obey RFC-1123 lowercase alphanumeric + hyphens, e.g., `fraud-detection`) already exists:
```bash
dhcli get project <project-name> -o yaml
```
If the project does not exist, create a `project.yaml` manifest and apply it via `dhcli create`:
```yaml
kind: project
name: <project-name>
metadata:
  name: <project-name>
  description: "Project created and managed via dhcli"
  labels:
    - managed-by:dhcli
spec: {}
```
```bash
dhcli create -f project.yaml
```

### Step 5: Verify Project Readiness
Confirm the project is created and inspect existing functions, dataitems, and models inside it:
```bash
dhcli list functions -p <project-name>
dhcli list dataitems -p <project-name>
dhcli list models -p <project-name>
```

