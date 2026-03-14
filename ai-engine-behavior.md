# How AI Engines Select and Cite Sources

## The RAG Pipeline (All AI Search Engines)

Every AI search engine follows the same basic architecture: **Retrieval Augmented Generation (RAG)**.

1. **Query Understanding** — The AI parses the user's question and identifies intent
2. **Retrieval** — The system searches its index (or the live web) for relevant passages
3. **Re-ranking** — Retrieved passages are scored by relevance, authority, and freshness
4. **Generation** — The LLM synthesizes an answer using the top passages as context
5. **Citation** — The system attributes claims to the source passages

Your content must win at steps 2 and 3 to earn a citation.

## ChatGPT Search (OpenAI)

### Key Facts
- **87.4%** of all AI referral traffic comes from ChatGPT
- **800M+** weekly active users
- Uses **Bing index** for real-time search
- **60%** of queries are answered from parametric knowledge (no search, no citations)
- Wikipedia is the #1 cited source (**7.8-47.9%** depending on query type)

### How It Selects Sources
- Triggered when the query needs current info, factual data, or the model is uncertain
- Searches Bing, retrieves top results, extracts relevant passages
- Prefers: high Domain Authority sites, established brands, .gov/.edu, Wikipedia
- Average age of cited domains: **17 years**
- Provides inline citations with clickable links

### What Gets Cited
- Clear, factual statements with data
- Definitions and explanations
- Comparative content ("X vs Y")
- Lists and structured information
- Content from well-known, authoritative domains

### Crawlers
- `GPTBot` — Training data collection
- `OAI-SearchBot` — Real-time search (this is the one that generates citations)
- `ChatGPT-User` — User-requested browsing

## Perplexity AI

### Key Facts
- **22M+** monthly active users
- **780M** queries/month (up 239% YoY)
- **200B+ URL** index
- Reddit is the #1 cited source (**6.6%**)
- Provides **numbered inline citations** — most transparent citation system

### How It Selects Sources
- ALWAYS searches the web (unlike ChatGPT which sometimes doesn't)
- Combines its own index with live web search
- Strongly favors community/UGC content (Reddit, forums, Quora)
- Cites more diverse sources than ChatGPT — smaller sites have a better chance
- Favors recent content

### What Gets Cited
- Reddit discussions and expert answers
- Detailed technical explanations
- Niche expertise content
- Recent news and updates
- Content with specific data points

### Crawlers
- `PerplexityBot` — Indexing crawler
- `Perplexity-User` — Real-time query-triggered crawl

### Controversy
- Cloudflare documented Perplexity using undeclared crawlers that bypass robots.txt
- Some sites have reported their content being used without proper crawl identification
- Know this for client conversations — it's a common concern

## Google AI Overviews / AI Mode

### Key Facts
- **1.5B+** monthly users (integrated into Google Search)
- Uses **Gemini** model
- Appears in **50%+** of US searches
- YouTube is the #1 cited source (**23.3%**)
- Wikipedia is #2 (**18.4%**)
- **93%** of AI Mode searches end without a click

### How It Selects Sources
- Uses the existing **Google index** (same as traditional search)
- Employs **query fan-out**: decomposes complex queries into sub-queries
- Cites pages that appear frequently across sub-query results
- A page ranked #40 for a sub-query CAN be cited in the AI Overview for the main query
- Citations from top-10 pages dropped from **76% to 38%** — lower-ranked pages increasingly cited

### What Gets Cited
- YouTube videos (by far the #1 source)
- Wikipedia articles
- Government and educational sites
- E-commerce product pages (for shopping queries)
- Sites with strong E-E-A-T signals

### Key Insight for GEO
- Traditional SEO ranking matters MORE here than on other AI engines
- But the query fan-out system means you can be cited even without ranking top 10
- Having content on YouTube is nearly mandatory for Google AI Overviews visibility

## Microsoft Copilot

### Key Facts
- Uses **Bing index** + **GPT-4o**
- Integrated into Windows, Edge, Microsoft 365
- Access to enterprise data via Microsoft Graph
- Growing B2B usage

### How It Selects Sources
- Searches Bing for web queries
- For enterprise queries, also searches user's Microsoft 365 data
- Provides citations with links
- Tends to cite Microsoft documentation heavily

### What Gets Cited
- Bing-indexed content (ensure Bing indexation)
- Microsoft ecosystem content (LinkedIn, GitHub)
- Technical documentation
- B2B and enterprise content

## Google Gemini (Standalone App)

### Key Facts
- **750M+** monthly users
- Uses Google's search infrastructure
- Deep integration with Google services

### How It Selects Sources
- Similar to AI Overviews but in a conversational format
- Uses Google Search for grounding
- Cites Google ecosystem sources (YouTube, Google Scholar, Google Books)

## Claude (Anthropic)

### Key Facts
- Uses **Brave Search** for web search when enabled
- Search is opt-in (not default)
- Favors well-structured, logical content

### What Gets Cited
- Content with clear logical structure
- Factual, well-sourced content
- Technical documentation
- Content accessible via Brave's index

## Cross-Platform Citation Patterns

### Overlap is Low
- Only **11%** of domains are cited by BOTH ChatGPT and Perplexity
- Each platform has distinct source preferences
- Optimizing for one doesn't guarantee visibility on others
- Multi-platform GEO strategy is essential

### Universal Factors That Increase Citation (All Platforms)
1. **Domain Authority** — Correlation coefficient of 0.334 with AI citation
2. **Content completeness** — Score >8.5/10 = 4.2x more likely to be cited
3. **Structural clarity** — 50-150 word blocks with descriptive headings = 2.3x more citations
4. **Factual density** — Statistics, data, named sources
5. **Freshness** — Content from last 6 months preferred
6. **Multi-platform presence** — Present on 4+ platforms = 2.8x more likely to appear in ChatGPT

### Source Type Distribution Across AI Engines
| Source Type | ChatGPT | Perplexity | Google AI Overviews |
|-------------|---------|------------|-------------------|
| Wikipedia | #1 | Top 5 | #2 |
| YouTube | Top 10 | Top 10 | #1 |
| Reddit | Top 10 | #1 | Rising fast (+450%) |
| News sites | Top 5 | Top 5 | Top 5 |
| Brand sites | Common | Common | Common |
| G2/Review sites | Moderate | Moderate | Moderate |
| LinkedIn | Growing | Growing | Growing |

## What 86% of AI Citations Have in Common (Yext Study)

A study of **6.8 million AI citations** found:
- **86%** come from brand-managed sources (own website + business listings)
- The rest come from third-party sources (press, UGC, reviews)
- Brand-managed sources you can control: website, Google Business Profile, Yelp, Apple Maps, Facebook, LinkedIn, Bing Places

**Implication:** You have direct control over the majority of what AI engines cite about you. Fix your own properties first.
