# Metronome Mature Ingest Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Campaign 08 targeted retry review, reviewer-approved shared-update grouping, and minimal campaign timing without changing the existing dynamic scheduler or starting ingestion.

**Architecture:** Extend the current trusted JSON contracts rather than adding a service or backend. The scheduler continues using the existing three-slot review-first loop; retry context travels through the job and work orders, approved shared suggestions are exposed as a grouped read-only plan, and the coordinator remains the only canonical writer.

**Tech Stack:** Python 3 standard library, JSON/Markdown tracking artifacts, `unittest`, existing `scripts/ingest_pilot` modules.

## Global Constraints

- Sol is the default worker; Terra is allowed only for isolated templated pages with no semantic shared-concept update.
- Every first-attempt candidate receives an independent complete-source Sol review.
- Targeted retry review is allowed only for an unchanged raw hash and enumerated bounded corrections with no unrelated semantic change.
- Factual errors, material omissions, misunderstandings, new evidence, and unresolved content risks require another complete-source review.
- Keep the existing three dynamic sub-agent slots and review-first scheduling behavior; do not add a batch barrier.
- Workers and reviewers remain repository-read-only; only the coordinator writes canonical wiki and campaign state.
- Shared updates are grouped for coordinator consumption but are never automatically applied to wiki files.
- Run global wiki validation, Metronome capsule validation, and the predetermined three-page audit once at campaign close.
- Add only `started_at` and `completed_at` timing fields; do not add event-level performance telemetry.
- Initialize new campaigns with state schema v2; keep Campaign 07 and other schema-v1 artifacts status-readable without migration or rewriting.
- Do not touch the unrelated untracked `CLAUDE copy.md`.

---

### Task 1: Validate structured shared updates and review decisions

**Files:**
- Modify: `scripts/ingest_pilot/state.py`
- Modify: `scripts/ingest_pilot/validator.py`
- Modify: `scripts/ingest_pilot/coordinator.py`
- Modify: `scripts/ingest_pilot/scheduler.py`
- Test: `tests/test_ingest_pilot_state.py`
- Test: `tests/test_ingest_pilot_validator.py`
- Test: `tests/test_ingest_pilot_coordinator.py`

**Interfaces:**
- Consumes: existing worker result key `suggestions` and review result processing in `_apply_review_result()`.
- Produces: state schema v2 with job `contract_version: 2`; suggestion objects with exact keys `update_id`, `target_path`, `update_kind`, `anchor`, `proposed_markdown`, `quote_indexes`, and `warnings`; review results with `review_scope`, `retry_review_scope`, and `shared_update_decisions`.

- [ ] **Step 1: Add failing state-version and worker-suggestion contract tests**

Assert newly initialized state uses `schema_version: 2` and each new job uses
`contract_version: 2`. Add a manually constructed schema-v1 campaign fixture
and assert `status()` can still render it without changing its files.

Change the test fixture's empty suggestions to retain the existing category keys:

```python
{"company": [], "concepts": [], "index": [], "log": []}
```

Add a valid concept update:

```python
{
    "update_id": "concept-billing-link",
    "target_path": "wiki/concepts/metronome/metronome-billing.md",
    "update_kind": "durable_fact",
    "anchor": "## Sources",
    "proposed_markdown": "- [[source-job-1]] — documented billing behavior",
    "quote_indexes": [0],
    "warnings": [],
}
```

Assert that `validate_worker_result()` accepts that object and rejects:

```python
{"update_id": "../escape"}                       # incomplete schema
{"target_path": "raw/metronome/source.md"}      # non-wiki target
{"update_kind": "rewrite_everything"}           # unknown kind
{"quote_indexes": [3]}                           # outside the 3-quote fixture
{"warnings": "none"}                            # wrong type
```

