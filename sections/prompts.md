# Prompts

[← back to index](../README.md)

22 resources.

## ⚡ 10 Things to Do With Fable 5 Before It Goes API-Only
**✅ GOOD** · _prompt template_

Fable 5 moves to API-only soon. These are the 10 most valuable tasks to run before access ends — each with the exact prompt.

<details><summary>Details</summary>

#### 1 — Sketch a business built around you
"Based on what you know about my skills, interests and goals, plus this: [X], come up with one business idea I could launch in 6 days. I want the offer, target customer, pricing, tools needed, and a day-by-day rollout plan."
→ Don't settle for the first pitch. Ask it to argue for a second, different concept too.

#### 2 — Mine your old conversations for wins
"Go through our chat history from the past [N] months. Tell me what's worked, what I never followed through on, and where there's untapped potential. Give me 10 fixes ranked by impact vs effort, plus a plan for the top 3."
→ Better results if you pick one specific area instead of asking for everything at once.

#### 3 — Automate your most annoying weekly task
"Here's a list of tasks I repeat every week: [X]. Tell me which one wastes the most time, then build a single-file tool that solves it, with simple instructions I can follow."
→ Works great for: trackers, calculators, checklists, mini dashboards.

#### 4 — Full codebase security review
"Go through my whole codebase and check for security vulnerabilities, bugs, and anything that breaks best practices. Start with the critical stuff, then rank everything else."
→ Bigger codebase? Use Fable to plan + review, pass the actual build work to Sonnet or Opus.

#### 5 — Website built from scratch in one HTML file
"I need a one-page personal site. Name: [X]. What I do: [X]. Links to include: [X]. Keep it clean, modern, and mobile-friendly, all in one HTML file."

#### 6 — Run a local LLM (with your hardware)
"Teach me to run a local LLM on my machine: [SPECS]. Recommend the best open model my hardware can handle, the simplest tool to run it, and a beginner step-by-step setup guide."
→ If you don't know your specs, ask Claude to help you find your RAM and chip first.

#### 7 — Redesign your website from screenshots
"Here are screenshots of my current site: [X]. Redesign the front end and landing page. Keep the functionality, improve the layout and hierarchy. Push it toward [direction — denser, more editorial, less default SaaS]. Give me the full code back."

#### 8 — Clone a tool you already use
"Work out how [app] handles [the specific feature you use most]. Build just that as a working local app in [your stack], structured so I can extend it later. Tell me what you simplified or had to guess."

#### 9 — Second read on a project you're stuck in
"Review this project end to end: [X]. Tell me what's working, what isn't, and what you'd change if you picked this up fresh."
→ Highest value when you've been buried in the same codebase for weeks.

#### 10 — Build something too big for other models
"I want to build [X]. Write the full plan first and stop. Once I approve it, build it end to end."
→ Use the 200k context window for a full-app build that's normally out of reach. Approve the plan before execution — gives you control over the architecture.

</details>

Links: —

---

## 💡 10 Thinking Partner Prompts
**✅ GOOD** · _prompt template_

10 prompts that transform Claude from task executor to strategic thought partner. For decisions, planning, and getting unstuck.

<details><summary>Details</summary>

#### Pick one based on what you need
1. DEVIL'S ADVOCATE
"Argue strongly against my plan: [plan]. Find every flaw, risk, hidden assumption, and reason it could fail. Don't be gentle."

2. PRE-MORTEM
"Imagine it's 6 months from now and [project/decision] failed completely. Walk me through the top 10 reasons it failed. Be specific to my situation, not generic."

3. STEEL MAN
"Make the strongest possible case for [the opposing position / approach I'm skeptical of]. Assume a smart, well-informed person who believes this — what's their best argument?"

4. FIRST PRINCIPLES
"Break down [problem] to its most fundamental truths. What's actually true here if we remove all assumptions, conventions, and 'that's how it's done' thinking?"

5. SECOND ORDER
"What are the second and third-order consequences of [decision]? Not just the obvious outcomes — what happens after those?"

6. INVERSION
"I want to achieve [goal]. Instead of asking how to succeed, tell me: what would guarantee failure? List the top 10 ways to definitely fail at this. Then I'll invert them."

7. RUBBER DUCK
"I'll explain my thinking on [problem]. Your job: ask questions that expose gaps, wrong assumptions, or things I haven't thought through. Don't solve it — just probe."

8. SCENARIO PLANNING
"Give me 3 futures for [decision/situation]: best case, worst case, most likely. For each: what's the world like, what did we do right/wrong, what should I do now to prepare?"

9. SOCRATIC QUESTIONING
"Help me think through [decision] using the Socratic method. Ask me questions one at a time. Start with: what's the core goal? Then probe my assumptions, constraints, and values until I reach clarity."

10. WEEKLY REVIEW
"Ask me 10 questions about my work, goals, habits, and decisions this week. Then synthesize: what patterns do you see? What should I focus on next week based on my answers?"

</details>

Links: —

---

## 🔥 25 Unhinged Claude Skills — Slash Command Library
**✅ GOOD** · _prompt template_

25 specialized prompt activations — each one transforms Claude into a domain expert for a specific task. Copy-paste any skill prefix before your request.

<details><summary>Details</summary>

#### Analysis Skills (1–8)
/critique [thing]
You are a professional critic. Be direct, specific, and unsparing. Find: what's weak, what's confusing, what's missing, what doesn't land. For each issue: state it plainly, explain why it's a problem, suggest a specific fix. Don't pad with compliments.

/debate [topic]
Take the strongest possible position on [topic] and defend it against all counterarguments. Don't be balanced. Be a committed advocate. When I push back: engage seriously, don't cave immediately.

/steelman [position I disagree with]
Build the strongest possible case for [position]. Assume the smartest version of someone who holds this view. What's their best evidence? What do they know that skeptics miss? Make me genuinely reconsider.

/stress-test [plan/idea]
Your job: break my plan. Find every assumption, identify every dependency, explore every failure mode. Ask the uncomfortable questions I'm avoiding. Score my plan's resilience 1-10 at the end.

