# IDEs & Dev

[← back to index](../README.md)

10 resources.

## 🚀 Antigravity (Atoms IDE)
**🔥 MUST USE** · _Interactive Portfolio Builder, 3-Phase Build_

The build system behind Atoms-style interactive portfolios. 3-phase approach: Phase 1 (scroll canvas), Phase 2 (video scrub), Phase 3 (mouse scrub + combined). Canvas + GSAP based.

<details><summary>Details</summary>

#### The 3-Phase Atoms Build

 **Phase 1 — Scroll-Driven Canvas**: HTML5 canvas animates as user scrolls. Image sequence or particle system that responds to scroll position. Core technique: listen to scroll events → map scroll % to canvas frame. **Phase 2 — Video Scrub**: A video that plays forward/backward based on scroll position. Load video as frames or as actual video element → update currentTime based on scroll. **Phase 3 — Mouse Scrub**: Canvas or image that responds to mouse X/Y position. Map mouse coordinates to animation frame or transformation. **Combined**: All three working together with GSAP ScrollTrigger.
 
#### Core stack

 HTML5 Canvas, GSAP + ScrollTrigger, vanilla JS (no React needed). Some implementations use Three.js for 3D effects. Vite for bundling.
 
#### Scroll-driven canvas starter code

 const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
const frames = []; // load your image sequence here

window.addEventListener('scroll', () => {
 const progress = window.scrollY / (document.body.scrollHeight - window.innerHeight);
 const frameIndex = Math.floor(progress * (frames.length - 1));
 ctx.drawImage(frames[frameIndex], 0, 0);
}); 
 
#### Video scrub pattern

 const video = document.querySelector('video');
ScrollTrigger.create({
 trigger: ".scrub-section",
 start: "top top",
 end: "bottom bottom",
 onUpdate: self => {
 video.currentTime = self.progress * video.duration;
 }
}); 
 
#### Where to get assets

 Image sequences: export from After Effects (PNG sequence). Videos: export H.264, compress with HandBrake. Use 60-100 frames for smooth scroll animation — more is heavier, fewer looks choppy.
 
#### Deployment

 Static files → deploy to Vercel or Netlify. Optimize images with imagemin. Use IntersectionObserver to lazy-load off-screen canvas work.

</details>

