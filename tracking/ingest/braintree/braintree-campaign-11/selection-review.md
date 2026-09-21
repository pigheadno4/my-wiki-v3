# Braintree C11 ten-page execution plan

Status: COMPLETE — exact-manifest execution approved2026-09-21.

**Goal:** Ingest ten currently unowned Braintree website raws as retrieval entries.
**Architecture:** Existing coordinator-only writes, Sol medium workers and different Sol high initial reviewers; three dynamic child slots including auditors.
**Tech Stack:** Existing Python runtime and Markdown/JSON records; no code changes.
**Spec:** rules/ingest.md, rules/psp/braintree-ingest.md, adopted rules/psp/metronome-ingest.md and this campaign's dispatch-contract.md.

## Fixed selection and20 questions

| Job | Raw lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| search-fields-node | 123 | Where is Node search-field operators documented? | Where are supported field types, operators and important qualifications documented? |
| search-results-node | 93 | Where is Node search-result consumption documented? | What SDK-version, stream/callback and result-consumption qualifications are documented? |
| customer-search-node | 190 | Where is Node customer search documented? | Where are filters and result-consumption examples, and what result-limitation notice is stated? |
| credit-card-verification-search-node | 128 | Where is Node credit-card verification search documented? | Where are verification-specific search criteria and result limits, distinct from transactions or customers? |
| dispute-accept-node | 37 | Where is Node dispute acceptance documented? | What access and refund warnings are stated, and which eligibility details are missing from the collected rendering? |
| dispute-finalize-node | 45 | Where is Node dispute finalization documented? | What eligibility, evidence-submission requirement and status transition are stated? |
| dispute-find-node | 29 | Where is Node single-dispute lookup documented? | What identifier, access restriction and result-limitation guidance does the page provide? |
| dispute-search-node | 61 | Where is Node dispute search documented? | Where are search criteria and result access documented, and what availability or result limits apply? |
| document-upload-create-node | 34 | Where is Node document upload creation documented? | What file input, purpose and result guidance is actually shown, without inferring dispute submission? |
| dispute-remove-evidence-node | 37 | Where is Node removal of dispute evidence documented? | What dispute status, identifiers and removal/result behavior are established, distinct from finalization? |

Selection uses headings, opening excerpts and metadata, not complete semantic
reading. Ten exact raw paths, hashes and canonical URLs are pinned in manifest;
all source targets and raw/canonical owners were absent at preparation.777 raw
lines total. Baseline71 sources=55 website+16 GitHub; expected81=65+16 if all
approve and no concurrent source additions. Recalculate before close.

Provisional routes: braintree-server-sdk for Node operations; disputes for
relevant dispute retrieval. Full-read concept audit decides meaningful routes
and whether a real provider-concept gap exists; do not copy endpoint schemas.
Accept's opening has a missing status value: do not reconstruct it. Keep prior
refund warnings, access restrictions, evidence upload/removal/finalization
boundaries and SDK/version qualifiers. The selected metadata cannot establish
all semantics; worker/reviewer full reading remains mandatory.

## Five fixed audit groups

A: Search Fields + Search Results.
B: Customer Search + Credit Card Verification Search.
C: Dispute Accept + Finalize.
D: Dispute Find + Search.
E: Document Upload Create + Dispute Remove Evidence.

Each group answers exactly its four table questions. Together these are one
20-question audit; no additional three-page audit. Start each ready group when
capacity permits, overlapping remaining reviews and serial promotions.

## Execution checklist after separate approval

- [x] Recheck all10 hashes, targets and ownership; confirm C10 complete and actual capacity. Initialize only braintree/braintree-campaign-11.
- [x] Persist each trusted order, then dispatch immediately; one full raw read, index-led concept audit,3–5 exact located quotes and existing8-key handoff per worker.
- [x] Different Sol high reviewer performs full initial review. Block false retained claims, important missing warnings and broken evidence routes, not optional detail inventories. Bounded corrections get targeted diff/context review when justified; maximum3 attempts.
- [x] Promote only approved concept updates then exact source, serially. Dispatch ready query groups before retrospective prose. All auditors count toward3 slots.
- [x] Aggregate company/index/log/count once, preserving unrelated GitHub work. Run one complete mechanical close across promoted candidates, raw hashes, canonical/raw ownership, bidirectional links, approved updates, unique catalogs, counts and touched typed wiki pages.
- [x] Accept all20 fixed query answers with correct object/action, direct answer, exact locator and verdict. Resolve concrete failures, not blanket source expansion.
- [x] Close existing runtime; record elapsed/per-page time, first-pass rate, retries and actual timing observations in quality-audit.md and retrospective.md. Separate overlapping analysis, queue/setup and delivery; no token estimates or new telemetry.

## Ownership and boundaries

Create exact manifest sources plus campaign attempts/monitor/audit/retrospective.
Coordinator alone edits shared concepts, wiki/companies/braintree.md,
wiki/braintree-index.md and wiki/braintree-log.md. Workers/reviewers are repo
read-only and return external handoffs. Raw is immutable; reverse provenance
comes from raw_files. No collection, GitHub ingest, code/rule/schema changes,
new scheduler, worktrees, review waiver, commit/push or subsequent campaign.
Execution approved separately on2026-09-21; runtime start12:02:24Z.

Completed2026-09-21T12:26:15Z;20/20 query audit and mechanical close passed.
