#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
"""
Regenerate the schema-derived sections of the agent knowledge base.

The DigitalHub Core JSON Schemas (``digitalhub-core/schemas/specs``) are the
single source of truth for entity and runtime ``spec`` fields. This script
renders them into Markdown tables and injects them into the hand-written pages
under ``knowledge/entities`` and ``knowledge/runtimes``, between markers:

    <!-- BEGIN GENERATED: <block> -->
    ...
    <!-- END GENERATED: <block> -->

Everything outside the markers is curated by humans and never touched.
It also regenerates ``knowledge/llms.txt`` from page front matter.

Usage:
    python scripts/generate_agent_knowledge.py \
        --schemas ../digitalhub-core/schemas/specs \
        [--i18n ../digitalhub-console/src/i18n/en/fields.json] \
        [--check]

``--check`` exits with status 1 if any file would change (use it in CI).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"

# --------------------------------------------------------------------------- #
# Catalogue: which schemas feed which page.
# --------------------------------------------------------------------------- #

# Entity page -> schema folder (all kinds in the folder are rendered).
ENTITY_SCHEMAS = {
    "project": "project",
    "artifact": "artifact",
    "dataitem": "dataitem",
    "model": "model",
    "secret": "secret",
    "trigger": "trigger",
}

# Runtime page -> (entity type, [kinds]).
RUNTIMES = {
    "python": ("function", ["python"]),
    "container": ("function", ["container"]),
    "dbt": ("function", ["dbt"]),
    "hera": ("workflow", ["hera"]),
    "kfp": ("workflow", ["kfp"]),
    "sklearnserve": ("function", ["sklearnserve"]),
    "mlflowserve": ("function", ["mlflowserve"]),
    "huggingfaceserve": ("function", ["huggingfaceserve"]),
    "vllmserve": ("function", ["vllmserve-text", "vllmserve-speech", "vllmserve-pooling"]),
    "kubeai": ("function", ["kubeai-text", "kubeai-speech"]),
    "openinference": ("function", ["openinference"]),
    "guardrail": ("function", ["guardrail"]),
    "flower": ("function", ["flower-app", "flower-server", "flower-client"]),
}

# Fields injected automatically by `dhcli run` / Core: never written by hand.
RUN_MANAGED_FIELDS = {"task", "function", "workflow", "local_execution"}

MAX_DEPTH = 2


# --------------------------------------------------------------------------- #
# Schema rendering
# --------------------------------------------------------------------------- #


class Renderer:
    def __init__(self, i18n: dict | None):
        self.i18n = i18n or {}

    # -- descriptions ------------------------------------------------------- #
    def describe(self, prop: dict) -> str:
        title = prop.get("title", "")
        if not title.startswith("fields."):
            return ""
        parts = title[len("fields.") :].rsplit(".", 1)[0].split(".")
        for candidate in (parts, parts[-1:]):
            node = self.i18n
            for p in candidate:
                node = node.get(p) if isinstance(node, dict) else None
                if node is None:
                    break
            if isinstance(node, dict) and node.get("description"):
                return str(node["description"]).replace("|", "\\|").replace("\n", " ")
        return ""

    # -- types -------------------------------------------------------------- #
    @staticmethod
    def _ref_name(ref: str) -> str:
        return ref.split("/")[-1]

    def resolve(self, prop: dict, defs: dict) -> tuple[dict, str | None]:
        ref = prop.get("$ref")
        if ref:
            name = self._ref_name(ref)
            return defs.get(name, {}), name
        return prop, None

    def type_of(self, prop: dict, defs: dict) -> str:
        target, name = self.resolve(prop, defs)
        if "enum" in target:
            return "enum: " + ", ".join(f"`{v}`" for v in target["enum"])
        if name and name.startswith("Map_String."):
            inner = name[len("Map_String.") :].rstrip("_") or "any"
            return f"map<string, {inner.lower()}>"
        t = target.get("type")
        if t == "array":
            items = target.get("items", {})
            return f"array<{self.type_of(items, defs)}>"
        if t == "object" or (name and "properties" in target):
            return f"object ({name})" if name else "object"
        if t:
            return t
        if name:
            return name
        if "anyOf" in target or "oneOf" in target:
            return "any"
        return "any"

    def rows(self, schema: dict, defs: dict, prefix: str = "spec", depth: int = 0,
             skip: set[str] | None = None) -> list[str]:
        out: list[str] = []
        required = set(schema.get("required", []))
        props = dict(schema.get("properties", {}))
        for sub in schema.get("allOf", []):
            props.update(sub.get("properties", {}))
            required |= set(sub.get("required", []))
        for key in sorted(props):
            if skip and key in skip:
                continue
            prop = props[key]
            path = f"{prefix}.{key}"
            target, _ = self.resolve(prop, defs)
            default = prop.get("default", target.get("default"))
            notes = []
            if default not in (None, "", [], {}):
                notes.append(f"default `{json.dumps(default)}`")
            if "minLength" in prop:
                notes.append(f"minLength {prop['minLength']}")
            if prop.get("pattern"):
                notes.append(f"pattern `{prop['pattern']}`")
            desc = self.describe(prop)
            if desc:
                notes.insert(0, desc)
            out.append(
                f"| `{path}` | {self.type_of(prop, defs)} | {'**yes**' if key in required else ''} | {'; '.join(notes)} |"
            )
            if depth + 1 < MAX_DEPTH and "properties" in target and target.get("type", "object") == "object":
                out.extend(self.rows(target, defs, path, depth + 1))
        return out

    def table(self, schema: dict, skip: set[str] | None = None) -> str:
        defs = schema.get("$defs", {})
        body = self.rows(schema, defs, skip=skip)
        if not body:
            return "_No configurable fields._\n"
        head = "| Field | Type | Required | Notes |\n| :--- | :--- | :---: | :--- |\n"
        return head + "\n".join(body) + "\n"


# --------------------------------------------------------------------------- #
# Page assembly
# --------------------------------------------------------------------------- #

MARK = "<!-- {kind} GENERATED: {name} -->"


def inject(text: str, name: str, content: str) -> str:
    begin = MARK.format(kind="BEGIN", name=name)
    end = MARK.format(kind="END", name=name)
    block = (
        f"{begin}\n"
        "<!-- Do not edit: regenerate with scripts/generate_agent_knowledge.py -->\n\n"
        f"{content.rstrip()}\n\n{end}"
    )
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if pattern.search(text):
        return pattern.sub(lambda _: block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def tasks_for(schemas: Path, kind: str) -> list[str]:
    return sorted(
        p.stem for p in (schemas / "task").glob(f"{kind}+*.json")
        if p.stem.split("+", 1)[0] == kind
    )


def entity_block(r: Renderer, schemas: Path, folder: str) -> str:
    parts = []
    for f in sorted((schemas / folder).glob("*.json")):
        parts.append(f"### Kind `{f.stem}`\n\nSchema: `schemas/specs/{folder}/{f.name}`\n\n{r.table(load(f))}")
    return "## Spec reference (from Core JSON Schemas)\n\n" + "\n".join(parts)


def runtime_block(r: Renderer, schemas: Path, etype: str, kinds: list[str]) -> str:
    out = ["## Spec reference (from Core JSON Schemas)\n"]
    for kind in kinds:
        out.append(f"### {etype.capitalize()} kind `{kind}`\n")
        out.append(f"Schema: `schemas/specs/{etype}/{kind}.json`\n")
        out.append(r.table(load(schemas / etype / f"{kind}.json")))
        for task in tasks_for(schemas, kind):
            run_schema = schemas / "run" / f"{task}:run.json"
            if not run_schema.exists():
                continue
            out.append(f"#### Task `{task}` → run kind `{task}:run`\n")
            out.append(
                f"Fields accepted under `spec:` of a run manifest "
                f"(task-level and run-level). `task`, `{etype}` and `local_execution` are "
                "set automatically and are omitted.\n"
            )
            out.append(r.table(load(run_schema), skip=RUN_MANAGED_FIELDS))
    return "\n".join(out)


def runtime_matrix(schemas: Path) -> str:
    lines = [
        "| Runtime page | Entity | Kind | Tasks (`dhcli run <task>`) | Run kind(s) |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for page, (etype, kinds) in RUNTIMES.items():
        for kind in kinds:
            tasks = tasks_for(schemas, kind)
            lines.append(
                f"| [{page}]({page}.md) | {etype} | `{kind}` | "
                + ", ".join(f"`{t}`" for t in tasks)
                + " | "
                + ", ".join(f"`{t}:run`" for t in tasks)
                + " |"
            )
    return "\n".join(lines) + "\n"


def entity_kinds(schemas: Path) -> str:
    lines = ["| Entity | Kinds |", "| :--- | :--- |"]
    for folder in ("project", "artifact", "dataitem", "model", "function", "workflow", "secret", "trigger"):
        kinds = sorted(p.stem for p in (schemas / folder).glob("*.json"))
        lines.append(f"| [{folder}]({folder}.md) | " + ", ".join(f"`{k}`" for k in kinds) + " |")
    lines.append("| [run](run.md) | `<task>:run` — see [runtimes](../runtimes/index.md) |")
    lines.append("| [task](task.md) | `<function-kind>+<action>` — see [runtimes](../runtimes/index.md) |")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# llms.txt
# --------------------------------------------------------------------------- #

FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)
HEAD1 = re.compile(r"(?m)^#\s+(.+)$")

SECTIONS = [
    ("entities", "Entities (Core Domain)"),
    ("runtimes", "Runtimes (Execution Engines)"),
    ("cli", "CLI Reference (dhcli)"),
    ("sdk", "Python SDK (In-Container Handlers & Fallback)"),
    ("management", "Platform Architecture, Kubernetes & Troubleshooting"),
]


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONT.match(text)
    data = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" ") and not line.startswith("-"):
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip().strip('"')
    if "title" not in data:
        h = HEAD1.search(text)
        if h:
            data["title"] = h.group(1).strip()
    if "description" not in data and "summary" in data:
        data["description"] = data["summary"]
    return data


def llms_txt() -> str:
    out = [
        "# DigitalHub Platform — Agent Knowledge Base",
        "",
        "> Reference knowledge for AI agents operating the DigitalHub platform via the `dhcli` CLI.",
        "> Entities and runtimes are the core model; every page is plain Markdown, relative to this file.",
        "> Resolve links against this file's fetched URL, keeping the same docs branch selected from the Core major.minor version.",
        "> Resolve links inside each page against that page's URL; never fall back to main, latest, or another release.",
        "",
    ]
    for folder, title in SECTIONS:
        pages = sorted((KNOWLEDGE / folder).glob("*.md"), key=lambda p: (p.name != "index.md", p.name))
        if not pages:
            continue
        out.append(f"## {title}\n")
        for p in pages:
            fm = front_matter(p)
            out.append(f"- [{fm.get('title', p.stem)}]({folder}/{p.name}): {fm.get('description', '')}")
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schemas", type=Path, default=ROOT.parent / "digitalhub-core" / "schemas" / "specs")
    ap.add_argument("--i18n", type=Path, default=ROOT.parent / "digitalhub-console" / "src" / "i18n" / "en" / "fields.json")
    ap.add_argument("--check", action="store_true", help="fail if any file is out of date")
    args = ap.parse_args()

    if not args.schemas.is_dir():
        print(f"schemas folder not found: {args.schemas}", file=sys.stderr)
        return 2
    i18n = load(args.i18n) if args.i18n and args.i18n.exists() else None
    r = Renderer(i18n)

    updates: dict[Path, str] = {}

    def update(path: Path, name: str, content: str, title: str) -> None:
        current = updates.get(path)
        if current is None:
            current = path.read_text(encoding="utf-8") if path.exists() else (
                f"---\ntitle: {title}\ndescription: TODO\n---\n\n# {title}\n"
            )
        updates[path] = inject(current, name, content)

    for page, folder in ENTITY_SCHEMAS.items():
        update(KNOWLEDGE / "entities" / f"{page}.md", "spec-reference",
               entity_block(r, args.schemas, folder), page.capitalize())

    for page, (etype, kinds) in RUNTIMES.items():
        update(KNOWLEDGE / "runtimes" / f"{page}.md", "spec-reference",
               runtime_block(r, args.schemas, etype, kinds), f"{page} runtime")

    update(KNOWLEDGE / "runtimes" / "index.md", "runtime-matrix", runtime_matrix(args.schemas), "Runtimes")
    update(KNOWLEDGE / "entities" / "index.md", "entity-kinds", entity_kinds(args.schemas), "Entities")

    changed = []
    for path, text in updates.items():
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != text:
            changed.append(path)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")

    # llms.txt is computed after pages are written so front matter is current.
    llms_path = KNOWLEDGE / "llms.txt"
    llms = llms_txt()
    if not llms_path.exists() or llms_path.read_text(encoding="utf-8") != llms:
        changed.append(llms_path)
        if not args.check:
            llms_path.write_text(llms, encoding="utf-8")

    for p in changed:
        print(("out of date: " if args.check else "updated: ") + str(p.relative_to(ROOT)))
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
