# AI Tools

[← back to index](../README.md)

14 resources.

## 🖱️ Cursor IDE
**🔥 MUST USE** · _AI-Native Code Editor, Best for Production_

The best AI code editor. VS Code fork with Claude/GPT-4 built in. Tab completion that understands your whole codebase. Agent mode for multi-file changes. Use this for serious projects.

<details><summary>Details</summary>

#### Essential keybinds

 Cmd+K — inline edit (select code → describe change). Cmd+L — open chat sidebar. Cmd+Shift+L — add selected code to chat context. Tab — accept AI suggestion. Cmd+I — composer (multi-file agent mode). These 5 cover 90% of usage.
 
#### .cursorrules setup

 Create .cursorrules in root of every project. Content: your stack, conventions, what NOT to do. Example:
 You are a TypeScript/React expert.
Stack: Next.js 14 App Router, Tailwind, shadcn/ui, Supabase.
Rules:
- Always use TypeScript with strict types
- Server components by default, 'use client' only when needed
- Never use useEffect for data fetching — use server components
- Always handle loading and error states
- Use Zod for all form validation 
 
#### Context management (the key skill)

 Cursor reads your @codebase but struggles with large codebases without guidance. Use @filename to pin specific files. Use @docs to add documentation URLs. Keep chat conversations short — start new chat for new tasks. Long context degrades quality.
 
#### Agent mode (Composer)

 Cmd+I → describe a feature → Cursor creates/edits multiple files autonomously. Best for: new feature scaffolding, refactoring, adding tests. Review diffs carefully before accepting — it can break things outside your specified scope.
 
#### Pricing

 Free: 2000 completions, 50 slow requests. **Pro $20/month**: unlimited completions, 500 fast requests (GPT-4o/Claude). Worth every dollar if you code daily.
 
#### Common mistakes

 Don't: let agent mode run without reviewing. Don't: forget to update .cursorrules when you make architectural decisions. Don't: use Cursor for tiny edits where Cmd+K is faster than opening chat.

</details>

