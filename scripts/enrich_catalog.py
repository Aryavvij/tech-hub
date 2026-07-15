#!/usr/bin/env python3
"""Enrich catalog.json:
  1. Fold in the 24 `wide-card` prompt/guide entries from tech-hub.html.
  2. Add the new external resources (repos/skills/guides Aryav sent).
  3. Dedupe by id, regenerate catalog.json + index.json.
Safe to re-run (idempotent by id: new/updated entries replace old ones).
"""
import re, json, html, pathlib
from collections import Counter

SRC = pathlib.Path("/Users/aryavvij/Documents/Claude/tech-hub.html")
OUT = pathlib.Path("/Users/aryavvij/Documents/Claude/techhub-repo")
RATING_LABEL = {"fire": "MUST USE", "good": "GOOD", "maybe": "MAYBE", "skip": "SKIP"}
SECTION_LABEL = {"prompts": "Prompts", "buildguides": "Build Guides",
                 "claudeskills": "Claude Skills", "vibe": "Vibe Sites",
                 "projects": "Projects", "claude": "Claude Power", "links": "Resources",
                 "tools": "AI Tools"}
STOP = set("""the and for you your with any all can that this from into out use uses used using
give gives given get gets best good great fast easy just like more most much very when what how
who why its their has have had are was were will would should could one two three each every
other than then them they need needs want wants make makes made run runs open set add via per
not but our own way ways lets let claude""".split())

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "item"

def clean(frag):
    frag = re.sub(r"<h4>(.*?)</h4>", r"\n#### \1\n", frag, flags=re.S | re.I)
    frag = re.sub(r"<strong>(.*?)</strong>", r"**\1**", frag, flags=re.S | re.I)
    frag = re.sub(r"<br\s*/?>", "\n", frag, flags=re.I)
    frag = re.sub(r"<[^>]+>", " ", frag)
    frag = html.unescape(frag)
    frag = re.sub(r"[ \t]+", " ", frag)
    frag = re.sub(r"\n\s*\n\s*\n+", "\n\n", frag)
    return frag.strip()

def kw(*srcs):
    s = set()
    for src in srcs:
        for t in re.findall(r"[a-zA-Z0-9\.\+#-]{3,}", (src or "").lower()):
            t = t.strip(".-")
            if t and t not in STOP:
                s.add(t)
    return sorted(s)

def entry(cid, name, section, rating, tags, purpose, notes, links, icon="", extra_kw=None):
    kws = kw(name, " ".join(tags), purpose)
    if extra_kw:
        kws = sorted(set(kws) | set(extra_kw))
    return {"id": cid, "name": name, "icon": icon, "section": section,
            "section_label": SECTION_LABEL.get(section, section.title()),
            "rating": rating, "rating_label": RATING_LABEL[rating],
            "tags": tags, "keywords": kws, "purpose": purpose, "notes": notes, "links": links}

# ── 1. wide-cards → prompt entries ───────────────────────────────────────────
def extract_widecards():
    raw = SRC.read_text(encoding="utf-8", errors="replace")
    parts = re.split(r'(?=<div class="wide-card")', raw)
    blocks = [p for p in parts if p.startswith('<div class="wide-card"')]
    out = []
    for b in blocks:
        m = re.search(r"<h3>(.*?)</h3>", b, re.S)
        if not m:
            continue
        title_raw = clean(m.group(1))
        em = re.match(r"^([^\w\s]+)\s*(.*)$", title_raw)
        icon, name = (em.group(1), em.group(2).strip()) if em else ("", title_raw)
        desc = ""
        pm = re.search(r"</h3>\s*<p>(.*?)</p>", b, re.S)
        if pm:
            desc = clean(pm.group(1))
        pairs = re.findall(
            r'<div class="prompt-label">(.*?)</div>\s*<div class="prompt-box">(.*?)</div>',
            b, re.S)
        notes_parts = []
        for lbl, box in pairs:
            notes_parts.append(f"#### {clean(lbl)}\n{clean(box)}")
        notes = "\n\n".join(notes_parts)
        sec_m = re.search(r'data-section="([a-z]+)"', b)
        section = sec_m.group(1) if sec_m else "prompts"
        out.append(entry(slug(name) or slug(title_raw), name or title_raw, section,
                         "good", ["prompt template"], desc, notes, [], icon=icon))
    return out

