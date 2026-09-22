# Braintree C14 ten-page execution plan

Status: COMPLETE — exact-manifest execution approved2026-09-22.

**Goal:** Add ten unowned website raws as retrieval entries, complementing the already ingested API endpoints.
**Architecture:** Existing three dynamic child slots; Sol medium workers and different Sol high initial reviewers; coordinator-only canonical/shared writes.
**Tech Stack:** Existing Python runtime, JSON handoffs and Markdown. No code changes.
**Spec:** CLAUDE.md, rules/ingest.md, rules/psp/braintree-ingest.md, adopted rules/psp/metronome-ingest.md and dispatch-contract.md here.

## Exact selection and twenty fixed questions

| Job | Raw lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| recurring-billing-manage-node | 261 | Where is Braintree Recurring Billing Manage documented? | What status-dependent update, proration, retry and refund qualifications matter, and where are detailed scenarios located? |
| recurring-billing-testing-go-live-node | 251 | Where is Braintree Recurring Billing Testing and Go Live documented? | What sandbox testing and production-transition steps or warnings are stated, without treating test data as live behavior? |
| recurring-billing-create-node | 133 | Where is Braintree Recurring Billing Create documented? | What prerequisites, plan inheritance and transaction-flow or timing qualifications are documented? |
| recurring-billing-overview | 64 | Where is Braintree Recurring Billing Overview documented? | What availability boundary, integration flow and subscription-status meanings are documented? |
| recurring-billing-plans-node | 83 | Where is Braintree Recurring Billing Plans documented? | What role do plans and add-ons or discounts play, and which creation or modification boundaries are stated? |
| transactions-guide-node | 135 | Where is Braintree Transactions Guide documented? | How are authorization, settlement, validation and dispute routes distinguished, with what material qualifications? |
| webhooks-disbursement-node | 38 | Where is Braintree Disbursement Webhooks documented? | What event conditions and payload categories are stated, without inferring merchant payout guarantees? |
| webhooks-sub-merchant-account-node | 34 | Where is Braintree Sub-merchant Account Webhooks documented? | Which account-event conditions and payload routes are stated, distinct from creating or activating an account? |
| webhooks-test-node | 32 | Where is Braintree Test Webhooks documented? | What triggers the test notification and what payload limits are documented, distinct from a real payment event? |
| webhooks-braintree-auth-node | 36 | Where is Braintree Braintree Auth Webhooks documented? | What beta scope, event conditions and payload categories are stated without importing OAuth or Grant behavior? |

Selection uses metadata, headings and opening excerpts, not a complete semantic
read. Ten hashes/URLs/targets pinned in manifest.json; no factual raw owner,
canonical owner or existing source target at preparation. Navigation-only
references from earlier sources do not count as prior ingestion. Baseline101
=85 website+16 GitHub; expected111=95+16 if all approve and no concurrent
additions. Recalculate at close. C13 complete and pushed before preparation.

Queue longer manage/testing/create guides first, then overview/plans and short
references. Guide pages can add lifecycle qualifications absent from earlier
endpoint retrieval entries; distinguish evidence scope from actual contradiction.
Never force every guide paragraph into source facts. Retain consequential
warnings, conditions and meaning; route routine tables/test values/examples
to verified raw locators. Preserve beta/Marketplace, SDK and test-versus-live
scope, damaged rendering and event-versus-operation boundaries.

Provisional concepts: recurring-payments, braintree-server-sdk and
braintree-webhooks. Use the existing index-led concept audit. Add a concept only
for a genuine gap, not automatically per guide. Adjacent authority requires a
retained cross-source claim or actual conflict; no blanket reference fan-out.

## Fixed audit groups

A: Recurring Billing Overview + Plans.
B: Recurring Billing Create + Manage.
C: Recurring Billing Testing and Go Live + Transactions Guide.
D: Disbursement + Sub-merchant Account Webhooks.
E: Test + Braintree Auth Webhooks.

Four predetermined questions per group,20 total; no additional three-page
audit. Full selected evidence reads, one actual route per page, direct answer,
object/action match, exact locator and verdict per question. One gap sweep and
completeness record per group. Start ready groups under the same3-slot capacity.

## Execution checklist after approval

- [x] Recheck10 hashes, absent raw/canonical/source owners, C13 completion and actual capacity; initialize only this campaign.
- [x] Persist trusted orders then dispatch immediately. One full raw per worker, concept audit first,3–5 exact located primary quotes, existing8-key external handoff, no repository writes.
- [x] Different reviewer reads complete first raw/candidate/quotes/suggestions. Block misleading claims, material warning omissions or broken routes, not optional schema detail. Maximum3 attempts; bounded corrections use targeted review when impact is bounded.
- [x] Promote approved concepts then exact source serially. Review priority/worker reserve; no batch barriers. Dispatch before reports; ready query groups share the3 slots.
- [x] Aggregate company/index/log/count once; check candidates, hashes, identities, unique primary owners, supporting evidence, approved snippets, required/reciprocal links, duplicates, counts and touched typed files. No documentation-only code suite.
- [x] Complete20 fixed query answers, resolving concrete failures only; preserve unrelated passes.
- [x] Close runtime and record first-pass rate, retries, actual UTC observations and elapsed time in quality-audit.md/retrospective.md. Overlapping spans are not additive.

## C13 lessons within existing rules

Do not change receipt schema: all3–5 receipt quotes come from the primary raw.
When a retained actual conflict needs supporting authority, read that authority
fully and identify its exact excerpt/locator in existing warning text. Use an
external narrowly scoped reciprocal-warning proposal for an existing source
when needed; reviewer explicitly approves it before coordinator writes. No new
registry or validator. Keep fully read supporting raw distinct from primary
ownership and navigation-only references. Record any exact mechanical wording
repair without mutating prior receipts or silently accepting broader diffs.

## Scope and approval boundary

Only manifest source targets, campaign-local artifacts, approved concept routes,
Braintree company/index/log/count and bounded independently reviewed reciprocal
conflict warnings if needed. Raw immutable; no collection, GitHub ingest, code/
rule/validator changes, review waiver, new scheduler, commit/push or subsequent
campaign. Execution separately approved2026-09-22; runtime and agents started. Other task changes
must be preserved. Ten pages is scope, not a promised speedup.
