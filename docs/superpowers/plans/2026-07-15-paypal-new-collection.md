# PayPal New Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone, inventory-first `fetch_paypal_new.py` collector that snapshots every PayPal catalog, seals a deterministic Markdown queue, collects immutable path-preserving raw pages, and records complete retryable run history without starting ingest.

**Architecture:** A PayPal-specific discovery module parses and consolidates the nested catalog hierarchy. A sealing module writes immutable discovery evidence and a hash-bound inventory before the collection module may fetch page bodies. The CLI orchestrates discovery, collection, retry, and status while reusing shared HTTP, versioning, and JSONL primitives.

**Tech Stack:** Python 3.9 standard library (`argparse`, `concurrent.futures`, `dataclasses`, `hashlib`, `json`, `pathlib`, `urllib`, `xml.etree.ElementTree`), `unittest`, existing collection helpers

## Global Constraints

- Remain compatible with Python 3.9; do not use `tomllib`, structural pattern matching, or `X | None` type syntax.
- Keep `raw/` immutable: validate in staging, never overwrite an accepted file, and use `-r2`, `-r3` for distinct same-day versions.
- Treat `llms.txt` catalogs as the selected download authority; use `sitemap.xml` only for coverage auditing.
- Extract only the first Markdown link from each catalog bullet.
- Preserve the full canonical page hierarchy beneath `raw/paypal-new/`.
- Refuse collection unless the inventory and discovery snapshot are complete, stable, sealed, and hash-valid.
- Keep collection batch-oriented but never start or perform wiki ingest.
- Do not change `AGENTS.md`; keep `CLAUDE.md` as the workflow router and source of truth.
- Do not refactor other provider collectors in this implementation.
- Preserve the unrelated untracked `CLAUDE copy.md` file.

---

## File Structure

| File | Responsibility |
| --- | --- |
| `scripts/collection_http.py` | Provider-independent text fetching, retry policy, response metadata, and attempt facts. |
| `scripts/collection_versions.py` | Existing content comparison plus atomic immutable text promotion. |
| `scripts/collection_reporting.py` | Existing reporting plus append-only JSONL and exact terminal reconciliation. |
| `scripts/paypal_new_discovery.py` | PayPal URL identity, first-link parsing, duplicate consolidation, and sitemap normalization. |
| `scripts/paypal_new_inventory.py` | Recursive traversal, stability checks, snapshots, inventory sealing, and manifest verification. |
| `scripts/paypal_new_collection.py` | Markdown validation, page collection, retry selection, version promotion, and aggregate status. |
| `scripts/fetch_paypal_new.py` | Standalone `discover`, `collect`, `retry`, and `status` CLI. |
| `tests/test_collection_http.py` | HTTP metadata and retry tests. |
| `tests/test_paypal_new_discovery.py` | PayPal parsing, normalization, deduplication, and sitemap tests. |
| `tests/test_paypal_new_inventory.py` | Traversal, stability, sealing, and tamper tests. |
| `tests/test_paypal_new_collection.py` | Validation, versioning, terminal states, retry, and status tests. |
| `tests/test_fetch_paypal_new.py` | CLI routing and no-ingest boundary tests. |
| `tests/fixtures/paypal_new/*` | Deterministic root, child, sitemap, Markdown, and invalid-response fixtures. |
| `rules/psp/paypal-new.md` | Provider-specific collection contract. |
| `rules/psp/paypal.md` | Clarification that the existing rule covers PayPal.ai. |
| `rules/psp-collection.md` | Shared invariants and provider-specific routing. |
| `CLAUDE.md` | Directory tree and Workflow Index routing. |

---

### Task 1: Shared immutable ledger primitives

**Files:**
- Modify: `scripts/collection_versions.py`
- Modify: `scripts/collection_reporting.py`
- Modify: `tests/test_collection_versions.py`
- Modify: `tests/test_collection_reporting.py`

**Interfaces:**
- Consumes: existing `source_body()`, `body_sha256()`, `latest_prior()`, and `next_target()`.
- Produces: `write_immutable_text(target: Path, content: str) -> None`, `append_jsonl(path: Path, event: Dict[str, object]) -> None`, `read_jsonl(path: Path) -> List[Dict[str, object]]`, and `validate_terminal_results(selected_urls, events, terminal_states) -> Counter`.

- [ ] **Step 1: Write the failing immutable-write test**

Add to `tests/test_collection_versions.py`:

```python
from collection_versions import write_immutable_text

def test_immutable_write_creates_and_never_overwrites(self):
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "nested" / "page.md"
        write_immutable_text(target, "first\n")
        self.assertEqual(target.read_text(encoding="utf-8"), "first\n")
        with self.assertRaises(FileExistsError):
            write_immutable_text(target, "second\n")
        self.assertEqual(target.read_text(encoding="utf-8"), "first\n")
        self.assertEqual(list(target.parent.glob(".page.md.*")), [])
```

