# Claude Power

[← back to index](../README.md)

9 resources.

## 📁 Claude Projects — 3-File System
**🔥 MUST USE** · _Persistent Context, Memory, Workflow_

Every serious project needs 3 files in its Claude Project: CLAUDE.md (context), FEEDBACK.md (session learnings), and a SCRATCH.md (working notes). This creates persistent AI memory across sessions.

<details><summary>Details</summary>

#### The 3 files and their roles

 **CLAUDE.md**: Permanent project context. Tech stack, architecture decisions, conventions, forbidden patterns, team preferences. Claude reads this at the start of every session. The source of truth for "what kind of project is this." **FEEDBACK.md**: Session learnings and feedback you give Claude. After every session, extract: what worked, what didn't, corrections to make, patterns Claude should know. Grows over time into a project-specific knowledge base. **SCRATCH.md**: Current working context. What you're working on now, decisions made this session, current blockers. Rewrite at the start of each session.
 
#### CLAUDE.md template

 # [Project Name]

## Overview
[What this project does in 2 sentences]

## Tech Stack
- Frontend: Next.js 14 App Router, TypeScript, Tailwind, shadcn/ui
- Backend: Next.js API routes, Supabase PostgreSQL
- Auth: Supabase Auth
- Deploy: Vercel

## Conventions
- Components: PascalCase, one per file in /components
- API routes: /app/api/[resource]/route.ts
- Types: in /types/index.ts

## NEVER DO
- useEffect for data fetching (use server components)
- Store sensitive data in localStorage
- Commit without running type-check 
 
#### Session start ritual

 Open Claude → open Project → paste: "Read CLAUDE.md, FEEDBACK.md, and SCRATCH.md. Here's what I'm working on today: [task]. Any questions before we start?" Claude now has full context and can proceed without re-explanation.
 
#### Session end ritual

 "Summarize what we accomplished this session. What patterns should I add to FEEDBACK.md? What should I update in CLAUDE.md?" Extract the learnings → paste into FEEDBACK.md → update CLAUDE.md with any new decisions made.
 
#### Why this beats long conversations

 Long conversations degrade Claude's attention (context window fills, early instructions get forgotten). The 3-file system keeps context documents short and fresh, ensuring Claude always has the most relevant information at peak attention.

</details>

Links: —

---

## 📄 CLAUDE.md Mastery
**🔥 MUST USE** · _Project Instructions, AI Context File_

The single most important file in any Claude Code project. Andrej Karpathy reported 65%→94% accuracy improvement after writing a proper CLAUDE.md. Every project needs one.

<details><summary>Details</summary>

#### What makes a great CLAUDE.md

 **Specific, not generic**: "Never use useEffect for data fetching — always use React Query or server components." Not: "Write good code." **Architectural decisions**: Document WHY you made key choices. "We use Zustand instead of Redux because X." Context prevents Claude from suggesting rewrites. **Pain points**: "The authentication flow is complex — see /docs/auth.md before touching anything in /lib/auth." **Environment specifics**: "Run 'npm run dev' not 'next dev' — we have custom env loading."
 
#### Sections to always include

 1. Project overview (2 sentences). 2. Tech stack (specific versions). 3. Folder structure (key directories and what they contain). 4. Development commands (exactly how to run/test/build). 5. Coding conventions (naming, patterns). 6. NEVER DO list (critical anti-patterns). 7. Known issues/gotchas. 8. Key contacts or docs.
 
#### Update cadence

 Update CLAUDE.md: after every major architectural decision, when you add a new significant dependency, when you establish a new convention, when you discover a gotcha that bit you. Think of it like comments that describe the codebase's philosophy, not just its mechanics.
 
#### CLAUDE.md for Claude Code (CLI)

 When using Claude Code (CLI), CLAUDE.md in the project root is automatically read. The file acts as persistent system instructions. Claude Code also reads CLAUDE.md files in subdirectories for sub-project context.
 