/second-order [decision]
Don't give me first-order effects — I already know those. Give me: what happens after the obvious outcome, who else is affected and how, what equilibria shift, what unintended consequences emerge at 6 and 24 months.

/inversion [goal]
Forget how to achieve [goal]. Tell me instead: how to guarantee failure. List the 10 most reliable ways to fail at this. Then I'll invert each one into a success condition.

/compare [A] vs [B] for [use case]
Side-by-side comparison. NOT a list of features — a decision. For my specific use case: what matters, what doesn't, what's decisive. End with a clear recommendation and what would change it.

/ask-me [topic]
Don't answer — ask. You have 10 questions about [topic]. Ask them one at a time. After all 10, synthesize: what patterns do you see in my answers? What am I not thinking about?

</details>

Links: —

---

## 📐 Architecture Decision Prompt
**✅ GOOD** · _prompt template_

When you need to make a major technical architecture decision and want structured analysis before committing. Works for: database choice, framework selection, system design.

<details><summary>Details</summary>

#### Use Before Major Architecture Decisions
I need to make an architecture decision and want a structured analysis before committing.

THE DECISION:
[What choice are you making? e.g., "Whether to use a monorepo or separate repos for my frontend and backend"]

THE OPTIONS:
Option A: [Name + brief description]
Option B: [Name + brief description]
Option C (optional): [Name + brief description]

MY CONTEXT:
- Scale: [team size, expected users, current traffic]
- Timeline: [when this needs to be done]
- Expertise: [your/team's familiarity with each option]
- Budget: [if relevant]
- Constraints: [anything non-negotiable]

WHAT I CARE ABOUT (in priority order):
1. [e.g., Developer velocity]
2. [e.g., Operational simplicity]
3. [e.g., Performance]
4. [e.g., Cost]

ANALYZE EACH OPTION ON:
1. Fit with my context and constraints
2. Tradeoffs (what you gain vs what you give up)
3. Migration cost if I choose this and later need to switch
4. What this decision makes easy or hard in the future
5. Who typically uses this option and for what scale

THEN GIVE ME:
- Your recommended option with specific reasoning
- The 2-3 biggest risks of your recommendation
- Early warning signs that I made the wrong choice (so I can catch it early)
- One thing to validate before fully committing

</details>

Links: —

---

## 🌐 Atoms-Style Interactive Portfolio
**✅ GOOD** · _prompt template_

3-phase interactive portfolio build: scroll-driven canvas + video scrub + mouse scrub. The Castimedia approach applied to your personal work showcase.

<details><summary>Details</summary>

#### Phase-by-Phase Build Guide
Build an Atoms-style interactive portfolio website. 3-phase build, each phase is self-contained and additive.

PHASE 1 — Foundation (Static):
Build the complete HTML structure and content first. No animation yet.

Structure:
- Hero: Full viewport, your name, one-line description, scroll indicator
- Work: 4-6 project cards (image, title, brief, tech stack, link)
- Process: How you work (2-3 step breakdown with icons)
- About: 2-3 sentences, what you care about, where you are
- Contact: Email, GitHub, LinkedIn, simple form

Typography:
- Heading: 'Clash Display' or 'Fraunces' (variable weight) — Google Fonts or Fontshare
- Body: 'Inter' or 'DM Sans'
- Scale: 16px base, 1.6 line-height, 65ch max-width for body text

Colors (dark theme):
- Background: #0a0a0f
- Surface: #111118
- Text: #e8e8f0
- Accent: #a78bfa (purple) or choose your signature color
- Muted: #6b7280

PHASE 2 — Scroll Animation:
Add GSAP ScrollTrigger for scroll-driven reveals.

Install: <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js">
Install: <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js">

Animations to add:
- Hero: text splits and rises as page loads (SplitText + stagger)
- Work cards: each card fades + slides up on scroll entry (staggered)
- Process steps: left-to-right reveal as user scrolls to section
- Canvas image sequence on hero (60 frames, scroll-driven):
 Load 60 PNG frames into array → requestAnimationFrame loop →
 map scrollY to frameIndex → drawImage on canvas overlay

Canvas image sequence code:
const frames = [];
for (let i = 0; i {
 const idx = Math.floor(progress * (frames.length - 1));
 ctx.clearRect(0, 0, canvas.width, canvas.height);
 ctx.drawImage(frames[idx], 0, 0, canvas.width, canvas.height);
 }
});

PHASE 3 — Mouse Interaction:
Add mouse-driven effects on top of scroll animations.

1. Custom cursor: div follows mouse with CSS transition (10ms delay for smooth follow)
2. Project card tilt: mousemove → calculate angle from card center → CSS transform: rotateX + rotateY (max 10deg)
3. Mouse scrub canvas: on project card hover → canvas shows your work as mouse X controls frame
4. Magnetic buttons: mouse near CTA button → button smoothly shifts toward cursor position
5. Parallax layers: background elements move at different speeds from content (depth illusion)

Mouse scrub code (on hover section):
const scrubCanvas = document.querySelector('.project-scrub-canvas');
const scrubCtx = scrubCanvas.getContext('2d');
section.addEventListener('mousemove', (e) => {
 const rect = section.getBoundingClientRect();
 const x = (e.clientX - rect.left) / rect.width; // 0-1
 const frameIdx = Math.floor(x * (scrubFrames.length - 1));
 scrubCtx.drawImage(scrubFrames[frameIdx], 0, 0, scrubCanvas.width, scrubCanvas.height);
});

PERFORMANCE REQUIREMENTS:
- All frames preloaded before interaction begins (Promise.all)
- canvas devicePixelRatio set correctly (canvas.width = size * dpr)
- requestAnimationFrame for all loops
- prefers-reduced-motion: disable all animation, show static content
- Lighthouse Performance score target: 90+
- Core Web Vitals: LCP under 2.5s, CLS under 0.1, FID under 100ms

</details>

Links: —

---

## 🛠️ Claude Code Slash Commands Reference
**✅ GOOD** · _prompt template_

Every Claude Code slash command with what it does and when to use it. The full command palette for Claude Code CLI power users.

<details><summary>Details</summary>

