# Metronome Minimum Parallel Ingest Dry-Run Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and execute the minimum five-page Metronome parallel candidate-generation and serial Sol-review dry-run, then stop before any canonical wiki promotion.

**Architecture:** A small Python state machine owns trusted campaign files and emits platform-neutral JSON work orders; the host agent, not Python, spawns Terra workers and returns their JSON results. The coordinator persists immutable attempt evidence, maintains a generated monitor, and emits at most one Sol review order. Canonical promotion is a separate future plan after the user approves the dry-run.

**Tech Stack:** Python 3.9 standard library, `unittest`, JSON/JSONL, Markdown, SHA-256, native Codex Terra sub-agents during the live dry-run.

## Global Constraints

- Read and follow `CLAUDE.md`, `rules/ingest.md`, and the approved design at `docs/superpowers/specs/2026-07-27-metronome-minimum-ingest-pilot-design.md`.
- English canonical Metronome documentation only.
- Process exactly one complete raw page per Terra worker.
- Terra and Sol never write repository files; only the primary coordinator writes campaign evidence.
- Candidate worker concurrency is exactly `5`; Sol review concurrency is exactly `1`.
- Each candidate contains exactly `3–5` verbatim grounding quotes and an exact Raw Sources link.
- Raw files are immutable and their SHA-256 values must match before and after the dry-run.
- `jobs.json` is current-state authority; `events.jsonl` is append-only audit history, not replay authority.
- A job has at most `3` total attempts. Retry goes to the queue tail.
- Restart converts `running` and `reviewing` to `failed`.
- This plan creates no canonical source, concept, company, index, log, comparison, or promotion commit.
- Do not modify or import `scripts/metronome_ingest_pilot.py`, `scripts/run_metronome_model_worker.py`, or their historical schemas and run directories.
- Do not copy or cherry-pick code from `codex/metronome-simplified-ingest-orchestration`.
- Do not add automatic crash recovery, operation receipts, exact replay, hostile-journal checks, generation binding, automatic rollback, per-worker Git worktrees, background threads, or a model-backend abstraction.
- Each implementation task gets one normal review. Fix only concrete contract failures; do not expand the design in response to hypothetical attacks.
- Allow at most one targeted fix round per task. If the follow-up review still finds a load-bearing defect, stop for user review instead of starting another repair loop.
- Do not create production or test files beyond the file structure below. If production code exceeds 1,000 nonblank lines in total or one module exceeds 350 nonblank lines, stop for design review; do not compress code merely to fit the guardrail.
- Gate 3 canonical promotion is intentionally excluded. It requires a separate user-approved plan after this dry-run.

---

## File Structure

```text
scripts/
├── manage_ingest_pilot.py          # six small CLI operations for dry-run state
└── ingest_pilot/
    ├── __init__.py                 # public dry-run interfaces
    ├── state.py                    # trusted state files, events, attempts, monitor
    ├── scheduler.py                # rolling worker slots and one review order
    ├── validator.py                # worker result, quote, raw-link, and hash checks
    └── coordinator.py              # state transitions and JSON action composition
tests/
├── test_ingest_pilot_state.py
├── test_ingest_pilot_scheduler.py
├── test_ingest_pilot_validator.py
├── test_ingest_pilot_coordinator.py
└── test_ingest_pilot_end_to_end.py
tracking/ingest/metronome/metronome-minimum-pilot-01/
├── manifest.json                   # five exact immutable inputs
├── campaign.json                   # created by init
├── jobs.json                       # created by init
├── events.jsonl                    # created by init
├── monitor.md                      # generated view
└── attempts/                       # created only when work orders are issued
```

### Shared interfaces

```python
class PilotError(Exception):
    pass

def init_campaign(root: Path, manifest_path: Path) -> dict:
    """Create one campaign and return its monitor payload."""

def run_once(
    root: Path,
    campaign_id: str,
    worker_result_path: Optional[Path] = None,
    review_result_path: Optional[Path] = None,
    available_worker_slots: Optional[int] = None,
) -> dict:
    """Apply at most one supplied result, then emit worker/review actions."""

def status(root: Path, campaign_id: str) -> dict:
    """Recover interrupted dry-run states, regenerate monitor, return state."""

def retry_job(root: Path, campaign_id: str, job_id: str) -> dict:
    """Queue one failed pre-promotion job at the tail."""

def reject_job(root: Path, campaign_id: str, job_id: str, reason: str) -> dict:
    """Mark one failed job terminal."""
```

