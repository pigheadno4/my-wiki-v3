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
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlsplit

from collection_discovery import DiscoveryRecord, reconcile_metronome
from collection_reporting import render_status, validate_terminal_counts, write_jsonl
from collection_versions import classify_candidate, latest_prior, next_target, source_body

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
STAGING = ROOT / "scripts" / ".psp_staging"
MANIFEST_DIR = ROOT / "scripts" / "manifests"
CONFIG = ROOT / "scripts" / "psp_config.toml"

UA = "wiki-fetch-psp/1.0 (+payments knowledge base; respectful crawl)"
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+\.md)\)")
HEADER_LINE_RE = re.compile(r"^\s*<!--\s*(Source URL|Fetched):.*-->\s*$")
TODAY = _dt.date.today().isoformat()
RETRYABLE = {408, 425, 429, 500, 501, 502, 503, 504}


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


def latest_flat_prior(prefix: str, slug: str) -> Optional[Path]:
    base = f"{prefix}-{slug}"
    dated = sorted(RAW.glob(f"{base}-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))
    if dated:
        return dated[-1]  # ISO dates sort lexicographically
    undated = RAW / f"{base}.md"
    return undated if undated.exists() else None


def make_raw(
    url: str,
    body: str,
    discovery: str = "llms.txt",
    collection_date: str = TODAY,
) -> str:
    return (
        "<!-- Source URL: " + url + " -->\n"
        "<!-- Fetched: " + collection_date + " -->\n"
        "<!-- Discovery: " + discovery + " -->\n\n"
        + body.rstrip()
        + "\n"
    )


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
        prior = latest_flat_prior(prefix, slug)
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


def relative_page_path(url: str) -> Path:
    path = urlsplit(url).path
    if path.endswith(".md"):
        path = path[:-3]
    clean = path.strip("/") or "index"
    return Path(clean + ".md")


def is_retryable_status(status: int, attempt: int) -> bool:
    if status == 403:
        return attempt == 1
    return status in RETRYABLE


def build_metronome_inventory(llms_text: str, sitemap_text: str) -> List[DiscoveryRecord]:
    return reconcile_metronome(llms_text, sitemap_text)


def fetch_with_retry(
    url: str,
    max_attempts: int = 3,
) -> Tuple[Optional[str], List[Dict[str, object]]]:
    attempts = []
    for attempt in range(1, max_attempts + 1):
        try:
            body = http_get(url)
            attempts.append({"attempt": attempt, "status": 200})
            return body, attempts
        except urllib.error.HTTPError as exc:
            attempts.append({"attempt": attempt, "status": exc.code, "error": str(exc)})
            if not is_retryable_status(exc.code, attempt) or attempt == max_attempts:
                return None, attempts
        except (TimeoutError, urllib.error.URLError) as exc:
            attempts.append({"attempt": attempt, "status": None, "error": str(exc)})
            if attempt == max_attempts:
                return None, attempts
        time.sleep(2 ** attempt)
    return None, attempts


def render_metronome_manifest(events: List[Dict[str, object]], run_id: str) -> str:
    counts = Counter(str(event.get("state")) for event in events)
    lines = ["# Metronome collection manifest - " + run_id, ""]
    for state in sorted(counts):
        lines.append("- " + state + ": " + str(counts[state]))
    failures = [event for event in events if event.get("state") == "failed"]
    if failures:
        lines += ["", "## Failures", ""]
        for event in failures:
            lines.append("- " + str(event.get("url")) + " - " + str(event.get("last_error", "")))
    lines += ["", "Collection stops here. Ingest requires a separate user action.", ""]
    return "\n".join(lines)


def _write_page_diff(
    tracking: Path,
    relative: Path,
    collection_date: str,
    previous_path: Path,
    previous: str,
    target: Path,
    candidate: str,
) -> Path:
    diff_name = "-".join(relative.with_suffix("").parts) + "-" + collection_date + ".diff"
    diff_path = tracking / "diffs" / diff_name
    diff_path.parent.mkdir(parents=True, exist_ok=True)
    diff_path.write_text(
        "\n".join(
            difflib.unified_diff(
                source_body(previous).splitlines(),
                source_body(candidate).splitlines(),
                fromfile=str(previous_path.relative_to(ROOT)),
                tofile=str(target.relative_to(ROOT)),
                lineterm="",
            )
        )
        + "\n",
        encoding="utf-8",
    )
    return diff_path


def _next_artifact_target(artifact_root: Path, stem: str, collection_date: str) -> Path:
    target = artifact_root / (stem + "-" + collection_date + ".json")
    revision = 2
    while target.exists():
        target = artifact_root / (
            stem + "-" + collection_date + "-r" + str(revision) + ".json"
        )
        revision += 1
    return target


def collect_metronome(
    cfg: Dict[str, object],
    limit: Optional[int],
    dry_run: bool,
    collection_date: str,
    run_id: str,
) -> List[Dict[str, object]]:
    discovery_sources = cfg["discovery"]
    discovery = {
        str(source["name"]): http_get(str(source["url"]))
        for source in discovery_sources
    }
    inventory = build_metronome_inventory(discovery["llms"], discovery["sitemap"])
    selected = [record for record in inventory if record.selected and record.kind == "page"]
    artifacts = [
        record for record in inventory if record.selected and record.kind == "artifact"
    ]
    if limit is not None:
        selected = selected[:limit]
    if dry_run:
        for record in selected:
            print(record.fetch_url)
        print("selected-pages=" + str(len(selected)))
        print("selected-artifacts=" + str(len(artifacts)))
        return []

    raw_root = ROOT / str(cfg["raw_root"])
    tracking = ROOT / "tracking" / "collections" / "metronome"
    discovery_dir = raw_root / "_discovery" / collection_date
    discovery_dir.mkdir(parents=True, exist_ok=True)
    (discovery_dir / "llms.txt").write_text(discovery["llms"], encoding="utf-8")
    (discovery_dir / "sitemap.xml").write_text(discovery["sitemap"], encoding="utf-8")

    events = []
    for record in selected:
        body, attempts = fetch_with_retry(record.fetch_url)
        event = record.to_dict()
        event["url"] = record.canonical_url
        event["attempts"] = attempts
        if body is None:
            event["state"] = "failed"
            event["last_error"] = attempts[-1].get("error", "fetch failed")
            events.append(event)
            continue
        relative = relative_page_path(record.fetch_url)
        previous_path = latest_prior(raw_root, relative)
        previous = previous_path.read_text(encoding="utf-8") if previous_path else None
        raw_body = make_raw(record.fetch_url, body, "llms.txt,sitemap.xml", collection_date)
        classification = classify_candidate(previous, raw_body)
        if classification == "unchanged":
            event["state"] = "unchanged"
            event["previous_raw"] = str(previous_path.relative_to(ROOT))
            events.append(event)
            continue
        target = next_target(raw_root, relative, collection_date)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(raw_body, encoding="utf-8")
        event["state"] = "collected-" + classification
        event["new_raw"] = str(target.relative_to(ROOT))
        event["content_sha256"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if classification == "changed":
            diff_path = _write_page_diff(
                tracking,
                relative,
                collection_date,
                previous_path,
                previous,
                target,
                raw_body,
            )
            event["diff_file"] = str(diff_path.relative_to(ROOT))
        events.append(event)
        time.sleep(0.3)

    artifact_root = raw_root / "_artifacts"
    artifact_root.mkdir(parents=True, exist_ok=True)
    for record in artifacts:
        body, attempts = fetch_with_retry(record.fetch_url)
        event = record.to_dict()
        event["url"] = record.canonical_url
        event["attempts"] = attempts
        if body is None:
            event["state"] = "failed"
            event["last_error"] = attempts[-1].get("error", "fetch failed")
            events.append(event)
            continue
        stem = Path(urlsplit(record.fetch_url).path).stem.replace(".", "-")
        previous_files = sorted(artifact_root.glob(stem + "-*.json"))
        previous_path = previous_files[-1] if previous_files else None
        previous_body = previous_path.read_text(encoding="utf-8") if previous_path else None
        if previous_body == body:
            event["state"] = "unchanged"
            event["previous_raw"] = str(previous_path.relative_to(ROOT))
            events.append(event)
            continue
        target = _next_artifact_target(artifact_root, stem, collection_date)
        target.write_text(body, encoding="utf-8")
        event["state"] = "collected-new" if previous_path is None else "collected-changed"
        event["new_raw"] = str(target.relative_to(ROOT))
        event["content_sha256"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if previous_path is not None:
            diff_path = tracking / "diffs" / (stem + "-" + collection_date + ".diff")
            diff_path.parent.mkdir(parents=True, exist_ok=True)
            diff_path.write_text(
                "\n".join(
                    difflib.unified_diff(
                        previous_body.splitlines(),
                        body.splitlines(),
                        fromfile=str(previous_path.relative_to(ROOT)),
                        tofile=str(target.relative_to(ROOT)),
                        lineterm="",
                    )
                )
                + "\n",
                encoding="utf-8",
            )
            event["diff_file"] = str(diff_path.relative_to(ROOT))
        events.append(event)

    validate_terminal_counts(events)
    run_path = tracking / "runs" / (run_id + ".jsonl")
    write_jsonl(run_path, events)
    latest_by_url = {event["url"]: event for event in events}
    inventory_payload = []
    for record in inventory:
        item = record.to_dict()
        event = latest_by_url.get(record.canonical_url)
        if event:
            item["collection_state"] = event["state"]
            item["local_path"] = event.get("new_raw") or event.get("previous_raw")
        else:
            item["collection_state"] = "not-in-run"
            item["local_path"] = None
        inventory_payload.append(item)
    tracking.mkdir(parents=True, exist_ok=True)
    (tracking / "inventory-current.json").write_text(
        json.dumps(inventory_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (tracking / "collection-status.md").write_text(
        render_status("metronome", inventory_payload, events),
        encoding="utf-8",
    )
    manifest_path = tracking / "runs" / (run_id + "-manifest.md")
    manifest_path.write_text(
        render_metronome_manifest(events, run_id),
        encoding="utf-8",
    )
    print("run-record=" + str(run_path.relative_to(ROOT)))
    print("manifest=" + str(manifest_path.relative_to(ROOT)))
    print("Collection is complete. Ingest requires a separate user action.")
    return events


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
    if args.psp == "metronome":
        if args.source:
            sys.exit("Metronome collection requires both llms and sitemap discovery sources")
        run_id = _dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
        collect_metronome(cfg, args.limit, args.dry_run, TODAY, run_id)
        return 0
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