# ── 2. new external resources ────────────────────────────────────────────────
# rating: fire/good/maybe. Purposes prefixed [NEEDS-VERIFY] were inferred without
# a successful fetch — correct on the GitHub-API pass.
NEW = [
    entry("ai-website-cloner-template", "AI Website Cloner Template", "vibe", "good",
          ["Next.js", "Website Cloning", "AI Agents"],
          "Reusable template that uses AI coding agents to reverse-engineer any website into a clean Next.js codebase — inspects design, extracts assets, rebuilds components.",
          "Point an AI agent at a URL; it rebuilds the site as modern Next.js + Tailwind + TypeScript. Good starting point for clone-then-customize builds.",
          [{"label": "GitHub", "url": "https://github.com/JCodesMore/ai-website-cloner-template"}],
          icon="🧬", extra_kw=["reverse-engineering", "scraping", "tailwind", "typescript", "react", "template"]),
    entry("fable-skills", "Fable Skills (oliwoodman)", "claudeskills", "good",
          ["Claude Skills", "Fable 5", "Workflows"],
          "Five reusable Claude skill files capturing how Fable 5 approached common dev tasks (security review, project setup, build planning, debugging) before its retirement from standard plans.",
          "Install manually into ~/.claude/skills/. Useful as reproducible method templates for security-review, project-setup, build-planning, bug-debugging workflows.",
          [{"label": "GitHub", "url": "https://github.com/oliwoodman/fable-skills"}],
          icon="📘", extra_kw=["security-review", "project-setup", "debugging", "handover"]),
    entry("humanizer", "Humanizer (blader)", "claudeskills", "fire",
          ["Writing", "AI-Detection", "Voice Match"],
          "Free open-source Claude skill (28k+ stars) that checks writing against 33 documented AI tells (from Wikipedia's 'Signs of AI Writing') and rewrites it to sound human. Two-pass audit + voice-match mode.",
          "#### Install\nnpx skills add blader/humanizer  (run from home dir to make it global)\n\n#### Use\n\"Humanize this: [draft]\" or \"Run the humanizer on draft.md\". For voice-match, paste 2-3 samples of your own writing. Flags em-dash overuse, 'it's not just X it's Y', rule-of-three, AI vocab (delve/tapestry/underscore), copula avoidance, promotional filler, and ~27 more. Make it the last step before shipping copy.",
          [{"label": "GitHub", "url": "https://github.com/blader/humanizer"}],
          icon="🧹", extra_kw=["copywriting", "editing", "content", "email", "marketing", "npx", "skill"]),
    entry("claude-seo", "Claude SEO (AgricIDaniel)", "claudeskills", "good",
          ["SEO", "Content", "Marketing"],
          "[NEEDS-VERIFY] Claude skill/toolkit for SEO work — keyword research, content optimization, and on-page recommendations. (Description inferred; repo metadata fetch was blocked.)",
          "Verify README on the GitHub-API pass. Likely covers SEO content generation and optimization workflows via Claude.",
          [{"label": "GitHub", "url": "https://github.com/AgricIDaniel/claude-seo"}],
          icon="🔎", extra_kw=["seo", "content", "keywords", "ranking", "optimization", "marketing"]),
    entry("ruflo", "ruFlo (ruvnet)", "claude", "good",
          ["Agents", "Orchestration", "Workflow"],
          "[NEEDS-VERIFY] Agentic workflow/orchestration project from ruvnet (author of claude-flow / ruv-swarm) — likely multi-agent coordination and flow automation. (Inferred; verify README.)",
          "Verify on the GitHub-API pass. ruvnet's tooling generally centers on multi-agent swarms and automated engineering flows.",
          [{"label": "GitHub", "url": "https://github.com/ruvnet/ruflo"}],
          icon="🌊", extra_kw=["agents", "multi-agent", "swarm", "orchestration", "automation", "ai-engineering"]),
    entry("3d-portfolio", "3D Portfolio (akashrmalhotra)", "projects", "good",
          ["Three.js", "Portfolio", "WebGL"],
          "[NEEDS-VERIFY] Template/starter for a 3D animated developer portfolio site, likely React + Three.js. (Inferred; verify README.)",
          "Verify on the GitHub-API pass. Good reference build for an interactive 3D portfolio.",
          [{"label": "GitHub", "url": "https://github.com/akashrmalhotra/3d-portfolio"}],
          icon="🧊", extra_kw=["three.js", "webgl", "react", "3d", "portfolio", "template", "frontend", "animation"]),
    entry("ponytail", "ponytail (DietrichGebert)", "links", "maybe",
          ["Unverified"],
          "[NEEDS-VERIFY] Purpose unknown — GitHub metadata fetch was blocked and the repo name is not self-describing. Categorize after reading the README.",
          "Fetch README on the GitHub-API pass and re-file into the right section with real keywords.",
          [{"label": "GitHub", "url": "https://github.com/DietrichGebert/ponytail"}],
          icon="❓"),
    entry("second-brain-claude-obsidian", "Second Brain — Claude + Obsidian", "buildguides", "good",
          ["Obsidian", "Knowledge Management", "Prompt"],
          "Guide + prompt to build a personal second brain: Claude interviews you and writes a folder of linked markdown notes (projects, people, ideas, journal) that Obsidian shows as a living graph. Fully local, no code.",
          "#### Setup\nClaude desktop app + Obsidian (both free). Paste the build prompt; Claude asks up to 5 questions then creates a 'Second Brain' folder with Home/Projects/People/Ideas/Journal, all linked. Open folder as vault in Obsidian → graph view.\n\n#### Upkeep habits\nCapture to Inbox, one journal line/day, make a note for anything mentioned twice. Weekly: let Claude file the inbox and summarize the week.",
          [{"label": "Guide", "url": "https://www.fionntobin.com/downloads/second-brain-claude-obsidian.md"}],
          icon="🧠", extra_kw=["obsidian", "second-brain", "pkm", "notes", "markdown", "journaling", "knowledge-graph"]),
    entry("brand-guidelines-to-skill", "Brand Guidelines → Claude Skill", "buildguides", "good",
          ["Branding", "Design System", "Claude Skill"],
          "[NEEDS-VERIFY] Guide on turning brand guidelines into a reusable Claude skill / design spec so outputs stay on-brand. (Inferred from title; verify article.)",
          "Verify article content. Pairs well with awesome-design-md and skillui for brand-consistent generation.",
          [{"label": "Article", "url": "https://nelsonxlee.substack.com/p/turn-your-brand-guidelines-into-a"}],
          icon="🎨", extra_kw=["branding", "brand-guidelines", "design-system", "style", "skill"]),
]

def main():
    catalog = json.loads((OUT / "catalog.json").read_text())
    by_id = {e["id"]: e for e in catalog}
    before = len(by_id)

    added_wide = 0
    for e in extract_widecards():
        if e["id"] not in by_id:
            added_wide += 1
        by_id[e["id"]] = e
    added_new = 0
    for e in NEW:
        if e["id"] not in by_id:
            added_new += 1
        by_id[e["id"]] = e

    catalog = list(by_id.values())
    (OUT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
    index = [{"id": e["id"], "name": e["name"], "section": e["section"],
              "rating": e["rating"], "tags": e["tags"], "keywords": e["keywords"],
              "purpose": e["purpose"]} for e in catalog]
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False))

    print(f"before: {before}  +wide: {added_wide}  +new: {added_new}  total: {len(catalog)}")
    print("sections:", dict(Counter(e["section"] for e in catalog)))
    print("NEEDS-VERIFY:", [e["id"] for e in catalog if "[NEEDS-VERIFY]" in e["purpose"]])

if __name__ == "__main__":
    main()