`run_once()` does not call a model. It emits JSON work orders. The host agent supplies its currently available native-worker slots, invokes that many Terra workers, writes each returned JSON to a unique temporary path outside the repository, and passes that path back through `--worker-result`. The configured campaign maximum remains five, while a host with fewer slots fills only its current capacity and refills as workers finish. The primary Sol agent handles review orders serially and passes one review JSON path through `--review-result`.

---

### Task 1: Trusted State Store, Attempts, Restart Rules, and Monitor

**Files:**
- Create: `scripts/ingest_pilot/__init__.py`
- Create: `scripts/ingest_pilot/state.py`
- Create: `tests/test_ingest_pilot_state.py`

**Interfaces:**
- Consumes: one exact manifest under `tracking/ingest/metronome/<campaign-id>/manifest.json`.
- Produces: `PilotError`, `campaign_paths()`, `load_campaign()`, `load_jobs()`, `save_jobs()`, `append_event()`, `create_attempt()`, `write_attempt_file()`, `recover_interrupted()`, and `render_monitor()`.

- [ ] **Step 1: Write the state initialization and atomic-update tests**

```python
class PilotStateTests(unittest.TestCase):
    def test_initialize_creates_only_minimum_campaign_files(self):
        initialize_state(self.root, self.manifest)
        campaign_dir = self.root / "tracking/ingest/metronome/metronome-minimum-pilot-01"
        self.assertEqual(
            sorted(path.name for path in campaign_dir.iterdir()),
            ["campaign.json", "events.jsonl", "jobs.json", "manifest.json", "monitor.md"],
        )
        jobs = load_jobs(self.root, "metronome-minimum-pilot-01")
        self.assertEqual([job["state"] for job in jobs], ["queued"] * 5)
        self.assertEqual([job["queue_position"] for job in jobs], [1, 2, 3, 4, 5])

    def test_save_jobs_replaces_projection_without_rewriting_events(self):
        initialize_state(self.root, self.manifest)
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0]["state"] = "running"
        before_events = self.events.read_bytes()
        save_jobs(self.root, self.campaign_id, jobs)
        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "running")
        self.assertEqual(self.events.read_bytes(), before_events)
```

- [ ] **Step 2: Run the state test and confirm the missing module failure**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest tests.test_ingest_pilot_state -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.ingest_pilot'`.

- [ ] **Step 3: Implement the fixed state schemas and atomic write**

Use schema version `1`.

`campaign.json`:

```json
{
  "schema_version": 1,
  "campaign_id": "metronome-minimum-pilot-01",
  "provider": "metronome",
  "state": "active",
  "worker_concurrency": 5,
  "max_attempts": 3,
  "review_concurrency": 1,
  "mode": "dry_run"
}
```

Each job in `jobs.json` contains only:

```json
{
  "job_id": "security-principles",
  "raw_path": "raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md",
  "raw_sha256": "<sha256>",
  "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-security-principles.md",
  "state": "queued",
  "attempt": 0,
  "queue_position": 1,
  "last_event": "initialized",
  "failure_reason": null
}
```

Implement `save_jobs()` with one sibling `.tmp`, `flush()`, `os.fsync()`, and `os.replace()`. Reject a pre-existing `.tmp` with a plain `PilotError`; do not reconcile it.

- [ ] **Step 4: Write attempt-retention and restart tests**

```python
def test_attempt_files_are_additive_and_never_overwritten(self):
    attempt = create_attempt(self.root, self.campaign_id, self.jobs[0], 1)
    write_attempt_file(attempt, "input.json", b"{}\n")
    with self.assertRaisesRegex(PilotError, "already exists"):
        write_attempt_file(attempt, "input.json", b'{"changed":true}\n')

def test_restart_fails_running_and_reviewing_jobs(self):
    jobs = self.initialized_jobs()
    jobs[0]["state"] = "running"
    jobs[1]["state"] = "reviewing"
    jobs[2]["state"] = "candidate_ready"
    save_jobs(self.root, self.campaign_id, jobs)
    recovered = recover_interrupted(self.root, self.campaign_id)
    self.assertEqual([recovered[0]["state"], recovered[1]["state"]], ["failed", "failed"])
    self.assertEqual(recovered[2]["state"], "candidate_ready")
    self.assertEqual(recovered[0]["failure_reason"], "interrupted")
```