- [ ] **Step 2: Run the worker-suggestion tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_validator -v
```

Expected: the new structured-suggestion tests fail because suggestions currently accept arbitrary array members.

- [ ] **Step 3: Implement the minimal structured-suggestion validator**

In `validator.py`, add:

```python
SUGGESTION_ITEM_KEYS = {
    "update_id", "target_path", "update_kind", "anchor",
    "proposed_markdown", "quote_indexes", "warnings",
}
UPDATE_KINDS = {
    "durable_fact", "reciprocal_source_link", "catalog_entry",
    "log_entry", "calculated_count",
}
TARGET_PREFIXES = {
    "company": "wiki/companies/",
    "concepts": "wiki/concepts/",
    "index": "wiki/",
    "log": "wiki/",
}
```

Add `_validate_suggestions(suggestions, quote_count)` and call it after quote validation. Require non-empty unique `update_id` values within one worker result, category-appropriate repository-relative Markdown paths, a known update kind, non-empty `anchor` and `proposed_markdown`, unique zero-based integer `quote_indexes` within the submitted quote list, and a list of text warnings. Permit empty `quote_indexes` only for `catalog_entry`, `log_entry`, and `calculated_count`.

- [ ] **Step 4: Add failing review-result contract tests**

Update `write_review()` in `tests/test_ingest_pilot_coordinator.py` to emit:

```python
{
    "job_id": job_id,
    "attempt": attempt,
    "verdict": verdict,
    "reason": "Grounded and complete",
    "required_changes": [],
    "review_scope": "full",
    "retry_review_scope": None,
    "shared_update_decisions": [],
}
```

Add tests proving:

- `approved` requires an empty `required_changes` list and null `retry_review_scope`;
- `changes_requested` requires a non-empty `required_changes` list and `retry_review_scope` equal to `targeted` or `full`;
- `review_scope` is only `full` or `targeted`;
- each shared update receives exactly one decision object with keys `update_id`, `verdict`, and `reason`;
- decision verdicts are only `approved` or `rejected`, and decision IDs exactly match the current attempt's `suggestions.json` IDs.

- [ ] **Step 5: Run the coordinator tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_coordinator -v
```

Expected: the new review fields are rejected by the current fixed schema.

- [ ] **Step 6: Implement review-result validation and persistence**

Use the eight-key contract from Step 4 for schema-v2 campaigns and retain the existing five-key contract only for status/read compatibility with schema v1. Add `_validate_review_result(result, expected_scope, suggestion_ids)` in `coordinator.py`. Load the current attempt's `suggestions.json`, validate all per-update decisions, and persist the validated fields in `review.json` together with `reviewer_identity` and `reviewer_model`.

Set `SCHEMA_VERSION = 2` in `state.py`, add `contract_version: 2` to newly initialized jobs, and copy it into worker/reviewer orders. In `validator.py`, apply the structured suggestion rules to contract v2 while retaining the legacy string-array acceptance path only when `job.get("contract_version", 1) == 1`.

Keep `review_order()` and `_review_orders()` defaulting first-attempt candidates to:

```python
{"review_scope": "full", "prior_attempt": None, "preferred_reviewer_identity": None}
```

- [ ] **Step 7: Run Task 1 tests**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_state tests.test_ingest_pilot_validator tests.test_ingest_pilot_coordinator -v
```

Expected: PASS.

- [ ] **Step 8: Commit Task 1**

```bash
git add scripts/ingest_pilot/state.py scripts/ingest_pilot/validator.py scripts/ingest_pilot/coordinator.py scripts/ingest_pilot/scheduler.py tests/test_ingest_pilot_state.py tests/test_ingest_pilot_validator.py tests/test_ingest_pilot_coordinator.py
git commit -m "Add Metronome structured review contracts"
```

### Task 2: Carry bounded retry context into worker and reviewer orders

**Files:**
- Modify: `scripts/ingest_pilot/coordinator.py`
- Modify: `scripts/ingest_pilot/scheduler.py`
- Test: `tests/test_ingest_pilot_coordinator.py`
- Test: `tests/test_ingest_pilot_scheduler.py`

**Interfaces:**
- Consumes: `retry_review_scope`, `required_changes`, current reviewer identity, and the immutable prior attempt directory from Task 1.
- Produces: job field `retry_context`; retry worker order field `retry_context`; review order fields `review_scope`, `prior_attempt`, and `preferred_reviewer_identity`.

- [ ] **Step 1: Add failing targeted-retry order tests**

Create a `changes_requested` review with:

```python
{
    "required_changes": ["Fix the concept backlink and no other prose."],
    "retry_review_scope": "targeted",
    "review_scope": "full",
}
```

Assert that the next queued job stores:

```python
{
    "prior_attempt": 1,
    "review_scope": "targeted",
    "required_changes": ["Fix the concept backlink and no other prose."],
    "prior_reviewer_identity": "reviewer-a",
}
```

Assert the retry worker order carries that exact `retry_context`. After the corrected result becomes `candidate_ready`, assert its review order has `review_scope: targeted`, `prior_attempt: 1`, and `preferred_reviewer_identity: reviewer-a`.

Add a parallel case for `retry_review_scope: full` and assert `preferred_reviewer_identity` is null.

- [ ] **Step 2: Run the retry tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_coordinator tests.test_ingest_pilot_scheduler -v
```

Expected: the new retry fields are absent from job and order output.

- [ ] **Step 3: Persist retry context after a change request**

In `_apply_review_result()`, when the verdict is `changes_requested`, set:

```python
job["retry_context"] = {
    "prior_attempt": job["attempt"],
    "review_scope": result["retry_review_scope"],
    "required_changes": list(result["required_changes"]),
    "prior_reviewer_identity": job.get("reviewer_identity"),
}
```

