# Projects

[← back to index](../README.md)

23 resources.

## 🏋️ AI Fitness Coach
**🔥 MUST USE** · _Vision Models, Supabase, Next.js, Difficulty: 5, 10_

Upload meal photos → calorie estimation. Workout planner, form analysis via camera, daily habit tracking. Perfect first AI + Vision project — impressive output, manageable complexity.

<details><summary>Details</summary>

#### Stack

 Next.js (frontend + API routes), OpenAI Vision or Gemini Vision API (photo analysis), Supabase (user data, workout history, streaks), Vercel AI SDK (streaming responses), Recharts or Tremor (progress charts).
 
#### Feature breakdown

 **Meal photo upload** — user uploads photo → Vision API returns estimated calories, macros, ingredients. Store per meal. **Workout planner** — Claude generates personalized plans based on goals/equipment. Progression logic (add weight each session). **Form analysis** — user records exercise via webcam → frame analysis for basic form feedback (advanced, use for v2). **Habit tracking** — streaks, weekly check-ins, progress toward goals.
 
#### Key learnings

 Vision model integration (multimodal inputs). Structured output (Zod schema for consistent calorie/macro JSON). Image upload handling in Next.js. Supabase real-time for live streak updates. Dashboard design with data visualization.
 
#### Claude prompt for build

 "Build an AI fitness coach app with Next.js and Supabase. Features: meal photo upload with calorie estimation using OpenAI Vision, personalized workout plan generator, streak tracking, and a dashboard with Recharts progress charts. Use Vercel AI SDK for streaming. Start with the data models and API routes."
 
#### Monetization

 Freemium: 5 meal analyses/day free, unlimited on Pro ($9/mo). Very buildable in a weekend for the MVP.

</details>

Links: —

---

## 🧠 AI Second Brain for Devs
**🔥 MUST USE** · _RAG, pgvector, LangGraph, Memory, Difficulty: 7, 10_

Remembers conversations, stores project context, lets you search old decisions. "What did we decide last week?" — actually answered. The developer tool version of the Obsidian second brain.

<details><summary>Details</summary>

#### Stack

 Next.js (chat UI), LangGraph or OpenAI Agents SDK (memory management), pgvector + Pinecone (vector storage), RAG (retrieval-augmented generation), Redis (session cache), Supabase (relational data).
 
#### Core architecture

 Every conversation chunk gets embedded and stored in pgvector. On new queries: retrieve top-k relevant chunks via semantic search, inject into context. Store project-level summaries separately (updated periodically). "Working memory" (recent 10 exchanges) vs "long-term memory" (vector search).
 
#### Key learnings

 Embeddings and vector similarity (cosine, dot product). RAG pipeline (chunk → embed → retrieve → augment → generate). Long-term memory architecture for AI agents. Context window management (what to include, what to summarize). pgvector queries in SQL.
 
#### Implementation tip

 Start without pgvector — just store all conversations in Supabase and do simple text search. Add semantic search in v2. Don't over-engineer the memory architecture upfront.
 
#### Claude prompt

 "Build an AI second brain for developers. Core feature: persistent memory that remembers past conversations and project decisions. Stack: Next.js, Supabase with pgvector, OpenAI embeddings. Implement: conversation storage, chunk embedding, semantic retrieval on new queries, and a simple chat UI. Start with the database schema and embedding pipeline."

</details>

Links: —

---

## 🥤 Freshify — Smoothie Bowl App
**🔥 MUST USE** · _Single HTML, Food Tech, AI Recipes_

Beautiful single-page smoothie bowl app. AI-powered recipe generation, nutrition info, ingredient tracker. Built as a single HTML file — proof that beautiful apps don't need complex stacks.

<details><summary>Details</summary>

#### Why single-HTML

 Single HTML files: deploy anywhere instantly (drag to Netlify drop), zero build step, no dependencies to break, works offline, portfolio-friendly (just view source). Perfect for: demos, client presentations, side projects that need to be maintainable long-term with zero maintenance.
 
#### Core features

 Recipe card gallery (CSS Grid, image-forward). AI recipe generator (user inputs: dietary restrictions, flavor preference, available ingredients → Claude returns custom recipe). Nutrition calculator (per-ingredient breakdown, total macros). Ingredient tracker (localStorage, persists across sessions). Seasonal ingredients banner.
 
#### The AI integration in vanilla JS

 async function generateRecipe(preferences) {
 const response = await fetch('/api/recipe', {
 method: 'POST',
 headers: {'Content-Type': 'application/json'},
 body: JSON.stringify({preferences})
 });
 const recipe = await response.json();
 renderRecipeCard(recipe);
} 
 The API route calls Anthropic API and returns structured JSON. Keep Claude's response as JSON: {name, ingredients, steps, macros, serving_tip}.
 
#### Design direction

 Bright, fresh, organic. Greens, soft oranges, creamy whites. Rounded corners everywhere. Food photography as hero images (use Unsplash API for free). Handwritten-style font for recipe names (Google Fonts: Caveat). Clean sans-serif for nutrition data.
 
