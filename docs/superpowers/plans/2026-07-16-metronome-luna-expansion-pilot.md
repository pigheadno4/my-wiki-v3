# Metronome Luna Expansion Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Validate Luna as the extraction tier on five new heterogeneous Metronome pages while keeping Sol responsible for concept synthesis, contradiction review, shared indexes/logs, and final approval.

**Architecture:** Each Luna worker receives one immutable raw page in an isolated minimal directory and writes only evidence artifacts. The coordinator then reads that complete raw page, audits existing concepts, reviews the Luna evidence, repairs the canonical source, validates the entire cycle, and commits it before the next page starts. Terra is parked because it failed the 900-second same-page throughput gate.

**Tech Stack:** Python 3.9 standard library, `unittest`, JSON Schema, Markdown/YAML frontmatter, Obsidian wikilinks, Git worktrees, Codex CLI with GPT-5.6 Luna high reasoning, and GPT-5.6 Sol review.

## Global Constraints

- Follow `CLAUDE.md` and `rules/ingest.md`: one source at a time, complete full-file read and concept audit before source creation, and finish the entire cycle before starting another page.
- Never modify `raw/metronome/`.
- Luna writes only its assigned `tracking/ingest/metronome/pilot/runs/<job-id>/` directory.
- Sol alone may edit canonical sources, concepts, company pages, indexes, logs, or final receipts.
- Every source must include the dated raw snapshot in `raw_files:` and a path-qualified backlink under `## Raw Sources`.
- Tags must be lowercase kebab-case and include `metronome`.
- Suggested existing concepts must match the current `wiki/concepts/metronome/*.md` inventory; new concept candidates remain recommendations for Sol and never create pages automatically.
- Repair deterministic tag, raw-link, and uniquely locatable quote-bound defects locally without a model retry.
- Preserve every attempt, failure reason, elapsed time, repair count, and available token usage.
- Do not promote a page with a critical omission, unsupported claim, unresolved contradiction, invalid raw link, or failed validator.
- Preserve unrelated user files and changes.

## Fixed Corpus and Order

| Cycle | Page type | Raw path | Lines |
| ---: | --- | --- | ---: |
| 1 | Long conceptual/financial guide | `raw/metronome/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition-2026-07-13.md` | 555 |
| 2 | Pricing concept guide | `raw/metronome/guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13.md` | 267 |
| 3 | Integration workflow | `raw/metronome/integrations/invoice-integrations/stripe-2026-07-13.md` | 331 |
| 4 | API reference | `raw/metronome/api-reference/billable-metrics/create-a-billable-metric-2026-07-13.md` | 342 |
| 5 | Long schema-heavy API reference | `raw/metronome/api-reference/contracts/edit-a-contract-2026-07-13.md` | 4,532 |

Expected successful coverage after all five cycles: 10 source summaries ingested and 215 documentation pages pending.

---

### Task 1: Harden Luna Taxonomy Validation

**Files:**
- Modify: `tests/test_run_metronome_model_worker.py`
- Modify: `tests/test_metronome_ingest_pilot.py`
- Modify: `scripts/run_metronome_model_worker.py`
- Modify: `scripts/metronome_ingest_pilot.py`
- Modify: `tracking/ingest/metronome/pilot/prompts/source-summary-v3.md`

**Interfaces:**
- Consumes: schema-version-3 `suggested_tags` and `suggested_metronome_concepts`.
- Produces: deterministic lowercase kebab-case tag repair and validation against existing Metronome concept slugs.

- [x] Write failing tests proving `Usage Events`, `usage_events`, uppercase duplicates, empty tags, and invalid punctuation normalize to unique lowercase kebab-case tags while preserving `metronome`.
- [x] Run `python3 -m unittest tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v`; confirm the new tests fail for missing normalization/inventory enforcement.
- [x] Implement minimal normalization and inventory validation. Existing concept slugs come from `wiki/concepts/metronome/*.md`; unknown values must be reported for Sol rather than silently accepted as existing concepts.
- [x] Update the worker prompt to require concise quotes, one final JSON object, lowercase kebab-case tags, and reuse of supplied existing concept slugs.
- [x] Run focused tests, `python3 -m unittest discover -s tests -v`, and `PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m py_compile scripts/run_metronome_model_worker.py scripts/metronome_ingest_pilot.py`.
- [x] Commit with message `fix: harden luna taxonomy validation`.

### Task 2: Define the Five Luna Jobs and Manifest

