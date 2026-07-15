# MCP Servers

[← back to index](../README.md)

14 resources.

## 🎨 BlenderMCP
**🔥 MUST USE** · _3D Generation, Claude Controls Blender_

Claude controls Blender via MCP socket server. Create 3D objects, scenes, materials, and animations through natural language. No Blender expertise needed.

<details><summary>Details</summary>

#### What it does

 BlenderMCP installs a Blender addon that opens a socket server. Claude Code connects via MCP and can: create/modify meshes, apply materials, set lighting, position objects, add animations, render images. You describe what you want → Claude executes Python/Blender API calls.
 
#### Install

 uvx blender-mcp — installs via uv (Python package manager). Then in Blender: Edit → Preferences → Add-ons → install the addon → enable it → start the server. Add to Claude Code config:
 {
 "blender": {
 "command": "uvx",
 "args": ["blender-mcp"]
 }
} 
 
#### Example commands

 "Create a low-poly forest scene with 10 trees, a dirt path, and sunset lighting." "Build a 3D product mockup: a phone on a table with studio lighting." "Animate this object rotating 360 degrees over 2 seconds." "Add a subsurface scattering material that looks like skin." "Render a preview at 1920x1080."
 
#### Best use cases

 Portfolio 3D visuals, product mockups, game asset creation (low-poly), architectural visualization sketches, animation prototypes. Not for: production-quality VFX (needs expert Blender knowledge), highly detailed character models (too complex for natural language).
 
#### Learning accelerator

 Even if you want to learn Blender properly: ask Claude to do something → see what Python code it executed → learn from the code. "Create X and show me the Python code you used." Fastest way to learn Blender's API.

</details>

Links: [blender-mcp](https://github.com/ahujasid/blender-mcp)

---

## 📚 Context7 MCP
**🔥 MUST USE** · _Live Docs, Framework Updates, No Hallucination_

Gives Claude access to live, version-specific documentation for 3000+ libraries. Instead of hallucinating outdated APIs, Claude fetches the actual current docs. Essential for any framework work.

<details><summary>Details</summary>

#### The problem it solves

 Claude's training data has a cutoff. Next.js 14 App Router patterns, Supabase v2 API, React 19 features — if these changed after the cutoff, Claude gives you outdated code. Context7 fetches current docs at query time, so Claude always gives you the right API.
 
#### Install

 {
 "context7": {
 "command": "npx",
 "args": ["-y", "@upstash/context7-mcp@latest"]
 }
} 
 
#### Usage

 In Claude Code: "Using Context7, show me the current way to handle form validation in React Hook Form v7." Claude queries Context7 → gets current docs → gives you accurate, versioned code examples. Always add "using Context7" or "with current docs" to trigger the tool.
 
#### Supported libraries (3000+)

 All major frontend (React, Next.js, Vue, Svelte), all major backend (Express, FastAPI, Django), databases (Supabase, Prisma, Drizzle), styling (Tailwind, shadcn/ui), testing (Vitest, Playwright, Jest). If it's popular, Context7 has it.
 
#### Version pinning

 Specify exact versions: "Next.js 14.2 docs via Context7." Claude fetches docs for that specific version. Critical when working with pinned dependencies.
 
#### Pricing

 Context7 by Upstash — free tier available. Generous for individual use.

</details>

Links: [context7.com](https://context7.com)

---

## 🐙 GitHub MCP
**🔥 MUST USE** · _Repos, Issues, PRs, Code Search_

Claude talks to GitHub. Search repos, read code, create issues, review PRs, manage branches — all via natural language. Turns Claude into your GitHub power user.

<details><summary>Details</summary>

#### What it enables

 "Search GitHub for MCP servers with 1000+ stars released in the last month." → Finds trending repos. "Show me all open issues labeled 'bug' in my repo." → Lists them. "Create a new issue: title X, body Y, labels Z." → Creates it. "Read the README for [repo] and summarize it." → Fetches and summarizes.
 
#### Config

 {
 "github": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-github"],
 "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..." }
 }
} 
 Create a fine-grained PAT (Personal Access Token) at github.com/settings/tokens with the minimum permissions needed (repos, issues, PRs).
 
