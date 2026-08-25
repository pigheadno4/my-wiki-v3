# Metronome Minimum Sufficient Source Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Operationalize the Minimum Sufficient Source contract for one bounded five-page Metronome Campaign 23 and measure whether it improves first-pass acceptance without weakening complete independent review.

**Architecture:** Keep the current Campaign v2 scheduler, result schemas, strong-model workers, independent strong-model reviewers, coordinator-only writes, and close validators. Add only a Metronome-local pilot rule, a small provider lessons file, and a campaign-local playbook/manifest; encode non-blocking reviewer notes in the existing review `reason` instead of adding state or schema fields.

**Tech Stack:** Markdown operating rules and campaign evidence, JSON Campaign v2 manifest, Python `manage_ingest_pilot.py`, native Codex subagents, `unittest`, existing wiki/capsule validators, and Git.

**Spec:** `docs/superpowers/specs/2026-08-25-minimum-sufficient-source-ingest-design.md`

## Global Constraints

- Collect and preserve all canonical English raw pages; workers and first reviewers read their assigned raw page completely.
- Keep the existing `source_required`, `raw_reference`, and `semantic_triage` routing dispositions; do not add a fourth state.
- A source is a query router, raw is complete evidence, and concepts hold cross-source durable synthesis.
- The semantic ranges of three to seven core facts, one to three material boundaries, and one to three primary concepts are guidance, never validator-enforced caps.
- Only material factual, authority, contradiction, primary-concept, or evidence-navigation defects block approval.
- Secondary concepts, formatting, wording, bounded quote ranges, and mechanical shared-file work do not consume a worker retry.
- Every first attempt keeps independent complete-source strong-model review; only an unchanged-hash bounded correction receives diff review.
- The coordinator is the only repository writer and performs no default third complete raw read.
- Do not change `scripts/ingest_pilot/`, its schemas, its validators, or its scheduler unless execution exposes a reproducible defect that blocks the approved pilot and the user separately approves that repair.
- Do not bulk-rewrite existing sources, change another provider, start reviewer sampling, or create telemetry, a registry, a scoring system, or a new monitoring layer.
- Incremental migration, periodic-update adoption, reviewer sampling, and cross-provider rollout remain conditional follow-ups from the approved design; Campaign 23 measures the prerequisite before any of them receives an implementation plan.
- Campaign 23 preparation and execution are separate gates. Commit the exact manifest and stop for explicit user approval before `init` or any complete raw read.
- Do not reuse candidate or review evidence from a closed negative campaign. `packages-overview` was queued but had no attempt directory in Campaign 13; Campaign 23 treats it as a fresh per-page-review job.
- Preserve unrelated working-tree files, including `CLAUDE copy.md`.

## File Map

- Modify `rules/psp/metronome.md`: authorize only the approved Campaign 23 profile and define worker, reviewer, retry, and close behavior without changing global PSP behavior.
- Create `tracking/ingest/metronome/lessons.md`: coordinator-owned repeated process lessons, organized by the five archetypes.
- Create `tracking/ingest/metronome/metronome-campaign-23/minimum-sufficient-source-playbook.md`: exact worker/reviewer source contract and five overlay checklists.
- Create `tracking/ingest/metronome/metronome-campaign-23/manifest.json`: exact five-page Campaign v2 manifest, still uninitialized.
- Create `tracking/ingest/metronome/metronome-campaign-23/selection-review.md`: metadata-only selection evidence, audit sample, success gate, and authorization boundary.
- Generate after manifest approval through the existing coordinator: `campaign.json`, `jobs.json`, `monitor.md`, `events.jsonl`, and per-attempt evidence under `tracking/ingest/metronome/metronome-campaign-23/`.
- Promote after per-page approval only: five canonical pages under `wiki/sources/metronome/`, reviewer-approved primary concept changes, one company/index/log update, and calculated counts.
- Create at close `tracking/ingest/metronome/metronome-campaign-23/quality-audit.md` and `retrospective.md`.

---

### Task 1: Add the provider-local pilot operating rule

**Files:**
- Modify: `rules/psp/metronome.md`
- Test: existing `tests/test_ingest_pilot_*.py` and full unit suite

**Interfaces:**
- Consumes: the approved design and unchanged Campaign v2 review/result contract.
- Produces: a Campaign 23-only authorization that workers, reviewers, and the coordinator can follow without a new JSON field.

