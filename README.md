# tech-hub catalog

Machine-readable catalog of Aryav's tech-hub resources. Consumed by the `techhub`
Claude Code skill (`~/.claude/skills/techhub/`), which fetches this repo, detects the
active project's stack, and recommends the best-fit resources.

## Files (the contract the skill depends on)

| File | Purpose | Required |
|------|---------|----------|
| `catalog.json` | Source of truth. Array of resource entries (full detail). | ✅ yes |
| `index.json` | Compact rows derived from `catalog.json`. Optional fast-path. | optional |

The skill only *requires* `catalog.json`. Keep it at the repo root.

## `catalog.json` entry schema

```jsonc
{
  "id": "supabase-mcp",            // unique slug
  "name": "Supabase MCP",
  "icon": "🗄️",
  "section": "mcp",               // one of the section codes below
  "section_label": "MCP Servers",
  "rating": "fire",               // fire | good | maybe | skip  (skip = excluded from recs)
  "rating_label": "MUST USE",
  "tags": ["Database", "SQL"],
  "keywords": ["database", "supabase", "sql", "..."],  // used for stack matching
  "purpose": "One-liner shown on the card.",
  "notes": "Long-form markdown-ish detail.",
  "links": [{ "label": "docs", "url": "https://..." }]
}
```

**Section codes:** `tools`, `ide`, `extensions`, `claude`, `mcp`, `claudeskills`,
`projects`, `jarvis`, `certs`, `links`, `vibe`, `stack`.

## How matching works

The skill scores each entry against the project's detected stack (from `package.json`,
`requirements.txt`, framework config, file extensions, etc.):

- Overlap between the entry's `keywords`/`tags`/`section` and the detected stack drives the score.
- `rating` is a quality prior (`fire` > `good` > `maybe`; `skip` is excluded).
- The optional `--query` (user intent) adds targeted weight.

So the two fields that most affect recommendation quality are **`keywords`** and **`rating`**.
When you add resources, give them accurate keywords and an honest rating.

## Adding / editing resources

- Edit `catalog.json` directly, **or** re-generate from `tech-hub.html` with the extractor
  (`extract_catalog.py`) if you keep the HTML as the source.
- Commit + push. The skill git-pulls on next use (local cache), so changes propagate automatically.

## Wiring the skill to this repo

After pushing, set `repo_url` in `~/.claude/skills/techhub/config.json` to this repo's URL.
Until then the skill reads `catalog.json` from its local fallback path.
