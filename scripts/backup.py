#!/usr/bin/env python3
"""Back up every public Tistory post listed in the blog sitemap."""

from __future__ import annotations

import os
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


BLOG_URL = os.environ.get("TISTORY_BLOG_URL", "https://dev-ej2.tistory.com").rstrip("/")
SITEMAP_URL = os.environ.get("TISTORY_SITEMAP_URL", f"{BLOG_URL}/sitemap.xml")
POSTS_DIR = Path(__file__).resolve().parents[1] / "posts"
VERIFY_SSL = os.environ.get("TISTORY_VERIFY_SSL", "true").lower() != "false"
REQUEST_DELAY = float(os.environ.get("TISTORY_REQUEST_DELAY", "1.0"))
MAX_RETRIES = int(os.environ.get("TISTORY_MAX_RETRIES", "6"))


def yaml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def slugify(title: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z가-힣]+", "-", title).strip("-").lower()
    return slug[:80].rstrip("-") or "post"


def fetch(session: requests.Session, url: str) -> str:
    for attempt in range(MAX_RETRIES):
        response = session.get(url, timeout=30, verify=VERIFY_SSL)
        if response.status_code not in {429, 500, 502, 503, 504}:
            response.raise_for_status()
            return response.text

        retry_after = response.headers.get("Retry-After", "")
        delay = float(retry_after) if retry_after.isdigit() else min(5 * (2**attempt), 60)
        print(f"HTTP {response.status_code} for {url}; retrying in {delay:g}s")
        time.sleep(delay)

    response.raise_for_status()
    raise RuntimeError(f"Unable to fetch after {MAX_RETRIES} attempts: {url}")


def post_urls(session: requests.Session) -> list[str]:
    root = ElementTree.fromstring(fetch(session, SITEMAP_URL))
    urls: list[str] = []
    for node in root.findall("{*}url/{*}loc"):
        url = (node.text or "").strip().rstrip("/")
        path = urlparse(url).path.strip("/")
        if path.isdigit() and urlparse(url).netloc == urlparse(BLOG_URL).netloc:
            urls.append(url)
    return sorted(set(urls), key=lambda value: int(urlparse(value).path.strip("/")))


def meta(soup: BeautifulSoup, property_name: str) -> str:
    node = soup.find("meta", attrs={"property": property_name})
    return str(node.get("content", "")).strip() if node else ""


def render(url: str, html: str) -> tuple[str, str, str]:
    soup = BeautifulSoup(html, "html.parser")
    identifier = urlparse(url).path.strip("/")
    title = meta(soup, "og:title") or soup.title.get_text(strip=True)
    published_raw = meta(soup, "article:published_time")
    published = datetime.fromisoformat(published_raw) if published_raw else datetime.now().astimezone()

    article = soup.select_one("#article-view .contents_style") or soup.select_one("#article-view")
    if article is None:
        raise RuntimeError(f"Article body not found: {url}")

    # Tistory injects presentation-only nodes that are not part of the post body.
    for unwanted in article.select("script, style"):
        unwanted.decompose()
    body = markdownify(str(article), heading_style="ATX", bullets="-").strip()
    tags = [node.get_text(" ", strip=True) for node in soup.select(".tags a, .tag-list a")]
    tags = list(dict.fromkeys(tag for tag in tags if tag))

    frontmatter = [
        "---",
        f"title: {yaml_string(title)}",
        f"source: {yaml_string(url)}",
        f"tistory_id: {yaml_string(identifier)}",
        f"published: {yaml_string(published.isoformat())}",
        "tags:",
        *[f"  - {yaml_string(tag)}" for tag in tags],
        "---",
        "",
    ]
    filename = f"{published:%Y-%m-%d}-{identifier}-{slugify(title)}.md"
    return identifier, filename, "\n".join(frontmatter) + body + "\n"


def remove_old_filename(identifier: str, keep: Path) -> None:
    expected = f'tistory_id: "{identifier}"'
    for existing in POSTS_DIR.glob("*.md"):
        if existing != keep and expected in existing.read_text(encoding="utf-8"):
            existing.unlink()
            print(f"Removed renamed file {existing.relative_to(POSTS_DIR.parent)}")


def main() -> None:
    session = requests.Session()
    session.headers["User-Agent"] = "dev-ej2-tistory-backup/1.0"
    urls = post_urls(session)
    if not urls:
        raise RuntimeError(f"No public post URLs found in {SITEMAP_URL}")

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    for index, url in enumerate(urls, start=1):
        identifier, filename, content = render(url, fetch(session, url))
        target = POSTS_DIR / filename
        remove_old_filename(identifier, target)
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            print(f"Updated {target.relative_to(POSTS_DIR.parent)}")
        print(f"Processed {index}/{len(urls)}: {url}")
        if REQUEST_DELAY:
            time.sleep(REQUEST_DELAY)

    print(f"Public posts processed: {len(urls)}")


if __name__ == "__main__":
    main()