- [ ] **Step 1: Add the Campaign 23 section to the provider rule**

Append one section named `## Campaign 23 Minimum Sufficient Source pilot authorization` with these exact operational rules:

```markdown
## Campaign 23 Minimum Sufficient Source pilot authorization

Campaign 23 is a bounded five-page Metronome-only pilot and may be initialized
only after its exact manifest is explicitly approved. It changes source
granularity and the review blocking contract, not collection, routing,
scheduling, result schemas, model routing, or close validation.

Each strong-model worker reads the complete assigned raw page, the campaign
playbook, and only the matching section of
`tracking/ingest/metronome/lessons.md`. It produces one Minimum Sufficient
Source with an overview, query-critical durable facts, material boundaries or
contradictions, a raw-detail coverage map, primary concept routes, and the
exact path-qualified raw backlink. Numeric ranges in the playbook are semantic
guidance and are not hard caps.

A different strong-model reviewer reads the complete assigned raw page and
applies the same archetype overlay. `changes_requested` is limited to a core
factual error, a material omission that changes an integration decision, an
authority error, a missing material contradiction, a missing or incorrect
primary concept, a broken evidence route, or a coverage-map gap that hides an
entire detail category central to the page purpose.

Secondary concept gaps, ordinary schema details left in raw, non-material
wording or formatting, mechanically repairable quote ranges, and mechanical
company/index/log work are non-blocking. The reviewer returns `approved`,
records any such follow-up in the existing `reason`, and approves or rejects
the existing shared update IDs normally. Do not add a `coordinator_actions`
schema field.

Use targeted review only for an unchanged-hash bounded correction whose exact
scope was identified by the prior complete review. Core misunderstanding,
material omission, authority confusion, new factual meaning, or unresolved
contradiction receives a full semantic retry and complete review. Secondary
issues do not consume a worker attempt.

The coordinator accepts the reviewer verdict, performs bounded non-semantic
repairs, applies approved primary concept changes, verifies reciprocal links,
promotes canonical sources, and runs close checks. It does not perform a
default third complete raw read. Campaign close records first-pass approvals,
bounded retries, full semantic retries, attempts, elapsed time, query audit,
raw deep-dive success, and primary-concept reciprocity using existing files
only.

This authorization does not apply to Campaign 22 evidence, another provider,
reviewer sampling, a larger campaign, or bulk migration.
```

- [ ] **Step 2: Verify the rule contains the approved boundaries**

Run:

```bash
rg -n "Campaign 23 Minimum Sufficient Source|Do not add a.*coordinator_actions|Secondary concept gaps|default third complete raw read" rules/psp/metronome.md
```

Expected: four matches in the new Campaign 23 section and no edits to `rules/ingest.md`.

- [ ] **Step 3: Run the full test suite because a rule changed**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Expected: PASS. A pre-existing unrelated failure must be recorded and separated from this task; do not edit unrelated code to make the suite green.

- [ ] **Step 4: Commit the provider-local rule**

```bash
git add rules/psp/metronome.md
git commit -m "Authorize Metronome minimum source pilot"
```

### Task 2: Create the small lessons file and campaign playbook

**Files:**
- Create: `tracking/ingest/metronome/lessons.md`
- Create: `tracking/ingest/metronome/metronome-campaign-23/minimum-sufficient-source-playbook.md`

**Interfaces:**
- Consumes: Campaign 19 through 22 retrospectives/reviews and the provider-local Campaign 23 rule.
- Produces: one small provider checklist and one campaign-local source/review contract referenced by every trusted order.

- [ ] **Step 1: Create the provider lessons file**

Create exactly five archetype sections. Keep each lesson to one preventive check, evidence campaigns, and one boundary. Seed only the recurring patterns already observed:

```markdown
# Metronome ingestion lessons

This coordinator-owned file records repeated ingest-process failures, not
Metronome product facts. Add a lesson only after it appears on at least two
different pages. Workers and reviewers read only their assigned archetype
section. Replace or delete obsolete checks instead of accumulating variants.

## API Read

- Separate OpenAPI request-body requiredness from required properties inside a
  supplied payload. A required identifier in the payload does not prove the
  request body itself is required. Seen in Campaigns 19 and 22.

## API List / Schema

- Do not describe a documented property set as closed unless
  `additionalProperties: false` is explicit; unknown-property runtime behavior
  otherwise remains undocumented. Seen in Campaigns 19 and 20.

## API Mutation

- Check the API-wide POST idempotency authority before declaring repeated-call
  behavior wholly undocumented, while keeping endpoint-specific state,
  concurrency, and recovery unknowns separate. Seen in Campaigns 19 and 22.

## Concept / Guide

- A worked amount, transition, or example retained as a query-critical fact
  needs direct quote coverage; otherwise narrow the summary and route the
  worked detail to raw. Seen in Campaigns 21 and 22.

## Integration Guide

- Separate Metronome-documented configuration and identifiers from external
  acceptance, delivery, payment, settlement, or reconciliation guarantees.
  Seen in Campaigns 21 and 22.
```

- [ ] **Step 2: Create the campaign-local playbook**

Write this exact operating content; it is guidance over the unchanged Campaign v2 result schema:

```markdown
# Metronome Campaign 23 Minimum Sufficient Source playbook

## Purpose

This bounded playbook tests whether a source can remain a reliable query
router without reconstructing its complete raw page. Raw remains complete
evidence, source preserves query-critical durable knowledge and navigation,
and concepts preserve cross-source synthesis. This playbook adds no routing
state, schema field, validator, scheduler, or hard content-size limit.

## Minimum Sufficient Source contract

Every candidate preserves:

1. a concise overview of page purpose and scope;
2. the durable facts needed to select the page and avoid a materially wrong
   integration decision;
3. material boundaries or contradictions;
4. a coverage map routing detailed schemas, enums, examples, errors, SQL, or
   setup steps to the exact raw page;
5. primary concept links; and
6. canonical URL, `raw_files`, and an exact path-qualified raw backlink.

Three to seven facts, one to three boundaries, and one to three primary
concepts are normal semantic ranges, not acceptance caps. Include more only
when the page purpose requires it. Do not copy fields merely to fill a quota.

## Primary versus secondary concepts

A primary concept directly defines the page purpose, operation, lifecycle, or
integration outcome; omitting it would impair a realistic query. A secondary
concept represents an optional field, incidental schema surface, or tangential
capability that exact raw navigation can cover safely.

Workers must identify primary concepts. They may return secondary suggestions,
but a missing secondary concept does not fail the candidate or consume a retry.

## Coverage map and raw evidence boundary

The coverage map names detail categories present in the assigned raw; it does
not summarize every item. `Raw Sources` contains only pages read completely and
used as evidence. An unread navigation page belongs under
`Related raw API references` and cannot support a source claim.

## API Read overlay

Preserve object identity, lookup purpose, key locator, returned state,
time-view or history semantics, and material visibility or consistency
boundaries. Route complete schemas, nullable fields, examples, and error
catalogs to raw. Separate request-body requiredness from required properties
inside a supplied payload.

## API List / Schema overlay

Preserve collection scope, principal filters and pagination, documented
ordering or time windows, completeness limits, and material schema/example
conflicts. Route the full filter, cursor, enum, and object catalogs to raw. Do
not infer a closed schema without explicit `additionalProperties: false`.

## API Mutation overlay

Preserve preconditions, principal state transition, observable result, and
material lifecycle, financial, failure, propagation, retry, concurrency, or
idempotency semantics established by official authority. Route the full
payload and error catalog to raw. Keep API-wide POST idempotency distinct from
endpoint-specific state and recovery behavior.

## Concept / Guide overlay

Preserve the definition, principal actors, lifecycle or data flow, decision
points, material integration limits, and important conflicts. Route long
worked examples, variants, calculations, and operational walkthroughs to raw.
Do not elevate a product guide into legal, accounting, or compliance authority.

## Integration Guide overlay

Preserve the integration outcome, system boundary, responsibility split,
identity mapping, state or data flow, recovery behavior, and relevant
environment scope. Route detailed setup steps, UI paths, payloads, optional
settings, and troubleshooting to raw. Do not turn Metronome documentation into
a complete guarantee of the external platform.

## Worker submission check

Before returning the unchanged Campaign v2 result, confirm each core fact and
material boundary is accurate and grounded, every primary concept is routed,
the coverage map exposes central raw-detail categories, and the canonical/raw
links are exact. Quotes ground retained claims; they do not need to reproduce
every raw schema table.

## Reviewer blocking defects

Return `changes_requested` only for a core factual error; a material omission
affecting integration, amount, state, lifecycle, or failure treatment; an
authority error; a missing material contradiction; a missing or incorrect
primary concept; a broken evidence route; or a coverage-map omission hiding an
entire detail category central to page purpose.

## Reviewer non-blocking coordinator actions

Approve when remaining work is limited to a secondary concept, ordinary raw
detail, non-material wording/formatting, a mechanically repairable quote range,
or company/index/log work. Record the bounded follow-up in the existing review
`reason` and decide existing shared update IDs normally. Do not add a
`coordinator_actions` result field.

## Retry scope

Use targeted review only when the raw hash is unchanged and the complete prior
review enumerated a bounded local correction. Use full review for core
misunderstanding, material omission, authority confusion, new factual meaning,
or unresolved contradiction. Secondary issues do not consume an attempt.

## Pilot measurement

Record first-pass approvals, bounded and full retries, attempts, review scope,
elapsed time, fixed query results, exact raw deep dive, and primary-concept
reciprocity in existing campaign evidence. The five-page limit and comparison
with Campaigns 20 through 22 guide the decision; no measurement becomes a new
validator rule.
```