- [ ] **Step 2: Write failing append-only and reconciliation tests**

Add to `tests/test_collection_reporting.py`:

```python
from collection_reporting import append_jsonl, read_jsonl, validate_terminal_results

def test_append_jsonl_preserves_prior_events(self):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "events.jsonl"
        append_jsonl(path, {"event": "attempt", "canonical_url": "a"})
        append_jsonl(path, {"event": "terminal", "canonical_url": "a", "state": "new"})
        self.assertEqual([item["event"] for item in read_jsonl(path)], ["attempt", "terminal"])

def test_exact_terminal_reconciliation(self):
    states = {"new", "unchanged", "http-failed"}
    events = [
        {"event": "terminal", "canonical_url": "a", "state": "new"},
        {"event": "terminal", "canonical_url": "b", "state": "http-failed"},
    ]
    counts = validate_terminal_results(["a", "b"], events, states)
    self.assertEqual(counts["new"], 1)
    with self.assertRaisesRegex(ValueError, "missing terminal result"):
        validate_terminal_results(["a", "b", "c"], events, states)
    with self.assertRaisesRegex(ValueError, "duplicate terminal result"):
        validate_terminal_results(["a"], [events[0], events[0]], states)
```

- [ ] **Step 3: Run the focused tests and verify red state**

Run:

```bash
python -m unittest tests.test_collection_versions tests.test_collection_reporting -v
```

Expected: import errors name the four missing functions.

- [ ] **Step 4: Implement atomic immutable writes**

Add to `scripts/collection_versions.py`:

```python
import os
import tempfile

def write_immutable_text(target: Path, content: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix="." + target.name + ".", dir=str(target.parent), text=True)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(str(temporary), str(target))
    finally:
        if temporary.exists():
            temporary.unlink()
```

- [ ] **Step 5: Implement append-only JSONL and exact reconciliation**

Add to `scripts/collection_reporting.py`:

```python
import os
from typing import Set

def append_jsonl(path: Path, event: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())

def read_jsonl(path: Path) -> List[Dict[str, object]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]

def validate_terminal_results(
    selected_urls: Iterable[str],
    events: List[Dict[str, object]],
    terminal_states: Set[str],
) -> Counter:
    selected = set(selected_urls)
    by_url: Dict[str, Dict[str, object]] = {}
    for event in events:
        if event.get("event") != "terminal":
            continue
        url = str(event.get("canonical_url"))
        if url in by_url:
            raise ValueError("duplicate terminal result: " + url)
        if url not in selected:
            raise ValueError("terminal result outside selection: " + url)
        if event.get("state") not in terminal_states:
            raise ValueError("invalid terminal state: " + str(event.get("state")))
        by_url[url] = event
    missing = sorted(selected - set(by_url))
    if missing:
        raise ValueError("missing terminal result: " + ", ".join(missing))
    return Counter(str(event["state"]) for event in by_url.values())
```

- [ ] **Step 6: Run shared helper tests**

Run: `python -m unittest tests.test_collection_versions tests.test_collection_reporting -v`

Expected: all existing and new tests pass.

- [ ] **Step 7: Commit the shared primitives**

```bash
git add scripts/collection_versions.py scripts/collection_reporting.py \
  tests/test_collection_versions.py tests/test_collection_reporting.py
git commit -m "feat: add immutable collection ledger primitives"
```

---

### Task 2: Shared HTTP fetch and retry contract

**Files:**
- Create: `scripts/collection_http.py`
- Create: `tests/test_collection_http.py`

**Interfaces:**
- Consumes: standard-library `urllib.request` and injected sleep/random functions.
- Produces: `TextResponse`, `FetchResult`, and `fetch_text()`.

- [ ] **Step 1: Write failing HTTP tests**

Create `tests/test_collection_http.py` with imports for `sys`, `unittest`, `urllib.error`, and `Path`; add the scripts directory to `sys.path`; import `fetch_text`; then place this `FakeResponse` and the three test methods inside `class HttpTests(unittest.TestCase)`:

```python
class FakeResponse:
    def __init__(self, body, headers=None):
        self.body = body
        self.status = 200
        self.headers = headers or {"Content-Type": "text/markdown", "ETag": "abc"}
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, traceback):
        return False
    def read(self):
        return self.body.encode("utf-8")
    def geturl(self):
        return "https://example.test/page.md"

class HttpTests(unittest.TestCase):
  def test_success_records_response_metadata(self):
    result = fetch_text(
        "https://example.test/page.md", "test-agent",
        opener=lambda request, timeout: FakeResponse("# Page\n"),
        sleep_fn=lambda seconds: None, random_fn=lambda: 0.0,
    )
    self.assertEqual(result.response.content_type, "text/markdown")
    self.assertEqual(result.response.etag, "abc")
    self.assertEqual(result.attempts[0]["status"], 200)

  def test_retry_after_precedes_backoff(self):
    calls, sleeps = [], []
    def opener(request, timeout):
        calls.append(request.full_url)
        if len(calls) == 1:
            raise urllib.error.HTTPError(request.full_url, 429, "limited", {"Retry-After": "7"}, None)
        return FakeResponse("# Recovered\n")
    result = fetch_text(
        "https://example.test/page.md", "test-agent", opener=opener,
        sleep_fn=sleeps.append, random_fn=lambda: 0.0,
    )
    self.assertEqual(len(result.attempts), 2)
    self.assertEqual(sleeps, [7.0])

  def test_non_retryable_404_returns_no_response(self):
    def opener(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 404, "missing", {}, None)
    result = fetch_text(
        "https://example.test/missing.md", "test-agent", opener=opener,
        sleep_fn=lambda seconds: None, random_fn=lambda: 0.0,
    )
    self.assertIsNone(result.response)
    self.assertEqual(result.attempts[-1]["status"], 404)
```

- [ ] **Step 2: Run the tests and verify red state**

Run: `python -m unittest tests.test_collection_http -v`

Expected: import error for missing `collection_http`.

- [ ] **Step 3: Implement immutable HTTP models and retry policy**

Create `scripts/collection_http.py` with:

```python
@dataclass(frozen=True)
class TextResponse:
    requested_url: str
    final_url: str
    status: int
    content_type: str
    etag: Optional[str]
    last_modified: Optional[str]
    body: str

@dataclass(frozen=True)
class FetchResult:
    response: Optional[TextResponse]
    attempts: Tuple[Dict[str, object], ...]
```

Implement this signature without external dependencies:

```python
def fetch_text(
    url: str,
    user_agent: str,
    max_attempts: int = 4,
    timeout: int = 30,
    sleep_fn: Callable[[float], None] = time.sleep,
    random_fn: Callable[[], float] = random.random,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> FetchResult:
```

Use retryable statuses `{408, 425, 429, 500, 501, 502, 503, 504}`. Record each attempt. Honor numeric `Retry-After`; otherwise sleep `min(30, 2 ** (attempt - 1)) + random_fn()`. Decode UTF-8 with replacement, strip content-type parameters, and retain final URL, ETag, and Last-Modified.

- [ ] **Step 4: Run HTTP tests**

Run: `python -m unittest tests.test_collection_http -v`

Expected: 3 tests pass.

- [ ] **Step 5: Commit the HTTP contract**

```bash
git add scripts/collection_http.py tests/test_collection_http.py
git commit -m "feat: add collection HTTP retry contract"
```

---

### Task 3: PayPal catalog parsing and canonical identity

**Files:**
- Create: `scripts/paypal_new_discovery.py`
- Create: `tests/test_paypal_new_discovery.py`
- Create: `tests/fixtures/paypal_new/root-llms.txt`
- Create: `tests/fixtures/paypal_new/payments-llms.txt`
- Create: `tests/fixtures/paypal_new/other-llms.txt`
- Create: `tests/fixtures/paypal_new/sitemap.xml`

**Interfaces:**
- Consumes: catalog text and catalog URLs.
- Produces: `PrimaryLink`, `PageRecord`, `parse_primary_links()`, `catalog_urls()`, `consolidate_pages()`, `parse_sitemap_pages()`, and `raw_identity_for()`.

- [ ] **Step 1: Add representative fixtures**

`root-llms.txt`:

```markdown
# PayPal Developer Documentation
- [Business — Payments](/payments/llms.txt): Payments docs (2 pages)
- [Other](/other/llms.txt): Other docs (2 pages)
```

`payments-llms.txt`:

```markdown
# Payments
- [Checkout Alpha](/checkout/alpha): See [descriptive link](/not-primary)
- [Checkout Alpha server section](/checkout/alpha#server)
```

`other-llms.txt`:

```markdown
# Other
- [API Reference](/api/reference)
- [External Example](https://github.com/paypal/example)
```

`sitemap.xml`:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://developer.paypal.com/checkout/alpha</loc></url>
  <url><loc>https://developer.paypal.com/sitemap-only</loc></url>