#### Enhancements

 PWA manifest → installable on home screen. Swipe gestures for recipe browsing. Shopping list export (PDF or email via Resend). Social share card generator (OG image with recipe name).

</details>

Links: —

---

## 🌐 Interactive Portfolio (Atoms-Style)
**🔥 MUST USE** · _Scroll Canvas, Mouse Scrub, GSAP_

The Atoms-style interactive portfolio with scroll-driven animation, mouse scrub effects, and video sequences. The portfolio that makes recruiters and clients stop and pay attention.

<details><summary>Details</summary>

#### The 3-phase build order

 **Phase 1 — Foundation**: Static HTML, content structure, typography, basic CSS. Get the words and layout right first. **Phase 2 — Scroll Canvas**: Add the scroll-driven image sequence or particle system. Test on mobile. Optimize performance. **Phase 3 — Interactive Layer**: Mouse scrub on hover states, cursor effects, subtle parallax. Final performance pass.
 
#### Essential libraries

 npm install gsap @gsap/observer — ScrollTrigger for scroll control. npm install three — Three.js for 3D elements (optional but impressive). Canvas API is native — no additional install. Vite for bundling (fast HMR for iterating).
 
#### Image sequence optimization

 Target: 60-90 frames for smooth animation. Export from After Effects as PNG sequence → compress with imagemin → total size target: under 8MB for the sequence. Load all frames on page load (prevents jank during animation). Use canvas, not img tags — canvas has better performance for rapid frame changes.
 
#### Mouse scrub implementation

 document.addEventListener('mousemove', (e) => {
 const x = e.clientX / window.innerWidth; // 0-1
 const y = e.clientY / window.innerHeight; // 0-1
 const frameIndex = Math.floor(x * (frames.length - 1));
 ctx.drawImage(frames[frameIndex], 0, 0, canvas.width, canvas.height);
}); 
 
#### Performance checklist before launch

 ☐ requestAnimationFrame for all animation loops. ☐ Canvas device pixel ratio set correctly. ☐ Images preloaded with Promise.all. ☐ will-change: transform on animated elements. ☐ Tested on iPhone SE (smallest common viewport). ☐ FPS stays above 50 on mid-range devices.
 
#### Hosting

 Vercel or Cloudflare Pages (both free for static sites). Use Cloudflare CDN for asset delivery — fastest global load times for your image sequences.

</details>

Links: —

---

## 🧠 Jarvis — Personal AI System
**🔥 MUST USE** · _6-Domain AI, Finance + Health + Career_

A personal AI operating system with 6 specialized domains: Finance (portfolio tracking), Health (fitness, nutrition), Learning (spaced repetition), Career (goals, resume), Research (knowledge base), Daily Ops (planning, habits).

<details><summary>Details</summary>

#### System architecture

 Central Jarvis dashboard (Next.js) connecting 6 specialized agents. Each agent has its own: system prompt, data sources, MCP connections, memory files. The dashboard routes requests to the right agent and aggregates outputs.
 
#### 6 domains

 **Finance**: Portfolio tracking, net worth calculation, spending analysis, investment thesis notes. **Health**: Workout logging, nutrition tracking (Cronometer API or manual), sleep tracking, weekly health review. **Learning**: SM-2 spaced repetition for concepts you're studying, reading tracker, note-taking with AI summaries. **Career**: Goal tracking, resume versioning, networking log, skill gap analysis. **Research**: Wiki-Brain integration, project notes, idea inbox. **Daily Ops**: Morning planning, habit tracking, evening review, weekly retrospective.
 
#### Tech stack

 Next.js 14 dashboard. Supabase for all persistent data. Claude API for all intelligence. Notion MCP for knowledge base. Slack MCP for daily digest delivery. Email MCP for daily brief. Stripe for tracking subscriptions (finance domain).
 
#### SM-2 spaced repetition implementation

 When reviewing a concept: rate recall (0-5). SM-2 algorithm: interval = prev_interval * easiness_factor. EF updates based on quality: EF' = EF + (0.1 - (5-q) * (0.08 + (5-q) * 0.02)). Next review = today + interval. Jarvis surfaces due cards in the Learning domain each morning.
 
#### Morning brief

 Daily at 7am: Slack message (or email) with: today's habits, due learning cards, calendar overview, 3 priorities, weather, relevant news. All generated by Jarvis running overnight.

</details>

Links: —

---

## 💰 Leadify — AI Lead Generation SaaS
**🔥 MUST USE** · _React, Vite, Tailwind, Framer Motion_

AI-powered B2B lead generation platform. Companies define their ICP, AI finds matching leads from public data sources, scores them, and drafts personalized outreach. Full SaaS with auth + payments.

<details><summary>Details</summary>

#### Tech stack

 React 18 + Vite + Tailwind CSS + Framer Motion (frontend). Supabase (database + auth). Anthropic Claude API (lead analysis + outreach draft). Stripe (subscription billing). Vercel (deployment). Exa or Apollo API (lead data source).
 