Retain the existing queue-tail behavior and three-attempt limit. Clear stale `reviewer_identity` and `reviewer_model` when returning the job to `queued`, but keep them inside `retry_context` as historical evidence.

- [ ] **Step 4: Emit retry context without changing slot allocation**

In `worker_orders()`, copy `retry_context` into an attempt-2/3 worker order when present. In `review_order()` and `_review_orders()`, derive:

```python
review_scope = job.get("retry_context", {}).get("review_scope", "full")
prior_attempt = job.get("retry_context", {}).get("prior_attempt")
preferred_reviewer_identity = (
    job.get("retry_context", {}).get("prior_reviewer_identity")
    if review_scope == "targeted" else None
)
```

Do not modify `shared_slot_orders()` capacity calculations. Assignment remains a coordinator decision: the previous reviewer is preferred for targeted review but not required when unavailable.

- [ ] **Step 5: Enforce the performed review scope**

When `_start_review()` or `_start_shared_orders()` changes a job to `reviewing`, persist the order's `review_scope` as `active_review_scope`. Reject a review result whose `review_scope` differs. On approval or terminal rejection, remove `active_review_scope` and `retry_context` from the job.

- [ ] **Step 6: Run Task 2 tests**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_scheduler tests.test_ingest_pilot_coordinator -v
```

Expected: PASS, including the existing three-slot review-first cases.

- [ ] **Step 7: Commit Task 2**

```bash
git add scripts/ingest_pilot/coordinator.py scripts/ingest_pilot/scheduler.py tests/test_ingest_pilot_coordinator.py tests/test_ingest_pilot_scheduler.py
git commit -m "Add bounded Metronome retry review context"
```

### Task 3: Expose reviewer-approved shared updates by target path

**Files:**
- Modify: `scripts/ingest_pilot/coordinator.py`
- Test: `tests/test_ingest_pilot_coordinator.py`

**Interfaces:**
- Consumes: approved jobs' `suggestions.json` and `review.json` files from Task 1.
- Produces: `_approved_shared_updates(root, campaign_id, jobs) -> dict[str, list[dict]]` and `shared_update_plan` in coordinator status output.

- [ ] **Step 1: Add a failing grouped-plan test**

Create two approved jobs whose reviewer decisions approve updates targeting the same concept and reject one unnecessary company update. Assert status returns:

```python
{
    "wiki/concepts/metronome/metronome-billing.md": [
        {"job_id": "job-1", "attempt": 1, "update_id": "billing-a", "proposed_markdown": "- [[source-job-1]] — billing fact A"},
        {"job_id": "job-2", "attempt": 1, "update_id": "billing-b", "proposed_markdown": "- [[source-job-2]] — billing fact B"},
    ]
}
```

The rejected update must be absent, and no wiki file may be created or modified.
Also assert a schema-v1 campaign returns an empty `shared_update_plan` without
parsing or rewriting its historical string suggestions.

- [ ] **Step 2: Run the grouped-plan test and verify failure**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_coordinator.CoordinatorTests.test_status_groups_only_reviewer_approved_shared_updates -v
```

Expected: FAIL because `shared_update_plan` does not exist.

- [ ] **Step 3: Implement read-only grouping**

Add `_approved_shared_updates()` to `coordinator.py`. Return an empty dictionary
for schema-v1 campaigns. For schema v2, read only each approved job's current
attempt `suggestions.json` and `review.json`, join suggestion objects to
`approved` decisions by `update_id`, add `job_id` and `attempt`, and group the
results by exact `target_path`. Preserve job queue order and suggestion order.
Raise `PilotError` on missing, malformed, or mismatched approved v2 evidence.

Add the grouped dictionary to `_campaign_payload()` as `shared_update_plan`. Do not deduplicate or merge prose automatically; the coordinator resolves duplicate links and semantic collisions while applying one patch per target.