Under `Reviewer non-blocking coordinator actions`, explicitly say to use the existing approved review result with follow-up notes in `reason`; do not add output fields. Under `Pilot measurement`, state that the five-page sample and existing tracking fields are sufficient and that no threshold is a new validator rule.

- [ ] **Step 3: Verify lessons remain small and the playbook contains all five overlays**

Run:

```bash
test "$(rg -c '^## (API Read|API List / Schema|API Mutation|Concept / Guide|Integration Guide)$' tracking/ingest/metronome/lessons.md)" -eq 5
test "$(rg -c '^## (API Read|API List / Schema|API Mutation|Concept / Guide|Integration Guide) overlay$' tracking/ingest/metronome/metronome-campaign-23/minimum-sufficient-source-playbook.md)" -eq 5
test "$(wc -l < tracking/ingest/metronome/lessons.md)" -le 45
```

Expected: all three commands exit 0.

- [ ] **Step 4: Commit the lessons and playbook**

```bash
git add tracking/ingest/metronome/lessons.md tracking/ingest/metronome/metronome-campaign-23/minimum-sufficient-source-playbook.md
git commit -m "Add Metronome minimum source guidance"
```

### Task 3: Prepare the exact Campaign 23 manifest for approval

**Files:**
- Create: `tracking/ingest/metronome/metronome-campaign-23/manifest.json`
- Create: `tracking/ingest/metronome/metronome-campaign-23/selection-review.md`

**Interfaces:**
- Consumes: collection inventory, capsule pending list, the Campaign v2 manifest interface, and the campaign playbook.
- Produces: an immutable five-job proposal that can be initialized only after explicit approval.

- [ ] **Step 1: Reconfirm the metadata-only candidate set**

Use only inventory metadata, paths, line counts, hashes, prior campaign membership, and source-target absence. Do not read the raw bodies. The exact proposed set is:

| Job | Archetype | Lines | SHA-256 | Canonical `.md` URL |
| --- | --- | ---: | --- | --- |
| `get-a-contract-v2` | API Read | 3091 | `fc929b1ed102106ef829006f505ee630159f5c895aa65dbb80270202007bb48f` | `https://docs.metronome.com/api-reference/contracts/get-a-contract-v2.md` |
| `list-invoices` | API List / Schema | 1126 | `dfb113ebaffb31bf7fecd97329451c145ca5cb593cfaea1b080c6433b3dfb2be` | `https://docs.metronome.com/api-reference/invoices/list-invoices.md` |
| `void-a-credit-grant` | API Mutation | 166 | `c917e52bbe854ca7a0c0eef6eae037616a75af2edfa6fbb92b4a3ffc602bd3d8` | `https://docs.metronome.com/api-reference/credit-grants/void-a-credit-grant.md` |
| `packages-overview` | Concept / Guide | 193 | `5e26b9b02883832ed82dd64b805ec3751fb910bbc81f1e9d179f7881ec7b83ff` | `https://docs.metronome.com/guides/implement-metronome/core-concepts/packages-overview.md` |
| `azure` | Integration Guide | 261 | `a616695b72d172eb01c53970e0245c3d506e0b749909c2693c2b994265cb3f36` | `https://docs.metronome.com/integrations/marketplace-integrations/azure.md` |

