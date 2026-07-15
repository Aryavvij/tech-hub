# Jarvis Build

[← back to index](../README.md)

13 resources.

## 🌅 Daily Operations Module
**🔥 MUST USE** · _Morning Brief, Habits, Planning, Review_

Jarvis Daily Ops: automated morning brief at 7am (Slack), habit tracking, daily planning session, and evening review. The infrastructure for consistent daily routines.

<details><summary>Details</summary>

#### Morning brief (Vercel Cron at 7am)

 // api/cron/morning-brief.ts
export async function GET() {
 const [habits, calendar, dueCards, topPriorities, weather] = await Promise.all([
 getHabitsDueToday(),
 getCalendarEvents(today),
 getDueFlashcards(),
 getTopPriorities(3),
 getWeatherSummary()
 ]);
 
 const brief = await claude.messages.create({
 model: 'claude-haiku-4-5',
 messages: [{role: 'user', content: `Generate a focused morning brief:
 Habits: ${JSON.stringify(habits)}
 Calendar: ${JSON.stringify(calendar)}
 Due cards: ${dueCards.length}
 Priorities: ${JSON.stringify(topPriorities)}
 Weather: ${weather}
 Keep it under 200 words. Be direct, not fluffy.`}]
 });
 
 await slack.chat.postMessage({channel: '#jarvis', text: brief.content[0].text});
} 
 
#### Habit tracking schema

 habits (id, name, frequency: daily|weekly, target_count, streak, last_completed)
habit_logs (id, habit_id, completed_at, notes) 
 Mark habits via Slack: "/done gym" → bot finds habit → logs completion → updates streak → replies "💪 Gym logged! Streak: 5 days." Simple slash commands via Slack Events API.
 
#### Daily planning session

 "What are my top 3 priorities for today? Context: [paste current projects, deadlines, energy level]. Consider: what moves the needle most, what's been avoided too long, what has an imminent deadline. Suggest 3 priorities as: [priority]: [why it matters today]."
 
#### Evening review (9pm Cron)

 Fetch today's habit completions, calendar completed events, priorities marked done. Slack message: "🌙 Day review: Habits: 3/5 (gym✅ reading✅ meditation❌ cold shower❌ journaling✅). Priorities: 2/3 done. What went well? What would you do differently?" User replies → stored as reflection → feeds weekly review.
 
#### Weekly retrospective (Sunday 6pm)

 Aggregate the week's data → send to Claude → generate: patterns noticed, wins to celebrate, one thing to improve next week, updated priorities. 10-minute Sunday ritual that compounds over time.

</details>

Links: —

---

## 💰 Finance Intelligence Module
**🔥 MUST USE** · _Portfolio, Net Worth, Spending Analysis_

Jarvis Finance: automated net worth tracking, spending categorization, investment analysis, and monthly financial review with AI insights. Your personal CFO.

<details><summary>Details</summary>

#### Data sources

 **Plaid API**: Bank + credit card transactions, account balances. Free for 100 Items (accounts). **Manual CSV**: Investment accounts (export from Fidelity/Schwab/Robinhood). **Crypto**: CoinGecko API (free, no key needed) for portfolio prices. **Real estate**: Manual input, Zillow estimate URL. All data lands in Supabase.
 
#### Database schema

 accounts (id, name, type: checking|savings|investment|crypto, institution, current_balance, updated_at)
transactions (id, account_id, date, amount, description, category, merchant)
net_worth_history (id, date, total_assets, total_liabilities, net_worth)
budgets (id, category, monthly_limit, year, month)
investment_positions (id, account_id, symbol, shares, avg_cost, current_price) 
 
#### Monthly financial review prompt

 "Here is my financial data for [month]: [paste JSON with transactions, balances, investments]. Generate my monthly financial review: 1) Net worth change vs last month, 2) Top spending categories with amounts, 3) Unusual transactions worth flagging, 4) Investment portfolio performance, 5) Progress toward financial goals: [list goals], 6) One specific action to improve finances this month."
 
#### Spending categorization (Claude)

 Feed uncategorized transactions to Haiku: "Categorize each transaction: {transactions}. Return JSON array with {id, category} where category is one of: Housing, Food, Transportation, Entertainment, Health, Education, Shopping, Subscriptions, Income." Fast and accurate — Haiku handles this well.
 