`recover_interrupted()` changes only `running` and `reviewing`. A future promotion plan will add the `promoting` pause rule.

- [ ] **Step 5: Implement append-only events and generated monitor**

`append_event()` writes one compact JSON object plus `\n` using append mode and reports an error without changing `jobs.json`.

`render_monitor()` produces:

```markdown
# Metronome Minimum Pilot 01

- Campaign state: `active`
- Worker concurrency: `5`
- Queued: 5
- Running: 0
- Candidate ready: 0
- Reviewing: 0
- Approved: 0
- Failed: 0
- Rejected: 0

| Job | Attempt | State | Raw | Source target | Last event | Failure |
```

The monitor is regenerated after every public state operation.

- [ ] **Step 6: Run focused tests**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest tests.test_ingest_pilot_state -v
git diff --check
```

Expected: all state tests PASS; `git diff --check` prints nothing.

- [ ] **Step 7: Commit**

```bash
git add scripts/ingest_pilot tests/test_ingest_pilot_state.py
git commit -m "feat: add minimum ingest pilot state"
```

---

### Task 2: Worker Validation and Rolling Scheduler

**Files:**
- Create: `scripts/ingest_pilot/validator.py`
- Create: `scripts/ingest_pilot/scheduler.py`
- Modify: `scripts/ingest_pilot/__init__.py`
- Create: `tests/test_ingest_pilot_validator.py`
- Create: `tests/test_ingest_pilot_scheduler.py`

**Interfaces:**
- Consumes: trusted manifest job, complete raw bytes, and one worker-result JSON object.
- Produces: `ValidationError`, `sha256_file()`, `validate_worker_result()`, `worker_orders()`, and `review_order()`.

```python
def validate_worker_result(root: Path, job: dict, result: dict) -> dict: ...

def worker_orders(
    jobs: list[dict],
    worker_concurrency: int,
    max_attempts: int,
    available_worker_slots: int,
) -> list[dict]: ...

def review_order(jobs: list[dict]) -> Optional[dict]: ...
```

- [ ] **Step 1: Write exact worker-result validation tests**

```python
def test_valid_worker_result_requires_quotes_hash_and_raw_link(self):
    result = valid_result(
        raw_path=self.job["raw_path"],
        raw_sha256=sha256_file(self.raw),
        quotes=[
            {"text": "Least privilege", "location": "Metronome's security principles"},
            {"text": "Separation of duties", "location": "Metronome's security principles"},
            {"text": "Secure by default", "location": "Metronome's security principles"},
        ],
        source_page=(
            "---\n"
            "title: \"Metronome security principles\"\n"
            "type: source\n"
            "date_ingested: 2026-07-27\n"
            "original_format: webpage\n"
            "raw_files:\n"
            "  - \"metronome/guides/platform-configuration/security-principles-2026-07-13.md\"\n"
            "tags: [metronome, security]\n"
            "---\n\n"
            "## Raw Sources\n"
            "- [[security-principles-2026-07-13]] — verbatim documentation\n"
        ),
    )
    validated = validate_worker_result(self.root, self.job, result)
    self.assertEqual(validated["status"], "candidate_ready")
    self.assertEqual(len(validated["quotes"]), 3)
```

Add separate negative tests for:

- two or six quotes;
- a quote absent from the raw bytes;
- wrong `raw_path`;
- wrong `raw_sha256`;
- missing or wrong `raw_files:` entry;
- missing `## Raw Sources`;
- wrong raw wikilink;
- a missing suggestions key;
- any output key outside the fixed schema.