Re-run `wc -l`, `shasum -a 256`, and source-target absence checks. Any mismatch stops preparation rather than silently updating the approved plan values.

- [ ] **Step 2: Write the exact Campaign v2 manifest**

Use:

```json
{
  "schema_version": 2,
  "campaign_id": "metronome-campaign-23",
  "provider": "metronome",
  "mode": "dry_run",
  "review_policy": "per_page",
  "worker_concurrency": 3,
  "review_concurrency": 3,
  "max_attempts": 3,
  "audit_job_ids": [
    "void-a-credit-grant",
    "get-a-contract-v2",
    "packages-overview"
  ],
  "jobs": [
    {
      "job_id": "get-a-contract-v2",
      "raw_path": "raw/metronome/api-reference/contracts/get-a-contract-v2-2026-07-13.md",
      "raw_sha256": "fc929b1ed102106ef829006f505ee630159f5c895aa65dbb80270202007bb48f",
      "source_target": "wiki/sources/metronome/source-metronome-api-reference-contracts-get-a-contract-v2.md",
      "canonical_url": "https://docs.metronome.com/api-reference/contracts/get-a-contract-v2.md",
      "recommended_worker_tier": "strong",
      "routing_reason": "API Read Minimum Sufficient Source pilot: preserve object identity, lookup and time-view semantics, material visibility or consistency boundaries, primary concepts, coverage map, and exact raw deep dive without transcribing the complete schema. Apply the Campaign 23 playbook and API Read lessons section."
    },
    {
      "job_id": "list-invoices",
      "raw_path": "raw/metronome/api-reference/invoices/list-invoices-2026-07-13.md",
      "raw_sha256": "dfb113ebaffb31bf7fecd97329451c145ca5cb593cfaea1b080c6433b3dfb2be",
      "source_target": "wiki/sources/metronome/source-metronome-api-reference-invoices-list-invoices.md",
      "canonical_url": "https://docs.metronome.com/api-reference/invoices/list-invoices.md",
      "recommended_worker_tier": "strong",
      "routing_reason": "API List / Schema Minimum Sufficient Source pilot: preserve collection scope, principal filters and pagination, material completeness or ordering limits, contradictions, primary concepts, coverage map, and raw deep dive without copying the field catalog. Apply the Campaign 23 playbook and API List / Schema lessons section."
    },
    {
      "job_id": "void-a-credit-grant",
      "raw_path": "raw/metronome/api-reference/credit-grants/void-a-credit-grant-2026-07-13.md",
      "raw_sha256": "c917e52bbe854ca7a0c0eef6eae037616a75af2edfa6fbb92b4a3ffc602bd3d8",
      "source_target": "wiki/sources/metronome/source-metronome-api-reference-credit-grants-void-a-credit-grant.md",
      "canonical_url": "https://docs.metronome.com/api-reference/credit-grants/void-a-credit-grant.md",
      "recommended_worker_tier": "strong",
      "routing_reason": "API Mutation Minimum Sufficient Source pilot: preserve preconditions, state transition, observable result, material lifecycle or financial effects, authority boundaries, primary concepts, coverage map, and raw deep dive. Apply the Campaign 23 playbook and API Mutation lessons section."
    },
    {
      "job_id": "packages-overview",
      "raw_path": "raw/metronome/guides/implement-metronome/core-concepts/packages-overview-2026-07-13.md",
      "raw_sha256": "5e26b9b02883832ed82dd64b805ec3751fb910bbc81f1e9d179f7881ec7b83ff",
      "source_target": "wiki/sources/metronome/source-metronome-guides-implement-metronome-core-concepts-packages-overview.md",
      "canonical_url": "https://docs.metronome.com/guides/implement-metronome/core-concepts/packages-overview.md",
      "recommended_worker_tier": "strong",
      "routing_reason": "Concept / Guide Minimum Sufficient Source pilot: preserve definition, actors, lifecycle or data flow, material decisions and conflicts, primary concepts, coverage map, and raw deep dive without copying every example. This is a fresh Campaign 23 job and must not reuse closed Campaign 13 state. Apply the Campaign 23 playbook and Concept / Guide lessons section."
    },
    {
      "job_id": "azure",
      "raw_path": "raw/metronome/integrations/marketplace-integrations/azure-2026-07-13.md",
      "raw_sha256": "a616695b72d172eb01c53970e0245c3d506e0b749909c2693c2b994265cb3f36",
      "source_target": "wiki/sources/metronome/source-metronome-integrations-marketplace-integrations-azure.md",
      "canonical_url": "https://docs.metronome.com/integrations/marketplace-integrations/azure.md",
      "recommended_worker_tier": "strong",
      "routing_reason": "Integration Guide Minimum Sufficient Source pilot: preserve system boundary, responsibility split, identifiers, lifecycle or data flow, external-platform limits, primary concepts, coverage map, and raw deep dive without copying all setup steps. Apply the Campaign 23 playbook and Integration Guide lessons section."
    }
  ]
}
```

