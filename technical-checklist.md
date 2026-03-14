# Technical AI-Readiness Checklist

## AI Crawler Access — robots.txt Rules

### Critical Bots (Block = Invisible to AI Search)

| Bot | Owner | Purpose | Impact if Blocked |
|-----|-------|---------|-------------------|
| `GPTBot` | OpenAI | Training data collection | Content won't be learned by future GPT models |
| `OAI-SearchBot` | OpenAI | ChatGPT Search (real-time) | **CRITICAL**: Site invisible in ChatGPT search results, no citations |
| `ChatGPT-User` | OpenAI | User-initiated "browse this site" | Users can't ask ChatGPT to read your pages |
| `PerplexityBot` | Perplexity | Indexing (200B+ URL index) | Invisible on Perplexity (780M queries/month) |
| `Googlebot` | Google | Main index (AI Overviews use this) | Invisible everywhere on Google including AI Overviews |
| `Bingbot` | Microsoft | Bing index (Copilot + ChatGPT use this) | ChatGPT and Copilot lose access to your content |
| `ClaudeBot` | Anthropic | Claude web search | Invisible in Claude search results |

### Important Bots

| Bot | Owner | Purpose |
|-----|-------|---------|
| `Google-Extended` | Google | Gemini training (separate from Googlebot) |
| `Bytespider` | ByteDance | AI products training |
| `Applebot-Extended` | Apple | Apple Intelligence features |
| `cohere-ai` | Cohere | Enterprise AI search |

### Recommended robots.txt for Maximum AI Visibility

```
User-agent: *
Allow: /

# Explicitly allow all AI crawlers
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Bingbot
Allow: /

# Block admin/private areas from all
User-agent: *
Disallow: /admin/
Disallow: /api/
Disallow: /private/
Disallow: /cart/
Disallow: /checkout/
Disallow: /account/

Sitemap: https://[domain]/sitemap.xml
```

### Common Mistakes
- Using `Disallow: /` for all user-agents (blocks everything)
- Blocking GPTBot thinking it only does training (OAI-SearchBot is the citation bot, but GPTBot also feeds the knowledge base)
- Not having a robots.txt at all (bots default to crawl everything, but you miss the chance to guide them)
- Blocking JavaScript/CSS files that bots need to understand page layout

## JavaScript Rendering Detection

### How to Check
1. Fetch page with `curl` (no JS execution) — this is what AI bots see
2. Look for content in the raw HTML `<body>`
3. If body contains only `<div id="root"></div>` or `<div id="app"></div>` or `<div id="__next"></div>` with no visible text content → site is client-side rendered

### Red Flags
- React apps without SSR/SSG (Create React App default)
- Vue SPA without Nuxt.js or SSR
- Angular SPA without Angular Universal
- Svelte without SvelteKit SSR
- Any framework where content loads via `fetch()` calls after page load

### Green Flags
- Next.js with `getServerSideProps` or `getStaticProps` (content in initial HTML)
- Nuxt.js with SSR mode
- Static site generators (Hugo, Jekyll, Gatsby with SSG, Astro)
- WordPress, Webflow, Squarespace (server-rendered by default)
- Plain HTML sites

### Quick Test
```bash
curl -s -A "GPTBot" "https://example.com" | grep -c "[a-zA-Z]{20,}"
```
If the count is very low (<10 matches of 20+ char strings), the page is likely JS-rendered and invisible to AI crawlers.

## llms.txt

### What It Is
A proposed standard (by Jeremy Howard, Answer.AI) — a Markdown file at the site root that provides AI engines with a structured summary of the site's content, purpose, and key pages.

### Format
```markdown
# [Site Name]

> [Brief description of what the site/company does]

## Key Pages
- [Page Title](https://example.com/page): Brief description
- [Page Title](https://example.com/page): Brief description

## Documentation
- [Doc Title](https://example.com/doc): Brief description
```

### Current Status
- Adoption is growing but still early
- Only 1 out of 94,614 URLs cited in AI responses was an llms.txt file (ALLMO.ai study)
- Low effort to implement, marginal but positive signal
- Recommendation: implement it, but don't prioritize over content and technical fixes

## Bing Webmaster Tools

### Why It's Critical for GEO
- ChatGPT Search uses the **Bing index** for real-time search
- Microsoft Copilot uses the Bing index
- If your site isn't in Bing's index, it can't appear in ChatGPT search citations
- Many sites are indexed by Google but NOT by Bing — this is a common blind spot

### Actions
1. Create a Bing Webmaster Tools account (free)
2. Verify site ownership
3. Submit sitemap
4. Check indexation status
5. Monitor for crawl errors specific to Bing

## HTTPS
- All AI engines require HTTPS for citations
- Mixed content (HTTP resources on HTTPS pages) can cause crawl issues
- Check: no HTTP links in internal navigation

## Core Web Vitals (Secondary for GEO)
- Less directly impactful for GEO than for SEO
- But extremely slow pages may be deprioritized by AI engines during retrieval
- Google AI Overviews use the main Google index, which factors in CWV
- LCP < 2.5s, INP < 200ms, CLS < 0.1 are the targets