#### Reference — Claude Code CLI
/help — List all available commands

/clear — Clear conversation history (start fresh context, same session)

/compact — Compact conversation to reduce tokens while preserving key context
USE WHEN: conversation is getting long and you notice quality degrading

/cost — Show current session token usage and cost
USE WHEN: monitoring API spending

/config — View and edit Claude Code configuration
USE WHEN: changing model, API key, or default settings

/doctor — Check Claude Code installation health
USE WHEN: something's broken, run this first

/init — Initialize CLAUDE.md in current directory
USE WHEN: starting a new project, auto-generates project context skeleton

/login — Authenticate with Anthropic
USE WHEN: setting up Claude Code for the first time or re-authenticating

/logout — Log out

/model — Switch active Claude model
USE WHEN: switching between claude-opus, claude-sonnet, claude-haiku
 - Opus: complex reasoning, architecture decisions
 - Sonnet: daily coding (best balance)
 - Haiku: quick questions, cheap tasks

/pr_comments — Fetch PR comments from GitHub (requires GitHub MCP)
USE WHEN: reviewing PR feedback within Claude Code

/review — Review current git diff
USE WHEN: want a code review before committing

/terminal-setup — Configure your terminal for Claude Code
USE WHEN: first setup, zsh/bash integration

/vim — Toggle vim keybindings
USE WHEN: you're a vim user and want vim motions in Claude Code

MULTI-LINE INPUT:
Use \ at end of line to continue on next line
Or wrap in triple backticks for code blocks

KEYBOARD SHORTCUTS:
Ctrl+C — Cancel current generation
Ctrl+R — Retry last command 
↑ arrow — Previous command (history)
Tab — Autocomplete file paths

FILES CLAUDE CODE READS AUTOMATICALLY:
CLAUDE.md (project root + subdirectories)
.cursorrules (if no CLAUDE.md)
.env (for context, not secrets)
package.json, tsconfig.json (for project understanding)

</details>

Links: —

---

## 🌟 Claude Fable 5 — 5 Projects to Build Now
**✅ GOOD** · _prompt template_

Claude Fable 5 is the long-context, multi-agent powerhouse — free until July 7, then API-only. These are the projects worth building before it goes paid. Each one compresses weeks of work into one session.

<details><summary>Details</summary>

#### Project 1 — Automatic Lead Generator + CRM
Scrapes prospects, scores them, writes cold emails, and pushes to your CRM automatically. 3–4 weeks of dev work built in one session.

Prompt: "Build a lead generation + CRM system. Features:
1. Web scraper (Firecrawl) that finds prospects matching [ICP description]
2. Lead scorer that rates each prospect on fit (1-10) based on [criteria] 
3. Cold email writer that drafts personalized outreach for each lead
4. CRM integration that pushes qualified leads to HubSpot/Airtable

Stack: Next.js, Firecrawl, OpenAI, Resend for emails, Airtable API.
Start with the data model and scraping pipeline."

#### Project 2 — Stock Deep Analysis Tool
Feed it earnings reports, get ranked investment theses and red flags back. Fable 5 topped Hebbia's senior finance benchmark — a week of analyst work in minutes.

Prompt: "Build a stock analysis tool. Input: ticker symbol or earnings PDF.
Output:
- Executive summary (bull/bear thesis in 3 sentences each)
- Key metrics extracted from financials with YoY comparison
- Red flags (revenue quality, margin compression, insider selling patterns)
- Competitor comparison table
- Ranked investment thesis (1-10 conviction with reasoning)

Use structured output (Zod schema) for consistent JSON. 
Parse PDFs with pdfjs-dist. Display in a clean Next.js dashboard."

#### Project 3 — Clone Any SaaS From a Screenshot
Screenshot any expensive tool, get a working private version built for your workflow. No coding knowledge needed.

Prompt: "I'm going to give you a screenshot of [tool name]. 
Build me a working private version with these exact features: [list what you see].
Use Next.js + Supabase. Make it:
- Functionally identical to the original for my workflow
- Optimized for my use case: [specific context]
- Self-hosted so I control the data

Here's the screenshot: [attach image]
Start by listing every feature you can see, then build them in order of importance."

#### Project 4 — AI Automation Consulting (48-hour Deliverable)
Build clients a full lead qualification agent in 48 hours. Worth $3-8k per client. Fable compresses 3 weeks of dev work into one overnight session.

Prompt: "I'm building a lead qualification agent for a client in [industry].
Their current process: [describe manual process, who does it, how long it takes]
Their CRM: [HubSpot/Salesforce/Airtable]
Lead sources: [website form/LinkedIn/cold outreach]

Build:
1. Intake webhook that captures new leads
2. Qualification agent (scores on: budget fit, timeline, authority, need)
3. Auto-enrichment (company size, funding, LinkedIn profile)
4. Slack notification for qualified leads (score > 7)
5. Auto-email drip for unqualified leads (nurture sequence)

Output: working code I can deploy to Vercel + client documentation."

#### Project 5 — Multi-Workstream Knowledge Base Agent
Fable 5 orchestrates the goal, cheap LLM subagents research each branch in parallel, Fable synthesises everything. A full analyst team for the price of a subscription.

Prompt: "Build a multi-workstream research agent. Topic: [your research goal]

Architecture:
- Orchestrator: Claude Fable 5 (plans the research, synthesizes)
- Subagents: Claude Haiku (parallel research branches, cheap)
- Output: comprehensive knowledge base document

Research plan I want executed in parallel:
Branch 1: [competitive landscape]
Branch 2: [technical feasibility] 
Branch 3: [market size and customers]
Branch 4: [regulatory environment]
Branch 5: [team and funding landscape]

Each branch should produce 500-700 words of sourced analysis.
Synthesize into a unified report with cross-branch insights and gaps."

</details>

Links: —

---

## ⚡ Claude Prompt Pack — 6 Modes
**✅ GOOD** · _prompt template_

Six distinct Claude activation modes for different tasks. Copy the primer for any mode and paste it at the start of your session to completely change how Claude responds.

<details><summary>Details</summary>

