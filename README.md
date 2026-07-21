# tech-hub

Aryav's curated catalog of AI/dev resources — tools, MCP servers, Claude skills, IDEs, build guides, project ideas, certs, and prompts. 226 entries, each rated 🔥 MUST USE / ✅ GOOD / 🤔 MAYBE.

This repo is consumed by the [`techhub`](https://github.com/Aryavvij/tech-hub) Claude Code skill, which detects the stack of whatever project you're in and recommends the best-fit resources from here. See [How the skill uses this repo](#how-the-skill-uses-this-repo) below.

## Browse by category

| Section | Count |
|---|---|
| [AI Tools](sections/ai-tools.md) | 14 |
| [IDEs & Dev](sections/ides-dev.md) | 10 |
| [VS Code Extensions](sections/vscode-extensions.md) | 12 |
| [Claude Power](sections/claude-power.md) | 9 |
| [MCP Servers](sections/mcp-servers.md) | 14 |
| [Claude Skills](sections/claude-skills.md) | 63 |
| [Projects](sections/projects.md) | 23 |
| [Build Guides](sections/build-guides.md) | 2 |
| [Jarvis Build](sections/jarvis-build.md) | 13 |
| [Free Certs](sections/free-certs.md) | 12 |
| [Prompts](sections/prompts.md) | 22 |
| [Resources](sections/resources.md) | 15 |
| [Vibe Sites](sections/vibe-sites.md) | 11 |
| [Full Stack](sections/full-stack.md) | 6 |

**By rating:** 84 🔥 MUST USE · 135 ✅ GOOD · 7 🤔 MAYBE

Each section page lists every entry with its rating, tags, one-line purpose, expandable details, and links.

## Repo layout

```
tech-hub/
├── README.md          ← you are here
├── catalog.json        ← source of truth. Every entry, full detail. Skill reads this.
├── index.json           ← compact derivative of catalog.json (id/name/section/rating/tags/keywords/purpose only)
├── sections/             ← human-browsable markdown, one file per category (generated from catalog.json)
└── scripts/
    ├── extract_catalog.py    ← parses tech-hub.html card divs → catalog.json (re-run if the HTML source changes)
    ├── enrich_catalog.py      ← folds in prompt/guide "wide-card" entries + hand-added external resources
    └── generate_sections.py   ← regenerates sections/*.md from catalog.json (run after any catalog.json edit)
```

**`catalog.json` and `index.json` stay at the repo root** — the `techhub` skill's sync logic expects them there. Don't move them into a subfolder without also updating `~/.claude/skills/techhub/techhub.py`.

## `catalog.json` entry schema

```jsonc
{
  "id": "supabase-mcp",             // unique slug
  "name": "Supabase MCP",
  "icon": "🗄️",
  "section": "mcp",                // section code — see table below
  "section_label": "MCP Servers",
  "rating": "fire",                // fire | good | maybe | skip  (skip = excluded from skill recommendations)
  "rating_label": "MUST USE",
  "tags": ["Database", "SQL"],
  "keywords": ["database", "supabase", "sql", "..."],  // drives stack-matching in the skill
  "purpose": "One-liner.",
  "notes": "Long-form detail (markdown-ish).",
  "links": [{ "label": "docs", "url": "https://..." }]
}
```

**Section codes:** `tools`, `ide`, `extensions`, `claude`, `mcp`, `claudeskills`, `projects`, `buildguides`, `jarvis`, `certs`, `prompts`, `links`, `vibe`, `stack`.

The two fields that most affect recommendation quality are **`keywords`** and **`rating`** — be accurate and honest when adding entries.

## Adding a resource

1. Add an entry to `catalog.json` by hand (follow the schema above), **or** if you've added a card to `tech-hub.html`, re-run `python3 scripts/extract_catalog.py` to regenerate from source.
2. Build `keywords` with a real tokenizer, not ad hoc string splitting — reuse the `kw()` helper pattern in `scripts/enrich_catalog.py` (regex-tokenize + strip a stopword list). A naive splitter lets stopwords/punctuation leak in and pollutes matching.
3. Regenerate the browsable pages: `python3 scripts/generate_sections.py`.
4. Commit and push. The `techhub` skill git-pulls this repo on next use — no other wiring needed.

## How the skill uses this repo

`~/.claude/skills/techhub/techhub.py`:
1. Git-clones/pulls this repo into a local cache (`~/.claude/skills/techhub/cache/`).
2. Reads `catalog.json` and detects the active project's stack from its manifest files (`package.json`, `requirements.txt`, framework configs, file extensions).
3. Scores every entry by keyword/tag overlap with the detected stack + an honest-rating prior + any explicit query terms.
4. Returns a ranked shortlist for Claude to apply judgment to and present.

Trigger it in any project with `/techhub` or "what should I use for this project."