#### Core features to build

 ICP definition form (industry, company size, role, tech stack, geography). Lead enrichment pipeline (fetch company data → enrich with LinkedIn/web data → score against ICP). Outreach generator (input: lead profile + ICP → output: personalized 150-word email). CRM-lite (track lead status: found/contacted/replied/converted). Export to CSV.
 
#### Database schema

 Users, Organizations, ICPs, Leads (with enrichment data + score), Campaigns, Emails (generated outreach drafts), Subscriptions. All with RLS policies so companies only see their own data.
 
#### Monetization

 Free: 10 leads/month. Starter $29/month: 100 leads + 100 outreach drafts. Pro $99/month: 1000 leads, AI scoring, CSV export, team members. Each tier locked behind Stripe subscription status check.
 
#### The AI lead scoring prompt

 "Score this company as a potential customer for [ICP description]. Company data: [enriched data]. Score 1-10 on: industry fit, size fit, tech stack fit, growth stage fit. Return JSON with scores and one sentence reasoning for each." Consistent, explainable scoring.
 
#### Portfolio value

 Leadify demonstrates: full-stack SaaS architecture, Stripe integration, AI integration, subscription gating, data pipeline, async processing. Strong portfolio piece for SaaS engineering and AI engineering roles.

</details>

Links: —

---

## 🤖 Multi-Agent Workflow Pipeline
**🔥 MUST USE** · _LangGraph, Anthropic SDK, Parallel Agents_

Build a production multi-agent system using LangGraph or Anthropic Agent SDK. Orchestrator routes to specialist agents (research, write, review). Demonstrates real AI engineering skills.

<details><summary>Details</summary>

#### LangGraph vs Anthropic Agent SDK

 **LangGraph**: More complex, more control, better for graph-based workflows with cycles and conditional routing. Python-first. Better for complex orchestration with branching logic. **Anthropic Agent SDK**: Simpler, TypeScript or Python, optimized for Claude. Better for straightforward delegation patterns. Use LangGraph for complex systems, Anthropic SDK for simpler ones.
 
#### LangGraph pipeline pattern

 from langgraph.graph import StateGraph, END

def create_pipeline():
 workflow = StateGraph(State)
 workflow.add_node("research", research_agent)
 workflow.add_node("write", write_agent)
 workflow.add_node("review", review_agent)
 
 workflow.add_edge("research", "write")
 workflow.add_edge("write", "review")
 workflow.add_conditional_edges("review",
 should_revise, # returns "write" or END
 {"write": "write", "done": END}
 )
 return workflow.compile() 
 
#### Parallel agent pattern

 # Research 3 topics simultaneously
results = await asyncio.gather(
 research_agent("topic 1"),
 research_agent("topic 2"),
 research_agent("topic 3")
)
merged = synthesis_agent(results) 
 
#### Build project idea

 Content creation pipeline: Research Agent (Exa search) → Outline Agent → Writing Agent (section by section) → Editor Agent → Fact-Check Agent → Final polish. Takes a topic, produces a polished article. Deployable as an API.
 
#### Portfolio demonstration value

 Multi-agent systems are the frontier of AI engineering. Building one demonstrates: async Python, API orchestration, prompt engineering at scale, error recovery, state management. Impressive to ML/AI-focused companies.

</details>

Links: —

---

## 🔍 RAG + Hybrid Search Pipeline
**🔥 MUST USE** · _ChromaDB, BM25, RRF Fusion_

Production-grade Retrieval Augmented Generation with hybrid search: dense vector (ChromaDB) + sparse BM25 keyword + RRF fusion ranking. The real RAG architecture, not toy implementations.

<details><summary>Details</summary>

#### Why hybrid search beats pure vector search

 Pure vector search finds semantically similar content but misses exact keyword matches (product IDs, person names, specific technical terms). Pure BM25 finds keywords but misses semantic similarity ("automobile" vs "car"). Hybrid combines both: vector handles meaning, BM25 handles specifics. RRF (Reciprocal Rank Fusion) merges the two ranked lists into one optimal list.
 
#### Architecture

 Query → parallel paths:
├─ Dense: query → embedding → ChromaDB cosine search → ranked list 1
└─ Sparse: query → BM25 index → keyword search → ranked list 2
→ RRF fusion → reranked combined list
→ Top k documents → LLM context → answer 
 
#### Full Python implementation

 pip install chromadb rank-bm25 anthropic sentence-transformers . Use sentence-transformers/all-MiniLM-L6-v2 for embeddings (384-dim, fast, free). ChromaDB for vector storage (local or hosted). BM25Okapi from rank-bm25 for keyword index. RRF formula: score = 1 / (k + rank) where k=60 (standard). Sum RRF scores across both rankings.
 
#### Chunking strategy

 Don't chunk naively by character count. Use semantic chunking: split at sentence boundaries, keep related sentences together, target 256-512 tokens per chunk. Overlap 50-100 tokens between chunks to prevent information loss at boundaries.
 
#### Reranking (advanced)

 After RRF: add a cross-encoder reranker (Cohere Rerank API or local Jina reranker) to re-score the top 20 results. Cross-encoders consider query+document together (better accuracy than separate encodings). Use for production where quality matters.
 