#### Research workflow

 "Find all GitHub repos tagged 'claude-skill' with more than 500 stars. Show name, star count, last updated, and one-line description." Claude searches → formats results → you have a curated list without manual browsing.
 
#### PR review assistant

 "Read the diff for PR #42 in my repo. Give me a code review focusing on: security, performance, and adherence to our conventions from CLAUDE.md." Claude reads the actual PR diff and gives structured feedback.
 
#### Issue triage

 "Read my open issues and categorize them by: bug, feature request, docs needed. Suggest priority order." Automated issue management.

</details>

Links: —

---

## 🌐 Playwright MCP
**🔥 MUST USE** · _Browser Automation, Web Scraping, Testing_

Give Claude a real browser. Navigate pages, click elements, fill forms, take screenshots, scrape data. Claude operates the browser as you would. Best MCP for web automation tasks.

<details><summary>Details</summary>

#### What Playwright MCP enables

 Claude can: navigate to any URL, click buttons and links, fill and submit forms, take screenshots, extract text and data from pages, execute JavaScript, handle authentication flows, interact with SPAs (single-page apps that require JS). Real browser, not just HTTP requests — it handles JavaScript-rendered content.
 
#### MCP config

 // claude_desktop_config.json
{
 "mcpServers": {
 "playwright": {
 "command": "npx",
 "args": ["-y", "@playwright/mcp@latest"]
 }
 }
} 
 
#### Power use cases

 **Data collection**: "Go to [site], find all job listings, extract title/company/salary, save as CSV." **Testing**: "Test my app at localhost:3000: sign up with test@test.com, complete onboarding, verify the dashboard loads." **Competitor research**: "Visit [competitor], screenshot their pricing page and main features." **Form automation**: "Fill out this application form with these details, then take a screenshot before submitting."
 
#### Combined with Claude's reasoning

 Claude navigates → reads page content → decides next action → navigates further. Full multi-step web workflows that adapt based on what's on each page. Not just pre-programmed — Claude reasons about what to do next.
 
#### Limitations

 Can't bypass CAPTCHA, can't access accounts without credentials, can be detected by anti-bot systems (uses real Chromium). For scraping: add realistic delays between actions. For private accounts: Claude needs your credentials (serious security consideration — only for your own accounts).

</details>

Links: —

---

## 🗄️ Supabase MCP
**🔥 MUST USE** · _Database Operations, Schema, SQL_

Claude talks directly to your Supabase database. Run queries, create tables, write migrations, manage RLS policies — all via natural language. Eliminates most Supabase dashboard time.

<details><summary>Details</summary>

#### What you can do

 "Show me all users who signed up in the last 7 days and haven't completed onboarding." → Claude writes the SQL, runs it, shows results. "Add a 'subscription_tier' column to the users table, default 'free'." → Claude writes the ALTER TABLE migration, runs it, confirms. "Create RLS policies for the posts table so users can only see their own posts." → Claude writes and applies the policies.
 
#### Config

 {
 "supabase": {
 "command": "npx",
 "args": ["-y", "@supabase/mcp-server-supabase@latest",
 "--supabase-url", "YOUR_URL",
 "--supabase-key", "YOUR_SERVICE_KEY"]
 }
} 
 Use the service role key (not anon key) — gives full DB access. Keep this key secure.
 
#### Daily workflow integration

 Instead of opening Supabase dashboard → Table Editor → writing SQL: just say in Claude Code "Show me the schema for the users table" or "How many active subscriptions do we have?" Claude handles all DB interaction.
 
#### Migration workflow

 "Write a migration to add [feature] to the schema. Include: column additions, indexes, RLS policies. Format as a SQL file with comments." Claude generates the full migration → you review → run with supabase db push .
 
#### Safety warning

 The service role key bypasses RLS. Claude can modify any data. Always review Claude's proposed SQL before confirming execution on production databases.

</details>

Links: —

---

## 🤖 21st.dev Magic MCP
**✅ GOOD** · _UI Components, Design System, Auto-Insert_

Claude searches 21st.dev's UI component library and inserts components directly into your code. Say "add a dark mode toggle" → Claude finds + installs the exact component. Design system aware.

<details><summary>Details</summary>

