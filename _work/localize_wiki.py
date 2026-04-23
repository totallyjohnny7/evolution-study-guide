"""
Localize external Wikimedia/Wikipedia image URLs in public/exam3_review.html.

- Finds all <img src="https://...wiki...">
- Downloads to public/images/wiki/<slug>.<ext>
- Rewrites src to /images/wiki/<slug>.<ext>
- Preserves loading="lazy" (we do string replacement of just the URL inside src).
- Idempotent: skips local files that already exist.
"""

from __future__ import annotations

import concurrent.futures
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(
    r"C:/Users/johnn/Desktop/School/Evolution_EVOL4230/evolution-study-guide"
)
HTML_PATH = REPO_ROOT / "public" / "exam3_review.html"
WIKI_DIR = REPO_ROOT / "public" / "images" / "wiki"
WIKI_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = "evolution-study-guide/1.0 (https://evolution-study-guide.pages.dev)"
TIMEOUT = 15
MAX_WORKERS = 8
MAX_RETRIES = 2

# Match src="https://...wiki..." inside <img> tags.
IMG_SRC_RE = re.compile(
    r'<img\b[^>]*\bsrc="(https://[^"]*(?:wikimedia\.org|wikipedia\.org)[^"]*)"',
    re.IGNORECASE,
)


def slugify_filename(url: str) -> str:
    """Derive a deterministic filename from the URL's last path segment."""
    parsed = urllib.parse.urlparse(url)
    # Strip query, take last path segment.
    last = parsed.path.rstrip("/").split("/")[-1]
    # URL-decode (%20 -> space, etc.).
    last = urllib.parse.unquote(last)
    # Lowercase
    last = last.lower()
    # Split extension
    base, dot, ext = last.rpartition(".")
    if not dot:
        base, ext = last, ""
    # Replace any char that isn't alphanumeric, dot, dash, or underscore with underscore.
    base = re.sub(r"[^a-z0-9._-]+", "_", base)
    base = re.sub(r"_+", "_", base).strip("._-")
    ext = re.sub(r"[^a-z0-9]+", "", ext)
    if ext:
        return f"{base}.{ext}"
    return base


def download(url: str, dest: Path) -> tuple[str, int, str | None]:
    """Download url -> dest. Returns (url, bytes_written, error)."""
    if dest.exists() and dest.stat().st_size > 0:
        return (url, dest.stat().st_size, None)

    last_err: str | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = resp.read()
            tmp = dest.with_suffix(dest.suffix + ".part")
            tmp.write_bytes(data)
            tmp.replace(dest)
            return (url, len(data), None)
        except Exception as e:  # noqa: BLE001
            last_err = f"{type(e).__name__}: {e}"
    return (url, 0, last_err)


def main() -> int:
    html = HTML_PATH.read_text(encoding="utf-8")

    # Unique URLs preserving order.
    urls: list[str] = []
    seen: set[str] = set()
    for m in IMG_SRC_RE.finditer(html):
        u = m.group(1)
        if u not in seen:
            seen.add(u)
            urls.append(u)

    print(f"Found {len(urls)} unique wiki image URLs.")

    # Map URL -> target filename/path.
    url_to_dest: dict[str, Path] = {}
    # Resolve duplicates where different URLs would map to the same slug:
    used_names: dict[str, str] = {}  # slug -> source url
    for u in urls:
        slug = slugify_filename(u)
        if not slug:
            slug = "wiki_image"
        # Disambiguate if slug already claimed by a different URL.
        base_slug = slug
        counter = 1
        while slug in used_names and used_names[slug] != u:
            # Insert a number before extension
            if "." in base_slug:
                b, e = base_slug.rsplit(".", 1)
                slug = f"{b}_{counter}.{e}"
            else:
                slug = f"{base_slug}_{counter}"
            counter += 1
        used_names[slug] = u
        url_to_dest[u] = WIKI_DIR / slug

    downloaded = 0
    skipped = 0
    failed = 0
    total_bytes = 0
    failed_urls: list[tuple[str, str]] = []
    # Track which URLs were successfully available locally (for HTML rewrite).
    success_map: dict[str, Path] = {}

    # Pre-compute which already existed (for skipped count).
    pre_existing = {u for u, p in url_to_dest.items() if p.exists() and p.stat().st_size > 0}

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(download, u, url_to_dest[u]): u for u in urls}
        for fut in concurrent.futures.as_completed(futs):
            u = futs[fut]
            try:
                url, nbytes, err = fut.result()
            except Exception as e:  # noqa: BLE001
                err = f"{type(e).__name__}: {e}"
                nbytes = 0
                url = u
            if err is None:
                if u in pre_existing:
                    skipped += 1
                else:
                    downloaded += 1
                total_bytes += nbytes
                success_map[u] = url_to_dest[u]
                print(f"OK   {nbytes:>9} B  {url_to_dest[u].name}")
            else:
                failed += 1
                failed_urls.append((u, err))
                print(f"FAIL {u}  -> {err}")

    # Rewrite HTML: replace each successful URL with /images/wiki/<name>.
    # Do exact string replace on the full URL (the src="..." attr will then point locally).
    new_html = html
    replacements = 0
    for u, dest in success_map.items():
        local = f"/images/wiki/{dest.name}"
        # Count occurrences to report.
        occ = new_html.count(u)
        if occ:
            new_html = new_html.replace(u, local)
            replacements += occ

    if new_html != html:
        HTML_PATH.write_text(new_html, encoding="utf-8")
        print(f"Rewrote HTML: {replacements} URL occurrences replaced.")
    else:
        print("No HTML changes written.")

    # Sanity check: grep for any remaining src="https:// in the output HTML.
    remaining = re.findall(r'src="https://[^"]*"', new_html)
    # Exclude the Dexie script CDN.
    non_dexie = [s for s in remaining if "dexie" not in s.lower()]
    print(f"Remaining src=\"https://...\" (non-Dexie): {len(non_dexie)}")
    for s in non_dexie[:10]:
        print(f"  {s}")

    mb = total_bytes / (1024 * 1024)
    print("")
    print("===== REPORT =====")
    print(f"Unique URLs:  {len(urls)}")
    print(f"Downloaded:   {downloaded}")
    print(f"Skipped:      {skipped}")
    print(f"Failed:       {failed}")
    print(f"Total bytes:  {total_bytes} ({mb:.2f} MB)")
    if failed_urls:
        print("Failed URLs:")
        for u, err in failed_urls:
            print(f"  {u}")
            print(f"    {err}")
    print("==================")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
