# Metronome Selective Ingest Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Validate the approved three-disposition selective-ingest strategy on Metronome Custom Fields with about five complete model reads instead of six full source-generation and review cycles.

**Architecture:** Keep the first pilot outside the production campaign scheduler: one coordinator-owned exact selection record and monitor drive three bounded native-Sol tasks. Only the official overview can become a canonical source in this pilot; a raw-reference audit and a semantic-triage decision test routing quality without expanding into endpoint ingestion. Add only the deterministic related-raw-link validation needed by the pilot, then close with three fixed query checks and existing wiki/capsule validation.

**Tech Stack:** Python 3 standard library, `unittest`, JSON, Markdown/Obsidian wikilinks, existing `validate_wiki.py` and `metronome_capsule.py`, native GPT-5.6 Sol subagents.

## Global Constraints

- Read `CLAUDE.md`, `rules/ingest.md`, `rules/query-and-synthesis.md`, `rules/lint.md`, and `rules/psp/metronome.md` before implementation.
- Do not initialize or execute Campaign 12 until the replacement exact selection record receives explicit user approval.
- Keep complete canonical collection unchanged; never modify accepted files under `raw/`.
- Each agent reads exactly one complete raw page and writes only to its assigned `/private/tmp/metronome-campaign-12/` directory.
- The coordinator is the only writer of repository tracking files, concepts, sources, company/index/log files, and commits.
- Use Sol for the overview worker, overview reviewer, raw-reference auditor, semantic-triage worker, and semantic-triage reviewer.
- After generating each native-agent order, confirm the returned agent identifier before processing another completion event.
- Do not use worktrees, modify the production campaign scheduler/schema, add a numeric score, initialize a full provider routing registry, or expand to the other three Custom Fields endpoints.
- `## Raw Sources` contains only completely read factual evidence; `## Related raw API references` contains navigation-only raw pages and cannot support source claims.
- A query promotion or triage decision does not create an endpoint source during this pilot; it records a future `source_required` disposition.
- Run full tests once at close because rules and validator code change; do not add repeated audit tiers.
- Leave `CLAUDE copy.md` and all unrelated worktree changes untouched.

## Scope Boundary

This plan implements one independently testable Metronome calibration pilot.
The provider-wide `routing.json`, periodic navigation-refresh automation,
Stripe/Adyen/PayPal/Braintree adoption, and legacy-source migration are a
second subsystem and receive a separate plan only after this pilot returns
`approve_selective_routing`. This prevents unvalidated pilot assumptions from
becoming production infrastructure.

---

### Task 1: Validate Navigation-Only Raw Links

**Files:**
- Modify: `scripts/metronome_capsule.py:13-182`
- Modify: `scripts/validate_metronome_capsule.py:13-28`
- Modify: `tests/test_metronome_capsule.py:15-159`

**Interfaces:**
- Consumes: existing `WIKILINK_RE`, source `raw_files`, and `## Raw Sources` parsing.
- Produces: `SourceRecord.related_raw_files: Tuple[str, ...]`; `inspect_capsule()` parses `## Related raw API references`; `validate_capsule()` rejects missing, outside-provider, duplicated, or evidence-overlapping related raw links while leaving them in `orphan_raw_files`; CLI output calls those paths raw pages without source summaries rather than mandatory pending ingest.

- [ ] **Step 1: Extend the fixture and write failing related-raw tests**

Add `related_links=()` to `write_source()`, render the section only when non-empty, and add these tests:

```python
def test_related_raw_reference_is_valid_navigation_but_remains_uningested(self):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = "source-metronome-guides-home"
        self.make_capsule(root, source_count=1, index_links=(source,))
        evidence = self.write_raw(root)
        related = self.write_raw(root, "guides/create-widget-2026-07-13.md")
        self.write_source(root, related_links=(related,))

        report = inspect_capsule(root)

        self.assertEqual((related,), report.orphan_raw_files)
        self.assertEqual((related,), report.sources[0].related_raw_files)
        self.assertEqual([], validate_capsule(report))

def test_related_raw_reference_must_exist(self):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = "source-metronome-guides-home"
        self.make_capsule(root, source_count=1, index_links=(source,))
        self.write_raw(root)
        self.write_source(
            root,
            related_links=("metronome/guides/missing-2026-07-13.md",),
        )

        errors = validate_capsule(inspect_capsule(root))

        self.assertTrue(any("related raw references do not exist" in error for error in errors))

def test_related_raw_reference_cannot_duplicate_factual_raw_source(self):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = "source-metronome-guides-home"
        self.make_capsule(root, source_count=1, index_links=(source,))
        evidence = self.write_raw(root)
        self.write_source(root, related_links=(evidence,))

        errors = validate_capsule(inspect_capsule(root))

        self.assertTrue(any("both Raw Sources and Related raw API references" in error for error in errors))
```

