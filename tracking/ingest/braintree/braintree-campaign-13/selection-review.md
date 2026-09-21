# Braintree C13 ten-page execution plan

Status: COMPLETE — exact-manifest execution approved2026-09-21.

**Goal:** Ingest ten currently unowned website raws as retrieval entries.
**Architecture:** Existing three dynamic child slots, Sol medium workers and different Sol high initial reviewers; coordinator-only canonical/shared writes.
**Tech Stack:** Existing Python runtime, JSON handoffs, Markdown. No code changes.
**Spec:** CLAUDE.md, rules/ingest.md, rules/psp/braintree-ingest.md, adopted rules/psp/metronome-ingest.md and dispatch-contract.md here.

## Exact selection and twenty fixed questions

| Job | Raw lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| subscription-create-node | 455 | Where is Node Subscription Create documented? | What payment-method prerequisites, creation scope and consequential qualifications are stated, and where are input details routed? |
| subscription-update-node | 302 | Where is Node Subscription Update documented? | What update scope and material billing or payment-method qualifications are stated without importing creation behavior? |
| transaction-search-node | 333 | Where is Node Transaction Search documented? | How are transaction criteria and result consumption documented, including policy limits and scope qualifications? |
| transaction-submit-for-partial-settlement-node | 100 | Where is Node Transaction Submit For Partial Settlement documented? | What payment-method availability, parent/child settlement behavior and consequential restrictions are documented? |
| transaction-adjust-authorization-node | 41 | Where is Node Transaction Adjust Authorization documented? | What authorization-adjustment scope, availability and fee qualifications are documented, distinct from capture? |
| transaction-clone-transaction-node | 52 | Where is Node Transaction Clone documented? | What is copied into a new transaction, what inputs or restrictions matter, and what alternative is recommended? |
| transaction-hold-in-escrow-node | 29 | Where is Node Transaction Hold In Escrow documented? | What Marketplace qualification, invocation and result guidance is shown without inventing lifecycle details? |
| transaction-release-from-escrow-node | 34 | Where is Node Transaction Release From Escrow documented? | What Marketplace qualification and release invocation are shown, distinct from holding or cancelling release? |
| transaction-cancel-release-node | 34 | Where is Node Transaction Cancel Release documented? | What Marketplace qualification and cancellation invocation are shown, without equating cancellation with a refund? |
| transaction-line-item-find-all-node | 38 | Where is Node Transaction Line Item Find All documented? | What collection and result guidance, policy notice and missing-rendering limitations are documented? |

Selection uses metadata, headings and opening excerpts, not a complete semantic
read. All ten raw hashes/canonical URLs are pinned in manifest.json; no source
raw owner, canonical owner or target existed at preparation. Baseline91 sources
=75 website+16 GitHub. Expected101=85+16 if all approve and no concurrent changes;
recalculate at close. This is not collection or a raw_reference classification.

This selection is heavier than C12: subscription create/update and transaction
search carry longer content. Queue these early to overlap their full reads with
shorter operation pages. Do not promise ten-page speedup. Preserve exact SDK,
payment-method/Marketplace scope, consequential warnings and damaged text;
never reconstruct missing code or infer lifecycle outcomes from operation names.
Routine fields/examples stay behind verified raw locators.

Provisional concepts: braintree-server-sdk and recurring-payments. Audit existing
index-led routes before proposing updates; create no concept without a real gap.
Read adjacent authority only for retained cross-source claims or actual conflicts.

## Fixed audit groups

A: Subscription Create + Update.
B: Transaction Search + Submit For Partial Settlement.
C: Transaction Adjust Authorization + Clone.
D: Transaction Hold In Escrow + Release From Escrow.
E: Transaction Cancel Release + Transaction Line Item Find All.

Each group answers four fixed questions;20 total, no additional three-page audit.
Do not accept a question's premise when raw says otherwise. One route per page,
object/action/direct answer/exact locator/verdict per question, one gap sweep and
completeness record per group. Start ready groups within the same3-slot capacity.

## Execution checklist after approval

- [x] Recheck hashes, absent source/canonical/raw owners, C12 completion and actual agent capacity; initialize only this campaign.
- [x] Persist trusted orders and dispatch immediately. Each worker reads one full raw, audits concepts, extracts3–5 exact located quotes and returns existing8-key handoff externally; no repository writes.
- [x] Different reviewer fully reads each first raw/candidate/quotes/suggestions. Review retained meaning, warnings and routes, not optional schema completeness. Maximum3 attempts; bounded corrections use targeted review only when impact is bounded.
- [x] Promote approved concept updates then exact source serially. Review priority with worker reserve; no batch barrier. Dispatch before retrospective prose or report polishing.
- [x] Aggregate company/index/log/count once. Check all hashes/URLs/candidate equality/unique owners/approved snippets/required and reciprocal links/duplicate catalogs/counts/touched typed files once; no documentation-only code suite.
- [x] Complete the20 fixed query questions, resolving concrete failures only; no blanket additional audit.
- [x] Close runtime and record first-pass rate, retries, UTC stage observations and total elapsed in quality-audit.md/retrospective.md. Overlapping windows are not additive.

## Scope

Only exact source targets, campaign-local artifacts, independently approved
concept updates, Braintree company/index/log/count. Raw immutable; reverse lookup
uses raw_files. Preserve concurrent GitHub/other-provider edits. No collection,
GitHub ingest, code/rule/validator changes, review waiver, new scheduler, commit,
push or later campaign authorized. Execution separately approved2026-09-21;
runtime initialized and first three trusted worker orders dispatched.