#### Portfolio application

 Build this as a personal knowledge base search: index all your notes, books, research papers → search across everything with natural language. Demonstrate: vector DB, embeddings, hybrid search, reranking, Claude integration. Strong portfolio piece for ML/AI roles.

</details>

Links: —

---

## 🔬 SE → AI Engineer: 15 Projects
**🔥 MUST USE** · _Production AI, Real Problems, Portfolio_

15 projects that solve real production AI problems. None of these are "I called an API and deployed a chatbot." Every one builds a real skill AI teams actually need at scale.

<details><summary>Details</summary>

#### Evals + Quality

 **1. Model regression detection system** — automated tests that catch when a model update breaks your outputs. **2. LLM cost autopilot** — monitor spend per model/feature, auto-switch to cheaper model when quality metrics stay above threshold. **13. Automated eval dataset generator** — takes your production logs, extracts good/bad examples, builds eval suite automatically.
 
#### Infrastructure

 **3. Failure forensics tool for AI pipelines** — when an agent fails, trace which step failed, why, and what context caused it. **7. Semantic caching layer** — cache LLM responses by semantic similarity, not exact text match. Reduces API costs 40-60% on repeated queries. **11. LLM gateway with rate limiting + fallback routing** — single API surface, automatic failover between providers.
 
#### RAG + Data

 **6. RAG pipeline with hybrid search** — dense (embeddings) + sparse (BM25) + RRF fusion. Beats pure semantic search for most production use cases. **8. Text-to-SQL with guardrails** — natural language → validated SQL → safe execution. The guardrails (query validation, scope limiting) are harder than the SQL generation. **14. Multi-modal document processor** — PDFs with tables, charts, images → structured data extraction.
 
#### Agents + Orchestration

 **4. Self-healing documentation bot** — detects when docs are outdated vs code, auto-generates PRs with updates. **15. Agent orchestration system** — route tasks to specialized subagents, handle retries and failures, aggregate results. **5. LLM output arbitration system** — run same prompt on 3 models, vote or judge to pick the best output.
 
#### Dev Tools

 **9. Prompt versioning + A/B testing platform** — git for prompts, run experiments, track win rates. **10. Fine-tuning pipeline with LoRA** — end-to-end: data collection → formatting → LoRA training → evaluation → deployment. **12. AI feature flag system** — roll out AI features gradually, monitor quality per cohort, auto-rollback.
 
#### How to pick

 Start with #6 (RAG hybrid search) or #7 (semantic caching) — high impact, medium complexity, immediately useful. Do #1 (regression detection) early if you have production AI. Do #15 (orchestration) last — it builds on everything else.

</details>

Links: —

---

## 🏄 Surf Ranch — Booking Platform
**🔥 MUST USE** · _Next.js, Canvas, Booking System_

Premium surf camp booking platform with wave simulation canvas animation, real-time availability, and seamless checkout. Combines beautiful frontend with full booking system backend.

<details><summary>Details</summary>

#### Tech stack

 Next.js 14 App Router + TypeScript + Tailwind. Supabase (availability calendar, bookings, user management). Stripe (payment + deposit holds). Canvas API + GSAP (wave animation hero). Resend (booking confirmation emails). Vercel (deployment).
 
#### Wave animation hero

 Canvas-based wave simulation: sinusoidal wave function with multiple overlapping waves, color transitions from deep blue to turquoise to white foam. Responds to scroll (waves intensify as user scrolls down). GSAP timeline controls the wave animation cycle.
 
#### Booking system architecture

 Camps table (id, name, location, capacity, price_per_person, start/end dates). Bookings table (id, camp_id, user_id, party_size, status, stripe_payment_id). Availability view (camp_id, date, spots_remaining — computed from capacity - booked). Atomic booking transaction: check availability → reserve → charge → confirm.
 
#### The key UX flow

 Availability calendar (visual month grid, color: available/limited/full) → Select dates → Party size → Real-time price calculation → Stripe checkout (with deposit hold, charge on confirmation) → Confirmation email → Booking dashboard.
 
#### Double-booking prevention

 Supabase transaction: BEGIN; SELECT ... FOR UPDATE; UPDATE availability; INSERT booking; COMMIT; The FOR UPDATE lock prevents two simultaneous bookings from both passing the availability check.
 
#### Portfolio value

 Combines: complex UI (canvas), real business logic (booking system), payments (Stripe), transactional DB (concurrent booking prevention). Shows full-stack thinking beyond CRUD apps.

</details>

Links: —

---

## 💡 10 Startup Ideas for 2026
**✅ GOOD** · _Opportunities, White Space, Build These_

10 startups that don't exist yet but will by 2026. Each one is a real gap — not "AI version of X," but fundamentally new products enabled by where AI actually is right now.

<details><summary>Details</summary>