#### Weekly budget check

 Vercel Cron every Sunday: fetch week's transactions → categorize → compare to budgets → generate summary → send to Slack: "💰 Week in review: $340 spent. Food: $120 (budget: $150 ✅). Entertainment: $95 (budget: $50 ⚠️). You're $45 over entertainment budget this week."

</details>

Links: —

---

## 📊 Jarvis Dashboard (Next.js)
**🔥 MUST USE** · _Central UI, Real-Time, Multi-Domain View_

The central Jarvis web dashboard. Domain overview cards, habit streaks, net worth chart, due cards, calendar today, and a central command input. Everything visible at a glance.

<details><summary>Details</summary>

#### Dashboard layout

 Top: command input bar ("Ask Jarvis anything…"). Left column: Today's calendar + habits checklist + 3 priorities. Center: Net worth chart (last 12 months) + spending breakdown pie. Right column: Due flashcards count + learning streak + recent research notes.
 
#### Command input (the key feature)

 Single input at top: user types anything → Jarvis classifies intent → routes to correct domain → returns response below input. "What did I spend on food last month?" → Finance domain. "Schedule a review of [topic] for next Tuesday" → Learning + Daily Ops. "What's my current learning streak?" → Learning domain.
 
#### Real-time habit checklist

 Each habit as a clickable checkbox. Click → Supabase update → optimistic UI (immediate visual update). Streak counter updates live. "🔥 5 day streak" animates when you hit milestones.
 
#### Net worth chart

 Recharts LineChart (already in your tech stack). Data: net_worth_history table, last 12 months. Show: total assets line, liabilities line, net worth line. Hover tooltip with exact values. Positive delta since last month shown in green header stat.
 
#### Mobile-first considerations

 Dashboard on phone: single column. Most-used features at top: habits checklist + today's priorities. Charts collapse to just the key number. Command input always visible (sticky bottom bar on mobile). You'll check Jarvis on your phone every morning — make mobile experience perfect.
 