- [ ] **Step 2: Run the focused tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_metronome_capsule -v
```

Expected: the new tests fail because `write_source()` and `SourceRecord` do not yet support `related_raw_files`.

- [ ] **Step 3: Add one reusable Markdown-section parser**

Replace the single-purpose parser with:

```python
RELATED_RAW_HEADING = re.compile(
    r"^## Related raw API references\s*$", re.MULTILINE
)


def _section_raw_files(body: str, heading_pattern: re.Pattern[str]) -> Tuple[str, ...]:
    heading = heading_pattern.search(body)
    if heading is None:
        return ()
    section_start = heading.end()
    next_heading = NEXT_HEADING.search(body, section_start)
    section = body[section_start:next_heading.start() if next_heading else len(body)]
    paths = []
    for target in WIKILINK_RE.findall(section):
        target = target.strip().rstrip("\\").strip()
        if target.startswith("raw/"):
            target = target[len("raw/"):]
        paths.append(target + ("" if target.endswith(".md") else ".md"))
    return tuple(paths)


def _raw_source_files(body: str) -> Tuple[str, ...]:
    return _section_raw_files(body, RAW_SOURCES_HEADING)


def _related_raw_files(body: str) -> Tuple[str, ...]:
    return _section_raw_files(body, RELATED_RAW_HEADING)
```

Add `related_raw_files: Tuple[str, ...]` to `SourceRecord` and populate it in `_source_record()`.

- [ ] **Step 4: Implement the four structural checks**

Inside the per-source validation loop, add:

```python
related_outside = [
    path for path in source.related_raw_files
    if not path.startswith("metronome/")
]
if related_outside:
    errors.append(
        f"{source.path}: related raw references must stay inside metronome/"
    )
related_missing = [
    path for path in source.related_raw_files
    if path not in raw_files
]
if related_missing:
    errors.append(
        f"{source.path}: related raw references do not exist: {related_missing}"
    )
related_duplicates = sorted({
    path for path in source.related_raw_files
    if source.related_raw_files.count(path) > 1
})
if related_duplicates:
    errors.append(
        f"{source.path}: duplicate related raw references: {related_duplicates}"
    )
evidence_overlap = sorted(set(source.raw_files) & set(source.related_raw_files))
if evidence_overlap:
    errors.append(
        f"{source.path}: raw files appear in both Raw Sources and "
        f"Related raw API references: {evidence_overlap}"
    )