**Files:**
- Create: five Luna job JSON files in `tracking/ingest/metronome/pilot/jobs/`
- Create: `tracking/ingest/metronome/pilot/luna-expansion-manifest.md`

**Interfaces:**
- Consumes: version-3 job validator and the fixed corpus above.
- Produces: reproducible Luna/high jobs whose only allowed write path is their own run directory.

- [ ] Create one `real_ingest` Luna/high job for each fixed-corpus page with exact canonical URL, raw path, source target, artifact directory, and forbidden shared files.
- [ ] Record fixed order, page type, acceptance gates, 900-second fail-fast limit, and the rule that no later cycle starts before the current canonical commit.
- [ ] Validate every job with `python3 scripts/validate_metronome_ingest.py --job <path>`.
- [ ] Commit with message `docs: define luna expansion jobs`.

### Task 3: Cycle 1 - ASC 606 Revenue Recognition

**Files:**
- Create: Luna run artifacts and final receipt for the ASC 606 job
- Create: `wiki/sources/metronome/source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition.md`
- Update as required: `wiki/concepts/metronome/*.md`, `wiki/companies/metronome.md`, `wiki/metronome-index.md`, `wiki/metronome-log.md`, `wiki/log.md`

- [ ] Read all 555 raw lines and record 3-5 exact grounding quotes.
- [ ] Complete and record the concept audit before creating the source.
- [ ] Run the Luna worker and preserve its receipt, output, and draft.
- [ ] Have Sol review every material section, correct taxonomy and claims, check contradictions, and promote only the approved canonical page.
- [ ] Validate touched pages, the final receipt, and capsule reconciliation at 6 ingested / 219 pending.
- [ ] Commit the complete cycle.

### Task 4: Cycle 2 - Enterprise Commit

- [ ] Read all 267 raw lines and finish the concept audit before source creation.
- [ ] Run Luna, then have Sol verify commit logic, timing, drawdown, rollover, limits, and scope boundaries.
- [ ] Promote the corrected source with its raw backlink; update required concept/company/index/log files and final receipt.
- [ ] Validate and reconcile at 7 ingested / 218 pending, then commit the complete cycle.

### Task 5: Cycle 3 - Stripe Invoice Integration

- [ ] Read all 331 raw lines and finish the concept audit before source creation.
- [ ] Run Luna, then have Sol verify prerequisites, ownership boundaries, invoice flow, configuration, limitations, and warnings.
- [ ] Promote the corrected source with its raw backlink; update required concept/company/index/log files and final receipt.
- [ ] Validate and reconcile at 8 ingested / 217 pending, then commit the complete cycle.

### Task 6: Cycle 4 - Create a Billable Metric

- [ ] Read all 342 raw lines and finish the concept audit before source creation.
- [ ] Run Luna, then have Sol verify method/path semantics, required and conditional fields, mutually exclusive alternatives, feature gates, responses, and inconsistencies.
- [ ] Promote the corrected source with its raw backlink; update required concept/company/index/log files and final receipt.
- [ ] Validate and reconcile at 9 ingested / 216 pending, then commit the complete cycle.

### Task 7: Cycle 5 - Edit a Contract

- [ ] Read all 4,532 raw lines and finish the concept audit before source creation.
- [ ] Run Luna, then have Sol verify operation families, nested schemas, conditional and mutually exclusive fields, feature gates, responses, and documentation inconsistencies.
- [ ] Promote the corrected source with its raw backlink; update required concept/company/index/log files and final receipt.
- [ ] Validate and reconcile at 10 ingested / 215 pending, then commit the complete cycle.

### Task 8: Pilot Report and Routing Decision

**Files:**
- Create: `tracking/ingest/metronome/pilot/luna-expansion-pilot-report.md`
- Update if warranted: `wiki/metronome-index.md` and the linked Metronome ingest workflow

- [ ] Aggregate all five jobs with elapsed time, attempts, input/cached/output/reasoning tokens, deterministic repairs, semantic Sol repairs, and review minutes.
- [ ] Compare page types for omissions, unsupported claims, evidence quality, taxonomy errors, and canonical repair burden.
- [ ] Choose one explicit routing outcome: expand Luna, restrict Luna to selected page types, or stop cheap-model scaling.
- [ ] Run the full unit suite, compilation, `python3 scripts/validate_metronome_capsule.py`, and targeted wiki validation.
- [ ] Obtain a final whole-branch review and commit the report.
