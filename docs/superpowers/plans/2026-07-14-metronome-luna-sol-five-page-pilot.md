# Metronome Luna/Sol Five-Page Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run five sequential, auditable Metronome ingest cases with GPT-5.6 Luna producing grounded draft artifacts, GPT-5.6 Sol owning canonical wiki synthesis and final approval, and a read-only review sub-agent assessing the completed pilot.

**Architecture:** A Python coordinator wrapper invokes `codex exec` with Luna at high reasoning in a read-only sandbox, captures structured output and runtime evidence, validates exact quotes and identity, and renders a stable draft. Sol performs the concept audit before writing canonical wiki content, records repairs and shared updates in a final receipt, and completes one entire cycle before the next begins. After all five cycles, a spawned read-only sub-agent reviews the raw files, Luna artifacts, Sol results, and receipts; the coordinator records both the independent findings and final scale recommendation.

**Tech Stack:** Python 3.9 standard library, `unittest`, JSON Schema consumed by Codex CLI, Markdown/YAML frontmatter, Obsidian wikilinks, Git worktrees, Codex CLI with GPT-5.6 Luna and GPT-5.6 Sol.

## Global Constraints

- Follow `CLAUDE.md` and `rules/ingest.md`; ingest exactly one raw file per cycle and read it completely.
- Do not modify any file under `raw/metronome/`.
- Keep the five cases sequential; do not dispatch page ingests in parallel.
- Luna runs as `gpt-5.6-luna` with reasoning effort `high`, web search disabled, approval policy `never`, and sandbox `read-only`.
- Luna produces only run artifacts under its assigned `tracking/ingest/metronome/pilot/runs/<job-id>/` directory.
- Sol performs the concept audit before creating or updating a canonical source page.
- Only Sol updates concepts, company pages, indexes, logs, canonical source pages, final receipts, and coverage counts.
- The existing getting-started baseline is shadow-tested and must not be overwritten.
- Permit one Luna retry only when deterministic validation or the Codex process fails.
- Preserve failed-attempt evidence and never count a Sol replacement as a Luna success.
- Do not change `/Users/tengtao/.codex/config.toml`; choose models per invocation.
- Preserve the unrelated untracked `CLAUDE copy.md`.
- Do not declare the pilot complete until the requested read-only review sub-agent has finished and its findings are shared.

---

### Task 1: Extend Pilot Contracts for Luna Drafts and Two-Stage Receipts

**Files:**
- Modify: `scripts/metronome_ingest_pilot.py:11-162`
- Modify: `scripts/validate_metronome_ingest.py:6-35`
- Modify: `tests/test_metronome_ingest_pilot.py:13-159`

**Interfaces:**
- Consumes: existing schema-version-1 strong-baseline jobs and receipts plus new Luna job/output/worker/final receipt dictionaries.
- Produces: `validate_luna_output(root, job, output) -> list[str]`, `render_luna_draft(job, output, ingest_date) -> str`, `validate_worker_receipt(root, job, receipt) -> list[str]`, and `validate_final_receipt(root, job, receipt) -> list[str]` while preserving `validate_receipt` compatibility.

- [x] **Step 1: Write failing Luna job and output tests**

Add fixtures and tests with these exact boundaries:

```python
def valid_luna_job(self):
    run_dir = "tracking/ingest/metronome/pilot/runs/pilot-invoices-overview-luna"
    return {
        "schema_version": 2,
        "job_id": "pilot-invoices-overview-luna",
        "provider": "metronome",
        "mode": "real_ingest",
        "canonical_url": "https://docs.metronome.com/guides/invoices/overview",
        "raw_path": "raw/metronome/guides/home.md",
        "source_page": "wiki/sources/metronome/source-metronome-guides-invoices-overview.md",
        "artifact_dir": run_dir,
        "role": "cheap_ingester",
        "allowed_write_paths": [run_dir],
        "forbidden_write_paths": [
            "wiki/companies/metronome.md",
            "wiki/metronome-index.md",
            "wiki/metronome-log.md",
            "wiki/index.md",
            "wiki/log.md",
        ],
        "forbidden_write_prefixes": ["raw/", "wiki/"],
    }

def valid_luna_output(self, job):
    return {
        "job_id": job["job_id"],
        "raw_path": job["raw_path"],
        "canonical_url": job["canonical_url"],
        "title": "Metronome Invoicing Overview",
        "grounding_quotes": [
            {"line_start": 1, "line_end": 1, "text": "alpha", "supports": "first claim"},
            {"line_start": 2, "line_end": 2, "text": "beta", "supports": "second claim"},
            {"line_start": 3, "line_end": 4, "text": "gamma\ndelta", "supports": "third claim"},
        ],
        "overview": "A grounded overview.",
        "key_takeaways": ["A grounded takeaway."],
        "details": [{"heading": "Scope", "facts": ["A grounded fact."]}],
        "suggested_tags": ["metronome", "invoicing"],
        "suggested_metronome_concepts": ["metronome-invoicing"],
        "proposed_raw_link": "[[raw/metronome/guides/home|collection snapshot]]",
        "unsupported_claim_self_check": [],
    }
```

Test that schema-version-2 Luna jobs require `mode`, `artifact_dir`, role `cheap_ingester`, an artifact directory matching the job ID, and a write set containing only that directory. Test that output identity must match the job, quotes must exactly match raw lines, tags must include `metronome`, concepts must start with `metronome-`, the raw link target must equal the raw path without `.md`, and unsupported claims make the output invalid.

- [x] **Step 2: Run the focused tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_metronome_ingest_pilot -v
```

Expected: import errors for the new validation and rendering functions or assertion failures because schema-version-2 jobs are not supported.

- [x] **Step 3: Implement backward-compatible Luna validation**

Add these constants and public functions:

```python
LUNA_MODEL = "gpt-5.6-luna"
LUNA_REASONING_EFFORT = "high"
LUNA_RUN_ROOT = "tracking/ingest/metronome/pilot/runs/"