```

Do not add related raw references to the `referenced` set used to calculate `orphan_raw_files`; raw-only navigation must remain distinguishable from ingested evidence.

- [ ] **Step 5: Correct the capsule report wording**

In `validate_metronome_capsule.py`, change the summary suffix from `pending ingest` to `raw pages without source summaries` and the detail heading from `Pending ingest:` to `Raw pages without source summaries:`. Keep the underlying `orphan_raw_files` field unchanged for compatibility.

- [ ] **Step 6: Run focused tests**

Run:

```bash
python3 -m unittest tests.test_metronome_capsule -v
```

Expected: all Metronome capsule tests pass.

- [ ] **Step 7: Commit the validator boundary**

```bash
git add scripts/metronome_capsule.py scripts/validate_metronome_capsule.py tests/test_metronome_capsule.py
git commit -m "feat: validate Metronome related raw references"
```

---

### Task 2: Define the Selective Pilot Rules and Exact Proposal

**Files:**
- Modify: `rules/ingest.md:11-71`
- Modify: `rules/query-and-synthesis.md:12-44`
- Modify: `rules/lint.md:40-55`
- Modify: `rules/psp/metronome.md:161-175`
- Replace: `tracking/ingest/metronome/metronome-campaign-12/manifest.json`
- Replace: `tracking/ingest/metronome/metronome-campaign-12/selection-review.md`

**Interfaces:**
- Consumes: approved design `docs/superpowers/specs/2026-08-02-selective-psp-ingest-routing-design.md` and the six immutable Custom Fields raw pages.
- Produces: common three-disposition terminology, query raw-fallback behavior, a Metronome-only bounded pilot authorization, and an exact uninitialized six-page classification proposal.

- [ ] **Step 1: Add the common selective-ingest boundary**

Add a section before the parallel-review exception in `rules/ingest.md` defining exactly:

```text
source_required  = full source generation plus independent review
raw_reference    = navigation-only raw; no routine source generation
semantic_triage  = one complete strong-model read to decide the disposition
```

State that `Raw Sources` is factual evidence, `Related raw API references` is navigation-only, metadata classification never authorizes facts from an unread page, and query/user-approved promotion to `source_required` queues a missing source without requiring a raw hash change.

- [ ] **Step 2: Correct raw fallback in the query rule**

Change step 3 to consult both `raw_files:`/`## Raw Sources` and `## Related raw API references`. Replace the automatic mutation in step 4 with this behavior:

```text
Read a relevant unlinked or related raw page completely when the query needs
it. Answering from raw does not itself authorize a source-page write. When the
raw contributes reusable knowledge, an important boundary, or repeated query
value, recommend promotion; ingest begins only after approval.
```

Update the example so its raw sweep answers from raw first and offers source promotion separately instead of creating a source automatically.

- [ ] **Step 3: Correct orphan terminology in the lint rule**

State that a raw page without a source summary is informational and may be an intentional `raw_reference`, an unresolved `semantic_triage` page, or a future source candidate. It is not a backlog that must reach zero. Preserve all existing failure conditions for duplicate canonical URLs, missing raw versions, `raw_files`/`Raw Sources` disagreement, index drift, and incorrect company counts.

- [ ] **Step 4: Add the Metronome Campaign 12 pilot authorization**

Append a provider-specific section that fixes:

- all five agents as Sol;
- three native tasks only: overview generation, create-key raw-reference audit, and delete-key semantic triage;
- three simultaneous initial native slots, followed by independent overview and triage reviewers as slots free;
- no production scheduler/schema modification;
- no source generation for create-key or delete-key in this pilot;
- disagreement on delete-key promotes its future disposition to `source_required` without a retry loop;
- related raw links cannot support overview facts;
- the existing dispatch-confirm discipline remains intact.

- [ ] **Step 5: Replace the superseded six-ingest manifest**

Write a pilot-specific `manifest.json` with `schema_version: 1`, `pilot_id: metronome-campaign-12`, `mode: selective_ingest_pilot`, and these exact page decisions:

| Job ID | SHA-256 | Initial disposition | Pilot action |
| --- | --- | --- | --- |
| `custom-fields-overview` | `5b984cff905793cfa4eb52dbf683585387559ffaa92c1aa54fa9c84d49b3859c` | `source_required` | `generate_source` |
| `create-custom-field-key` | `54ffdb826b8aeddafd3226aa1e7e3b8b6ca41835ea27cddefdcf478daf9e5231` | `raw_reference` | `audit_raw_reference` |
| `delete-custom-field-key` | `271549e978d195fc8294289cf7343257c3f2c9fac6554c40b7e6f19d7af62e10` | `semantic_triage` | `review_triage` |
| `list-custom-field-keys` | `f0f16c6ed70865d5bb56e8c42fe109329d05e153c1b70949ff55447d5fbd3f38` | `raw_reference` | `navigation_only` |
| `set-custom-field-values` | `f19ec0dbbbd9032d441099f33f9b3df8a8eb417fd7dc6ec34e8036614e100b64` | `semantic_triage` | `record_only` |
| `delete-custom-fields` | `994543f4191b3314347139ee1a83c3f60208bca242219b43850a95143e831a9b` | `semantic_triage` | `record_only` |