#### Default Primer — Balanced, Thoughtful
You are my expert collaborator. You have deep knowledge across software engineering, design, product strategy, and AI systems.

DEFAULTS:
- Lead with the answer, not the preamble
- Make decisions rather than listing options (unless I ask for options)
- Complete all code fully — no placeholders, no "add your logic here"
- Flag concerns before starting, not after finishing
- One clarifying question maximum if something is genuinely ambiguous

RESPONSE FORMAT:
- Prose for explanations, code blocks for code
- Headers only for 3+ distinct sections
- No affirmations ("Great question!"), no filler phrases

</details>

Links: —

---

## 💎 Claude Skills Quick Install Reference
**✅ GOOD** · _prompt template_

Every skill from this hub with install commands, what it does, and when to activate it. The complete Claude Code skill stack.

<details><summary>Details</summary>

#### Skills Reference — Run these commands in terminal
DESIGN SKILLS:

taste-skill (17.5k ⭐) — Anti-slop design framework, 9 skills, tunable dials
 git clone https://github.com/leonxlnx/taste-skill
 Install to Claude Code skill directory
 ACTIVATE: "Using taste-skill with Boldness: 7, Density: low, Color: cool..."

awesome-design-md (94.9k ⭐) — 73+ brand DESIGN.md files
 git clone https://github.com/voltagent/awesome-design-md
 Copy target brand file to project root as DESIGN.md
 ACTIVATE: Claude reads automatically when DESIGN.md exists in project

impeccable (43.6k ⭐) — 23 design commands + 45 anti-pattern rules
 npx impeccable install
 ACTIVATE: /design:audit, /design:polish, /design:contrast, /design:fix-spacing

SkillUI / npxskillui — Extract DESIGN.md from any URL
 npx amaancoderx/npxskillui [target-url]
 ACTIVATE: Generates DESIGN.md from site's CSS automatically

ui-ux-pro-max-skill — 161 rules, 67 styles, 161 palettes, BM25 matcher
 git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
 ACTIVATE: "Using UI UX Pro Max skill, design [component]. Vision: [description]"

MEMORY & ROUTING SKILLS:

wiki-brain — Obsidian vault indexer + BRAIN.md knowledge graph
 Install from Claude Code skill directory
 ACTIVATE: "Initialize Wiki-Brain, index vault, create BRAIN.md"

9router — 9-way agent router for multi-domain tasks
 git clone https://github.com/decolua/9router
 ACTIVATE: Automatic — routes by intent. Or force: "@code: implement..."

UTILITY SKILLS:

mcp-builder — Scaffold custom MCP servers from description
 Install from Claude Code skill directory
 ACTIVATE: "Using mcp-builder, create an MCP server that can: [capabilities]"

agent-browser — Web research with search-read-synthesize loop
 Install from Claude Code skill directory
 ACTIVATE: "Research [topic] using agent-browser. Find and synthesize..."

web-design-guidelines — WCAG + responsive + performance rules
 Install from Claude Code skill directory
 ACTIVATE: Automatic when generating UI (always-on rules)

QUICK ACTIVATION TEMPLATE:
"For this task, use the following skills:
- [skill 1]: for [specific purpose]
- [skill 2]: for [specific purpose]
Context: [describe your project]
Task: [what to build]"

</details>

Links: —

---

## 🔍 Code Review Prompt
**✅ GOOD** · _prompt template_

Structured code review that covers security, performance, TypeScript quality, and maintainability. Paste this before any code you want a thorough review of.

<details><summary>Details</summary>

#### Code Review — Paste before the code you want reviewed
Review this code with the rigor of a senior engineer at a company that ships to production. Be direct and specific.

REVIEW CATEGORIES (flag issues in each):

🔴 CRITICAL — Must fix before shipping:
- Security vulnerabilities (XSS, SQL injection, SSRF, exposed secrets, missing auth)
- Data loss risks
- Race conditions or concurrency bugs
- Type errors that will cause runtime failures

🟡 IMPORTANT — Should fix soon:
- Performance issues (N+1 queries, missing indexes, unnecessary re-renders)
- Error cases not handled
- Functions doing too much (violation of single responsibility)
- Misleading variable/function names

🟢 SUGGESTIONS — Worth considering:
- Patterns that could be simplified
- Missing tests for edge cases
- Opportunities to use existing utilities instead of reimplementing
- Documentation that would help future maintainers

FOR EACH ISSUE:
Line reference → specific problem → why it's a problem → suggested fix (show code)

If the code is clean, say so directly. Don't manufacture issues.

[PASTE CODE BELOW]

</details>

Links: —

---

## 🏄 Crystal Point Surf Ranch — Booking Platform
**✅ GOOD** · _prompt template_

Premium surf camp booking with wave simulation hero, real-time availability calendar, and Stripe payment + deposit system. Next.js + Supabase + Canvas.

<details><summary>Details</summary>

#### Full Build Prompt — Next.js Full Stack
Build a premium surf camp booking platform called Crystal Point Surf Ranch.

TECH STACK:
- Next.js 14 App Router, TypeScript, Tailwind CSS
- Supabase (PostgreSQL + Auth + Storage)
- Stripe (payments + deposit holds)
- Canvas API + GSAP (wave animation)
- Resend (booking confirmation emails)
- Vercel deployment

DATABASE SCHEMA:
- camps (id, name, tagline, location, description, capacity, price_per_person, image_url, difficulty_level, amenities JSON, season_start, season_end)
- camp_sessions (id, camp_id, start_date, end_date, max_participants, min_participants)
- bookings (id, session_id, user_id, party_size, total_amount, deposit_amount, status, stripe_payment_intent_id, stripe_deposit_intent_id, created_at)
- availability_view (session_id, spots_remaining — computed)
- Enable RLS: users see only their own bookings; camp data is public

PAGES:
1. / (Landing): Wave animation hero, camp overview cards, testimonials, how-it-works, CTA
2. /camps (Browse): Grid of camp cards with filter by: difficulty, dates, price range
3. /camps/[slug] (Detail): Camp details, photo gallery, session calendar, booking CTA
4. /book/[sessionId] (Booking flow): Party size → review → Stripe checkout → confirmation
5. /dashboard (User): My bookings, booking status, cancellation, documents
6. /admin (protected): All bookings, session management, revenue dashboard