- [ ] **Step 2: Run validator tests and confirm failure**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest tests.test_ingest_pilot_validator -v
```

Expected: FAIL because `validator.py` does not exist.

- [ ] **Step 3: Implement the small validator**

The accepted worker-result keys are exactly:

```python
{
    "job_id",
    "attempt",
    "source_page",
    "quotes",
    "suggestions",
    "raw_path",
    "raw_sha256",
    "status",
}
```

The suggestions keys are exactly `company`, `concepts`, `index`, and `log`, each holding a JSON array.

Quote validation uses exact substring membership in the raw text. Do not add fuzzy quote repair or claim-level evidence.

- [ ] **Step 4: Write rolling scheduler tests**

```python
def test_worker_orders_fill_five_slots_then_refill_one(self):
    jobs = make_jobs(10)
    first = worker_orders(
        jobs,
        worker_concurrency=5,
        max_attempts=3,
        available_worker_slots=5,
    )
    self.assertEqual([order["job_id"] for order in first], [f"job-{n}" for n in range(1, 6)])
    for job in jobs[:5]:
        job["state"] = "running"
    jobs[0]["state"] = "candidate_ready"
    refill = worker_orders(
        jobs,
        worker_concurrency=5,
        max_attempts=3,
        available_worker_slots=1,
    )
    self.assertEqual([order["job_id"] for order in refill], ["job-6"])

def test_review_order_is_serial(self):
    jobs = make_jobs(3)
    jobs[0]["state"] = "candidate_ready"
    jobs[1]["state"] = "candidate_ready"
    self.assertEqual(review_order(jobs)["job_id"], "job-1")
    jobs[0]["state"] = "reviewing"
    self.assertIsNone(review_order(jobs))
```

Add tests proving failed/rejected jobs do not consume slots and queue order is ascending `queue_position`.

- [ ] **Step 5: Implement pure scheduler projections**

`worker_orders()` and `review_order()` return JSON-ready dictionaries and never mutate jobs. `available_worker_slots` is bounded to `0..worker_concurrency`; it represents host capacity, not a second campaign concurrency setting.

Each worker order contains:

```json
{
  "action": "spawn_worker",
  "job_id": "security-principles",
  "attempt": 1,
  "raw_path": "raw/metronome/...",
  "raw_sha256": "<sha256>",
  "source_target": "wiki/sources/metronome/..."
}
```

- [ ] **Step 6: Run focused tests and commit**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest \
  tests.test_ingest_pilot_validator \
  tests.test_ingest_pilot_scheduler -v
git diff --check
```

Expected: all validator and scheduler tests PASS.

```bash
git add scripts/ingest_pilot tests/test_ingest_pilot_validator.py tests/test_ingest_pilot_scheduler.py
git commit -m "feat: validate and schedule ingest candidates"
```

---

### Task 3: Coordinator Transitions and Thin JSON CLI

**Files:**
- Create: `scripts/ingest_pilot/coordinator.py`
- Create: `scripts/manage_ingest_pilot.py`
- Modify: `scripts/ingest_pilot/__init__.py`
- Create: `tests/test_ingest_pilot_coordinator.py`

**Interfaces:**
- Consumes: Task 1 state functions and Task 2 validator/scheduler projections.
- Produces: `init_campaign()`, `run_once()`, `status()`, `retry_job()`, `reject_job()`, and the five dry-run CLI commands `init`, `run`, `status`, `retry`, `reject`.

- [ ] **Step 1: Write a test for work-order publication**

```python
def test_run_emits_five_orders_and_persists_running_attempts(self):
    init_campaign(self.root, self.manifest)
    output = run_once(self.root, self.campaign_id)
    self.assertEqual(len(output["worker_orders"]), 5)
    jobs = load_jobs(self.root, self.campaign_id)
    self.assertEqual([job["state"] for job in jobs], ["running"] * 5)
    self.assertEqual([job["attempt"] for job in jobs], [1] * 5)
    for job in jobs:
        attempt = self.campaign_dir / "attempts" / job["job_id"] / "attempt-1"
        self.assertTrue(attempt.joinpath("input.json").is_file())
```

- [ ] **Step 2: Run and observe the missing coordinator failure**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest tests.test_ingest_pilot_coordinator -v
```

Expected: FAIL because `coordinator.py` does not exist.

- [ ] **Step 3: Implement work-order state transitions**

Under one in-process `run_once()` call:

1. Load trusted campaign and jobs.
2. If a worker result path is supplied, apply exactly that result first.
3. If a review result path is supplied, apply exactly that result first.
4. Ask the scheduler for the lesser of campaign capacity and the host-supplied available worker slots.
5. For each selected job, increment `attempt`, create its attempt directory and `input.json`, set `running`, and append `worker_started`.
6. Emit at most one review order.
7. Save jobs once and regenerate `monitor.md`.

There is no process lock. The operator must not run two coordinators at once.

- [ ] **Step 4: Write worker-result persistence and failure tests**

```python
def test_valid_worker_result_persists_candidate_and_refills_slot(self):
    self.start_five()
    result_path = self.write_temp_worker_result("job-1", attempt=1)
    output = run_once(self.root, self.campaign_id, worker_result_path=result_path)
    self.assertEqual(load_job(self.root, self.campaign_id, "job-1")["state"], "reviewing")
    attempt = self.attempt("job-1", 1)
    self.assertTrue(attempt.joinpath("candidate.md").is_file())
    self.assertTrue(attempt.joinpath("receipt.json").is_file())
    self.assertTrue(attempt.joinpath("suggestions.json").is_file())
    self.assertEqual(output["review_order"]["job_id"], "job-1")

