# Full Stack

[← back to index](../README.md)

6 resources.

## ▲ Next.js App Router — Key Patterns
**🔥 MUST USE** · _Server Components, Data Fetching, Routing_

Next.js 14 App Router fundamentals — the mental model shift from Pages Router, Server vs Client Components, data fetching, layouts. What changed and why it matters.

<details><summary>Details</summary>

#### The single most important rule

 Server Components (default in App Router) run on the server — can access DB directly, can't use hooks or browser APIs. Client Components ( 'use client' at top) run in browser — can use hooks, can't directly access DB. Wrong: making everything a Client Component (what everyone does by accident). Right: Server Component fetches data, passes as props to Client Component for interactivity.
 
#### Correct data fetching

 // app/dashboard/page.tsx — Server Component (NO 'use client')
export default async function DashboardPage() {
 // Runs on server — direct DB access, no loading state
 const { data: tasks } = await supabase.from('tasks').select();
 return <TaskList tasks={tasks} />; // TaskList is a Client Component
} 
 
#### Folder structure (App Router)

 app/
├── layout.tsx # Root layout (wraps everything)
├── page.tsx # Home page
├── (auth)/ # Route group (no URL segment)
│ ├── login/page.tsx
│ └── signup/page.tsx
├── dashboard/
│ ├── layout.tsx # Dashboard layout (sidebar, nav)
│ ├── page.tsx # Dashboard home
│ └── [id]/page.tsx # Dynamic route
└── api/
 └── webhook/route.ts # API route 
 
#### Special files

 loading.tsx → shows while page.tsx data fetches (Suspense boundary). error.tsx → error boundary, shown on unhandled errors. not-found.tsx → 404 page. middleware.ts → runs before every request (auth checks, redirects). layout.tsx → wraps children, persists across navigation.
 
#### Common mistake to avoid

 Fetching data client-side with useEffect when you could fetch server-side. Server-side is: faster (no client-server round trip), safer (DB credentials never leave server), better for SEO. Default to server components, add 'use client' only when you need hooks/events.

</details>

Links: [Next.js Tutorial](https://learn.nextjs.org)

---

## 🏗️ Recommended Stack 2025
**🔥 MUST USE** · _Next.js, Supabase, Tailwind, Full Blueprint_

The optimal stack for building production apps in 2025 — industry standard, great AI tooling support, strong community, everything deployed for under $10/month.

<details><summary>Details</summary>

#### The stack

 **Frontend**: Next.js 14 (App Router) + TypeScript (strict) + Tailwind CSS v3 + shadcn/ui + Framer Motion. **State**: React Query (server state) + Zustand (client state) + React Hook Form + Zod (forms). **Backend**: Next.js API Routes (simple CRUD) / FastAPI Python (AI-heavy or complex logic). **Database**: Supabase (PostgreSQL + Auth + Storage + Realtime). **Payments**: Stripe. **Email**: Resend. **Deployment**: Vercel (frontend) + Railway (backend) + Supabase cloud (DB). **Monitoring**: Sentry (errors) + Plausible (analytics).
 
#### Why this stack specifically

 Every tool: has excellent documentation, is actively maintained, has strong community support, integrates well with AI builders (Lovable, V0, Cursor all target this exact stack), is used at real companies. You're learning what the industry actually uses.
 
#### Monthly cost at student scale

 Vercel: free. Supabase: free tier (500MB DB, 50k MAU). Railway: $5/month after trial. Resend: free (3k emails/month). Sentry: free. Plausible: $9/month. Total: $14/month for a production-grade full-stack app serving real users. Scale costs linearly with usage.
 
#### AI builder compatibility

 Lovable generates this stack by default. V0 generates shadcn/ui components. Cursor's .cursorrules is written for this stack. Claude Code understands all these tools deeply. The AI tooling is optimized for this exact combination — any other stack choice means less effective AI assistance.
 
#### When to deviate

 Need native mobile → add React Native (Expo) or Flutter. Need heavy ML inference → add FastAPI + PyTorch on Railway. Need real-time collaborative features → Supabase Realtime is built-in. Need search → Algolia (free 10k records) or Supabase full-text search.

</details>

Links: —

---

## 🗄️ Supabase — Complete Reference
**🔥 MUST USE** · _PostgreSQL, Auth, Storage, Realtime_

The complete backend-as-a-service. PostgreSQL, Auth, file storage, edge functions, realtime. Generous free tier. The entire backend for most student projects.

<details><summary>Details</summary>

#### Core services (and when to use each)

 **Database**: Full PostgreSQL. Write real SQL. Use for: all structured data (users, posts, transactions, etc). **Auth**: Email/password, OAuth (Google, GitHub, Apple, etc.), magic links, phone OTP. Handles sessions, JWTs, refresh tokens. Use for: all user authentication. **Storage**: File upload/download with access policies. Use for: user avatars, uploaded documents, product images. **Realtime**: Subscribe to table changes. Use for: live feeds, collaborative features, notifications. **Edge Functions**: Deno-based serverless functions at Supabase's infrastructure. Use for: webhooks, scheduled tasks, auth hooks.
 
#### RLS is not optional

 Enable RLS on every table. Without it: every user can read/write every row. Example policy:
 CREATE POLICY "Users see only their data"
ON tasks FOR ALL
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id); 
 The MCP + Claude Code workflow: "Add RLS policies for the [table] table so users can only see their own records." Claude writes the SQL, you review, apply.
 