#### Dark theme tokens

 All Jarvis domain colors distinct: Finance: green (#22c55e), Health: red (#ef4444), Learning: blue (#3b82f6), Career: orange (#f97316), Research: purple (#a78bfa), Daily Ops: cyan (#06b6d4). Each domain's cards use its color as the accent.

</details>

Links: —

---

## 🏗️ Jarvis System Architecture
**🔥 MUST USE** · _6-Domain Blueprint, Tech Stack, Agent Design_

The complete Jarvis architecture: 6 specialized AI domains (Finance, Health, Learning, Career, Research, Daily Ops), central orchestrator, shared memory layer, and multi-channel delivery (Slack, email, dashboard).

<details><summary>Details</summary>

#### System overview diagram

 User Input (voice/text/scheduled)
 ↓
 Orchestrator (intent routing)
 ├── Finance Agent ← Plaid API, portfolio data
 ├── Health Agent ← Apple Health export, Cronometer
 ├── Learning Agent ← SM-2 scheduler, notes index
 ├── Career Agent ← job tracker, resume versions
 ├── Research Agent ← Wiki-Brain, Exa search
 └── Daily Ops Agent ← calendar, habits, priorities
 ↓
 Shared Memory (Supabase + BRAIN.md)
 ↓
 Delivery Layer (Slack / Email / Dashboard / Voice) 
 
#### Tech stack decision rationale

 **Next.js 14**: Dashboard + API routes in one project. Server components for data fetching. **Supabase**: PostgreSQL for all structured data (transactions, habits, bookings). Row Level Security so each domain only reads its tables. **Claude API**: claude-haiku-4-5 for routine responses (fast, cheap), claude-sonnet-4-6 for complex reasoning. **Vercel Cron**: Scheduled tasks (daily brief, weekly review, SM-2 due reviews). **Slack API**: Primary delivery channel for daily briefings and alerts.
 
#### Domain isolation strategy

 Each domain has: dedicated Supabase tables, dedicated Claude system prompt (tuned for domain expertise), dedicated MCP tools, dedicated memory file (finance-context.md, health-context.md etc). Isolation prevents context bleeding between domains. Orchestrator routes to the right domain based on intent classification.
 
#### Build sequence

 Phase 1: Dashboard shell + auth + DB schema. Phase 2: Daily Ops domain (simplest — habits + calendar). Phase 3: Learning domain (SM-2 + notes). Phase 4: Finance domain (highest value). Phase 5: Health + Career + Research. Phase 6: Voice interface + automation. Don't try to build all 6 domains simultaneously.
 
#### Cost estimate at full operation

 Claude API: ~$3-8/month (using Haiku for routine, Sonnet for analysis). Supabase: free tier (500MB, more than enough). Vercel: free tier. Slack: free. Total: <$10/month for a sophisticated personal AI system.

</details>

Links: —

---

## 📚 Learning Accelerator Module
**🔥 MUST USE** · _SM-2, Flashcards, Study Tracking, Notes_

Jarvis Learning: SM-2 spaced repetition system for any subject, AI-generated cards from your notes, reading tracker, and daily review sessions surfaced in your morning brief.

<details><summary>Details</summary>

#### SM-2 implementation in Supabase

 -- Cards table
CREATE TABLE cards (
 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
 front TEXT NOT NULL,
 back TEXT NOT NULL,
 deck_id UUID REFERENCES decks(id),
 interval INTEGER DEFAULT 1,
 ease_factor DECIMAL DEFAULT 2.5,
 repetitions INTEGER DEFAULT 0,
 next_review DATE DEFAULT CURRENT_DATE,
 created_at TIMESTAMPTZ DEFAULT NOW()
); 
 
#### SM-2 algorithm (TypeScript)

 function updateCard(card: Card, quality: 0 | 1 | 2 | 3 | 4 | 5): Card {
 const q = quality;
 let ef = card.ease_factor + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02));
 ef = Math.max(1.3, ef); // minimum EF
 
 let interval: number;
 if (q 
 
#### Card generation from notes

 User uploads lecture notes (PDF or text) → Claude: "Generate 20 spaced repetition flashcards from this material. Each card: front (question/prompt), back (answer/explanation). Focus on: definitions, cause-effect relationships, key distinctions, application examples. Return as JSON array." → Save to cards table → SM-2 schedules reviews.
 
#### Morning brief integration

 Cron job fetches: cards where next_review ≤ today. Send Slack message: "📚 5 cards due today. Reply with /review to start. Topics: [preview card fronts]." User replies → bot sends one card at a time → user rates recall → bot updates SM-2 → repeat until done.
 
#### Reading tracker

 Books table: title, author, pages, current_page, goal_finish_date. Daily: track pages read. Weekly: "At current pace, you'll finish [book] in X days. You're [ahead/behind] your goal." Automatic reading velocity calculation.

</details>

Links: —

---

## 💼 Career Development Module
**✅ GOOD** · _Job Tracker, Resume, Skills, Networking_

Jarvis Career: track job applications, maintain resume versions, identify skill gaps, log networking contacts, and generate targeted outreach. Your career strategy co-pilot.

<details><summary>Details</summary>

#### Database schema

 job_applications (id, company, role, status: wishlist|applied|phone|interview|offer|rejected, applied_date, notes, job_url, salary_range, contact_name)
resume_versions (id, version_name, target_role, content, created_at)
skills (id, name, proficiency: learning|competent|strong, last_practiced)
networking_contacts (id, name, company, role, met_at, last_contact, notes, linkedin_url)
skill_gaps (id, target_role, required_skill, current_level, plan) 
 
#### Application funnel tracking

 Weekly: count applications by status → calculate conversion rates (applied→phone rate, phone→interview rate, interview→offer rate). Claude analyzes: "My application funnel this month: applied 20, phone screen 3 (15%), interview 1 (33%), offer 0. Where is the biggest drop-off and what likely causes it?"
 
#### Skill gap analysis

 User inputs target role. Claude: "For a [Target Role] at companies like [examples], what are the most important technical skills in 2025? Compare against my current skills: [skill list]. Identify the top 3 gaps and suggest a 3-month plan for each gap with specific resources."
 
#### Networking follow-up

 Cron: check networking_contacts where last_contact > 60 days → Slack alert: "👋 It's been 60 days since you connected with [Name] at [Company]. Want to reconnect? [Draft message]." Prevents networking decay. Jarvis drafts the follow-up for you.
 
#### Resume tailoring

 Paste job description → "Tailor my resume for this role. My current resume: [resume text]. Job description: [JD]. Changes to highlight: relevant projects, matching skills, reorder bullet points. Keep under 1 page."

</details>

Links: —

---

## 🌊 Google Whisk → ezgif → Portfolio Pipeline
**✅ GOOD** · _prompt template_

Complete pipeline for creating distinctive portfolio visuals using Google Whisk image blending, animating with ezgif, and deploying as interactive portfolio assets.

<details><summary>Details</summary>

#### Visual Pipeline Guide
WHISK → EZGIF → PORTFOLIO PIPELINE

STEP 1: PLAN YOUR VISUAL DIRECTION
Before opening Whisk, decide:
- Subject: what/who is the focus (your avatar, a product, an abstract concept)
- Scene: the environment/context (architectural space, landscape, studio)
- Style: the aesthetic (editorial photography, concept art, product photography, abstract)
Write these down — you'll be swapping references to iterate.

STEP 2: GENERATE IN GOOGLE WHISK (labs.google/whisk)
Upload 3 reference images:
- Slot 1 (Subject): Reference of the subject
- Slot 2 (Scene): Reference of the environment
- Slot 3 (Style): Reference of the visual style/aesthetic

Hit Generate → wait 30-60 seconds → 4 variations appear.
To iterate: swap one reference image at a time (not all three).
Use the Refine text field for style adjustments:
 - "cinematic lighting, dramatic shadows"
 - "soft natural light, airy"
 - "high contrast, black and white"
 - "ultra detailed, 8k resolution"
 - "minimal, clean, product photography"

Download: click any output → download full resolution.

STEP 3: CREATE VARIATION SET (for animation)
To create an animatable sequence:
- Keep Subject + Scene the same
- Generate 4-8 times with slight Style variations
OR
- Use the same 3 references, hit Generate multiple times → collect variations
Target: 4-8 images that feel like frames from a single sequence

STEP 4: ANIMATE IN EZGIF (ezgif.com)
Go to ezgif.com → GIF Maker (or WebP Maker for better quality)
Upload your 4-8 images in order
Settings:
 - Delay: 20-30 (lower = faster)
 - Loop: 0 (forever)
 - Width: 800px (resize for web)
 - Colors: 256 (max GIF colors)
For smoother animation: use WebP format (ezgif supports it, much better quality than GIF)
Download the animated file.

STEP 5: INTEGRATE INTO PORTFOLIO
Option A — Static hero image:
Single best Whisk output as your portfolio hero (full-viewport background)
CSS: object-fit: cover; filter: brightness(0.7);
Overlay your text on top.

Option B — Animated hover effect:
Show static image on load, play animation on hover:
img { transition: opacity 0.3s; }
.project-card:hover .static { opacity: 0; }
.project-card:hover .animated { opacity: 1; }

Option C — Mouse scrub with Whisk frames:
Load 4-8 Whisk outputs as canvas frames → mouse X controls which frame shows.
This creates the "living portfolio" effect — your image morphs as the cursor moves.
(See: mouse scrub implementation in Atoms portfolio guide)

Option D — Background video loop:
Convert your sequence to WebM video: ffmpeg -i frame%d.webp -c:v libvpx-vp9 output.webm
Use as: <video autoplay muted loop playsinline src="output.webm">
Video is smoother than GIF and smaller file size.

STYLE COMBINATIONS THAT WORK WELL:
- Portfolio: subject (headshot) + scene (minimal white desk) + style (editorial magazine)
- Tech project: subject (laptop/device) + scene (architectural space) + style (product photography)
- Creative: subject (abstract texture) + scene (landscape) + style (concept art)
- Agency: subject (team photo) + scene (modern office) + style (documentary photography)

PERFORMANCE:
- Optimize images before adding to portfolio: imagemin, squoosh.app
- Target: single images under 200KB, sequences under 2MB total
- WebP format: 25-35% smaller than JPEG at same quality
- Use loading="lazy" on non-hero images

</details>

Links: —

---

## 🏃 Health & Fitness Module
**✅ GOOD** · _Workout, Nutrition, Sleep, Progress_

Jarvis Health: workout logging with progressive overload tracking, nutrition macro tracking, sleep analysis, and weekly health score. AI coaches you toward your fitness goals.

<details><summary>Details</summary>

#### Workout tracking schema

 workouts (id, date, type: strength|cardio|mobility, duration_min, notes)
sets (id, workout_id, exercise_name, sets, reps, weight_kg, rpe)
body_metrics (id, date, weight_kg, body_fat_pct, resting_hr)
sleep_logs (id, date, hours, quality: 1-5, notes) 
 
#### Progressive overload tracking

 For each exercise: track volume (sets × reps × weight) over time. Weekly: "Your squat volume this week: 7,200kg. Last week: 6,800kg (+5.9%). Are you progressing? Compare last 4 weeks and identify any plateaus (less than 2% weekly increase for 3+ weeks)."
 
#### Workout logging (Slack)

 "/workout bench 3x8x100" → Jarvis parses: bench press, 3 sets, 8 reps, 100kg → logs to Supabase → checks vs last workout → responds: "💪 Bench logged. Last week you did 3x8x97.5kg — this is a PR! Running total for today: 2,400kg volume."
 
#### Nutrition via Cronometer export

 Cronometer (free app) tracks macros with a better database than MyFitnessPal. Weekly: export CSV → import to Supabase → Claude: "Here's my nutrition data for the week. My goals: [protein/carbs/fat targets]. How often did I hit my targets? What patterns do you see? One specific change to improve adherence?"
 
#### Weekly health score

 Compute 0-100 score: workouts completed vs plan (30 pts), avg sleep hours (20 pts), protein target hit (20 pts), steps walked (15 pts), meditation/recovery (15 pts). Send Sunday: "📊 Health Score: 74/100. Sleep dragged it down (avg 6.2hrs this week). Everything else solid."

</details>

Links: —

---

## 📬 Inbox Management Module
**✅ GOOD** · _Email, Slack Digest, Priority Triage_

Jarvis triages your email and Slack daily. Morning summary: what needs a response, what can wait, what to unsubscribe from. Draft replies for complex threads.

<details><summary>Details</summary>

#### Email triage pipeline

 Each morning: fetch unread emails (Gmail API) → Claude Haiku classifies each: URGENT (reply today), RESPOND (reply this week), FYI (read-only), NEWSLETTER (auto-label), SPAM (flag for unsubscribe). Triage results sent to Slack: "📬 23 new emails. 3 urgent, 7 need reply, 13 FYI/newsletters."
 
#### Gmail API setup

 Google Cloud Console → enable Gmail API → OAuth2 credentials → scope: gmail.readonly + gmail.modify. Store refresh token in Supabase (encrypted). Use googleapis npm package. Token refresh is automatic with the googleapis library.
 
#### Draft reply generation

 For URGENT or RESPOND emails: "Draft a reply to this email. Context: I am a [your role]. Reply: [specific action to take — accept/decline/provide info/schedule meeting]. Tone: [professional/casual]. Keep under [100/200] words." User reviews draft → click send → Gmail API sends.
 
#### Newsletter unsubscribe automation

 After 2 weeks of newsletters being auto-labeled and unread → Jarvis flags: "You haven't opened [newsletter] in 14 days. Unsubscribe? [Yes/No]." One-click unsubscribe via Slack reaction emoji.
 
#### Slack digest

 End of workday (5pm Cron): scan Slack channels you specify → identify: messages that @ you, messages about projects you're working on, any "urgent" or "ASAP" mentions. Send digest to your personal DM: "Slack summary: 3 mentions, 1 urgent. [Preview]."

</details>

Links: —

---

## 📱 Instagram Analytics Module
**✅ GOOD** · _Content Performance, Posting Strategy, Growth_

Jarvis tracks your Instagram metrics via the Graph API, identifies your best-performing content types, and generates data-driven content strategy recommendations.

<details><summary>Details</summary>

#### Instagram Graph API setup

 Requires: Professional (Creator/Business) account. Facebook Developer account → create app → add Instagram Graph API product → get access token. Access token expires — implement refresh flow. Permissions needed: instagram_basic, instagram_manage_insights.
 
#### Metrics to track

 posts (id, timestamp, media_type, caption, permalink, like_count, comment_count, reach, impressions, saved, engagement_rate)
stories (id, timestamp, reach, impressions, exits, replies, swipe_ups)
account_insights (date, follower_count, follower_delta, profile_views, website_clicks) 
 
#### Weekly content analysis prompt

 "Here are my Instagram post metrics for the past 4 weeks: [JSON]. Analyze: 1) Which content types perform best (carousel vs reel vs image), 2) Best posting times (by engagement rate), 3) Caption length correlation with engagement, 4) Hashtag performance patterns, 5) 3 specific recommendations for next week's content. Be data-driven and specific."
 
#### Optimal posting schedule

 Build a posting time heatmap from your historical data: group posts by day/hour → average engagement rate → find the top 3 time slots. Your optimal schedule is unique to YOUR audience, not generic "post on Tuesday at 11am" advice.
 
#### Content calendar integration

 Link Instagram module to Daily Ops: when content_calendar table has a post due today → morning brief includes a reminder with the content plan. Jarvis tracks if you posted on schedule.

</details>

Links: —

---

## 🤖 Jarvis Agent Routines
**✅ GOOD** · _Automation, Cron, Multi-Step Workflows_

The scheduled automation routines that make Jarvis run on autopilot. Cron schedules, Vercel serverless functions, and multi-step agent workflows that run without you triggering them.

<details><summary>Details</summary>

#### Full cron schedule

 # vercel.json crons
{ "crons": [
 {"path": "/api/cron/morning-brief", "schedule": "0 7 * * *"}, // 7am daily
 {"path": "/api/cron/habit-reminder", "schedule": "0 20 * * *"}, // 8pm daily
 {"path": "/api/cron/evening-review", "schedule": "0 21 * * *"}, // 9pm daily
 {"path": "/api/cron/weekly-finance", "schedule": "0 18 0 * 0"}, // Sunday 6pm
 {"path": "/api/cron/weekly-health", "schedule": "0 18 0 * 0"}, // Sunday 6pm
 {"path": "/api/cron/email-triage", "schedule": "0 8 * * 1-5"}, // 8am weekdays
 {"path": "/api/cron/instagram-sync", "schedule": "0 10 * * *"}, // 10am daily
 {"path": "/api/cron/sm2-due-check", "schedule": "0 7 * * *"}, // 7am daily
 {"path": "/api/cron/networking-alerts", "schedule": "0 9 * * 1"} // Monday 9am
]} 
 
#### Failure handling

 Each cron function: try/catch everything. On failure: log to Supabase cron_logs table (function, timestamp, error, success). Slack alert on failure: "⚠️ Jarvis cron /morning-brief failed: [error]." Monitor the cron_logs weekly to catch silent failures.
 
#### Idempotency (critical)

 Crons can run multiple times (Vercel guarantees at-least-once, not exactly-once). Every cron must be idempotent: running it twice should have the same result as running it once. Pattern: check if today's brief already sent before sending → skip if yes.
 
#### Multi-step weekly workflow

 Sunday 6pm: (1) fetch week's Finance data → (2) fetch Health data → (3) fetch Learning data → (4) fetch Career data → (5) Claude generates unified weekly review covering all domains → (6) Send to Slack as formatted report → (7) Store in weekly_reviews table. This is Jarvis's biggest weekly output.
 
#### Gradual rollout

 Start with just morning brief + habit reminder. Verify they work reliably for 2 weeks. Then add finance weekly. Then health. Add complexity gradually — a broken cron that spams you is worse than no cron.

</details>

Links: —

---

## 🔧 Jarvis Tech Stack Reference
**✅ GOOD** · _Full Config, Dependencies, Env Vars_

Complete Jarvis technology reference: all dependencies, environment variables, MCP connections, API keys needed, and the full package.json. Save for project setup.

<details><summary>Details</summary>

#### package.json dependencies

 "dependencies": {
 "next": "14.2.x",
 "@anthropic-ai/sdk": "latest",
 "@supabase/supabase-js": "^2",
 "@supabase/ssr": "latest",
 "stripe": "latest",
 "resend": "latest",
 "@slack/web-api": "latest",
 "googleapis": "latest",
 "openai": "latest", // Whisper TTS
 "recharts": "latest",
 "framer-motion": "latest",
 "date-fns": "latest",
 "zod": "latest"
},
"devDependencies": {
 "typescript": "^5",
 "@types/node": "latest",
 "tailwindcss": "^3",
 "eslint": "latest",
 "prettier": "latest"
} 
 
#### Required environment variables

 ANTHROPIC_API_KEY=sk-ant-...
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
RESEND_API_KEY=re_...
SLACK_BOT_TOKEN=xoxb-...
SLACK_CHANNEL_ID=C...
GMAIL_CLIENT_ID=...
GMAIL_CLIENT_SECRET=...
GMAIL_REFRESH_TOKEN=...
OPENAI_API_KEY=sk-... # for Whisper
ELEVENLABS_API_KEY=... # for TTS
INSTAGRAM_ACCESS_TOKEN=...
PLAID_CLIENT_ID=...
PLAID_SECRET=... 
 
#### Supabase tables needed (full list)

 accounts, transactions, net_worth_history, budgets, investment_positions, workouts, sets, body_metrics, sleep_logs, cards, decks, habit_logs, habits, job_applications, resume_versions, skills, networking_contacts, instagram_posts, weekly_reviews, cron_logs. Create all with RLS policies before building features.
 
#### MCP servers for Jarvis development

 Supabase MCP (DB management), Filesystem MCP (vault access), GitHub MCP (code tracking), Slack MCP (testing Slack integration), Memory MCP (Jarvis context). Configure all before starting development.

</details>

Links: —

---

## 🎤 Voice Interface Module
**✅ GOOD** · _Whisper, TTS, Hands-Free Jarvis_

Add voice input/output to Jarvis. Speak commands → Whisper transcribes → Claude responds → TTS reads the answer aloud. Hands-free Jarvis for morning routines.

<details><summary>Details</summary>

#### Voice pipeline

 Mic input (Web Audio API)
 → MediaRecorder captures audio blob
 → POST to /api/voice/transcribe
 → OpenAI Whisper API (or Whisper.cpp local)
 → Text → Jarvis orchestrator
 → Claude response text
 → POST to /api/voice/speak
 → ElevenLabs TTS (or native browser TTS)
 → Audio plays back 
 
#### Browser audio capture

 const stream = await navigator.mediaDevices.getUserMedia({audio: true});
const recorder = new MediaRecorder(stream);
const chunks = [];
recorder.ondataavailable = e => chunks.push(e.data);
recorder.onstop = async () => {
 const blob = new Blob(chunks, {type: 'audio/webm'});
 const formData = new FormData();
 formData.append('audio', blob, 'voice.webm');
 const {text} = await fetch('/api/voice/transcribe', {
 method: 'POST', body: formData
 }).then(r => r.json());
 sendToJarvis(text);
}; 
 
#### Whisper transcription (server)

 // pages/api/voice/transcribe.ts
import OpenAI from 'openai';
const openai = new OpenAI();

const transcription = await openai.audio.transcriptions.create({
 file: audioFile, model: 'whisper-1', language: 'en'
});
return transcription.text; 
 Whisper pricing: $0.006/minute. A 30-second voice command = $0.003. Essentially free for personal use.
 
#### TTS options

 **Browser built-in**: speechSynthesis API — free, robotic voice. **ElevenLabs**: $5/month for 10k characters, very natural voice. Choose a voice that sounds like "your assistant." **OpenAI TTS**: $0.015/1k characters, good quality. ElevenLabs best quality for the price.
 
#### Wake word (optional)

 Use Picovoice Porcupine (free tier) for "Hey Jarvis" wake word. Browser stays in listening mode — detects wake word → starts full recording. Makes it feel like a real assistant.

</details>

Links: —

---
