# Metronome Terra Comparison Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. The user selected inline execution, so no sub-agents are needed for this pilot.

**Goal:** Determine whether GPT-5.6 Terra materially reduces Sol repair work while preserving query-grade accuracy by ingesting five new Metronome pages with Terra and running paired Luna shadows on the shortest and longest pages.

**Architecture:** Preserve the existing Luna/Sol pilot contracts as schema version 2 and add a backward-compatible schema-version-3, model-neutral worker contract. The runner stages only the assigned immutable raw page in a temporary directory, builds a deterministic page profile, requires claim-level evidence, corrects quote line locations locally when safe, and records every attempt plus cumulative token usage. Terra produces the five candidate drafts; Luna produces evidence-only paired shadows for two pages; Sol reads each complete raw page, performs the concept audit, repairs and promotes only the Terra draft, updates shared files, and signs the final receipt. Ingestion remains one page per complete cycle.

**Tech Stack:** Python 3.9 standard library, `unittest`, JSON Schema for Codex CLI structured output, Markdown/YAML frontmatter, Obsidian wikilinks, Git worktrees, Codex CLI using GPT-5.6 Terra at medium reasoning, GPT-5.6 Luna at high reasoning, and GPT-5.6 Sol for final review.

## Global Constraints

- Follow `CLAUDE.md` and `rules/ingest.md`; read one complete raw page and finish its whole ingest cycle before starting the next canonical page.
- Never modify `raw/metronome/`.
- Preserve schema-version-2 Luna jobs, outputs, receipts, and validators.
- Terra and Luna workers may write only their assigned run artifact directory; they never write canonical sources, concepts, indexes, or logs.
- Sol owns concept selection, contradiction review, canonical source content, shared files, and final approval.
- Each source page must link to its retained raw snapshot under `## Raw Sources`.
- Paired Luna jobs are `shadow` mode and must not change canonical coverage.
- Preserve every rejected attempt, validation reason, per-attempt usage, and cumulative usage.
- When quote text exists exactly and only its line bounds are wrong, repair the bounds deterministically without rerunning the model.
- Use a temporary minimal worker directory so repository instructions, plugins, and unrelated wiki files are not in the worker's working set.
- Preserve the unrelated untracked `CLAUDE copy.md`.

## Pilot Corpus and Order

| Cycle | Page | Raw path | Terra | Luna shadow |
| --- | --- | --- | --- | --- |
| 1 | Design usage events | `raw/metronome/guides/events/design-usage-events-2026-07-13.md` | yes | yes |
| 2 | Enterprise commit | `raw/metronome/guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13.md` | yes | no |
| 3 | Stripe invoice integration | `raw/metronome/integrations/invoice-integrations/stripe-2026-07-13.md` | yes | no |
| 4 | Create a billable metric | `raw/metronome/api-reference/billable-metrics/create-a-billable-metric-2026-07-13.md` | yes | no |
| 5 | Edit a contract | `raw/metronome/api-reference/contracts/edit-a-contract-2026-07-13.md` | yes | yes |

Expected successful coverage after five Terra promotions: 10 source pages and 215 pending raw pages.

---

### Task 1: Add the Model-Neutral Version-3 Contract

**Files:**
- Modify: `scripts/metronome_ingest_pilot.py`
- Modify: `scripts/validate_metronome_ingest.py`
- Modify: `tests/test_metronome_ingest_pilot.py`
- Modify: `tests/test_validate_metronome_ingest.py`
- Create: `tracking/ingest/metronome/pilot/schemas/model-output-v3.schema.json`

- [x] Write failing tests proving schema-version-3 jobs accept exactly `gpt-5.6-terra`/`medium` or `gpt-5.6-luna`/`high`, preserve the artifact-only write boundary, and reject any other model/reasoning pair.
- [x] Write failing tests for evidence-bearing takeaways and facts, `sections_covered`, `scope_boundaries`, `conditional_requirements`, `feature_gates`, `internal_inconsistencies`, `material_omissions`, and exact raw links.
- [x] Write failing tests requiring every takeaway and fact to cite one or more defined grounding quote IDs.
- [x] Implement version-3 job/output/worker/final receipt validation while leaving version 2 unchanged.
- [x] Add model-neutral CLI flags and labels without breaking the existing `--luna-output` path.
- [x] Run `python3 -m unittest tests.test_metronome_ingest_pilot tests.test_validate_metronome_ingest -v` and the full suite.

### Task 2: Harden the Worker Runner

**Files:**
- Create: `scripts/run_metronome_model_worker.py`
- Keep: `scripts/run_metronome_luna_worker.py` as the version-2 compatibility runner
- Modify: `scripts/metronome_ingest_pilot.py`
- Create: `tests/test_run_metronome_model_worker.py`
- Create: `tracking/ingest/metronome/pilot/prompts/source-summary-v3.md`

