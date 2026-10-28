# Authoring guide: DigitalHub agent knowledge base

This folder is the **versioned knowledge base** for AI agents (Claude Code, GitHub Copilot, Cursor, Codex,
Antigravity, the DigitalHub agent, and others). It lives on the docs branch of each platform release
(`0.15`, `0.16`, …). Agents fetch it remotely, pinned to that release, through the URLs that
`dhcli init --agent` writes into the user's `AGENTS.md` and skills. The router and skills are
maintained separately in the CLI repository's
[`templates/` folder](https://github.com/scc-digitalhub/digitalhub-cli/tree/main/templates)
and embedded in the CLI binary. They do not live in the docs repository.

> This file is for maintainers. Agents start at [`index.md`](index.md) or [`llms.txt`](llms.txt).

## Layout

| Folder | Purpose |
| :--- | :--- |
| `entities/` | **Core.** One page per entity (project, function, workflow, task, run, artifact, dataitem, model, secret, trigger). |
| `runtimes/` | **Core.** One page per runtime (python, container, dbt, hera, kfp, *serve, kubeai, …): kinds, tasks, manifests, run examples. |
| `cli/` | `dhcli` command reference, verified against the CLI source. |
| `sdk/` | Python SDK used **inside** handlers (data access, logging, pipelines DSL), plus the SDK fallback for things `dhcli` cannot do. |
| `management/` | Platform architecture, `store://` keys and versioning, Kubernetes resources, governance, and troubleshooting. |

## Page rules

1. **Front matter.** Every page starts with exactly two keys:
   ```yaml
   ---
   title: Python runtime
   description: One sentence that says what the page covers and when to read it.
   ---
   ```
   `scripts/generate_agent_knowledge.py` uses them to build `llms.txt`.
2. **One topic per page.** Aim for under about 300 curated lines. Put the action first, with copy-pasteable examples.
3. **Only verified commands.** Every `dhcli` invocation must exist in the CLI source (`digitalhub-cli/pkg/cmd`).
   Use placeholders `<project>`, `<name>`, `<id>`, `<run-id>`.
4. **CLI on the host, SDK in the container.** Host-side actions use `dhcli` and YAML. The Python SDK appears in handler code,
   and also in the documented fallback ([`sdk/sdk-fallback.md`](sdk/sdk-fallback.md)) for operations `dhcli` does not support.
5. **Generated blocks are read-only.** Text between `<!-- BEGIN GENERATED: … -->` and `<!-- END GENERATED: … -->` comes
   from the Core JSON Schemas. Write curated content above the block, then run:
   ```bash
   python scripts/generate_agent_knowledge.py --schemas ../digitalhub-core/schemas/specs
   ```
   CI can run it with `--check` to detect drift.
6. **Relative links only** between knowledge pages, so they resolve on any branch and from raw URLs.
   Resolve them against the fetched page URL, not the user's local workspace. Catalog `path` values
   are relative to `knowledge/` on the selected branch. Do not hard-code a release or link to `main`/`latest`.
7. **No template placeholders in knowledge links.** `{{DOCS}}` belongs only in the CLI's
   agent templates. `dhcli init --agent` replaces it with the GitHub raw repository
   root for the connected Core's `major.minor` branch (for example, `0.16.2` selects `0.16`).
   It unpacks the embedded router and skills locally; the agent fetches knowledge from that branch
   on demand, without falling back to another release. Knowledge pages are fetched as-is, so they must not use
   `{{DOCS}}` in link targets. If you need literal double braces (dbt, Jinja), fence them in code blocks.
8. **No secrets** in examples. Reference Kubernetes secrets by name and use `<token>` placeholders.

## Release checklist

1. Regenerate schema blocks against the Core tag of the release.
2. Re-verify the `dhcli` reference against the CLI tag of the release.
3. Commit on the release branch (`0.x`). The URL `https://raw.githubusercontent.com/scc-digitalhub/docs/<branch>/knowledge/` is then live.

## Testing version-pinned links

Run the documentation-only checks in this repository:

```bash
python3 -m unittest discover -s scripts -p 'test_agent_links.py'
python3 scripts/generate_agent_knowledge.py --check
```

The link tests check local knowledge targets, catalog coverage, and relative URL resolution
on multiple release branches without depending on a sibling CLI checkout. The generator check
requires the matching Core schemas and, for descriptions, the Console translations (see the
generation command above).

Run `go vet ./...` and `go build ./...` in the CLI repository before release. Separately verify
installation, local skill links, and version substitution in a temporary workspace.
No docs-side copies or bootstrap simulator are needed.
Before releasing, ensure every remote knowledge target in the CLI templates exists on the
supported docs release branch; publish knowledge before distributing the CLI release that
references it.