</urlset>
```

- [ ] **Step 2: Write failing parser tests**

Assert that:

```python
links = parse_primary_links(payments_text, "https://developer.paypal.com/payments/llms.txt")
self.assertEqual([item.resolved_url for item in links], [
    "https://developer.paypal.com/checkout/alpha",
    "https://developer.paypal.com/checkout/alpha#server",
])
self.assertEqual(catalog_urls(root_text, "https://developer.paypal.com/llms.txt"), [
    "https://developer.paypal.com/other/llms.txt",
    "https://developer.paypal.com/payments/llms.txt",
])
records, duplicates = consolidate_pages(links + parse_primary_links(other_text, "https://developer.paypal.com/other/llms.txt"))
by_url = {record.canonical_url: record for record in records}
self.assertEqual(by_url["https://developer.paypal.com/checkout/alpha"].fragments, ("server",))
self.assertEqual(by_url["https://github.com/paypal/example"].exclusion_reason, "external-host")
self.assertEqual(len(duplicates), 1)
self.assertEqual(parse_sitemap_pages(sitemap_text), (
    "https://developer.paypal.com/checkout/alpha",
    "https://developer.paypal.com/sitemap-only",
))
```

Add a separate test requiring `ValueError("unknown query")` for `/checkout/alpha?mode=unknown`.

- [ ] **Step 3: Run parser tests and verify red state**

Run: `python -m unittest tests.test_paypal_new_discovery -v`

Expected: import error for missing `paypal_new_discovery`.

- [ ] **Step 4: Implement parsing and identity**

Create exact immutable models:

```python
@dataclass(frozen=True)
class PrimaryLink:
    title: str
    raw_url: str
    resolved_url: str
    catalog_url: str

@dataclass(frozen=True)
class PageRecord:
    canonical_url: str
    markdown_url: str
    raw_identity: str
    discovered_from: Tuple[str, ...]
    catalog_titles: Tuple[str, ...]
    fragments: Tuple[str, ...]
    selection: str
    exclusion_reason: Optional[str]
```

Use `re.compile(r"^\s*-\s+\[([^\]]+)\]\(([^)\s]+)\)", re.MULTILINE)` so only the first link on a bullet is selected. Resolve with `urljoin`; lowercase scheme/host; collapse path separators; remove trailing slash, `.md`, and fragment from identity; preserve fragments as metadata. Remove only `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, and `utm_content`; reject remaining query keys. Encode raw path segments with `quote(unquote(segment), safe="-._~")`.

Return deterministically sorted values from:

```python
def parse_primary_links(text: str, catalog_url: str) -> List[PrimaryLink]
def catalog_urls(text: str, catalog_url: str) -> List[str]
def raw_identity_for(canonical_url: str) -> str
def consolidate_pages(links: Iterable[PrimaryLink]) -> Tuple[Tuple[PageRecord, ...], Tuple[Dict[str, object], ...]]
def parse_sitemap_pages(text: str) -> Tuple[str, ...]
```

Merge titles, catalogs, and fragments by canonical URL. Select only HTTPS `developer.paypal.com`; retain other primary links as excluded. Raise if two selected canonical URLs map to one raw identity.

- [ ] **Step 5: Run parser tests**

Run: `python -m unittest tests.test_paypal_new_discovery -v`

Expected: all parser tests pass.

- [ ] **Step 6: Commit parsing**

```bash
git add scripts/paypal_new_discovery.py tests/test_paypal_new_discovery.py \
  tests/fixtures/paypal_new
git commit -m "feat: parse paypal new catalog hierarchy"
```

---

### Task 4: Recursive discovery and stability verification

**Files:**
- Create: `scripts/paypal_new_inventory.py`
- Create: `tests/test_paypal_new_inventory.py`

**Interfaces:**
- Consumes: `FetchResult` and Task 3 parsing functions.
- Produces: `CatalogSnapshot`, `DiscoveryBundle`, `DiscoveryError`, and `discover_corpus()`; `DiscoveryError` retains immutable attempt events for failure diagnostics.

- [ ] **Step 1: Write failing traversal tests**

Use a fake fetcher returning two identical results for every catalog because each is fetched once for discovery and once for stability. Assert:

```python
bundle = discover_corpus(fetcher)
self.assertEqual([item.url for item in bundle.catalogs], [
    "https://developer.paypal.com/llms.txt",
    "https://developer.paypal.com/other/llms.txt",
    "https://developer.paypal.com/payments/llms.txt",
])
self.assertEqual(len([item for item in bundle.pages if item.selection == "selected"]), 2)
self.assertEqual(bundle.sitemap_only, ("https://developer.paypal.com/sitemap-only",))
self.assertEqual(bundle.catalog_only, ("https://developer.paypal.com/api/reference",))
self.assertTrue(bundle.stable)
```

Add one test where a required child returns a 404 result and raises `DiscoveryError("required catalog failed")`. Add one where the stability fetch body differs and raises `DiscoveryError("changed during discovery")`.

- [ ] **Step 2: Run traversal tests and verify red state**

Run: `python -m unittest tests.test_paypal_new_inventory -v`

Expected: import error for missing `paypal_new_inventory`.

- [ ] **Step 3: Implement recursive discovery**

Create:

```python
@dataclass(frozen=True)
class CatalogSnapshot:
    url: str
    body: str
    content_sha256: str
    content_type: str
    etag: Optional[str]
    last_modified: Optional[str]
    attempts: Tuple[Dict[str, object], ...]

@dataclass(frozen=True)
class DiscoveryBundle:
    catalogs: Tuple[CatalogSnapshot, ...]
    pages: Tuple[PageRecord, ...]
    duplicates: Tuple[Dict[str, object], ...]
    sitemap_body: str
    sitemap_response: TextResponse
    sitemap_attempts: Tuple[Dict[str, object], ...]
    sitemap_only: Tuple[str, ...]
    catalog_only: Tuple[str, ...]
    advertised_counts: Dict[str, int]
    events: Tuple[Dict[str, object], ...]
    stable: bool

class DiscoveryError(RuntimeError):
    def __init__(self, message: str, events: Iterable[Dict[str, object]]):
        super().__init__(message)
        self.events = tuple(events)
```

Implement:

```python
def discover_corpus(
    fetcher: Callable[[str], FetchResult],
    root_url: str = "https://developer.paypal.com/llms.txt",
    sitemap_url: str = "https://developer.paypal.com/sitemap.xml",
) -> DiscoveryBundle:
```

Use a sorted, cycle-safe queue beginning with `root_url`. Require every catalog response to be status 200, non-empty plain text or Markdown, not HTML, and parsable into primary bullet links. Parse every successful catalog for nested same-host `llms.txt` links and primary page links. Abort on a failed required catalog or malformed catalog, retaining prior attempts in `DiscoveryError.events`. Fetch the sitemap, require status 200, and reject malformed XML. Re-fetch catalogs in sorted order and compare body hashes. Record advertised root counts with `r"\((\d+)\s+pages?\)"`; count mismatch is an event, not a blocker. Derive sitemap-only and catalog-only from selected page identities without adding sitemap pages to `pages`.

- [ ] **Step 4: Run traversal tests**

Run: `python -m unittest tests.test_paypal_new_inventory -v`

Expected: traversal, missing-child, and changed-catalog tests pass.

- [ ] **Step 5: Commit recursive discovery**

```bash
git add scripts/paypal_new_inventory.py tests/test_paypal_new_inventory.py
git commit -m "feat: traverse paypal new discovery catalogs"
```

---

### Task 5: Seal and verify immutable inventories

**Files:**
- Modify: `scripts/paypal_new_inventory.py`
- Modify: `tests/test_paypal_new_inventory.py`

**Interfaces:**
- Consumes: `DiscoveryBundle`, `DiscoveryError`, and `write_immutable_text()`.
- Produces: `seal_discovery()`, `write_discovery_failure()`, and `load_verified_inventory()`.

- [ ] **Step 1: Write failing sealing tests**

Seal a fixture bundle into a temporary workspace and assert:

```python
pages_path = seal_discovery(bundle, workspace, "2026-07-15T120000Z-test", "2026-07-15T12:00:00Z")
raw_snapshot = workspace / "raw/paypal-new/_discovery/2026-07-15T120000Z-test"
self.assertTrue((raw_snapshot / "root-llms.txt").exists())
self.assertTrue((raw_snapshot / "catalogs/payments/llms.txt").exists())
self.assertTrue((raw_snapshot / "sitemap.xml").exists())
manifest, pages = load_verified_inventory(pages_path, workspace)
self.assertEqual(manifest["status"], "sealed")
self.assertEqual(len([page for page in pages if page["selection"] == "selected"]), 2)
```

Add a tamper test that appends `{}` to `pages.jsonl` and expects `ValueError("inventory hash mismatch")`. Add a second-seal test expecting `FileExistsError` for an existing discovery ID.

Add a failure-diagnostics test that passes `DiscoveryError("required catalog failed", events)` to `write_discovery_failure()` and asserts a non-sealed `.staging-<discovery-id>/failure.json` plus `discovery-events.jsonl` are preserved under `tracking/collections/paypal-new/inventories/`. Assert `load_verified_inventory()` rejects that directory.

- [ ] **Step 2: Run sealing tests and verify red state**

Run: `python -m unittest tests.test_paypal_new_inventory -v`

Expected: failures name missing sealing interfaces.

- [ ] **Step 3: Implement deterministic serialization**

Add:

```python
def _json_text(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"

def _jsonl_text(values: Iterable[Dict[str, object]]) -> str:
    return "".join(json.dumps(value, sort_keys=True) + "\n" for value in values)

def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def _artifact_fact(text: str, records: int) -> Dict[str, object]:
    return {"sha256": _sha256_text(text), "bytes": len(text.encode("utf-8")), "records": records}
```

- [ ] **Step 4: Implement sealing and verification**

Use signatures:

```python
def seal_discovery(
    bundle: DiscoveryBundle,
    workspace_root: Path,
    discovery_id: str,
    retrieved_at: str,
) -> Path:

def load_verified_inventory(
    pages_path: Path,
    workspace_root: Path,
) -> Tuple[Dict[str, object], List[Dict[str, object]]]:
```

Also implement:

```python
def write_discovery_failure(
    workspace_root: Path,
    discovery_id: str,
    error: DiscoveryError,
) -> Path:
```