- [ ] **Step 3: Write the selection review**

Record the metadata-only evidence, five source-target absence checks, the `packages-overview` Campaign 13 attempt-0 boundary, the three fixed audit jobs, comparative metrics, and this exact authorization boundary:

```text
Approval authorizes Campaign 23 initialization, complete reads of only these
five raw pages, strong-model workers, distinct complete-source strong-model
reviewers, bounded retries, reviewer-approved promotion, and fixed or expanded
close audit. It does not authorize a sixth page, reuse of Campaign 13 output,
reviewer sampling, another provider, bulk migration, remote push, or unrelated
file modification.
```

- [ ] **Step 4: Validate the proposal without initialization**

Run:

```bash
python3 -m json.tool tracking/ingest/metronome/metronome-campaign-23/manifest.json >/dev/null
python3 scripts/validate_metronome_capsule.py
test ! -e tracking/ingest/metronome/metronome-campaign-23/campaign.json
test ! -e tracking/ingest/metronome/metronome-campaign-23/jobs.json
git diff --check
```

Expected: JSON valid; capsule reports 225 raw, 132 sources, and 99 pending before Campaign 23; no initialized state exists; diff check passes.

- [ ] **Step 5: Commit the exact proposal**

```bash
git add tracking/ingest/metronome/metronome-campaign-23/manifest.json tracking/ingest/metronome/metronome-campaign-23/selection-review.md
git commit -m "Prepare Metronome Campaign 23 minimum source pilot"
```

- [ ] **Step 6: Stop at the manifest approval gate**

Report the five jobs, their archetypes, hashes, audit sample, rule/lessons commits, and exact manifest commit. Do not run `manage_ingest_pilot.py init` until the user explicitly approves this manifest.

### Task 4: Initialize Campaign 23 after explicit manifest approval

**Files:**
- Generate: `tracking/ingest/metronome/metronome-campaign-23/campaign.json`
- Generate: `tracking/ingest/metronome/metronome-campaign-23/jobs.json`
- Generate: `tracking/ingest/metronome/metronome-campaign-23/monitor.md`
- Generate: `tracking/ingest/metronome/metronome-campaign-23/events.jsonl`

**Interfaces:**
- Consumes: the exact user-approved manifest commit.
- Produces: trusted worker orders under per-job attempt directories; it does not authorize canonical writes before review.

- [ ] **Step 1: Confirm approval and clean scope**

Verify the user approved the exact Campaign 23 manifest and the manifest hash still matches the approved commit. Check `git status --short`; do not absorb unrelated changes.

- [ ] **Step 2: Initialize through the existing coordinator**

Run:

```bash
python3 scripts/manage_ingest_pilot.py init --manifest tracking/ingest/metronome/metronome-campaign-23/manifest.json
```

Expected: Campaign v2 state is created with five queued jobs, attempt 0, no worker/reviewer identity, and no canonical source write.

- [ ] **Step 3: Validate initialized state**

Run:

```bash
python3 scripts/manage_ingest_pilot.py status --campaign metronome-campaign-23
python3 -m json.tool tracking/ingest/metronome/metronome-campaign-23/campaign.json >/dev/null
python3 -m json.tool tracking/ingest/metronome/metronome-campaign-23/jobs.json >/dev/null
```

Expected: five queued jobs and an unstarted campaign with no attempt evidence fabricated.

- [ ] **Step 4: Commit initialized state**

```bash
git add tracking/ingest/metronome/metronome-campaign-23/campaign.json tracking/ingest/metronome/metronome-campaign-23/jobs.json tracking/ingest/metronome/metronome-campaign-23/monitor.md tracking/ingest/metronome/metronome-campaign-23/events.jsonl
git commit -m "Initialize Metronome Campaign 23"
```