#### Person + Productivity

 **1. AI Cofounder for Solo Builders** — not a chatbot. A thinking partner that knows your startup, remembers everything, and pushes back when you're wrong. Memory + context + disagreement = different from ChatGPT. **3. Life OS for Founders** — one system treating your personal life with the same seriousness as your startup: goals, energy, deep work, relationships, finances — all in one place. **7. AI That Makes You a Better Decision Maker** — doesn't give you answers. Slows you down, asks the right questions, helps you think clearly when emotions take over.
 
#### Health + Wellbeing

 **2. Burnout Prediction App** — reads your patterns (sleep, output, screen time) and warns you the week before you crash. Not a wellness app — a predictive alert system. **10. Digital Detox Without Burning Your Life Down** — a system that helps you step back from screen overload without disappearing from work, people, or presence.
 
#### Finance + Career

 **5. The Money App for Irregular Income** — built for founders and creators who don't have a salary: tracks runway, decisions, and the anxiety between them. **6. Community for People Building Hard Things Beautifully** — not hustle culture. Ambitious people who refuse to sacrifice everything else to get there.
 
#### Infrastructure + Future

 **4. AI Inbox That Acts, Not Just Filters** — reads context, drafts replies, follows up autonomously. An actual assistant, not another label system. **8. Reputation Layer for the AI Economy** — trust system for the world where half your coworkers, vendors, and collaborators are AI agents. **9. Personal API for Your Knowledge** — everything you've read, written, learned — searchable, connectable, usable. A second brain that actually works.
 
#### How to evaluate these

 Pick the one that makes you think "I would pay for this right now." That's your signal. Build the smallest version that proves the core value — don't try to build the whole vision first. Idea 9 (Personal API for Knowledge) is closest to what Obsidian Second Brain does — there's a product in there.

</details>

Links: —

---

## 🧊 3D Portfolio (akashrmalhotra)
**✅ GOOD** · _Three.js, Portfolio, Template_

3D animated developer portfolio website template devs can use as a starting point.

<details><summary>Details</summary>

350 stars. TypeScript. No listed topics — treat as a straightforward starter template, not a framework.

</details>

Links: [GitHub](https://github.com/akashrmalhotra/3d-portfolio)

---

## 💼 AI Job Hunter
**✅ GOOD** · _RAG, Firecrawl, Cover Letters, Portfolio AI, Difficulty: 7, 10_

Resume optimizer, LinkedIn profile review, portfolio feedback, job matching, auto-generated cover letters, interview prep. Full AI-powered job application stack — builds portfolio while solving a real problem.

<details><summary>Details</summary>

#### Stack

 Next.js, OpenAI (analysis + generation), Firecrawl (job listing scraper), RAG (match resume to job descriptions), Clerk (auth), Supabase (user data, applications tracker).
 
#### Feature build order

 1. **Resume analyzer** — upload PDF → Claude extracts skills, experience, gaps → gives feedback. 2. **Cover letter generator** — paste job description + your resume → personalized cover letter in your voice. 3. **Job matching** — Firecrawl scrapes job boards → embed job descriptions → match against your resume embeddings → ranked list. 4. **Portfolio reviewer** — enter your portfolio URL → Claude reviews it for target role. 5. **Interview prep** — paste job description → Claude generates likely questions + ideal answers based on your background.
 
#### Monetization angle

 Charge per cover letter ($1-2 each) or subscription ($15/mo for unlimited). Job hunters will pay — they're motivated and the value is clear.
 
#### Key learnings

 PDF parsing (mammoth or pdfjs). Structured generation (extract resume fields into JSON). Web scraping (Firecrawl). Semantic similarity (RAG for job matching). Personalization (maintaining user voice in generated content).

</details>

Links: —

---

## 💬 AI Study Buddy — Spaced Repetition
**✅ GOOD** · _SM-2, Flashcards, Adaptive Learning_

An AI-powered flashcard and spaced repetition system. Auto-generates cards from notes/textbooks, tracks performance with SM-2, surfaces due cards, and explains concepts in new ways when you struggle.

<details><summary>Details</summary>

#### What makes this different from Anki

 Anki requires manual card creation. This app: uploads your lecture notes/PDF → Claude generates cards automatically → SM-2 schedules reviews → when you can't recall, Claude explains the concept from a different angle, not just repeating the same text.
 
#### Card generation prompt

 "From this text, create 20 flashcards. For each concept: one question (front), one concise answer (back), and a related example. Focus on: definitions, relationships between concepts, application examples. Format as JSON array with {front, back, example, difficulty} fields."
 
#### SM-2 implementation

 For each card: store interval, easiness_factor, repetition_count. On review: user rates recall 0-5. Algorithm: if quality >= 3: interval = max(1, prev_interval * EF); EF = EF + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02) . Queue cards due today in review session.
 
#### AI explanation on failure

 When user rates < 3: "Explain [concept] from the card using a completely different approach. The original explanation wasn't working. Try: analogy, visualization, step-by-step breakdown, or real-world example." Claude adapts the explanation style to help retention.
 
#### Stack

 Next.js + Supabase (card storage + SM-2 data) + Claude API (card generation + explanations) + Framer Motion (card flip animation). Progressive Web App for mobile use.

</details>

Links: —

---

