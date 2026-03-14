# Schema Markup Guide for GEO

## Why Schema Matters for AI Engines

AI engines don't read schema markup directly the way Google's rich results do. But schema has strong **indirect impact**:
- Google AI Overviews use the Google index, which heavily uses schema
- Schema helps crawlers understand content type, authorship, and entity relationships
- Well-structured schema reduces ambiguity — AI engines can confidently identify what your page is about
- FAQPage schema maps directly to the Q&A format AI engines use

## Priority Schema Types for GEO

### 1. FAQPage (Highest GEO Impact)

Maps directly to how users query AI engines. Each Q&A pair is a potential extraction target.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Generative Engine Optimization?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generative Engine Optimization (GEO) is the practice of optimizing web content to appear in AI-generated search results from engines like ChatGPT, Perplexity, Gemini, and Google AI Overviews. Unlike traditional SEO which targets Google's link-based results, GEO focuses on making content extractable and citable by AI models."
      }
    }
  ]
}
```

**Rules:**
- Each answer should be 40-100 words (AI extraction sweet spot)
- Questions should match real user queries
- Answers must be self-contained and factual
- Maximum 10 Q&A pairs per page for best results

### 2. HowTo

For step-by-step content. AI engines love procedural information.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to optimize your robots.txt for AI crawlers",
  "description": "Step-by-step guide to allowing AI search bots access to your website content.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Locate your robots.txt file",
      "text": "Access your robots.txt file at yourdomain.com/robots.txt. If it doesn't exist, create one in your site's root directory."
    },
    {
      "@type": "HowToStep",
      "name": "Add AI bot permissions",
      "text": "Add explicit Allow directives for GPTBot, OAI-SearchBot, PerplexityBot, and ClaudeBot."
    }
  ]
}
```

### 3. Article + Author (Person)

Critical for E-E-A-T signals. Links content to a real, verifiable author.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Complete Guide to GEO in 2026",
  "description": "How to optimize your website for AI search engines.",
  "datePublished": "2026-03-01",
  "dateModified": "2026-03-14",
  "author": {
    "@type": "Person",
    "name": "Antoine Dupont",
    "url": "https://example.com/team/antoine",
    "jobTitle": "GEO Consultant",
    "sameAs": [
      "https://linkedin.com/in/antoinedupont",
      "https://twitter.com/antoinedupont"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example Company",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
```

**Critical fields:**
- `datePublished` AND `dateModified` — always include both
- `author` as a `Person` object with `url` and `sameAs` (not just a string name)
- `sameAs` links to author's social profiles build the Author Graph

### 4. Organization

Defines the entity. Helps AI engines understand who you are.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Brief description of what the company does.",
  "foundingDate": "2024",
  "founder": {
    "@type": "Person",
    "name": "Founder Name"
  },
  "sameAs": [
    "https://linkedin.com/company/example",
    "https://twitter.com/example",
    "https://github.com/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "contact@example.com"
  }
}
```

**Key:** `sameAs` array should list ALL official social/platform profiles. This builds entity recognition across the web.

### 5. Product

For e-commerce and SaaS product pages.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "Clear, factual product description.",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "49.99",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "127"
  }
}
```

### 6. BreadcrumbList

Helps AI engines understand site structure and page hierarchy.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://example.com/blog"},
    {"@type": "ListItem", "position": 3, "name": "GEO Guide", "item": "https://example.com/blog/geo-guide"}
  ]
}
```

### 7. Speakable

Marks content sections suitable for AI voice/audio responses. Emerging but increasingly relevant.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".key-takeaways"]
  }
}
```

## Schema Validation

### Tools
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/
- JSON-LD Playground: https://json-ld.org/playground/

### Common Mistakes
1. Using Microdata instead of JSON-LD (JSON-LD is preferred and easier to maintain)
2. Missing `dateModified` (signals stale content)
3. Author as a plain string instead of a Person object (loses E-E-A-T value)
4. Inconsistent Organization name across pages
5. Duplicate schema types on the same page (e.g., two Article schemas)
6. Missing `@context` declaration
7. Invalid JSON syntax (trailing commas, unescaped quotes)

## Schema Implementation Priority

For a site with NO existing schema, implement in this order:

1. **Organization** on every page (header/footer) — defines the entity
2. **Article + Author** on all blog/content pages — builds authority
3. **FAQPage** on key landing pages and guides — direct AI extraction
4. **BreadcrumbList** on all pages — structural context
5. **Product** on product/pricing pages — for commercial queries
6. **HowTo** on tutorial/guide content — procedural extraction
7. **Speakable** on key pages — future-proofing for voice AI