Each entry also contains its existing exact `canonical_url`, `raw_path`, the overview `source_target` or overview `anchor_source`, a non-empty reason, and `model_tier: strong` only for the three executed samples. Add `execution_sample_ids` in this exact order:

```json
[
  "custom-fields-overview",
  "create-custom-field-key",
  "delete-custom-field-key"
]
```

Do not include production `worker_concurrency`, `review_concurrency`, or `audit_job_ids`; this file is never passed to `manage_ingest_pilot.py`.

- [ ] **Step 6: Rewrite the selection review as an approval gate**

Set `Status: pending exact-manifest approval`. Include the six classifications, the maximum five complete reads, the three fixed quality queries, the no-expansion rule, and this boundary:

```text
Approval authorizes only the three selected pilot tasks. It does not authorize
source generation for the five endpoint pages, initialize the production
campaign scheduler, or create the cross-provider routing registry.
```

- [ ] **Step 7: Mechanically verify the proposal**

Run a read-only Python check that asserts:

- six unique canonical URLs and job IDs;
- three exact execution samples;
- every raw path exists and matches its SHA-256;
- the overview source target is absent;
- all six pages are selected English canonical pages in `inventory-current.json`;
- two `raw_reference`, three `semantic_triage`, and one `source_required` dispositions.

Run:

```bash
git diff --check -- rules/ingest.md rules/query-and-synthesis.md rules/lint.md rules/psp/metronome.md
python3 -m unittest tests.test_metronome_capsule -v
```

Expected: the proposal check prints one PASS line, diff check is silent, and focused tests pass.

- [ ] **Step 8: Commit the pending exact proposal**

```bash
git add rules/ingest.md rules/query-and-synthesis.md rules/lint.md rules/psp/metronome.md tracking/ingest/metronome/metronome-campaign-12/manifest.json tracking/ingest/metronome/metronome-campaign-12/selection-review.md
git commit -m "docs: propose Metronome selective ingest pilot"
```

- [ ] **Step 9: Stop for exact-manifest approval**

Report the committed proposal and request explicit user approval. Do not create `monitor.md`, agent orders, attempts, source candidates, or canonical wiki changes before that approval.

---

### Task 3: Initialize the Approved Three-Task Monitor

**Files:**
- Modify: `tracking/ingest/metronome/metronome-campaign-12/selection-review.md`
- Create: `tracking/ingest/metronome/metronome-campaign-12/monitor.md`

**Interfaces:**
- Consumes: explicit approval of the exact Task 2 manifest.
- Produces: one coordinator-owned execution monitor with three task states and one campaign start time.

- [ ] **Step 1: Verify the approval and immutable inputs**

Re-run the Task 2 proposal check. Stop if any hash, canonical URL, raw path, source-target absence, or sample ID differs from the approved manifest.

- [ ] **Step 2: Mark selection approval**

Change only the selection-review status to `approved`. Do not mutate the approved manifest.

- [ ] **Step 3: Create the three-row monitor**

Use this state vocabulary:

```text
pending -> running -> candidate_ready/reviewing -> approved/failed
```

The monitor header records:

```text
Pilot state: running
Started at: the exact output of `date -u +"%Y-%m-%dT%H:%M:%SZ"` captured at initialization
Completed at: pending
Complete raw reads: 0
Canonical sources promoted: 0
```

Rows are exactly `custom-fields-overview`, `create-custom-field-key`, and `delete-custom-field-key`. Record native agent IDs only after dispatch returns them.

- [ ] **Step 4: Validate and commit initialization**

Run `git diff --check`, verify no `attempts/` or wiki source exists, then commit:

```bash
git add tracking/ingest/metronome/metronome-campaign-12/selection-review.md tracking/ingest/metronome/metronome-campaign-12/monitor.md
git commit -m "chore: initialize Metronome selective ingest pilot"
```

---

### Task 4: Run the Three Initial Sol Tasks

**Files:**
- Create: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-1/candidate.md`
- Create: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-1/receipt.json`
- Create: `tracking/ingest/metronome/metronome-campaign-12/attempts/create-custom-field-key/attempt-1/audit.json`
- Create: `tracking/ingest/metronome/metronome-campaign-12/attempts/delete-custom-field-key/attempt-1/decision.json`
- Modify: `tracking/ingest/metronome/metronome-campaign-12/monitor.md`

