# Metronome Ingest Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a provider-neutral, auditable Metronome ingest pilot and complete one grounded strong-model baseline source before spending on cross-model candidates.

**Architecture:** A coordinator-owned benchmark manifest and job contract select representative immutable raw files. A worker owns only its assigned source page and leased Metronome concept in an isolated worktree; after review, the coordinator owns the receipt, company count, provider index, and provider log. Deterministic validation checks job identity, write-set boundaries, grounding quotes against exact raw lines, source/raw/index/count reconciliation, and final receipt completeness.

**Tech Stack:** Python 3.9 standard library, `unittest`, JSON, Markdown/YAML frontmatter, Obsidian wikilinks, Git worktrees, optional gstack provider-adapter dry run.

## Global Constraints

- Ingest exactly one raw file per cycle and read that file completely before writing wiki content.
- Extract 3–5 verbatim grounding quotes with raw line locations before creating the concept or source page.
- Do not modify any file under `raw/metronome/`.
- Use one canonical source page per canonical URL, with path-qualified raw links newest first.
- Workers may edit only their assigned source page, leased Metronome-specific concept, and worker-local draft artifacts.
- Only the coordinator edits `wiki/companies/metronome.md`, `wiki/metronome-index.md`, `wiki/metronome-log.md`, root navigation, calculated counts, and approved receipts.
- Do not run a paid cross-model benchmark without showing adapter readiness and receiving an explicit provider choice.
- Do not bind repository configuration to DeepSeek, MiniMax, or another vendor; record the logical role `cheap_ingester` and the actual provider/model in each receipt.
- The changed-page benchmark case remains deferred until recollection creates a genuine second raw version.
- Preserve the unrelated untracked `CLAUDE copy.md` file.

---

### Task 1: Define Pilot Manifest, Job, and Receipt Validation

**Files:**
- Create: `tracking/ingest/metronome/pilot/benchmark-set.json`
- Create: `tracking/ingest/metronome/pilot/jobs/pilot-home-baseline.json`
- Create: `scripts/metronome_ingest_pilot.py`
- Create: `scripts/validate_metronome_ingest.py`
- Create: `tests/test_metronome_ingest_pilot.py`

**Interfaces:**
- Consumes: immutable raw files under `raw/metronome/` and repository-relative write-set paths.
- Produces: `load_json(path: Path) -> dict`, `validate_job(root: Path, job: dict) -> list[str]`, `validate_receipt(root: Path, job: dict, receipt: dict) -> list[str]`, and a CLI accepting `--job` plus optional `--receipt`.

- [ ] **Step 1: Write failing validation tests**

Cover these behaviors with temporary repositories:

- a valid job requires an existing raw path, one source output, one concept lease, disjoint allowed/forbidden write sets, and provider `metronome`;
- a receipt must match the job ID, canonical URL, raw path, and source page;
- every `files_changed` path must be in `allowed_write_paths`;
- each grounding quote must use valid one-based line bounds and match the raw text exactly;
- successful receipts require a worker commit, passing validation commands, actual model provider/model, and approved review status;
- missing token usage is allowed only when recorded as `null` with a reason.

- [ ] **Step 2: Run the focused test and confirm failure**

Run: `python3 -m unittest tests.test_metronome_ingest_pilot -v`

Expected: import failure because `metronome_ingest_pilot` does not exist.

- [ ] **Step 3: Implement minimal validators and CLI**

Use Python 3.9-compatible dictionaries and lists. Validate raw quote text with `splitlines()` and `"\n".join(lines[start - 1:end])`. Keep schema validation deterministic and return all errors instead of stopping at the first one. The CLI prints `job: valid` and, when supplied, `receipt: valid`; otherwise it prints each error and exits `1`.

- [ ] **Step 4: Create the representative benchmark manifest**

Record these five immutable inputs with categories and line counts:

| Category | Raw path | Lines |
| --- | --- | ---: |
| short guide | `raw/metronome/guides/invoices/overview-2026-07-13.md` | 31 |
| baseline guide | `raw/metronome/guides/get-started/home-2026-07-13.md` | 140 |
| long SDK guide | `raw/metronome/guides/get-started/developer-sdks-2026-07-13.md` | 944 |
| schema-heavy guide | `raw/metronome/guides/reporting-insights/data-export/database-reference-2026-07-13.md` | 1600 |
| API reference | `raw/metronome/api-reference/contracts/create-a-contract-2026-07-13.md` | 4561 |

Add evaluation dimensions: quote accuracy, unsupported claims, raw-link correctness, focused-validator pass rate, capsule-validator pass rate after coordinator finalization, coordinator repair minutes, elapsed seconds, turns, input/output tokens when available, and cost when available. Record the changed-page case as deferred with the reason `no canonical URL currently has two retained raw versions`.

