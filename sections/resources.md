# Resources

[← back to index](../README.md)

15 resources.

## 🎥 Andrej Karpathy — YouTube & Writing
**🔥 MUST USE** · _Deep ML Understanding, Neural Networks_

Best ML educator alive. "Neural Networks: Zero to Hero" builds GPT from scratch. Watching this changes how you think about language models. Non-negotiable if you want to understand AI deeply.

<details><summary>Details</summary>

#### Neural Networks: Zero to Hero (YouTube series)

 8 videos, ~25 hours total. Builds progressively: micrograd (backprop in 100 lines of Python) → makemore (bigram language model) → makemore with MLP → makemore with BatchNorm → WaveNet → GPT from scratch. By the end you understand exactly how ChatGPT and Claude work at the mechanism level.
 
#### The single most important video

 "Let's build GPT: from scratch, in code, spelled out" — 2 hours. Implements the transformer architecture from "Attention Is All You Need" paper in PyTorch, explaining every line. After watching this once (and again): the mystery of how LLMs work disappears. Watch at 1x speed, pause and code along.
 
#### State of GPT (Microsoft Build talk)

 YouTube search: "Karpathy State of GPT". 1-hour talk on how GPT models are trained: pre-training, RLHF, how instruction-following works, how to prompt effectively based on how the model was trained. The best 1-hour intro to LLM fundamentals that actually explains the training process.
 
#### CLAUDE.md insight

 Karpathy publicly stated his CLAUDE.md file took his Claude coding accuracy from ~65% to ~94%. This single data point popularized project-level AI context files across the industry. The actual file structure he recommends: tech stack, conventions, what NOT to do, key file locations.
 
#### His X/Twitter (@karpathy)

 Regular commentary on new research, practical takes on AI tools, observations on how LLMs work. Worth following for: staying current on LLM research, getting the actual-practitioner perspective (not hype), his thread on AI-assisted coding workflows is excellent.

</details>

