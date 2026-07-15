# Vibe Sites

[← back to index](../README.md)

11 resources.

## 🌊 Anime.js
**🔥 MUST USE** · _JS Animation, SVG, Timeline, DOM_

Animate anything in the browser — CSS properties, SVG paths, DOM attributes, JavaScript objects. Simple API, powerful timeline control. The go-to for bespoke interactions.

<details><summary>Details</summary>

#### Why not just Framer Motion?

 Framer Motion is React-only and focused on layout animations. Anime.js works anywhere (vanilla JS, React, Vue, any framework) and can animate *anything* — SVG path drawing, scroll-linked animations, staggered list reveals, complex sequenced timelines. For creative/portfolio sites, anime.js is the right tool.
 
#### Core patterns

 // Stagger reveal on scroll
anime({
 targets: '.card',
 opacity: [0, 1],
 translateY: [20, 0],
 delay: anime.stagger(80),
 easing: 'easeOutExpo'
}); 
 
#### SVG path drawing

 The strokeDashoffset animation in anime.js draws SVGs like they're being hand-drawn. For logo animations, illustrated sections, or signature effects — this is the cleanest implementation.
 
#### Timeline control

 Chain multiple animations in sequence or parallel with the timeline API. Build complex multi-step animations (logo in → hero text → CTA button) with exact timing control — no CSS animation juggling.
 
#### Pricing

 Free and open source. V4 (latest) has a new API — check migration guide if using V3 tutorials.

</details>

