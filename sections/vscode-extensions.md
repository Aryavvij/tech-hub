# VS Code Extensions

[← back to index](../README.md)

12 resources.

## 🔴 Error Lens
**🔥 MUST USE** · _Inline Errors, No Panel Switching_

Shows TypeScript/ESLint errors and warnings inline on the affected line — no more clicking to the Problems panel. Makes debugging 2x faster by keeping errors visible at all times.

<details><summary>Details</summary>

#### What it does

 Displays the full error message directly at the end of the problem line, color-coded: red for errors, yellow for warnings, blue for info. You see "Cannot read property 'map' of undefined" right next to the broken line instead of hunting in the Problems panel.
 
#### Essential settings

 "errorLens.enabledDiagnosticLevels": ["error", "warning"],
"errorLens.delay": 300,
"errorLens.fontSize": "12px",
"errorLens.fontStyle": "italic" 
 Set delay to 300ms so it doesn't flicker while you're typing. Disable "hint" and "info" levels to reduce noise — just errors and warnings.
 
#### Color customization

 "errorLens.errorBackground": "rgba(239,68,68,0.1)",
"errorLens.warningBackground": "rgba(234,179,8,0.1)" 
 Subtle backgrounds highlight error lines without being distracting.
 
#### Workflow benefit

 TypeScript type errors appear immediately as you type. This creates a tight feedback loop: write code → see error inline → fix it → error disappears. No command palette, no panel switching. Significant reduction in "why isn't this working" time.
 
#### Works with

 TypeScript, JavaScript, ESLint, Prettier, any VS Code language server. Install and it just works — no configuration required for basic use.

</details>

Links: —

---

## 🔶 GitLens
**🔥 MUST USE** · _Git Blame, History, Code Authorship_

Adds git blame inline — hover any line to see who wrote it, when, and in which commit. File history, branch comparison, interactive rebase UI. Makes git visible without leaving the editor.

<details><summary>Details</summary>

#### Most used features

 **Inline blame**: Every line shows "User, 2 days ago — commit message" on hover. Essential for understanding why code exists. **File history**: Right-click any file → "Open File History" → see every change ever made to that file. **Line history**: Right-click a selection → "Show Line History" → see every change to those specific lines. **Compare branches**: GitLens sidebar → compare any two branches or commits.
 
#### Settings to use

 "gitlens.currentLine.enabled": true,
"gitlens.currentLine.format": "${author}, ${agoOrDate} • ${message|50}",
"gitlens.hovers.currentLine.over": "line" 
 Shows blame on current line only when you hover, keeping UI clean.
 
#### Interactive Rebase Editor

 GitLens replaces the terminal-based rebase UI with a visual drag-and-drop interface. Reorder, squash, edit, drop commits with clicks instead of remembering vim rebase commands.
 
#### Commit graph (Pro)

 Visual branch graph showing all commits, branches, and merges. Free for public repos, Pro for private. The source control panel in VS Code shows basic history — GitLens Pro's graph is significantly better.
 
#### Pricing

 Core features: free. GitLens Pro: $5/month (visual commit graph, worktrees, more history views). Free tier covers 95% of daily use.

</details>

Links: —

---

## 🌐 Live Server
**🔥 MUST USE** · _Local Server, Hot Reload, HTML_

One-click local dev server for static HTML/CSS/JS files with automatic hot-reload. Right-click any HTML file → "Open with Live Server" → instant browser preview that refreshes on save.

<details><summary>Details</summary>

#### When to use

 Whenever you're working with plain HTML/CSS/JS files that don't need Node.js or a build step. Static landing pages, vanilla JS projects, CSS experiments, HTML email templates. For React/Next.js projects with npm run dev, you don't need this — those have their own dev servers.
 
#### Key benefit: CORS for local APIs

 Browsers block fetch() requests from file:// protocol. Live Server runs on http://localhost:5500, so fetch() works correctly. This matters when testing HTML files that call APIs.
 
#### Configuration

 "liveServer.settings.port": 5500,
"liveServer.settings.CustomBrowser": "chrome",
"liveServer.settings.donotShowInfoMsg": true 
 Set your preferred browser. Right-click HTML → Open with Live Server → Done.
 
#### Portfolio use case

 When building your atoms-style portfolio (scroll canvas, mouse scrub effects): open index.html with Live Server → edit CSS/JS → browser updates instantly. Much faster than manually refreshing.
 
#### Multi-file watching

 Live Server watches ALL files in the workspace, not just the open HTML. Edit a linked CSS file → browser refreshes automatically. Complete automatic sync between editor and browser.
 
