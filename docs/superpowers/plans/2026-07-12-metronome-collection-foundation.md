# Metronome Collection Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify the deterministic Metronome discovery, nested raw versioning, retry, run-record, and monitoring foundation through a three-page smoke test, without starting wiki ingest or the full 225-page collection.

**Architecture:** Keep `fetch_psp.py` as the public collector CLI and extract focused standard-library modules for discovery reconciliation, immutable version comparison, and reporting. Register Metronome in the existing provider registry with both `llms.txt` and sitemap discovery sources, store its content under `raw/metronome/`, and make every state transition auditable through per-run JSONL plus generated aggregate views.

**Tech Stack:** Python 3.9-compatible standard library (`argparse`, `dataclasses`, `hashlib`, `json`, `pathlib`, `unittest`, `urllib`, `xml.etree.ElementTree`), TOML registry with the existing fallback parser, Markdown documentation.

## Global Constraints

- Collection and ingest remain separate; this plan must never create or update wiki source, company, concept, index, or log pages.
- English canonical scope is the union of Metronome `llms.txt` and `sitemap.xml`; `/fr/`, external blog, and status targets are excluded with recorded reasons.
- The observed baseline is 225 English documentation pages plus two separate OpenAPI JSON artifacts; verification reports drift instead of hard-coding the count as permanent truth.
- Accepted raw files are immutable. Unchanged content creates no new raw file; changed content retains every dated version.
- Body SHA-256 comparison ignores only repository-owned `Source URL`, `Fetched`, and `Discovery` metadata headers.
- Raw content lives under `raw/metronome/` and preserves URL directory hierarchy.
- Every selected URL ends in exactly one reconciled terminal state for a completed run.
- Network retries cover timeouts, HTTP 408, 425, 429, and 500-504; HTTP 403 receives one retry; other terminal failures remain visible.
- Python code must run on Python 3.9 and use no third-party package.
- `CLAUDE copy.md` is unrelated user content and must remain untouched.

## Delivery Sequence

This is Plan 1 of 3:

1. **This plan:** collection, reconciliation, immutable versions, monitoring, and a limited smoke test.
2. **Later plan:** nested wiki paths, Metronome index/log/company/source/concept capsule, and deterministic link/count validation.
3. **Later plan:** worktree-based parallel ingest, receipts, concept leases/reduction, model routing, and the low-cost-model benchmark.

The full 225-page collection requires a separate user-approved execution checkpoint after this plan's smoke test passes.

---

### Task 1: Discovery Reconciliation Module

**Files:**
- Create: `scripts/collection_discovery.py`
- Create: `tests/__init__.py`
- Create: `tests/test_collection_discovery.py`
- Create: `tests/fixtures/metronome/llms.txt`
- Create: `tests/fixtures/metronome/sitemap.xml`

**Interfaces:**
- Produces: `DiscoveryRecord`, `canonicalize_url(url)`, `parse_llms(text)`, `parse_sitemap(text)`, and `reconcile_metronome(llms_text, sitemap_text)`.
- `reconcile_metronome` returns a deterministic `List[DiscoveryRecord]` sorted by canonical URL.
- Later tasks consume `DiscoveryRecord.to_dict()` for inventories and reports.

- [ ] **Step 1: Add representative discovery fixtures**

Create `tests/fixtures/metronome/llms.txt`:

```markdown
# Metronome

- [Home](https://docs.metronome.com/guides/get-started/home.md)
- [Contracts](https://docs.metronome.com/api-reference/contracts/create-a-contract.md)
- [OpenAPI](https://docs.metronome.com/openapi.json)
- [Blog](https://metronome.com/blog)
- [Status](https://status.metronome.com/)
```

Create `tests/fixtures/metronome/sitemap.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://docs.metronome.com/guides/get-started/home</loc></url>
  <url><loc>https://docs.metronome.com/api-reference/contracts/create-a-contract</loc></url>
  <url><loc>https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant</loc></url>
  <url><loc>https://docs.metronome.com/fr/guides/get-started/home</loc></url>
</urlset>
```

- [ ] **Step 2: Write failing reconciliation tests**

Create `tests/test_collection_discovery.py`:

```python
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection_discovery import canonicalize_url, reconcile_metronome  # noqa: E402


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        fixture = ROOT / "tests" / "fixtures" / "metronome"
        self.llms = (fixture / "llms.txt").read_text(encoding="utf-8")
        self.sitemap = (fixture / "sitemap.xml").read_text(encoding="utf-8")

    def test_canonicalize_markdown_and_trailing_slash(self):
        self.assertEqual(
            canonicalize_url("https://docs.metronome.com/guides/home.md#start"),
            "https://docs.metronome.com/guides/home",
        )

    def test_reconcile_selects_english_union(self):
        records = reconcile_metronome(self.llms, self.sitemap)
        selected = [record for record in records if record.selected and record.kind == "page"]
        self.assertEqual(len(selected), 3)
        by_url = {record.canonical_url: record for record in records}
        home = by_url["https://docs.metronome.com/guides/get-started/home"]
        self.assertTrue(home.in_llms)
        self.assertTrue(home.in_sitemap)
        gap = by_url[
            "https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant"
        ]
        self.assertFalse(gap.in_llms)
        self.assertTrue(gap.in_sitemap)
        self.assertEqual(
            gap.fetch_url,
            "https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant.md",
        )

    def test_reconcile_records_artifact_and_exclusions(self):
        records = reconcile_metronome(self.llms, self.sitemap)
        payload = json.dumps([record.to_dict() for record in records])
        self.assertIn('"kind": "artifact"', payload)
        self.assertIn('"exclusion_reason": "localized-fr"', payload)
        self.assertIn('"exclusion_reason": "external-host"', payload)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run tests and confirm the module is missing**

Run: `python3 -m unittest tests.test_collection_discovery -v`

Expected: FAIL with `ModuleNotFoundError: No module named 'collection_discovery'`.

- [ ] **Step 4: Implement canonical discovery parsing**

Create `scripts/collection_discovery.py`:

```python
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional
from urllib.parse import urlsplit, urlunsplit

LLMS_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
DOC_HOST = "docs.metronome.com"


@dataclass(frozen=True)
class DiscoveryRecord:
    canonical_url: str
    fetch_url: str
    in_llms: bool
    in_sitemap: bool
    language: str
    selected: bool
    kind: str
    section: str
    exclusion_reason: Optional[str] = None

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


def canonicalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    path = parts.path.rstrip("/") or "/"
    if path.endswith(".md"):
        path = path[:-3]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def parse_llms(text: str) -> List[str]:
    return sorted(set(LLMS_LINK_RE.findall(text)))


def parse_sitemap(text: str) -> List[str]:
    root = ET.fromstring(text)
    return sorted(
        set(
            element.text.strip()
            for element in root.iter()
            if element.tag.endswith("loc") and element.text
        )
    )


def _section(path: str) -> str:
    segments = [part for part in path.split("/") if part]
    return "/".join(segments[:2]) if segments else "root"


def reconcile_metronome(llms_text: str, sitemap_text: str) -> List[DiscoveryRecord]:
    llms_urls = parse_llms(llms_text)
    sitemap_urls = parse_sitemap(sitemap_text)
    llms_by_canonical = {canonicalize_url(url): url for url in llms_urls}
    sitemap_by_canonical = {canonicalize_url(url): url for url in sitemap_urls}
    records = []
    for canonical in sorted(set(llms_by_canonical) | set(sitemap_by_canonical)):
        parts = urlsplit(canonical)
        in_llms = canonical in llms_by_canonical
        in_sitemap = canonical in sitemap_by_canonical
        language = "fr" if parts.path.startswith("/fr/") else "en"
        kind = "artifact" if parts.path.endswith(".json") else "page"
        reason = None
        if parts.netloc != DOC_HOST:
            reason = "external-host"
        elif language == "fr":
            reason = "localized-fr"
        selected = reason is None
        original = llms_by_canonical.get(canonical) or sitemap_by_canonical[canonical]
        if kind == "artifact":
            fetch_url = original
        elif original.endswith(".md"):
            fetch_url = original
        else:
            fetch_url = original.rstrip("/") + ".md"
        records.append(
            DiscoveryRecord(
                canonical_url=canonical,
                fetch_url=fetch_url,
                in_llms=in_llms,
                in_sitemap=in_sitemap,
                language=language,
                selected=selected,
                kind=kind,
                section=_section(parts.path),
                exclusion_reason=reason,
            )
        )
    return records