#### Length

 Keep under 2000 words. Long CLAUDE.md files dilute attention. If it's getting long: split into linked docs. CLAUDE.md links to /docs/auth.md, /docs/api.md etc. Main file stays concise, detailed docs exist for deep dives.

</details>

Links: —

---

## 🌐 Headroom — Multi-Agent Framework
**🔥 MUST USE** · _Agent Orchestration, Anthropic SDK_

Multi-agent orchestration library built on Anthropic's Agent SDK. Route tasks to specialized agents, coordinate parallel work, build compound AI systems. The framework for serious AI engineering.

<details><summary>Details</summary>

#### What Headroom does

 Headroom provides: Agent routing (send task to the right specialist agent), memory management (agents share a working memory), tool orchestration (agents coordinate tool use), error recovery (retry logic and fallback chains), parallel execution (run multiple agents simultaneously and merge results).
 
#### Core concept: agent hierarchy

 **Orchestrator**: Receives the high-level goal, plans steps, delegates to specialists. **Specialists**: Research agent, code agent, writing agent, analysis agent — each optimized for its domain. **Merger**: Combines results from parallel specialist runs into a coherent output.
 
#### Simple setup

 import { Headroom, Agent } from 'headroom-sdk';

const hr = new Headroom({ apiKey: process.env.ANTHROPIC_API_KEY });

const researchAgent = new Agent({ role: 'researcher', model: 'claude-haiku-4-5' });
const writerAgent = new Agent({ role: 'writer', model: 'claude-sonnet-4-6' });

const result = await hr.run([researchAgent, writerAgent], {
 task: "Research quantum computing and write a summary"
}); 
 
#### When to use Headroom vs single Claude

 Single Claude: most tasks. Headroom: tasks that need specialized expertise (research + code + writing combined), tasks that benefit from parallelism (research 5 topics simultaneously), tasks too long for a single context window (chain agents sequentially).
 
#### Source

 GitHub: search "headroom anthropic" — open source, actively maintained.
 
#### Learning path

 Start with Anthropic's Agent SDK docs → build a simple two-agent system → then adopt Headroom for orchestration patterns. Don't start with Headroom — understand the underlying SDK first.

</details>

