# Braintree C12 ten-page execution plan

Status: COMPLETE; exact-manifest execution approved2026-09-21.

**Goal:** Add ten unowned website raws as useful retrieval entries.
**Architecture:** Existing Sol medium workers, different Sol high initial reviewers, three dynamic child slots including auditors; coordinator-only canonical/shared writes.
**Tech Stack:** Existing Python runtime, JSON handoffs and Markdown; no code changes.
**Spec:** rules/ingest.md, rules/psp/braintree-ingest.md, rules/psp/metronome-ingest.md and dispatch-contract.md here.

## Exact selection and fixed20 questions

| Job | Raw lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| dispute-add-text-evidence-node | 220 | Where is Node dispute text-evidence addition documented? | What access/status restrictions and evidence-content routes are documented, and how is adding evidence distinguished from final submission? |
| merchant-account-create-node | 116 | Where is Node merchant-account creation documented? | What identity/funding/agreement inputs and result handling do the examples establish without implying universal onboarding eligibility? |
| merchant-account-create-for-currency-node | 63 | Where is Node merchant-account creation for a currency documented? | What Braintree Auth availability restriction and currency/input/result guidance is stated? |
| merchant-account-update-node | 41 | Where is Node merchant-account updates documented? | What account identifier, changes and result handling are shown, and which wider update effects are not established? |
| merchant-account-all-node | 30 | Where is Node merchant-account listing documented? | How are the returned account collection and callback consumed without importing account-creation behavior? |
| merchant-account-find-node | 25 | Where is Node single merchant-account lookup documented? | What identifier, callback and not-found guidance is stated, and where are response details routed? |
| webhooks-grant-api-node | 47 | Where is Node Grant API webhooks documented? | Which granted-instrument event conditions and payload categories are documented, distinct from granting or revoking access? |
| webhooks-oauth-node | 82 | Where is Node OAuth webhooks documented? | What production/sandbox availability and event/payload qualifications are stated? |
| webhooks-local-payment-methods-node | 36 | Where is Node local-payment-method webhooks documented? | How do instant and non-instant events differ, and which event requires a separate transaction-creation action? |
| settlement-batch-summary-generate-node | 40 | Where is Node settlement batch summary generation documented? | What date/grouping/report scope and result access are documented, distinct from submitting a transaction for settlement? |

Total700 logical raw lines. Selection used metadata/headings/opening excerpts,
not a complete semantic read. All ten exact raw paths/hashes/URLs pinned in
manifest.json; targets and current raw/canonical owners absent at preparation.
C11 verified complete. Baseline81 sources=65 website+16 GitHub; expected91=75+16
if all approve and no concurrent source additions. Recalculate before closing.

Selection extends C11 dispute evidence, merchant-account operations and existing
webhook/reporting retrieval. Apple Pay Node register/unregister/list pages were
not selected: their short content mainly repeats a PHP/Ruby-only availability
notice. This is selection deferral, not a raw_reference disposition or permanent
exclusion. No unsupported Node capability may be inferred from their URL.

Provisional main concepts: disputes, braintree-server-sdk, braintree-webhooks.
Each full-read worker audits existing routes; add a concept only for a genuine
uncovered topic, never a mandatory one per endpoint. Preserve actual conflicts
with existing sources, including add-evidence versus finalize terminology;
read adjacent authority only if needed for a retained claim or real conflict.

## Five fixed audit groups

A: Dispute Add Text Evidence + Merchant Account Create.
B: Merchant Account Create For Currency + Update.
C: Merchant Account All + Find.
D: Grant API Webhooks + OAuth Webhooks.
E: Local Payment Methods Webhooks + Settlement Batch Summary Generate.

Each group answers its four table questions; together one20-question audit.
No extra three-page audit. Groups may overlap remaining ingestion when their
sources are promoted and capacity permits. No blanket neighboring raw reads.

## Execution checklist after approval

- [x] Recheck all10 hashes, source/canonical/raw ownership, C11 complete and actual capacity. Initialize only braintree/braintree-campaign-12.
- [x] Persist trusted orders then promptly dispatch. Worker fully reads one raw, audits concepts index-first and returns one narrow source,3–5 exact located quotes and existing8-key result; no repository writes.
- [x] Different Sol high reviewer fully reads each first raw/candidate/quotes/suggestions. Block misleading retained claims, material missing warnings and broken routes, not optional API inventories. Maximum3 attempts; bounded fixes use targeted diff/context review where justified.
- [x] Coordinator serially promotes approved concept changes then exact candidates. Fill eligible slots promptly under existing review priority/worker reserve; auditors share the3-slot cap. Start ready groups without waiting for the whole campaign.
- [x] Aggregate company/provider-index/provider-log/count once. Validate all promoted candidate equality, raw hashes/canonical identity, unique owners, required and reciprocal links, approved snippets, duplicate catalogs, counts and touched typed pages once. No documentation-only code suite.
- [x] Verify20 fixed query answers: actual route, correct object/action, direct answer, exact locator and verdict; one gap sweep/completeness check per group. Resolve concrete failures only.
- [x] Close runtime; record timing, first-pass rate and retries in existing quality-audit.md/retrospective.md. Distinguish queue/setup/delivery from self-reported analysis; overlapping spans are not additive.

## Scope and ownership

Exact source targets in manifest; campaign-local attempts/state/monitor/audit/
retrospective; approved concept updates; wiki/companies/braintree.md,
wiki/braintree-index.md and wiki/braintree-log.md. Workers/reviewers return
external handoffs only. Shared writes stay serial with coordinator. Preserve
concurrent GitHub/other-PSP edits. Raw is immutable, reverse provenance uses
raw_files. No collection, GitHub ingest, historical rewrite, code/rule changes,
review waiver, new scheduler/registry, commit/push or subsequent campaign.
Execution separately approved2026-09-21; runtime start12:36:08Z.