```

- [ ] **Step 5: Run reconciliation tests**

Run: `python3 -m unittest tests.test_collection_discovery -v`

Expected: `Ran 3 tests` and `OK`.

- [ ] **Step 6: Commit discovery reconciliation**

```bash
git add scripts/collection_discovery.py tests/__init__.py tests/test_collection_discovery.py tests/fixtures/metronome/llms.txt tests/fixtures/metronome/sitemap.xml
git commit -m "feat: reconcile metronome discovery sources"
```

---

### Task 2: Immutable Nested Raw Versioning

**Files:**
- Create: `scripts/collection_versions.py`
- Create: `tests/test_collection_versions.py`

**Interfaces:**
- Produces: `body_sha256(content)`, `latest_prior(raw_root, relative_path)`, `classify_candidate(previous, candidate)`, and `next_target(raw_root, relative_path, collection_date)`.
- `classify_candidate` returns `new`, `changed`, or `unchanged`.
- Later collector code uses the returned `Path` and never overwrites it.

- [ ] **Step 1: Write failing versioning tests**

Create `tests/test_collection_versions.py`:

```python
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection_versions import (  # noqa: E402
    body_sha256,
    classify_candidate,
    latest_prior,
    next_target,
)


class VersionTests(unittest.TestCase):
    def test_hash_ignores_only_repository_headers(self):
        left = "<!-- Source URL: a -->\n<!-- Fetched: 2026-07-12 -->\n\n# Body\n"
        right = "<!-- Source URL: b -->\n<!-- Fetched: 2026-08-05 -->\n\n# Body\n"
        self.assertEqual(body_sha256(left), body_sha256(right))
        self.assertNotEqual(body_sha256(left), body_sha256(right + "Changed\n"))

    def test_latest_prior_and_same_day_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            page = raw / "guides" / "home-2026-07-12.md"
            page.parent.mkdir(parents=True)
            page.write_text("old", encoding="utf-8")
            self.assertEqual(
                latest_prior(raw, Path("guides/home.md")),
                page,
            )
            first = next_target(raw, Path("guides/home.md"), "2026-08-05")
            first.parent.mkdir(parents=True, exist_ok=True)
            first.write_text("new", encoding="utf-8")
            self.assertEqual(
                next_target(raw, Path("guides/home.md"), "2026-08-05").name,
                "home-2026-08-05-r2.md",
            )

    def test_classification(self):
        self.assertEqual(classify_candidate(None, "body"), "new")
        self.assertEqual(classify_candidate("body", "body"), "unchanged")
        self.assertEqual(classify_candidate("body", "changed"), "changed")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm the module is missing**

Run: `python3 -m unittest tests.test_collection_versions -v`

Expected: FAIL with `ModuleNotFoundError: No module named 'collection_versions'`.

- [ ] **Step 3: Implement immutable version helpers**

Create `scripts/collection_versions.py`:

```python
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Optional

HEADER_RE = re.compile(
    r"^\s*<!--\s*(Source URL|Fetched|Discovery):.*-->\s*$",
    re.MULTILINE,
)
DATED_RE = re.compile(r"-(\d{4}-\d{2}-\d{2})(?:-r(\d+))?\.md$")


def source_body(content: str) -> str:
    return HEADER_RE.sub("", content).strip()


def body_sha256(content: str) -> str:
    return hashlib.sha256(source_body(content).encode("utf-8")).hexdigest()


def classify_candidate(previous: Optional[str], candidate: str) -> str:
    if previous is None:
        return "new"
    return "unchanged" if body_sha256(previous) == body_sha256(candidate) else "changed"


def latest_prior(raw_root: Path, relative_path: Path) -> Optional[Path]:
    parent = raw_root / relative_path.parent
    stem = relative_path.stem
    candidates = [path for path in parent.glob(stem + "-*.md") if DATED_RE.search(path.name)]
    def version_key(path: Path):
        match = DATED_RE.search(path.name)
        return (match.group(1), int(match.group(2) or "1"))
    return sorted(candidates, key=version_key)[-1] if candidates else None


def next_target(raw_root: Path, relative_path: Path, collection_date: str) -> Path:
    parent = raw_root / relative_path.parent
    base = parent / (relative_path.stem + "-" + collection_date + ".md")
    if not base.exists():
        return base
    revision = 2
    while True:
        candidate = parent / (
            relative_path.stem + "-" + collection_date + "-r" + str(revision) + ".md"
        )
        if not candidate.exists():
            return candidate
        revision += 1
```