Links: [atoms.ac](https://atoms.ac)

---

## ⚡ Bolt.new
**🔥 MUST USE** · _In-Browser Full-Stack, WebContainers_

StackBlitz's AI builder that runs Node.js in the browser (WebContainers). Generates full-stack apps, runs npm, installs packages, hot-reloads — all in a tab. No setup required.

<details><summary>Details</summary>

#### Why Bolt is uniquely useful

 Other AI builders (V0, Lovable) generate code you then run locally. Bolt runs the code IN the browser using WebContainers technology. This means: instant preview, no local setup, zero environment issues, and you can share a link to a live running app. It's the fastest path from idea to working prototype.
 
#### Getting the best results

 **Be specific about stack**: "Build a Next.js 14 app with TypeScript and Tailwind." If you don't specify, Bolt picks defaults that may not be what you want. **Start simple**: Get a basic version working first, then add features. Complex prompts on first try often produce broken code. **Use the diff view**: Bolt shows what it changed. Review before accepting.
 
#### Best for

 Hackathons (zero setup time), demos you need to share a URL for, quick prototypes to show clients, learning a new framework without configuring a local environment, Node.js scripts and tools.
 
#### Limitations

 No persistent storage in free tier (DB resets on reload), WebContainers can't do everything a real server does (no raw TCP, limited native modules). Not ideal for projects that need a real backend with file system access or custom OS packages.
 
#### Export to local

 When you've prototyped in Bolt and want to go further: "Export" → downloads your project as a zip → open in Cursor for production development. Clean handoff.
 
#### Pricing

 Free: 50k tokens/day AI usage. **Basic $20/month**: 10M tokens. **Pro $50/month**: 50M tokens. Tokens go fast on complex apps.

</details>

Links: [bolt.new](https://bolt.new)

---

## 🎨 Google Stitch (DESIGN.md)
**🔥 MUST USE** · _AI Design System, UI Generation_

Google's AI design tool that generates UI from descriptions + creates DESIGN.md files — a markdown design system description that Claude can read to maintain visual consistency across generated code.

<details><summary>Details</summary>

#### What DESIGN.md is

 A markdown file that describes your design system: colors, typography, spacing, component styles, tone. When placed in a project, Claude Code reads it and generates code that matches your aesthetic. It's like giving Claude a style guide.
 
#### Creating a DESIGN.md with Stitch

 1. Go to Google Stitch (labs.google). 2. Describe your app and desired aesthetic. 3. Stitch generates UI mockups and a corresponding DESIGN.md. 4. Save the DESIGN.md to your project root. 5. Claude Code will reference it automatically when generating components.
 
#### DESIGN.md structure

 # Design System

## Colors
- Primary: #7c6af5
- Background: #0f0f13
- Surface: #16161d

## Typography
- Headings: Inter, 700 weight
- Body: Inter, 400, 1.6 line-height

## Components
- Cards: 12px border-radius, 1px border
- Buttons: pill-shaped, 8px 20px padding 
 
#### Using with SkillUI

 SkillUI ( npx skillui ) can extract a DESIGN.md from any live URL — reverse engineers a site's design system by analyzing CSS. Combine: extract DESIGN.md from a site you like → put in project → Claude generates matching components.
 
#### awesome-design-md collection

 GitHub: voltagent/awesome-design-md — 73+ DESIGN.md files for major brands (Apple, Notion, Linear, Vercel, etc). Drop any of these in your project to instantly inherit that brand's aesthetic.
 
#### Pricing

 Google Stitch: free (Google Labs). SkillUI: free CLI.

</details>

Links: [Google Labs](https://labs.google) · [awesome-design-md](https://github.com/voltagent/awesome-design-md)

---

## ▲ V0 by Vercel
**🔥 MUST USE** · _Component Generator, shadcn, ui, React_

Vercel's AI component generator. Describe or screenshot → get production React components with shadcn/ui + Tailwind. Copy component code directly into your project. Best UI generation tool available.

<details><summary>Details</summary>

#### The two ways to use V0

 **Text description**: "Create a pricing table with 3 tiers (Free, Pro, Enterprise), monthly/annual toggle, feature comparison, and highlighted recommended tier. Use a dark theme with purple accents." **Image reference**: Screenshot any UI you like → drag into V0 → "Build this component with [your colors/content]." Image-to-component is extremely powerful.
 
#### Getting high-quality output

 Specify: component type (card, modal, form, table), theme (dark/light, specific colors), state (hover, active, loading), responsiveness requirements, specific behaviors (drag-drop, sortable, expandable). Vague prompts → generic output. Specific prompts → production-ready code.
 
#### Iterating

 V0 has a conversation interface — keep iterating in the same thread. "Make the buttons larger," "Add a loading skeleton state," "Make it mobile-first." You get version history and can revert. Much faster than editing code manually.
 
#### Shadcn/ui compatibility

 V0 outputs standard shadcn/ui components. If your project has shadcn/ui installed, you just paste the component — it automatically uses your theme variables. Zero extra styling work.
 
#### Export to Cursor

 V0 has a "Sync with Cursor" button in some configurations. Otherwise: copy code → paste into new file in Cursor → done. V0 for UI scaffolding, Cursor for logic and integration.
 
#### Pricing

 Free: 200 credits/month. **Premium $20/month**: 5000 credits. Most components cost 20-40 credits. Free tier is workable for occasional use.

</details>

Links: [v0.dev](https://v0.dev)

---

## 🎨 Figma → Code (Dev Mode)
**✅ GOOD** · _Design-to-Code, CSS Export, Tokens_

Figma's Dev Mode exports CSS, React components, and design tokens directly from designs. Use when working from a designer's Figma file. Saves hours of manual CSS translation.

<details><summary>Details</summary>

#### Dev Mode workflow

 1. Open Figma file in Dev Mode (switch in top bar). 2. Select any element → see CSS properties in right panel. 3. Click "Copy as CSS" → paste directly into your stylesheet. For React: select frame → "Copy as React" exports a component with inline styles or Tailwind classes (depending on your Figma plugin).
 
#### Figma + Claude Code workflow

 Screenshot a Figma design section → paste into Claude Code: "Build this component exactly as shown. Use Tailwind CSS. The design shows [describe key elements]. Match the spacing, typography, and colors." Claude can translate Figma screenshots to code faster than reading CSS values manually.
 
#### Design tokens

 Use the Figma Tokens plugin to export your design system as a JSON file (colors, spacing, typography). Import into your CSS custom properties or a tokens package. Keeps design and code in sync when designers change the design system.
 
#### Plugins that make this faster

 **Figma to Code**: Exports components to React, Vue, HTML, Tailwind automatically. **Locofy.ai**: More sophisticated AI export to production-quality component code. **Anima**: Full prototype to React export.
 
#### When not to rely on auto-export

 Auto-generated code is often verbose and hard to maintain. Use it for: getting exact values (colors, spacing, border-radius), understanding layout structure. Then write clean, semantic code yourself rather than shipping auto-generated output.

</details>

Links: [Figma](https://figma.com)

---

## 🔥 Firebase Studio
**✅ GOOD** · _Google AI IDE, App Prototyper_

Google's full-stack AI development environment. Gemini-powered code generation + Firebase backend + cloud preview. Good for apps that need Firebase/Firestore.

<details><summary>Details</summary>

#### What makes Firebase Studio different

 Tightly integrated with Google's Firebase ecosystem: Firestore database, Firebase Auth, Cloud Functions, Firebase Hosting. If your app needs any of these, Firebase Studio generates code that directly uses the real Firebase SDK — no glue code needed.
 
#### App Prototyper feature

 Built-in "App Prototyper" mode: describe your app → AI generates a working prototype in minutes → shows live preview. Similar to Bolt/Lovable but with Firebase as the default backend.
 
#### Gemini integration

 Uses Gemini 1.5 Pro for code generation. Strong at: multi-modal inputs (paste a screenshot of a UI), long-context understanding, Google API integrations (Maps, YouTube, Calendar). Choose Firebase Studio over Bolt/Lovable when your app needs Google services.
 
#### Cloud preview

 Every project gets a shareable preview URL. No manual deployment — click "Preview" and get a link you can share immediately. Useful for client demos.
 
#### Pricing

 Free during preview phase. Firebase backend costs: Firestore charges per read/write (Spark plan: 50k reads/day, 20k writes/day free). More than enough for development and small production apps.
 
#### When to prefer over Lovable/Bolt

 Your app uses Firebase Auth (especially Google Sign-In), Firestore real-time data, Cloud Functions, or you need Gemini API access. Otherwise Lovable + Supabase is more flexible.

</details>

Links: [Firebase Studio](https://firebase.google.com/studio)

---

## 📱 FlutterFlow
**✅ GOOD** · _No-Code Flutter, Mobile Apps, Firebase_

Visual Flutter app builder. Drag-and-drop UI + logic, then export real Flutter/Dart code. If you need native mobile (iOS + Android) without deep Flutter knowledge, this is your tool.

<details><summary>Details</summary>

#### What FlutterFlow produces

 Real Flutter/Dart code — not a wrapper or WebView. Apps built in FlutterFlow are indistinguishable from hand-coded Flutter apps at the Dart level. You can export the code and continue in VS Code or Android Studio at any point.
 
#### Build workflow

 1. Create project → choose platform (iOS, Android, web). 2. Drag UI components onto canvas. 3. Set data bindings (connect to Firebase Firestore, Supabase, or custom API). 4. Add logic with Action Flows (visual event handling). 5. Preview on device (FlutterFlow app on phone). 6. Publish: one-click to App Store Connect / Google Play internal testing.
 
#### Firebase integration

 Native Firestore integration — point-and-click queries, real-time listeners, Firebase Auth with Google Sign-In. No code needed for basic CRUD. For complex queries: write custom Dart code in "Custom Action" blocks.
 
#### When to export code

 Export when: you need custom animations, complex state management (Riverpod, Bloc), native OS APIs, performance optimization, or features FlutterFlow doesn't support. Code export is a one-way door — you can continue in FlutterFlow after export but it gets messy.
 
#### Pricing

 Free: test on emulator, limited features. **Standard $30/month**: custom code, API integrations, deploy to stores. **Pro $70/month**: team features, white-labeling.
 
#### Alternative

 If your app is web-first and doesn't need truly native mobile: use Lovable/Next.js with Capacitor to wrap as an app instead.

</details>

Links: [flutterflow.io](https://flutterflow.io)

---

## ✅ Pre-Launch Production Checklist
**✅ GOOD** · _Deploy Checklist, Security, Performance_

Everything to verify before launching any app. Security, performance, SEO, auth, error handling. Save this. Run it before every deploy that goes public.

<details><summary>Details</summary>

#### Security checklist

 ☐ No secrets in .env committed to git ( git log --all --full-history -- .env* ). ☐ All API routes authenticated. ☐ Supabase RLS enabled on all tables. ☐ Input validation on all forms (Zod). ☐ CORS configured correctly. ☐ Rate limiting on auth endpoints. ☐ HTTPS enforced. ☐ No console.log() with sensitive data.
 
#### Performance checklist

 ☐ Images optimized (WebP/AVIF, next/image for Next.js). ☐ Fonts: subset, preloaded. ☐ Core Web Vitals green in Vercel Analytics. ☐ No unused dependencies. ☐ Code splitting working (check bundle analyzer). ☐ Caching headers set for static assets.
 
#### Functionality checklist

 ☐ Auth flow tested: sign up, log in, forgot password, log out. ☐ All forms submit and validate. ☐ Error states shown (not just success states). ☐ Loading states on all async operations. ☐ Empty states designed. ☐ 404 and error pages exist. ☐ Mobile tested on real device (not just browser resize).
 
#### Monitoring checklist

 ☐ Sentry or equivalent error tracking installed. ☐ Uptime monitoring (UptimeRobot free tier). ☐ Analytics (Plausible, Vercel Analytics, or GA4). ☐ Payment webhooks tested in Stripe test mode.
 
#### SEO checklist

 ☐ Meta title and description on all pages. ☐ Open Graph tags (og:title, og:image) for social sharing. ☐ sitemap.xml generated. ☐ robots.txt configured. ☐ No broken links.

</details>

Links: —

---

## 🧩 Replit
**✅ GOOD** · _Cloud IDE, Instant Deploy, Learn_

Browser-based IDE with AI assistant, instant deployment, and multiplayer editing. Best for: learning environments, collaboration, quick Python/Node scripts without local setup.

<details><summary>Details</summary>

#### Best use cases

 **Learning**: Zero environment setup. Open browser → start coding in Python, JS, Go, Ruby, Rust. Perfect for picking up a new language without installation friction. **Teaching**: Share a Repl link → collaborator joins with a cursor. Real-time pair programming. **Quick scripts**: Need to run a Python script that scrapes something? Replit is faster than setting up a local venv. **Background tasks**: Keep a Repl running 24/7 (paid tier) for bots, cron jobs, APIs.
 
#### Replit AI (Ghostwriter)

 AI assistant built in. Complete code, explain errors, refactor selections. Similar to GitHub Copilot but inside the browser. Quality is decent for learning but less powerful than Cursor for serious projects.
 
#### Deployment

 Every Repl gets a URL instantly (repl.co domain). No Vercel/Heroku needed for simple projects. Custom domains on paid plan. For production apps: still better to use Vercel/Railway, but Replit is fine for personal tools and demos.
 
#### Database options

 Replit DB: built-in key-value store (simple, no SQL). For relational data, connect to Supabase or use SQLite within the Repl. Replit also supports PostgreSQL add-on on paid plans.
 
#### Pricing

 Free: basic Repls, 1 "Always On" Repl. **Core $25/month**: more compute, Always On Repls, more storage, custom domains. Use free tier for learning, paid only if you're running production workloads on Replit.

</details>

Links: [replit.com](https://replit.com)

---

## 🧩 Chrome Extension Builder
**🤔 MAYBE** · _Extension Scaffold, Manifest V3_

AI tools and templates for building Chrome extensions with Manifest V3. Faster scaffold than starting from scratch. Good for adding browser automation and productivity tools.

<details><summary>Details</summary>

#### Chrome extension structure

 **manifest.json**: Config file (name, permissions, icons, background script declaration). **background.js**: Service worker (Manifest V3) — runs in background, handles events, API calls. **content.js**: Script injected into web pages — reads/modifies DOM. **popup.html**: UI that appears when you click the extension icon.
 
#### Build with Claude Code

 "Build a Chrome extension that: [description]. Use Manifest V3. Include: manifest.json, background service worker, content script for [specific site], and a popup UI. Show the complete file structure." Claude generates all files. Load in Chrome: chrome://extensions → Developer mode → Load unpacked → select folder.
 
#### Useful permissions to know

 tabs : Read tab URL/title. activeTab : Access current tab content. storage : Save settings persistently. scripting : Inject scripts into pages. notifications : Show OS notifications. Minimize permissions — Chrome Web Store reviewers flag over-permissioned extensions.
 
#### Useful extension ideas

 Save selected text to Notion/Obsidian, summarize the current page with Claude, add keyboard shortcuts to any site, auto-fill repetitive forms, capture LinkedIn profiles to your CRM, highlight keywords on job boards.
 
#### Publishing to Chrome Web Store

 $5 one-time developer fee. Submit ZIP → review takes 1-3 days. Need screenshots, description, privacy policy. Keep it focused — extensions with one clear purpose get approved faster.

</details>

Links: —

---
