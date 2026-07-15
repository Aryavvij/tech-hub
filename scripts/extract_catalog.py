#!/usr/bin/env python3
"""Extract all cards from tech-hub.html into catalog.json + index.json.

catalog.json = full data (source of truth pushed to the repo).
index.json   = compact rows the skill loads for fast matching.
"""
import re, json, html, sys, pathlib

SRC = sys.argv[1] if len(sys.argv) > 1 else "/Users/aryavvij/Documents/Claude/tech-hub.html"
OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "/Users/aryavvij/Documents/Claude/techhub-repo")
OUT.mkdir(parents=True, exist_ok=True)

raw = pathlib.Path(SRC).read_text(encoding="utf-8", errors="replace")

# Human-readable labels for the section codes used in data-section.
SECTION_LABEL = {
    "tools": "AI Tools", "ide": "IDEs & Dev", "extensions": "VS Code",
    "claude": "Claude Power", "mcp": "MCP Servers", "claudeskills": "Claude Skills",
    "projects": "Projects", "buildguides": "Build Guides", "jarvis": "Jarvis Build",
    "certs": "Free Certs", "prompts": "Prompts", "links": "Resources",
    "vibe": "Vibe Sites", "stack": "Full Stack",
}
RATING_LABEL = {"fire": "MUST USE", "good": "GOOD", "maybe": "MAYBE", "skip": "SKIP"}

STOPWORDS = set("""the and for you your with any all can that this from into out use uses used
using give gives given get gets best good great fast easy just like more most much very when
what how who why into out its their has have had are was were will would should could into
one two three each every other than then them they need needs want wants make makes made
run runs ran open opens set sets add adds via per not but our own way ways lets let via
claude""".split())

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "item"

def strip_html_to_text(frag):
    frag = re.sub(r"<h4>(.*?)</h4>", r"\n#### \1\n", frag, flags=re.S | re.I)
    frag = re.sub(r"<strong>(.*?)</strong>", r"**\1**", frag, flags=re.S | re.I)
    frag = re.sub(r"<em>(.*?)</em>", r"*\1*", frag, flags=re.S | re.I)
    frag = re.sub(r"<li>(.*?)</li>", r"\n- \1", frag, flags=re.S | re.I)
    frag = re.sub(r"<br\s*/?>", "\n", frag, flags=re.I)
    frag = re.sub(r"<[^>]+>", " ", frag)            # drop any remaining tags
    frag = html.unescape(frag)
    frag = re.sub(r"[ \t]+", " ", frag)
    frag = re.sub(r"\n\s*\n\s*\n+", "\n\n", frag)
    return frag.strip()

def first(pat, chunk, flags=re.S):
    m = re.search(pat, chunk, flags)
    return m.group(1).strip() if m else ""

# Split into per-card chunks. Each chunk runs from one card-open to the next.
parts = re.split(r'(?=<div class="card" )', raw)
chunks = [p for p in parts if p.startswith('<div class="card" ')]

catalog, index = [], []
seen_ids = {}
for c in chunks:
    rating = first(r'data-rating="([^"]+)"', c)
    section = first(r'data-section="([^"]+)"', c)
    icon = first(r'class="card-icon">(.*?)</span>', c)
    name = strip_html_to_text(first(r'class="card-name">(.*?)</div>', c))
    tag = strip_html_to_text(first(r'class="card-tag">(.*?)</div>', c))
    purpose = strip_html_to_text(first(r'class="card-purpose">(.*?)</div>\s*<div class="card-notes"', c) or
                                 first(r'class="card-purpose">(.*?)</div>', c))
    notes_raw = first(r'<div class="card-notes">(.*?)</div>\s*<div class="card-(?:links|expand-hint)"', c)
    notes = strip_html_to_text(notes_raw)
    links = [{"label": strip_html_to_text(lbl), "url": url}
             for url, lbl in re.findall(r'<a class="link-chip" href="([^"]+)"[^>]*>(.*?)</a>', c, re.S)]

    if not name:
        continue
    cid = slug(name)
    if cid in seen_ids:
        seen_ids[cid] += 1
        cid = f"{cid}-{seen_ids[cid]}"
    else:
        seen_ids[cid] = 1

    tag_parts = [t.strip() for t in re.split(r"[·|,/]", tag) if t.strip()]
    kw = set()
    for src in [name, tag, purpose]:
        for tok in re.findall(r"[a-zA-Z0-9\.\+#-]{3,}", src.lower()):
            kw.add(tok.strip(".-"))
    kw = {k for k in kw if k and k not in STOPWORDS}
    keywords = sorted(kw)

    entry = {
        "id": cid, "name": name, "icon": icon,
        "section": section, "section_label": SECTION_LABEL.get(section, section),
        "rating": rating, "rating_label": RATING_LABEL.get(rating, rating.upper()),
        "tags": tag_parts, "keywords": keywords,
        "purpose": purpose, "notes": notes, "links": links,
    }
    catalog.append(entry)
    index.append({
        "id": cid, "name": name, "section": section, "rating": rating,
        "tags": tag_parts, "keywords": keywords, "purpose": purpose,
    })

(OUT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
(OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False))

# quick report
from collections import Counter
by_sec = Counter(e["section"] for e in catalog)
by_rat = Counter(e["rating"] for e in catalog)
print(f"cards extracted: {len(catalog)}")
print("by section:", dict(by_sec))
print("by rating :", dict(by_rat))
print("no purpose:", sum(1 for e in catalog if not e["purpose"]))
print("no links  :", sum(1 for e in catalog if not e["links"]))
print("catalog.json bytes:", (OUT / "catalog.json").stat().st_size)
print("index.json bytes  :", (OUT / "index.json").stat().st_size)
