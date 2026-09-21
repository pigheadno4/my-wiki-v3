# Braintree C07 five-page execution plan

Status: COMPLETE; exact-manifest execution approved and completed on 2026-09-20. C01–C06 remain closed.

> For agentic workers: use the approved coordinator-controlled parallel workflow and its role-specific skills for this exact manifest only.

**Goal:** Add five currently unowned website raw pages as accurate retrieval entries.
**Architecture:** Existing Sol medium workers, different Sol high reviewers, three dynamic child slots; coordinator alone promotes and aggregates.
**Tech Stack:** Existing Python ingest runtime, native agents and Markdown/JSON artifacts; no code changes.
**Spec:** rules/psp/braintree-ingest.md, adopted rules/psp/metronome-ingest.md and this campaign's dispatch-contract.md.

## Selected pages and predetermined query audit

| Job | Lines | Provisional concept | Navigation question | Detail question |
| --- | ---: | --- | --- | --- |
| address-create-node | 39 | braintree-server-sdk | Where is Node Vault address creation documented? | What customer association, address-ID scope and per-customer limit does the page state? |
| webhooks-dispute-node | 51 | braintree-webhooks | Where are Node dispute notification kinds and payload routes documented? | Where are the event-specific trigger conditions and notification attributes documented? |
| address-update-node | 36 | braintree-server-sdk | Where is Node address updating documented? | Which identifiers and result handling appear in the update example, and what update qualifications does this page state, if any? |
| address-delete-node | 26 | braintree-server-sdk | Where is Node address deletion documented? | Which identifiers are required, and what deletion effect or error guidance does this page explicitly provide? |
| plan-all-node | 32 | braintree-server-sdk | Where is Node retrieval of all plans documented? | Where are the returned collection and callback/Promise result forms documented? |

184 logical lines including metadata (splitlines; final unterminated lines counted).
Selection used metadata, opening excerpts and headings, not full semantic analysis.
All five exact raw paths and canonical URLs have no matching current source owner
across wiki/sources; all targets are absent. This is not a historical-alias audit.
Hashes/URLs/targets are pinned in manifest.json. Short pages are not assumed low risk.
Full-read concept audit may refine these provisional routes.

## Execution checklist after exact-manifest approval

- [x] Recheck all five hashes, source absence and current source ownership; verify C06 is closed and actual agent capacity. Initialize only braintree/braintree-campaign-07 using manifest.json. Record actual UTC start.
- [x] Persist each trusted order before native dispatch. Each worker fully reads one raw, audits the relevant existing concept, returns one narrow source, 3–5 located exact quotes and supported concept suggestions. No repository writes by workers.
- [x] Have a different Sol high reviewer fully read the raw and review retained meaning, warnings, quotes and suggested routes. Use existing bounded targeted corrections only when justified; maximum three attempts.
- [x] Serially promote each job's approved concept changes then exact source. As soon as an audit group's sources are live and an eligible slot exists, dispatch its fixed questions before aggregate/report work. Group A: Address Create plus Dispute Webhooks (4 questions). Group B: Address Update/Delete plus Plan All (6 questions). No batch barrier.
- [x] Once at close, aggregate wiki/braintree-index.md, wiki/braintree-log.md and wiki/companies/braintree.md. Baseline 46 sources =30 website+16 GitHub; expected 51 =35+16 if all five approve and no unrelated concurrent source change occurs. Recalculate, do not blindly overwrite.
- [x] Run the single ten-question query audit and one aggregate mechanical check: exact approved candidates, canonical URLs/hashes, unique raw ownership, required/reciprocal links, approved concept snippets, duplicate catalogs, counts and touched typed-page validation. Do not add another three-page audit or full unit suite.
- [x] Close existing runtime and write quality-audit.md/retrospective.md with actual stage windows, first worker-handoff versus first content-review rate, full/targeted retries and post-audit repairs. Preserve overlapping intervals; do not infer missing timestamps.

Files created during execution: the five source targets in manifest.json, existing
runtime/attempt artifacts, quality-audit.md and retrospective.md in this directory.
Shared writes: the three provider aggregates above and approved relevant concept
sections (provisionally braintree-server-sdk.md and braintree-webhooks.md).
Root index needs no duplicate provider entries. Any genuine new concept gap must
be justified by full-read concept audit, not invented at preparation time.

## Only two operational refinements

1. Remind workers that the existing trusted result status is exactly
   `candidate_ready`, not `completed`; preserve all other trusted identity/schema
   fields. Do this during the existing handoff self-check, without a new checker.
2. Dispatch ready query audit groups before aggregate edits or retrospective prose;
   keep the same three-slot capacity and independent-review gates.

No runtime/rule changes, registry, worktrees, new validation mechanism, collection,
GitHub ingest, historical refresh, commit, push or automatic following campaign.
C07 is shorter than C06; a lower wall time alone cannot establish a workflow speedup.
