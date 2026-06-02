#!/usr/bin/env python3
"""
fetch_psp.py — collect a PSP's documentation as dated raw markdown files.

Pipeline (see rules/psp-collection.md):
  discovery file (llms.txt / llms-full.txt)
    -> parse links, apply per-source url_fixups
    -> fetch each <page>.md
    -> stage, diff vs latest prior version (dated or undated baseline)
    -> keep only NEW or CHANGED -> raw/<prefix>-<slug>-YYYY-MM-DD.md
    -> write a round manifest, then STOP (a human kicks off ingest, one at a time)

Never overwrites an accepted raw file (raw/ is immutable). Re-runs are idempotent:
identical re-fetches are discarded.

Usage:
  python scripts/fetch_psp.py <psp>                       # all discovery sources
  python scripts/fetch_psp.py <psp> --source api-explorer # one discovery source
  python scripts/fetch_psp.py <psp> --limit 3             # cap pages (smoke test)
  python scripts/fetch_psp.py <psp> --dry-run             # list targets, fetch nothing
"""
from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
STAGING = ROOT / "scripts" / ".psp_staging"
MANIFEST_DIR = ROOT / "scripts" / "manifests"
CONFIG = ROOT / "scripts" / "psp_config.toml"

UA = "wiki-fetch-psp/1.0 (+payments knowledge base; respectful crawl)"
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+\.md)\)")
HEADER_LINE_RE = re.compile(r"^\s*<!--\s*(Source URL|Fetched):.*-->\s*$")
TODAY = _dt.date.today().isoformat()


def load_config() -> dict:
    """Load psp_config.toml. Uses tomllib (3.11+) or tomli if present, else a
    tiny stdlib fallback that handles this config's subset (works on 3.9+)."""
    try:
        import tomllib  # Python 3.11+
        with CONFIG.open("rb") as fh:
            return tomllib.load(fh)
    except ModuleNotFoundError:
        pass
    try:
        import tomli  # pip install tomli
        with CONFIG.open("rb") as fh:
            return tomli.load(fh)
    except ModuleNotFoundError:
        return _load_toml_subset(CONFIG)


def _load_toml_subset(path: Path) -> dict:
    """Minimal TOML reader for psp_config.toml: # comments, [table],
    [[parent.child]] arrays of tables, and `key = <json-value>` on one line
    (strings, bools, numbers, arrays — all JSON-compatible in this config)."""
    root: dict = {}
    ctx = root
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[[") and line.endswith("]]"):
            keys = line[2:-2].strip().split(".")
            d = root
            for k in keys[:-1]:
                d = d.setdefault(k, {})
            d.setdefault(keys[-1], []).append({})
            ctx = d[keys[-1]][-1]
        elif line.startswith("[") and line.endswith("]"):
            keys = line[1:-1].strip().split(".")
            d = root
            for k in keys[:-1]:
                d = d.setdefault(k, {})
            ctx = d.setdefault(keys[-1], {})
        elif "=" in line:
            key, _, val = line.partition("=")
            try:
                ctx[key.strip()] = json.loads(val.strip())
            except json.JSONDecodeError:
                ctx[key.strip()] = val.strip().strip('"')
    return root


