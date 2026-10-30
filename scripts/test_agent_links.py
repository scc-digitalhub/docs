#!/usr/bin/env python3
"""Check release-specific knowledge navigation without network access or a CLI checkout."""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)\s]+)\)")


class AgentLinkTests(unittest.TestCase):
    def test_knowledge_navigation_keeps_selected_branch(self):
        sources = [*sorted((ROOT / "knowledge").rglob("*.md")), ROOT / "knowledge/llms.txt"]
        for branch in ("0.16", "0.17"):
            base = f"https://raw.githubusercontent.com/scc-digitalhub/docs/{branch}/"
            for source in sources:
                source_url = base + source.relative_to(ROOT).as_posix()
                for target in LINK.findall(source.read_text(encoding="utf-8")):
                    if target.startswith("/-/"):
                        continue  # Illustrative Console routes are not knowledge references.
                    if urlsplit(target).scheme:
                        self.assertFalse(target.startswith("https://raw.githubusercontent.com/scc-digitalhub/docs/"))
                        continue  # Maintainer links to other repositories are not knowledge references.
                    with self.subTest(branch=branch, source=source.relative_to(ROOT), target=target):
                        self.assertNotIn("{{DOCS}}", target)
                        self.assertNotIn("<%DOCS%>", target)
                        self.assertFalse(urlsplit(target).scheme, target)
                        resolved = urljoin(source_url, target)
                        self.assertTrue(resolved.startswith(base), resolved)
                        relative = unquote(urlsplit(resolved).path.removeprefix(f"/scc-digitalhub/docs/{branch}/"))
                        self.assertTrue((ROOT / relative).exists(), relative)

    def test_catalog_paths_are_relative_to_knowledge(self):
        catalog = (ROOT / "knowledge/index.md").read_text(encoding="utf-8")
        for relative in re.findall(r'^\s+path: "([^"]+)"', catalog, re.MULTILINE):
            with self.subTest(path=relative):
                self.assertFalse(relative.startswith(("/", "http", "{{", "<%")))
                self.assertTrue((ROOT / "knowledge" / relative).is_file())

    def test_llms_catalog_covers_knowledge_pages(self):
        catalog = (ROOT / "knowledge/llms.txt").read_text(encoding="utf-8")
        for source in sorted((ROOT / "knowledge").glob("*/*.md")):
            relative = source.relative_to(ROOT / "knowledge").as_posix()
            with self.subTest(page=relative):
                self.assertIn(f"]({relative})", catalog)


if __name__ == "__main__":
    unittest.main()