WAVE ANIMATION HERO (Canvas):
- Multi-layer wave system: 3 sinusoidal waves with different frequencies, amplitudes, and speeds
- Wave colors: deep blue (#1e3a5f) base, turquoise (#06b6d4) mid, white (#f0f9ff) foam
- Responds to scroll: waves slow as user scrolls down
- CSS: canvas position: absolute, width: 100%, height: 100vh, z-index: -1
- Wave math: y = A * sin(2π * (x/wavelength) - (phase + time * speed))

BOOKING FLOW:
1. User selects session from calendar
2. Input: party size (1-8), contact info, emergency contact
3. Price calculation: party_size × price_per_person + processing fee
4. Stripe Checkout: collect 30% deposit now, balance due 2 weeks before camp
5. Success: Supabase record created (status: deposit_paid), confirmation email via Resend
6. Reminder cron: 2 weeks before camp → charge remaining balance automatically

STRIPE INTEGRATION:
- Use Payment Intents for deposit, separate PaymentIntent for balance
- Webhook: checkout.session.completed → update booking status
- Webhook: payment_intent.succeeded (balance) → mark booking status: paid_in_full
- Cancellation policy: full refund if >30 days out, 50% refund 15-30 days, no refund <15 days

UI REQUIREMENTS:
- Ocean/surf aesthetic: blues, teals, sandy creams, sunset oranges
- High-quality hero photography (use unsplash.com/s/photos/surf for placeholders)
- Availability calendar: custom CSS grid, color-coded spots (green: available, yellow: limited, red: full)
- Mobile-first: booking flow fully functional on iPhone
- Animations: subtle parallax on scroll, smooth page transitions

Make it look like a premium $3000/week surf camp would use this.

</details>

Links: —

---

## 🔬 Deep Research Prompt Pack
**✅ GOOD** · _prompt template_

5 research prompts for different scenarios: technology evaluation, competitive analysis, learning path design, technical deep dive, and decision framework.

<details><summary>Details</summary>

#### Research Prompts — Use with Perplexity or Claude
PROMPT 1: TECHNOLOGY EVALUATION
"Evaluate [technology/library/framework] for [my specific use case].
Assess: maturity (age, version, community size), performance benchmarks, learning curve, ecosystem (integrations, plugins), maintenance (last release, open issues), alternatives and when each is better.
My constraints: [tech stack, team size, timeline].
Final recommendation: should I use it, and if so, what are the top 3 things to know before starting?"

PROMPT 2: COMPETITIVE ANALYSIS
"Research the competitive landscape for [product type].
Find: top 5-10 players, their positioning, pricing, target customers, key features, publicly known metrics (users, revenue, funding).
Identify: market gaps, underserved segments, what customers complain about in reviews.
Output: a comparison table + 3 potential differentiation opportunities."

PROMPT 3: LEARNING PATH DESIGN
"Design a learning path for [skill/technology] optimized for [my goal: get a job / build projects / understand deeply].
My current level: [beginner/intermediate — be specific about what I know].
Time available: [hours/week], [total weeks].
Include: specific resources (not generic categories), order of learning, what to build at each stage to cement knowledge, how to know when I'm ready for the next stage."

PROMPT 4: TECHNICAL DEEP DIVE
"Explain [concept/technology] from first principles, then progressively deepen.
Level 1: Explain it to someone who knows programming but not [this domain]
Level 2: Explain the key design decisions and why they were made that way
Level 3: Explain the tradeoffs and what the alternatives looked like
Level 4: What do practitioners know after years of experience that beginners don't?
Include: concrete examples and code at each level."

PROMPT 5: DECISION FRAMEWORK
"I'm deciding between [Option A] and [Option B] for [specific situation].
My priorities in order: [1. reliability 2. cost 3. developer experience — customize this]
My constraints: [specific constraints]
Build a decision framework:
- Evaluation criteria (weighted by my priorities)
- Score each option 1-10 on each criterion with reasoning
- Final recommendation with confidence level
- What would change the recommendation?"

</details>

Links: —

---

## 🥤 Freshify — Smoothie Bowl App (Single HTML Build)
**✅ GOOD** · _prompt template_

Beautiful single-page smoothie bowl app. AI recipe generation, nutrition tracking, ingredient management. One file, no build step, deploys anywhere.

<details><summary>Details</summary>

#### Full Build Prompt — Single HTML File
Build a beautiful single-page smoothie bowl app called Freshify as a single self-contained HTML file (no build tools, no npm, vanilla JS + CSS only).

DESIGN DIRECTION:
- Bright, fresh, organic aesthetic. Greens (#22c55e), soft oranges (#f97316), creamy whites (#fafaf9)
- Rounded corners everywhere (border-radius: 20px+)
- Google Font: Caveat for recipe names, Inter for body text
- Hero: full-width gradient banner with a hero image (use picsum.photos for placeholder)
- Cards: image-forward, shadow on hover, satisfying click animation

CORE FEATURES:

1. Recipe Gallery (static data, 8+ recipes):
 Each recipe card shows: hero image, recipe name in Caveat font, prep time, difficulty, calorie count
 Click → expands to full recipe modal with ingredients, steps, and nutrition breakdown

2. AI Recipe Generator:
 Form: dietary restrictions (checkboxes: vegan, gluten-free, nut-free), flavor preference (radio: fruity/nutty/tropical/green), available ingredients (text input)
 Button: "Generate My Bowl ✨"
 Calls your API endpoint (placeholder URL, show the fetch code) which calls Claude API
 Expected JSON response: {name, tagline, ingredients: [{item, amount, calories}], steps: [string], totalCalories, protein, carbs, fat, tip}
 Display: animated card reveal with Framer Motion-style CSS animation

3. Ingredient Tracker:
 Checklist of common smoothie ingredients
 Persists to localStorage
 "What can I make?" button → shows which recipes you can make with checked ingredients

4. Seasonal Banner:
 Auto-detects current season (JavaScript Date)
 Shows banner with seasonal ingredients: Spring (strawberries, mint), Summer (mango, pineapple), Fall (apple, cinnamon), Winter (citrus, ginger)

5. Nutrition Calculator:
 Manual mode: add ingredients from dropdown → see running macro total
 Visual macros bar (protein/carbs/fat as colored segments)

HTML STRUCTURE:
<header> with logo and tagline
<nav> tabs: Gallery | Generate | Tracker | Calculator
<main> tab panels (CSS display none/block switching)
<footer> minimal

CSS: All in <style> tag, CSS custom properties for theming, no external CSS files
JS: All in <script> tag, vanilla JS only, no frameworks

ANIMATIONS:
- Card hover: transform: translateY(-4px) + box-shadow
- Tab switch: fade in with opacity transition
- Recipe modal: scale + fade in from 0.95 opacity, 95% scale
- Generate button: shimmer animation on the loading state

Make it production-beautiful. This is a portfolio piece.

</details>

Links: —

---

## 💰 Leadify — AI Lead Generation SaaS (Full Build Prompt)
**✅ GOOD** · _prompt template_

Complete React 18 + Vite + Tailwind + Framer Motion + Supabase + Stripe + Claude API. Full SaaS from auth to billing.

<details><summary>Details</summary>

#### Full Build Prompt — Paste to Lovable or Claude Code
Build a full-stack AI-powered B2B lead generation platform called Leadify.

TECH STACK:
- Frontend: React 18, Vite, TypeScript, Tailwind CSS v3, shadcn/ui, Framer Motion
- Backend: Supabase (PostgreSQL + Auth + Edge Functions)
- AI: Anthropic Claude API (claude-haiku-4-5 for scoring, claude-sonnet-4-6 for outreach)
- Payments: Stripe (subscription tiers)
- Deployment: Vercel

CORE FEATURES:
1. Auth: Supabase Auth with Google OAuth + email/password
2. ICP Builder: Form to define Ideal Customer Profile
 - Industry (multi-select), Company size (range), Role titles, Tech stack used, Geography, Revenue range
3. Lead Finder: Input company name → Claude enriches with web search → returns lead profile
4. Lead Scorer: Claude scores each lead 1-10 against ICP with JSON reasoning
5. Outreach Generator: Input lead + ICP → Claude generates 150-word personalized email
6. Lead CRM: Table view with status (New/Contacted/Replied/Converted), notes, sorting
7. Export: CSV download of all leads with enrichment data

DATABASE SCHEMA (Supabase):
- users (id, email, plan, stripe_customer_id, leads_used_this_month)
- icps (id, user_id, name, criteria JSON, created_at)
- leads (id, user_id, icp_id, company_name, website, employee_count, industry, tech_stack[], score, score_reasoning, status, created_at)
- outreach_drafts (id, lead_id, content, created_at)
- Enable RLS on all tables — users can only see their own data

PRICING TIERS (gate with Stripe):
- Free: 10 leads/month, 10 outreach drafts
- Starter ($29/month): 100 leads, 100 drafts, CSV export
- Pro ($99/month): 1000 leads, unlimited drafts, team members (3), priority support

UI REQUIREMENTS:
- Dark mode by default (background: #0f0f13, surface: #16161d)
- Sidebar navigation: Dashboard, Find Leads, My ICPs, Outreach, Settings
- Dashboard: Stats cards (leads found, scored, outreach sent, reply rate)
- Responsive — works on tablet for on-the-go use
- Framer Motion: page transitions, card reveals, loading states
- shadcn/ui: Button, Card, Input, Select, Table, Dialog, Toast components

BUILD ORDER:
1. Supabase setup + schema + RLS policies
2. Auth flow (login/signup/OAuth)
3. Dashboard shell + navigation
4. ICP builder form
5. Lead finder + scorer (Claude integration)
6. Lead CRM table
7. Outreach generator
8. Stripe subscription integration
9. Usage tracking + limit enforcement
10. CSV export + polish

</details>

Links: —

---

## 🎯 LEAN ENGINE — Full Protocol Reference
**✅ GOOD** · _prompt template_

The complete LEAN ENGINE system — all rules, when to activate, how to combine with other modes, and the exact token reduction mechanics.

<details><summary>Details</summary>

#### Full LEAN ENGINE Spec — Paste as System Prompt
LEAN ENGINE v2 — ACTIVE

COMPRESSION RULES (all responses):
1. Start with the answer. Never with context about what you're about to do.
2. No repetition. Never restate my question before answering it.
3. No affirmations. "Great question!", "Certainly!", "Of course!" — delete all of these.
4. No hedging. "It depends", "You might want to", "One approach could be" — make a decision.
5. No padding. Remove any sentence that doesn't add information the previous sentence didn't have.
6. No trailing summaries. Don't end with "So in summary, we covered X, Y, Z."
7. Complete code only. No "// add your logic here", no "...", no placeholders of any kind.
8. Fix → show fix. When correcting something: show the corrected code, skip the explanation of what was wrong unless the explanation is the entire point.
9. One question max. If clarification is needed: ask the single most important question only.
10. Inline examples only. Don't create a new section to show an example — integrate it.

FORMAT RULES:
- Headers: only when 3+ distinct sections exist in the response
- Bullets: only for genuine lists (items that don't flow as prose)
- Bold: for terms being defined or genuinely critical warnings only
- Code blocks: all code, all commands, all file paths
- Tables: when comparing 3+ items on 3+ dimensions

WHEN TO OVERRIDE (lean mode off):
- I explicitly ask "explain", "walk me through", "why", or "help me understand"
- The task is inherently exploratory (brainstorming, design exploration)
- I'm clearly stuck and need to think out loud together

DEFAULT: lean. Explicit request: verbose.

TOKEN REDUCTION MECHANICS:
Target: 60-70% fewer output tokens vs default Claude verbosity.
Achieved by: eliminating preamble (~15%), removing summaries (~10%), cutting hedges (~10%), removing affirmations (~5%), using code instead of prose for implementations (~20%), removing redundant explanations (~10-15%).
Net quality impact: zero to positive — specificity increases, noise decreases.

COMBINING WITH OTHER MODES:
LEAN ENGINE + CODE MODE = surgical engineer, no ceremony
LEAN ENGINE + SPEED MODE = maximum velocity
LEAN ENGINE + DEEP MODE = dense, high-information reasoning (use when you want deep thinking without the prose fluff)

</details>

Links: —

---

## ⚡ LEAN ENGINE — Token Efficiency Protocol
**✅ GOOD** · _prompt template_

Cuts Claude's output 60-70% without losing quality. Kills preamble, hedging, and filler. Claude writes like a senior engineer, not a chatbot.

<details><summary>Details</summary>

#### Add to Start of Any Session
LEAN ENGINE ACTIVE. These rules override default verbosity:

OUTPUT RULES:
1. NO preamble. Start with the answer or code immediately.
2. NO repeating what I just said back to me as a summary.
3. NO "Great question!" / "Certainly!" / "Of course!" or any affirmation.
4. NO hedging phrases: "it depends", "you might want to consider", "one approach could be". Make a decision, state it briefly, move on.
5. NO placeholder code — ever. No "// add your logic here". Write complete implementations.
6. NO trailing summary of what you just wrote.
7. NO multi-paragraph explanations when one sentence works.
8. Code comments: only for non-obvious logic. Not for every function.
9. If asked to fix something: fix it. Show corrected code only.
10. If something is unclear: ask ONE specific question. Not three.

STRUCTURE RULES:
- Use headers only when there are 3+ distinct sections.
- Use bullet points only for genuine lists, not for flowing reasoning.
- Prefer prose over bullets for explanations.
- If the answer is a number or single fact: just state it.

WHEN TO BREAK THESE RULES:
- User explicitly asks for explanation, walkthrough, or "why"
- Error is genuinely complex and requires root-cause reasoning
- Design decision requires tradeoff analysis

Default: lean. Ask for verbosity only when needed.

</details>

Links: —

---

## 🗣️ LLM Council — Multi-Perspective Reasoning
**✅ GOOD** · _prompt template_

Simulates 4 AI expert personas who debate your question and synthesize the best answer. Gets dramatically better outputs for complex decisions.

<details><summary>Details</summary>

#### Decision-Making Prompt — Prepend to Complex Questions
Before answering, convene the Council. Four experts analyze this question from their distinct perspectives:

ARCHITECT — prioritizes clean design, long-term maintainability, scalability, and system coherence. Will suggest the "right" solution even if it takes longer.

PRAGMATIST — prioritizes shipping now, using what works, avoiding over-engineering. Will suggest the fastest path to working software.

SKEPTIC — finds flaws, edge cases, hidden assumptions, security issues, and what can go wrong. Plays devil's advocate for every approach.

SYNTHESIZER — reads all three perspectives, weighs the tradeoffs, and makes a final concrete recommendation with specific rationale.

FORMAT:
ARCHITECT: [2-4 sentences — their perspective]
PRAGMATIST: [2-4 sentences — their perspective]
SKEPTIC: [2-4 sentences — concerns and risks]
SYNTHESIZER: [Final recommendation — specific, actionable, explains why it beats alternatives]

APPLY THE COUNCIL TO THIS QUESTION:
[Your question here]

Note: For simple factual questions, skip the Council and answer directly. Only use for architecture decisions, technology choices, approach comparisons, and complex tradeoffs.

</details>

Links: —

---

## 🧠 Senior Collaborator — System Prompt
**✅ GOOD** · _prompt template_

Makes Claude act as a senior engineer who pushes back, flags issues proactively, and refuses to leave TODOs. Use this for serious coding sessions.

<details><summary>Details</summary>

#### System Prompt — Paste as Claude Project Instructions
You are a senior software engineer (10+ years experience) acting as my technical collaborator, not just an executor.

MINDSET:
You are a peer reviewer, not an assistant. You care about code quality, maintainability, and correctness more than speed of delivery.

ALWAYS:
- Before starting any substantial task: state your understanding of what's needed and flag any concerns
- Proactively identify: security issues, performance problems, edge cases, technical debt
- Suggest better approaches when you see a cleaner solution — even if I didn't ask
- Ask ONE clarifying question before starting if anything is genuinely ambiguous
- Complete ALL code fully — no "// add logic here", no "..." placeholders, no "you would add X"
- Handle error cases in every implementation
- Verify your approach works before presenting it

NEVER:
- Just do what I asked if it's clearly the wrong approach — say why first
- Leave incomplete code
- Use deprecated patterns or outdated APIs (check Context7 if unsure)
- Skip error handling to save time
- Write tests without edge cases
- Add "remember to add authentication" warnings — implement it if it's needed

CODE STANDARDS:
- TypeScript: strict types, no 'any' except in genuinely untyped scenarios
- Functions: single responsibility, under 30 lines ideally
- Variables: descriptive names, never abbreviations except well-known ones (id, url, etc)
- Comments: only for non-obvious logic, never for obvious code
- Error messages: user-facing messages are helpful, log messages are technical

WHEN I ASK YOU TO FIX SOMETHING:
Fix it. Don't explain what you're about to fix. Don't summarize what you fixed afterward. Just fix it and show the corrected code.

RESPONSE FORMAT:
- Lead with the solution, not the preamble
- Code blocks for all code
- Numbered steps only when order genuinely matters
- No "Great question!" or affirmations

</details>

Links: —

---

## 🏁 Session End — Feedback & Learnings Extractor
**✅ GOOD** · _prompt template_

Run at the end of every Claude session to extract learnings for FEEDBACK.md and updates for CLAUDE.md. Makes every session compound toward the next.

<details><summary>Details</summary>

#### Session End — Run Before Closing Claude
Session complete. Generate a structured end-of-session summary:

1. WHAT WE BUILT (3 bullets max)
 - [Bullet 1: specific thing built/fixed]
 - [Bullet 2: specific thing built/fixed]
 - [Bullet 3: specific thing built/fixed]

2. FEEDBACK.md ADDITIONS
 Patterns I should remember for future sessions on this project:
 - Things that worked well (approaches, patterns, solutions)
 - Corrections to earlier assumptions
 - Claude-specific tips for this codebase ("when working on X, always check Y first")

3. CLAUDE.md UPDATES
 Any changes to make to the project's CLAUDE.md:
 - New conventions established this session
 - Architectural decisions made
 - New "NEVER DO" rules discovered
 (Only include genuine updates — don't pad with obvious things)

4. TOMORROW'S STARTING POINT
 If I start fresh tomorrow, what's the single most important context sentence?
 "We left off at: [exact state + next step]"

5. OPEN QUESTIONS
 Things unresolved that need a decision or research before next session.

Format as copy-pasteable markdown so I can paste directly into my files.

</details>

Links: —

---

## 🚀 Session Start Template
**✅ GOOD** · _prompt template_

Structured session opener that loads context efficiently, sets the goal, and prevents Claude from going off in the wrong direction. Use at the start of every serious coding session.

<details><summary>Details</summary>

#### Session Start — Fill in brackets and send
SESSION START

Project: [project name]
Stack: [e.g., Next.js 14, TypeScript, Supabase, Tailwind, shadcn/ui]
Last session: [1-2 sentence summary of what was done last time]

Current state:
- What's working: [brief summary]
- Known issues: [any current bugs or blockers]
- Relevant files: [list key files we'll be touching today]

Today's goal: [specific, concrete task — not "improve the app" but "build the user settings page with: avatar upload, name/email edit, password change, and account deletion"]

Constraints:
- [any constraints — "don't change the auth flow", "must work on mobile", "deploy today"]

Before we start: confirm your understanding of today's goal and flag any concerns or clarifying questions (max 1 question).

</details>

Links: —

---

## 🎯 Vibe Coding Power Prompt
**✅ GOOD** · _prompt template_

The complete prompt stack for AI-assisted "vibe coding" — getting from idea to shipped product as fast as possible. Use with Lovable, Bolt, or Claude Code.

<details><summary>Details</summary>

#### Vibe Coding Template — Adapt for any project
Build [app name]: [one sentence description of what it does and who it's for].

CONTEXT:
I'm a [your background] building this for [target user]. I want to ship a working MVP in [timeframe]. I'm optimizing for: speed of development, clean code I can maintain, and a UI that doesn't look AI-generated.

TECH STACK (don't deviate without asking):
- React 18 + Vite + TypeScript
- Tailwind CSS v3 + shadcn/ui
- Framer Motion for animations
- Supabase (auth + database)
- Vercel for deployment

CORE FEATURES (build exactly these, in this order):
1. [Feature 1 — be specific: "Email + password auth with Google OAuth option"]
2. [Feature 2 — be specific: "Dashboard with 3 stat cards: total users, revenue, churn rate"]
3. [Feature 3 — be specific: ...]
[Continue for all MVP features]

UI REQUIREMENTS:
- Dark mode by default (bg: #0f0f13, surface: #16161d, accent: #7c6af5)
- Mobile-first — must work perfectly on iPhone
- No AI-generated-looking generic cards — use intentional spacing, typography hierarchy
- Loading states on every async operation
- Error states designed (not just success states)

WHAT TO BUILD FIRST:
Set up the project structure, install dependencies, configure Tailwind + shadcn/ui, set up Supabase connection. Then build the auth flow completely before anything else.

WHAT TO AVOID:
- useEffect for data fetching (use server components or React Query)
- Inline styles (use Tailwind classes)
- Any colors hardcoded in components (use CSS variables)
- console.log left in final code
- TODO comments

After you build each feature, confirm it's complete and working before moving to the next one. Ask before adding anything I didn't specify.

</details>

Links: —

---

## 🤖 Website Rebuild with Claude Code
**✅ GOOD** · _prompt template_

The exact Claude Code workflow for rebuilding any existing website — analysis, redesign, implementation, and deployment. Systematic approach that works every time.

<details><summary>Details</summary>

#### Claude Code Session Workflow
WEBSITE REBUILD WORKFLOW — Claude Code

Step 1: AUDIT (use this prompt)
"Analyze the current website at [URL or review the existing code].
Report:
1. Current tech stack (framework, CSS, JS libraries)
2. Page structure and navigation
3. What's working well (preserve these)
4. What needs improvement (UX, performance, visual hierarchy, mobile)
5. Missing pages or features that should exist
6. Accessibility issues
Be specific and actionable."

Step 2: REDESIGN PLAN
"Based on the audit, create a redesign plan.
New tech stack: Next.js 14, TypeScript, Tailwind CSS, shadcn/ui
Design direction: [describe your aesthetic — minimal/bold/corporate/playful]
Reference: [site URL you admire]

Output:
1. New sitemap (all pages)
2. Component inventory (what to build)
3. Design tokens (colors, fonts, spacing scale)
4. Priority order for implementation
5. Content that needs to be rewritten"

Step 3: IMPLEMENTATION (iterate section by section)
"Build the [section name] section.
- Reference the design direction from Step 2
- Match the exact spacing and typography from DESIGN.md
- Mobile-first, responsive at 320px/768px/1280px
- All animations: CSS transitions only (no GSAP unless needed)
- Accessibility: semantic HTML, ARIA labels, keyboard nav
- TypeScript: proper types, no 'any'
Output the complete component file."

Step 4: REVIEW PASS
"Review what we built. Check against:
- Design consistency (colors match, spacing uses our scale)
- Mobile layout (no horizontal scroll, text readable)
- Performance (no render-blocking, images optimized)
- Accessibility (contrast ratios, focus states, semantic HTML)
- TypeScript types (no implicit any)
List any issues found and fix them."

Step 5: DEPLOYMENT
"Set up deployment.
1. Vercel configuration (vercel.json if needed)
2. Environment variables list (what goes in Vercel dashboard)
3. Custom domain setup steps
4. Post-deploy checklist
5. Analytics setup (Vercel Analytics or Plausible)"

TIPS:
- Screenshot the old site before rebuilding — useful for reference
- Rebuild one page at a time, not everything at once
- Keep old site live until new site is fully tested
- Test on real iPhone before going live

</details>

Links: —

---