- [x] Write failing tests for job-selected model/reasoning, read-only Codex execution, a temporary minimal working directory containing only `raw.md`, and model-neutral artifact names.
- [x] Write failing tests for deterministic quote-bound repair: a uniquely matching exact quote receives corrected line bounds with zero retry; ambiguous or missing text still triggers the single allowed retry.
- [x] Write failing tests for immutable attempt records containing status, process exit code, validation errors, retry reason, rejected output path, individual token usage, and cumulative token usage.
- [x] Write failing tests proving cumulative usage sums all numeric usage fields across both attempts instead of retaining only the last attempt.
- [x] Implement a deterministic page profile with heading coverage for every page and OpenAPI endpoint/method, response-code, required-field, feature-gate, conditional, and mutually-exclusive hints when present.
- [x] Include the page profile in the prompt and require the worker to account explicitly for every profiled section or mark it as immaterial.
- [x] Render a model-neutral evidence draft while retaining the assigned raw deep link.
- [x] Run focused tests, the full suite, and Python compilation using `PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache`.

### Task 3: Define the Seven Reproducible Jobs

**Files:**
- Create: five Terra job JSON files under `tracking/ingest/metronome/pilot/jobs/`
- Create: two Luna-shadow job JSON files under the same directory
- Create: `tracking/ingest/metronome/pilot/terra-comparison-manifest.md`

- [ ] Record the exact model, reasoning, mode, raw path, target source, artifact directory, and forbidden shared files for each job.
- [ ] Record the fixed run order and acceptance thresholds in the manifest.
- [ ] Validate all seven jobs before any live model run.

### Task 4: Run Cycle 1 — Design Usage Events

**Files:**
- Create: paired Luna and Terra artifacts under `tracking/ingest/metronome/pilot/runs/`
- Create: `wiki/sources/metronome/source-metronome-guides-events-design-usage-events.md`
- Update after concept audit: relevant `wiki/concepts/metronome/*.md`
- Update: `wiki/metronome-index.md`, `wiki/metronome-log.md`
- Create: Terra final receipt under the Terra run directory

- [ ] Read all 88 raw lines and perform the concept audit.
- [ ] Run the Luna shadow and Terra candidate in isolated worker worktrees; keep both evidence sets.
- [ ] Have Sol compare both drafts with the full raw page, promote only the corrected Terra version, and record omissions, contradictions, repairs, minutes, and validation.
- [ ] Reconcile coverage at 6 sources / 219 pending and commit the complete cycle.

### Task 5: Run Cycle 2 — Enterprise Commit

- [ ] Read the complete 267-line raw file and perform the concept audit.
- [ ] Run the Terra worker, then have Sol verify commit logic, timing, drawdown, rollover, and scope boundaries before promotion.
- [ ] Create the canonical source with raw link, update concepts/index/log, write the final receipt, validate, reconcile at 7 / 218, and commit.

### Task 6: Run Cycle 3 — Stripe Invoice Integration

- [ ] Read the complete 331-line raw file and perform the concept audit.
- [ ] Run Terra, then have Sol verify prerequisites, ownership boundaries, invoice flow, configuration, limitations, and warnings before promotion.
- [ ] Create the canonical source with raw link, update concepts/index/log, write the final receipt, validate, reconcile at 8 / 217, and commit.

### Task 7: Run Cycle 4 — Create a Billable Metric

- [ ] Read the complete 342-line raw file and perform the concept audit.
- [ ] Run Terra, then have Sol verify endpoint semantics, required and conditional fields, mutually exclusive alternatives, feature gates, responses, and source inconsistencies before promotion.
- [ ] Create the canonical source with raw link, update concepts/index/log, write the final receipt, validate, reconcile at 9 / 216, and commit.

### Task 8: Run Cycle 5 — Edit a Contract

- [ ] Read the complete 4,532-line raw file and perform the concept audit.
- [ ] Run paired Luna and Terra workers in isolated worker worktrees; retain both evidence sets.
- [ ] Have Sol verify operation families, nested schemas, conditional/mutually-exclusive fields, feature gates, response behavior, and internal documentation inconsistencies.
- [ ] Promote only the corrected Terra source, update concepts/index/log, write the final receipt, validate, reconcile at 10 / 215, and commit.

### Task 9: Compare Terra with Luna and Decide the Next Routing Rule

**Files:**
- Create: `tracking/ingest/metronome/pilot/terra-comparison-pilot-report.md`
- Update if warranted: provider workflow documentation referenced from `wiki/metronome-index.md`

- [ ] Aggregate all seven worker runs, including rejected attempts and cumulative input/cached/output/reasoning tokens.
- [ ] Compare paired-page omissions, unsupported claims, section coverage, exact evidence, retries, elapsed time, and Sol repairs.
- [ ] Report Terra's five-page average repairs and repair minutes against the original Luna pilot's 23 repairs / 59 minutes baseline.
- [ ] Apply these gates: zero critical canonical omissions or unsupported claims; no quote-only full regeneration; 100% attempt accounting; no more than two Sol repairs per Terra page on average; at least 30% lower Sol repair time than the Luna baseline (target at most 41.3 total minutes / 8.26 per page).
- [ ] Choose one explicit outcome: keep Luna, route selected page types to Terra, make Terra the default cheap ingester, or stop cheap-model scaling.
- [ ] Run all focused validators, `python3 -m unittest discover -s tests -v`, compilation, `python3 scripts/validate_metronome_capsule.py`, and targeted wiki validation.