- [ ] **Step 4: Run versioning tests**

Run: `python3 -m unittest tests.test_collection_versions -v`

Expected: `Ran 3 tests` and `OK`.

- [ ] **Step 5: Commit immutable versioning**

```bash
git add scripts/collection_versions.py tests/test_collection_versions.py
git commit -m "feat: add immutable nested raw versioning"
```

---

### Task 3: Run Records and Generated Monitor

**Files:**
- Create: `scripts/collection_reporting.py`
- Create: `tests/test_collection_reporting.py`

**Interfaces:**
- Produces: `write_jsonl(path, events)`, `validate_terminal_counts(events)`, and `render_status(provider, records, events)`.
- `validate_terminal_counts` raises `ValueError` when selected totals do not reconcile.
- Later collector code writes per-run fragments first and aggregate views only after validation.

- [ ] **Step 1: Write failing reporting tests**

Create `tests/test_collection_reporting.py`:

```python
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection_reporting import (  # noqa: E402
    render_status,
    validate_terminal_counts,
    write_jsonl,
)


class ReportingTests(unittest.TestCase):
    def test_terminal_counts_reconcile(self):
        events = [
            {"selected": True, "state": "collected-new"},
            {"selected": True, "state": "unchanged"},
            {"selected": True, "state": "failed"},
        ]
        self.assertEqual(validate_terminal_counts(events), 3)

    def test_pending_state_rejects_completed_run(self):
        with self.assertRaisesRegex(ValueError, "non-terminal"):
            validate_terminal_counts([{"selected": True, "state": "pending"}])

    def test_jsonl_and_markdown(self):
        events = [{"url": "https://example.test/a", "selected": True, "state": "failed"}]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "run.jsonl"
            write_jsonl(path, events)
            self.assertEqual(json.loads(path.read_text().strip())["state"], "failed")
        status = render_status("metronome", [], events)
        self.assertIn("# Metronome Collection Status", status)
        self.assertIn("| failed | 1 |", status)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm the module is missing**

Run: `python3 -m unittest tests.test_collection_reporting -v`

Expected: FAIL with `ModuleNotFoundError: No module named 'collection_reporting'`.

- [ ] **Step 3: Implement run reporting**

Create `scripts/collection_reporting.py`:

```python
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List

TERMINAL = {
    "collected-new",
    "collected-changed",
    "unchanged",
    "retry-pending",
    "failed",
}