## 📱 Castimedia Portfolio (Antigravity 3-Phase)
**✅ GOOD** · _Agency Portfolio, Client Work, Showcase_

Agency-style portfolio using the full Antigravity/Atoms 3-phase interactive build. Project showcases with scroll animation, case study format, and client work presentation.

<details><summary>Details</summary>

#### Castimedia portfolio structure

 Hero: full-viewport canvas with scroll-driven image sequence of your work. Work section: project case studies with scroll reveals. Each case study: problem → process → solution → results. About: brief, personality-forward. Contact: simple, clear CTA.
 
#### Phase implementation order

 Phase 1: Static HTML structure and content. All typography, all copy, all project images. Get the message right before adding motion. Phase 2: Add GSAP scroll animations. Section reveals, text animations, image parallax. Phase 3: Interactive overlays. Mouse-following cursor effects. Project card tilt on hover. Final polish pass.
 
#### Case study format (converts best)

 Each project: 1-line outcome ("Increased conversion 40%"). Problem: what the client needed. Approach: what you did (3-4 bullets). Result: measurable outcome. Visuals: before/after or process screenshots. Tech stack used. Duration. Client quote (if you have one).
 
#### The canvas hero sequence

 60 frames showing your best work as a scroll-driven slideshow. Frame 1: overview shot. Frames 2-20: project A screens. Frames 21-40: project B. Frames 41-60: project C or your process. Export from Figma or After Effects.
 
#### Client-facing considerations

 Load time: under 3 seconds on 4G. Test with real clients' devices (often older Mac or Windows machines). Reduce sequence frame count if loading is slow. Add a text-based fallback for users who prefer to skip animation (prefers-reduced-motion media query).

</details>

Links: —

---

## 🧩 Chrome Extension — Productivity Tool
**✅ GOOD** · _Manifest V3, Content Scripts, AI_

Build a Chrome extension that adds AI capabilities to any website: summarize pages, highlight key concepts, save to Notion, generate email replies. Highly distributable portfolio piece.

<details><summary>Details</summary>

#### Ideas that are actually useful

 **Page summarizer**: Highlight any text → right-click → "Summarize with Claude" → floating summary appears. **Email assistant**: Gmail integration → read email thread → generate contextual reply drafts. **LinkedIn helper**: On any profile → generate personalized connection request or outreach. **Save to Notion**: Highlight → save with context → organized into Notion database. **Job analyzer**: On any job listing → analyze skills required → compare to your resume → highlight gaps.
 
#### Architecture for AI-powered extension

 Content script injects into page → captures user intent (selection, button click) → sends to background service worker → background calls Claude API (or your own backend to keep API key safe) → returns result → content script shows floating UI with result.
 
#### Keeping the API key safe

 NEVER put your API key in content scripts (visible to anyone who inspects the extension). Options: 1. User enters their own key in popup settings (stored in chrome.storage.local). 2. Route through your own backend (extension → your API route → Claude API). Option 2 is better for production.
 
#### Chrome Web Store submission

 $5 one-time developer fee. Zip the extension directory → upload. Review: 1-3 business days. Need: 3+ screenshots, privacy policy URL (simple privacy policy page), icon set (16/48/128px), clear description without spam keywords.
 
#### Distribution without store

 Share as a .crx or zip. Users install via Developer Mode → Load Unpacked. Simpler for internal tools or controlled distribution.

</details>

Links: —

---

## 🤖 Discord/Telegram Bot with Claude
**✅ GOOD** · _Bot Development, Community AI, Commands_

Build a community bot powered by Claude. Answer questions from your server's knowledge base, moderate content, generate content, run polls. Practical and highly distributable.

<details><summary>Details</summary>

#### Discord bot setup

 1. Create application at discord.com/developers. 2. Create bot → copy token. 3. npm install discord.js @anthropic-ai/sdk . 4. Listen to message events → if contains @bot mention or command prefix → send to Claude API → reply in thread.
 
#### Useful bot commands

 !ask [question] → Claude answers from server knowledge base. !summarize → summarize last 50 messages in channel. !explain [code] → explain code attached to message. !translate [text] to [language] . !mood → analyze the server's current vibe. !help → list commands.
 
#### RAG for server context

 Build a knowledge base from: server rules, FAQs, documentation. Embed and index in ChromaDB. When !ask is used: retrieve relevant context → inject into Claude prompt → answer grounded in server-specific knowledge.
 
#### Rate limiting (essential)

 const userLimits = new Map(); Track per-user request count per minute. If > 10 requests/minute: reply "Rate limited, try again in a minute." Without this: one user can drain your Claude API credits instantly.
 
#### Deployment

 Railway.app: $5/month, persistent Node.js process. The bot needs to always be running (unlike web apps that respond to requests). Railway keeps it alive 24/7.
 
#### Telegram alternative

 Telegram bots: simpler API (python-telegram-bot library), no $5 developer fee, bot creation via @BotFather. Better for: personal tools, smaller communities. Discord better for: larger communities, gaming/tech communities.

</details>

Links: —

---

## 🏗️ ECC — Elliptic Curve Cryptography
**✅ GOOD** · _Cryptography, Python, Math_

