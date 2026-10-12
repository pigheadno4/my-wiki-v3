# Adyen C01 selection and execution plan

Status: COMPLETE after explicit approval of the exact manifest and provider authorization. Fifty sources and 100 fixed queries completed; no collection, commit or push authorized.

> **For agentic workers:** Use the existing coordinator-controlled campaign workflow in CLAUDE.md and rules/ingest.md; delegated roles use rules/ingest-roles.md. No new execution framework.

**Goal:** Generate 50 grounded retrieval sources for previously unreferenced Adyen website pages.

**Architecture:** One complete raw page per job; proposed rolling pool of ten children shared by workers/reviewers/query auditors, excluding coordinator. Different strong-model independent initial reviewer per job. Only coordinator writes repository/canonical/shared files.

**Tech Stack:** Existing filesystem campaign artifacts and Python structural validators.

**Spec:** rules/ingest.md, rules/psp/adyen.md and dispatch-contract.md (proposed Adyen-specific authorization).

## Scope and constraints

50 General Docs pages, no API Explorer or GitHub ingestion. Select latest locally collected snapshot per exact documentation path; pin immutable bytes by SHA-256. Selection is metadata-only, not semantic ingestion or a low-risk verdict. No claims may be inferred from titles/URLs alone.

Cover online-payment overview and lifecycle, tokenization, 3DS/SCA, API access/idempotency/security, webhook handling and testing. Five broad overview routes first, then remaining selected pages descending by metadata word count to reduce tail blocking. Total 95,531 words; word count includes captured code and navigation, not semantic complexity.

Defer two exceptional long guides: online-payments/build-your-integration/advanced-flow (95,267 words), sessions-flow (49,628 words). This is scheduling only, not a raw_reference classification. No partial-read shortcut.

## Review focus

- Keep sessions/advanced/classic integration and client/server/environment distinctions; unread linked guides are navigation, not evidence.
- Preserve object/event/action qualifiers in capture, refund, cancel and token management; do not invent universal lifecycle guarantees.
- Webhook receipt/authenticity/processing and synchronous payment results are distinct; preserve locally documented qualifications.
- 3DS/SCA guidance retains geography, flow and exception boundaries; snapshot content does not prove current universal compliance.
- Concepts default to purpose-fit retrieval routes; factual evidence and navigation-only raw links remain separate. Check exact path-qualified links because raw filenames are dates.

## Files and execution steps

- [x] Prepare exact 50-job manifest and proposed provider dispatch authorization.
- [x] Verify unique jobs/URLs/targets, hash pins, latest local snapshots and absence from source raw_files.
- [x] Obtain explicit approval of this manifest and dispatch-contract.md before initializing runtime or spawning.
- [x] Initialize existing campaign.json/jobs.json/events.jsonl/monitor.md pattern; no new schema or scheduler. Persist all per-job attempts and receipts; raw remains immutable.
- [x] Full raw read, concept audit, 3–5 located literal primary-raw quotes and retrieval candidate per job; independent first full review; maximum three attempts. Unchanged-evidence bounded fixes may use targeted diff review; factual/uncertain failures require full review.
- [x] Coordinator promotes approved concept updates before their sources, serially; aggregate company/index/log/count once at close. No default coordinator third full read.
- [x] Complete fixed query questions below for all 50 jobs, resolve material failures, then one structural close and one touched-page validation. No full unit suite absent code/rule changes.
- [x] Record first-pass rate, retries, started_at/completed_at and timing limitations; commit/push approval remains a separate future action.

## Fixed query checks

For each exact selected page: (1) What document/product/object/action and environment/flow scope does this source establish, and what must not be inferred? (2) What central purpose and material qualifications/warnings are retained, and where are the detailed procedures/schema/examples retrievable in the pinned raw? Direct answers with locators; no report-polishing pass.

Three fixed audit exemplars: `docs-online-payments`, `docs-online-payments-psd2-sca-compliance-and-implementation-guide-sca-options`, `docs-development-resources-api-authentication` (standard overview, longest selected page, ordinary sample). Material failure expands sampling to the complete campaign. Broken links, duplicate catalog entries, counts and raw hashes always checked for all jobs.