def test_invalid_worker_result_fails_only_that_job(self):
    self.start_five()
    result_path = self.write_invalid_temp_result("job-1")
    output = run_once(self.root, self.campaign_id, worker_result_path=result_path)
    self.assertEqual(load_job(self.root, self.campaign_id, "job-1")["state"], "failed")
    self.assertTrue(self.attempt("job-1", 1).joinpath("failure.json").is_file())
    self.assertEqual(output["campaign_state"], "active")
```

The five-page campaign has no sixth initial job, so refill behavior is proven with a ten-job fake manifest in Task 4.

- [ ] **Step 5: Write serial Sol result tests**

Accepted review-result keys are exactly:

```json
{
  "job_id": "security-principles",
  "attempt": 1,
  "verdict": "approved",
  "reason": "Grounded and complete",
  "required_changes": []
}
```

Tests:

```python
def test_approved_review_stays_dry_run_approved(self):
    self.make_reviewing("job-1", attempt=1)
    output = run_once(
        self.root,
        self.campaign_id,
        review_result_path=self.write_review("job-1", 1, "approved"),
    )
    self.assertEqual(load_job(self.root, self.campaign_id, "job-1")["state"], "approved")
    self.assertNotIn("promotion_order", output)

def test_changes_requested_queues_fresh_attempt_at_tail(self):
    self.make_reviewing("job-1", attempt=1)
    run_once(
        self.root,
        self.campaign_id,
        review_result_path=self.write_review("job-1", 1, "changes_requested"),
    )
    job = load_job(self.root, self.campaign_id, "job-1")
    self.assertEqual(job["state"], "queued")
    self.assertGreater(job["queue_position"], max_initial_queue_position(self.jobs))

def test_third_changes_request_rejects_job(self):
    self.make_reviewing("job-1", attempt=3)
    run_once(
        self.root,
        self.campaign_id,
        review_result_path=self.write_review("job-1", 3, "changes_requested"),
    )
    self.assertEqual(load_job(self.root, self.campaign_id, "job-1")["state"], "rejected")
```

Also test Sol `rejected` is immediately terminal.

- [ ] **Step 6: Implement retry and reject**

`retry_job()` accepts only `failed` jobs with `attempt < 3`. It sets `queued`, clears `failure_reason`, and assigns `queue_position = max(queue_position) + 1`.

`reject_job()` accepts only `failed` jobs and records the supplied non-empty reason.

Neither command deletes an attempt.

- [ ] **Step 7: Add black-box CLI tests**

The CLI prints exactly one JSON object to stdout and errors to stderr.

```bash
python3 scripts/manage_ingest_pilot.py init --manifest <path>
python3 scripts/manage_ingest_pilot.py run --campaign metronome-minimum-pilot-01
python3 scripts/manage_ingest_pilot.py run --campaign metronome-minimum-pilot-01 --available-worker-slots 3
python3 scripts/manage_ingest_pilot.py run --campaign metronome-minimum-pilot-01 --worker-result /tmp/job-1.json
python3 scripts/manage_ingest_pilot.py run --campaign metronome-minimum-pilot-01 --review-result /tmp/job-1-review.json
python3 scripts/manage_ingest_pilot.py status --campaign metronome-minimum-pilot-01
python3 scripts/manage_ingest_pilot.py retry --campaign metronome-minimum-pilot-01 --job job-1
python3 scripts/manage_ingest_pilot.py reject --campaign metronome-minimum-pilot-01 --job job-1 --reason "three attempts exhausted"
```

Do not add `resume` in this dry-run plan because no promotion state exists yet.

- [ ] **Step 8: Run focused tests and commit**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest \
  tests.test_ingest_pilot_state \
  tests.test_ingest_pilot_scheduler \
  tests.test_ingest_pilot_validator \
  tests.test_ingest_pilot_coordinator -v
python3 -m py_compile scripts/manage_ingest_pilot.py scripts/ingest_pilot/*.py
git diff --check
```