- [ ] **Step 5: Create the baseline job**

Use job ID `pilot-home-baseline`, canonical URL `https://docs.metronome.com/guides/get-started/home`, raw path `raw/metronome/guides/get-started/home-2026-07-13.md`, source output `wiki/sources/metronome/source-metronome-guides-get-started-home.md`, concept lease `wiki/concepts/metronome/metronome-usage-based-billing.md`, and role `strong_baseline`. Allow only those two wiki paths for the worker; forbid company, provider index/log, root index/log, generic concepts, comparisons, and all raw paths.

- [ ] **Step 6: Run tests and commit**

Run:

```bash
python3 -m unittest tests.test_metronome_ingest_pilot -v
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-home-baseline.json
python3 -m unittest discover -s tests -v
```

Expected: all tests pass and the job is valid.

Commit:

```bash
git add scripts/metronome_ingest_pilot.py scripts/validate_metronome_ingest.py tests/test_metronome_ingest_pilot.py tracking/ingest/metronome/pilot/benchmark-set.json tracking/ingest/metronome/pilot/jobs/pilot-home-baseline.json
git commit -m "feat: define metronome ingest pilot contract"
```

---

### Task 2: Create the Reusable Benchmark Prompt and Check Adapter Readiness

**Files:**
- Create: `tracking/ingest/metronome/pilot/prompts/source-summary-benchmark.md`
- Create: `tracking/ingest/metronome/pilot/adapter-readiness.md`

**Interfaces:**
- Consumes: a benchmark-set raw path and the source-page contract from the approved design.
- Produces: a read-only prompt that requests a fact packet rather than repository edits, plus a dated no-cost readiness record.

- [ ] **Step 1: Write the benchmark prompt**

Require the candidate model to read one complete raw file and return JSON containing: canonical URL, 3–5 exact quotes with line locations, overview, takeaways, structured details, suggested tags, concept targets, unsupported-claim self-check, and proposed path-qualified raw link. Explicitly forbid repository edits, external facts, batch reading, company/index/log changes, and claims not supported by the assigned raw file.

- [ ] **Step 2: Locate the benchmark binary and run only the no-cost dry run**

Run:

```bash
BIN="$HOME/.agents/skills/gstack/bin/gstack-model-benchmark"
[ -x "$BIN" ] || BIN="/Users/tengtao/gstack/.agents/skills/gstack/bin/gstack-model-benchmark"
"$BIN" --prompt "unused, dry-run" --models claude,gpt,gemini --dry-run
```

Record adapter availability and remediation hints in `adapter-readiness.md`. State that the gstack adapter set does not cover DeepSeek or MiniMax and that no paid benchmark was run.

- [ ] **Step 3: Commit**

```bash
git add tracking/ingest/metronome/pilot/prompts/source-summary-benchmark.md tracking/ingest/metronome/pilot/adapter-readiness.md
git commit -m "docs: add metronome model benchmark prompt"
```

---

### Task 3: Produce the Strong-Model Baseline in an Isolated Worker Worktree

**Files:**
- Read completely: `raw/metronome/guides/get-started/home-2026-07-13.md`
- Read for audit: `wiki/concepts/`, `wiki/sources/metronome/`, `wiki/companies/metronome.md`
- Create: `wiki/concepts/metronome/metronome-usage-based-billing.md`
- Create: `wiki/sources/metronome/source-metronome-guides-get-started-home.md`

**Interfaces:**
- Consumes: `pilot-home-baseline.json` and the complete raw page.
- Produces: one grounded source summary and one leased platform concept; no shared coordinator files.

- [ ] **Step 1: Create the worker worktree and verify baseline tests**

Create branch `codex/metronome-pilot-home-worker` under `.worktrees/metronome-pilot-home-worker`, verify `.worktrees/` is ignored, and run `python3 -m unittest discover -s tests -v`.

- [ ] **Step 2: Read the full raw file and extract grounding quotes**

Read all 140 lines with line numbers. Record 3–5 exact quotes covering the platform problem, event-driven billing flow, pricing model objects, and downstream invoice/reporting outcomes. Do not write wiki content until the full read and concept audit are complete.

- [ ] **Step 3: Complete the concept audit first**

Search all existing concept pages for the same topic. Because this is the first Metronome platform source, create `metronome-usage-based-billing.md` with concept frontmatter, a source-grounded definition, the documented workflow, relationships to [[metronome]] and [[stripe]], open questions explicitly limited by the single source, and a `## Sources` link to the new source page.