def write_jsonl(path: Path, events: Iterable[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
        encoding="utf-8",
    )


def validate_terminal_counts(events: List[Dict[str, object]]) -> int:
    selected = [event for event in events if event.get("selected")]
    bad = [event for event in selected if event.get("state") not in TERMINAL]
    if bad:
        raise ValueError("selected run contains non-terminal states")
    return len(selected)


def render_status(
    provider: str,
    records: List[Dict[str, object]],
    events: List[Dict[str, object]],
) -> str:
    counts = Counter(str(event.get("state")) for event in events)
    title = provider.replace("-", " ").title()
    lines = ["# " + title + " Collection Status", "", "## Current summary", ""]
    lines += ["| State | Count |", "| --- | ---: |"]
    for state in sorted(counts):
        lines.append("| " + state + " | " + str(counts[state]) + " |")
    lines += ["", "## Discovery reconciliation", ""]
    membership = Counter(
        "both" if record.get("in_llms") and record.get("in_sitemap")
        else "llms-only" if record.get("in_llms")
        else "sitemap-only"
        for record in records
        if record.get("selected") and record.get("kind") == "page"
    )
    lines += ["| Membership | Count |", "| --- | ---: |"]
    for name in ("both", "llms-only", "sitemap-only"):
        lines.append("| " + name + " | " + str(membership[name]) + " |")
    lines += ["", "## Failed and retry queue", ""]
    for event in events:
        if event.get("state") in {"failed", "retry-pending"}:
            lines.append("- " + str(event.get("url")) + " - " + str(event.get("last_error", "")))
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run reporting tests**

Run: `python3 -m unittest tests.test_collection_reporting -v`

Expected: `Ran 3 tests` and `OK`.

- [ ] **Step 5: Commit reporting foundation**

```bash
git add scripts/collection_reporting.py tests/test_collection_reporting.py
git commit -m "feat: add collection run reporting"
```

---

### Task 4: Register Metronome and Refactor the Collector CLI

**Files:**
- Modify: `scripts/psp_config.toml`
- Modify: `scripts/fetch_psp.py`
- Create: `tests/test_fetch_psp.py`

**Interfaces:**
- `python3 scripts/fetch_psp.py metronome --dry-run` fetches discovery inputs, reconciles them, prints selected counts, and writes nothing.
- `python3 scripts/fetch_psp.py metronome --limit 3` collects at most three selected pages into `raw/metronome/` and writes run artifacts under `tracking/collections/metronome/`.
- Existing Stripe, PayPal, and Adyen configuration remains accepted.

- [ ] **Step 1: Add failing CLI behavior tests**

Create `tests/test_fetch_psp.py`:

```python
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_psp  # noqa: E402


class FetchPspTests(unittest.TestCase):
    def test_metronome_relative_page_path(self):
        self.assertEqual(
            fetch_psp.relative_page_path(
                "https://docs.metronome.com/guides/get-started/home.md"
            ),
            Path("guides/get-started/home.md"),
        )

    def test_retryable_status_policy(self):
        self.assertTrue(fetch_psp.is_retryable_status(429, 1))
        self.assertTrue(fetch_psp.is_retryable_status(503, 2))
        self.assertTrue(fetch_psp.is_retryable_status(403, 1))
        self.assertFalse(fetch_psp.is_retryable_status(403, 2))
        self.assertFalse(fetch_psp.is_retryable_status(404, 1))

    def test_dry_run_does_not_write(self):
        llms = "- [Home](https://docs.metronome.com/guides/get-started/home.md)"
        sitemap = "<urlset><url><loc>https://docs.metronome.com/guides/get-started/home</loc></url></urlset>"
        with tempfile.TemporaryDirectory() as tmp, patch.object(fetch_psp, "ROOT", Path(tmp)):
            result = fetch_psp.build_metronome_inventory(llms, sitemap)
            self.assertEqual(len([item for item in result if item.selected]), 1)
            self.assertFalse((Path(tmp) / "raw").exists())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and verify the missing interfaces**

Run: `python3 -m unittest tests.test_fetch_psp -v`

Expected: FAIL because `relative_page_path`, `is_retryable_status`, and `build_metronome_inventory` do not exist.

- [ ] **Step 3: Add the Metronome registry entry**

Append to `scripts/psp_config.toml`:

```toml
# Metronome - Stripe-owned usage-based billing platform
[metronome]
host = "docs.metronome.com"
raw_root = "raw/metronome"
md_rule = "append-.md"
exclude_path_prefixes = ["/fr/"]
include_hosts = ["docs.metronome.com"]

[[metronome.discovery]]
name = "llms"
url = "https://docs.metronome.com/llms.txt"
kind = "llms.txt"
url_fixups = []

[[metronome.discovery]]
name = "sitemap"
url = "https://docs.metronome.com/sitemap.xml"
kind = "sitemap.xml"
url_fixups = []
```

- [ ] **Step 4: Refactor `fetch_psp.py` around the new modules**

Add these imports and constants:

```python
import hashlib
import urllib.error
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlsplit

from collection_discovery import DiscoveryRecord, reconcile_metronome
from collection_reporting import render_status, validate_terminal_counts, write_jsonl
from collection_versions import classify_candidate, latest_prior, next_target, source_body

RETRYABLE = {408, 425, 429, 500, 501, 502, 503, 504}
```

Replace provider-specific path flattening for nested providers with:

```python
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
```

Add a fetch helper that returns response text and attempt metadata:

```python
def fetch_with_retry(url: str, max_attempts: int = 3) -> Tuple[Optional[str], List[Dict[str, object]]]:
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
```

Add a Metronome collection path that:

```python
def collect_metronome(
    cfg: Dict[str, object],
    limit: Optional[int],
    dry_run: bool,
    collection_date: str,
    run_id: str,
) -> List[Dict[str, object]]:
    discovery = {source["name"]: http_get(source["url"]) for source in cfg["discovery"]}
    inventory = build_metronome_inventory(discovery["llms"], discovery["sitemap"])
    selected = [record for record in inventory if record.selected and record.kind == "page"]
    artifacts = [record for record in inventory if record.selected and record.kind == "artifact"]
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
            diff_name = "-".join(relative.with_suffix("").parts) + "-" + collection_date + ".diff"
            diff_path = tracking / "diffs" / diff_name
            diff_path.parent.mkdir(parents=True, exist_ok=True)
            diff_path.write_text(
                "\n".join(
                    difflib.unified_diff(
                        source_body(previous).splitlines(),
                        source_body(raw_body).splitlines(),
                        fromfile=str(previous_path.relative_to(ROOT)),
                        tofile=str(target.relative_to(ROOT)),
                        lineterm="",
                    )
                ) + "\n",
                encoding="utf-8",
            )
            event["diff_file"] = str(diff_path.relative_to(ROOT))
        events.append(event)

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
        stem = Path(urlsplit(record.fetch_url).path).stem
        previous_files = sorted(artifact_root.glob(stem + "-*.json"))
        previous_path = previous_files[-1] if previous_files else None
        previous_body = previous_path.read_text(encoding="utf-8") if previous_path else None
        if previous_body == body:
            event["state"] = "unchanged"
            event["previous_raw"] = str(previous_path.relative_to(ROOT))
            events.append(event)
            continue
        target = artifact_root / (stem + "-" + collection_date + ".json")
        revision = 2
        while target.exists():
            target = artifact_root / (
                stem + "-" + collection_date + "-r" + str(revision) + ".json"
            )
            revision += 1
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
                ) + "\n",
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
    return events