Expected: all focused tests and compilation PASS.

```bash
git add scripts/manage_ingest_pilot.py scripts/ingest_pilot tests/test_ingest_pilot_coordinator.py
git commit -m "feat: coordinate minimum ingest dry run"
```

---

### Task 4: Exact Five-Page Manifest and Fake End-to-End Gate

**Files:**
- Create: `tracking/ingest/metronome/metronome-minimum-pilot-01/manifest.json`
- Create: `tests/test_ingest_pilot_end_to_end.py`

**Interfaces:**
- Consumes: Tasks 1–3 public coordinator API.
- Produces: one exact five-page pending-source manifest and one deterministic ten-job rolling-refill E2E test.

- [ ] **Step 1: Create the exact pending-source case table in the E2E test**

```python
METRONOME_CASES = (
    (
        "security-principles",
        "raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-guides-platform-configuration-security-principles.md",
        "https://docs.metronome.com/guides/platform-configuration/security-principles.md",
    ),
    (
        "design-usage-events",
        "raw/metronome/guides/events/design-usage-events-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-guides-events-design-usage-events.md",
        "https://docs.metronome.com/guides/events/design-usage-events.md",
    ),
    (
        "setup-webhooks",
        "raw/metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-guides-platform-configuration-setup-webhooks.md",
        "https://docs.metronome.com/guides/platform-configuration/setup-webhooks.md",
    ),
    (
        "preview-events",
        "raw/metronome/api-reference/invoices/preview-events-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-api-reference-invoices-preview-events.md",
        "https://docs.metronome.com/api-reference/invoices/preview-events.md",
    ),
    (
        "get-contract-edit-history",
        "raw/metronome/api-reference/contracts/get-contract-edit-history-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-api-reference-contracts-get-contract-edit-history.md",
        "https://docs.metronome.com/api-reference/contracts/get-contract-edit-history.md",
    ),
)
```

Assert all raw files exist, are regular non-symlink files, all source targets do not yet exist, URLs match the raw `Source URL` headers, and line counts demonstrate the intended short, standard, long guide, schema-heavy API, and long API mix.

- [ ] **Step 2: Create the fixed manifest**

`manifest.json` contains:

```json
{
  "schema_version": 1,
  "campaign_id": "metronome-minimum-pilot-01",
  "provider": "metronome",
  "mode": "dry_run",
  "worker_concurrency": 5,
  "review_concurrency": 1,
  "max_attempts": 3,
  "jobs": [
    {
      "job_id": "security-principles",
      "raw_path": "raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md",
      "raw_sha256": "07c9a57f56b4c56ed3c219b5d87aa3994d4f02da10f3ef5109bf94ea3a2eb276",
      "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-security-principles.md",
      "canonical_url": "https://docs.metronome.com/guides/platform-configuration/security-principles.md"
    },
    {
      "job_id": "design-usage-events",
      "raw_path": "raw/metronome/guides/events/design-usage-events-2026-07-13.md",
      "raw_sha256": "ae48bff62df062d45d423bc66fbeabc2a08951782a435e9fd48047cd82813d3c",
      "source_target": "wiki/sources/metronome/source-metronome-guides-events-design-usage-events.md",
      "canonical_url": "https://docs.metronome.com/guides/events/design-usage-events.md"
    },
    {
      "job_id": "setup-webhooks",
      "raw_path": "raw/metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md",
      "raw_sha256": "be2dac89292c31ac5f489809e5f4b483f2e1633b82799ccff45d6c20e44ad73a",
      "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-setup-webhooks.md",
      "canonical_url": "https://docs.metronome.com/guides/platform-configuration/setup-webhooks.md"
    },
    {
      "job_id": "preview-events",
      "raw_path": "raw/metronome/api-reference/invoices/preview-events-2026-07-13.md",
      "raw_sha256": "022e7c970bf8eb8dbe80c6f15d6f4be8cbdcaab9733dc51718958edf407d34b6",
      "source_target": "wiki/sources/metronome/source-metronome-api-reference-invoices-preview-events.md",
      "canonical_url": "https://docs.metronome.com/api-reference/invoices/preview-events.md"
    },
    {
      "job_id": "get-contract-edit-history",
      "raw_path": "raw/metronome/api-reference/contracts/get-contract-edit-history-2026-07-13.md",
      "raw_sha256": "73072ca968bca78aa30ebcb896a1738061c3a3f90caabfa782af58ef60438c81",
      "source_target": "wiki/sources/metronome/source-metronome-api-reference-contracts-get-contract-edit-history.md",
      "canonical_url": "https://docs.metronome.com/api-reference/contracts/get-contract-edit-history.md"
    }
  ]
}
```