### Task 5: Run five worker/reviewer cycles under the new contract

**Files:**
- Generate/update: `tracking/ingest/metronome/metronome-campaign-23/attempts/<job>/attempt-<n>/`
- Update: `tracking/ingest/metronome/metronome-campaign-23/{campaign.json,jobs.json,monitor.md,events.jsonl}`
- Temporary worker/review JSON: `/private/tmp/metronome-campaign-23-*.json`

**Interfaces:**
- Consumes: generated trusted orders, one raw page per worker, matching lessons section, campaign playbook, and existing authority pages.
- Produces: one independently approved candidate and shared suggestion set per job, or a durable failed/rejected record after the existing maximum attempts.

- [ ] **Step 1: Start no more than three native strong-model workers**

Use the existing dynamic slot rule. Each agent receives only its generated `input.json`, exact `/private/tmp` result path, campaign playbook path, and matching lessons section. Confirm each native spawn returns an agent ID before treating the job as active.

- [ ] **Step 2: Validate each worker result before state mutation**

For every result, run the current Campaign v2 worker-result validator through `manage_ingest_pilot.py run`. Reject invalid hash, URL, top-level contract, quote substring, backlink, or shared-update schema without manually normalizing the worker output.

- [ ] **Step 3: Dispatch a different strong-model full reviewer immediately when a candidate is ready**

The reviewer reads the complete raw and applies the blocking/non-blocking contract. When no blocking defect exists, verdict is `approved`; optional follow-up is written in the existing `reason`, and each shared update receives its normal decision. Reviewer identity must differ from worker identity.

- [ ] **Step 4: Classify every requested correction**

Use `targeted` only for an unchanged-hash bounded issue enumerated by the complete review. Use `full` for factual meaning, material omission, authority, primary-concept, contradiction, or evidence uncertainty. Do not retry a worker solely for a secondary concept, format, wording, ordinary schema detail, or mechanical catalog action.

- [ ] **Step 5: Continue the dynamic loop without batch barriers**

Release each completed worker/reviewer slot and fill it with a ready reviewer or queued worker according to `rules/psp/metronome.md`. One failed job does not pause unrelated jobs. Preserve attempt evidence and events after interruptions instead of reconstructing state.

- [ ] **Step 6: Verify terminal per-page evidence**

Expected for each approved job: current raw hash, candidate equals receipt source page, suggestions equal receipt suggestions, distinct worker/reviewer identities, approved shared decisions, exact canonical URL/raw backlink, and an approved final review. No canonical source is promoted before this check.

### Task 6: Promote approved content and close the pilot

**Files:**
- Create: the five manifest-declared `wiki/sources/metronome/*.md` targets that achieved approval
- Modify: reviewer-approved primary concept files under `wiki/concepts/metronome/`
- Modify: `wiki/companies/metronome.md`
- Modify: `wiki/metronome-index.md`
- Modify: `wiki/metronome-log.md`
- Update: Campaign 23 state/evidence files
- Create: `tracking/ingest/metronome/metronome-campaign-23/quality-audit.md`
- Create: `tracking/ingest/metronome/metronome-campaign-23/retrospective.md`
- Modify only if a lesson recurred again: `tracking/ingest/metronome/lessons.md`

**Interfaces:**
- Consumes: terminal approved candidates, reviewer-approved primary concept suggestions, and non-blocking coordinator notes.
- Produces: canonical query routers, reciprocal primary concept links, one shared close update, quality evidence, and a go/hold recommendation.

- [ ] **Step 1: Apply shared concept updates once per target**

Group only reviewer-approved durable facts and reciprocal links. Resolve duplicates and collisions at the target. Secondary concept notes may be applied if trivial and directly supported, or deferred in the retrospective; they never reopen the worker attempt.

After validating each updated concept, stage that exact approved target immediately rather than staging the concept directory:

```bash
case "$target" in
  wiki/concepts/metronome/*.md) git add -- "$target" ;;
  *) printf 'Refusing out-of-scope concept path: %s\n' "$target" >&2; exit 1 ;;
esac
```

- [ ] **Step 2: Promote canonical sources exactly from approved candidates**

Write each approved candidate to its manifest target. Apply only coordinator-owned mechanical corrections already recorded by the reviewer; if a correction changes factual meaning, return it to review instead of silently editing canonical content.

- [ ] **Step 3: Update shared catalogs once**