Implement Elliptic Curve Cryptography from scratch in Python. ECDH key exchange, ECDSA signing, secp256k1 curve. Demonstrates deep CS fundamentals and mathematical rigor.

<details><summary>Details</summary>

#### Why ECC matters

 ECC is used in: Bitcoin (secp256k1), TLS/HTTPS (key exchange), Signal (messaging encryption), SSH (key authentication). Understanding it gives you: cryptographic intuition, real-world security knowledge, and demonstrates strong CS fundamentals.
 
#### Core math to implement

 Point addition on elliptic curve (over finite field Fp). Scalar multiplication (fast via double-and-add algorithm). Group operations: identity element (point at infinity), inverse, order. secp256k1 curve: y² = x³ + 7 over Fp where p = 2²⁵⁶ - 2³² - 977.
 
#### ECDH key exchange

 Alice: private_key_a = random 256-bit integer
 public_key_A = private_key_a * G # G = generator point

Bob: private_key_b = random 256-bit integer
 public_key_B = private_key_b * G

Shared secret = private_key_a * public_key_B
 = private_key_b * public_key_A
 = private_key_a * private_key_b * G 
 
#### ECDSA signing

 Sign: k = random, r = (k*G).x, s = k⁻¹ * (hash + r * private_key) mod n. Verify: (hash * s⁻¹) * G + (r * s⁻¹) * public_key = (r, ?). If x-coordinate matches r, signature valid.
 
#### Learning resources

 "Programming Bitcoin" by Jimmy Song — best technical book on ECC/Bitcoin implementation. "An Introduction to Mathematical Cryptography" — rigorous math. Implementing secp256k1 from scratch in Python is a multi-week project with strong portfolio value for security-focused roles.

</details>