#### Config

 {
 "21st-magic": {
 "command": "npx",
 "args": ["-y", "@21st-dev/magic@latest"],
 "env": { "API_KEY": "your-21st-key" }
 }
} 
 
#### Example commands

 "Add a responsive data table with sorting, filtering, and pagination using 21st.dev." "Find a glassmorphism card component from 21st.dev and add it to /components/Card.tsx." "What UI components does 21st.dev have for e-commerce? Show me the top 5."
 
#### Integration with design system

 Components are built with Tailwind + shadcn/ui → they automatically inherit your theme CSS variables. Style consistency across all 21st.dev components without any extra configuration.
 
#### When to use

 When you need a UI element that's complex to build from scratch (data tables, command palettes, complex forms) but don't want to spend time building it. 21st.dev's library is curated for quality.

</details>

Links: [21st.dev](https://21st.dev)

---

## 📧 Email + Calendar MCP
**✅ GOOD** · _Gmail, Outlook, Google Calendar_

Claude reads email threads, drafts replies, schedules events, and manages your calendar. Turns Claude into a real executive assistant for communications.

<details><summary>Details</summary>

#### Gmail MCP setup

 Use the Google Workspace MCP (community-built, multiple versions). Search GitHub for "gmail mcp server" — several options with OAuth2 setup guides. Connect with read + compose permissions.
 
#### Power workflows

 **Email triage**: "Summarize my unread emails from the past 24 hours. Categorize by: urgent/respond, newsletter, FYI, no action." **Reply drafting**: "Draft a reply to the email from [person] about [topic]. Tone: professional but friendly. Accept their meeting request for Tuesday." **Thread summary**: "Summarize this email thread and tell me what action is required from me." **Template drafting**: "Write a cold outreach email to [company] about [offer]. Keep it under 150 words."
 
#### Calendar MCP

 "What's on my calendar next week? Are there any conflicts?" "Schedule a 30-minute call with [person] next Wednesday afternoon." "Block 2 hours every morning this week for deep work." "What's my longest meeting-free stretch this week?"
 
#### Combining both

 "Read my unread emails from this morning. For any that require scheduling a meeting, draft a reply and add the meeting to my calendar." Full workflow automation.
 
#### Privacy consideration

 Email and calendar contain highly sensitive data. Use MCPs with minimal required permissions. Anthropic's API handles data per their privacy policy — understand this before connecting.

</details>

Links: —

---

## 🔍 Exa Search MCP
**✅ GOOD** · _Web Search, Neural Search, Real-Time_

Neural search API that finds semantically relevant content, not just keyword matches. Claude uses Exa to research topics with current, high-quality sources. Better than Bing for research queries.

<details><summary>Details</summary>

#### What makes Exa different

 Exa uses neural (embedding-based) search — it finds semantically similar content, not just keyword matches. Search "latest approaches to preventing LLM hallucinations" → Exa finds academic papers, technical blog posts, and forum discussions that discuss the concept, even if they use different terminology.
 
#### Config

 {
 "exa": {
 "command": "npx",
 "args": ["-y", "exa-mcp-server"],
 "env": { "EXA_API_KEY": "your-key" }
 }
} 
 API key from exa.ai.
 
#### Use cases

 **Research**: "Use Exa to find the 10 most cited recent papers on [topic]." **Competitor research**: "Find blog posts, case studies, and documentation from [competitor company]." **Trend tracking**: "Find what developers are saying about [technology] in the last month. Look for HN posts, Reddit, and dev blogs." **News synthesis**: "Find recent news about [company/topic]. Summarize the top 5 developments."
 
#### Content-focused search

 Exa can filter by: content type (news, academic, blog, social), time range (last day/week/month), domain (only search specific sites). More powerful filtering than standard web search.
 
#### Pricing

 Free tier: 1000 searches/month. Paid: $0.25 per 1000 queries. Very affordable for research-heavy workflows.

</details>

Links: [exa.ai](https://exa.ai)

---

## 📁 Filesystem MCP
**✅ GOOD** · _File Ops, Local Files, Directory Management_

Claude reads, writes, and organizes files on your computer. Mass rename, restructure directories, process file contents, generate files from templates — all from natural language.

<details><summary>Details</summary>

#### Config

 {
 "filesystem": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-filesystem",
 "/Users/username/Documents",
 "/Users/username/Projects"]
 }
} 
 Specify which directories Claude can access. It can ONLY touch what you list here.
 
