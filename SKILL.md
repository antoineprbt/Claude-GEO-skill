---
name: geo
description: Generative Engine Optimization (GEO) skill for Claude Code. Audit and optimize any website for AI search visibility — ChatGPT, Perplexity, Gemini, Google AI Overviews, Claude. Use this skill whenever the user mentions GEO, AEO, AI search, AI visibility, AI citations, appearing in ChatGPT, Perplexity optimization, AI Overviews, LLM optimization, generative search, or wants to check if their site/brand is visible to AI engines. Also trigger when the user asks about robots.txt for AI crawlers, llms.txt, schema markup for AI, answer islands, or content structure for AI citation. Covers technical AI-readiness audit, content optimization for AI citation, multi-platform presence analysis, competitor AI visibility, and GEO action planning.
---

# GEO — Generative Engine Optimization Skill

Comprehensive GEO analysis skill for Claude Code. Audits and optimizes websites for visibility in AI-generated search results (ChatGPT, Perplexity, Gemini, Google AI Overviews, Claude, Copilot).

## Commands

| Command | Description |
|---------|-------------|
| `/geo audit <url>` | Full GEO audit — technical + content + presence |
| `/geo page <url>` | Deep analysis of a single page's AI citability |
| `/geo technical <url>` | AI crawler access & technical readiness only |
| `/geo content <url>` | Content structure & answer island analysis |
| `/geo schema <url>` | Schema markup audit for AI engines |
| `/geo presence <brand>` | Multi-platform presence check (Reddit, YouTube, G2, Wikipedia, LinkedIn) |
| `/geo competitors <url>` | Identify who AI engines cite in the user's niche |
| `/geo fix <url>` | Generate prioritized fix list with code snippets |
| `/geo plan <url>` | 90-day GEO action plan |
| `/geo score <url>` | Quick AI Citability Score (0-100) |

## Full Audit Workflow (`/geo audit`)

When the user runs `/geo audit <url>`, execute ALL of the following phases. Present results in a single structured report.

### Phase 1 — Fetch & Parse

1. Fetch the page HTML using `curl` or the `fetch_page.py` script
2. Fetch `robots.txt` from the root domain
3. Check for `llms.txt` at the root domain
4. Fetch `sitemap.xml` if it exists
5. Store raw HTML for analysis

### Phase 2 — Technical AI-Readiness

Read `references/technical-checklist.md` for the full checklist, then evaluate:

**AI Crawler Access (Critical)**
- robots.txt: Check if these user-agents are allowed or blocked:
  - `GPTBot` (OpenAI — training data)
  - `OAI-SearchBot` (OpenAI — ChatGPT search, generates citations)
  - `ChatGPT-User` (OpenAI — user-initiated browsing)
  - `PerplexityBot` (Perplexity — indexing)
  - `Google-Extended` (Google — Gemini training)
  - `Googlebot` (Google — AI Overviews use the main Google index)
  - `Bingbot` (Microsoft — Copilot uses Bing index)
  - `ClaudeBot` (Anthropic — Claude web search)
  - `Bytespider` (ByteDance — used by some AI products)
- Score: Each blocked critical bot = -10 points. GPTBot and OAI-SearchBot blocked = CRITICAL failure.

**JavaScript Rendering**
- Check if the page content is rendered via client-side JavaScript (React, Vue, Angular, Next.js CSR) or server-side
- Method: Compare content in raw HTML vs what a full render would show
- AI crawlers (GPTBot, PerplexityBot) do NOT execute JavaScript — if content is JS-only, it's invisible to AI
- Flag: If `<div id="root"></div>` or `<div id="app"></div>` is nearly empty in raw HTML, the site is likely JS-rendered → CRITICAL issue

**llms.txt**
- Check if `/llms.txt` exists
- If it exists, validate its Markdown structure
- This is a bonus signal, not critical — adoption is still early

**Sitemap & Indexability**
- Verify sitemap.xml exists and is accessible
- Check that key pages are included
- Verify the site is submittable to Bing Webmaster Tools (critical for ChatGPT which uses Bing)

**HTTPS & Performance**
- Confirm HTTPS
- Check basic load time indicators in the HTML (large inline scripts, massive images)