- [ ] **Step 4: Create the source page**

Use the exact source contract: `date_ingested: 2026-07-14`, canonical URL from the job, `original_format: webpage`, the one path relative to `raw/`, tags `[metronome, usage-based-billing, getting-started]`, all six required body sections, a concise initial change-history entry, links to the company and leased concept, and `[[raw/metronome/guides/get-started/home-2026-07-13|2026-07-13 snapshot - initial collection]]`.

- [ ] **Step 5: Validate write ownership and content**

Run focused wiki validation on the source and concept. Compare `git diff --name-only` against the job's allowed write paths. Run the full test suite. Do not run the capsule validator in the worker because coordinator-owned index/count updates have not occurred yet.

- [ ] **Step 6: Commit worker output**

```bash
git add wiki/concepts/metronome/metronome-usage-based-billing.md wiki/sources/metronome/source-metronome-guides-get-started-home.md
git commit -m "docs: ingest metronome getting started baseline"
```

Record the resulting commit hash for the coordinator receipt.

---

### Task 4: Coordinator Review, Receipt, and Aggregate Finalization

**Files:**
- Create: `tracking/ingest/metronome/pilot/receipts/pilot-home-baseline.json`
- Modify: `wiki/companies/metronome.md`
- Modify: `wiki/metronome-index.md`
- Modify: `wiki/metronome-log.md`
- Merge from worker: source and concept files from Task 3

**Interfaces:**
- Consumes: reviewed worker commit, job contract, grounding quotes, focused validation results, and actual runtime model identity when available.
- Produces: approved receipt and coordinator-owned query routing/count updates.

- [ ] **Step 1: Review and merge the worker commit**

Verify the worker diff touches exactly its two allowed wiki files, read both files completely, compare every factual claim to the raw page, and fast-forward or cherry-pick only after the review passes.

- [ ] **Step 2: Write the final receipt**

Record the exact job/source/raw identity, successful status, 3–5 grounding quotes and locations, worker commit, the two worker files, proposed and completed shared updates, all validation commands/results, logical role `strong_baseline`, actual current model provider/model when exposed by the runtime, token usage or `null` plus an availability reason, elapsed time when available, and review status `approved` with coordinator notes.

- [ ] **Step 3: Update coordinator-owned wiki pages**

Set company `source_count` to `1` and replace the empty-capsule language only with claims grounded in the baseline source. Update the Metronome index to `1` ingested and `224` pending, link the new source and concept, and preserve the planned taxonomy for the remaining concepts. Prepend a `2026-07-14` ingest entry to the provider log with the source, concept, worker role, receipt path, and validation result.

- [ ] **Step 4: Validate the complete cycle**

Run:

```bash
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-home-baseline.json --receipt tracking/ingest/metronome/pilot/receipts/pilot-home-baseline.json
python3 scripts/validate_wiki.py wiki/sources/metronome/source-metronome-guides-get-started-home.md wiki/concepts/metronome/metronome-usage-based-billing.md wiki/companies/metronome.md wiki/metronome-log.md
python3 scripts/validate_metronome_capsule.py
python3 -m unittest discover -s tests -v
```

Expected: job and receipt valid; focused wiki validation passes; capsule reports 225 raw, 1 source, 224 pending ingest; all tests pass.

- [ ] **Step 5: Commit coordinator finalization**

```bash
git add tracking/ingest/metronome/pilot/receipts/pilot-home-baseline.json wiki/companies/metronome.md wiki/metronome-index.md wiki/metronome-log.md
git commit -m "docs: finalize metronome baseline ingest"
```

---

### Task 5: Final Verification and Local Integration

**Files:**
- Modify: `docs/superpowers/plans/2026-07-14-metronome-ingest-pilot.md`

**Interfaces:**
- Consumes: all pilot commits.
- Produces: a verified local `main` state and a clear paid-benchmark decision point.

- [ ] **Step 1: Mark completed plan checkboxes and run final verification**

Run the full tests, Python compilation, job/receipt validation, focused wiki validation, capsule validation, and `git diff --check`. Run the full wiki validator and confirm any remaining failures are the same unrelated pre-existing issues.

- [ ] **Step 2: Merge locally and verify on `main`**

Use a local fast-forward merge without pull or push, rerun the full tests and capsule validator, then remove the temporary worktree and feature branches.

- [ ] **Step 3: Stop before paid model runs or parallel scale-out**

Report the baseline quality evidence, adapter readiness, remaining 224-page queue, receipts, and commits. Request the provider choice before any paid Claude/GPT/Gemini benchmark. Note that DeepSeek/MiniMax require a separate compatible adapter or runtime configuration before they can be benchmarked.