#### Power use cases

 **Mass rename**: "Rename all files in /photos with format YYYY-MM-DD-[original-name]." **Content processing**: "Read all markdown files in /notes, find any mentioning [topic], and create a combined summary document." **Project scaffolding**: "Create a Next.js project structure at /projects/my-app with standard folders and config files." **Cleanup**: "Find all files in /downloads older than 90 days and list them (don't delete without my confirmation)."
 
#### Batch processing

 "Read all CSV files in this directory, combine them into one, remove duplicate rows, and save as combined.csv." Data wrangling without Python scripts.
 
#### Template generation

 "Using the template in /templates/component.tsx, generate 10 component files for these names: [list]. Place each in /components/[name]/index.tsx." Batch scaffolding.
 
#### Safety

 Always have Claude list/preview what it's going to do before actually modifying files. "What would you do before doing it?" is a good first command. Irreversible operations (delete) should always require explicit confirmation.

</details>

Links: —

---

## 📋 Linear MCP
**✅ GOOD** · _Project Management, Issues, Sprints_

Claude manages your Linear workspace. Create issues, update statuses, triage bugs, plan sprints — from natural language. Turns Claude into your project management assistant.

<details><summary>Details</summary>

#### What it enables

 "Create a Linear issue for: [bug description]. Priority: High. Assign to [team]. Add to current sprint." "Show me all issues in the current sprint and their status." "Move all 'In Review' issues to 'Done' except the ones without an assignee." "Create a new project for [feature] and add these 10 issues to it: [list]."
 
#### Config

 {
 "linear": {
 "command": "npx",
 "args": ["-y", "linear-mcp-server"],
 "env": { "LINEAR_API_KEY": "lin_api_..." }
 }
} 
 API key from linear.app/settings/api.
 
#### Sprint planning workflow

 "Look at our backlog. We have 2 engineers for 2 weeks. Which issues should be in the next sprint? Consider: priority, estimated complexity (from labels), and dependencies." Claude reasons about sprint composition.
 
#### Bug triage

 "Show me all bug issues opened in the last week. Group by: customer-facing vs internal, severity. Draft a triage prioritization." AI-assisted issue management.
 
#### Release notes

 "Find all issues completed in the last sprint. Write release notes grouped by: new features, improvements, bug fixes." Automatic release notes from Linear issues.
 
#### Alternative

 GitHub Issues MCP works similarly if you use GitHub for project management instead of Linear.

</details>

Links: —

---

## 🧠 Memory MCP
**✅ GOOD** · _Persistent Knowledge, Cross-Session Memory_

Gives Claude a persistent knowledge graph that survives across sessions. Store facts, preferences, project context — Claude remembers them in all future conversations.

<details><summary>Details</summary>

#### What it solves

 Every Claude conversation starts fresh — it doesn't remember previous sessions. Memory MCP maintains a knowledge graph (entity-relationship pairs) that Claude can read and write. "Remember that I prefer TypeScript over JavaScript" → stored → Claude knows this in all future sessions.
 
#### Config

 {
 "memory": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-memory"]
 }
} 
 Stores memory in a local JSON file. Private, no cloud sync.
 
#### What to store

 Preferences ("always use Tailwind for styling"), facts about projects ("Leadify uses Supabase on project ID xyz"), constraints ("never suggest jQuery"), past decisions ("we chose Zustand over Redux because of bundle size"), personal context ("I'm a computer science student learning full-stack").
 
#### Memory commands in chat

 "Remember that [fact]." → Claude stores it. "What do you know about me/this project?" → Claude retrieves stored entities. "Update your memory: [changed fact]." → Claude updates the knowledge graph.
 
#### Best for

 Long-term projects where you want Claude to accumulate project-specific knowledge. Personal assistant workflows where you want consistent behavior across sessions. Not needed if you maintain good CLAUDE.md files (those serve the same purpose for coding projects).

</details>

Links: —

---

## 📝 Notion MCP
**✅ GOOD** · _Notes, Docs, Database, Knowledge Base_