`seal_discovery()` writes both staging directories, then promotes each by rename. The raw snapshot stores root, path-preserving child catalogs, sitemap, and response-metadata manifest. The tracking inventory stores sorted `raw-md-links.txt`, `pages.jsonl`, `duplicates.jsonl`, `excluded-pages.jsonl`, `sitemap-only.txt`, `catalog-only.txt`, `coverage-summary.json`, `discovery-events.jsonl`, and a sealed hash manifest. The tracking manifest records the raw manifest relative path and SHA-256. Existing final directories cause `FileExistsError`.

`write_discovery_failure()` preserves only diagnostic JSON/JSONL beneath `.staging-<discovery-id>` and never writes a sealed manifest or accepted raw snapshot. `load_verified_inventory()` requires sealed status, verifies `pages.jsonl`, verifies the raw manifest is inside the workspace and matches its hash, and returns parsed page records. Syntax-valid unsealed files are rejected.

- [ ] **Step 5: Run all inventory tests**

Run: `python -m unittest tests.test_paypal_new_inventory -v`

Expected: all traversal and sealing tests pass.

- [ ] **Step 6: Commit sealing**

```bash
git add scripts/paypal_new_inventory.py tests/test_paypal_new_inventory.py
git commit -m "feat: seal paypal new collection inventories"
```

---

### Task 6: Validate, collect, retry, and report Markdown pages

**Files:**
- Create: `scripts/paypal_new_collection.py`
- Create: `tests/test_paypal_new_collection.py`
- Create: `tests/fixtures/paypal_new/page.md`
- Create: `tests/fixtures/paypal_new/html-404.html`

**Interfaces:**
- Consumes: sealed inventories, `FetchResult`, version helpers, and ledger helpers.
- Produces: `validate_markdown_response()`, `collect_inventory()`, `retry_run()`, `status_for_inventory()`, and `TERMINAL_STATES`.

- [ ] **Step 1: Add response fixtures**

`page.md`:

```markdown
# Checkout Alpha

This page describes the PayPal checkout integration and contains enough text for validation.
```

`html-404.html`:

```html
<!doctype html><html><body><h1>Page not found</h1></body></html>
```

- [ ] **Step 2: Write failing validation and collection tests**

Use the sealed fixture inventory and a fake fetcher. Assert:

```python
self.assertEqual(validate_markdown_response(html_response, alpha_canonical), "html-response")
run_dir = collect_inventory(
    workspace, pages_path, fetcher,
    collection_date="2026-07-15", run_id="run-1", workers=1,
)
summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
self.assertEqual(summary["selected"], 2)
self.assertEqual(sum(summary["terminal_counts"].values()), 2)
self.assertTrue((workspace / "raw/paypal-new/checkout/alpha-2026-07-15.md").exists())
self.assertFalse((workspace / "wiki").exists())
```

Run collection again with identical bodies and assert `unchanged`. Change Alpha on the same date, run again, and assert `alpha-2026-07-15-r2.md` exists while the first version is unchanged. Add a selection test with records from three catalogs and assert `select_smoke_sample(records, 3)` returns one page from each catalog in deterministic order.

- [ ] **Step 3: Run tests and verify red state**

Run: `python -m unittest tests.test_paypal_new_collection -v`

Expected: import error for missing `paypal_new_collection`.

- [ ] **Step 4: Implement validation and raw rendering**

Define:

```python
TERMINAL_STATES = {
    "new", "changed", "unchanged", "http-failed",
    "network-failed", "invalid-content", "path-conflict",
}

def make_raw(markdown_url: str, body: str, collection_date: str) -> str:
    return (
        "<!-- Source URL: " + markdown_url + " -->\n"
        "<!-- Fetched: " + collection_date + " -->\n"
        "<!-- Discovery: paypal-new sealed inventory -->\n\n"
        + body.rstrip() + "\n"
    )
```

`validate_markdown_response()` returns `None` or one of `unexpected-status`, `external-redirect`, `unexpected-redirect`, `html-response`, `empty-response`, `too-short`, `access-denied`, or `unexpected-catalog`. Allow `text/plain`, `text/markdown`, `text/x-markdown`, and `application/markdown`. Require the final `.md` URL to normalize to the expected canonical identity.

Implement `select_smoke_sample(records, limit)` by grouping records on their first sorted `discovered_from` catalog and taking one page per group in round-robin order until the limit is reached. Normal full collection remains canonical-URL sorted.

- [ ] **Step 5: Implement bounded collection and terminal reconciliation**

Use:

```python
def collect_inventory(
    workspace_root: Path,
    pages_path: Path,
    fetcher: Callable[[str], FetchResult],
    collection_date: str,
    run_id: str,
    workers: int = 6,
    limit: Optional[int] = None,
    selected_urls: Optional[Set[str]] = None,
    retry_of: Optional[str] = None,
) -> Path:
```