#### Alternative for React

 Vite's dev server ( npm run dev ) includes hot module replacement (HMR) — more powerful for component-based projects. Live Server is specifically for vanilla HTML projects.

</details>

Links: —

---

## 🛤️ Path Intellisense
**🔥 MUST USE** · _File Path Autocomplete, Import Helper_

Autocompletes file paths as you type in import statements and src attributes. Eliminates path typos and "module not found" errors. Tiny extension, massive daily time saving.

<details><summary>Details</summary>

#### How it works

 When you type import ... from './ or import ... from '../ , Path Intellisense shows a dropdown of real files and folders in your project. Tab to autocomplete. Prevents the most common cause of "module not found" errors.
 
#### Works in

 JavaScript import statements, TypeScript imports, HTML src attributes, CSS url() references, require() calls, JSON file references. Comprehensive coverage of everywhere you reference a file path.
 
#### TypeScript path aliases

 If you use path aliases in tsconfig.json ( "@/*": ["./src/*"] ), configure Path Intellisense to understand them:
 "path-intellisense.mappings": {
 "@": "${workspaceRoot}/src"
} 
 Now import from '@/components/ autocompletes correctly.
 
#### Works with absolute imports

 In Next.js projects using absolute imports (no ../../ chains): Path Intellisense respects your baseUrl setting in tsconfig. Just start typing the module path and it suggests real files.
 
#### Zero configuration for basic use

 Install and it works. No setup needed for relative paths. Only configure if you use path aliases or custom module resolution.

</details>

Links: —

---

## ✨ Prettier + ESLint
**🔥 MUST USE** · _Auto-Format, Code Style, Linting_

Prettier auto-formats code on save. ESLint catches logic errors and style violations. Together they enforce consistent, clean code automatically — you never manually format again.

<details><summary>Details</summary>

#### Setup (the right way)

 1. npm install -D prettier eslint eslint-config-prettier . 2. Create .prettierrc : {"semi": true, "singleQuote": true, "tabWidth": 2} . 3. VS Code settings: "editor.formatOnSave": true, "editor.defaultFormatter": "esbenp.prettier-vscode" . 4. Install ESLint extension. Done — code auto-formats on every save.
 
#### .prettierrc for React projects

 {
 "semi": true,
 "singleQuote": true,
 "tabWidth": 2,
 "trailingComma": "es5",
 "printWidth": 100,
 "jsxSingleQuote": false,
 "bracketSameLine": false
} 
 
#### ESLint for TypeScript (recommended config)

 // .eslintrc.json
{
 "extends": ["next/core-web-vitals", "prettier"],
 "rules": {
 "no-unused-vars": "warn",
 "no-console": "warn",
 "@typescript-eslint/no-explicit-any": "warn"
 }
} 
 
#### Conflict resolution

 ESLint and Prettier can conflict on formatting rules. Solution: always use eslint-config-prettier (turns off ESLint formatting rules) and let Prettier handle all formatting. Never configure ESLint to format — that's Prettier's job.
 
#### Git hooks (enforce for whole team)

 npx husky-init + npx lint-staged --init → runs Prettier/ESLint on staged files before every commit. No unformatted code can enter the repo.

</details>

Links: —

---

## ⚡ Thunder Client
**🔥 MUST USE** · _API Testing, REST, Lightweight Postman_

Postman-equivalent API testing built into VS Code. Test REST/GraphQL endpoints without leaving the editor. Lightweight, fast, stores collections in your project. Free.

<details><summary>Details</summary>

#### Why Thunder Client over Postman

 Postman has become bloated and requires an account. Thunder Client: lives inside VS Code (no context switch), stores collections as JSON files you can commit to git, starts instantly, no account required, and covers 95% of what most developers need from Postman.
 
#### Basic workflow

 1. Open Thunder Client sidebar (lightning bolt icon). 2. New Request → set method (GET/POST/PUT/DELETE), URL, headers, body. 3. Click Send → see response, status code, timing. 4. Save to a Collection for reuse.
 
#### Test your APIs during development

 Before writing frontend code: test your API route in Thunder Client. Confirm it returns the right data shape, handles error cases, and responds to auth headers correctly. Catch issues at the API layer before debugging frontend.
 
#### Environment variables

 Set up environments: Development (localhost:3000), Staging, Production. Variables like {{baseUrl}} and {{authToken}} switch between environments. Never hardcode URLs in requests.
 