```

Rename the existing flat-provider lookup to avoid shadowing the imported nested helper and make its annotation Python 3.9-compatible:

```python
def latest_flat_prior(prefix: str, slug: str) -> Optional[Path]:
    base = f"{prefix}-{slug}"
    dated = sorted(RAW.glob(f"{base}-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))
    if dated:
        return dated[-1]
    undated = RAW / f"{base}.md"
    return undated if undated.exists() else None
```

Change the existing legacy `collect_source` call from `latest_prior(prefix, slug)` to `latest_flat_prior(prefix, slug)`. Remove the old local `latest_prior` definition so nested collection calls the imported helper.

Change `make_raw` to accept explicit metadata while preserving the existing two-argument legacy call:

```python
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
        + body.rstrip() + "\n"
    )
```

In `main`, derive a collision-resistant run id and route only Metronome through the new path while leaving existing providers on their current path:

```python
run_id = _dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
if args.psp == "metronome":
    collect_metronome(cfg, args.limit, args.dry_run, TODAY, run_id)
    return 0
```

- [ ] **Step 5: Run focused and full unit tests**

Run: `python3 -m unittest tests.test_fetch_psp -v`

Expected: `Ran 3 tests` and `OK`.

Run: `python3 -m unittest discover -s tests -v`

Expected: `Ran 12 tests` and `OK`.

- [ ] **Step 6: Verify existing provider dry-run parsing remains available**

Run: `python3 scripts/fetch_psp.py stripe --limit 1 --dry-run`

Expected: one Stripe target is printed and no raw, tracking, or manifest file is created.

- [ ] **Step 7: Commit the provider-aware collector**

```bash
git add scripts/fetch_psp.py scripts/psp_config.toml tests/test_fetch_psp.py
git commit -m "feat: add metronome collection pipeline"
```

---

### Task 5: Metronome Collection Rules and Operator Contract

**Files:**
- Create: `rules/psp/metronome.md`
- Modify: `rules/psp-collection.md`
- Modify: `CLAUDE.md`

**Interfaces:**
- Documents exact discovery scope, nested raw paths, monitoring files, smoke-test command, full-run approval gate, and collection-to-ingest boundary.
- The Workflow Index continues to route collection work through `rules/psp-collection.md` and then the provider profile.

- [ ] **Step 1: Write the Metronome provider profile**

Create `rules/psp/metronome.md` with:

```markdown
# Provider: Metronome - collection profile

> Used with `rules/psp-collection.md` and `scripts/psp_config.toml`. Verified 2026-07-12.

## Ownership and wiki placement

Metronome is a Stripe-owned usage-based billing platform with an independent provider capsule:

- Raw root: `raw/metronome/`
- Provider index: `wiki/metronome-index.md`
- Provider log: `wiki/metronome-log.md`
- Company page: `wiki/companies/metronome.md`
- Source summaries: `wiki/sources/metronome/`
- Concepts: `wiki/concepts/metronome/`

## Discovery sources

| Source | URL | Purpose |
| --- | --- | --- |
| LLM index | `https://docs.metronome.com/llms.txt` | Markdown targets and OpenAPI artifacts |
| Sitemap | `https://docs.metronome.com/sitemap.xml` | Canonical-page coverage and gap detection |

Collect the English union. Exclude `/fr/`, `https://metronome.com/blog`, and `https://status.metronome.com/`, recording each exclusion.

## Pilot baseline

- 208 pages shared by both discovery sources
- 17 additional English sitemap-only pages
- 225 selected English documentation pages
- 2 separate OpenAPI JSON artifacts
- 105 excluded French-localized pages

Treat these as drift-detection baselines, not permanent constants.

## Commands

```bash
python3 scripts/fetch_psp.py metronome --dry-run
python3 scripts/fetch_psp.py metronome --limit 3
```

Do not run the full corpus until the limited smoke test, monitor reconciliation, immutable rerun check, and user checkpoint all pass.

## Boundary

Collection ends after raw files, run records, aggregate status, and manifest validation. It never starts ingest automatically.
```

- [ ] **Step 2: Update the shared collection rule**

Add to `rules/psp-collection.md` under collection behavior:

```markdown
Providers may use either flat raw filenames or a configured nested `raw_root`. When a provider has multiple discovery formats, reconcile them into one canonical inventory before fetching. Each selected URL must reach a terminal collection state, and aggregate status is written only after per-run records reconcile.
```

Add under the collection-to-ingest boundary:

```markdown
For providers with a smoke-test gate, stop after the limited run and request approval before collecting the full corpus. A successful smoke test does not authorize ingest.
```

- [ ] **Step 3: Update the root directory schema**

Add these provider-capsule examples to the `raw/` and `wiki/` portions of `CLAUDE.md`:

```text
├── raw/
│   └── metronome/          # provider capsule preserving documentation paths
├── tracking/collections/    # generated collection inventory, runs, diffs, and status
└── wiki/
    ├── metronome-index.md
    ├── metronome-log.md
    ├── sources/metronome/
    └── concepts/metronome/
```

- [ ] **Step 4: Check documentation for incomplete markers and stale flat-only claims**

Run:

```bash
rg -n "\\b(T[B]D|T[O]DO|F[I]XME)\\b|raw/.*-.*-YYYY-MM-DD|top-level files" CLAUDE.md rules/psp-collection.md rules/psp/metronome.md
```

Expected: no incomplete-marker hits; any remaining flat-only text is explicitly scoped to legacy providers rather than stated as universal behavior.

- [ ] **Step 5: Commit the operator contract**

```bash
git add CLAUDE.md rules/psp-collection.md rules/psp/metronome.md
git commit -m "docs: add metronome collection workflow"
```

---

### Task 6: Offline Verification and Live Dry Run

**Files:**
- Modify only if a test exposes a defect: files owned by Tasks 1-5
- Do not commit downloaded live discovery data during the dry run

**Interfaces:**
- Proves the implementation is Python 3.9-compatible at the syntax level, deterministic offline, non-mutating in dry-run mode, and able to reconcile the live discovery sources.

- [ ] **Step 1: Run the complete offline test suite**

Run: `python3 -m unittest discover -s tests -v`

Expected: all 12 tests pass.

- [ ] **Step 2: Compile all collector modules**

Run:

```bash
python3 -m py_compile scripts/fetch_psp.py scripts/collection_discovery.py scripts/collection_versions.py scripts/collection_reporting.py
```

Expected: exit code 0 and no output.

- [ ] **Step 3: Confirm dry-run immutability before network access**

Run: `git status --short`

Expected: only pre-existing unrelated user files are listed; no `raw/metronome/` or `tracking/collections/metronome/` paths exist.

- [ ] **Step 4: Reconcile the live discovery set without collecting pages**

Run: `python3 scripts/fetch_psp.py metronome --dry-run`

Expected on the 2026-07-12 baseline: 225 selected English pages are reported, two JSON artifacts are reported separately, 105 French pages and two external targets are excluded, and no raw or tracking file is written. If counts drift, record the new counts and URL-level differences rather than changing the code to force 225.

- [ ] **Step 5: Recheck the worktree after dry run**

Run: `git status --short`

Expected: identical output to Step 3.

- [ ] **Step 6: Run the existing wiki validator as a regression check**

Run: `python3 scripts/validate_wiki.py`

Expected: no new validation issue attributable to this plan. Pre-existing unrelated issues, if any, are recorded without being repaired in this task.

- [ ] **Step 7: Commit only defect fixes, if the verification exposed any**

When no defect was found, make no commit. When a defect was fixed:

```bash
git add scripts/fetch_psp.py scripts/collection_discovery.py scripts/collection_versions.py scripts/collection_reporting.py scripts/psp_config.toml tests
git commit -m "fix: harden metronome collection dry run"
```

---

### Task 7: Three-Page Collection Smoke Test and Approval Checkpoint

**Files:**
- Create through the collector: `raw/metronome/_discovery/YYYY-MM-DD/llms.txt`
- Create through the collector: `raw/metronome/_discovery/YYYY-MM-DD/sitemap.xml`
- Create through the collector: up to three dated raw Markdown pages under `raw/metronome/`
- Create through the collector: two dated JSON artifacts under `raw/metronome/_artifacts/`
- Create through the collector: `tracking/collections/metronome/inventory-current.json`
- Create through the collector: `tracking/collections/metronome/collection-status.md`
- Create through the collector: `tracking/collections/metronome/runs/YYYY-MM-DDTHHMMSS.jsonl`

**Interfaces:**
- Produces the first real collection evidence without authorizing the remaining corpus or any ingest.
- A successful rerun must report all three pages and two artifacts unchanged and create no duplicate raw versions.

- [ ] **Step 1: Run the limited collection**

Run: `python3 scripts/fetch_psp.py metronome --limit 3`

Expected: three selected pages and two OpenAPI artifacts reach `collected-new`, discovery snapshots are saved, and generated status reconciles to five selected terminal events.

- [ ] **Step 2: Inspect the generated monitor and run record**

Run:

```bash
sed -n '1,220p' tracking/collections/metronome/collection-status.md
python3 -m json.tool tracking/collections/metronome/inventory-current.json >/dev/null
```

Expected: Markdown shows three collected pages, two collected artifacts, and accurate discovery membership; JSON parsing exits 0.

- [ ] **Step 3: Verify raw metadata and non-empty bodies**

Run:

```bash
find raw/metronome -type f -name '*.md' -print
rg -L "^<!-- Source URL: https://docs\.metronome\.com/" raw/metronome -g '*.md'
```

Expected: exactly three collected page files are listed outside `_discovery`; the metadata check prints no page missing its source URL.

- [ ] **Step 4: Rerun the same limited collection**

Run: `python3 scripts/fetch_psp.py metronome --limit 3`

Expected: all three pages and both artifacts are `unchanged`; no second dated or `-r2` raw file is created.

- [ ] **Step 5: Run smoke-test regression checks**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_wiki.py
git diff --check
```

Expected: unit tests pass, the wiki validator has no new issue attributable to the collector, and `git diff --check` exits 0.

- [ ] **Step 6: Commit the accepted smoke-test evidence**

After confirming the three raw pages are verbatim Markdown captures:

```bash
git add raw/metronome tracking/collections/metronome
git commit -m "data: smoke test metronome collection"
```

- [ ] **Step 7: Stop for the full-collection decision**

Report selected counts, three-page results, rerun idempotency, failures, generated paths, and commit IDs. Do not run an unrestricted Metronome collection and do not begin ingest until the user explicitly approves the next action.