Verify the inventory before creating an immutable run manifest with the inventory hash and exact selection. Sort full runs by canonical URL; when `limit` is supplied, use `select_smoke_sample()` so the smoke run spans catalogs. Apply any explicit retry selection after inventory verification and use `ThreadPoolExecutor(max_workers=workers)` with `executor.map()`.

For each page, append every network attempt, map absent responses to `http-failed` or `network-failed`, map validation rejection to `invalid-content`, and compare valid bodies with `latest_prior()`. Record unchanged without writing. Use `next_target()` and `write_immutable_text()` for new/changed; map `FileExistsError` to `path-conflict`. Append exactly one terminal record and record accepted files separately. Call `validate_terminal_results()` and write an immutable terminal summary whose status is `complete` or `complete-with-failures`.

- [ ] **Step 6: Run collection tests**

Run: `python -m unittest tests.test_paypal_new_collection -v`

Expected: validation, new, unchanged, invalid-content, and revision tests pass.

- [ ] **Step 7: Add failing retry and aggregate-status tests**

Assert that retry creates a new run with `retry_of`, selects prior `http-failed`/`network-failed` URLs plus selected URLs lacking a terminal result, excludes successes, and selects `invalid-content` only with `include_invalid_content=True`. Assert aggregate unresolved becomes zero after a retry succeeds.

- [ ] **Step 8: Implement retry and status interfaces**

Use:

```python
def retry_run(
    workspace_root: Path,
    prior_run_dir: Path,
    fetcher: Callable[[str], FetchResult],
    collection_date: str,
    run_id: str,
    workers: int = 6,
    include_invalid_content: bool = False,
) -> Path:

def status_for_inventory(workspace_root: Path, pages_path: Path) -> Dict[str, object]:
```

Retry verifies the prior immutable manifest and inventory, derives eligible failures and missing terminal URLs, then invokes the internal runner with explicit selection. Status scans completed runs with the same inventory hash, applies terminal results in run creation order, and returns inventory hash, selected, resolved, unresolved, sorted state counts, and sorted unresolved URLs.

- [ ] **Step 9: Run collection regressions**

Run:

```bash
python -m unittest tests.test_paypal_new_collection \
  tests.test_collection_versions tests.test_collection_reporting -v
```

Expected: all tests pass.

- [ ] **Step 10: Commit collection**

```bash
git add scripts/paypal_new_collection.py tests/test_paypal_new_collection.py \
  tests/fixtures/paypal_new/page.md tests/fixtures/paypal_new/html-404.html
git commit -m "feat: collect immutable paypal new pages"
```

---

### Task 7: Standalone PayPal-new CLI

**Files:**
- Create: `scripts/fetch_paypal_new.py`
- Create: `tests/test_fetch_paypal_new.py`

**Interfaces:**
- Consumes: discovery, sealing, failure-diagnostic, collection, retry, status, and HTTP interfaces.
- Produces: `main(argv: Optional[Sequence[str]] = None) -> int`.

- [ ] **Step 1: Write failing CLI routing tests**

Patch orchestration functions and assert `discover` prints the produced `pages.jsonl`, `collect` requires `--inventory` and passes `--workers`, `retry` resolves the named run, and the module has no ingest function. Tests must make no network request and write no wiki file.

- [ ] **Step 2: Run CLI tests and verify red state**

Run: `python -m unittest tests.test_fetch_paypal_new -v`

Expected: import error for missing `fetch_paypal_new`.

- [ ] **Step 3: Implement CLI parsing and routing**

Use:

```python
ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "wiki-fetch-paypal-new/1.0 (+payments knowledge base; respectful crawl)"
ROOT_CATALOG_URL = "https://developer.paypal.com/llms.txt"
SITEMAP_URL = "https://developer.paypal.com/sitemap.xml"

def main(argv: Optional[Sequence[str]] = None) -> int:
```

Required subcommands:

```text
discover
collect --inventory PATH [--workers 6] [--limit N]
retry --run RUN_ID [--workers 6] [--include-invalid-content]
status --inventory PATH
```

Generate UTC IDs with microseconds. Bind `fetch_text` with the user agent. Resolve relative paths under `ROOT` and reject paths escaping the workspace. If `discover_corpus()` raises `DiscoveryError`, call `write_discovery_failure()` with the same discovery ID, print the diagnostic directory, and return nonzero without sealing an inventory. Print successful artifact paths or JSON status. Return nonzero with a concise message for manifest or collection errors. Every successful collection output ends with `Collection stops here. Ingest requires a separate user action following rules/ingest.md.`

- [ ] **Step 4: Run CLI and collector tests**

Run:

```bash
python -m unittest tests.test_collection_http tests.test_collection_versions \
  tests.test_collection_reporting tests.test_paypal_new_discovery \
  tests.test_paypal_new_inventory tests.test_paypal_new_collection \
  tests.test_fetch_paypal_new -v
```