Keep `jobs` in the exact case-table order. The hashes above are the current immutable bytes and must be checked again by the manifest test.

- [ ] **Step 3: Write one ten-job fake rolling campaign test**

The E2E fixture creates ten small raw files in `TemporaryDirectory` and proves:

1. `init_campaign()` creates ten queued jobs.
2. First `run_once(..., available_worker_slots=5)` emits jobs 1–5.
3. Submitting job 1 emits job 6 immediately.
4. Submitting jobs 2–5 never exceeds five running workers.
5. One invalid result fails only its job.
6. `retry_job()` moves that job behind jobs 7–10.
7. Review orders are emitted one at a time.
8. One `changes_requested` result creates attempt 2 at the tail.
9. A third `changes_requested` becomes rejected.
10. A simulated restart changes running/reviewing to failed while retaining candidate and attempt files.
11. No fake raw file changes.
12. No file under `wiki/` is created.

- [ ] **Step 4: Run the fake E2E and complete repository suite**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest tests.test_ingest_pilot_end_to_end -v
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest discover -s tests -q
python3 -m py_compile scripts/manage_ingest_pilot.py scripts/ingest_pilot/*.py
git diff --check
```

Expected:

- fake E2E PASS;
- complete repository suite PASS;
- compilation PASS;
- no diff whitespace errors.

- [ ] **Step 5: Commit**

```bash
git add \
  tracking/ingest/metronome/metronome-minimum-pilot-01/manifest.json \
  tests/test_ingest_pilot_end_to_end.py
git commit -m "test: gate minimum Metronome ingest pilot"
```

---

### Task 5: Execute Five Terra Candidates and Serial Sol Dry-Run Review

**Files:**
- Create through the coordinator:
  - `tracking/ingest/metronome/metronome-minimum-pilot-01/campaign.json`
  - `tracking/ingest/metronome/metronome-minimum-pilot-01/jobs.json`
  - `tracking/ingest/metronome/metronome-minimum-pilot-01/events.jsonl`
  - `tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md`
  - `tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/**`
- Modify: none under `raw/` or `wiki/`.

**Interfaces:**
- Consumes: exact five-page manifest, native Terra workers, and primary Sol review.
- Produces: five dry-run candidates or explicit failed/rejected evidence, plus the monitor and raw-hash proof.

- [ ] **Step 1: Record raw hashes before initialization**

Run:

```bash
shasum -a 256 \
  raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md \
  raw/metronome/guides/events/design-usage-events-2026-07-13.md \
  raw/metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md \
  raw/metronome/api-reference/invoices/preview-events-2026-07-13.md \
  raw/metronome/api-reference/contracts/get-contract-edit-history-2026-07-13.md \
  > /tmp/metronome-minimum-pilot-01-before.sha256
```

- [ ] **Step 2: Initialize and emit work orders up to current host capacity**

Run:

```bash
python3 scripts/manage_ingest_pilot.py init \
  --manifest tracking/ingest/metronome/metronome-minimum-pilot-01/manifest.json
python3 scripts/manage_ingest_pilot.py run \
  --campaign metronome-minimum-pilot-01 \
  --available-worker-slots 3
```

Expected in the current Codex host: exactly three `spawn_worker` orders and three `running` jobs. The campaign maximum remains five; the fake E2E proves five-slot behavior independently of the host's smaller native-agent capacity.

- [ ] **Step 3: Spawn all five native Terra workers with rolling host capacity**

The primary Sol coordinator uses the native sub-agent interface with:

- model: `gpt-5.6-terra`;
- reasoning effort: `medium`;
- one complete raw page per worker;
- no repository write permission in the task instructions;
- one unique result path `/tmp/metronome-minimum-pilot-01/<job-id>.json`;
- the exact work order JSON;
- the source-page template from `rules/ingest.md`;
- an instruction to read the raw file from first through last line and return exactly the worker-result schema.

The current collaboration host permits three worker sub-agents alongside the primary agent. Start three, then spawn the remaining two as slots are released. Do not invent another launcher merely to reach five simultaneous native workers.

Do not use CLI model launchers, Git worktrees, or the historical Metronome model-runner scripts.

- [ ] **Step 4: Import each completed result and keep worker slots rolling**

For each returned result:

```bash
python3 scripts/manage_ingest_pilot.py run \
  --campaign metronome-minimum-pilot-01 \
  --worker-result /tmp/metronome-minimum-pilot-01/<job-id>.json \
  --available-worker-slots 1
```

The five-page campaign has no sixth initial job. Rolling refill is already proven by the fake ten-job E2E; do not add extra live pages to demonstrate it.

If a worker result fails validation, leave the job `failed`. Do not silently repair or retry it. Report it to the user before using the explicit `retry` command.

- [ ] **Step 5: Review candidates serially with the primary Sol agent**

For each emitted review order:

1. Read the entire raw file.
2. Read the candidate, quotes, suggestions, and relevant existing wiki pages.
3. Check factual completeness, quote accuracy, source-page structure, taxonomy suggestions, contradictions, and raw link.
4. Write one review JSON outside the repository at `/tmp/metronome-minimum-pilot-01/<job-id>-review.json`.
5. Import it:

```bash
python3 scripts/manage_ingest_pilot.py run \
  --campaign metronome-minimum-pilot-01 \
  --review-result /tmp/metronome-minimum-pilot-01/<job-id>-review.json
```

Review exactly one candidate at a time. Do not ask another Sol sub-agent to parallelize reviews.

- [ ] **Step 6: Verify raw immutability and dry-run write boundary**

Run:

```bash
shasum -a 256 \
  raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md \
  raw/metronome/guides/events/design-usage-events-2026-07-13.md \
  raw/metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md \
  raw/metronome/api-reference/invoices/preview-events-2026-07-13.md \
  raw/metronome/api-reference/contracts/get-contract-edit-history-2026-07-13.md \
  > /tmp/metronome-minimum-pilot-01-after.sha256
diff -u \
  /tmp/metronome-minimum-pilot-01-before.sha256 \
  /tmp/metronome-minimum-pilot-01-after.sha256
```

Also run:

```bash
git status --short
git diff --name-only
```

Expected:

- raw hash diff prints nothing;
- changed files are only under `tracking/ingest/metronome/metronome-minimum-pilot-01/`;
- no file under `wiki/` changed;
- no source target from `METRONOME_CASES` exists.

- [ ] **Step 7: Run final validation**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/metronome-minimum-pilot-pycache \
python3 -m unittest \
  tests.test_ingest_pilot_state \
  tests.test_ingest_pilot_validator \
  tests.test_ingest_pilot_scheduler \
  tests.test_ingest_pilot_coordinator \
  tests.test_ingest_pilot_end_to_end -v
python3 -m py_compile scripts/manage_ingest_pilot.py scripts/ingest_pilot/*.py
git diff --check
```

Expected: all minimum-pilot tests and static checks PASS.

- [ ] **Step 8: Commit dry-run evidence and stop**

```bash
git add tracking/ingest/metronome/metronome-minimum-pilot-01
git commit -m "tracking: record minimum Metronome ingest dry run"
```

Stop and report:

- job and attempt counts;
- approved, failed, and rejected counts;
- per-page Sol verdicts;
- raw-hash comparison;
- Terra output quality and recurring repair themes;
- monitor path;
- exact commit.

Do not create a canonical-promotion plan or edit `wiki/` until the user reviews and approves the dry-run results.

---

## Completion Gate

This plan is complete only when:

- Tasks 1–4 pass the full repository suite;
- the five-page live dry-run has durable candidate/review evidence;
- every raw hash is unchanged;
- no canonical wiki file changed;
- the monitor accurately explains every job;
- the branch stops for user approval.

If implementation requires recovery.py, an operation journal, a background daemon, a worker Git worktree, or more than the files listed in this plan, stop and revise the design instead of adding them.