- [ ] **Step 4: Run Task 3 tests**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_coordinator -v
```

Expected: PASS and no canonical wiki mutation.

- [ ] **Step 5: Commit Task 3**

```bash
git add scripts/ingest_pilot/coordinator.py tests/test_ingest_pilot_coordinator.py
git commit -m "Group approved Metronome shared updates"
```

### Task 4: Record minimal campaign timing and completion metrics

**Files:**
- Modify: `scripts/ingest_pilot/state.py`
- Modify: `scripts/ingest_pilot/coordinator.py`
- Modify: `scripts/manage_ingest_pilot.py`
- Test: `tests/test_ingest_pilot_state.py`
- Test: `tests/test_ingest_pilot_coordinator.py`

**Interfaces:**
- Consumes: terminal job states and persisted `review.json` artifacts.
- Produces: campaign fields `started_at`, `completed_at`, and `coordinator_repairs`; `save_campaign(root, campaign_id, campaign)`; `complete_campaign(root, campaign_id, coordinator_repairs)`; CLI command `complete --campaign ID --coordinator-repairs N`.

- [ ] **Step 1: Add failing initialization and monitor tests**

Patch `scripts.ingest_pilot.state._utc_now` to return `2026-07-31T01:02:03Z`. Assert initialization writes:

```python
{
    "started_at": "2026-07-31T01:02:03Z",
    "completed_at": None,
    "coordinator_repairs": 0,
}
```

Assert the monitor renders start time, incomplete completion time, full-review count, targeted-review count, coordinator repairs, and elapsed time as `in progress`.

- [ ] **Step 2: Add failing explicit-completion tests**

Assert `complete_campaign()`:

- rejects a negative or boolean repair count;
- rejects campaigns containing `queued`, `running`, `candidate_ready`, `reviewing`, or `failed` jobs;
- accepts only all-`approved`/`rejected` jobs;
- sets campaign state to `complete`, records `_utc_now()` in `completed_at`, records the supplied repair count, and does not rewrite attempt evidence;
- rejects a second completion call.

- [ ] **Step 3: Run timing tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_state tests.test_ingest_pilot_coordinator -v
```

Expected: the clock helper, completion function, fields, and monitor metrics are absent.

- [ ] **Step 4: Implement timestamp and atomic campaign-state writes**

In `state.py`, add:

```python
def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

Initialize the three fields from Step 1. Add an atomic `_replace_campaign()` using the same sibling-temp, `fsync`, and `os.replace` pattern as `_replace_jobs()`.

Expose `save_campaign(root, campaign_id, campaign)` as the narrow state-writing interface. Have `_write_monitor()` count full and targeted reviews from persisted `review.json` files and calculate elapsed seconds only when both timestamps exist.

In `coordinator.py`, add `complete_campaign()` and persist through `save_campaign()`. Do not add timestamps to individual events.

- [ ] **Step 5: Add the thin completion CLI**

Add this parser shape in `manage_ingest_pilot.py`:

```text
complete --campaign CAMPAIGN_ID --coordinator-repairs NON_NEGATIVE_INTEGER
```

Dispatch it to `complete_campaign()`. Keep completion explicit so job approval does not falsely imply that canonical promotion, backlinks, and campaign-close validation have finished.

- [ ] **Step 6: Run Task 4 tests**

Run:

```bash
python3 -m unittest tests.test_ingest_pilot_state tests.test_ingest_pilot_coordinator -v
```

Expected: PASS.

- [ ] **Step 7: Commit Task 4**

```bash
git add scripts/ingest_pilot/state.py scripts/ingest_pilot/coordinator.py scripts/manage_ingest_pilot.py tests/test_ingest_pilot_state.py tests/test_ingest_pilot_coordinator.py
git commit -m "Record Metronome campaign completion metrics"
```

### Task 5: Align rules and run the complete regression gate

**Files:**
- Modify: `rules/ingest.md`
- Modify: `rules/psp/metronome.md`
- Test: existing `tests/test_ingest_pilot_*.py`

**Interfaces:**
- Consumes: implemented contracts and commands from Tasks 1-4.
- Produces: the canonical operator rules for Campaign 08 simplified production mode.

- [ ] **Step 1: Update the shared ingest rule**

In the coordinator-controlled exception in `rules/ingest.md`, state exactly:

- first attempts require complete-source strong review;
- bounded unchanged-hash corrections may use targeted diff review;
- factual or uncertain corrections require full review;
- reviewer-approved shared updates are grouped by target and applied once by the coordinator;
- coordinator does not perform a default third full-source read;
- campaign-close validations are run once.

- [ ] **Step 2: Update the Metronome provider rule**

In `rules/psp/metronome.md`, add the Campaign 08 mature-mode routing and operation rules: Sol default worker, Terra isolation restriction, three dynamic slots, no batch barrier, targeted-review preference for the prior reviewer, explicit campaign completion, two timing fields, and coordinator consumption of `shared_update_plan`.

- [ ] **Step 3: Run the ingest-pilot regression suite**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_ingest_pilot*.py' -v
```

Expected: PASS.

- [ ] **Step 4: Run the Metronome capsule and wiki rule checks**

Run:

```bash
python3 scripts/validate_metronome_capsule.py
python3 scripts/validate_wiki.py wiki/metronome-index.md wiki/metronome-log.md wiki/companies/metronome.md
git diff --check
```

Expected: capsule validation passes with the pending queue reported; the three targeted wiki files pass; `git diff --check` emits no output.

- [ ] **Step 5: Commit Task 5**

```bash
git add rules/ingest.md rules/psp/metronome.md
git commit -m "Adopt Metronome simplified production ingest mode"
```

## Post-implementation gate

After all five tasks pass, prepare but do not execute the exact Campaign 08 selection review and manifest. The user must approve those source job IDs and the three predetermined audit job IDs before any worker is spawned.