Expected: all tests pass.

- [ ] **Step 5: Verify command help**

Run:

```bash
python scripts/fetch_paypal_new.py --help
python scripts/fetch_paypal_new.py collect --help
```

Expected: four subcommands are listed; collect requires `--inventory` and documents workers and limit.

- [ ] **Step 6: Commit CLI**

```bash
git add scripts/fetch_paypal_new.py tests/test_fetch_paypal_new.py
git commit -m "feat: add standalone paypal new collector CLI"
```

---

### Task 8: Rules, live smoke gate, and final verification

**Files:**
- Create: `rules/psp/paypal-new.md`
- Modify: `rules/psp/paypal.md`
- Modify: `rules/psp-collection.md`
- Modify: `CLAUDE.md`

**Interfaces:**
- Consumes: final CLI and approved design.
- Produces: accurate workflow routing, provider commands, smoke gate, and verified collection-only behavior.

- [ ] **Step 1: Update shared PSP workflow wording**

Document that simple providers may keep using `fetch_psp.py`, while complex providers use the standalone script named in their provider rule. Shared invariants remain frozen/recorded inventory, response validation, immutable raw versions, terminal reconciliation, and an explicit stop before ingest. Provider rules own sources, transformations, recovery, raw mapping, and commands.

- [ ] **Step 2: Add `rules/psp/paypal-new.md`**

Include these sections:

```markdown
# Provider rule: PayPal-new developer documentation

## Identity and boundary
## Discovery authority
## Frozen inventory
## Canonical URL and raw path
## Commands
## Validation and retry
## Sitemap audit
## Smoke-test gate
## Collection to ingest boundary
## Comparison readiness
```

Document root catalog, sitemap, recursive same-host traversal, first-link parsing, `raw/paypal-new/`, tracking layout, four commands, `--limit 10` smoke gate, terminal reconciliation, sitemap-only exclusion, and no batch ingest.

- [ ] **Step 3: Clarify PayPal.ai and update root routing**

Add to `rules/psp/paypal.md`: `This rule covers docs.paypal.ai only; upgraded developer.paypal.com documentation follows rules/psp/paypal-new.md.`

Update `CLAUDE.md` to list the standalone script/rule, describe `fetch_psp.py` as the simple-provider fetcher, and route PayPal-new through both generic and provider rules. Do not edit `AGENTS.md`; the approved design document already has status `Approved`.

- [ ] **Step 4: Run documentation validation**

Run:

```bash
python scripts/validate_wiki.py
git diff --check
```

Expected: validation exits 0 and whitespace check emits no output.

- [ ] **Step 5: Run the full automated suite**

Run: `python -m unittest discover -s tests -v`

Expected: zero failures and zero errors.

- [ ] **Step 6: Run live discovery**

Run: `python scripts/fetch_paypal_new.py discover`

Expected: exit 0, one sealed `pages.jsonl`, root plus every dynamically reached catalog and sitemap in the raw snapshot, matching hashes, no unstable catalog, and no documentation page or wiki write. Record the printed discovery ID.

- [ ] **Step 7: Run a ten-page collection smoke test**

Run:

```bash
python scripts/fetch_paypal_new.py collect \
  --inventory tracking/collections/paypal-new/inventories/<discovery-id>/pages.jsonl \
  --limit 10 --workers 2
```

Replace `<discovery-id>` with Step 6's printed ID. Expect exactly 10 selected terminal results, path-preserving accepted raw files, invalid responses only in tracking, and the explicit ingest stop message.

- [ ] **Step 8: Re-run the same smoke selection**

Run the Step 7 command again. Expect accepted identical pages to be `unchanged`, no overwrite, and a revision suffix only if upstream content changed during the same day.

- [ ] **Step 9: Inspect scope and commit rules**

Run:

```bash
git status --short
git diff -- CLAUDE.md rules/psp-collection.md rules/psp/paypal.md \
  rules/psp/paypal-new.md
```

Confirm no change to `AGENTS.md`, other provider collectors, wiki ingest pages, or `CLAUDE copy.md`. Then:

```bash
git add CLAUDE.md rules/psp-collection.md rules/psp/paypal.md \
  rules/psp/paypal-new.md
git commit -m "docs: add paypal new collection workflow"
```

- [ ] **Step 10: Final verification checkpoint**

Run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_wiki.py
git diff --check
git status --short
```

Expected: tests and validation exit 0, whitespace check emits no output, and status contains only intentional uncommitted raw/tracking smoke artifacts plus pre-existing `CLAUDE copy.md`.

---

## Execution Result Boundary

Completing this plan produces a verified standalone collector, a sealed full PayPal-new raw-link inventory, and a ten-page collection smoke run. It does not authorize the full multi-thousand-page download, wiki ingest, old-versus-new semantic comparison, or migration of any other provider collector. Those actions begin only after the user reviews the smoke results and explicitly requests the next phase.