Links: [animejs.com](https://animejs.com)

---

## 🎨 Layers.to
**🔥 MUST USE** · _Design Inspiration, Best Sites, Curated_

The best website design gallery on the internet. Curated, tagged, and searchable. Every time you need inspiration, check Layers first before opening Dribbble or Behance.

<details><summary>Details</summary>

#### Why it beats Dribbble

 Dribbble shows you UI mockups — pretty but often impractical. Layers shows you *real live websites* — designs that actually shipped and work in production. You see real interactions, real copy, real conversion flows.
 
#### How to use for your projects

 Filter by: industry (SaaS, portfolio, e-commerce), style (minimal, editorial, bold), feature (dark mode, animation, video). When redesigning a site: collect 5-10 references from Layers before starting. Show Claude your references: "I want my site to look like these — [URLs]."
 
#### What to look for

 Nav patterns (how they handle mobile vs desktop). Hero structure (what information goes above the fold). CTA copy (what language converts). Pricing page layout (how they reduce friction). Footer density (what they include vs exclude).
 
#### Pro tip

 Make a Layers collection (they let you bookmark/organize). When you find something you love, save it immediately — you'll never find it again by scrolling.

</details>

Links: [layers.to](https://layers.to)

---

## 🤖 Manus.im
**🔥 MUST USE** · _Agentic AI, Website Designer, Fully Automated_

Agentic AI website designer. Describe your site, Manus autonomously browses for inspiration, writes copy, generates layouts, and produces a complete website. Next-level beyond Lovable or V0.

<details><summary>Details</summary>

#### What makes it different

 Unlike V0 (component-level) or Lovable (single chat turn), Manus is fully agentic — it runs multiple steps autonomously: researching competitors, generating content strategy, writing all copy, creating visual hierarchy, assembling the page. You describe the goal, it builds the full site.
 
#### Best prompt format

 Be specific about: industry, target customer, tone (corporate/startup/creative), what you sell, competitors to draw inspiration from, and what the page needs to achieve (leads, signups, sales). The more context, the better the output.
 
#### Use cases

 Landing pages for new products. Personal portfolio sites. Agency site templates. Coming-soon pages. Event pages. Anywhere speed matters more than 100% custom design.
 
#### When to NOT use it

 When you need full custom control of every element. When brand guidelines are strict. When you need specific integrations baked in (auth, payments, CMS). Use Manus for the first 80%, then hand-edit the remaining 20%.
 
#### Pricing

 Usage-based model — check manus.im for current credits/pricing.

</details>

Links: [manus.im](https://manus.im)

---

## 🎯 Motion.dev
**🔥 MUST USE** · _Framer Motion, Hover Effects, Drag, Layout_

The definitive animation library for React. Smooth hover effects, drag interactions, layout transitions, scroll animations. If you're building in React/Next.js, this is non-negotiable.

<details><summary>Details</summary>

#### Install

 npm install motion (renamed from framer-motion). Import: import {"{ motion, AnimatePresence }"} from 'motion/react' 
 
#### Most-used patterns

 **Hover scale:** {" "} . **Entrance:** {" "} . **Page transitions:** Wrap routes in {" "} . **Drag:** {" "} . **Layout transitions:** Add layout prop — Motion handles reflow animations automatically.
 
#### Scroll animations

 useScroll + useTransform for parallax: tie any CSS value to scroll position. Parallax hero images, fading sections, sticky elements — all possible in ~10 lines.
 
#### Variants (advanced)

 Define animation states as objects, then toggle between them. Parent variants automatically stagger children. This is how you build choreographed page transitions without timing math.
 
#### Performance

 Motion offloads animations to the GPU when possible (transform, opacity). Never animate width/height/margin — use transform: scale instead. The library does this automatically for its built-in animations.

</details>

Links: [motion.dev](https://motion.dev)

---

## ⚡ Skiper UI
**🔥 MUST USE** · _Animated Components, Copy-Paste, Production Ready_

Premium animated UI component library. Drop-in animated cards, buttons, heroes, navbars — all with Tailwind + Framer Motion. No design system needed.

<details><summary>Details</summary>

#### What it is

 Skiper UI is a curated collection of animated UI components designed for landing pages and SaaS products. Every component is ready to copy-paste — no npm install required, just copy the JSX and tailwind classes.
 
#### Best components

 **Animated hero** — text that types itself with gradient. **Bento grids** — animated feature tiles with hover effects. **Glowing cards** — cards with animated border glow. **Magnetic buttons** — buttons that follow your cursor. **Number tickers** — animated counting stats.
 
#### How to use

 1. Browse the component library. 2. Find one you want. 3. Click "Copy Code." 4. Paste into your Next.js/React component. 5. Install any missing deps shown. Most components only need: npm install framer-motion 
 
#### Pro tips

 Mix Skiper components with shadcn/ui for a complete design system. The animated gradient background components are 🔥 for landing page heroes. Pair with Phosphor Icons for consistent iconography.

</details>

Links: [skiper.io](https://skiper.io)

---

## 📱 10x App
**✅ GOOD** · _iOS Submission, App Tools, Developer Utility_

All-in-one app for iOS developers. App Store submission helpers, ASO tools, screenshot generators, review management, and more — designed for indie devs.

<details><summary>Details</summary>

#### Core features

 **App Store submission** — guided checklist for every App Store requirement. **Screenshot generator** — auto-generates all required device sizes from one design. **ASO tools** — keyword research and metadata optimization for App Store ranking. **Review management** — track and respond to reviews across multiple apps. **Revenue tracking** — see earnings across all your apps in one dashboard.
 
#### Best for

 Solo iOS developers and small teams shipping multiple apps. Especially valuable for the screenshot/device size generation — manually exporting screenshots for all device sizes wastes 2+ hours per release.
 
#### Pricing

 Freemium model. Core features free. Some advanced ASO and analytics features behind a subscription. Worth it if you're shipping regularly.

</details>

Links: [10xapp.dev](https://10xapp.dev)

---

## 🧬 AI Website Cloner Template
**✅ GOOD** · _Next.js, Website Cloning, AI Agents_

Reusable template that uses AI coding agents to reverse-engineer any website into a clean Next.js codebase — inspects design, extracts assets, rebuilds components.

<details><summary>Details</summary>

Point an AI agent at a URL; it rebuilds the site as modern Next.js + Tailwind + TypeScript. Good starting point for clone-then-customize builds.

</details>

Links: [GitHub](https://github.com/JCodesMore/ai-website-cloner-template)

---

## 💫 Animista
**✅ GOOD** · _CSS Animations, Visual Builder, No Code_

Visual CSS animation playground. See animations live, tweak timing/easing/direction visually, copy the exact CSS. No more guessing keyframe values.

<details><summary>Details</summary>

#### What it does

 Animista has a massive library of CSS animations grouped by type: entrance (fade, slide, scale, rotate, flip), exit, text, background. You click an animation, see it live on a preview element, tweak the duration/delay/easing with sliders, then copy the generated CSS keyframes.
 
#### Use case: landing pages

 Instead of spending 30 minutes writing and testing a fade-in-up animation for your hero text, open Animista, find "fade-in-up," set duration to 0.4s, ease to cubic-bezier, copy. Done in 2 minutes.
 
#### Combine with Framer Motion

 Animista is for pure CSS animations (no JS required). For React projects with Framer Motion, use Animista to explore what you want visually, then translate the timing values and keyframe logic into Framer Motion variants. Best of both: visual discovery + production-ready implementation.
 
#### Text animations specifically

 The text animation collection is exceptional — letter-spacing animations, character-by-character reveals, typewriter effects. Copy exactly what you see. Works in every browser.

</details>

Links: [animista.net](https://animista.net)

---

## 📊 Bklit UI
**✅ GOOD** · _Charts, Visuals, Dashboard Components_

Beautiful chart and visual components for dashboards. Pre-built data visualizations that actually look good — not the default Recharts grey. For any project with an analytics or stats section.

<details><summary>Details</summary>

#### What it has

 Animated line charts with gradient fills. Bar charts with smooth entrance animations. Donut/pie charts with interactive segments. Stat cards with animated number counts. Sparklines for compact trend display. Heatmaps for calendar/activity views.
 
#### When to use vs Recharts directly

 Recharts gives you the chart primitives — you still need to style them, add tooltips, handle responsiveness. Bklit UI wraps Recharts (or similar) with pre-built styling and interactions. Use Bklit UI when: you want good-looking charts fast. Use Recharts directly when: you need precise custom behavior or an unusual chart type.
 
#### Jarvis dashboard integration

 Bklit UI is ideal for the Jarvis Build dashboard section. Drop in their stat cards for Finance metrics, line chart for health trends, heatmap for learning streaks. Get a production-quality dashboard in one afternoon.
 
#### Pricing

 Check current pricing on site — may have free + pro tiers.

</details>

Links: [bklit UI](https://bklit.ui)

---

## 🥥 Kokonut UI
**✅ GOOD** · _Animated Components, Transitions, Ready-Made_

Ready-made components with built-in animations and transitions. Saves hours of micro-animation work. Copy-paste components that already feel polished and alive.

<details><summary>Details</summary>

#### What's in it

 Animated buttons with ripple/glow effects. Modal transitions with backdrop blur. Notification toasts with entrance/exit animations. Tab switchers with sliding indicator. Dropdown menus with spring physics. Card hover animations with subtle lift + shadow.
 
#### How it differs from shadcn/ui

 shadcn/ui gives you functional, accessible, minimally styled components. Kokonut UI gives you the same components but pre-wired with animations. If your goal is to ship something that looks premium without spending time on micro-interactions, Kokonut UI is the answer.
 
#### Integration approach

 You can mix: use shadcn/ui for complex components (forms, tables, data), use Kokonut UI for the visually prominent elements (hero CTA button, announcement banner, modal, toast). Don't try to use both for the same component type — pick one.
 
#### Customization

 All Tailwind-based — customize by editing the classes. The animation values are explicit in the code so you can adjust duration and easing to match your brand feel.

</details>

Links: [kokonutui.com](https://kokonutui.com)

---

## 🔷 Phosphor Icons
**✅ GOOD** · _Icons, Visual Style, Consistent Design_

The most flexible icon library for vibe coders. 1,000+ icons in 6 weights — thin, light, regular, bold, fill, duotone. One install, consistent across everything.

<details><summary>Details</summary>

#### Why Phosphor over Lucide/Heroicons

 Phosphor has 6 weight variants per icon vs Lucide's 1. This means you can use thin icons for decorative UI and bold for interactive elements — the same icon family at different visual weights. Huge for a cohesive design language.
 
#### Install

 npm install @phosphor-icons/react 
 Usage: import {"{ House, User, Gear }"} from '@phosphor-icons/react' . Each icon accepts a weight prop: "thin" | "light" | "regular" | "bold" | "fill" | "duotone".
 
#### Design rule

 Pick 2 weights max per project. Common pattern: regular for labels and navigation, fill for active/selected states, thin for decorative backgrounds. Never mix more than 2 — it looks inconsistent.
 
#### Duotone variant

 The duotone weight renders each icon with 2 layers — you can color them independently for a premium look. Used heavily in dashboards and hero sections. Set primary color normally, secondary via CSS variable.

</details>

Links: [phosphoricons.com](https://phosphoricons.com)

---