**Interfaces:**
- Consumes: approved manifest rows, exact raw paths/hashes, source schema, current Metronome concepts, and isolated `/private/tmp/metronome-campaign-12/{job_id}/attempt-1/` output directories.
- Produces: one grounded overview candidate/receipt, one raw-reference audit, and one semantic-triage decision; no canonical wiki writes.

- [ ] **Step 1: Dispatch the overview worker**

The Sol worker reads only `raw/metronome/api-reference/custom-fields-2026-07-13.md` completely. It returns `candidate.md` and a receipt with exactly:

```json
{
  "job_id": "custom-fields-overview",
  "raw_path": "raw/metronome/api-reference/custom-fields-2026-07-13.md",
  "raw_sha256": "5b984cff905793cfa4eb52dbf683585387559ffaa92c1aa54fa9c84d49b3859c",
  "canonical_url": "https://docs.metronome.com/api-reference/custom-fields",
  "complete_read": true,
  "related_raw_paths": [
    "raw/metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13.md",
    "raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md",
    "raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13.md",
    "raw/metronome/api-reference/custom-fields/list-custom-field-keys-2026-07-13.md",
    "raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13.md"
  ],
  "shared_update_plan": []
}
```

The receipt also contains `grounding_quotes`, an array of three to five objects. Each object has a non-empty byte-matching `text`, a `location` formatted as `lines N-M`, and a non-empty `supports` value naming the candidate claim. The candidate lists the overview raw only in `raw_files` and `## Raw Sources`; it lists all five endpoint pages under `## Related raw API references` with `not summarized` labels and makes no endpoint-specific claim.

Confirm native dispatch returned an agent ID, then update the monitor to `running`.

- [ ] **Step 2: Dispatch the raw-reference auditor**

The Sol auditor reads only `create-a-custom-field-key-2026-07-13.md` completely and returns:

```json
{
  "job_id": "create-custom-field-key",
  "raw_path": "raw/metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13.md",
  "raw_sha256": "54ffdb826b8aeddafd3226aa1e7e3b8b6ca41835ea27cddefdcf478daf9e5231",
  "complete_read": true,
  "classification": "raw_reference",
  "missed_durable_facts": [],
  "grounding_quotes": []
}
```

The returned artifact replaces the empty example quote array with three to five byte-matching quote objects and adds non-empty `reason` and `risk` strings grounded in the complete page. `classification` may instead be `source_required`; that is a recorded pilot miss, not authorization to generate a source. Confirm the agent ID before updating the monitor.

- [ ] **Step 3: Dispatch the semantic-triage worker**

The Sol worker reads only `delete-a-custom-field-key-2026-07-13.md` completely and returns:

```json
{
  "job_id": "delete-custom-field-key",
  "raw_path": "raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md",
  "raw_sha256": "271549e978d195fc8294289cf7343257c3f2c9fac6554c40b7e6f19d7af62e10",
  "complete_read": true,
  "decision": "source_required",
  "grounding_quotes": []
}
```

The returned artifact replaces the empty example quote array with three to five byte-matching quote objects and adds a non-empty `reason` grounded in the complete page. `decision` may be `source_required` or `raw_reference`. Confirm the agent ID before updating the monitor.

- [ ] **Step 4: Validate each returned artifact before repository copy**

For each output, verify exact raw hash, canonical identity, complete-read flag, allowed enum, three to five byte-matching non-empty quotes, and no repository writes by the agent. For the overview candidate, also verify frontmatter target, exact `raw_files`, exact `Raw Sources`, five related links, and absence of endpoint-derived claims.

Copy only validated artifacts from `/private/tmp` into the paths listed above. Mark create-key `approved` after its audit is validated; mark overview `candidate_ready` and delete-key `candidate_ready` for review. Set `Complete raw reads: 3`.

- [ ] **Step 5: Commit initial evidence**

```bash
git add tracking/ingest/metronome/metronome-campaign-12/attempts tracking/ingest/metronome/metronome-campaign-12/monitor.md
git commit -m "test: record Metronome selective ingest samples"
```

---

### Task 5: Run the Two Independent Sol Reviews

