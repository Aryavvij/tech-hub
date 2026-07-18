# Claude Skills

[← back to index](../README.md)

36 resources.

## 🏗️ /architect — System Design Mode
**🔥 MUST USE** · _Architecture, System Design, Decisions_

Activates systems architect mode. Claude designs before building: components, data flow, key decisions with rationale, failure modes, scale considerations. Use for any non-trivial system.

<details><summary>Details</summary>

#### Activation

 /architect [what you're building] — describe the system goal and constraints. Include: expected scale (users, requests), team size, timeline, existing stack if relevant.
 
#### What architect mode produces

 Component breakdown (what exists and why), data model sketch (key entities and relationships), API design outline, technology choices with explicit rationale ("we use Supabase here because X, not Y because Y would require Z"), identified failure modes, what breaks at 10x scale.
 
#### The "simplest that works" rule

 /architect is explicitly instructed to avoid over-engineering. Claude will propose the simplest architecture that meets your requirements, then tell you what you'd change at 10x scale. You decide when to invest in that complexity.
 
#### Best use pattern

 /architect first → review the plan → ask "what's the riskiest assumption in this architecture?" → Claude identifies it → validate that assumption before building. Prevents building on a wrong foundation.
 
#### Output use

 Copy the architecture output into your project's CLAUDE.md under an "Architecture" section. Future sessions can reference it, preventing Claude from suggesting designs that conflict with your established architecture.

</details>

Links: —

---

## 🔥 /critique — Unsparing Review
**🔥 MUST USE** · _Analysis, Quality, Direct Feedback_

Activates brutal honesty mode. Claude finds what's weak, confusing, or missing — with specific fixes, no padding. Use on: landing pages, essays, pitch decks, code, product ideas.

<details><summary>Details</summary>

#### Activation

 /critique [thing] — paste your content immediately after. Works on: writing, UI screenshots (describe it), code, business ideas, plans.
 
#### What changes vs default Claude

 Default Claude softens criticism and leads with positives. /critique disables the softening. You get: "The third paragraph is incoherent — it makes two contradictory claims. The call-to-action is buried and uses weak language. The pricing section assumes the reader already understands your product." Specific. Actionable. No filler.
 
#### Best use cases

 Landing page copy before you show it to anyone. Portfolio before submitting to jobs. Business idea before spending time on it. Code before a PR review where reputation matters. Essay before submission.
 
#### Combining with other modes

 /critique + LEAN ENGINE = the most efficient feedback loop. Dense, specific issues only, no prose explanation of what's correct. If you want the reasoning: remove LEAN ENGINE from the session.
 
#### What to do with the output

 Don't defend immediately. Read the whole critique. Mark each issue: fix now, fix later, disagree (and why). Fix the "fix now" items. Re-run /critique on the revised version. Usually 2-3 rounds produces a significantly better result.

</details>

Links: —

---

## 💡 /prompting — Smart Prompt Suggester
**🔥 MUST USE** · _Prompts, Proactive_

Proactive prompt suggester — watches the conversation and offers to apply the right prompt from the prompt library. Triggers on /prompting, 'suggest a prompt', or proactively mid-conversation when a better prompt exists.

<details><summary>Details</summary>

Watches for triggers (session start/end, code review, architecture decisions, verbosity) and surfaces the matching prompt from the library, one at a time.

</details>

Links: —

---

## 🔬 /research-assistant — Deep Dive & Writing Partner
**🔥 MUST USE** · _Academic Writing, Peer Review, Socratic Method, Token-Efficient_

Deep-dive research and academic writing partner — Socratic questioning on logic gaps, draft compilation with citation-safety, and blind peer review. Runs inline (no multi-agent orchestration) for token efficiency.

<details><summary>Details</summary>

#### Core Mandate
Never hallucinate evidence — unsourced claims get tagged `[CITE: ...]` instead of invented. Academic voice, no AI-tell words. Runs a Three-Way Scan on any review: WHY (problem defended?), HOW (methodology sound?), WHAT (findings tied to data?).

#### /dive-deep [section/argument]
Socratic mentor mode — asks exactly 3 targeted questions to find logic gaps before any drafting happens. Writes no prose.

#### /compile-draft [notes/outline/data]
Turns raw notes into formal academic prose with an evidence hook on every major claim. Clean Markdown by default.

#### /devil-advocate [draft/section]
Hostile peer review structured under WHY/HOW/WHAT. For long drafts or explicit 'blind review' requests, offers a single isolated Agent call so the critique isn't softened by the drafting conversation's rapport.

#### Design note
Built as one file, not a multi-agent pipeline, specifically to control token cost. Inspired by (not copied from) imbad0202/academic-research-skills (13/12/7/10-agent version, CC-BY-NC) and Weizhena/Deep-Research-skills (two-phase outline-then-investigation pattern).

</details>

Links: [inspired by: academic-research-skills](https://github.com/imbad0202/academic-research-skills) · [inspired by: Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills)

---

## 🔍 /security-audit — Vulnerability Scan
**🔥 MUST USE** · _Security, Auth, Injection, CVE_

Full security review mode. Claude looks for: XSS, SQL injection, SSRF, auth gaps, exposed secrets, missing validation. Categorizes by severity. Essential before any public launch.

<details><summary>Details</summary>

#### Activation

 /security-audit [paste code] — paste the specific files or functions you want audited. More targeted = more useful output. "Audit my entire codebase" is too broad — "audit my auth middleware and API routes" is actionable.
 
#### What it looks for

 **Critical**: SQL injection, command injection, authentication bypass, exposed private keys or tokens in code. **High**: XSS (cross-site scripting), SSRF (server-side request forgery), insecure direct object references (can user A access user B's data?). **Medium**: Missing input validation, weak session management, information disclosure in error messages. **Low**: Missing security headers, overly permissive CORS, verbose error messages in production.
 
#### RLS specifically

 Always run /security-audit on your Supabase RLS policies. The most common mistake: "I thought users could only see their own data but the RLS policy has a gap when the user_id column is null." Claude catches these pattern-level issues.
 
#### Before launch checklist use

 Run /security-audit on: all auth-related code, all API routes that handle user data, all database query code, any code that makes external HTTP requests. Not on: pure UI components, utility functions, test files.
 
#### Caveat

 Claude finds code-level security issues well. It cannot: run dynamic analysis (actually try attacks), test your production environment, find issues in dependencies (use npm audit for that). Complement with: OWASP ZAP (free) for dynamic testing.

</details>

Links: —

---

## ⚡ /speed-build — Ship Fast
**🔥 MUST USE** · _Build, No Questions, Fastest Path_

Build it now. No clarifying questions, no option lists, no confirming. Claude makes the obvious choices and produces complete, runnable code immediately. For when you want velocity over perfect alignment.

<details><summary>Details</summary>

#### Activation

 /speed-build [feature description] — be specific enough that Claude can make sensible choices. "A user profile page" is fine. "Build me something" is too vague.
 
#### What Claude does

 Picks the most obvious tech choices for your stack (inferred from CLAUDE.md or previous context), builds a complete working implementation, skips any explanation of what it's doing, delivers code ready to paste.
 
#### When to use vs pair-program

 /speed-build: you trust the obvious implementation and want it fast. /pair-program: the problem is complex enough that the obvious implementation might be wrong and you want to think through it.
 
#### Iteration pattern

 Run /speed-build → get first version → review it → give specific feedback: "change the button color to red, add a loading state, and use the Card component instead of a plain div" → Claude patches the specific issues. Much faster than upfront specification.
 
#### Caution

 Don't use for: security-sensitive code (auth, payments, data access — these need careful review), complex business logic with many edge cases, anything touching production data. Use for: UI components, utility functions, scaffolding, prototypes.

</details>

Links: —

---

## 🧭 /techhub — Resource Recommender
**🔥 MUST USE** · _Meta, Recommender, This Catalog_

Recommends the best-fit resources from this catalog (tools, MCP servers, Claude skills, IDEs, build guides, projects, certs) for the active project. Detects project stack, ranks by fit + rating.

<details><summary>Details</summary>

The skill that consumes this very repo. Syncs via git pull into a local cache, detects the active project's stack from manifests/deps/extensions, scores catalog entries, prints a ranked shortlist. Source: ~/.claude/skills/techhub/.

</details>

Links: —

---

## 🧪 /test-cases — Complete Test Suite Gen
**🔥 MUST USE** · _Testing, Edge Cases, TDD_

Generates a complete test suite — happy path, edge cases, error cases, boundary conditions, and things you forgot to think about. Uses Vitest/Jest syntax. TDD accelerator.

<details><summary>Details</summary>

#### Activation

 /test-cases [paste function or describe feature] . Works on: individual functions (paste the code), API endpoints (describe behavior), React components (describe user interactions), entire features (describe the spec).
 
#### What it generates

 Happy path test (normal usage, expected output). Boundary condition tests (empty arrays, zero values, max values, single items). Error cases (invalid input, network failure, missing required fields). Edge cases specific to the function logic (things you didn't think to test). Async behavior (loading states, error states, race conditions for async functions).
 
#### Framework output

 Default: Vitest syntax (works with React + Next.js projects). Specify if different: "Use Jest with React Testing Library" or "Use Pytest" for Python. The output is runnable — paste into your test file.
 
#### TDD workflow

 /test-cases before writing implementation → review and add any missed cases → implement until all tests pass. This forces you to think about behavior before coding, which almost always produces a cleaner API design.
 
#### Coverage insight

 After generating: ask "what would I need to mock to make these tests fast and deterministic?" Claude identifies external dependencies (DB, APIs, file system) and suggests mock strategies.

</details>

Links: —

---

## 🌟 Awesome DESIGN.md
**🔥 MUST USE** · _94.9k ⭐, 73+ Brand Design Systems_

94.9k⭐ GitHub. A collection of 73+ DESIGN.md files for major tech brands. Drop any file in your project and Claude generates UI that matches that brand's exact aesthetic — Apple, Notion, Linear, Stripe, Vercel, etc.

<details><summary>Details</summary>

#### What's in each DESIGN.md

 Each file contains: color palette (exact hex values), typography (font families, weights, sizes, line heights), spacing system, border radiuses, shadow styles, animation principles, component patterns, tone of voice. Enough for Claude to reproduce the brand's complete visual language.
 
#### How to use

 1. git clone github.com/voltagent/awesome-design-md . 2. Copy the DESIGN.md for the aesthetic you want into your project root (or reference it). 3. Tell Claude: "Follow the design system in DESIGN.md when generating components." 4. Every component Claude writes inherits that brand's aesthetic.
 
#### Best DESIGN.md files in the collection

 **Linear.md**: Compact, dark, sharp typography — perfect for developer tools. **Notion.md**: Clean, document-first, generous whitespace. **Stripe.md**: Financial trustworthiness, blue gradients, precise. **Vercel.md**: Dark, minimal, technical elegance. **Apple.md**: Premium, spacious, SF Pro typography. **Figma.md**: Purple accents, modern gradients.
 
#### Creating your own

 Use SkillUI ( npx skillui [url] ) to auto-generate a DESIGN.md from any website's CSS. Point it at a site you love → get a DESIGN.md you can use immediately.
 
#### Project strategy

 Don't mix design systems. Pick one DESIGN.md per project and stick with it. Mixing Linear.md with Apple.md produces inconsistent UI. Consistency wins.

</details>

Links: [awesome-design-md](https://github.com/voltagent/awesome-design-md)

---

## 🔎 Claude SEO (AgricIDaniel)
**🔥 MUST USE** · _SEO, Claude Code Skill, 25 sub-skills_

Universal SEO skill for Claude Code — 25 sub-skills + 18 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, semantic clustering, e-commerce/international SEO, Google APIs, PDF/Excel reporting.

<details><summary>Details</summary>

11,300+ stars. Optional DataForSEO, Firecrawl, and Banana extensions for live data. Python. Install via the repo's setup instructions into ~/.claude/skills/.

</details>

Links: [GitHub](https://github.com/AgricIDaniel/claude-seo)

---

## 🧹 Humanizer (blader)
**🔥 MUST USE** · _Writing, AI-Detection, Voice Match_

Free open-source Claude skill (28k+ stars) that checks writing against 33 documented AI tells (from Wikipedia's 'Signs of AI Writing') and rewrites it to sound human. Two-pass audit + voice-match mode.

<details><summary>Details</summary>

#### Install
npx skills add blader/humanizer  (run from home dir to make it global)

#### Use
"Humanize this: [draft]" or "Run the humanizer on draft.md". For voice-match, paste 2-3 samples of your own writing. Flags em-dash overuse, 'it's not just X it's Y', rule-of-three, AI vocab (delve/tapestry/underscore), copula avoidance, promotional filler, and ~27 more. Make it the last step before shipping copy.

</details>

Links: [GitHub](https://github.com/blader/humanizer)

---

## 🎯 Impeccable
**🔥 MUST USE** · _43.6k ⭐, 23 Commands, Anti-Pattern Detector_

43.6k⭐ GitHub. 23 design commands + 45 anti-pattern detection rules for Claude Code. Catches: inconsistent spacing, low-contrast text, accessibility violations, visual clutter. Makes AI-generated UI professional-grade.

<details><summary>Details</summary>

#### Install

 npx impeccable install — installs the skill directly into your Claude Code setup. Or: npx impeccable install --project to scope to one project.
 
#### The 23 commands

 /design:audit — full design audit of current code. /design:fix-spacing — normalize all spacing to 4px grid. /design:typography — enforce type scale. /design:contrast — fix all contrast issues. /design:accessibility — WCAG compliance check. /design:motion — add/fix animations. /design:mobile — optimize for mobile. /design:dark-mode — add dark mode. /design:polish — overall quality pass. 14 more specialized commands.
 
#### The 45 anti-pattern rules

 Patterns Impeccable detects and corrects: "4px border-radius on a component with 16px radius siblings" (inconsistency), "text under 4.5:1 contrast ratio on backgrounds" (accessibility), "padding inconsistent with the established spacing scale" (system violation), "font size below 14px for body text" (readability), "z-index above 100 without isolation" (stacking context smell). 40 more like these.
 
#### Typical workflow

 Build UI with Lovable/V0/Cursor → run /design:audit → Impeccable finds 10-15 issues → run /design:fix-spacing + /design:contrast → run /design:polish → professional result. Takes 5 minutes vs hours of manual fixes.
 
#### Why 43.6k stars

 It solves the #1 problem with AI-generated UI: it looks close but not quite right. Impeccable finds the "not quite right" and fixes it systematically.

</details>

Links: [impeccable](https://github.com/ImeccableAI/impeccable)

---

## 📦 kepano/obsidian-skills
**🔥 MUST USE** · _Official, 5 Skills, Obsidian Markdown, CLI, Bases_

Official Obsidian agent skills by Kepano (Obsidian creator). 5 skills that teach Claude Code everything about Obsidian: markdown syntax, CLI commands, Bases (database views), JSON Canvas, and web extraction via Defuddle.

<details><summary>Details</summary>

#### Install

 npx skills add https://github.com/kepano/obsidian-skills or manually copy to /.claude/skills/ in your vault root.
 
#### 5 skills breakdown

 **obsidian-markdown** — Obsidian-flavored markdown: wikilinks ([[note]]), embeds (![[note]]), callouts (> [!NOTE]), properties (YAML frontmatter). Claude stops generating standard markdown when working in Obsidian. **obsidian-bases** — Create .base files (database-style views with filters, formulas, summaries). **json-canvas** — Create visual .canvas files with nodes, edges, groups. **obsidian-cli** — Control Obsidian via CLI (1.12+): open notes, run commands, manage plugins. **defuddle** — Extract clean markdown from any web URL, removing clutter to save tokens.
 
#### Why these matter

 Without these skills, Claude generates standard markdown that displays incorrectly in Obsidian (no wikilinks, no callouts, no properties). With the obsidian-markdown skill, every note Claude creates is natively Obsidian-compatible.
 
#### Combine with obsidian-mind

 obsidian-mind pre-installs these 5 skills in its .claude/skills/ folder. If you're using obsidian-mind, you already have these. Install them standalone if you're using Obsidian without the full obsidian-mind system.
 
#### Defuddle specifically

 npm install -g defuddle then use in Claude: "Extract clean content from [URL] using defuddle." Gets the article without nav, ads, sidebars. Token-efficient for research workflows.

</details>

Links: [GitHub](https://github.com/kepano/obsidian-skills) · [Spec](https://agentskills.io/specification)

---

## ⚖️ LLM Council Skill
**🔥 MUST USE** · _5 Advisors, Peer Review, Final Verdict, Karpathy Method_

Turns one question into five independent expert opinions + peer review + a chairman's verdict. Based on Karpathy's LLM Council methodology. For decisions where you need more than one perspective.

<details><summary>Details</summary>

#### Install

 Tell Claude in any chat: "Please install this Claude skill for me. The SKILL.md file lives at: https://github.com/aiwithremy/claude-skills-llm-council." Claude fetches and installs automatically.
 
#### Trigger phrases

 "council this," "run the council on [question]," "pressure-test this," "stress-test this," "war room this." Claude spins up 5 advisors, runs peer review, delivers chairman's verdict.
 
#### Why it works

 One AI gives one answer — which might be great or mediocre, and you can't tell. The council runs your question through 5 independent advisors, each from a fundamentally different angle. They review each other's work. The chairman synthesizes: where they agree, where they clash, what you should actually do. You see the full reasoning landscape, not just one path.
 
#### Best council questions

 "Should I launch a $97 workshop or a $497 course?" "Which of these 3 positioning angles is strongest?" "I'm thinking of pivoting from X to Y — am I crazy?" "Here's my landing page copy — what's weak?" "Should I hire a VA or build automation first?" Basically: any decision where the cost of a bad call is high and multiple perspectives matter.
 
#### What makes a bad council question

 Factual questions ("What's the capital of France?"), creation tasks ("Write me a tweet"), processing tasks ("Summarize this article"). The council shines on judgment calls, not lookups or generation. It will tell you things you don't want to hear — that's the point.
 
#### Credit

 Built by Ole Lehmann (@itsolelehmann). Methodology from Andrej Karpathy's LLM Council.

</details>

Links: [GitHub](https://github.com/aiwithremy/claude-skills-llm-council) · [Karpathy Original](https://github.com/karpathy/llm-council)

---

## 🧠 Obsidian Mind
**🔥 MUST USE** · _Persistent Memory, 18 Commands, 9 Subagents, QMD Search_

Gives Claude Code a persistent brain via your Obsidian vault. Hooks fire on every session start — Claude reads your North Star, active projects, open tasks, and recent changes before you type a word.

<details><summary>Details</summary>

#### Install

 npm install -g shardmind then shardmind install github:breferrari/obsidian-mind . Or: git clone https://github.com/breferrari/obsidian-mind.git . Open the folder as an Obsidian vault + run Claude Code from that directory.
 
#### How it works

 5 lifecycle hooks: SessionStart (injects context), UserPromptSubmit (classifies each message), PostToolUse (validates markdown writes), PreCompact (backs up transcript), Stop (end-of-session checklist). You just talk — hooks handle routing.
 
#### 18 built-in commands

 /om-standup — morning kickoff with full context. /om-dump — freeform brain dump, routes everything. /om-wrap-up — session close, verify notes + catch wins. /om-weekly — cross-session synthesis. /om-incident-capture — turns Slack threads into incident reports. /om-review-brief — generates a full performance review document from your vault evidence.
 
#### QMD semantic search

 Install npm install -g @tobilu/qmd for semantic retrieval. Claude finds "what we decided about caching" even when the note is titled "Redis Migration ADR." Registered as MCP server — appears as native tools alongside Read/Edit.
 
#### Token efficiency

 Does NOT dump your full vault into context. SessionStart injects ~2K tokens (excerpts + filenames + git summary). Notes are fetched on-demand semantically. Classification hook: ~100 tokens per message. You pay only for what's relevant.
 
#### 9 subagents

 brag-spotter, context-loader, cross-linker, people-profiler, review-prep, slack-archaeologist, vault-librarian, review-fact-checker, vault-migrator. Heavy operations run in isolated context windows — your main conversation stays clean.
 
#### Works with

 Claude Code (full support), Codex CLI, Gemini CLI, OpenCode. All hooks are platform-agnostic TypeScript.

</details>

Links: [GitHub](https://github.com/breferrari/obsidian-mind) · [ShardMind](https://github.com/breferrari/shardmind)

---

## 🔄 Obsidian Second Brain
**🔥 MUST USE** · _33 Commands, Auto-Synthesis, X, Web, YouTube Research, Self-Updating Vault_

Your vault rewrites itself. Extends Karpathy's LLM Wiki pattern: new sources update existing pages instead of appending new ones. 33 commands, 4 scheduled agents, live research from X + web + YouTube. The vault gets smarter while you sleep.

<details><summary>Details</summary>

#### Install

 curl -fsSL https://raw.githubusercontent.com/eugeniughelbur/obsidian-second-brain/main/scripts/quick-install.sh | bash . Then /obsidian-init to set up vault structure.
 
#### How it extends Karpathy's LLM Wiki

 Karpathy's pattern: drop sources → LLM creates wiki pages → ask questions. This goes further: new sources *rewrite existing pages* with updated context. Contradictions reconcile automatically. Patterns get synthesized into connection pages. One URL in → 5-15 vault pages updated.
 
#### Research toolkit (killer feature)

 /x-read [url] — Grok with live X access: verbatim post + thread + TL;DR + reply sentiment. ~$0.05/call. /x-pulse [topic] — scan X for what's trending: themes, gaps, hooks, post ideas. ~$0.13/call. /research [topic] — Perplexity dossier with citations and recency markers. ~$0.04/call. /research-deep [topic] — vault-first: scans what you already know, fills only gaps. ~$0.40/call. /youtube [url] — transcript + summary + quotes saved to vault.
 
#### 33 commands include

 /obsidian-save (capture everything from convo), /obsidian-ingest (URL/PDF/audio/screenshot → rewrite vault), /obsidian-challenge (vault argues against you using your own history), /obsidian-emerge (surfaces patterns from 30 days of notes), /obsidian-connect A B (bridges unrelated domains), /obsidian-graduate (turns idea fragment into full project), /obsidian-visualize (canvas map of your entire knowledge graph).
 
#### 4 scheduled agents

 Morning (8AM) — daily note + tasks. Nightly (10PM) — close day + reconcile contradictions + synthesize + heal orphans. Weekly (Friday 6PM) — review. Sunday — vault health audit. You wake up to a smarter vault.
 
#### 4 presets

 executive (OKRs), builder (sprints), creator (drafts → published), researcher (reading → synthesized). Pick at bootstrap.
 
#### API keys needed for research

 xAI (Grok), Perplexity, Google Gemini (for /notebooklm), YouTube Data API (optional). Without keys, the 27 core vault commands still work fully.

</details>

Links: [GitHub](https://github.com/eugeniughelbur/obsidian-second-brain) · [Blog](https://theaioperator.io)

---

## 🐴 ponytail (DietrichGebert)
**🔥 MUST USE** · _Claude Code Plugin, YAGNI, Code Minimalism_

Makes your AI coding agent think like a lazy senior dev — pushes back against over-engineering. "The best code is the code you never wrote."

<details><summary>Details</summary>

82,900+ stars. JavaScript. A Claude Code plugin (also works as cursor-rules) enforcing YAGNI: simpler diffs, fewer abstractions, less code shipped for the same requirement.

</details>

Links: [GitHub](https://github.com/DietrichGebert/ponytail)

---

## 🔧 SkillUI / npx skillui
**🔥 MUST USE** · _Design Extraction, DESIGN.md Generator_

CLI that reverse-engineers any website's design system into a DESIGN.md file. Point at any URL → get a complete design system description Claude can use. Turn any website's aesthetic into a Claude skill.

<details><summary>Details</summary>

#### How it works

 SkillUI fetches the CSS and DOM structure of a website, analyzes: font families, color values, spacing scales, border radiuses, shadow values, animation timings. It synthesizes these into a structured DESIGN.md following the standard format Claude understands.
 
#### Usage

 npx skillui https://linear.app → outputs Linear's DESIGN.md. npx skillui https://stripe.com --output stripe-design.md → saves to file. Or: npx amaancoderx/npxskillui [url] (the community version with additional features).
 
#### What it extracts

 Primary/secondary/tertiary colors, background and surface colors, heading and body fonts with weights and sizes, spacing scale (4/8/16/24/32px patterns), component patterns (border-radius values, shadow styles), animation durations (transition timing functions).
 
#### Quality varies by site

 Works best on: sites with CSS custom properties (variables), design-system-based codebases, shadcn/ui-based sites. Less accurate for: sites using CSS-in-JS with hashed class names, old jQuery sites, heavily image-based designs.
 
#### Workflow

 Find a site with the aesthetic you want → npx skillui [url] → add to project → "Follow DESIGN.md" in Claude. Complete aesthetic capture in under a minute.
 
#### Combining with taste-skill

 SkillUI gives you the what (specific values). Taste-skill gives you the how (design philosophy). Together: DESIGN.md from SkillUI defines the system, taste-skill defines the judgment within that system.

</details>

Links: [npxskillui](https://github.com/amaancoderx/npxskillui)

---

## 🎨 Taste-Skill — Anti-Slop Framework
**🔥 MUST USE** · _17.5k ⭐, 9 Skills, Design Quality_

17.5k⭐ GitHub. A suite of 9 Claude Code skills that prevent generic AI-generated UI. Enforces aesthetic taste through tunable dials, typography rules, spacing systems, and color theory built into the model's instructions.

<details><summary>Details</summary>

#### What taste-skill actually does

 AI-generated UIs suffer from "slop": generic cards, safe color choices, predictable layouts, no visual hierarchy. Taste-skill injects a design philosophy into Claude's instructions that pushes toward: intentional typography, meaningful whitespace, purposeful color, surprising but coherent layouts.
 
#### The 9 skills

 **Core skills**: taste-ui (general UI), taste-landing (landing pages), taste-dashboard (data UIs), taste-mobile (mobile layouts). **Component skills**: taste-typography (type system), taste-color (color theory), taste-motion (animation philosophy), taste-layout (grid + spacing). **Image gen**: taste-image-gen (prompts for AI image generation with taste). Plus 3 image generation skills for creating visual assets.
 
#### Tunable dials

 Each skill has dials you set: BOLDNESS (conservative → avant-garde), DENSITY (minimal → information-rich), COLOR_TEMPERATURE (warm → cool), FORMALITY (playful → corporate). Set these for each project to tune the aesthetic output.
 
#### Install and use

 git clone github.com/leonxlnx/taste-skill . Install skills to Claude Code. In any session: "Using the taste-ui skill, design this component. Boldness: 7/10, Density: low, Color: cool." The skill reshapes how Claude approaches every design decision.
 
#### What changes with taste-skill

 Without: button with rounded corners, blue, generic. With: button that fits the visual hierarchy, typography-driven, spacing that breathes, color that means something. The diff is visible immediately in AI-generated UIs.
 
#### Combining with awesome-design-md

 taste-skill (design philosophy) + awesome-design-md/Linear.md (Linear's specific design system) = AI that designs with Linear's aesthetic and taste. Powerful combination for matching specific brand aesthetics.

</details>

Links: [taste-skill](https://github.com/leonxlnx/taste-skill)

---

## 🏆 UI UX Pro Max Skill
**🔥 MUST USE** · _161 Reasoning Rules, 67 UI Styles, BM25_

A massive Claude skill containing 161 UI/UX reasoning rules, 67 named UI styles (glassmorphism, brutalism, etc.), 161 color palettes with hex values, and a BM25 ranking engine to match your prompt to the best style.

<details><summary>Details</summary>

#### What's inside

 **161 reasoning rules**: Design principles Claude must apply when generating UI. "Visual hierarchy must be established before color." "Interactive elements need clear affordances." "Whitespace is not empty space — it creates rhythm." **67 UI styles**: Named styles Claude understands: glassmorphism, neumorphism, brutalism, flat design, material design, skeuomorphism, Swiss/International, Bauhaus, etc. Each with defining characteristics. **161 color palettes**: Named palettes (Midnight Ocean, Autumn Fire, Forest Calm, etc.) with exact hex codes for primary/secondary/accent/background/text. **BM25 Ranking Engine**: Matches your natural language prompt to the closest matching style and palette using keyword scoring.
 
#### How the BM25 engine works

 You say: "I want a dark, moody design for a music app." → BM25 scores your description against all 67 styles and 161 palettes → returns: "Best style match: Neo-Brutalism (score: 0.87). Best palette match: Midnight Noir (score: 0.91)." Claude then applies those specific rules.
 
#### Install and use

 git clone github.com/nextlevelbuilder/ui-ux-pro-max-skill . Install to Claude Code. Activate: "Using the UI UX Pro Max skill, design [component]. My vision: [description]." The BM25 engine handles style matching automatically.
 
#### Workflow impact

 Without this skill: Claude guesses what "modern" or "clean" means. With this skill: Claude applies 161 specific rules from a named design tradition. The precision of output is dramatically higher.
 
#### Combining skills

 UI UX Pro Max (reasoning + style rules) + taste-skill (tunable dials) + DESIGN.md (specific brand values) = the most opinionated, consistent AI design output possible.

</details>

Links: [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

---

## 🧠 Wiki-Brain Skill
**🔥 MUST USE** · _Obsidian, AI Memory, Knowledge Graph_

Claude Code skill that turns Obsidian into a compound AI memory system. Claude indexes your vault, maintains a BRAIN.md knowledge graph, and recalls relevant notes in any conversation. Persistent AI memory.

<details><summary>Details</summary>

#### Setup process

 1. Install Wiki-Brain skill to Claude Code. 2. Open Claude Code in your Obsidian vault directory. 3. Run: "Initialize Wiki-Brain. Index all notes in this vault and create BRAIN.md." 4. Claude reads all files, identifies key concepts and connections, creates the index. 5. Takes 5-15 minutes depending on vault size.
 
#### BRAIN.md structure

 # BRAIN.md — Knowledge Index

## Key Concepts
- [[LangGraph]]: Multi-agent framework (see: agents.md, langraph-tutorial.md)
- [[Supabase]]: PostgreSQL-based backend (see: db-patterns.md)
- [[GSAP]]: Animation library (see: animation-notes.md)

## Recent Additions
- 2025-06-15: Added notes on MCP server configuration
- 2025-06-10: Research on RAG architectures

## Cross-Links
- LangGraph ↔ Headroom: Both handle agent orchestration 
 
#### Daily usage

 "Before answering, check BRAIN.md for anything I've written about [topic]." Claude reads the index → fetches relevant notes → incorporates your prior research. You stop re-learning things you've already documented.
 
#### The compound effect

 Every new note you add gets indexed. Every Claude conversation that touches your notes adds connections. After 6 months: Claude understands your entire knowledge base and can surface connections you forgot you made.
 
#### What makes this different from Obsidian AI plugins

 Wiki-Brain integrates with your coding workflow — the same Claude Code instance that writes your code also has access to your notes. Ask "What did I write about authentication flows?" while building an auth feature.

</details>

Links: —

---

## 🎻 /fablepro — Fable 5 Orchestrator Mode
**✅ GOOD** · _Fable 5, Multi-Agent, Cost Optimization_

Optimised operating mode for Claude Fable 5. Sets Fable as pure orchestrator — planning, decomposition, review — routing all implementation to cheaper Sonnet/Haiku subagents. Trigger: /fablepro, long-context builds, multi-agent orchestration.

<details><summary>Details</summary>

Pairs with model-router for cost-aware multi-agent builds using Fable 5.

</details>

Links: —

---

## ⚡ /lean-engine — Token Efficiency Protocol
**✅ GOOD** · _Verbosity, Efficiency_

Activates LEAN ENGINE token efficiency protocol — cuts verbosity, removes preamble, forces direct answers and complete code. Trigger: /lean-engine, 'stop being verbose', 'cut the fluff'.

<details><summary>Details</summary>

Use when responses are running long or the task just needs fast, dense output.

</details>

Links: —

---

## 🧮 /model-router — Model Selection Advisor
**✅ GOOD** · _Cost, Model Selection_

Tells you exactly which model (Opus/Fable 5, Sonnet, Haiku) to use for any task to minimise cost without sacrificing quality. Trigger: /model-router or when starting a task and wanting to route it optimally.

<details><summary>Details</summary>

Useful before kicking off a large or multi-agent task to avoid overpaying for model tier.

</details>

Links: —

---

## ⚡ /performance-audit — Speed Analysis
**✅ GOOD** · _Performance, N+1, Re-renders, Caching_

Performance review mode: N+1 queries, unnecessary re-renders, missing caching, expensive loops, sync-when-should-be-async. Estimated impact per issue. For when the app is slow and you don't know why.

<details><summary>Details</summary>

#### Activation

 /performance-audit [paste code] . Works best on: React components you suspect are re-rendering too much, API routes with DB queries, data processing functions.
 
#### What it finds in React

 Components missing memo/useMemo/useCallback where expensive. State updates that trigger full re-renders instead of targeted updates. useEffect dependencies that cause unnecessary re-runs. Prop drilling that forces unrelated components to re-render. Missing virtualization on long lists (should use react-virtual for >100 items).
 
#### What it finds in DB queries

 N+1: "You're calling the DB once per item in a loop — use a single IN query." Missing SELECT specificity: "SELECT * on a table with 50 columns when you only need 3 — waste." Missing indexes: "You're filtering on user_id but I don't see an index — table scans on every query." Synchronous operations that should be parallel (Promise.all instead of sequential awaits).
 
#### Estimated impact

 Each issue comes with an estimated performance impact: "This N+1 adds ~200ms per user on a 100-item list" vs "This missing memo saves ~2ms per render." Prioritize by impact, not by what's easiest to fix.
 
#### Measurement first

 Before /performance-audit: measure what's actually slow. Chrome DevTools Performance tab, Lighthouse, database EXPLAIN queries. Fix what the measurements show is slow, not what seems like it should be slow. Premature optimization is still the root of all evil.

</details>

Links: —

---

## 📋 /pr-description — Perfect PR Copy
**✅ GOOD** · _Git, PR, Documentation_

Generates a professional PR description from your diff or change summary. What changed + why + what to test + deployment notes. Makes your PRs look like a senior engineer wrote them.

<details><summary>Details</summary>

#### Activation

 /pr-description [paste diff or describe changes] . Best input: actual git diff ( git diff main ). Also works with: a list of what you changed, a summary of the feature, a commit message.
 
#### Output structure

 **Summary** (1-2 sentences): what changed and why — the "why" is most important, the diff shows the "what." **Changes**: bullet list of specific changes, grouped logically. **Testing**: what to test and how — specific steps, not "tested locally." **Screenshots**: placeholder if UI changed (you add screenshots). **Deployment notes**: DB migrations, env var changes, feature flags, anything needed beyond normal deploy. **Related**: issue/ticket links if relevant.
 
#### The "why" focus

 Most PR descriptions say "Added X feature." Good PR descriptions say "Added X feature to reduce support tickets about Y — users previously had to contact support to do Z, which can now be done in settings." The diff shows the code; the PR description gives the context reviewers need.
 
#### Commit message companion

 Run /commit-msg for the individual commit message and /pr-description for the full PR. They serve different audiences: commit messages are for git log, PR descriptions are for reviewers.

</details>

Links: —

---

## 🎯 /pre-mortem — Failure Analysis
**✅ GOOD** · _Planning, Risk, Decision Quality_

Imagine 6 months in the future — the project failed. What went wrong? Pre-mortem forces you to surface risks before they happen, when you can still prevent them.

<details><summary>Details</summary>

#### Activation

 /pre-mortem [project/plan/decision] — describe what you're planning in detail. The more specific the input, the more specific the failure modes.
 
#### What it does that forward planning doesn't

 Forward planning: "Here's how we'll succeed." Pre-mortem: "Here's how we failed, specifically." The mental shift from "planning success" to "explaining failure" bypasses optimism bias. You suddenly find it easy to say "we assumed users would want feature X but they didn't" — something you wouldn't say during normal planning.
 
#### Output structure

 5-10 specific failure modes, ranked by likelihood × severity. Each one: what happened, why we didn't prevent it, what the early warning sign was that we ignored. Ends with: the top 3 preventable risks and specific actions to mitigate each.
 
#### How to use the output

 For each "early warning sign we ignored": make it a metric you track from day 1. For each "specific action to mitigate": put it in your project plan. You've now pre-committed to preventing the most likely failures.
 
#### Combine with /stress-test

 /pre-mortem → big picture failures. /stress-test → specific plan weaknesses. Run both before committing to any significant decision.

</details>

Links: —

---

## 🔄 /refactor — Code Cleanup Mode
**✅ GOOD** · _Refactor, Readability, Simplify_

Targeted refactor mode. Priority order: readability → simplicity → performance. Shows before/after with only non-obvious changes explained. For code that works but is painful to read.

<details><summary>Details</summary>

#### Activation

 /refactor [paste code] . Optionally add: "prioritize: [readability/performance/type safety]" to shift emphasis. Default priority: readability → simplicity → performance.
 
#### What it changes (and what it doesn't)

 **Will change**: Variable names (clearer), function decomposition (too-long functions split), early returns (remove nested conditionals), consistent patterns (pick one way to do X and use it everywhere), TypeScript types (add missing, fix incorrect). **Won't change**: Architecture (that's /architect), logic (that would break behavior), external interfaces (other code depends on these).
 
#### Output format

 Full refactored file + a brief note for each non-obvious change (obvious changes like renaming get no explanation). You see the complete new version, not a diff — easier to review holistically.
 
#### Incremental refactor

 For large files: "Refactor just the auth-related functions in this file, leave everything else unchanged." Targeted refactoring is safer and easier to review than whole-file refactors.
 
#### Post-refactor check

 Always: run your tests after refactoring (if you have them). If behavior changed: Claude made an error. If tests pass: safe to commit. This is why /test-cases + /refactor is a powerful pair.

</details>

Links: —

---

## 🐥 /rubber-duck — Thinking Partner Mode
**✅ GOOD** · _Problem Solving, Unstuck, Debug Thinking_

Claude asks, you answer. The rubber duck debugging technique at scale — but Claude asks probing questions that expose gaps in your reasoning. For when you need to think, not just get an answer.

<details><summary>Details</summary>

#### Activation

 /rubber-duck [topic] — then explain your thinking. Claude will NOT solve the problem. It asks questions. You answer. After 5-10 exchanges, you usually have the answer yourself.
 
#### Why this works

 The act of explaining a problem often reveals the solution. The classic rubber duck debug technique: explaining code to a rubber duck causes you to see the bug. /rubber-duck does this with an AI that asks follow-up questions when your explanation reveals a gap.
 
#### Question types Claude uses

 Clarifying: "What specifically do you mean by X?" Assumption: "You said X — what evidence do you have for that?" Gap-finding: "You went from A to C without explaining B." Inversion: "You're focused on how to do X — have you considered whether X is the right thing to do?" These questions are probes, not answers.
 
#### When it's most valuable

 Stuck on a bug you've been debugging for 2+ hours. Can't decide between two architectural approaches. Writing code for a spec you don't fully understand. Planning something complex and feeling vague about it. The moment of highest value: when you say "Oh wait — I just realized..." in the middle of explaining.
 
#### Mode switch

 If after 10 exchanges you still don't have an answer: "Switch out of rubber duck mode and tell me what you think." Claude reveals its analysis of what you've said. Often the answer was in the questions it was asking.

</details>

Links: —

---

## 🔀 9router — Multi-Agent Router
**✅ GOOD** · _Agent Routing, Task Distribution_

A Claude Code skill implementing 9-way agent routing. Routes tasks to specialized Claude agents based on intent classification. Efficient for complex multi-domain tasks.

<details><summary>Details</summary>

#### What 9router does

 When you give Claude a complex task, 9router classifies it into one of 9 domains: code, research, design, analysis, writing, planning, debugging, review, or general. Then routes to the specialized agent prompt optimized for that domain. One entry point → right specialist every time.
 
#### The 9 agents

 **CODE_AGENT**: Focused on implementation, follows CLAUDE.md strictly. **RESEARCH_AGENT**: Sources, citations, web search focused. **DESIGN_AGENT**: UI/UX, uses DESIGN.md context. **ANALYSIS_AGENT**: Data, reasoning, conclusions. **WRITING_AGENT**: Content, tone, audience awareness. **PLAN_AGENT**: Architecture, roadmaps, prioritization. **DEBUG_AGENT**: Error diagnosis, stack trace reading, systematic isolation. **REVIEW_AGENT**: Code review, quality assessment, security. **GENERAL**: Everything else.
 
#### Usage

 Install to Claude Code. Works transparently — just describe your task and 9router automatically routes it. Or explicitly: "@code: implement the user authentication flow" to force a specific agent.
 
#### Source

 GitHub: decolua/9router. Install as a Claude Code skill.
 
#### When it's most valuable

 Long sessions where you switch between different types of tasks. Without routing: Claude's system prompt stays the same whether you're debugging or designing. With 9router: each task type gets expert-level instructions optimized for it.

</details>

Links: [9router](https://github.com/decolua/9router)

---

## 🌐 Agent-Browser Skill
**✅ GOOD** · _Autonomous Web Agent, Research Loops_

Claude Code skill that gives Claude structured browser access for research tasks. Implements search → read → synthesize loops. Claude researches topics autonomously and returns sourced summaries.

<details><summary>Details</summary>

#### What it enables

 Without agent-browser: Claude can only use information from its training data. With agent-browser: Claude searches the web, reads pages, extracts information, and synthesizes across multiple sources — all in one agentic loop.
 
#### Research workflow

 "Research the current state of AI coding assistants. Find: market leaders, pricing, key differentiators, recent developments. Create a comparison table." Claude: searches → reads top 10 results → extracts relevant info from each → synthesizes into your requested format. Real research, not hallucination.
 
#### Agentic loop

 The skill implements: Search → Read page → Extract key info → Decide: is this sufficient or search more? → If more: refine query → repeat → When sufficient: synthesize. Claude reasons about what to search next based on what it's found, not just doing a single search.
 
#### How it's different from Perplexity

 Agent-browser integrates directly with your coding workflow. "Research this library and then implement it" — research phase uses browser, implementation uses your codebase context. Perplexity is a separate tool; agent-browser is in-workflow.
 
#### Best for

 Technical research (library comparisons, API docs, implementation examples), competitive analysis, current-events grounding for decisions, finding code examples for unfamiliar patterns.

</details>

Links: —

---

## 📘 Fable Skills (oliwoodman)
**✅ GOOD** · _Claude Skills, Fable 5, Workflows_

Five reusable Claude skill files capturing how Fable 5 approached common dev tasks (security review, project setup, build planning, debugging) before its retirement from standard plans.

<details><summary>Details</summary>

Install manually into ~/.claude/skills/. Useful as reproducible method templates for security-review, project-setup, build-planning, bug-debugging workflows.

</details>

Links: [GitHub](https://github.com/oliwoodman/fable-skills)

---

## 🔍 Find-Skills CLI
**✅ GOOD** · _Skill Discovery, Claude Code Skills Search_

A CLI tool for discovering and installing Claude Code skills from the community ecosystem. Search by capability, install in one command. Keeps your Claude Code setup current with new community skills.

<details><summary>Details</summary>

#### What it does

 The Claude Code skill ecosystem is spread across GitHub. Find-skills aggregates skills from known repos, a central registry, and community contributions. Search: "design" → lists all design-related skills. Search: "mcp" → lists all MCP-related skills.
 
#### Usage

 npx find-skills search "design" → lists matching skills. npx find-skills install taste-skill → installs to Claude Code. npx find-skills list → shows all installed skills. npx find-skills update → updates all installed skills.
 
#### How to evaluate a skill before installing

 Stars: signals community validation. Last update: skills not updated in 6+ months may be stale. SKILL.md quality: read it — is the instruction set specific and opinionated? Or vague? Specific and opinionated = high quality. README examples: do the before/after examples show meaningful improvement?
 
#### Building your skill stack

 Core stack to install: impeccable (design quality), taste-skill (aesthetic taste), wiki-brain (memory), 9router (routing), your preferred DESIGN.md. This covers: quality, aesthetics, memory, routing. Add specialized skills as projects require them.
 
#### Contributing skills

 If you write a SKILL.md that solves a problem, submit to the find-skills registry. Community skills are the long-term value — more domain coverage, more specialized expertise, better results.

</details>

Links: —

---

## 🏗️ MCP-Builder Skill
**✅ GOOD** · _Build Custom MCP Servers, Scaffolding_

Claude Code skill that helps you build custom MCP servers. Scaffolds the boilerplate, implements tools, handles the MCP protocol — you describe what you want Claude to be able to do, it builds the server.

<details><summary>Details</summary>

#### What a custom MCP server is

 MCPs are the way you give Claude new capabilities. A custom MCP server lets Claude interact with any API, internal tool, or local service. With mcp-builder, you can create: a server that connects Claude to your company's internal API, a server that reads your custom database format, a server that controls a local tool you built.
 
#### Usage

 "Using mcp-builder, create an MCP server that can: (1) search my product database by keyword, (2) get product details by ID, (3) update product inventory. The API base URL is [url] and it uses Bearer auth." → Scaffold generates the complete MCP server with tools, auth handling, and error handling.
 
#### What gets generated

 Full TypeScript or Python MCP server with: tool definitions (name, description, input schema), implementation functions, error handling, authentication, claude_desktop_config.json snippet for your server. Ready to run and test immediately.
 
#### Learn the MCP protocol

 After mcp-builder generates your first server, read the code. The protocol is simple: define tools with JSON Schema inputs → implement a function that receives calls → return results. Once you understand one server, building more is fast.
 
#### Community MCP registry

 modelcontextprotocol.io/servers — browse 200+ community MCP servers. Before building custom: check if someone already built what you need.

</details>

Links: —

---

## 📐 Web Design Guidelines Skill
**✅ GOOD** · _Accessibility, Responsive, Best Practices_

A comprehensive set of web design best practices encoded as a Claude skill. WCAG accessibility rules, responsive design patterns, typography standards — always applied when generating UI.

<details><summary>Details</summary>

#### What it enforces

 **Accessibility (WCAG 2.1 AA)**: Color contrast ≥4.5:1 for body text, ≥3:1 for large text. All interactive elements keyboard-accessible. Alt text on all images. Semantic HTML (button not div). Focus indicators visible. **Responsive design**: Mobile-first approach, no fixed pixel widths, image max-width: 100%, viewport meta tag, touch targets ≥44px. **Typography**: Body text minimum 16px, line-height 1.5-1.7, max line width 65-75 characters (60ch), font stack fallbacks.
 
#### Performance rules

 No render-blocking scripts (defer/async), images with width/height attributes (prevent layout shift), font preloading for critical fonts, CSS variables for theming (not repeated hex values), no inline styles except for dynamic values.
 
#### Component patterns

 Forms: labels before inputs (not placeholder-only), error messages with role="alert", required fields marked visually AND with aria-required. Navigation: skip-to-content link, landmark roles (main, nav, aside), breadcrumbs for deep pages.
 
#### When to activate

 Any project where you care about: production quality (public apps, portfolio), accessibility compliance, SEO (accessibility and performance affect rankings), client work. For quick prototypes and demos: fine to skip.
 
#### Checking compliance manually

 axe DevTools Chrome extension (free): run accessibility audit in browser → see violations with fix suggestions. Lighthouse: built into Chrome DevTools → Performance, Accessibility, Best Practices scores.

</details>

Links: —

---

## 🈺 /chinese-grandpa — Prompt Compression
**🤔 MAYBE** · _Token Compression, Novelty_

Translates prompts into Mandarin to compress instructions and save tokens. Use for long, multi-step, or repeated instructions for sub-agents.

<details><summary>Details</summary>

Niche token-saving trick for dense sub-agent instructions — not a general-purpose skill.

</details>

Links: —

---