Links: [cursor.com](https://cursor.com)

---

## 🎨 Gamma.app
**🔥 MUST USE** · _AI Presentations, Decks, Docs_

AI-generated slide decks, documents, and webpages in under 2 minutes. Paste an outline → full presentation with design. Best for rapid decks you'd otherwise spend hours in Google Slides.

<details><summary>Details</summary>

#### The fastest workflow

 1. Open Gamma → "Create new" → "Generate" → paste a bullet-point outline. 2. Choose theme (dark/light, color palette). 3. Gamma generates full deck in ~60 seconds. 4. Click any card to edit text/swap images. 5. Export as PDF or share link. Total time: under 5 minutes for a polished deck.
 
#### Prompt strategies that work

 **Bad prompt**: "Make slides about my startup." **Good prompt**: "Create a 10-slide pitch deck for a B2B SaaS tool that helps small law firms automate client intake. Audience: angel investors. Tone: confident, data-driven. Include: problem, solution, market size, traction, team, ask." The more context, the better the output.
 
#### Import from existing content

 Paste a Google Doc → Gamma structures it into slides. Upload a PDF → Gamma converts to web page. Great for converting boring reports into shareable interactive docs.
 
#### Templates to use

 "Pitch Deck" template → investor-ready structure. "One-Pager" → executive summary page. "Proposal" → client proposals with pricing sections. Start from these rather than blank.
 
#### Pricing

 Free: 400 AI credits (each generation uses ~40). **Plus $10/month**: unlimited generations, custom domains, analytics. Worth it if you make decks weekly.
 
#### What Gamma can't do

 Complex custom animations, pixel-perfect brand design, complex data visualizations. For those: use PowerPoint/Keynote. Use Gamma for speed, not perfection.

</details>

Links: [gamma.app](https://gamma.app)

---

## 💜 Lovable.dev
**🔥 MUST USE** · _Full-Stack App Builder, Ship Fast_

AI-generated full-stack apps from a description. React + Supabase + Tailwind + shadcn/ui. Deploy to lovable.dev subdomain instantly. Best for: MVPs, hackathons, client demos.

<details><summary>Details</summary>

#### The build flow

 1. Describe your app in detail: "Build a task manager with user auth, projects, tasks with due dates, priority levels, and a kanban board view. Use Supabase for the DB." 2. Lovable generates the full codebase in ~2 minutes. 3. Connect your Supabase project. 4. Preview live. 5. Iterate by describing changes in plain English: "Add a dark mode toggle" or "Make the kanban cards draggable."
 
#### Prompting for quality

 **Always specify**: tech stack preferences, auth method, data model, key pages/views, UI style (clean/minimal, feature-rich, etc). **Reference example apps**: "Make it look like Linear but for X." **Iterate in small steps**: don't try to describe the entire app in one prompt — build feature by feature.
 
#### Supabase integration

 Connect your own Supabase project in Settings → Integrations. Lovable auto-creates tables, sets up RLS policies, and wires auth. Always review the generated RLS policies — they're usually correct but check before going live.
 
#### GitHub sync

 Push your Lovable project to GitHub. Then use Cursor or Claude Code to make complex changes the AI builder can't handle. This is the killer workflow: Lovable for scaffolding, Cursor for precision.
 
#### Pricing

 Free: 5 messages. **Starter $20/month**: 100 messages. **Launch $50/month**: unlimited. Each "message" is one build iteration. Complex apps use 10-30 messages to get right.
 
#### What Lovable struggles with

 Complex state management, real-time features, custom animations, backend logic beyond basic CRUD. When you hit these walls, export to GitHub and finish in Cursor.

</details>

Links: [lovable.dev](https://lovable.dev)

---

## 📱 Mobbin
**🔥 MUST USE** · _Mobile UI Reference, App Screens, Patterns_

50,000+ real mobile app screens organized by pattern, industry, and element. The best UI reference for mobile design. Screenshot → paste into V0/Lovable as reference.

<details><summary>Details</summary>

#### How to use it in your workflow

 1. Find the pattern you need (onboarding, dashboard, settings, auth, etc.). 2. Filter by industry (fintech, health, social). 3. Screenshot the screens you like. 4. Open V0 → drag + drop screenshot → "Build a component inspired by this layout with [your content and colors]." This is 10x faster than describing UI from scratch.
 
#### Best pattern categories

 **Onboarding flows**: How top apps handle first-run experience. **Auth screens**: Login, signup, forgot password patterns. **Empty states**: What apps show when there's no data — often overlooked. **Settings**: Options, toggles, lists. **Cards & feeds**: List/card content layouts. **Navigation**: Bottom tabs, drawers, top nav patterns.
 
#### Search strategies

 Search by: element name ("bottom sheet", "search bar", "onboarding"), action ("sign up", "checkout"), industry ("banking", "fitness"). You can also browse by app — search "Notion" to see all Notion screens, "Linear" for Linear patterns.
 
#### Save to collections

 Create a collection for each project. Save screens as you find inspiration. Refer back during design review.
 
#### Pricing

 Free: limited browsing. **Pro $14/month**: full access to all 50k+ screens, download originals, team collections. Worth it if you design mobile interfaces regularly.
 
#### Alternative

 Screenlane (web-focused), Dribbble (more polished/conceptual, less real-world). Mobbin is best for real production app patterns.

</details>

Links: [mobbin.com](https://mobbin.com)

---

## 📓 NotebookLM
**🔥 MUST USE** · _AI Research, Podcast Gen, Source Grounding_

Google's AI notebook that reads your sources and answers questions based only on them. Best feature: generates a podcast-style audio overview of any document set. Zero hallucination.

<details><summary>Details</summary>

#### Core workflow

 1. Create a new notebook. 2. Upload sources: PDFs, Google Docs, YouTube URLs, web URLs (up to 50 sources, 500k words each). 3. Ask questions — answers are 100% grounded in your sources with citations. 4. Generate audio overview (2 hosts discussing your material) — great for passive learning while commuting.
 
#### Best use cases

 **Research papers**: Upload 10 papers → "What are the key findings across these papers? Where do they disagree?" **Course material**: Upload lecture slides, readings → "Create a study guide covering the main concepts." **Textbooks**: Upload chapters → generate audio summaries to listen to while commuting. **Meeting prep**: Upload company docs → "What should I know before this meeting?"
 
#### Audio overview trick

 Click "Generate" → Audio Overview → two AI hosts synthesize your entire source set into a conversational podcast. You can customize focus: "Focus on practical applications" or "Focus on the debate between X and Y." Takes 2-3 minutes to generate. Listen at 1.5x speed.
 
#### Study cards

 Ask: "Create 20 flashcard-style Q&A pairs for the key concepts in these documents." Paste output into Anki or any spaced repetition app.
 
#### Limitations

 No web browsing (unless you add URLs as sources), can't process images within PDFs deeply, no code execution. Works best for text-heavy research.
 
#### Pricing

 Completely free. Part of Google Labs. No subscription needed.

</details>

Links: [notebooklm.google.com](https://notebooklm.google.com)

---

## 🔍 Perplexity AI
**🔥 MUST USE** · _AI Search, Research, Citations_

AI-powered search that cites sources. Replaces Google for any research-heavy query. Pro unlocks GPT-4o, Claude, and deep research mode.

<details><summary>Details</summary>

#### When to use Perplexity vs Google

 Use Perplexity for: "What's the best way to implement X in 2025?", "Explain how Y works with current context", "Compare tool A vs B", "Find recent news about Z". Use Google for: exact URLs, shopping, local search, very specific known-answer lookups. Perplexity synthesizes; Google indexes.
 
#### Power query formats

 **Deep Research mode** (Pro): "Write a comprehensive analysis of [topic] including recent developments, key players, and practical implications." Takes 2-3 min, produces 2000-word sourced report. **Code questions**: "How do I implement streaming responses in Next.js App Router with Anthropic Claude? Show current 2025 patterns." Gets you up-to-date answers vs stale StackOverflow posts. **Comparison**: "Compare Supabase vs Firebase for a solo developer building a SaaS in 2025. Include pricing, DX, scalability."
 
#### Perplexity Spaces

 Create a Space for any ongoing project. Upload docs, set context, invite collaborators. All searches within the space are grounded in your uploaded materials. Useful for: research projects, company-specific queries, topic deep-dives.
 
#### Pricing

 Free: unlimited basic search (GPT-3.5 level). **Pro $20/month**: GPT-4o, Claude Sonnet, Deep Research (5/day free, unlimited Pro), image gen, file uploads. Worth it if you search 20+ times/day for complex topics.
 
#### What to avoid

 Don't use for: math calculations (use Wolfram), real-time stock prices, anything requiring login (it can't authenticate). Citations are usually accurate but occasionally hallucinated — verify critical claims.
 
#### Workflow integration

 Use as first stop before starting any new project. 15-minute Perplexity research session → paste findings into Claude for synthesis + planning. Saves hours of scattered Googling.

</details>

Links: [perplexity.ai](https://perplexity.ai)

---

## 🌊 Windsurf (Codeium)
**🔥 MUST USE** · _AI IDE, Cascade Agent, Free Tier_

Cursor's main competitor from Codeium. Cascade AI agent has deeper multi-file awareness. Better free tier than Cursor. Use when Cursor hits its limits.

<details><summary>Details</summary>

#### Windsurf vs Cursor

 **Windsurf advantages**: Better free tier (no request limit on basic), Cascade agent is more "aware" of full project context, slightly better at understanding large codebases. **Cursor advantages**: More mature, better keybind customization, .cursorrules file support, larger community. Use both: Windsurf when your Cursor Pro requests run out, or for large codebase refactors.
 
#### Cascade agent

 Cascade (Windsurf's agent) proactively understands your codebase without you specifying files. Tell it: "Refactor the authentication flow to use Supabase Auth v2" → it finds all relevant files, understands dependencies, makes coordinated changes. More autonomous than Cursor's Composer.
 
#### Flows (Windsurf's .cursorrules equivalent)

 Settings → Windsurf Rules → add your project conventions. Same concept as .cursorrules — establish your stack, conventions, forbidden patterns.
 
#### Best use case

 Large refactors where you need the agent to find all affected files. "Rename the User model to Account everywhere in the codebase, update all references, types, API routes, and DB queries." Cascade handles this better than most tools.
 
#### Pricing

 Free: 25 Cascade actions/day. **Pro $15/month**: 90 Cascade actions/day + priority access. Cheaper than Cursor Pro.
 
#### When to stick with Cursor

 Day-to-day coding, inline edits, when you want precise control. Windsurf's autonomy is great but sometimes surprising — it touches things you didn't ask it to.

</details>

Links: [windsurf.com](https://windsurf.com)

---

## 🪄 21st.dev Magic MCP
**✅ GOOD** · _UI Component Search, MCP for Claude_

MCP server that lets Claude search and use UI components from 21st.dev's library. Say "add a pricing table" → Claude fetches the exact component and inserts it. Design system integration built in.

<details><summary>Details</summary>

#### What it does

 21st.dev Magic MCP connects Claude Code to the 21st.dev component library. When you ask Claude to add a UI component, instead of hallucinating code, it searches the curated library and returns the exact component code. Guarantees production-quality output.
 
#### Install

 Add to Claude Code MCP config:
 "21st-magic": {
 "command": "npx",
 "args": ["-y", "@21st-dev/magic@latest"],
 "env": { "API_KEY": "your-key" }
} 
 Get API key from 21st.dev.
 
#### How to use

 In Claude Code: "Add a responsive pricing table with 3 tiers using 21st.dev." Claude searches the library → fetches the component → integrates it into your project with your color scheme. You can also say "find me a sidebar navigation" or "use a data table component."
 
#### Best components available

 Pricing tables, data tables, kanban boards, sidebars, modals, command palettes, dashboards, auth forms. Saved hours vs writing from scratch.
 
#### Integration with design system

 Components are built with shadcn/ui + Tailwind, so they inherit your existing CSS variables automatically. No theme conflicts.

</details>

Links: [21st.dev](https://21st.dev)

---

## 🖼️ Google Whisk → ezgif Pipeline
**✅ GOOD** · _AI Image Blending, Portfolio Visuals_

Blend 3 reference images into a new AI-generated image. Subject + Scene + Style → output. Then animate with ezgif. Portfolio-grade visuals in under 5 minutes.

<details><summary>Details</summary>

#### Full pipeline step-by-step

 1. Go to labs.google.com/whisk. 2. **Subject**: upload a reference image of the subject (person, object). 3. **Scene**: upload a scene/background image. 4. **Style**: upload a style reference (artwork, photo style). 5. Click Generate → Whisk creates a new image blending all 3 inputs. 6. Iterate by swapping inputs or using text prompt in "Refine" field. 7. Download the generated image.
 
#### Best combinations

 Portrait photo (subject) + architectural interior (scene) + dramatic photography (style) → editorial-quality portrait. Product photo (subject) + white studio (scene) + product photography style → e-commerce hero shot. Character art (subject) + landscape (scene) + cinematic film still (style) → concept art.
 
#### Text refinement prompts

 After initial generation, add text prompts to refine: "cinematic lighting", "8k ultra detailed", "photorealistic", "golden hour", "minimalist". Keep refinements short — one style direction at a time.
 
#### ezgif animation

 Take 3-5 Whisk outputs of the same subject → upload to ezgif.com → create GIF or WebP animation. Use for: portfolio hero animations, product showcases, social media content.
 
#### Portfolio deployment

 Use Whisk outputs as hero images on your portfolio. Much more distinctive than stock photos. Pair with mouse-scrub interaction (from Atoms techniques) for portfolio wow-factor.
 
#### Pricing

 Google Whisk: free (Google Labs). ezgif: free.

</details>

Links: [Google Whisk](https://labs.google.com/whisk) · [ezgif.com](https://ezgif.com)

---

## 🤖 Manus AI
**✅ GOOD** · _Autonomous Agent, Multi-Step Tasks_

General-purpose autonomous AI agent that browses the web, writes code, and completes multi-step tasks end-to-end. Give it a task and walk away.

<details><summary>Details</summary>

#### What Manus actually does

 Manus is a fully autonomous agent: it opens a browser, searches the web, reads pages, writes and executes code, creates files, and completes goals end-to-end without step-by-step supervision. Think of it as an AI intern who can work independently for 15-60 minute stretches.
 
#### Best task types

 **Research + report**: "Research the top 10 venture capital firms investing in AI startups in 2025. Create a report with each firm's focus area, recent investments, and how to contact them." **Data collection**: "Find all YC companies from the S24 batch focused on developer tools. Compile their names, founders, and LinkedIn URLs." **Code tasks**: "Write a Python script that fetches cryptocurrency prices every hour and sends a Telegram alert if any drop 10%." **Content**: "Write 5 LinkedIn posts about AI productivity tools targeting software engineers."
 
#### How to prompt Manus

 Be specific about the output format: "Create a CSV with columns: Name, Website, Founder, Category, Funding Stage." The more specific your output requirements, the better. Give it a goal, not a series of steps — Manus figures out the steps.
 
#### Monitoring

 You can watch Manus work in real-time — it shows its browser, terminal, and reasoning. This is useful for complex tasks to course-correct early if it goes off track.
 
#### Pricing

 Currently invite-based / limited access. Check manus.ai for current availability.
 
#### When to use vs Claude Code

 Manus: when you want full autonomy and don't want to supervise. Claude Code: when you want to be in the loop and the task is code-specific. Manus is better for research + web scraping; Claude Code for actual software development.

</details>

Links: [manus.ai](https://manus.ai)

---

## 🔎 Perplexity Deep Research
**✅ GOOD** · _Multi-Source Research, Long-Form Reports_

Perplexity's extended research mode. Searches 20+ sources, synthesizes into a 2000+ word structured report with full citations. Takes 2-3 min. Replaces hours of manual research.

<details><summary>Details</summary>

#### How to trigger Deep Research

 In Perplexity Pro: click the "Deep Research" button before searching, or type "deep research:" before your query. It will show a progress indicator as it searches multiple sources.
 
#### Best query formats

 "Deep research: Comprehensive overview of [topic] including current state, key players, challenges, and future direction." "Deep research: Compare [A] vs [B] for [specific use case]. Include pricing, technical specs, community size, and real-world performance data." "Deep research: What are the most promising approaches to [problem] in 2025? Include academic research and industry implementations."
 
#### Output quality

 Reports include: executive summary, detailed sections with subsections, comparison tables, citations for every claim. Quality varies — better for technical/scientific topics than subjective opinion pieces.
 
#### Integration with Claude

 Run Deep Research → copy the full report → paste into Claude: "Here's a research report on [topic]. Based on this, help me create an action plan for [specific goal]." Claude synthesizes the sourced facts into personalized guidance.
 
#### Pricing

 Pro plan required ($20/month). Free users get ~5 Deep Research queries/day as a sample.
 
#### Alternatives

 ChatGPT Deep Research (OpenAI Pro, $200/month), Gemini Deep Research (Google One AI). Perplexity is cheapest for research at $20/month. OpenAI's version is more thorough but 10x more expensive.

</details>

Links: [perplexity.ai](https://perplexity.ai)

---

## ✨ ReactBits
**✅ GOOD** · _Animated React Components, Copy-Paste_

Library of animated, interactive React components you copy-paste into projects. Particles, text effects, card animations, backgrounds. Elevates UI from bland to impressive instantly.

<details><summary>Details</summary>

#### Best components to use

 **Backgrounds**: Aurora (colorful gradient), Particles (interactive dots), Grid (subtle grid overlay). **Text effects**: Split text, gradient text, scramble text. **Cards**: Tilting card, spotlight card, glass card. **Buttons**: Magnetic, shimmer, gooey. **Loaders**: Dot loaders, ring loaders, progress bars.
 
#### Integration workflow

 1. Browse reactbits.dev → find component. 2. Click "Code" tab → copy the component code. 3. Create file in your project → paste. 4. Adjust colors/sizing to match your design system. 5. Import and use. Most components have zero dependencies or use framer-motion (which Lovable and V0 projects include by default).
 
#### Framer Motion dependency

 Most ReactBits components use Framer Motion. Install: npm install framer-motion . Already included in Lovable and most AI-generated projects. This is a production-quality animation library — not bloat.
 
#### Customization tips

 All components expose props for customization. Change colors to match your CSS variables. Adjust speed/intensity via props (most have a `speed` or `intensity` prop). Don't use everything at once — pick 1-2 effects per page max.
 
#### What to avoid

 Don't use particle backgrounds + spinning loaders + 3 animated text effects on the same page. More ≠ better. One signature effect per page, done well.
 
#### Performance note

 Canvas-based animations (particles, aurora) can impact performance on low-end devices. Use `prefers-reduced-motion` media query to disable for accessibility.

</details>

Links: [reactbits.dev](https://reactbits.dev)

---

## 🎙️ Wispr Flow
**✅ GOOD** · _AI Dictation, Voice-to-Text, Any App_

Dictate in any text field on Mac. Press hotkey → speak → AI transcribes + polishes in real-time. Faster than typing for anything over 50 words. Works everywhere: Cursor, Claude, email, Notion.

<details><summary>Details</summary>

#### Setup

 1. Download Wispr Flow (Mac only). 2. Set hotkey (default: hold Option). 3. Click any text field → hold your hotkey → speak naturally → release → text appears. Works in: Cursor chat, Claude.ai, Notion, Gmail, VS Code comments, Slack, literally anywhere.
 
#### Speaking naturally

 Say "new line" → inserts \n. Say "period" or "question mark" → punctuation. Say "comma" → comma. No need to speak like a robot. Just talk conversationally — Wispr handles punctuation and capitalization automatically.
 
#### Best use cases

 **Long Claude prompts**: Dictate complex prompts instead of typing. Faster and more conversational. **Code comments**: Dictate detailed explanations. **Emails**: Dictate drafts, then edit. **Slack messages**: Faster for long updates. **Journal entries**: Voice → text in Notion or Obsidian.
 
#### Accuracy

 Near-perfect for clear speech. Struggles with: technical jargon (use "spell out" mode), heavy accents, background noise. Keep a quiet environment for best results.
 
#### Pricing

 Free: 5 min/day. **$10/month**: unlimited. Worth it if you dictate daily — saves 30-60 min/week in typing time.
 
#### Alternatives

 MacOS built-in dictation (free, worse accuracy), Otter.ai (better for meetings/transcription), Superwhisper (similar, also good).

</details>

Links: [wisprflow.com](https://wisprflow.com)

---

## 🌱 Sprout / Jobsuit
**🤔 MAYBE** · _Job Search AI, Application Automation_

AI tools for job searching: resume tailoring, application tracking, cover letter gen. Useful during active job search but not day-to-day. Try when actively applying.

<details><summary>Details</summary>

#### What these tools do

 **Sprout**: Analyzes job descriptions → suggests resume edits to match keywords → ATS optimization. **Jobsuit**: Tailors resume to each specific job description automatically. Both tools help you pass ATS (Applicant Tracking Systems) that filter resumes before a human sees them.
 
#### ATS optimization basics (regardless of tool)

 Match keywords from the job description exactly. If the JD says "React.js", your resume should say "React.js" not "ReactJS." ATS is keyword matching, not semantic understanding. Use: standard section headers (Experience, Education, Skills), .docx format, no tables/columns, no images.
 
#### Cover letter gen workflow

 1. Paste job description into Claude. 2. Paste your resume. 3. "Write a cover letter for this role based on my resume. Highlight [specific achievement] as most relevant. Tone: confident and specific, not generic." Better than using Sprout's template output.
 
#### When to use vs just using Claude

 These tools are wrappers around Claude/GPT prompts. For one-off applications: just use Claude directly. For bulk applications (10+ at once): these tools save time with automation. Evaluate on the volume of applications you're sending.
 
#### Pricing

 Both have free tiers. Sprout Pro ~$20/month. Try free tier first — it may be sufficient.

</details>

Links: —

---