**Files:**
- Create: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-1/review.json`
- Create on first correction only: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-2/candidate.md`
- Create on first correction only: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-2/receipt.json`
- Create on first correction only: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-2/review.json`
- Create on second correction only: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-3/candidate.md`
- Create on second correction only: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-3/receipt.json`
- Create on second correction only: `tracking/ingest/metronome/metronome-campaign-12/attempts/custom-fields-overview/attempt-3/review.json`
- Create: `tracking/ingest/metronome/metronome-campaign-12/attempts/delete-custom-field-key/attempt-1/review.json`
- Modify: `tracking/ingest/metronome/metronome-campaign-12/monitor.md`

**Interfaces:**
- Consumes: Task 4 candidate/receipt/decision and the exact corresponding raw page.
- Produces: one complete source review and one complete classification review by agents different from the initial workers.

- [ ] **Step 1: Dispatch the overview reviewer**

The reviewer reads the overview raw completely, checks all candidate claims and grounding quotes, confirms the five navigation-only links are not evidence, checks concept/shared suggestions and contradictions, and returns:

```json
{
  "job_id": "custom-fields-overview",
  "review_scope": "full",
  "complete_raw_read": true,
  "reviewer_is_distinct": true,
  "verdict": "approved",
  "required_changes": [],
  "related_raw_used_as_evidence": false,
  "notes": "approved after complete raw and candidate review"
}
```

If required changes are bounded wording/link/frontmatter issues, issue at most the existing three-attempt correction path and targeted unchanged-hash review. A factual or uncertain change gets complete rereview. Do not let a review read any endpoint raw page.

- [ ] **Step 2: Dispatch the triage reviewer**

A different Sol reviewer reads the delete-key raw completely and returns:

```json
{
  "job_id": "delete-custom-field-key",
  "review_scope": "full_classification",
  "complete_raw_read": true,
  "reviewer_is_distinct": true,
  "decision": "source_required",
  "agrees_with_worker": true,
  "grounding_quotes": []
}
```

The returned artifact replaces the empty example quote array with three to five byte-matching quote objects and adds a non-empty independent `reason`. The decision enum is `source_required` or `raw_reference`. If it disagrees with the worker, record final disposition `source_required`; do not retry classification and do not generate the endpoint source in this pilot.

- [ ] **Step 3: Validate, copy, and close review states**

Verify both reviewers are different agents, both raw hashes are unchanged, all new quotes byte-match, and all required fields are present. Copy validated reviews into the repository attempt paths. Mark overview `approved` only after an approved final candidate; mark delete-key `approved` after recording its deterministic final disposition. Set `Complete raw reads: 5` when both complete reviews finish.

- [ ] **Step 4: Commit review evidence**

```bash
git add tracking/ingest/metronome/metronome-campaign-12/attempts tracking/ingest/metronome/metronome-campaign-12/monitor.md
git commit -m "test: review Metronome selective ingest decisions"
```

---

### Task 6: Promote the Overview and Close the Pilot Once

**Files:**
- Create: `wiki/concepts/metronome/metronome-custom-fields.md`
- Create: `wiki/sources/metronome/source-metronome-api-reference-custom-fields.md`
- Modify: `wiki/companies/metronome.md`
- Modify: `wiki/metronome-index.md`
- Modify: `wiki/metronome-log.md`
- Create: `tracking/ingest/metronome/metronome-campaign-12/quality-audit.md`
- Modify: `tracking/ingest/metronome/metronome-campaign-12/monitor.md`

**Interfaces:**
- Consumes: final approved overview candidate, raw-reference audit, semantic-triage worker/reviewer decision, and the immutable six-page manifest.
- Produces: one canonical overview source, one fact-bearing platform concept, consolidated company/index/log updates, terminal pilot evidence, and a decision on whether broader routing implementation is safe.

- [ ] **Step 1: Derive the two classification outcomes**

Set create-key final disposition to its auditor's `classification`. Set delete-key final disposition to `source_required` when either worker or reviewer chose it; otherwise set it to `raw_reference`. Record both in `quality-audit.md`; do not mutate the approved manifest.

If create-key is `source_required`, set pilot verdict to `revise_routing_rule`. Continue promoting the independently approved overview, but do not authorize cross-provider rollout. If it remains `raw_reference`, the false-negative sample passes.