#### GraphQL support

 Full GraphQL support — introspection, query builder, variables. If you're using Supabase's GraphQL API or building a GraphQL API: Thunder Client handles it cleanly.
 
#### Commit to git

 Thunder Client saves collections as .thunder-client folder. Add to git → share API test collection with teammates. Everyone gets the same test requests.

</details>

Links: —

---

## 🔵 Auto Import + Tailwind IntelliSense
**✅ GOOD** · _Import Automation, CSS Autocomplete_

Auto Import: automatically adds import statements when you use components/functions. Tailwind IntelliSense: autocompletes Tailwind class names with a preview of what they do.

<details><summary>Details</summary>

#### Auto Import workflow

 Type a component name you know exists → VS Code suggests it → Tab → the import statement is automatically added at the top of the file. Without this: manually write import statements. With this: never write another import statement by hand in TypeScript/React projects.
 
#### Tailwind IntelliSense features

 Autocomplete: type flex → see flex , flex-col , flex-row , flex-wrap . Hover preview: hover any Tailwind class → see the actual CSS it generates. Error detection: unknown/misspelled classes are underlined. Color preview: hover any color class → see the color swatch.
 
#### Tailwind IntelliSense setup

 Must have a tailwind.config.js in your project root for the extension to activate. Standard for any project using Tailwind. Install extension → open project with tailwind.config.js → autocomplete activates automatically.
 
#### Class sorting

 Install Prettier + prettier-plugin-tailwindcss → automatically sorts Tailwind classes in the recommended order on save. Consistent, scannable className strings. npm install -D prettier-plugin-tailwindcss .
 
#### Custom classes

 If you define custom utilities in tailwind.config.js, IntelliSense picks them up and shows them in autocomplete. Works seamlessly with your design system extensions.

</details>

Links: —

---

## 🤖 Codeium
**✅ GOOD** · _Free AI Autocomplete, Copilot Alternative_

Free GitHub Copilot alternative with AI code completion. No usage limits on free tier. Use when Cursor's completions run out or as primary autocomplete in standard VS Code.

<details><summary>Details</summary>

#### Codeium vs GitHub Copilot vs Cursor

 **Codeium**: Free, good autocomplete, no chat. **GitHub Copilot**: $10/month, strong completions, GitHub integration. **Cursor**: $20/month, completions + chat + agent mode + codebase awareness. Use Codeium if you want AI completion without paying. Use Cursor if you want the full AI coding experience and will use it daily.
 
#### Codeium free tier

 Unlimited completions, no rate limits, no credit system. Genuinely free — not a trial. Codeium makes money from their enterprise product, so individual developers get the free tier indefinitely.
 
#### Quality vs Copilot

 Comparable quality for most use cases. Copilot slightly better for: obscure languages, GitHub-specific patterns. Codeium slightly better for: some TypeScript patterns, CSS. Difference is marginal in practice.
 
#### Works in

 VS Code, Cursor (as an additional autocomplete layer), JetBrains, Vim/Neovim, Emacs. Cross-editor if you switch environments.
 
#### Privacy note

 Your code is sent to Codeium's servers for completion. For proprietary/confidential codebases: check your company policy. GitHub Copilot has similar data practices. Cursor can be configured with local models for air-gapped use.
 
#### Best setting

 Enable "Show Ghost Text" — suggestions appear as faded text you can accept with Tab. Standard GitHub Copilot UX.

</details>