def validate_luna_output(root: Path, job: Dict[str, Any], output: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for field in ("job_id", "raw_path", "canonical_url"):
        if output.get(field) != job.get(field):
            errors.append(f"luna output: {field} does not match job")
    errors.extend(_validate_quotes(root, job, output.get("grounding_quotes", []), "luna output"))
    tags = output.get("suggested_tags", [])
    if not isinstance(tags, list) or "metronome" not in tags:
        errors.append("luna output: suggested_tags must include metronome")
    concepts = output.get("suggested_metronome_concepts", [])
    if not isinstance(concepts, list) or any(not str(item).startswith("metronome-") for item in concepts):
        errors.append("luna output: concepts must use metronome-prefixed slugs")
    expected_target = str(job.get("raw_path", ""))[:-3]
    raw_link = str(output.get("proposed_raw_link", ""))
    if (
        not raw_link.startswith(f"[[{expected_target}|")
        or not raw_link.endswith("]]" )
    ):
        errors.append("luna output: proposed_raw_link must target the assigned raw file without .md")
    if output.get("unsupported_claim_self_check") not in ([], None):
        errors.append("luna output: unsupported_claim_self_check must be empty for acceptance")
    return errors
```

Extract existing quote checking into `_validate_quotes(...)` so baseline receipt behavior stays unchanged. Branch `validate_job` on `schema_version == 2`: validate the Luna fields and do not require `concept_leases`; retain the current schema-version-1 path without changes.

- [x] **Step 4: Implement deterministic draft rendering**

Render the accepted Luna substance without adding facts:

```python
def render_luna_draft(job: Dict[str, Any], output: Dict[str, Any], ingest_date: str) -> str:
    tags = ", ".join(output["suggested_tags"])
    takeaways = "\n".join(f"- {item}" for item in output["key_takeaways"])
    detail_blocks = []
    for section in output["details"]:
        facts = "\n".join(f"- {fact}" for fact in section["facts"])
        detail_blocks.append(f"### {section['heading']}\n\n{facts}")
    details = "\n\n".join(detail_blocks)
    return (
        "---\n"
        f"title: \"{output['title']}\"\n"
        "type: source\n"
        f"date_ingested: {ingest_date}\n"
        f"canonical_url: \"{job['canonical_url']}\"\n"
        "original_format: webpage\n"
        "raw_files:\n"
        f"  - \"{job['raw_path'][4:]}\"\n"
        f"tags: [{tags}]\n"
        "---\n\n"
        f"## Overview\n\n{output['overview']}\n\n"
        f"## Key takeaways\n\n{takeaways}\n\n"
        f"## Details\n\n{details}\n\n"
        "## Change history\n\n"
        f"- {ingest_date}: Luna pilot draft from the assigned raw snapshot.\n\n"
        "## Related\n\n"
        "- Company: [[metronome]]\n"
        "- Concepts: coordinator concept audit required before promotion.\n\n"
        "## Raw Sources\n\n"
        f"- {output['proposed_raw_link']}\n"
    )
```

Test exact frontmatter, raw path relative to `raw/`, required headings, and path-qualified raw link.

- [x] **Step 5: Implement worker and final receipt validation**

Require worker receipts to contain job identity, model `gpt-5.6-luna`, reasoning `high`, attempt count `1` or `2`, timestamps, elapsed seconds, process exit code, output/draft/log paths inside the artifact directory, deterministic checks, and token usage or an unavailability reason. Require final receipts to reference the worker receipt, classify mode as `shadow` or `real_ingest`, list repairs and repair minutes, list concepts/shared files, include validation commands, and carry a Sol decision of `approved`, `approved_with_repairs`, or `rejected`.

Keep `validate_receipt` as the schema-version-1 baseline validator; expose the new validators separately so the existing receipt remains valid.

- [x] **Step 6: Extend the CLI and verify both generations**

Add mutually independent options:

```python
parser.add_argument("--luna-output")
parser.add_argument("--worker-receipt")
parser.add_argument("--final-receipt")
```

Load and validate only the supplied artifacts after the job passes. Print `luna output: valid`, `worker receipt: valid`, and `final receipt: valid` for passing inputs.

Run:

```bash
python3 -m unittest tests.test_metronome_ingest_pilot -v
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-home-baseline.json --receipt tracking/ingest/metronome/pilot/receipts/pilot-home-baseline.json
python3 -m unittest discover -s tests -v
```

Expected: the old job/receipt and every test pass.

- [x] **Step 7: Commit the contract extension**

```bash
git add scripts/metronome_ingest_pilot.py scripts/validate_metronome_ingest.py tests/test_metronome_ingest_pilot.py
git commit -m "feat: add luna ingest artifact contracts"
```

---

### Task 2: Add the Structured Luna Runner

**Files:**
- Create: `scripts/run_metronome_luna_worker.py`
- Create: `tests/test_run_metronome_luna_worker.py`
- Create: `tracking/ingest/metronome/pilot/schemas/luna-output.schema.json`
- Modify: `tracking/ingest/metronome/pilot/prompts/source-summary-benchmark.md:1-59`

**Interfaces:**
- Consumes: one schema-version-2 Luna job and the immutable assigned raw file.
- Produces: `build_prompt(template, job, validation_errors=None) -> str`, `build_codex_command(root, schema_path, output_path, prompt) -> list[str]`, and `run_worker(root, job_path, ingest_date) -> int` with at most two model attempts.

- [x] **Step 1: Write failing command, success, and retry tests**

Mock `subprocess.run` and assert the command contains exactly:

```python
[
    "codex", "exec",
    "-m", "gpt-5.6-luna",
    "-c", 'model_reasoning_effort="high"',
    "-s", "read-only",
    "-a", "never",
    "--ephemeral",
    "--output-schema", str(schema_path),
    "--json",
    "-o", str(output_path),
    "-C", str(root),
    prompt,
]
```

Test that a valid first output writes one accepted output, draft, worker receipt, and attempt log. Test that an invalid first output triggers exactly one second call whose prompt contains the deterministic errors. Test that a second invalid result returns exit code `1`, preserves both attempts, and writes a failed receipt without a draft.

- [x] **Step 2: Run the runner tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_run_metronome_luna_worker -v
```

Expected: import failure because `run_metronome_luna_worker.py` does not exist.

- [x] **Step 3: Create the strict output schema**

Define a JSON object with `additionalProperties: false`. Require `job_id`, `raw_path`, `canonical_url`, `title`, `grounding_quotes`, `overview`, `key_takeaways`, `details`, `suggested_tags`, `suggested_metronome_concepts`, `proposed_raw_link`, and `unsupported_claim_self_check`. Constrain grounding quotes to 3-5 items; every quote requires integer `line_start`, integer `line_end`, string `text`, and string `supports`. Require at least one takeaway, one detail section, and one tag.

- [x] **Step 4: Update the prompt contract**

Add `job_id` and `title` to the required JSON shape. State that the output is a draft artifact, not a canonical wiki page; Luna must not edit files or concepts. Preserve the full-file, exact-quote, no-web, one-source, and raw-link rules. Add this retry clause:

```markdown
When the coordinator supplies deterministic validation errors, correct only those errors while re-reading the assigned raw file. Do not copy or infer facts from the error messages.
```

- [x] **Step 5: Implement the runner with immutable attempt evidence**

Create `attempt-1/` and, only if needed, `attempt-2/` under the job artifact directory. For each attempt, capture Codex JSONL stdout as `events.jsonl`, stderr as `stderr.log`, exit code, timestamps, and the model's last message as `output.json`. Validate the output before rendering. Copy the accepted output to `luna-output.json`, render `luna-source-draft.md`, and write `luna-worker-receipt.json` with runtime metadata.

Use `subprocess.run(..., capture_output=True, text=True, cwd=root)` without `shell=True`. Do not log environment variables or authentication material.

- [x] **Step 6: Run the runner tests and full suite**

```bash
python3 -m unittest tests.test_run_metronome_luna_worker -v
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/metronome_ingest_pilot.py scripts/validate_metronome_ingest.py scripts/run_metronome_luna_worker.py
```

Expected: all tests and compilation pass without a real model call.

- [x] **Step 7: Commit the Luna runner**

```bash
git add scripts/run_metronome_luna_worker.py tests/test_run_metronome_luna_worker.py tracking/ingest/metronome/pilot/schemas/luna-output.schema.json tracking/ingest/metronome/pilot/prompts/source-summary-benchmark.md
git commit -m "feat: add structured metronome luna runner"
```

---

### Task 3: Define and Validate the Five Luna Jobs

**Files:**
- Create: `tracking/ingest/metronome/pilot/jobs/pilot-invoices-overview-luna.json`
- Create: `tracking/ingest/metronome/pilot/jobs/pilot-home-luna-shadow.json`
- Create: `tracking/ingest/metronome/pilot/jobs/pilot-developer-sdks-luna.json`
- Create: `tracking/ingest/metronome/pilot/jobs/pilot-database-reference-luna.json`
- Create: `tracking/ingest/metronome/pilot/jobs/pilot-create-contract-luna.json`
- Modify: `tracking/ingest/metronome/pilot/benchmark-set.json`

**Interfaces:**
- Consumes: the approved five-case benchmark and schema-version-2 Luna job contract.
- Produces: five ordered, validated jobs with disjoint artifact directories and exact target source paths.

- [x] **Step 1: Create the five exact job identities**

Use these values:

| Job ID | Mode | Canonical URL | Target source page |
| --- | --- | --- | --- |
| `pilot-invoices-overview-luna` | `real_ingest` | `https://docs.metronome.com/guides/invoices/overview` | `wiki/sources/metronome/source-metronome-guides-invoices-overview.md` |
| `pilot-home-luna-shadow` | `shadow` | `https://docs.metronome.com/guides/get-started/home` | `wiki/sources/metronome/source-metronome-guides-get-started-home.md` |
| `pilot-developer-sdks-luna` | `real_ingest` | `https://docs.metronome.com/guides/get-started/developer-sdks` | `wiki/sources/metronome/source-metronome-guides-get-started-developer-sdks.md` |
| `pilot-database-reference-luna` | `real_ingest` | `https://docs.metronome.com/guides/reporting-insights/data-export/database-reference` | `wiki/sources/metronome/source-metronome-guides-reporting-insights-data-export-database-reference.md` |
| `pilot-create-contract-luna` | `real_ingest` | `https://docs.metronome.com/api-reference/contracts/create-a-contract` | `wiki/sources/metronome/source-metronome-api-reference-contracts-create-a-contract.md` |

Each artifact directory is `tracking/ingest/metronome/pilot/runs/<job-id>`. Each allowed write path contains only that directory. Forbid all `raw/` and `wiki/` prefixes. Set role `cheap_ingester`, model provider `openai`, model `gpt-5.6-luna`, and reasoning effort `high`.

- [x] **Step 2: Add job IDs and behavior to the benchmark manifest**

Preserve categories, paths, line counts, and evaluation dimensions. Add `job_id`, `mode`, and `target_source_page` to each case so the manifest remains the ordered source of truth.

- [x] **Step 3: Validate all jobs without model calls**

```bash
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-invoices-overview-luna.json
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-home-luna-shadow.json
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-developer-sdks-luna.json
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-database-reference-luna.json
python3 scripts/validate_metronome_ingest.py --job tracking/ingest/metronome/pilot/jobs/pilot-create-contract-luna.json
```

Expected: each command prints `job: valid`.

- [x] **Step 4: Commit the job queue**

```bash
git add tracking/ingest/metronome/pilot/benchmark-set.json tracking/ingest/metronome/pilot/jobs/pilot-*-luna*.json
git commit -m "docs: define metronome luna pilot jobs"
```

---

### Task 4: Run and Finalize the Short Invoicing Case

**Files:**
- Create: `tracking/ingest/metronome/pilot/runs/pilot-invoices-overview-luna/`
- Create: `wiki/sources/metronome/source-metronome-guides-invoices-overview.md`
- Create or modify after concept audit: `wiki/concepts/metronome/metronome-invoicing.md`
- Create: `tracking/ingest/metronome/pilot/receipts/pilot-invoices-overview-luna-final.json`
- Modify: `wiki/companies/metronome.md`
- Modify: `wiki/metronome-index.md`
- Modify: `wiki/metronome-log.md`

**Interfaces:**
- Consumes: the complete 31-line raw page and the validated Luna job.
- Produces: the first Luna evidence set, one Sol-approved canonical source, concept/shared updates, and coverage `2 sources / 223 pending`.

- [x] **Step 1: Create the isolated worker worktree**

Create `.worktrees/metronome-pilot-invoices-luna` on branch `codex/metronome-pilot-invoices-luna`. Verify `.worktrees/` is ignored and the full tests pass before the model call.

- [x] **Step 2: Run Luna once with automatic validation retry**

```bash
python3 scripts/run_metronome_luna_worker.py --job tracking/ingest/metronome/pilot/jobs/pilot-invoices-overview-luna.json --ingest-date 2026-07-14
```

Expected: exit `0`; accepted output, draft, receipt, and one or two attempt directories exist only under the job run directory.

- [x] **Step 3: Validate Luna evidence and write ownership**

Run the pilot validator with `--luna-output` and `--worker-receipt`. Compare the worktree diff against the single allowed artifact directory. Reject any raw or wiki edit.

- [x] **Step 4: Perform the Sol concept audit before canonical writing**

Read the 31-line raw file, Luna output, draft, all existing Metronome source pages, and relevant concepts. Create or update `metronome-invoicing.md` first, grounded only in this page and existing approved sources. Record whether Luna omitted or overstated Stripe invoicing, marketplace invoicing, ERP invoicing, distribution channels, or optionality.

- [x] **Step 5: Promote and review the canonical source page**

Create the target source page from the Luna draft. Replace the draft-only Related placeholder with actual company/concept links. Verify every claim against the complete raw page, record every Sol repair by category, and preserve the path-qualified raw link.

- [x] **Step 6: Finalize shared state and receipt**

Set company coverage to `2`, index coverage to `2 ingested / 223 pending`, add source/concept links, prepend a provider-log entry, and write the Sol final receipt with repair minutes and commands.

- [x] **Step 7: Validate and commit the complete cycle**

Run final receipt validation, focused wiki validation, capsule validation expecting `225 raw, 2 sources, 223 pending ingest`, the full test suite, and `git diff --check`. Commit evidence and approved wiki updates as:

```bash
git commit -m "docs: complete metronome luna invoicing pilot"
```

Remove the worker worktree only after the commit is integrated locally.

---

### Task 5: Run the Getting-Started Shadow Comparison

**Files:**
- Create: `tracking/ingest/metronome/pilot/runs/pilot-home-luna-shadow/`
- Create: `tracking/ingest/metronome/pilot/receipts/pilot-home-luna-shadow-final.json`
- Do not modify: `wiki/sources/metronome/source-metronome-guides-get-started-home.md`
- Do not modify shared wiki pages for this case.

**Interfaces:**
- Consumes: the complete 140-line raw page and the existing strong baseline source/receipt.
- Produces: a Luna shadow artifact and Sol comparison receipt while coverage remains `2 sources / 223 pending`.

- [x] **Step 1: Create `.worktrees/metronome-pilot-home-luna-shadow`**

Use branch `codex/metronome-pilot-home-luna-shadow`, confirm a clean baseline except `CLAUDE copy.md`, and run tests.

- [x] **Step 2: Run the Luna shadow job**

```bash
python3 scripts/run_metronome_luna_worker.py --job tracking/ingest/metronome/pilot/jobs/pilot-home-luna-shadow.json --ingest-date 2026-07-14
```

Expected: valid run artifacts with no wiki changes.

- [x] **Step 3: Compare Luna with the strong baseline**

Sol reads the raw page, Luna artifacts, existing canonical source, concept, and `pilot-home-baseline.json`. Record missed routes, unsupported additions, emphasis differences, structural differences, and the edits that would have been required. Do not alter the baseline page or shared files.

- [x] **Step 4: Write and validate the shadow final receipt**

Use mode `shadow`, an empty canonical write set, comparison repairs, repair minutes, and an approval or rejection decision. Run worker/final receipt validation, capsule validation expecting `2 / 223`, tests, and diff checks.

- [x] **Step 5: Commit and remove the shadow worktree**

```bash
git commit -m "docs: record metronome luna baseline comparison"
```

---

### Task 6: Run and Finalize the Long SDK Case

**Files:**
- Create: `tracking/ingest/metronome/pilot/runs/pilot-developer-sdks-luna/`
- Create: `wiki/sources/metronome/source-metronome-guides-get-started-developer-sdks.md`
- Create or modify only after audit: Metronome event-ingestion, billable-metric, customer/contract, or SDK-related concepts supported by the full source
- Create: `tracking/ingest/metronome/pilot/receipts/pilot-developer-sdks-luna-final.json`
- Modify: company, Metronome index, and Metronome log

**Interfaces:**
- Consumes: the complete 944-line SDK guide.
- Produces: one canonical SDK source plus justified concept/shared updates and coverage `3 sources / 222 pending`.

- [x] **Step 1: Create `.worktrees/metronome-pilot-developer-sdks-luna` and verify tests**

Use branch `codex/metronome-pilot-developer-sdks-luna`.

- [x] **Step 2: Run and validate Luna**

```bash
python3 scripts/run_metronome_luna_worker.py --job tracking/ingest/metronome/pilot/jobs/pilot-developer-sdks-luna.json --ingest-date 2026-07-14
```

Validate exact quotes, full identity, raw link, attempt evidence, and write boundaries.

- [x] **Step 3: Perform the Sol concept audit first**

Read all 944 raw lines and the complete Luna artifacts. Audit planned Metronome concepts before writing the source. Create or update only concepts directly supported by the page; keep language examples and SDK mechanics on the source page when they do not justify a new concept.

- [x] **Step 4: Finalize source, contradictions, shared state, and receipt**

Check installation/configuration, usage events, billable metrics, customers, contracts, invoices, language parity, code caveats, and any limits stated by the raw page. Record omissions and repairs. Update coverage to `3 / 222` only after approval.

- [x] **Step 5: Validate, commit, and remove the worktree**

Require final receipt validation, focused wiki validation, capsule `225 / 3 / 222`, tests, compilation, and diff checks. Commit:

```bash
git commit -m "docs: complete metronome luna sdk pilot"
```

---

### Task 7: Run and Finalize the Schema-Heavy Database Reference

**Files:**
- Create: `tracking/ingest/metronome/pilot/runs/pilot-database-reference-luna/`
- Create: `wiki/sources/metronome/source-metronome-guides-reporting-insights-data-export-database-reference.md`
- Create or modify after audit: `wiki/concepts/metronome/metronome-reporting-and-analytics.md`
- Create: `tracking/ingest/metronome/pilot/receipts/pilot-database-reference-luna-final.json`
- Modify: company, Metronome index, and Metronome log

**Interfaces:**
- Consumes: the complete 1,600-line database reference.
- Produces: a query-useful schema summary without pretending to reproduce the full reference, plus coverage `4 sources / 221 pending`.

- [x] **Step 1: Create `.worktrees/metronome-pilot-database-reference-luna` and verify tests**

Use branch `codex/metronome-pilot-database-reference-luna`.

- [x] **Step 2: Run and validate Luna**

```bash
python3 scripts/run_metronome_luna_worker.py --job tracking/ingest/metronome/pilot/jobs/pilot-database-reference-luna.json --ingest-date 2026-07-14
```

Reject summaries that turn selected table examples into an exhaustive claim or omit the all-columns-nullable warning when it is materially relevant.

- [x] **Step 3: Perform Sol audit and canonical finalization**

Read all 1,600 lines. Create or update the reporting concept first. Ensure the canonical source explains export purpose, schema-navigation strategy, important global cautions, representative table families, and the raw deep-dive path. Record table-family omissions separately from critical omissions.

- [x] **Step 4: Finalize receipt and shared coverage**

Record factual/omission/taxonomy repairs and repair minutes. Update coverage to `4 / 221`, source/concept navigation, company knowledge status, and provider log only after approval.

- [x] **Step 5: Validate, commit, and remove the worktree**

Require final receipt validation, focused wiki validation, capsule `225 / 4 / 221`, tests, compilation, and diff checks. Commit:

```bash
git commit -m "docs: complete metronome luna database pilot"
```

---

### Task 8: Run and Finalize the API Contract Reference

**Files:**
- Create: `tracking/ingest/metronome/pilot/runs/pilot-create-contract-luna/`
- Create: `wiki/sources/metronome/source-metronome-api-reference-contracts-create-a-contract.md`
- Create or modify after audit: `wiki/concepts/metronome/metronome-customers-and-contracts.md`
- Create: `tracking/ingest/metronome/pilot/receipts/pilot-create-contract-luna-final.json`
- Modify: company, Metronome index, and Metronome log

**Interfaces:**
- Consumes: the complete 4,561-line create-contract API reference.
- Produces: a precise, navigable endpoint summary with raw fallback and coverage `5 sources / 220 pending`.

- [x] **Step 1: Create `.worktrees/metronome-pilot-create-contract-luna` and verify tests**

Use branch `codex/metronome-pilot-create-contract-luna`.

- [x] **Step 2: Run and validate Luna**

```bash
python3 scripts/run_metronome_luna_worker.py --job tracking/ingest/metronome/pilot/jobs/pilot-create-contract-luna.json --ingest-date 2026-07-14
```

Require exact quotes and a path-qualified raw link; validators alone do not establish field completeness.

- [x] **Step 3: Perform Sol concept and API accuracy review**

Read all 4,561 lines and audit concepts before creating the source. Verify endpoint purpose, use cases, key request sections, nested structures, response/error coverage, and which details remain delegated to the raw reference. Reject invented required fields, defaults, limits, or lifecycle behavior.

- [x] **Step 4: Finalize source, shared state, and receipt**

Create or update the customer/contracts concept first, then finalize the source. Record critical and non-critical omissions separately. Update coverage to `5 / 220` only after every validation passes.

- [x] **Step 5: Validate, commit, and remove the worktree**

Require final receipt validation, focused wiki validation, capsule `225 / 5 / 220`, tests, compilation, and diff checks. Commit:

```bash
git commit -m "docs: complete metronome luna contract api pilot"
```

---

### Task 9: Spawn the Independent Review Sub-Agent and Publish the Pilot Report

**Files:**
- Create: `tracking/ingest/metronome/pilot/luna-sol-five-page-pilot-report.md`
- Modify: `wiki/metronome-log.md`
- Modify: `wiki/metronome-index.md` only if the final validated counts differ from `5 / 220`
- Modify: this implementation plan to mark completed checkboxes

**Interfaces:**
- Consumes: all five raw files, Luna artifacts, worker receipts, Sol-finalized pages, final receipts, strong baseline, and quality gates.
- Produces: an independent read-only assessment, coordinator-verified final report, and one of `scale`, `scale_with_changes`, or `do_not_scale`.

- [x] **Step 1: Verify all five cases are closed before delegation**

Run every job/output/worker/final receipt validator, capsule validation, full tests, Python compilation, and `git diff --check`. Confirm there are five run directories and five final Luna-pilot receipts, including the shadow case.

- [x] **Step 2: Spawn one read-only review sub-agent**

Give the sub-agent this bounded assignment:

```text
Review the completed Metronome GPT-5.6 Luna five-page pilot. Do not edit files. For each case, read the complete raw file, Luna output and draft, worker receipt, Sol-finalized source/concept pages when present, and final receipt. Verify factual accuracy, material completeness, emphasis, raw-link usefulness, and whether recorded Sol repairs match the actual differences. Identify cross-case failure patterns that deterministic validators missed. Return: (1) per-case findings with evidence paths, (2) systematic risks, (3) prompt/schema/process improvements, and (4) one recommendation: scale, scale_with_changes, or do_not_scale. Treat the existing getting-started source as a shadow baseline and do not penalize it for having no new canonical write.
```

Wait for the sub-agent to finish before writing the final recommendation.

- [x] **Step 3: Verify the review against repository evidence**

The Sol coordinator checks every actionable reviewer claim against the cited raw/output/source/receipt files. Preserve disagreements explicitly instead of silently rewriting the independent conclusion.

- [x] **Step 4: Write the durable pilot report**

Include these exact sections:

```markdown
# Metronome GPT-5.6 Luna Five-Page Pilot Report

## Decision
## Case Results
## Luna Reliability
## Sol Repairs
## Cost and Timing
## Deterministic Validation Coverage
## Independent Review
## Coordinator Assessment
## Required Changes Before Scale-Out
## Evidence
```

Report per-case attempts, status, quote accuracy, unsupported claims, critical omissions, repair categories/minutes, validators, token/cost data or unavailability reasons, independent findings, and final decision.

- [x] **Step 5: Update operational navigation and run final verification**

Prepend a Metronome log entry linking the report and final decision. Confirm the index and company `source_count` match the capsule validator. Run:

```bash
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/metronome_ingest_pilot.py scripts/validate_metronome_ingest.py scripts/run_metronome_luna_worker.py scripts/validate_metronome_capsule.py
python3 scripts/validate_metronome_capsule.py
git diff --check
```

Expected if all real-ingest cases pass: `225 raw, 5 sources, 220 pending ingest`; all tests and compilation pass.

- [x] **Step 6: Commit the final report and completed plan**

```bash
git add tracking/ingest/metronome/pilot/luna-sol-five-page-pilot-report.md wiki/metronome-log.md wiki/metronome-index.md docs/superpowers/plans/2026-07-14-metronome-luna-sol-five-page-pilot.md
git commit -m "docs: conclude metronome luna ingest pilot"
```

- [x] **Step 7: Share both review perspectives with the user**

Report the independent sub-agent recommendation, the Sol coordinator recommendation, any disagreement, measured repair burden, failed cases, and the exact conditions for processing the remaining 220-page queue. Do not begin scale-out without a new user decision.