Links: [YouTube](https://www.youtube.com/@AndrejKarpathy) · [@karpathy](https://x.com/karpathy)

---

## 📖 Anthropic Documentation
**🔥 MUST USE** · _Claude API, Prompt Engineering, Agent SDK_

Primary reference for everything Claude. Prompt engineering guide, API reference, tool use, extended thinking, agent SDK. Read the prompt engineering section once properly.

<details><summary>Details</summary>

#### Most valuable pages

 **Prompt Engineering Overview** (docs.anthropic.com/en/docs/build-with-claude/prompt-engineering): XML tagging, chain-of-thought, role setting, few-shot examples — read top to bottom once. **Tool Use**: how to give Claude callable functions. Essential for agents. **Extended Thinking**: activates Claude's step-by-step reasoning mode for complex problems. **Prompt Caching**: cache repeated system prompts at 10% of normal input price — saves significantly on API-heavy apps.
 
#### Prompt Library

 docs.anthropic.com/en/prompt-library — tested prompts for 60+ use cases. Good starting templates before writing from scratch.
 
#### Model string reference (current)

 claude-opus-4-6 (most capable, highest cost), claude-sonnet-4-6 (best balance — use for most tasks), claude-haiku-4-5-20251001 (fastest, cheapest — use for classification/routing). Always check docs for the latest model strings — they change.
 
#### Rate limits (know before you build)

 Tier 1 ($5 spent): 50k tokens/min Sonnet. Tier 2 ($500 spent): 100k. Tier 3 ($5k): 150k. Plan your app architecture around these — burst requests can hit limits. Use exponential backoff with jitter for retry logic.
 
#### Key headers for API calls

 anthropic-version: 2023-06-01 (required). x-api-key: your key. content-type: application/json. For streaming: accept: text/event-stream. The SDK handles all these — only relevant if making raw HTTP calls.

</details>

Links: [docs.anthropic.com](https://docs.anthropic.com) · [Prompt Library](https://docs.anthropic.com/en/prompt-library)

---

## 🐙 GitHub Trending (Daily)
**🔥 MUST USE** · _Discovery, Stay Current, Find Skills_

github.com/trending — daily list of fastest-rising repos. Filter by language. How you discover tools like impeccable, taste-skill, blender-mcp before everyone else. Check once a day.

<details><summary>Details</summary>

#### How to use effectively

 Go daily or weekly. Filter: "Today" (most viral right now), language = "All" or filter to TypeScript/Python. Look for: 500+ stars gained in one day (viral), repos with "claude" or "mcp" or "skill" in the name (relevant to your workflow), tools that solve a problem you've been working around.
 
#### What to do when you find something

 Star it (saves it for later). Read the README in 2 minutes — is it solving a real problem you have? Check: last commit (active?), open issues count (red flag if 500+), license (MIT = free to use). If relevant: clone and try it today while it's top of mind.
 
#### Trending for Claude skills specifically

 Search GitHub directly: topic:claude-skill stars:>100 . Or: topic:mcp-server stars:>500 . Topic searches surface the best repositories regardless of when they trended. Combine with trending for daily discovery.
 
#### Alternative discovery surfaces

 Hacker News "Show HN" posts (news.ycombinator.com — "Show HN" filter), Product Hunt (producthunt.com — dev tools category), X/Twitter: follow @anthropic, @clarifai_eng, @karpathy, @sama for AI tool announcements. These often have repos before they hit GitHub trending.
 
#### Curation signal

 A repo on GitHub trending AND on Hacker News front page simultaneously = very likely worth your time. Two independent signals of quality reduce noise significantly.

</details>

Links: [github.com/trending](https://github.com/trending)

---

## 🤖 model context protocol (MCP) Registry
**🔥 MUST USE** · _Official MCP Servers, Community, Discovery_

modelcontextprotocol.io/servers — the official and community registry of MCP servers. 200+ servers covering every API and service. Check here before building a custom MCP.

<details><summary>Details</summary>

#### What's in the registry

 Official servers (from Anthropic and major companies): GitHub, Slack, Google Drive, Notion, Linear, Stripe, Supabase, Filesystem, SQLite, PostgreSQL, Brave Search. Community servers: hundreds more covering long-tail integrations. New servers added weekly.
 
#### How to find what you need

 Browse by category: Databases, Communication, Developer Tools, File Systems, Web Services, AI/ML. Or search by name. GitHub search: topic:mcp-server returns all public MCP servers (often more current than the official registry).
 
#### Evaluating server quality

 Stars (community signal), last commit date (actively maintained?), README quality (does it explain the tools clearly?), issues count (red flag if many open). Prefer servers with: >100 stars, recent commits, maintained by the service itself (e.g., Supabase's own MCP is better than community-built).
 
#### Before building custom

 Always check the registry first. "I want Claude to interact with my CRM" → search "CRM" or "[specific CRM name]" in registry. Someone has likely already built it. Building custom MCPs is worthwhile for internal tools only.
 
#### MCP Inspector

 github.com/modelcontextprotocol/inspector — a visual tool to inspect and test MCP servers. Run any server → see what tools it exposes → test tools directly → debug without needing Claude. Essential for MCP development.

</details>

Links: [MCP Registry](https://modelcontextprotocol.io/servers) · [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

---

## 🧩 shadcn/ui Component Library
**🔥 MUST USE** · _Production Components, Accessible, Tailwind_

Copy-paste React components built on Radix UI primitives. Production-quality, accessible, customizable. What V0 generates. The foundation of any serious Next.js project.

<details><summary>Details</summary>

#### Why shadcn/ui is the right choice

 Unlike MUI or Chakra that you import as packages, shadcn/ui components are copied into your codebase — you own the code entirely. Built on Radix UI (handles all accessibility: ARIA, keyboard navigation, focus management). Tailwind-based so you customize with familiar classes. Dark mode included via CSS variables.
 
#### Setup

 npx shadcn@latest init — sets up tailwind, CSS variables, utils. npx shadcn@latest add button — adds Button component. Add components one at a time as you need them. Check ui.shadcn.com for the full component list.
 
#### Components to add immediately

 button, input, card, dialog, dropdown-menu, select, table, tabs, toast, form, badge, avatar. These cover ~80% of UI needs. Add: command (command palette), data-table (TanStack Table wrapper), calendar (date picker) when needed.
 
#### CSS variable theming

 All colors reference CSS variables: --primary, --secondary, --muted, --accent, --destructive. Change the variable → entire UI updates. Add your custom theme by modifying globals.css. Never hardcode colors in shadcn/ui components.
 
#### V0 + shadcn/ui

 V0 generates shadcn/ui by default. This means: prompt V0 for a component → copy code → paste into project (which has shadcn/ui installed) → zero rework. The integration is intentional — Vercel built both.
 
#### Extending components

 Don't modify the copied component files directly (breaks on updates). Instead: create a wrapper component that extends the shadcn/ui base. Example: Button.tsx wraps shadcn's Button with your custom variants.

</details>

Links: [ui.shadcn.com](https://ui.shadcn.com)

---

## 📚 Awesome Lists — Curated GitHub Collections
**✅ GOOD** · _awesome-mcp, awesome-llm, awesome-claude_

GitHub's "Awesome" lists are curated collections of the best resources in any domain. awesome-mcp-servers, awesome-claude-prompts, awesome-llm-apps — bookmarked goldmines for your stack.

<details><summary>Details</summary>

#### Awesome lists to bookmark

 **awesome-mcp-servers**: github.com/punkpeye/awesome-mcp-servers — the most complete list of MCP servers, categorized. Updated weekly. Better discovery than the official registry for community servers. **awesome-claude-prompts**: Multiple repos — search "awesome claude prompts" — collections of tested system prompts for different use cases. **awesome-llm-apps**: github.com/Shubhamsaboo/awesome-llm-apps — example apps built with LLMs (with source code). Learn by reading real implementations. **awesome-nextjs**: Resources, boilerplates, and patterns for Next.js. **awesome-design-md**: (you have this) — brand DESIGN.md files.
 
#### How to use Awesome lists

 Don't read top-to-bottom (overwhelming). Use Ctrl+F to search for what you need: "github" → find GitHub-related MCP servers. "search" → find search tools. "AI" → find AI service integrations. They're reference documents, not sequential reading.
 
#### Finding the right Awesome list

 Search GitHub: "awesome [topic]". Filter results by: stars (>1000 = well-maintained), last updated (within 6 months = current). The "Awesome" repository itself (github.com/sindresorhus/awesome) indexes all quality Awesome lists.
 
#### Contributing

 If you build something useful — a Claude skill, an MCP server, a prompt pack — submit a PR to the relevant Awesome list. Good for visibility and community contribution.

</details>

Links: [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) · [awesome list index](https://github.com/sindresorhus/awesome)

---

## 🗂️ Boris Cherny CLAUDE.md Template
**✅ GOOD** · _Best CLAUDE.md Starting Point_

The best public CLAUDE.md template. Adapt it for every project. Establishes conventions, constraints, and workflow instructions that dramatically improve Claude Code output quality.

<details><summary>Details</summary>

#### What makes this template stand out

 Boris Cherny (former Meta engineer) published a CLAUDE.md template that's been forked thousands of times. Key insight: CLAUDE.md is most valuable for "NEVER DO" rules, not "always do" rules. "Never store auth tokens in localStorage" > "write good code."
 
#### Core sections in the template

 Project overview (2 sentences), Tech stack (specific: "Next.js 14.2.x" not "Next.js"), Architecture overview (key directories and their purpose), Development workflow (exact commands to run), Coding conventions (naming, patterns, file organization), NEVER DO list (the most valuable section), Known issues / gotchas, External docs (links to relevant docs for your stack).
 
#### The NEVER DO list (most valuable)

 Examples: "Never use useEffect for data fetching — use server components." "Never commit without running tsc --noEmit first." "Never use any as a TypeScript type without a comment explaining why." "Never call the Supabase client from client components — only from server components and API routes." These prevent Claude from reverting to generic patterns.
 
#### Maintenance cadence

 Update CLAUDE.md: after every architecture decision, after every "Claude did the wrong thing again" moment (turn that correction into a rule), when adding a significant dependency. Delete stale entries — a wrong CLAUDE.md is worse than no CLAUDE.md.
 
#### Source

 github.com/ThaddaeusSandidge/BorisChernyClaudeMarkdown — the preserved template with the README explaining each section.

</details>

Links: [Template](https://github.com/ThaddaeusSandidge/BorisChernyClaudeMarkdown)

---

## 🧩 Claude Code — Power User Shortcuts
**✅ GOOD** · _prompt template_

The non-obvious Claude Code workflows that 10x your velocity. These aren't in the docs — they're discovered through heavy usage.

<details><summary>Details</summary>

#### Advanced Claude Code Patterns
PARALLEL AGENT PATTERN:
"Do these 3 tasks simultaneously: (1) write the unit tests for UserService, (2) update the API documentation for /users endpoints, (3) generate TypeScript types from this JSON schema: [schema]. I'll review all three when done."
→ Claude works on all three in parallel, returns all at once. Saves 3x the time.

CHECKPOINT PATTERN:
"Before you write any code: state your plan in 3 bullets. I'll confirm before you proceed."
→ Catches wrong approaches before they're implemented. Saves debugging time.

CONTEXT ANCHORING:
"For this entire session: you are working in a Next.js 14 App Router codebase. All components are server components by default. We use Supabase for auth and data. tailwind + shadcn/ui for UI. Never use useEffect for data fetching. Confirm you understand."
→ Set the context once, Claude remembers for the session. Eliminates repeated clarifications.

FILE-FIRST PATTERN:
"Read /src/lib/supabase.ts, /src/types/index.ts, and /src/app/dashboard/page.tsx before we start. Then tell me how the current auth flow works."
→ Make Claude read actual files before reasoning about them. Prevents hallucinated "I assume your code does X."

CONSTRAINT LADDER:
"Build a user settings form. Requirements in priority order: (1) works on mobile, (2) uses shadcn/ui Form + Zod validation, (3) saves to Supabase, (4) shows success/error toast. Implement in priority order. If (4) would compromise (1-3), skip it and tell me."
→ Explicit priority ordering. Claude knows what to sacrifice if something conflicts.

ROLE FLIP:
"You're now reviewing code I'm about to write — not writing it yourself. I'll write it and you tell me what's wrong."
→ Changes Claude from writer to reviewer. Sometimes you need to write it yourself and just want critique.

THE RUBBER DUCK PROTOCOL:
"I'm going to explain my approach to [problem]. Don't solve it. Ask me questions that expose gaps in my thinking. Start when I'm done explaining."
→ Claude asks rather than tells. Excellent for debugging your own reasoning.

DIFF REVIEW:
"Here's the git diff of my last commit: [diff]. Review it for: security issues (priority 1), logic errors (priority 2), style inconsistencies (priority 3). Only report issues — skip commentary on what's correct."
→ Targeted review of actual changes, not hypothetical code.

ESCALATION PATTERN:
"First: try to solve this with the simplest possible approach. If that doesn't work, escalate to a more complex solution. Tell me which level you ended up at and why."
→ Gets you the right level of complexity, not Claude's preferred complexity.

TEACH-BACK:
"Explain [concept] as if I'm a smart developer who has never used [technology] before. Then give me the 3 things about it that surprised experienced developers when they first learned it."
→ Gets you both the fundamentals AND the non-obvious insights in one response.

</details>

Links: —

---

## 🎨 Design Inspiration Sites
**✅ GOOD** · _Godly, Awwwards, Lapa, Mobbin_

Curated UI/UX inspiration. Use before starting any project: 20 minutes of intentional reference browsing → specific patterns to implement → V0 or Claude code that matches your vision.

<details><summary>Details</summary>

#### Sites by use case

 **Godly.website**: Best for AI-era dark web design. Heavy on glassmorphism, particle effects, dramatic typography. Good for portfolio and SaaS hero sections. **Awwwards**: Award-winning sites, experimental design. More avant-garde — use for creative agency / portfolio inspiration. **Lapa.ninja**: Landing pages specifically. 2000+ SaaS and startup landing pages. Best for: pricing pages, feature sections, social proof patterns. **Mobbin**: Real mobile app screens. Best for: onboarding flows, dashboard patterns, settings screens. **Screenlane**: Mobile + web UI patterns. Good complement to Mobbin.
 
#### The right workflow with these sites

 Don't browse aimlessly. Come with a specific UI challenge: "I need to design a pricing page." Spend 15-20 minutes, screenshot 3-5 references. Then: open V0 → drag in screenshots → "Inspired by these layouts, build a pricing page for [my product] with [my colors]." Reference-driven prompting produces dramatically better output than text-only description.
 
#### Saving references

 Use: Arc browser's "pinned tab" for pages you revisit, Raindrop.io for organized link saving with screenshots, Figma's "Inspiration" page (create one) for saving screenshots directly. Don't rely on browser history — organize your references.
 
#### When NOT to use these

 Don't browse inspiration when you should be building. These are planning tools. Set a 20-minute timer, get your references, then close them and build. Endless inspiration browsing is productive procrastination.

</details>

Links: [Godly](https://godly.website) · [Awwwards](https://awwwards.com) · [Lapa](https://lapa.ninja)

---

## 🔥 Hacker News (YC / Show HN)
**✅ GOOD** · _Tech News, Startup Launches, Discussion_

news.ycombinator.com — the best signal-to-noise tech news source. "Show HN" posts are developers launching things. The comments are where real engineers discuss tools, disagree with hype, and share production experience.

<details><summary>Details</summary>

#### Why HN is different from Twitter/X

 HN comments are written by practitioners, not influencers. When a new AI tool launches: Twitter is hype, HN comments are "I tried this and here's what actually broke." The skepticism is valuable — it surfaces real limitations quickly.
 
#### Most valuable sections

 **Show HN**: Filter to "Show HN" — developers launching projects. Where you find things like impeccable, blender-mcp, taste-skill before they're popular. **Ask HN**: "Ask HN: What's the best tool for X?" — crowd-sourced recommendations from practitioners. **Who is Hiring**: Monthly thread, real companies, real salaries, remote options listed. Better signal than LinkedIn for tech-specific roles.
 
#### How to read HN efficiently

 15 minutes max. Read headlines. Click only: "Show HN" posts relevant to your stack, Ask HN posts on topics you care about, any post about tools/frameworks you use. Read 2-3 top comments, judge quality. Skip: political discussions, philosophy, anything with >300 comments (usually controversial not insightful).
 
#### HN Search

 hn.algolia.com — full-text search of all HN posts. "claude code" → find every HN discussion about Claude Code. Excellent for: finding what practitioners actually think about a tool, researching a company before an interview, finding threads about errors you're hitting.
 
#### Frequency

 Daily: 10-minute skim. Weekly: read 2-3 interesting long threads fully. This keeps you current without the noise of Twitter's AI hype cycle.

</details>

Links: [Hacker News](https://news.ycombinator.com) · [HN Search](https://hn.algolia.com)

---

## 📊 Plausible + Sentry — Monitoring Stack
**✅ GOOD** · _Analytics, Error Tracking, Privacy-First_

Plausible (privacy-first analytics, no cookies) + Sentry (error tracking with full stack traces). The production monitoring stack every launched app needs, set up in 30 minutes.

<details><summary>Details</summary>

#### Plausible Analytics

 $9/month for up to 10k monthly pageviews. No cookies → no GDPR cookie banner needed. Simple dashboard: pageviews, unique visitors, top pages, referrers, geography, device. No sessions or user-level tracking — just aggregate. Lightweight script ( npm install next-plausible . Wrap your app with PlausibleProvider in layout.tsx. Track custom events: plausible('Signup', {props: {plan: 'pro'}}) . Works with Next.js App Router and Pages Router.
 
#### Sentry error tracking

 Free tier: 5,000 errors/month (more than enough for early-stage apps). Captures: unhandled exceptions with full stack traces, browser console errors, API errors, performance issues (slow transactions, Core Web Vitals). Install: npx @sentry/wizard@latest -i nextjs — wizard does everything.
 
#### What Sentry shows you

 "TypeError: Cannot read property 'map' of undefined at UserList.tsx:45" — exact file, exact line, user's browser, their session replay (you can watch what they did before the error), frequency (how many users hit this?). You find out about bugs before users report them.
 
#### Setup priority

 Add both before your first real user. Cost of missing errors > cost of $9/month. "I'll add monitoring later" means you're blind during the most critical period (initial user testing). Add day 1.
 
#### Alternative: PostHog

 PostHog ($0 for 1M events/month) does: analytics + session recordings + feature flags + A/B testing + error tracking. More complex but extremely powerful free tier. Consider if you want all monitoring in one tool.

</details>

Links: [Plausible](https://plausible.io) · [Sentry](https://sentry.io)

---

## ⚡ TanStack Libraries
**✅ GOOD** · _React Query, Table, Router, Form_

TanStack's suite: React Query (server state), Table (headless tables), Router (type-safe routing), Form (form state). The gold standard for production React data management.

<details><summary>Details</summary>

#### React Query (TanStack Query) — most important

 The definitive solution for server state in React. Handles: data fetching, caching, background refetching, loading/error states, pagination, infinite scroll. Without it: every developer reinvents these patterns badly. With it: correct behavior out of the box.
 const { data, isLoading, error } = useQuery({
 queryKey: ['tasks', userId],
 queryFn: () => fetchTasks(userId),
 staleTime: 5 * 60 * 1000, // 5 minutes
}); 
 
#### When to use React Query vs Server Components

 Server Components (Next.js App Router): use for initial page data — no loading state, SEO-friendly, runs on server. React Query: use for data that changes after page load (user actions, real-time updates, mutations with optimistic UI). They complement each other — don't pick one, use both appropriately.
 
#### TanStack Table

 Headless table library — handles: sorting, filtering, pagination, row selection, column visibility. You bring your own UI. The shadcn/ui Data Table component is built on TanStack Table. Add sorting to any column in 5 lines.
 
#### Mutations with optimistic updates

 const mutation = useMutation({
 mutationFn: updateTask,
 onMutate: async (newTask) => {
 await queryClient.cancelQueries({ queryKey: ['tasks'] });
 const previous = queryClient.getQueryData(['tasks']);
 queryClient.setQueryData(['tasks'], old => [...old, newTask]); // optimistic
 return { previous };
 },
 onError: (err, newTask, context) => {
 queryClient.setQueryData(['tasks'], context.previous); // rollback
 }
}); 
 
#### Pricing

 All TanStack libraries: MIT license, completely free. The pro courses on tanstack.com are paid but not necessary — the docs are excellent.

</details>

Links: [React Query](https://tanstack.com/query) · [TanStack Table](https://tanstack.com/table)

---

## 🛠️ Vercel AI SDK
**✅ GOOD** · _Streaming, Multi-Model, React Hooks_

Vercel's SDK for integrating AI into web apps. Unified interface for Claude, OpenAI, Gemini. React hooks for streaming chat. The fastest way to add AI to a Next.js app.

<details><summary>Details</summary>

#### What it provides

 Unified API across providers (switch between Claude/GPT-4/Gemini with one line change). React hooks: useChat (streaming chat UI), useCompletion (streaming text generation). Server-side: streamText, generateText, generateObject (structured JSON output). Built-in: retry logic, error handling, abort signals.
 
#### Install and basic usage

 npm install ai @ai-sdk/anthropic 
 // app/api/chat/route.ts
import { anthropic } from '@ai-sdk/anthropic';
import { streamText } from 'ai';

export async function POST(req: Request) {
 const { messages } = await req.json();
 const result = streamText({
 model: anthropic('claude-sonnet-4-6'),
 messages,
 });
 return result.toDataStreamResponse();
} 
 // components/Chat.tsx
import { useChat } from 'ai/react';
const { messages, input, handleInputChange, handleSubmit } = useChat();
// streaming responses out of the box 
 
#### generateObject (structured output)

 const { object } = await generateObject({
 model: anthropic('claude-haiku-4-5-20251001'),
 schema: z.object({ category: z.string(), score: z.number() }),
 prompt: 'Classify this: ' + text
});
// object is guaranteed to match your Zod schema 
 
#### Switching models

 One import change: import { openai } from '@ai-sdk/openai' → same API for GPT-4o. Useful for: A/B testing models, fallback providers, cost routing (use cheaper model first).
 
#### Pricing / Cost

 SDK is free. You pay per model provider's rates. The SDK doesn't add cost — it just abstracts the API calls.

</details>

Links: [sdk.vercel.ai](https://sdk.vercel.ai)

---

## 🔄 Zustand — Lightweight State Management
**✅ GOOD** · _Client State, No Boilerplate, Simple_

The right state management library for 2025. No boilerplate, no providers, no reducers. Just a store with a getter and setter. Use for global client state that isn't server data.

<details><summary>Details</summary>

#### Zustand vs Redux vs Context API

 **Redux**: Powerful but excessive boilerplate. Actions, reducers, selectors, dispatches — 5 files to add one feature. Overkill for most apps. **Context API**: Built-in, but causes performance issues (any state change re-renders all consumers). Not good for frequently-updated state. **Zustand**: 1 file per store, direct mutation-style syntax (uses Immer internally), fine-grained subscriptions (components only re-render when their specific slice changes). Best for: theme, user preferences, UI state (modal open/close, sidebar state), cart, multi-step form state.
 
#### Complete store example

 import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface UIStore {
 theme: 'dark' | 'light';
 sidebarOpen: boolean;
 setTheme: (theme: 'dark' | 'light') => void;
 toggleSidebar: () => void;
}

export const useUIStore = create ()(
 persist(
 (set) => ({
 theme: 'dark',
 sidebarOpen: false,
 setTheme: (theme) => set({ theme }),
 toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
 }),
 { name: 'ui-store' } // persists to localStorage
 )
); 
 
#### Using the store

 // Any component, anywhere — no Provider needed
const { theme, setTheme } = useUIStore();
// Only re-renders when theme or setTheme changes 
 
#### What NOT to put in Zustand

 Server data (use React Query), form state (use React Hook Form + Zod), data that only one component uses (use useState). Zustand is for shared client state, nothing more.
 
#### Bundle size

 Zustand: ~1.5kb gzipped. Tiny. Compare: Redux Toolkit ~18kb, MobX ~22kb. Use Zustand even if you only have one small store — the simplicity is worth it.

</details>

Links: [Zustand](https://github.com/pmndrs/zustand)

---

## 📐 Framer Motion — Animation Library
**🤔 MAYBE** · _React Animations, Page Transitions, Gestures_

Production-grade React animation library. Page transitions, element reveals, drag gestures, spring physics. Used by Vercel, Linear, Raycast. The animation library for serious React projects.

<details><summary>Details</summary>

#### Core patterns to know

 **Element reveal on scroll**:
 import { motion } from 'framer-motion';
<motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
 transition={{ duration: 0.4, ease: 'easeOut' }} viewport={{ once: true }}>
 Content reveals as user scrolls here
</motion.div> 
 **Staggered children**:
 const container = { hidden: {}, show: { transition: { staggerChildren: 0.1 } } };
const item = { hidden: { opacity: 0 }, show: { opacity: 1 } };
<motion.ul variants={container} initial="hidden" animate="show">
 {items.map(i => <motion.li variants={item}>{i}</motion.li>)}
</motion.ul> 
 
#### Page transitions (Next.js App Router)

 Use AnimatePresence in your layout.tsx to wrap page content. key={pathname} on the page container tells Framer Motion when to play exit/enter animations.
 
#### Performance rules

 Only animate: opacity, transform (translate, scale, rotate). Never animate: width, height, top, left (causes layout recalculation = slow). Use layout prop for smooth element reflow. Test on mobile — 60fps on desktop often means 30fps on mobile.
 
#### Bundle size

 Framer Motion ~40kb gzipped. Not tiny — only include if you're using it meaningfully. For simple fade-in animations: CSS transitions are 0kb. Use Framer Motion when: spring physics matter, complex gesture interactions, AnimatePresence for exit animations.
 
#### Pricing

 MIT license, completely free. Framer (the design tool) has paid plans but Framer Motion (the library) is free.

</details>

Links: [Framer Motion](https://framer.com/motion)

---