- [ ] **Step 2: Apply the concept audit before source promotion**

Create `metronome-custom-fields.md` from overview evidence only with standard concept frontmatter, definition, durable overview facts, explicit limits of the overview, the overview source wikilink, and related Metronome concept links. Do not include create/list/set/delete endpoint methods, schemas, or behavior.

- [ ] **Step 3: Promote the byte-identical approved overview candidate**

Write the reviewer-approved candidate unchanged to `source-metronome-api-reference-custom-fields.md`. It must contain:

- canonical URL `https://docs.metronome.com/api-reference/custom-fields`;
- only `metronome/api-reference/custom-fields-2026-07-13.md` in `raw_files` and `## Raw Sources`;
- all five path-qualified endpoint snapshots under `## Related raw API references`, each labelled `raw reference; not summarized`;
- `[[metronome]]` and `[[metronome-custom-fields]]` links;
- no endpoint-specific fact unsupported by the overview raw.

- [ ] **Step 4: Apply the consolidated mechanical shared updates**

Add exactly one source catalog link to the Metronome company and provider index, append one Campaign 12 log entry, and derive counts from disk. With exactly one promoted source, the expected corpus is 91 source summaries and 134 raw pages without source summaries; use derived counts rather than hardcoding them before promotion. Replace “pending ingest” wording in touched Metronome coverage text with “raw pages without source summaries” so raw-only pages are not presented as a backlog that must reach zero.

- [ ] **Step 5: Run the three fixed query-quality checks**

Record answer, evidence route, and pass/partial/fail for:

1. `What are Metronome Custom Fields and what role does the overview document establish?` — must answer from the overview source.
2. `What exact request fields are needed to create a custom-field key?` — must route to and completely read create-key raw; the overview must not supply the schema.
3. `What happens to existing values when a custom-field key is deleted?` — must route to delete-key raw and state only what that raw supports.

A material partial/fail is an answer-critical missing or incorrect fact, boundary, evidence route, or unsupported overview inference. It does not expand into reading the other three pages; it sets the pilot verdict to `revise`.

- [ ] **Step 6: Run the single close validation set**

Run targeted wiki validation on the source, concept, and company page:

```bash
python3 scripts/validate_wiki.py wiki/sources/metronome/source-metronome-api-reference-custom-fields.md wiki/concepts/metronome/metronome-custom-fields.md wiki/companies/metronome.md
```

Run capsule validation:

```bash
python3 scripts/validate_metronome_capsule.py
```

Expected after one overview promotion: `225 raw, 91 sources, 134` raw pages without source summaries and no structural error.

Because code and rules changed, run the full unit suite once:

```bash
python3 -m unittest discover -s tests
```

Expected: all tests pass. Do not repeat the suite unless a failing test requires a code correction.

- [ ] **Step 7: Finalize terminal evidence**

Write `quality-audit.md` with:

- final verdict `approve_selective_routing` or `revise_routing_rule`;
- five expected complete reads plus any explicitly justified source retry reads;
- create-key and delete-key final dispositions and evidence paths;
- overview candidate/source byte identity;
- evidence/navigation separation checks;
- three query results;
- validator commands/results;
- explicit statement that list-key, set-values, and delete-fields raw bodies were not read;
- recommendation to write a separate cross-provider routing/migration plan only after an approving verdict.

Update the monitor to terminal `complete`, set `completed_at`, final complete-read count, one promoted source, three approved tasks, and zero unresolved running states.

- [ ] **Step 8: Verify the final diff and commit only pilot files**

Run:

```bash
git diff --check
git status --short
```

Verify `CLAUDE copy.md` and unrelated changes are not staged. Stage only files named in Tasks 1–6 that remain uncommitted, then commit:

```bash
git commit -m "docs: complete Metronome selective ingest pilot"
```

- [ ] **Step 9: Report the bounded next decision**

If the verdict is `approve_selective_routing`, recommend a separate implementation plan for the provider routing registry, periodic navigation refresh, and incremental legacy migration. If the verdict is `revise_routing_rule`, report the exact classification miss and propose one bounded rule correction before another small Metronome sample. Do not automatically start either path.