Links: [codeium.com](https://codeium.com)

---

## 🕹️ Console Ninja
**✅ GOOD** · _Inline console.log, Runtime Values_

Shows console.log() output directly next to the line that logged it — no more Alt-Tab to browser DevTools to check logs. Runtime values appear inline in the editor.

<details><summary>Details</summary>

#### What it shows

 Next to every console.log() , Console Ninja displays the actual runtime value inline in the editor: console.log(user) // → {id: 1, name: "Aryav", email: "..."} . You see what every log outputs without switching to the browser.
 
#### Works with

 Node.js (server-side), browser JS (via Chrome extension companion), Next.js (both server and client), Jest tests. Wide coverage of the JS ecosystem.
 
#### Debugging workflow improvement

 Old workflow: add console.log → save → switch to browser → open DevTools → find the log in the console → switch back. New workflow: add console.log → save → see value right next to the line. 5 steps → 1 step.
 
#### Settings

 "console-ninja.toolsToEnableSupportAutomatically": ["live-server", "next.js", "node"] 
 Enable for your specific setup. Works best when you have Live Server or Next.js dev server running.
 
#### Pricing

 Free: core features. Pro $8/month: more runtime info, performance insights. Free tier is sufficient for daily use.
 
#### Alternative

 Quokka.js (similar concept, longer-standing). Both are good — install whichever has better reviews at time of reading.

</details>

Links: —

---

## 🔑 DotENV + ENV File Syntax
**✅ GOOD** · _Environment Variables, Secret Management_

Syntax highlighting for .env files. Makes managing environment variables readable. Pairs with dotenv-vault or 1Password for secret sharing across teams.

<details><summary>Details</summary>

#### What it does

 .env files are plain text with no default syntax highlighting. This extension adds: key names highlighted in one color, values in another, comments in a third. Makes large .env files scannable at a glance.
 
#### Managing env vars properly

 .env : Committed to git — ONLY non-secret defaults. .env.local : Local overrides, NEVER committed (in .gitignore). .env.example : Template with all keys but no values — committed to git. New team members copy .env.example → .env.local → fill in values.
 
#### Required .gitignore entries

 .env
.env.local
.env.*.local
*.pem
*.key 
 Verify nothing sensitive is committed: git log --all --full-history -- "*.env*" 
 
#### Secret rotation workflow

 When a secret is compromised: 1. Immediately rotate in the platform (Supabase, Stripe, etc). 2. Update in Vercel/Railway env vars. 3. Redeploy. 4. Update in your local .env.local. Never try to "clean" git history of a leaked secret — rotate it instead.
 
#### For teams

 Use 1Password Secrets Automation or Doppler for sharing secrets across team. Both integrate with CI/CD to inject secrets at build time. Never share secrets via Slack/email.

</details>

Links: —

---

## 🌈 Indent Rainbow + Better Comments
**✅ GOOD** · _Visual Clarity, Code Readability_

Indent Rainbow: colorizes indentation levels so nested code is instantly readable. Better Comments: color-codes comment types (TODO, FIXME, !, ?) for visual scanning.

<details><summary>Details</summary>

#### Indent Rainbow

 Each indentation level gets a different subtle color: level 1 = light blue, level 2 = light green, level 3 = light yellow, etc. Makes deeply nested code (JSX, complex conditionals, callbacks) far easier to parse visually. No configuration needed — install and it works.
 
#### Better Comments color system

 // TODO: → orange. // FIXME: → red. // ! → red (important). // ? → blue (question). // * → bright green (highlighted). Regular // comments stay gray. Scan a file and immediately see all action items, questions, and important notes.
 
#### Config for Better Comments

 "better-comments.tags": [
 {"tag": "!", "color": "#ef4444", "bold": true},
 {"tag": "?", "color": "#3b82f6"},
 {"tag": "TODO", "color": "#f97316", "bold": true},
 {"tag": "FIXME", "color": "#ef4444", "bold": true},
 {"tag": "*", "color": "#22c55e"}
] 
 
#### Usage pattern

 Use // TODO: for planned work. Use // FIXME: for known bugs. Use // ! for "don't touch this, it's critical." Use // ? for "I'm not sure about this logic." Scan files quickly for all issues.
 
#### Pairing tip

 Use these two together with Error Lens for maximum visual information density while coding.

</details>

Links: —

---

## 🔲 Todo Tree
**🤔 MAYBE** · _TODO Scanner, Task Tracker_

Finds all TODO/FIXME/HACK/NOTE comments across your entire codebase and shows them in a sidebar tree. Useful for solo projects to track in-code tasks without a separate tool.

<details><summary>Details</summary>

#### What it scans

 Searches all files in your workspace for: TODO, FIXME, HACK, NOTE, BUG, XXX (configurable). Groups them by file in a sidebar panel. Click any item → jumps to that line in the file.
 
#### When it's useful vs not

 **Useful**: Solo project, you use comments as your TODO list, you forget which files have TODOs. **Not useful**: Team project with a proper task tracker (Linear, Jira), or you already use Better Comments and grep for TODOs manually.
 
#### Configuration

 "todo-tree.general.tags": ["TODO", "FIXME", "BUG", "HACK", "NOTE"],
"todo-tree.highlights.enabled": true 
 
#### Workflow recommendation

 Pair with Better Comments (colors TODOs in the editor) + Todo Tree (aggregates them all). At the end of a coding session: open Todo Tree → review all outstanding TODOs → prioritize for next session.
 
#### Alternative approach

 Some developers prefer keeping TODOs in a proper system (Linear tickets, Notion page). In-code TODOs get forgotten. The discipline of moving TODOs to a task tracker prevents that.

</details>

Links: —

---