Links: [ECC repo](https://github.com/affaan-m/ECC)

---

## 🎯 LoRA Fine-Tuning Project
**✅ GOOD** · _ML, HuggingFace, Custom Model_

Fine-tune a language model on your own data using LoRA (Low-Rank Adaptation). Much cheaper than full fine-tuning. Deploy on HuggingFace Spaces. Strong ML portfolio project.

<details><summary>Details</summary>

#### What LoRA is

 LoRA adds small trainable matrices to frozen model weights. Instead of updating 7B parameters, you update ~1-10M adapter parameters. Training: 10-100x cheaper and faster than full fine-tuning. Inference: adapters can be swapped at runtime — same base model, different behaviors for different tasks.
 
#### Tools

 pip install transformers peft datasets trl accelerate bitsandbytes . PEFT (Parameter Efficient Fine-Tuning) from HuggingFace implements LoRA. TRL (Transformer Reinforcement Learning) for instruction fine-tuning workflows.
 
#### Dataset preparation

 Format as instruction-response pairs: {"instruction": "...", "response": "..."} . Minimum: 500-1000 examples. Ideal: 2000-5000 high-quality examples. Quality >> quantity — 500 perfect examples beats 5000 noisy ones. Data format: JSON Lines (.jsonl), one example per line.
 
#### Recommended base models

 Mistral 7B or Llama 3 8B (small enough to fine-tune on consumer GPU or Google Colab Pro). Phi-3 Mini (very small, fine-tunes on free Colab). Use Colab T4 (free) or A100 (Colab Pro) for training.
 
#### Training time

 1000 examples, 3 epochs, Mistral 7B, T4 GPU: ~2-4 hours. Save checkpoints every 100 steps. Monitor training loss — should decrease steadily. If it spikes or plateaus early: reduce learning rate.
 
#### Portfolio application

 Fine-tune on: your writing style (personal AI), a specialized domain (legal, medical, technical), a specific task (code review, recipe generation). Deploy on HuggingFace Spaces for a live demo recruiters can try.

</details>

Links: —

---

## 🔧 Open Source Agent Builder
**✅ GOOD** · _LangGraph, MCP, Docker, Multi-model, Difficulty: 9, 10_

Visual agent builder. Swap LLMs, configure tools, manage memory and prompt playground, deploy with one click. The hardest project on the list — also the most impressive for a portfolio or productization.

<details><summary>Details</summary>

#### Stack

 Next.js (visual builder UI), LangGraph (agent orchestration), OpenAI + Claude + Gemini support, MCP (tool integration), Docker (deployment), Redis (session state), PostgreSQL (persistence).
 
#### Core features

 **Visual builder** — drag-drop agent graph: nodes = steps, edges = conditions. **LLM swapper** — configure which model handles each node (e.g., Claude for reasoning, Gemini for multimodal). **Tool configurator** — add MCP servers as tools via UI, no code. **Memory panel** — configure memory type (in-context, vector, summary). **Prompt playground** — test system prompts live. **One-click deploy** — package agent as Docker container, deploy to Fly.io.
 
#### Key learnings

 Agent orchestration patterns (sequential, parallel, conditional branching). MCP protocol implementation. Multi-model routing. State machine architecture for agents. Production AI deployment.
 
#### Start minimal

 V1: text-based config (YAML), single model, 2-3 pre-built tools. V2: visual builder. V3: multi-model. Don't try to build all three phases at once.

</details>

Links: —

---

## 📊 Personal Analytics Dashboard
**✅ GOOD** · _Data Viz, API Integration, Self-Tracking_

A self-tracking dashboard pulling from: GitHub (contributions), Spotify (listening habits), fitness tracker, finances, habits, productivity apps. AI generates weekly insights and identifies patterns.

<details><summary>Details</summary>

#### Data sources to integrate

 GitHub API (commits, PRs, contributions), Spotify API (listening history, top artists), Strava/Fitbit/Apple Health (fitness data via export), Toggl/Clockify (time tracking), financial data (Plaid API for accounts or manual CSV import), habit tracker (Beeminder or custom).
 
#### Tech stack

 Next.js dashboard, Supabase for data storage, Recharts or Tremor for visualization, scheduled Vercel cron jobs for data sync. Data pipeline: cron → fetch from APIs → normalize → store in Supabase → dashboard queries Supabase.
 
#### AI insights layer

 Weekly: "Analyze my activity data from this week. Find: 1) my most productive days/times, 2) correlations between sleep/exercise and productivity, 3) patterns in my music listening that correlate with focus. Suggest one change based on the data." Claude reads the past 7 days of data and generates a personal insight report.
 
#### Interesting correlations to look for

 Sleep hours vs GitHub commits the next day. Exercise frequency vs productivity score. Spotify genre vs coding time. Coffee consumption vs error rate in commits (if you track both). These personal correlations are genuinely interesting and can change your habits.
 
#### Portfolio value

 Shows: API integration (multiple external APIs), data pipeline design, visualization, AI analytics, cron jobs, personal initiative. Unique because it's personal — you can actually talk to it in interviews.

</details>

Links: —

---

## 📰 Personalized AI News Agent
**✅ GOOD** · _Firecrawl, Trigger.dev, Tavily, Email, Difficulty: 6, 10_

Reads hundreds of articles, learns your interests, sends a daily digest with explanations of why each story matters. Agentic workflows, scheduling, and email automation in one project.

<details><summary>Details</summary>

#### Stack

 Firecrawl (web scraping), OpenAI (summarization + personalization), Trigger.dev or Inngest (scheduled jobs), Tavily (search), Resend (email delivery).
 
#### Architecture

 1. **Source crawler** — Firecrawl scrapes RSS feeds + selected sites daily. 2. **Relevance scorer** — score each article against user interest profile. 3. **Summarizer** — generate TL;DR + "why this matters" for top articles. 4. **Digest composer** — group by topic, format email. 5. **Scheduler** — Trigger.dev cron job at 7am daily. 6. **Email sender** — Resend with HTML template.
 
#### Personalization

 Start: user selects topics on signup. Improve: track click-through on digest links → update interest profile. Advanced: embed articles and user's clicks → semantic similarity scoring.
 
#### Key learnings

 Scheduled agent workflows (cron + long-running jobs). Web scraping at scale. Tool calling (agent decides what to search for). Summarization with structured output. Email HTML templates.
 
#### MVP scope

 3 hard-coded news sources, 5 topics to choose from, email sent at 7am. Ship this in a weekend, add personalization later.

</details>

Links: —

---

## 🎮 HuggingFace Portfolio Trick
**🤔 MAYBE** · _Free GPU, Spaces, Model Demo_

Deploy ML project demos on HuggingFace Spaces for free. GPU-backed demos that let recruiters interact with your ML work directly. Gradio or Streamlit UI in minutes.

<details><summary>Details</summary>

#### What HuggingFace Spaces gives you

 Free hosting for ML demos with: CPU instances (always free), GPU instances (ZeroGPU free tier for community models, paid for persistent). Gradio UI builder (10 lines of Python → interactive ML demo). Persistent storage. Public URL you can share.
 
#### Fastest path to a demo

 import gradio as gr
from transformers import pipeline

pipe = pipeline("text-generation", model="your-fine-tuned-model")

def generate(prompt):
 return pipe(prompt, max_length=200)[0]['generated_text']

gr.Interface(fn=generate, inputs="text", outputs="text").launch() 
 That's a complete Gradio demo. Push to HuggingFace Spaces → live at huggingface.co/spaces/your-name/demo-name.
 
#### The portfolio trick

 Fine-tune a model on a niche dataset → upload to HuggingFace Hub → create Space with Gradio demo → link in portfolio and resume. Recruiters can click and actually use your ML project. This is rare — most candidates only have GitHub code with no live demo.
 
#### Best demo types

 Text classifier (sentiment, topic, spam detection), text generator (fine-tuned on your writing), image classifier (trained on interesting dataset), question answering over documents, text summarizer.
 
#### Combining with portfolio site

 Embed the HuggingFace Space iframe in your portfolio page. Or: link from portfolio → HuggingFace Space. Either way, it's live and interactive. Frame it as a deployed ML API, not just a script.

</details>

Links: [HuggingFace Spaces](https://huggingface.co/spaces)

---