## Pinned 50-page list

| Order | Job | Words | Raw |
| --- | --- | ---: | --- |
| 1 | docs-online-payments | 626 | [[raw/adyen/docs/online-payments/2026-09-15]] |
| 2 | docs-online-payments-build-your-integration | 547 | [[raw/adyen/docs/online-payments/build-your-integration/2026-09-15]] |
| 3 | docs-online-payments-tokenization | 997 | [[raw/adyen/docs/online-payments/tokenization/2026-09-15]] |
| 4 | docs-online-payments-3d-secure | 594 | [[raw/adyen/docs/online-payments/3d-secure/2026-09-15]] |
| 5 | docs-development-resources-webhooks | 662 | [[raw/adyen/docs/development-resources/webhooks/2026-09-15]] |
| 6 | docs-online-payments-psd2-sca-compliance-and-implementation-guide-sca-options | 7169 | [[raw/adyen/docs/online-payments/psd2-sca-compliance-and-implementation-guide/sca-options/2026-09-16]] |
| 7 | docs-online-payments-adjust-authorisation-adjust-with-preauth | 6755 | [[raw/adyen/docs/online-payments/adjust-authorisation/adjust-with-preauth/2026-09-15]] |
| 8 | docs-online-payments-3d-secure-standalone-authentication | 5379 | [[raw/adyen/docs/online-payments/3d-secure/standalone-authentication/2026-09-15]] |
| 9 | docs-development-resources-webhooks-webhook-types | 5141 | [[raw/adyen/docs/development-resources/webhooks/webhook-types/2026-09-15]] |
| 10 | docs-online-payments-3d-secure-redirect-3ds2-web-drop-in | 4733 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/web-drop-in/2026-09-15]] |
| 11 | docs-online-payments-capture | 4368 | [[raw/adyen/docs/online-payments/capture/2026-09-15]] |
| 12 | docs-online-payments-tokenization-create-tokens | 4257 | [[raw/adyen/docs/online-payments/tokenization/create-tokens/2026-09-15]] |
| 13 | docs-online-payments-refund | 3913 | [[raw/adyen/docs/online-payments/refund/2026-09-15]] |
| 14 | docs-online-payments-tokenization-make-token-payments | 3769 | [[raw/adyen/docs/online-payments/tokenization/make-token-payments/2026-09-15]] |
| 15 | docs-online-payments-partial-payments | 3010 | [[raw/adyen/docs/online-payments/partial-payments/2026-09-15]] |
| 16 | docs-online-payments-partial-authorizations | 2639 | [[raw/adyen/docs/online-payments/partial-authorizations/2026-09-15]] |
| 17 | docs-online-payments-network-tokenization | 2560 | [[raw/adyen/docs/online-payments/network-tokenization/2026-09-15]] |
| 18 | docs-online-payments-3d-secure-for-regulation-compliance | 2210 | [[raw/adyen/docs/online-payments/3d-secure-for-regulation-compliance/2026-09-15]] |
| 19 | docs-online-payments-adjust-authorisation | 2175 | [[raw/adyen/docs/online-payments/adjust-authorisation/2026-09-15]] |
| 20 | docs-online-payments-cancel | 1922 | [[raw/adyen/docs/online-payments/cancel/2026-09-15]] |
| 21 | docs-development-resources-webhooks-configure-and-manage | 1873 | [[raw/adyen/docs/development-resources/webhooks/configure-and-manage/2026-09-15]] |
| 22 | docs-development-resources-webhooks-webhook-types-additional-settings | 1851 | [[raw/adyen/docs/development-resources/webhooks/webhook-types/additional-settings/2026-09-15]] |
| 23 | docs-online-payments-surcharge | 1828 | [[raw/adyen/docs/online-payments/surcharge/2026-09-15]] |
| 24 | docs-online-payments-web-best-practices | 1793 | [[raw/adyen/docs/online-payments/web-best-practices/2026-09-15]] |
| 25 | docs-online-payments-tokenization-managing-tokens | 1710 | [[raw/adyen/docs/online-payments/tokenization/managing-tokens/2026-09-15]] |
| 26 | docs-development-resources-webhooks-secure-webhooks-verify-hmac-signatures | 1623 | [[raw/adyen/docs/development-resources/webhooks/secure-webhooks/verify-hmac-signatures/2026-09-15]] |
| 27 | docs-development-resources-api-credentials | 1545 | [[raw/adyen/docs/development-resources/api-credentials/2026-09-15]] |
| 28 | docs-development-resources-api-idempotency | 1350 | [[raw/adyen/docs/development-resources/api-idempotency/2026-09-15]] |
| 29 | docs-development-resources-response-handling | 1253 | [[raw/adyen/docs/development-resources/response-handling/2026-09-15]] |
| 30 | docs-online-payments-capture-failure-reasons | 1241 | [[raw/adyen/docs/online-payments/capture/failure-reasons/2026-09-15]] |
| 31 | docs-development-resources-testing-payments-and-modifications | 1240 | [[raw/adyen/docs/development-resources/testing/payments-and-modifications/2026-09-15]] |
| 32 | docs-online-payments-checkout-settings | 1164 | [[raw/adyen/docs/online-payments/checkout-settings/2026-09-15]] |
| 33 | docs-online-payments-build-your-integration-payment-result-codes | 1099 | [[raw/adyen/docs/online-payments/build-your-integration/payment-result-codes/2026-09-15]] |
| 34 | docs-online-payments-two-step-checkout | 1013 | [[raw/adyen/docs/online-payments/two-step-checkout/2026-09-15]] |
| 35 | docs-online-payments-3d-secure-data-only | 998 | [[raw/adyen/docs/online-payments/3d-secure/data-only/2026-09-15]] |
| 36 | docs-online-payments-co-badged-cards-compliance | 974 | [[raw/adyen/docs/online-payments/co-badged-cards-compliance/2026-09-15]] |
| 37 | docs-development-resources-api-credentials-roles | 971 | [[raw/adyen/docs/development-resources/api-credentials/roles/2026-09-15]] |
| 38 | docs-development-resources-live-endpoints | 924 | [[raw/adyen/docs/development-resources/live-endpoints/2026-09-15]] |
| 39 | docs-development-resources-webhooks-troubleshoot | 878 | [[raw/adyen/docs/development-resources/webhooks/troubleshoot/2026-09-15]] |
| 40 | docs-online-payments-3d-secure-authorize-mpidata | 828 | [[raw/adyen/docs/online-payments/3d-secure/authorize-mpidata/2026-09-15]] |
| 41 | docs-development-resources-webhooks-secure-webhooks | 820 | [[raw/adyen/docs/development-resources/webhooks/secure-webhooks/2026-09-15]] |
| 42 | docs-online-payments-card-encryption-with-jwe | 760 | [[raw/adyen/docs/online-payments/card-encryption-with-jwe/2026-09-15]] |
| 43 | docs-development-resources-webhooks-handle-webhook-events | 740 | [[raw/adyen/docs/development-resources/webhooks/handle-webhook-events/2026-09-15]] |
| 44 | docs-online-payments-accessibility | 729 | [[raw/adyen/docs/online-payments/accessibility/2026-09-15]] |
| 45 | docs-development-resources-testing-tokenization | 699 | [[raw/adyen/docs/development-resources/testing/tokenization/2026-09-15]] |
| 46 | docs-development-resources-security-api-security | 618 | [[raw/adyen/docs/development-resources/security/api-security/2026-09-15]] |
| 47 | docs-online-payments-integration-checklist | 524 | [[raw/adyen/docs/online-payments/integration-checklist/2026-09-15]] |
| 48 | docs-online-payments-psd2-sca-compliance-and-implementation-guide | 489 | [[raw/adyen/docs/online-payments/psd2-sca-compliance-and-implementation-guide/2026-09-15]] |
| 49 | docs-development-resources-testing | 301 | [[raw/adyen/docs/development-resources/testing/2026-09-15]] |
| 50 | docs-development-resources-api-authentication | 269 | [[raw/adyen/docs/development-resources/api-authentication/2026-09-15]] |
