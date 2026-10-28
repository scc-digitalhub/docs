---
id: cli-auth-and-env
domain: cli
type: operational_guide
version: "0.16"
tags: [cli, dhcli, register, login, pat, use, list-env, refresh, config, credentials, init, dhcore.ini]
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
summary: "Registering DigitalHub Core endpoints, OAuth2 PKCE vs non-interactive PAT login, managing multiple environments in `.dhcore.ini`, inspecting short-lived credentials, and bootstrapping workspaces with `dhcli init`."
---

# CLI Environment Registration, Authentication & Configuration

The DigitalHub CLI (`dhcli`) manages platform endpoints, OAuth2 tokens, and S3/DB credentials inside an INI configuration file (`.dhcore.ini`). Both `dhcli` and the Python SDK (`digitalhub`) share this configuration file automatically.

---

## 1. Configuration File Resolution (`.dhcore.ini`)

`dhcli` resolves `.dhcore.ini` in the following strict priority order:
1. **`DH_CONFIG` environment variable**: If set (e.g. `export DH_CONFIG=/path/to/my-config.ini`), `dhcli` reads and writes to that file.
2. **Current Working Directory (`./.dhcore.ini`)**: If `.dhcore.ini` exists in the current directory, it takes precedence over the home directory.
3. **User Home Directory (`~/.dhcore.ini`)**: Default fallback location used across all terminal sessions.

---

## 2. Registering & Switching Environments (`register`, `list-env`, `use`, `remove`)

### 2.1 Register a Platform Endpoint (`dhcli register`)
Fetches `.well-known/configuration` and `.well-known/openid-configuration` from the DigitalHub Core server and writes a named profile section to `.dhcore.ini`.

```bash
# Register with an explicit environment name (-e)
dhcli register -e prod https://core.digitalhub.example.com

# Overwrite an existing environment pointing to a different URL (--force / -f)
dhcli register -e dev -f http://localhost:8080
```

- If `-e` is omitted, the `dhcore_name` returned by the Core endpoint is used as the environment name.
- The first registered environment is automatically set as `current_environment`.

### 2.2 List, Switch, and Remove Environments
```bash
# List all registered environments in .dhcore.ini
dhcli list-env

# Set the active default environment
dhcli use prod

# Remove an environment section from .dhcore.ini
dhcli remove dev
```

---

## 3. Authentication & Token Lifecycle (`login`, `refresh`)

### 3.1 Interactive Browser Login (OAuth2 PKCE)
When a user is at a local workstation with a browser:
```bash
dhcli login
# Or target a specific environment:
dhcli login -e prod
```

### 3.2 Non-Interactive / Headless Login (`--pat` — Recommended for Agents & CI)
In headless containers, remote SSH sessions, or automated agent runs where a browser cannot open, authenticate using a **Personal Access Token (PAT)**:

```bash
# Option A: Pass token via --pat flag
dhcli login -e prod --pat "<your-personal-access-token>"

# Option B: Export environment variable (DHCORE_PERSONAL_ACCESS_TOKEN or DHCORE_PAT)
export DHCORE_PERSONAL_ACCESS_TOKEN="<your-personal-access-token>"
dhcli login -e prod
```

### 3.3 Refreshing Expired Tokens (`dhcli refresh`)
Access tokens and STS S3 credentials are short-lived (typically 1 to 24 hours). If a command fails with `401 Unauthorized` or expired token errors, refresh the session using the stored `refresh_token`:

```bash
dhcli refresh
```

---

## 4. Inspecting Configuration & Short-Lived Credentials (`config`, `credentials`)

To inspect the active environment's endpoints, API version, or temporary backing-service credentials (S3 MinIO STS keys, PostgreSQL DB password, Core Bearer token):

```bash
# Print non-secret platform configuration (DHCORE_ENDPOINT, S3_BUCKET, DHCORE_API_LEVEL, etc.)
dhcli config -o json

# Print active short-lived credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DHCORE_ACCESS_TOKEN, etc.)
dhcli credentials -o json
```

> **Security Rule for Agents**: Never print or log the raw output of `dhcli credentials` in user-visible chat messages unless explicitly requested by the user, as it contains live bearer and S3 tokens.

---

## 5. Bootstrapping a Python Workspace (`dhcli init`)

`dhcli init` creates (or activates) a local Python virtual environment (`venv` or `uv`) and installs the exact minor version of `digitalhub[full]` and `digitalhub-runtime-python` matching the connected Core server's `dhcore_version`:

```bash
# Create/update a virtual environment at ./.venv matching the active Core version
dhcli init ./.venv

# Include pre-release (beta/rc) Python SDK packages
dhcli init --pre ./.venv

# Also install version-pinned agent instructions and skills in the current workspace
dhcli init --agent ./.venv
```

With `--agent`, the CLI fetches `dhcore_version` from the active Core endpoint's
`/.well-known/configuration`. Both SDK packages and agent documentation use that release's
`major.minor` version. Agent instructions and skills are embedded from the CLI repository's
`templates/` folder, not downloaded from the docs repository. It installs `AGENTS.md`,
`CLAUDE.md` and `.agents/skills/` in the **current working directory**, not inside the venv.
For Core `0.16.2`, all `{{DOCS}}` placeholders become
`https://raw.githubusercontent.com/scc-digitalhub/docs/0.16`; the agent fetches knowledge
on demand from its `knowledge/` directory. Relative knowledge links resolve against the
page URL and stay on that branch. `CLAUDE.md` directs Claude to the installed `AGENTS.md`.
Initialization requires the live Core version, but does not contact GitHub.
Agents must report missing knowledge rather than fall back to another release.
Identical installed files are left unchanged on repeated initialization; conflicting files
and symlink destinations cause an error before installation. Move conflicting files aside
and reconcile customizations before reinitializing for a different Core version. Failed writes
roll back files and directories created by the installation. Cancelling package installation,
or a package-installation failure, installs no agent files. Without `--agent`, initialization
retains its existing Python-environment-only behavior.

> **Note for Automated Agents**: `dhcli init` prompts for `Y/n` confirmation before installing packages. Pipe `echo y | dhcli init ./.venv` if running non-interactively.
