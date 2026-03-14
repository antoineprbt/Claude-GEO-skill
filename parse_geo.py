#!/usr/bin/env python3
"""
GEO Page Fetcher & Parser
Fetches a URL as an AI crawler would see it (no JS) and extracts GEO-relevant data.
"""

import sys
import re
import json
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin


class GEOHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.meta_robots = ""
        self.headings = []  # [(level, text)]
        self.json_ld_blocks = []
        self.images = []  # [(src, alt)]
        self.internal_links = []
        self.external_links = []
        self.text_content = []
        self.word_count = 0

        self._current_tag = None
        self._current_attrs = {}
        self._in_script = False
        self._in_style = False
        self._in_json_ld = False
        self._json_ld_buffer = ""
        self._heading_buffer = ""
        self._title_buffer = ""
        self._in_title = False
        self._in_heading = False
        self._heading_level = 0
        self._base_url = ""

    def set_base_url(self, url):
        parsed = urlparse(url)
        self._base_url = f"{parsed.scheme}://{parsed.netloc}"

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self._current_tag = tag
        self._current_attrs = attrs_dict

        if tag == "title":
            self._in_title = True
            self._title_buffer = ""

        elif tag == "meta":
            name = attrs_dict.get("name", "").lower()
            content = attrs_dict.get("content", "")
            if name == "description":
                self.meta_description = content
            elif name == "robots":
                self.meta_robots = content

        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._in_heading = True
            self._heading_level = int(tag[1])
            self._heading_buffer = ""

        elif tag == "script":
            script_type = attrs_dict.get("type", "")
            if script_type == "application/ld+json":
                self._in_json_ld = True
                self._json_ld_buffer = ""
            else:
                self._in_script = True

        elif tag == "style":
            self._in_style = True

        elif tag == "img":
            src = attrs_dict.get("src", "")
            alt = attrs_dict.get("alt", "")
            self.images.append({"src": src, "alt": alt})

        elif tag == "a":
            href = attrs_dict.get("href", "")
            if href and not href.startswith(("#", "javascript:", "mailto:", "tel:")):
                if href.startswith("http"):
                    if self._base_url and urlparse(href).netloc == urlparse(self._base_url).netloc:
                        self.internal_links.append(href)
                    else:
                        self.external_links.append(href)
                elif href.startswith("/"):
                    self.internal_links.append(urljoin(self._base_url, href))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            self.title = self._title_buffer.strip()

        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._in_heading = False
            self.headings.append({
                "level": self._heading_level,
                "text": self._heading_buffer.strip()
            })

        elif tag == "script":
            if self._in_json_ld:
                self._in_json_ld = False
                try:
                    parsed = json.loads(self._json_ld_buffer)
                    self.json_ld_blocks.append(parsed)
                except json.JSONDecodeError:
                    pass
            self._in_script = False

        elif tag == "style":
            self._in_style = False

    def handle_data(self, data):
        if self._in_title:
            self._title_buffer += data
        elif self._in_heading:
            self._heading_buffer += data
        elif self._in_json_ld:
            self._json_ld_buffer += data
        elif not self._in_script and not self._in_style:
            stripped = data.strip()
            if stripped:
                self.text_content.append(stripped)

    def get_results(self):
        full_text = " ".join(self.text_content)
        self.word_count = len(full_text.split())

        images_without_alt = [img for img in self.images if not img["alt"].strip()]

        schema_types = []
        for block in self.json_ld_blocks:
            if isinstance(block, dict):
                t = block.get("@type", "Unknown")
                schema_types.append(t)
            elif isinstance(block, list):
                for item in block:
                    if isinstance(item, dict):
                        schema_types.append(item.get("@type", "Unknown"))

        h1_count = len([h for h in self.headings if h["level"] == 1])
        h2_count = len([h for h in self.headings if h["level"] == 2])

        return {
            "title": self.title,
            "meta_description": self.meta_description,
            "meta_robots": self.meta_robots,
            "word_count": self.word_count,
            "headings": self.headings,
            "h1_count": h1_count,
            "h2_count": h2_count,
            "schema_types": schema_types,
            "json_ld_blocks": self.json_ld_blocks,
            "images_total": len(self.images),
            "images_without_alt": len(images_without_alt),
            "internal_links": len(self.internal_links),
            "external_links": len(self.external_links),
            "has_content": self.word_count > 100,
        }


def fetch_url(url, user_agent="GPTBot"):
    """Fetch URL as an AI crawler would."""
    req = urllib.request.Request(url, headers={
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return f"ERROR: HTTP {e.code}"
    except Exception as e:
        return f"ERROR: {str(e)}"


def fetch_robots_txt(url):
    """Fetch and parse robots.txt for AI bot rules."""
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    content = fetch_url(robots_url, "Mozilla/5.0")

    if content.startswith("ERROR:"):
        return {"exists": False, "content": content, "ai_bots": {}}

    ai_bots = [
        "GPTBot", "OAI-SearchBot", "ChatGPT-User",
        "PerplexityBot", "Google-Extended", "ClaudeBot",
        "Googlebot", "Bingbot", "Bytespider"
    ]

    bot_status = {}
    lines = content.lower().split("\n")

    for bot in ai_bots:
        bot_lower = bot.lower()
        status = "allowed"  # default if not mentioned

        current_agent = None
        for line in lines:
            line = line.strip()
            if line.startswith("user-agent:"):
                current_agent = line.split(":", 1)[1].strip()
            elif current_agent in (bot_lower, "*"):
                if line.startswith("disallow: /") and line == "disallow: /":
                    status = "blocked"
                elif line.startswith("allow: /"):
                    status = "allowed"

        bot_status[bot] = status

    return {
        "exists": True,
        "content": content[:2000],
        "ai_bots": bot_status
    }


def check_llms_txt(url):
    """Check if llms.txt exists."""
    parsed = urlparse(url)
    llms_url = f"{parsed.scheme}://{parsed.netloc}/llms.txt"
    content = fetch_url(llms_url, "Mozilla/5.0")
    if content.startswith("ERROR:"):
        return {"exists": False}
    return {"exists": True, "length": len(content)}


def analyze(url):
    """Run full GEO analysis on a URL."""
    print(f"🔍 Fetching {url} as GPTBot...")
    html = fetch_url(url)

    if html.startswith("ERROR:"):
        print(f"❌ Failed to fetch: {html}")
        return

    parser = GEOHTMLParser()
    parser.set_base_url(url)
    parser.feed(html)
    results = parser.get_results()

    print(f"\n📊 Fetching robots.txt...")
    robots = fetch_robots_txt(url)

    print(f"📄 Checking llms.txt...")
    llms = check_llms_txt(url)

    output = {
        "url": url,
        "page_analysis": results,
        "robots_txt": robots,
        "llms_txt": llms,
        "raw_html_length": len(html),
        "js_rendering_risk": results["word_count"] < 50,
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))
    return output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_geo.py <url>")
        sys.exit(1)

    analyze(sys.argv[1])