Links: [Anthropic Agents](https://docs.anthropic.com/en/docs/agents)

---

## ⚡ LEAN ENGINE Protocol
**🔥 MUST USE** · _Token Efficiency, 60-70% Reduction_

A prompt protocol that reduces Claude's output by 60-70% without losing quality. Eliminates preamble, hedging, repetition, and filler. Claude writes like a senior engineer, not a chatbot.

<details><summary>Details</summary>

#### The LEAN ENGINE system prompt

 LEAN ENGINE ACTIVE. Rules:
1. NO preamble. Start with the answer/code immediately.
2. NO repetition of what I said back to me.
3. NO "Great question!" or affirmations.
4. NO hedging ("it depends", "you might want to consider").
 Make a decision and explain it briefly.
5. NO placeholder code (no "// add logic here").
 Write complete, working implementations.
6. NO ending summaries of what you just wrote.
7. Code comments only for non-obvious logic.
8. When asked to fix something: fix it. Don't explain what you're about to fix.
9. If something is genuinely unclear, ask ONE specific question.
 Don't ask multiple questions.
10. Use headers only when there are 3+ distinct sections. 
 
#### Before vs After LEAN ENGINE

 **Before**: "That's a great question! When working with React state management, there are several approaches to consider. Let me walk you through the options. First, we have..." (100 words before answering). **After**: "Use Zustand for this — lightweight, no boilerplate. Here's the store:" [code]. (10 words, then code.)
 
#### When to activate

 Complex coding sessions, long projects, API usage where you pay per token. Not for: exploratory conversations where you want Claude to think out loud, creative tasks, learning sessions where explanation is the point.
 
#### API cost impact

 At 60-70% output reduction: same number of interactions, ~60% fewer output tokens, ~40% overall cost reduction (input tokens unchanged). Significant for heavy API users.
 
#### Where to put it

 Top of your system prompt, or beginning of a new chat session. Can combine with other prompts — place LEAN ENGINE rules first so they take priority.

</details>

Links: —

---

## 🗣️ LLM Council
**🔥 MUST USE** · _Multi-Model Debate, Best-Answer Synthesis_

A prompt that makes Claude simulate 3-5 distinct AI personas, each with different reasoning styles, debate a problem, and synthesize the best answer. Gets significantly better answers on complex decisions.

<details><summary>Details</summary>

#### The LLM Council prompt

 Before answering, convene a Council of 4 experts:

ARCHITECT: Focuses on clean design and long-term maintainability.
PRAGMATIST: Focuses on shipping fast and what works right now.
SKEPTIC: Finds flaws, edge cases, and what can go wrong.
SYNTHESIZER: Combines insights and makes the final recommendation.

Format:
ARCHITECT: [their perspective]
PRAGMATIST: [their perspective]
SKEPTIC: [concerns and edge cases]
SYNTHESIZER: [final recommendation and why]

Question: [your question here] 
 
#### When to use it

 Architecture decisions, library choices, approach comparisons, debugging complex issues, business decisions. NOT for simple factual questions or clear-cut implementation tasks.
 
#### Example output quality

 SKEPTIC might surface: "This approach works but fails when the network is unreliable and the user has slow 3G — here's what happens..." PRAGMATIST might counter: "You could add retry logic in 5 lines and ship today." SYNTHESIZER combines both into a concrete recommendation you wouldn't have gotten from a single perspective.
 
#### Customizing the council

 Replace the 4 personas with domain-specific experts: SECURITY_ENGINEER, PERFORMANCE_ENGINEER, UX_DESIGNER, PRODUCT_MANAGER. The council works for any domain — business, design, product, research.
 
#### Combined with Chain-of-Thought

 Adding "Think step by step" to the council prompt makes the reasoning even more transparent. You can see exactly how each perspective reaches its conclusion and choose which chain of reasoning is most relevant to your situation.

</details>

Links: —

---

## 🌊 ruFlo (ruvnet)
**🔥 MUST USE** · _Agent Meta-Harness, Multi-Agent, MCP_

Agent meta-harness for deploying multi-agent swarms, coordinating autonomous workflows, and building conversational AI systems. Adaptive memory, self-learning, RAG integration, native Claude Code / Codex / Hermes integrations.

<details><summary>Details</summary>

64,400+ stars. TypeScript. From ruvnet (claude-flow / ruv-swarm author). Ships as an MCP server + npm package — heavyweight option for serious multi-agent orchestration.

</details>

Links: [GitHub](https://github.com/ruvnet/ruflo)

---

## 🧩 Wiki-Brain (Obsidian + Claude)
**🔥 MUST USE** · _Compound Memory, Knowledge Graph_

A Claude Code skill that turns Obsidian into a compound AI memory system. Claude reads your notes, builds connections, maintains a BRAIN.md index, and grows smarter about your knowledge base over time.

<details><summary>Details</summary>

#### What Wiki-Brain does

 Wiki-Brain is a SKILL.md file for Claude Code that instructs Claude to: read your Obsidian vault, identify key concepts and connections, maintain a structured BRAIN.md index of your knowledge, surface relevant notes during conversations, and suggest connections between concepts you've written about at different times.
 
#### Setup

 1. Install the Wiki-Brain skill in Claude Code. 2. Point it at your Obsidian vault directory. 3. Run initial indexing: "Index my vault and create BRAIN.md." 4. In future sessions: "Before answering, check my notes for anything relevant to [topic]."
 
#### BRAIN.md structure

 The skill creates a BRAIN.md in your vault root: an index of key concepts, file names, and cross-references. Think of it as a manually curated sitemap for your second brain. Claude uses it to quickly find relevant notes without reading every file.
 
#### Power workflow

 Research a topic → write notes in Obsidian → ask Claude to index → Claude connects your new notes to existing knowledge and surfaces connections you hadn't noticed. "I see you have a note on LangGraph from 3 months ago that's relevant to this multi-agent question."
 
#### Privacy consideration

 Your Obsidian notes are sent to Claude's API. Keep sensitive personal information (passwords, medical info, financials) out of the vault you index, or use local Claude models for maximum privacy.
 
#### Source

 GitHub: search "wiki-brain claude skill" — it's a community-built Claude Code skill. Free and open source.

</details>

Links: —

---

## 🎭 Life OS — Claude as Life System
**✅ GOOD** · _Personal System, Goals, Review_

Using Claude Projects as a personal operating system: goal tracking, weekly reviews, decision journaling, habit accountability. The Claude version of a Notion Life OS.

<details><summary>Details</summary>

#### Setup

 Create a Claude Project called "Life OS". Upload your goals doc, values doc, current commitments. Set project instructions: "You're my personal advisor. You have context on my goals, values, and situation. Be direct and honest. Push back on excuses."
 
#### Weekly review template

 Weekly Review [date]:

Energy this week (1-10): 
Key wins:
What I avoided:
Decisions I need to make:
Questions I'm sitting with:

Based on this, ask me the 3 questions that 
would be most useful for me to answer. 
 
#### Decision journal

 Before any major decision: "I'm deciding between [A] and [B]. Here's my thinking: [reasoning]. What am I missing? What questions should I answer before deciding?" Document the reasoning. Review past decisions monthly to improve your decision-making patterns.
 
#### Goal tracking

 Upload your quarterly goals to the Project. Weekly: "Here's what I did on my goals this week: [updates]. Am I on track? What's the most important thing to focus on this week?" Claude gives honest accountability without judgment.
 
#### Habit accountability

 "Check in: here are my habits for this week [list]. Score me on each one and tell me what's most likely preventing progress on the ones I'm struggling with."
 
#### Privacy consideration

 This system works best with honest, detailed inputs. Be comfortable with Anthropic's data handling before adding sensitive personal information. Claude Projects data is used per Anthropic's privacy policy.

</details>

Links: —

---

## 🔄 Session Start / End Rituals
**✅ GOOD** · _Workflow, Context Management, Consistency_

Structured prompts for beginning and ending Claude sessions. Session Start loads context correctly; Session End extracts learnings for FEEDBACK.md. Makes every session compounding.

<details><summary>Details</summary>

#### Session Start prompt

 Session start. Context:
- Project: [project name]
- Stack: [tech stack]
- Last session: [1-2 sentence summary of what you did last time]
- Today's goal: [specific task]
- Relevant files: [list key files to focus on]

Read the above, confirm your understanding, and ask one question 
if anything is unclear. Then we'll begin. 
 
#### Why the start prompt works

 Front-loads all context before Claude starts reasoning. Claude's attention peaks at the start of a conversation — the most important information should be there. "Read and confirm" step catches misunderstandings before they cascade into wrong code.
 
#### Session End prompt

 Session complete. Generate:

1. SUMMARY (3 bullets): What we built/fixed/decided
2. FEEDBACK.md additions: Patterns I should remember, 
 corrections to make, things that worked well
3. CLAUDE.md updates: Any new conventions or decisions
4. Next session: Recommended starting point

Format as copy-pasteable markdown sections. 
 
#### The compounding effect

 Month 1: each session starts from scratch. Month 3 with consistent FEEDBACK.md: Claude has 30 sessions of project-specific learnings. Month 6: Claude knows your codebase, your preferences, your common mistakes. Each session gets more efficient.
 
#### The practical habit

 Literally 2 minutes at the end of each session to run the end prompt and paste the output into your files. This is the highest ROI 2 minutes in any project.

</details>

Links: —

---
