# Metronome Luna/Sol Five-Page Pilot Design

**Date:** 2026-07-14  
**Status:** Approved design, pending implementation plan  
**Scope:** Five representative Metronome documentation pages

## Goal

Determine whether GPT-5.6 Luna can serve as the cost-efficient `cheap_ingester` for grounded Metronome source summaries while GPT-5.6 Sol remains responsible for semantic synthesis, contradiction handling, shared wiki state, and final approval.

The pilot must preserve enough evidence to explain every accepted claim, every Sol repair, and the final scale-out recommendation.

## Selected Architecture

Use a sequential two-stage pipeline with an independent read-only review after all five cases:

1. GPT-5.6 Luna reads one complete raw file and produces isolated draft artifacts.
2. Deterministic validation verifies the Luna output before any wiki page is written.
3. GPT-5.6 Sol performs the mandatory concept audit, reviews and repairs the draft, writes canonical wiki pages, updates shared state, and records final approval.
4. After all five Luna-to-Sol cycles finish, a spawned read-only sub-agent reviews the complete evidence set and recommends whether and how to scale.

Only one source cycle may be active at a time. The next raw page does not begin until the current page has completed Luna generation, deterministic validation, Sol finalization, and all required checks.

## Model Invocation

Do not change the user's global Codex model configuration. Select models per invocation:

- Luna worker: `codex exec -m gpt-5.6-luna -c model_reasoning_effort="high"`
- Sol coordinator: the active main coordinator running GPT-5.6 Sol, or an explicit `codex exec -m gpt-5.6-sol -c model_reasoning_effort="high"` when a reproducible external review run is needed

Luna receives only the assigned job, complete raw file access, repository instructions, and the source-draft output contract. It may not use web search or outside knowledge.

## Pilot Cases

The canonical case list remains `tracking/ingest/metronome/pilot/benchmark-set.json`:

| Order | Category | Raw file | Behavior |
| ---: | --- | --- | --- |
| 1 | short guide | `raw/metronome/guides/invoices/overview-2026-07-13.md` | Real ingest after Sol approval |
| 2 | baseline guide | `raw/metronome/guides/get-started/home-2026-07-13.md` | Shadow comparison only; do not overwrite the existing strong baseline |
| 3 | long SDK guide | `raw/metronome/guides/get-started/developer-sdks-2026-07-13.md` | Real ingest after Sol approval |
| 4 | schema-heavy guide | `raw/metronome/guides/reporting-insights/data-export/database-reference-2026-07-13.md` | Real ingest after Sol approval |
| 5 | API reference | `raw/metronome/api-reference/contracts/create-a-contract-2026-07-13.md` | Real ingest after Sol approval |

The ordering moves from short to difficult while retaining the existing baseline as an early comparison point. Four new source summaries are expected if every real-ingest case passes; Metronome coverage then becomes 5 ingested source pages and 220 pending documentation pages.

## Ownership Boundaries

### Luna worker owns

Inside one isolated worker worktree and only for its assigned job:

- `tracking/ingest/metronome/pilot/runs/<job-id>/luna-output.json`
- `tracking/ingest/metronome/pilot/runs/<job-id>/luna-source-draft.md`
- `tracking/ingest/metronome/pilot/runs/<job-id>/luna-worker-receipt.json`
- worker-local execution logs under the same run directory

Luna must not modify:

- any file under `raw/`
- any canonical file under `wiki/`
- job contracts or benchmark definitions
- scripts or tests
- company, concept, comparison, analysis, index, or log pages
- another pilot run directory

### Sol coordinator owns

- job creation and worktree lifecycle
- deterministic validation and retry decisions
- all canonical files under `wiki/sources/metronome/`
- all Metronome and generic concept decisions
- contradiction review
- `wiki/companies/metronome.md`
- `wiki/metronome-index.md`
- `wiki/metronome-log.md`
- root indexes and logs when required
- final receipts under `tracking/ingest/metronome/pilot/receipts/`
- final pilot report and scale-out decision

### Independent review sub-agent owns

The sub-agent is read-only. It writes no repository files and returns its assessment to the Sol coordinator. The coordinator records the assessment in the final pilot report without silently changing the reviewer's findings.

## Artifact Contracts

### Luna output

`luna-output.json` contains:

- job ID, canonical URL, and raw path
- 3-5 verbatim grounding quotes with one-based line ranges
- two-to-four-sentence overview
- key takeaways
- structured detail sections
- suggested tags
- suggested Metronome-specific concepts
- path-qualified raw wikilink without `.md`
- unsupported-claim self-check

The model output is constrained with a JSON schema. A deterministic renderer converts accepted fields into `luna-source-draft.md`; this keeps the Markdown template stable while Luna remains responsible for the substantive summary.

### Luna worker receipt

`luna-worker-receipt.json` contains:

- exact job and source identity
- model `gpt-5.6-luna` and reasoning effort `high`
- start/end timestamps and elapsed seconds
- process exit status
- retry number
- output and execution-log paths
- exact grounding quotes
- deterministic validation results
- token usage when exposed, otherwise `null` plus an availability reason
- worker status: `success`, `retryable_failure`, or `failed`

