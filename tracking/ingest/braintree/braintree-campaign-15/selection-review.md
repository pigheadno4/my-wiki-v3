# Braintree C15 ten-page execution plan

Status: COMPLETE — exact manifest execution approved and closed 2026-09-23.

**Goal:** Add ten previously unowned website raws as retrieval entries for server SDK usage, lifecycle and response/error handling.
**Architecture:** Existing three dynamic child slots; Sol medium workers, different Sol high initial reviewers; coordinator-only canonical/shared/state writes.
**Tech Stack:** Existing Python runtime, JSON handoffs and Markdown; no code changes.
**Spec:** CLAUDE.md, rules/ingest.md, rules/psp/braintree-ingest.md, adopted rules/psp/metronome-ingest.md and dispatch-contract.md here.

## Exact selection and twenty fixed questions

| Job | Raw lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| best-practices-node | 204 | Where is Braintree Best Practices (Node.js) documented? | Which integration, timeout, version and transport-security qualifications must remain visible, and where are exact configuration details? |
| authorization-responses | 192 | Where is Braintree Authorization Responses documented? | How are approvals, decline categories and retry restrictions distinguished, including the stated merchant-fee qualification? |
| exceptions-node | 156 | Where is Braintree Exceptions (Node.js) documented? | How are exception handling and timeout/error categories distinguished without inferring transaction outcome or safe retry? |
| result-objects-node | 142 | Where is Braintree Result Objects (Node.js) documented? | What does a result object establish, which calls return other shapes, and where are success versus validation-error details? |
| server-sdk-deprecation-policy | 81 | Where is Braintree Server SDK Deprecation Policy documented? | What lifecycle categories and update guidance are stated, without treating the collected version list as current support? |
| server-sdk-migration-guide-node | 73 | Where is Braintree Server SDK Migration Guide (Node.js) documented? | Which language/version scope and migration changes are documented, distinct from a universal current upgrade requirement? |
| upgrade | 62 | Where is Braintree Upgrade to Braintree SDKs documented? | Which historical integration paths and upgrade routes are described, without asserting current feature availability? |
| settlement-responses | 50 | Where is Braintree Settlement Responses documented? | How are settlement approval, pending and decline responses distinguished without turning a pending request into final settlement? |
| avs-cvv-responses | 46 | Where is Braintree AVS and CVV Responses documented? | Which AVS and CVV result categories are documented, and what cannot be inferred from the damaged response-object introduction? |
| merchant-advice-codes | 39 | Where is Braintree Merchant Advice Codes documented? | What do optional Mastercard advice codes communicate about declines and possible retries, without overriding other retry restrictions? |

Total1045 logical raw lines. Selection uses metadata, headings and opening
excerpts, not complete semantic reads. Hashes, canonical URLs and source targets
are pinned in manifest.json. All ten lack factual raw ownership, canonical
ownership and an existing target at preparation. Navigation-only references
do not count as prior ingestion.

C14 completed and was committed/pushed as35c5a9e1f1fb58c308bed6083e9b41fbb6b3b35a
to origin/main before preparation. Baseline111=95website+16GitHub; expected121
=105+16 if all approve and no concurrent additions. Recalculate at execution
and close. This count does not claim raw-corpus completion.

## Scope and selection judgment

Queue longer Best Practices/Authorization/Exceptions/Result Objects first.
Preserve actual SDK/version and historical migration scope. Collected version,
cipher and support tables are evidence as collected, not current recommendations.
Processor approval, gateway success, authorization, capture request, pending
settlement and final settlement must not be collapsed. Preserve damaged
rendering; never reconstruct missing response object names.

The class-level-versus-instance-methods Node-URL page was excluded from this
round because its opening says the subject applies to specified legacy
Ruby/Python/PHP integrations, not Node. Apple Pay domain request pages and
standalone verification remain outside this manifest; no disposition change
or claim that those pages are unnecessary is made.

Provisional main concept: braintree-server-sdk. Use index-led concept audit for
a meaningful additional route; no automatic concept per error family. Concept
updates default to reciprocal retrieval entries, not code tables or version
inventories. A genuine missing principal topic can justify a provider concept
under existing rules. Read adjacent authority only for a retained cross-source
claim or an actual relevant conflict, never blanket fan-out.

## Fixed query groups

A: Result Objects + Exceptions.
B: Authorization Responses + Merchant Advice Codes.
C: AVS and CVV Responses + Settlement Responses.
D: Best Practices + Server SDK Deprecation Policy.
E: Server SDK Migration Guide + Upgrade to Braintree SDKs.

Exactly four questions per group,20 total; no extra three-page audit.
Each selected raw is read completely; record one actual route per page and
direct answer/object-action/exact locator/verdict per question. One bounded
gap sweep and completeness record per group. Ready groups may overlap remaining
jobs within the same three-slot cap.

## Execution checklist after approval

- [x] Recheck all hashes, absent owners/targets, C14 completion, baseline counts and actual capacity; initialize only this campaign.
- [x] Persist each trusted order and dispatch immediately. Each worker fully reads one primary raw, audits concepts, drafts a narrow retrieval source and extracts3–5 exact located primary quotes.
- [x] Obtain a different reviewer's complete initial raw/candidate/quotes/suggestions review. Maximum3 attempts; bounded correction review uses unchanged evidence, prior findings and actual diff, not hash alone.
- [x] Incrementally promote approved concept updates then exact source; coordinator writes only. Follow existing review priority/worker reserve without batch barriers.
- [x] Aggregate company/index/log/count once; run one mechanical close for equality, identity, hashes, links, ownership, duplicate catalogs, approved snippets, counts and touched typed files.
- [x] Complete all20 fixed query answers; repair concrete defects only, preserving unrelated passes.
- [x] Close runtime and record first-pass rate, full/targeted reviews, bounded repairs and actual UTC stage observations. Do not sum overlapping windows.

## C14 lessons without additional gates

Apply the existing drafting subject/condition/action self-check: preserve exact
nouns and alternatives instead of broader synonyms; retain a consequential
qualification when summarizing a lifecycle. Default routine fields to raw
locators; if retaining a field, verify its actual SDK spelling rather than a
prose/link label. Keep the source's corrected qualification in query answers.
One ready Markdown concept snippet and one real heading anchor per update ID;
do not wrap proposals in narrative instructions or combine headings.

Reports return when complete, without stylistic polishing. Coordinator fills an
available slot before promotion narration or retrospective writing. Store
required time observations, defer prose until close. No new schema, registry,
validator, mandatory checklist artifact or review round.

## Approval boundary

Preparation ended with explicit approval on 2026-09-23. Execution may write
manifest source targets, approved concept routes and
Braintree company/index/log/count plus campaign artifacts; no collection,
GitHub ingest, code/rule changes, review waiver, commit/push or next campaign
without separate authority. Preserve unrelated shared-checkout work.