### Phase 3 — Content AI-Citability Analysis

Read `references/content-optimization.md` for detailed guidelines, then analyze:

**Heading Hierarchy (H1-H6)**
- Exactly 1 H1 per page containing the primary topic
- H2s that are descriptive and self-contained (not vague like "Our Approach")
- Logical nesting: H1 → H2 → H3, no skipped levels
- Score: Well-structured hierarchy = high AI extractability

**Answer Islands**
- Look for self-contained blocks of 40-80 words that directly answer a question
- Best location: immediately after each H2
- These blocks should work as standalone answers if extracted by an AI
- Count how many H2 sections start with a direct answer vs. fluff/intro text

**Factual Density**
- Count statistics, data points, percentages, dates
- Count citations of external sources
- Count named entities (people, organizations, studies)
- Princeton GEO study finding: adding statistics improves AI visibility by 33.9%, adding citations improves it by up to 115%

**Content Freshness**
- Check for `datePublished` and `dateModified` in schema or visible on page
- Content published in last 6 months receives preferential treatment from AI engines
- Flag if no date is visible or if content appears outdated

**FAQ Sections**
- Check for FAQ sections (with or without FAQPage schema)
- Q&A format maps directly to user queries on AI engines
- Each FAQ answer should be 40-80 words, self-contained

**Meta Information**
- Title tag: present, descriptive, under 60 characters, keyword-rich
- Meta description: present, compelling, under 160 characters
- Both should contain the primary topic clearly — AI engines use these for context

### Phase 4 — Schema Markup Analysis

Read `references/schema-guide.md` for full schema type reference, then check:

**Existing Schema**
- Parse all JSON-LD blocks in the page
- Identify schema types present
- Validate required fields for each type

**Priority Schema for GEO** (ordered by impact):
1. `FAQPage` — Directly maps to AI Q&A extraction. Highest GEO impact.
2. `HowTo` — Step-by-step content is highly extractable by AI
3. `Article` + `author` (Person) — E-E-A-T signals for AI trust
4. `Organization` — Entity definition, helps AI understand who you are
5. `Product` — For e-commerce, essential for AI product recommendations
6. `Review` / `AggregateRating` — Social proof that AI engines weight
7. `Speakable` — Marks content suitable for voice/AI audio responses
8. `BreadcrumbList` — Helps AI understand site structure

**Schema Quality**
- Are `datePublished` and `dateModified` present and current?
- Is `author` a linked Person with a URL, not just a string?
- Does Organization schema match across the site and external profiles?

### Phase 5 — Multi-Platform Presence

For the brand/domain, check presence on AI-cited platforms:

| Platform | Why It Matters | Check Method |
|----------|---------------|--------------|
| YouTube | #1 cited source by Google AI Overviews (23.3%) | Search `site:youtube.com "brand name"` |
| Reddit | #1 cited source by Perplexity (6.6%), up 450% in AI Overviews | Search `site:reddit.com "brand name"` |
| Wikipedia | Top cited by ChatGPT (7.8-47.9%) and Google AI Overviews (18.4%) | Search `site:wikipedia.org "brand name"` |
| LinkedIn | Top 25 for 37% of B2B brands | Search `site:linkedin.com "brand name"` |
| G2 / Capterra | Structured review data trusted by AI | Search `site:g2.com "brand name"` |
| GitHub | For tech/dev brands | Search `site:github.com "brand name"` |
| Crunchbase | For startups | Search `site:crunchbase.com "brand name"` |

Score presence as: ✅ Present with rich content / ⚠️ Mentioned but thin / ❌ Not found

**Entity Consistency**
- Is the brand name consistent across all platforms?
- Is the description/positioning consistent?
- Are key facts (founding date, location, product category) aligned?
- Inconsistent entity data confuses AI engines and reduces citation likelihood

### Phase 6 — Scoring

Calculate the **AI Citability Score (0-100)** using this weighted model:

| Category | Weight | Max Points |
|----------|--------|-----------|
| AI Crawler Access | 25% | 25 |
| Content Structure (headings, answer islands) | 25% | 25 |
| Schema Markup | 15% | 15 |
| Factual Density & Freshness | 15% | 15 |
| Multi-Platform Presence | 10% | 10 |
| Technical (HTTPS, performance, JS rendering) | 10% | 10 |

**Score Bands:**
- 80-100: AI-Ready — Strong likelihood of being cited
- 60-79: Needs Work — Some visibility but significant gaps
- 40-59: At Risk — Missing critical elements, competitors likely dominate
- 0-39: Invisible — AI engines are unlikely to cite this content

### Phase 7 — Report Output

Generate a Markdown report with this structure:

```markdown
# GEO Audit Report — [domain]
**Date:** [date]
**AI Citability Score:** [X]/100 — [Band Label]

## Executive Summary
[2-3 sentences: overall status, biggest strengths, most critical issues]

## 🔴 Critical Issues (Fix Immediately)
[Issues that make the site invisible to AI engines]

## 🟡 Important Issues (Fix This Month)
[Issues that significantly reduce AI visibility]

## 🟢 Quick Wins (Easy Fixes, High Impact)
[Low-effort changes with disproportionate impact]

## Technical AI-Readiness
### AI Crawler Access
[Table of bots: allowed/blocked status]
### JavaScript Rendering
[SSR status]
### llms.txt
[Present/absent]

## Content Citability
### Heading Structure
[Analysis]
### Answer Islands
[Count and quality assessment]
### Factual Density
[Stats count, citation count, freshness]

## Schema Markup
[Current schema vs. recommended]

## Multi-Platform Presence
[Platform presence table]

## 90-Day Priority Action Plan
### Month 1: Technical Foundation
[3-5 actions]
### Month 2: Content Optimization  
[3-5 actions]
### Month 3: Authority Building
[3-5 actions]
```

## Single Page Analysis (`/geo page`)

Deep-dive on one URL. Run Phases 2-4 from the full audit but with more granular content analysis:
- Word count per H2 section
- Answer island quality rating per section (1-5)
- Specific rewrite suggestions for each section to improve AI extractability
- Exact schema markup code to add (ready-to-paste JSON-LD)

## Quick Score (`/geo score`)

Lightweight version. Fetch the page, run scoring only, output a single score with top 3 issues. Takes under 30 seconds.

## Fix Generation (`/geo fix`)

For each issue found in an audit, generate:
- The exact code change needed (robots.txt lines, schema JSON-LD, HTML restructuring)
- Before/after examples
- Priority level (critical/important/nice-to-have)

## Competitor Analysis (`/geo competitors`)

1. Identify the site's niche from its content
2. Generate 10 likely queries users would ask AI engines about this niche
3. For each query, note which types of sources AI engines typically cite (based on the knowledge in references/ai-engine-behavior.md)
4. Suggest the content and presence strategy needed to compete

## 90-Day Plan (`/geo plan`)

Read `references/action-plan-template.md` and generate a customized plan based on audit findings.

## Reference Files

Read these on-demand when their topic is relevant:

| File | When to Read |
|------|-------------|
| `references/technical-checklist.md` | During technical audit (Phase 2) |
| `references/content-optimization.md` | During content analysis (Phase 3) |
| `references/schema-guide.md` | During schema audit (Phase 4) |
| `references/ai-engine-behavior.md` | During competitor analysis or when explaining how AI engines work |
| `references/action-plan-template.md` | When generating a 90-day plan |

## Key Principles

1. **GEO ≠ SEO.** GEO optimizes for AI citation, not Google ranking. A page can rank #1 on Google and be invisible to ChatGPT.
2. **Every fact is an optimization unit.** In SEO you optimize pages. In GEO you optimize individual facts, statistics, and statements that AI can extract.
3. **Answer islands are king.** Self-contained 40-80 word blocks after each H2 that directly answer a question — this is the atomic unit of GEO.
4. **Multi-platform > single site.** AI engines triangulate across sources. A brand mentioned on YouTube + Reddit + G2 + its own site is 2.8x more likely to be cited than one present only on its site.
5. **Schema enables, content delivers.** Schema helps AI understand your content's structure. But it's the content quality that earns the citation.