Add each promoted source exactly once to the Metronome company page and provider index, write one consolidated Campaign 23 log entry, and recompute `source_count` and provider totals mechanically.

- [ ] **Step 4: Run close validation once**

Run:

```bash
python3 scripts/validate_metronome_capsule.py
source_paths=(
  wiki/sources/metronome/source-metronome-api-reference-contracts-get-a-contract-v2.md
  wiki/sources/metronome/source-metronome-api-reference-invoices-list-invoices.md
  wiki/sources/metronome/source-metronome-api-reference-credit-grants-void-a-credit-grant.md
  wiki/sources/metronome/source-metronome-guides-implement-metronome-core-concepts-packages-overview.md
  wiki/sources/metronome/source-metronome-integrations-marketplace-integrations-azure.md
)
existing_sources=()
for path in "${source_paths[@]}"; do
  test ! -e "$path" || existing_sources+=("$path")
done
python3 scripts/validate_wiki.py "${existing_sources[@]}" \
  wiki/concepts/metronome/*.md wiki/companies/metronome.md \
  wiki/metronome-index.md wiki/metronome-log.md
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

Expected if all five promote: 225 raw, 137 sources, and 94 pending; all touched links/frontmatter pass; unit suite and diff check pass. If a job reaches durable failed/rejected status, calculate expected source and pending counts from the actual promoted total and record the difference rather than forcing five promotions.

- [ ] **Step 5: Run the fixed query audit**

Audit `void-a-credit-grant` as the short mutation, `get-a-contract-v2` as the longest/schema-heavy page, and `packages-overview` as the ordinary cross-structure sample. For each, test:

1. factual retrieval from source;
2. boundary or contradiction handling; and
3. exact raw deep dive.

Expand to all five only if any fixed query is partial/fail or a primary reciprocal link is missing.

- [ ] **Step 6: Write the retrospective and update lessons only on recurrence**

Record first-pass approvals, bounded retries, full semantic retries, total attempts, full versus targeted reviews, elapsed time, query results, raw deep-dive results, primary-concept reciprocity, reviewer defect attribution, and one line whose value matches `^- Coordinator repairs: [0-9]+$`. Compare directly with Campaigns 20 through 22. Add or revise a lesson only when the same process defect again meets the two-page recurrence rule.

- [ ] **Step 7: Complete the coordinator state**

Read the exact repair count recorded in the retrospective and pass the integer to the existing CLI:

```bash
repair_count=$(sed -n 's/^- Coordinator repairs: \([0-9][0-9]*\)$/\1/p' tracking/ingest/metronome/metronome-campaign-23/retrospective.md)
test -n "$repair_count"
python3 scripts/manage_ingest_pilot.py complete --campaign metronome-campaign-23 --coordinator-repairs "$repair_count"
```

Expected: completion succeeds only after terminal approval/rejection state and required close evidence are present.

- [ ] **Step 8: Commit the completed campaign**

Concept targets were staged individually in Step 1. Stage Campaign 23, catalogs/log, and the lessons file without staging either shared directory wholesale. Then stage each of the five exact source targets only when it exists, so a durable rejected job cannot turn into a pathspec error:

```bash
git add tracking/ingest/metronome/metronome-campaign-23 \
  wiki/companies/metronome.md wiki/metronome-index.md wiki/metronome-log.md \
  tracking/ingest/metronome/lessons.md

for path in \
  wiki/sources/metronome/source-metronome-api-reference-contracts-get-a-contract-v2.md \
  wiki/sources/metronome/source-metronome-api-reference-invoices-list-invoices.md \
  wiki/sources/metronome/source-metronome-api-reference-credit-grants-void-a-credit-grant.md \
  wiki/sources/metronome/source-metronome-guides-implement-metronome-core-concepts-packages-overview.md \
  wiki/sources/metronome/source-metronome-integrations-marketplace-integrations-azure.md
do
  test ! -e "$path" || git add -- "$path"
done

git commit -m "Complete Metronome Campaign 23 minimum source pilot"
```

- [ ] **Step 9: Report the rollout decision**

Recommend a second five-page Metronome pilot only if quality closes and efficiency materially improves. If quality passes without efficiency improvement, hold expansion and identify the remaining worker/reviewer contract defect. If quality declines, reject cross-provider rollout. Reviewer sampling remains a separate future design and is never inferred from Campaign 23 approval.