#### supabase-js query patterns (memorize these 5)

 // Select
const { data } = await supabase.from('tasks').select('*').eq('user_id', uid);
// Insert
await supabase.from('tasks').insert({ title, user_id: uid });
// Update
await supabase.from('tasks').update({ done: true }).eq('id', id);
// Delete
await supabase.from('tasks').delete().eq('id', id);
// Realtime
supabase.channel('tasks').on('postgres_changes', { event: '*', schema: 'public', table: 'tasks' }, payload => setTasks(prev => [...prev, payload.new])).subscribe(); 
 
#### Local development

 npx supabase start — runs a full Supabase stack locally (Docker). Make schema changes locally → test → supabase db push to production. Never make schema changes directly in production dashboard.

</details>

Links: [supabase.com/docs](https://supabase.com/docs)

---

## 🤖 Claude API — Integration Patterns
**✅ GOOD** · _Streaming, Cost Routing, Structured Output_

Production Claude API integration patterns — streaming responses, cost routing between models, structured JSON output with Zod, and prompt caching for system prompts.

<details><summary>Details</summary>

#### Basic streaming (Next.js + Vercel AI SDK)

 // app/api/chat/route.ts
import { anthropic } from '@ai-sdk/anthropic';
import { streamText } from 'ai';
export async function POST(req: Request) {
 const { messages } = await req.json();
 const result = streamText({
 model: anthropic('claude-sonnet-4-6'),
 system: 'You are a helpful assistant.',
 messages
 });
 return result.toDataStreamResponse();
} 
 
#### Cost routing pattern

 Use Haiku for cheap tasks, Sonnet for reasoning:
 function selectModel(task: string) {
 const cheapTasks = ['classify', 'categorize', 'extract', 'yes/no'];
 const isCheap = cheapTasks.some(t => task.includes(t));
 return isCheap ? anthropic('claude-haiku-4-5-20251001') : anthropic('claude-sonnet-4-6');
}
// Haiku: $0.25/1M input tokens. Sonnet: $3/1M. 12x cost difference. 
 
#### Structured output (guaranteed JSON)

 import { generateObject } from 'ai';
import { z } from 'zod';
const { object } = await generateObject({
 model: anthropic('claude-haiku-4-5-20251001'),
 schema: z.object({
 category: z.enum(['bug', 'feature', 'question']),
 priority: z.number().min(1).max(5),
 summary: z.string().max(100)
 }),
 prompt: `Classify this support ticket: ${ticket}`
});
// object.category is guaranteed to be 'bug' | 'feature' | 'question' 
 
#### Prompt caching (saves 90% on repeated system prompts)

 For system prompts > 1024 tokens: add cache_control: {type: 'ephemeral'} . Cached tokens cost 10% of normal input price. Cache TTL: 5 minutes. Break-even: 2+ requests with same system prompt in 5 min.
 
#### Extended thinking

 For complex reasoning: thinking: {type: 'enabled', budgetTokens: 10000} . Claude shows its reasoning chain. Better accuracy on: math, logic, multi-step planning. Higher cost — use selectively.

</details>

Links: [Anthropic Docs](https://docs.anthropic.com) · [Vercel AI SDK](https://sdk.vercel.ai)

---

## ⚡ Deployment — Vercel + Railway
**✅ GOOD** · _CI, CD, Custom Domains, Production_



<details><summary>Details</summary>

#### Vercel for Next.js (the obvious choice)

 Push to GitHub → connect to Vercel → auto-deploys on every push to main. Preview deployments for every branch/PR — share with stakeholders before merging. Environment variables in Vercel dashboard → never in code. Custom domain: add in Vercel → update nameservers to Vercel or add DNS record → works in minutes.
 
#### Deployment checklist before adding custom domain

 ☐ All environment variables set in Vercel dashboard. ☐ Build passes ( npm run build locally first). ☐ No hardcoded localhost URLs. ☐ Database (Supabase) production project created (not using local). ☐ Stripe webhook URL updated to production URL. ☐ Any OAuth redirect URLs updated (Supabase Auth settings).
 
#### Railway for Python backends

 FastAPI or Express: push to Railway → Railway auto-detects (Procfile or nixpacks). Set env vars in Railway dashboard. $5/month after free trial. Add-ons: PostgreSQL, Redis, MongoDB — all managed. For Python: Railway detects requirements.txt or pyproject.toml automatically.
 
#### Healthcheck endpoint

 Always add: GET /health → {status: 'ok', timestamp: Date.now()} . Railway and Vercel use this to confirm deployment is live. Configure in Railway as healthcheck path.
 
#### Domain setup (Cloudflare DNS)

 Buy domain on Cloudflare (~$10/year) → in Vercel: add domain → Vercel gives you DNS records → add to Cloudflare → SSL certificate auto-provisioned. Cloudflare adds: DDoS protection, global CDN, free. Takes 5-10 minutes total.
 
#### Rollback

 Vercel: every deployment is immutable and stored. Broken deploy → go to Vercel dashboard → previous deploy → "Promote to Production." Instant rollback, no downtime.

</details>

Links: [Vercel Docs](https://vercel.com/docs) · [Railway Docs](https://railway.app/docs)

---

## 💳 Stripe Integration Reference
**✅ GOOD** · _Payments, Subscriptions, Webhooks_

The correct Stripe integration pattern — checkout sessions, webhooks (source of truth), subscriptions, and testing. The pattern that works without breaking in production.

<details><summary>Details</summary>

#### The golden rule of Stripe

 NEVER trust the redirect URL to confirm payment. The success URL tells you the user completed checkout — it doesn't tell you the payment succeeded. Always verify via webhook. Webhooks are the source of truth.
 
#### One-time payment flow

 // 1. Create checkout session (server-side only)
const session = await stripe.checkout.sessions.create({
 mode: 'payment',
 line_items: [{ price: 'price_xxx', quantity: 1 }],
 success_url: `${origin}/success?session_id={CHECKOUT_SESSION_ID}`,
 cancel_url: `${origin}/cancel`,
});
// 2. Redirect user to session.url
// 3. Stripe redirects to success_url after payment
// 4. Webhook confirms: checkout.session.completed → update DB 
 
#### Subscription flow

 Same pattern but mode: 'subscription' . Key webhooks to handle: checkout.session.completed → grant access. customer.subscription.updated → update plan. customer.subscription.deleted → revoke access. invoice.payment_failed → send dunning email.
 
#### Webhook verification

 const event = stripe.webhooks.constructEvent(
 req.body, // raw body (not parsed JSON)
 req.headers['stripe-signature'],
 process.env.STRIPE_WEBHOOK_SECRET
); // throws if signature invalid 
 
#### Testing

 Test cards: 4242424242424242 (success), 4000000000000002 (declined), 4000000000009995 (insufficient funds). Run local webhook testing: stripe listen --forward-to localhost:3000/api/webhooks/stripe . Test every subscription lifecycle event before going live.
 
#### Customer Portal

 stripe.billingPortal.sessions.create({customer: stripeCustomerId, return_url: ...}) → managed subscription page where users can cancel, update payment method, view invoices. No code needed for self-serve subscription management.

</details>

Links: [stripe.com/docs](https://stripe.com/docs)

---