Claude reads and writes to Notion. Search pages, create notes, update databases, add task entries — without opening Notion. Great for saving Claude outputs directly to your workspace.

<details><summary>Details</summary>

#### Most useful capabilities

 "Save this meeting summary to my 'Meeting Notes' Notion database." → Claude creates the page. "Search my Notion for anything about [topic]." → Returns relevant pages. "Add a new task to my project tracker database: title, priority, due date." → Creates DB entry. "Update the status of task X to 'In Progress'." → Updates the DB.
 
#### Config

 {
 "notion": {
 "command": "npx",
 "args": ["-y", "@notionhq/notion-mcp-server"],
 "env": { "NOTION_API_KEY": "secret_..." }
 }
} 
 Create an integration at notion.so/my-integrations → share specific pages/databases with the integration → Claude only has access to what you share.
 
#### Best workflow

 After a Claude session: "Summarize what we built today and save it to my [Project] database in Notion with today's date." Automated project journaling without copy-pasting.
 
#### Content pipeline

 "Research [topic] and create a detailed Notion page with: summary, key concepts, resources, and action items." → Research and documentation in one command. Outputs directly to your workspace.
 
#### Database queries

 Filter by properties: "Show me all tasks in my DB where Status = 'Blocked' and Priority = 'High'." Claude queries the Notion API and formats results clearly.

</details>

Links: —

---

## 💬 Slack MCP
**✅ GOOD** · _Team Communication, Message Search, Post_

Claude reads Slack messages, searches channels, drafts responses, and posts updates. Turns Claude into a Slack power user for message summaries and team communication automation.

<details><summary>Details</summary>

#### Capabilities

 Read channel history, search for specific messages, send messages to channels or DMs, get thread context, list users and channels. Essential for: message drafting, channel summarization, automated status updates.
 
#### Config (official Slack MCP)

 {
 "slack": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-slack"],
 "env": { "SLACK_BOT_TOKEN": "xoxb-...",
 "SLACK_TEAM_ID": "T..." }
 }
} 
 Create a Slack app → add bot token scopes → install to workspace.
 
#### Useful workflows

 **Daily standup**: "Summarize what each team member shared in #standup today." **Meeting prep**: "Find all Slack messages mentioning [project] from the last week. What are the key points and open questions?" **Draft message**: "Draft a message to #team announcing [update]. Tone: concise and professional." **Alert**: "Post to #alerts: [status update message]."
 
#### Search

 "Search Slack for all messages about [topic] in the last month." Claude retrieves and synthesizes discussions across channels. Replaces manual Slack search for research.
 
#### Privacy

 Slack messages often contain sensitive team information. The bot can only read channels it's added to — be intentional about which channels you grant access to.

</details>

Links: —

---

## ⚙️ MCP Config Reference
**🤔 MAYBE** · _Setup Guide, claude_desktop_config.json_

Reference for the Claude Desktop config file that wires up all MCP servers. Location, format, common patterns, and debugging tips.

<details><summary>Details</summary>

#### Config file location

 Mac: ~/Library/Application Support/Claude/claude_desktop_config.json . Windows: %APPDATA%\Claude\claude_desktop_config.json . Linux: ~/.config/claude/claude_desktop_config.json .
 
#### Full config structure

 {
 "mcpServers": {
 "filesystem": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/docs"],
 "env": {}
 },
 "supabase": {
 "command": "npx",
 "args": ["-y", "@supabase/mcp-server-supabase", "--url", "...", "--key", "..."]
 },
 "github": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-github"],
 "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..." }
 }
 }
} 
 
#### After editing

 Restart Claude Desktop completely (Cmd+Q → reopen). MCP servers load on startup. If a server fails to start: check Claude Desktop logs at ~/Library/Logs/Claude/.
 
#### Debugging

 In Claude: check the hammer icon — it shows all loaded tools. If a tool is missing, the server failed to start. Common issues: wrong npx package name, missing env vars, wrong file path, port conflict. Run the command in terminal first to see the error.
 
#### Security

 Never put plain-text API keys in version-controlled config files. For shared machines: use environment variables or a secrets manager. The config file is plain JSON on disk — anyone with filesystem access can read it.

</details>

Links: —

---
