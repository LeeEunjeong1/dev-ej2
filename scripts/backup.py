#!/usr/bin/env python3
"""Back up posts exposed by a Tistory RSS feed as Markdown."""

from __future__ import annotations

import hashlib
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import feedparser
from markdownify import markdownify


FEED_URL = os.environ.get("TISTORY_FEED_URL", "https://dev-ej2.tistory.com/rss")
POSTS_DIR = Path(__file__).resolve().parents[1] / "posts"


def yaml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def post_id(entry: feedparser.FeedParserDict) -> str:
    path = urlparse(entry.link).path.rstrip("/")
    candidate = path.rsplit("/", 1)[-1]
    if candidate.isdigit():
        return candidate
    return hashlib.sha1(entry.link.encode("utf-8")).hexdigest()[:12]


def slugify(title: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z가-힣]+", "-", title).strip("-").lower()
    return slug[:80].rstrip("-") or "post"


def entry_date(entry: feedparser.FeedParserDict) -> datetime:
    parsed = entry.get("published_parsed") or entry.get("updated_parsed")
    if parsed:
        return datetime(*parsed[:6])
    return datetime.now()


def render(entry: feedparser.FeedParserDict) -> tuple[str, str]:
    published = entry_date(entry)
    identifier = post_id(entry)
    title = entry.get("title", "Untitled").strip()
    html = entry.get("content", [{}])[0].get("value") or entry.get("description", "")
    body = markdownify(html, heading_style="ATX", bullets="-").strip()
    tags = [tag.get("term", "") for tag in entry.get("tags", []) if tag.get("term")]
    frontmatter = [
        "---",
        f"title: {yaml_string(title)}",
        f"source: {yaml_string(entry.link)}",
        f"tistory_id: {yaml_string(identifier)}",
        f"published: {yaml_string(published.isoformat())}",
        "tags:",
        *[f"  - {yaml_string(tag)}" for tag in tags],
        "---",
        "",
    ]
    filename = f"{published:%Y-%m-%d}-{identifier}-{slugify(title)}.md"
    return filename, "\n".join(frontmatter) + body + "\n"


def main() -> None:
    feed = feedparser.parse(FEED_URL)
    if feed.bozo and not feed.entries:
        raise RuntimeError(f"Unable to parse {FEED_URL}: {feed.bozo_exception}")

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    for entry in feed.entries:
        filename, content = render(entry)
        target = POSTS_DIR / filename
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            print(f"Updated {target.relative_to(POSTS_DIR.parent)}")

    print(f"RSS entries processed: {len(feed.entries)}")


if __name__ == "__main__":
    main()