def http_get(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def apply_fixups(url: str, fixups: list) -> str:
    for pattern, replacement in fixups:
        url = url.replace(pattern, replacement)
    return url


def parse_links(text: str, fixups: list) -> list[str]:
    """Extract de-duplicated .md links from an llms.txt, applying fixups."""
    seen, out = set(), []
    for raw_url in LINK_RE.findall(text):
        url = apply_fixups(raw_url, fixups)
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def slugify(url: str, host: str) -> str:
    """https://host/a/b/c.md -> a-b-c"""
    path = re.sub(r"^https?://", "", url)
    path = path.split("/", 1)[1] if "/" in path else path  # drop host
    path = re.sub(r"\.md$", "", path)
    path = path.strip("/").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", path).strip("-")
    return slug or "index"


def strip_header(content: str) -> str:
    lines = [ln for ln in content.splitlines() if not HEADER_LINE_RE.match(ln)]
    return "\n".join(lines).strip()


def latest_prior(prefix: str, slug: str) -> Path | None:
    base = f"{prefix}-{slug}"
    dated = sorted(RAW.glob(f"{base}-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))
    if dated:
        return dated[-1]  # ISO dates sort lexicographically
    undated = RAW / f"{base}.md"
    return undated if undated.exists() else None


def make_raw(url: str, body: str) -> str:
    return f"<!-- Source URL: {url} -->\n<!-- Fetched: {TODAY} -->\n\n{body}\n"


def collect_source(psp: str, cfg: dict, source: dict, limit: int | None, dry_run: bool,
                   results: dict) -> None:
    prefix = cfg["raw_prefix"]
    host = cfg["host"]
    fixups = source.get("url_fixups", [])
    print(f"\n[{psp}/{source['name']}] discovery: {source['url']}")
    try:
        index = http_get(source["url"])
    except Exception as exc:  # noqa: BLE001
        print(f"  !! could not fetch discovery file: {exc}")
        return
    links = parse_links(index, fixups)
    if limit:
        links = links[:limit]
    print(f"  {len(links)} target page(s)" + (" (dry-run)" if dry_run else ""))

    for url in links:
        slug = slugify(url, host)
        if dry_run:
            print(f"    - {slug}  <-  {url}")
            continue
        try:
            body = http_get(url)
        except Exception as exc:  # noqa: BLE001
            print(f"    !! fetch failed {url}: {exc}")
            results["errors"].append(url)
            continue

        staged = make_raw(url, body)
        prior = latest_prior(prefix, slug)
        target = RAW / f"{prefix}-{slug}-{TODAY}.md"

        if prior is not None and strip_header(prior.read_text(encoding="utf-8")) == strip_header(staged):
            results["unchanged"] += 1
            continue  # identical -> discard staged copy (never written)

        if target.exists():  # already collected today; immutable, skip
            results["unchanged"] += 1
            continue

        target.write_text(staged, encoding="utf-8")
        if prior is None:
            results["new"].append(target.name)
        else:
            diff = "\n".join(difflib.unified_diff(
                strip_header(prior.read_text(encoding="utf-8")).splitlines(),
                strip_header(staged).splitlines(),
                fromfile=prior.name, tofile=target.name, lineterm="",
            ))
            results["changed"].append((target.name, prior.name, diff))
        time.sleep(0.3)  # be polite


def write_manifest(psp: str, results: dict) -> Path:
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    path = MANIFEST_DIR / f"{psp}-{TODAY}.md"
    lines = [f"# PSP collection manifest — {psp} — {TODAY}", ""]
    lines.append(f"- new: {len(results['new'])}")
    lines.append(f"- changed: {len(results['changed'])}")
    lines.append(f"- unchanged (discarded): {results['unchanged']}")
    lines.append(f"- errors: {len(results['errors'])}")
    lines.append("")
    if results["new"]:
        lines += ["## New (ingest one at a time)", *[f"- [[{n[:-3]}]] — `{n}`" for n in results["new"]], ""]
    if results["changed"]:
        lines.append("## Changed (update source page from the delta)")
        for name, prior, diff in results["changed"]:
            lines += [f"### `{name}`  (was `{prior}`)", "", "```diff", diff, "```", ""]
    if results["errors"]:
        lines += ["## Errors", *[f"- {u}" for u in results["errors"]], ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description="Collect a PSP's docs as dated raw markdown.")
    ap.add_argument("psp", help="PSP key from psp_config.toml (e.g. stripe, paypal, adyen)")
    ap.add_argument("--source", help="only this discovery source (e.g. docs, api-explorer)")
    ap.add_argument("--limit", type=int, help="cap pages per source (smoke testing)")
    ap.add_argument("--dry-run", action="store_true", help="list targets, fetch nothing")
    args = ap.parse_args()

    config = load_config()
    if args.psp not in config:
        sys.exit(f"unknown PSP '{args.psp}'. Known: {', '.join(k for k in config)}")
    cfg = config[args.psp]
    sources = cfg.get("discovery", [])
    if args.source:
        sources = [s for s in sources if s["name"] == args.source]
        if not sources:
            sys.exit(f"no discovery source named '{args.source}' for {args.psp}")

    STAGING.mkdir(parents=True, exist_ok=True)
    results = {"new": [], "changed": [], "unchanged": 0, "errors": []}
    for source in sources:
        collect_source(args.psp, cfg, source, args.limit, args.dry_run, results)

    if args.dry_run:
        return 0

    manifest = write_manifest(args.psp, results)
    print("\n" + "=" * 60)
    print(f"DONE. new={len(results['new'])} changed={len(results['changed'])} "
          f"unchanged={results['unchanged']} errors={len(results['errors'])}")
    print(f"Manifest: {manifest.relative_to(ROOT)}")
    print(">>> Collection is complete. NEXT: kick off ingest ONE SOURCE AT A TIME")
    print(">>> per rules/ingest.md. Do NOT batch-ingest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
