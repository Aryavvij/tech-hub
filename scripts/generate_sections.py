#!/usr/bin/env python3
"""Regenerate sections/*.md from catalog.json — the human-browsable view of
the catalog. Run this any time catalog.json changes."""
import json, pathlib, re

OUT = pathlib.Path("/Users/aryavvij/Documents/Claude/techhub-repo")
SECTIONS_DIR = OUT / "sections"
SECTIONS_DIR.mkdir(exist_ok=True)

# order controls both filename and README nav order
SECTION_ORDER = [
    ("tools", "ai-tools", "AI Tools"),
    ("ide", "ides-dev", "IDEs & Dev"),
    ("extensions", "vscode-extensions", "VS Code Extensions"),
    ("claude", "claude-power", "Claude Power"),
    ("mcp", "mcp-servers", "MCP Servers"),
    ("claudeskills", "claude-skills", "Claude Skills"),
    ("projects", "projects", "Projects"),
    ("buildguides", "build-guides", "Build Guides"),
    ("jarvis", "jarvis-build", "Jarvis Build"),
    ("certs", "free-certs", "Free Certs"),
    ("prompts", "prompts", "Prompts"),
    ("links", "resources", "Resources"),
    ("vibe", "vibe-sites", "Vibe Sites"),
    ("stack", "full-stack", "Full Stack"),
]
RATING_ORDER = {"fire": 0, "good": 1, "maybe": 2, "skip": 3}
RATING_BADGE = {"fire": "🔥 MUST USE", "good": "✅ GOOD", "maybe": "🤔 MAYBE", "skip": "⛔ SKIP"}

def md_escape(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()

def main():
    catalog = json.loads((OUT / "catalog.json").read_text())
    by_section = {}
    for e in catalog:
        by_section.setdefault(e["section"], []).append(e)

    nav_lines = []
    for code, fname, label in SECTION_ORDER:
        entries = by_section.get(code, [])
        entries.sort(key=lambda e: (RATING_ORDER.get(e["rating"], 9), e["name"].lower()))
        count = len(entries)
        nav_lines.append(f"| [{label}](sections/{fname}.md) | {count} |")

        lines = [f"# {label}", "", f"[← back to index](../README.md)", "",
                 f"{count} resources.", ""]
        for e in entries:
            name = md_escape(e["name"])
            icon = e.get("icon", "")
            badge = RATING_BADGE.get(e["rating"], e["rating"])
            tags = ", ".join(e.get("tags", []))
            purpose = md_escape(e["purpose"])
            links = e.get("links") or []
            link_md = " · ".join(f"[{md_escape(l['label'])}]({l['url']})" for l in links) or "—"
            lines.append(f"## {icon} {name}".strip())
            lines.append(f"**{badge}**" + (f" · _{tags}_" if tags else ""))
            lines.append("")
            lines.append(purpose)
            lines.append("")
            if e.get("notes"):
                notes = e["notes"].strip()
                if notes:
                    lines.append("<details><summary>Details</summary>")
                    lines.append("")
                    lines.append(notes)
                    lines.append("")
                    lines.append("</details>")
                    lines.append("")
            lines.append(f"Links: {link_md}")
            lines.append("")
            lines.append("---")
            lines.append("")
        (SECTIONS_DIR / f"{fname}.md").write_text("\n".join(lines))

    print(f"generated {len(SECTION_ORDER)} section files, {len(catalog)} total entries")
    return nav_lines

if __name__ == "__main__":
    for l in main():
        print(l)
