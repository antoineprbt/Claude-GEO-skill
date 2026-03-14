# 🔍 Claude GEO — Generative Engine Optimization Skill

**Audit and optimize any website for AI search visibility — ChatGPT, Perplexity, Gemini, Google AI Overviews, Claude.**

> Traditional SEO gets you ranked on Google. GEO gets you **cited by AI.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## What is GEO?

**Generative Engine Optimization** is the practice of optimizing web content to appear in AI-generated search results. When someone asks ChatGPT *"What's the best CRM for startups?"*, GEO determines whether your brand appears in the answer.

- 🤖 **800M+ weekly ChatGPT users** — are they seeing your brand?
- 📉 **60% of Google searches** now end without a click — AI gives the answer
- 📈 AI referral traffic converts at **14.2%** vs 2.8% for Google
- ⚡ Only **23% of marketers** invest in GEO — the window is wide open

## Quick Start

### Install

```bash
git clone https://github.com/antoineprbt/Claude-GEO-skill.git
cp -r Claude-GEO-skill ~/.claude/skills/geo
cp Claude-GEO-skill/scripts/parse_geo.py ~/.claude/scripts/parse_geo.py

```

Restart Claude Code after installation.

### Commands

```bash
# Full GEO audit
/geo audit https://example.com

# Single page deep analysis
/geo page https://example.com/pricing

# Technical AI-readiness check only
/geo technical https://example.com

# Content structure & answer islands
/geo content https://example.com/blog/guide

# Schema markup audit
/geo schema https://example.com

# Multi-platform brand presence
/geo presence "Brand Name"

# Competitor AI visibility analysis
/geo competitors https://example.com

# Generate fix list with code snippets
/geo fix https://example.com

# 90-day GEO action plan
/geo plan https://example.com

# Quick AI Citability Score (0-100)
/geo score https://example.com
```

## What It Audits

### 🔧 Technical AI-Readiness
- **robots.txt** — Are GPTBot, PerplexityBot, ClaudeBot allowed?
- **JavaScript rendering** — Can AI crawlers see your content? (They don't execute JS)
- **llms.txt** — Present and properly formatted?
- **Bing indexation** — Critical because ChatGPT uses Bing's index
- **Sitemap** accessibility

### 📝 Content AI-Citability
- **Heading hierarchy** — H1/H2/H3 structure for AI extraction
- **Answer islands** — Self-contained 40-80 word blocks that AI can extract and cite
- **Factual density** — Statistics, citations, named sources (Princeton study: +33.9% visibility)
- **Content freshness** — Dates, update signals
- **FAQ sections** — Direct Q&A mapping for AI queries
- **TLDR-first pattern** — Conclusions at the top, not the bottom

### 🏷️ Schema Markup
- FAQPage, HowTo, Article, Organization, Product, BreadcrumbList, Speakable
- Author/Person linking for E-E-A-T
- datePublished/dateModified validation
- Entity consistency checks

### 🌐 Multi-Platform Presence
- YouTube (23.3% of Google AI Overview citations)
- Reddit (6.6% of Perplexity citations, +450% in AI Overviews)
- Wikipedia (7.8-47.9% of ChatGPT citations)
- LinkedIn, G2, Capterra, GitHub, Crunchbase
- Entity consistency across platforms

### 📊 AI Citability Score (0-100)

| Score | Band | Meaning |
|-------|------|---------|
| 80-100 | AI-Ready | Strong likelihood of being cited |
| 60-79 | Needs Work | Some visibility but significant gaps |
| 40-59 | At Risk | Competitors likely dominate |
| 0-39 | Invisible | AI engines are unlikely to cite you |

## How It's Different from SEO Tools

| | Traditional SEO Tools | Claude GEO |
|---|---|---|
| **Optimizes for** | Google rankings | AI citations (ChatGPT, Perplexity, Gemini) |
| **Unit of optimization** | Pages | Individual facts and statements |
| **Checks** | Backlinks, keywords, page speed | Answer islands, AI crawler access, entity consistency |
| **Schema focus** | Rich snippets | AI extraction (FAQPage, HowTo, Speakable) |
| **Presence check** | Google index | 8+ AI-cited platforms |
| **Output** | Ranking recommendations | Citation-ready content structure |

## File Structure

```
claude-geo/
├── geo/
│   ├── SKILL.md              # Main skill (commands, workflow, scoring)
│   └── references/
│       ├── technical-checklist.md    # AI crawler rules, JS rendering, robots.txt
│       ├── content-optimization.md   # Answer islands, factual density, E-E-A-T
│       ├── schema-guide.md           # JSON-LD templates for GEO
│       ├── ai-engine-behavior.md     # How ChatGPT/Perplexity/Gemini select sources
│       └── action-plan-template.md   # 90-day GEO action plan template
├── scripts/
│   └── parse_geo.py          # Page fetcher & HTML parser
├── LICENSE
└── README.md
```

## Based On

Inspired by the structure of [claude-seo](https://github.com/AgriciDaniel/claude-seo) by @AgriciDaniel (MIT License). This skill is built from scratch with a 100% GEO focus — optimized for AI search visibility rather than traditional SEO.

## Key Research & Data Sources

- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) — Princeton, Georgia Tech, IIT Delhi (KDD 2024)
- [Yext AI Citation Study](https://investors.yext.com/) — 6.8M AI citations analyzed
- [Surfer AI Citation Report 2025](https://surferseo.com/blog/ai-citation-report/)
- [Profound AI Platform Citation Patterns](https://www.tryprofound.com/blog/ai-platform-citation-patterns)

## License

MIT License — use it, fork it, improve it, share it.

## Contributing

PRs welcome! If you find new AI engine behaviors, citation patterns, or optimization techniques, please contribute.

---

**Built for the age of AI search.** 🚀