Runtime metadata comes from the coordinator wrapper rather than model-authored claims.

### Final receipt

The Sol-owned final receipt contains:

- a reference to the immutable Luna worker receipt
- Luna draft and canonical source-page paths
- whether the case was shadow-only or a real ingest
- concepts created or updated
- contradictions found and their resolution
- shared files updated
- each Sol repair, classified as factual, omission, structure, link, taxonomy, or wording
- coordinator repair minutes
- every validation command and result
- Sol review status and notes
- final status: `approved`, `approved_with_repairs`, or `rejected`

The shadow baseline receipt records comparison findings but no canonical or shared-file mutations.

## Per-Page Data Flow

1. The Sol coordinator generates and validates one job contract.
2. The coordinator creates a dedicated branch and worktree for that job.
3. Luna reads the complete assigned raw file and produces its JSON output.
4. The coordinator wrapper records runtime evidence and renders the draft source page.
5. Deterministic checks validate schema, exact quotes, raw link, identity, and write boundaries.
6. If validation fails, Luna receives only the validation errors and gets one retry.
7. After validation passes, Sol reads the complete raw file, Luna output, Luna draft, and relevant existing wiki pages.
8. Sol performs the mandatory concept audit before creating any canonical source page.
9. For a real-ingest case, Sol creates or updates concepts first, promotes and repairs the source draft, checks contradictions, and updates coordinator-owned shared pages.
10. For the shadow baseline, Sol compares Luna's output with the existing strong baseline without changing canonical wiki content.
11. Sol writes the final receipt and runs focused wiki validation, Metronome capsule validation, job/receipt validation, tests, and diff checks.
12. The coordinator preserves the worker evidence for either outcome, integrates canonical wiki changes only for an approved real-ingest case, removes the worker worktree, and starts the next case.

## Failure and Retry Rules

- A Codex process failure, invalid JSON, schema failure, incorrect quote, invalid raw link, or write-boundary violation is retryable once.
- The retry prompt contains the deterministic errors and the original assignment; it does not expose Sol-written content.
- A second Luna failure records the case as `failed`. Sol may diagnose it but must not silently replace the worker output and count the case as a Luna success.
- Unsupported claims, critical omissions, or misleading emphasis found by Sol are recorded as repairs. The canonical page may be corrected, but the immutable Luna artifact remains unchanged.
- Successful worker evidence is integrated with the approved cycle. Failed worker evidence is copied into the coordinator-owned run directory and recorded in the final receipt without integrating unauthorized or invalid worker changes.
- No next case begins until the current final receipt and required validation pass, or the case is explicitly closed as failed with its evidence preserved.
- Any raw-file mutation or edit outside the Luna write set is an immediate rejection.

## Quality Gates

Every accepted case requires:

- 100% exact grounding-quote verification
- 3-5 valid quotes
- 100% correct canonical identity and raw link
- zero unsupported claims in the canonical source page
- zero critical omissions after Sol review
- focused wiki validation passing
- Metronome capsule validation passing after coordinator finalization
- job and receipt validation passing
- all Metronome pilot tests passing
- complete repair and timing evidence

The pilot is not approved for scale-out if the long SDK, schema-heavy, or API-reference case fails, even if the short cases pass. Sol repair effort is reported per page and in aggregate; repeated factual reconstruction or major omission repair means Luna is unsuitable for unattended source drafting even when validators pass.

## Independent Review Sub-Agent

After all five cases are closed, the Sol coordinator spawns one read-only review sub-agent with access to:

- all five raw files
- all Luna outputs, drafts, worker receipts, and execution evidence
- all Sol-finalized source and concept pages
- all final receipts
- the existing strong baseline
- the quality gates in this specification

The review request requires:

1. a per-case assessment of factual accuracy, completeness, emphasis, link quality, and repair severity;
2. cross-case patterns that deterministic validators missed;
3. whether the prompt, schema, routing, or thresholds should change;
4. a recommendation: `scale`, `scale_with_changes`, or `do_not_scale`;
5. prioritized suggestions with evidence paths.

The main coordinator checks the sub-agent's report against the evidence, shares both the independent findings and its own recommendation with the user, and does not declare the pilot complete before this review finishes.

## Final Pilot Report

The coordinator creates a durable report under `tracking/ingest/metronome/pilot/` containing:

- pass/fail status for every case
- Luna retries and failures
- validation outcomes
- Sol repair counts, categories, and minutes
- token and cost data when available
- independent sub-agent findings
- final scale-out recommendation
- required changes before processing the remaining queue

The report, receipts, and immutable Luna artifacts form the audit trail for future model or prompt comparisons.

## Out of Scope

- Processing the remaining 220 pages
- Parallel production ingest
- Changing the global Codex model default
- Recollecting Metronome documentation
- Creating a changed-page benchmark before a genuine second raw version exists
- Allowing Luna to synthesize concepts, resolve contradictions, or update shared wiki files
