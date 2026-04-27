"""Fetches and parses the Guidance section from USWDS component documentation pages."""

import re
from urllib.error import URLError
from urllib.request import Request, urlopen

_cache: dict[str, str | None] = {}

_HEADERS = {
    "User-Agent": "django-cotton-uswds-mcp/1.0 (component documentation fetcher)"
}


def _extract_guidance(html: str) -> str | None:
    """Extract the Guidance section from USWDS component page HTML."""
    # The guidance section sits between an h2 "Guidance" and the next h2.
    match = re.search(
        r"<h2[^>]*>\s*Guidance\s*</h2>(.*?)(?=<h2|\Z)",
        html,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return None

    guidance_html = match.group(1)

    # Convert to readable markdown-ish text.
    text = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", guidance_html, flags=re.DOTALL)
    text = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n#### \1\n", text, flags=re.DOTALL)
    text = re.sub(r"<li[^>]*>", "\n- ", text)
    text = re.sub(r"</li>", "", text)
    text = re.sub(r"<p[^>]*>", "\n", text)
    text = re.sub(r"</p>", "", text)
    text = re.sub(r"<[^>]+>", "", text)  # strip remaining tags

    # Decode common HTML entities.
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&nbsp;", " ")
    text = text.replace("&#39;", "'")
    text = text.replace("&quot;", '"')
    text = re.sub(r"&#\d+;", "", text)
    text = re.sub(r"&\w+;", "", text)

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() or None


def fetch_uswds_guidance(url: str) -> str | None:
    """
    Fetch the Guidance section from a USWDS component page.

    Results are cached for the lifetime of the MCP server process.
    Returns None on network failure or if the Guidance section is not found.
    """
    if url in _cache:
        return _cache[url]

    try:
        req = Request(url, headers=_HEADERS)
        with urlopen(req, timeout=8) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except (URLError, OSError):
        _cache[url] = None
        return None

    result = _extract_guidance(html)
    _cache[url] = result
    return result


def clear_cache() -> None:
    """Clear the session cache (useful in tests)."""
    _cache.clear()
