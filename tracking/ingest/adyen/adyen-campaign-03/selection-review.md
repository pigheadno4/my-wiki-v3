# Adyen C03 selection and execution plan

Status: **COMPLETE — execution approved and validated**.
Prepared 2026-10-13 after C02 commit `24f92195d269900289bc43e6a7411fa688b72887` was pushed to origin/main and exact remote SHA verified.

> For agentic workers: use rules/ingest-roles.md, trusted job order and coordinator scope notes. Use the existing workflow; no new execution framework.

**Goal:** 50 previously unreferenced English General Docs retrieval sources.
**Architecture:** Existing ten shared rolling child slots, bounded by actual capacity; gpt-6-sol medium workers and different gpt-6-sol high independent first reviewers. Repository-read-only delegates; coordinator-only writes. No worktrees.
**Spec:** CLAUDE.md, rules/ingest.md, rules/psp/adyen.md and this round's dispatch-contract.md.

## Selection and evidence boundary

Select 39 remaining risk-management paths under 10,000 metadata words and 11 online-payment follow-ups. The five risk/dispute hubs run first; remaining selected pages are scheduled largest-first. Total metadata size is **42,190 words**, including code and navigation. The largest selected page is fraud-data-collection (1,554 words). These counts inform scheduling only, not risk or summary depth. Short hub/reference pages still receive a full read and independent first review.

Cover risk settings, profiles, rules, data and operational routes; scheme-specific dispute guides and timeframes; and Batch Account Updater, Giving tests/terms, legacy payout follow-ups, go-live/data tracking, regional compliance and reversal. API Explorer, GitHub, payment-method integration collection and classic-integration expansion are excluded. No network collection/refresh or unread-page behavior claims.

The 35,383-word risk-management/understanding-disputes/dispute-reason-codes page remains deferred. Also defer the exceptional 95,267-word Advanced flow, 49,628-word Sessions flow, 77,554-word online release notes, 33,163-word native 3DS2 and 10,980-word Checkout migration guide. These are scheduling exclusions, not raw_reference dispositions or semantic approvals. All other unselected raws retain their current state.

Baseline: **114 Adyen sources = 100 website + 14 GitHub**. Use existing provider concepts as retrieval hubs; do not preselect new concepts from metadata. Preserve C02 version/flow distinctions and unresolved Giving, SEPA, card-data, example and certificate qualifications when relevant. Scheme deadlines, fees, eligibility and regional legal guidance are dated snapshot claims, never universal current rules. Keep actor, object, condition, action and result identity attached.

## Fixed audit jobs

- Standard: `docs-risk-management-configure-risk-settings`.
- Longest: `docs-risk-management-fraud-data-collection`.
- Ordinary manifest sample: `docs-online-payments-reversal`.

A material exemplar partial/fail expands quality audit to every selected page. Every promoted source still receives hash, provenance, link, duplicate/catalog and count checks.

## Execution checklist

- [x] Confirm C02 completed, committed and pushed; verify exact remote main SHA.
- [x] Select latest local English snapshots and pin 50 unique jobs, URLs, raw paths and source targets; verify hashes and absent factual source ownership/targets.
- [x] Pin three distinct fixed exemplar IDs and retain the proposed provider authorization.
- [x] Obtain explicit approval of this exact manifest and dispatch-contract.md. Preparation alone grants no execution.
- [x] Recheck hashes, latest local snapshots, source ownership, C02 closure/count, shared-file ownership and native-agent capacity; initialize existing runtime only after approval.
- [x] Each worker fully reads one raw and obtains 3–5 located exact quotes, audits concepts and returns one retrieval source with semantically scoped shared suggestions.
- [x] Different strong-model reviewer performs the initial full read/review; maximum three attempts. Bound unchanged-hash fixes by actual diff/context; broad/factual uncertainty receives full review. No review waiver or automatic campaign-wide retry.
- [x] Coordinator promotes only independently approved concept updates before the corresponding source, serially. Aggregate company/index/log/count once at close.
- [x] Answer two predetermined queries/page (100 total), retaining concise locator-backed answers and bounded correction evidence; complete the three fixed full-read exemplars.
- [x] Run one complete structural close and touched typed validation; full unit suite only if code/rules/validators change. Record timestamps and qualified elapsed timing. Commit/push separately gated for the executed round.

## Fixed queries

For each exact pinned page: (1) What documentation purpose, product/object/action, actor, flow/version/environment and region/scheme scope does it establish, and what must not be inferred? (2) Can a reader navigate index → concept → source → raw to the central capability, consequential prerequisites/limits/warnings and detailed procedure/schema/examples? Answer with exact raw headings or line locators; routine detail may remain in raw. No separate redundant full audit layer.

## Pinned selection

| Order | Documentation path | Metadata words | Raw snapshot |
| --- | --- | ---: | --- |
| 1 | risk-management/configure-risk-settings | 911 | [[raw/adyen/docs/risk-management/configure-risk-settings/2026-09-15]] |
| 2 | risk-management/create-a-risk-profile | 863 | [[raw/adyen/docs/risk-management/create-a-risk-profile/2026-09-15]] |
| 3 | risk-management/configure-your-risk-profile | 1000 | [[raw/adyen/docs/risk-management/configure-your-risk-profile/2026-09-15]] |
| 4 | risk-management/understanding-disputes | 252 | [[raw/adyen/docs/risk-management/understanding-disputes/2026-09-15]] |
| 5 | risk-management/chargeback-guidelines | 168 | [[raw/adyen/docs/risk-management/chargeback-guidelines/2026-09-15]] |
| 6 | risk-management/fraud-data-collection | 1554 | [[raw/adyen/docs/risk-management/fraud-data-collection/2026-09-15]] |
| 7 | online-payments/go-live-checklist | 1429 | [[raw/adyen/docs/online-payments/go-live-checklist/2026-09-15]] |
| 8 | risk-management/chargeback-guidelines/klarna-chargebacks | 1394 | [[raw/adyen/docs/risk-management/chargeback-guidelines/klarna-chargebacks/2026-09-15]] |
| 9 | risk-management/configure-your-risk-profile/custom-rules | 1369 | [[raw/adyen/docs/risk-management/configure-your-risk-profile/custom-rules/2026-09-15]] |
| 10 | risk-management/configure-your-risk-profile/risk-lists | 1303 | [[raw/adyen/docs/risk-management/configure-your-risk-profile/risk-lists/2026-09-15]] |
| 11 | online-payments/account-updater/batch-account-updater | 1249 | [[raw/adyen/docs/online-payments/account-updater/batch-account-updater/2026-09-15]] |
| 12 | online-payments/analytics-and-data-tracking | 1248 | [[raw/adyen/docs/online-payments/analytics-and-data-tracking/2026-09-15]] |
| 13 | risk-management/manage-disputes | 1218 | [[raw/adyen/docs/risk-management/manage-disputes/2026-09-15]] |
| 14 | risk-management/configure-your-risk-profile/machine-learning-rules | 1214 | [[raw/adyen/docs/risk-management/configure-your-risk-profile/machine-learning-rules/2026-09-15]] |
| 15 | risk-management/chargeback-guidelines/riverty-chargebacks | 1159 | [[raw/adyen/docs/risk-management/chargeback-guidelines/riverty-chargebacks/2026-09-15]] |
| 16 | risk-management/automate-submitting-referrals/referrals-api-reference | 1136 | [[raw/adyen/docs/risk-management/automate-submitting-referrals/referrals-api-reference/2026-09-15]] |
| 17 | risk-management/chargeback-guidelines/pulse-chargebacks | 1120 | [[raw/adyen/docs/risk-management/chargeback-guidelines/pulse-chargebacks/2026-09-15]] |
| 18 | risk-management/chargeback-guidelines/accel-star-chargebacks | 1099 | [[raw/adyen/docs/risk-management/chargeback-guidelines/accel-star-chargebacks/2026-09-15]] |
| 19 | risk-management/understanding-disputes/dispute-timeframes | 1062 | [[raw/adyen/docs/risk-management/understanding-disputes/dispute-timeframes/2026-09-15]] |
| 20 | risk-management/chargeback-guidelines/elo-chargebacks | 991 | [[raw/adyen/docs/risk-management/chargeback-guidelines/elo-chargebacks/2026-09-15]] |
| 21 | online-payments/auspaynet-compliance-guide | 970 | [[raw/adyen/docs/online-payments/auspaynet-compliance-guide/2026-09-15]] |
| 22 | online-payments/payments-india-compliance-guide/go-live-india | 966 | [[raw/adyen/docs/online-payments/payments-india-compliance-guide/go-live-india/2026-09-15]] |
| 23 | risk-management/chargeback-guidelines/afterpay-chargebacks | 936 | [[raw/adyen/docs/risk-management/chargeback-guidelines/afterpay-chargebacks/2026-09-15]] |
| 24 | risk-management/automate-submitting-referrals | 925 | [[raw/adyen/docs/risk-management/automate-submitting-referrals/2026-09-15]] |
| 25 | risk-management/chargeback-guidelines/mastercard-chargebacks | 915 | [[raw/adyen/docs/risk-management/chargeback-guidelines/mastercard-chargebacks/2026-09-15]] |
| 26 | risk-management/chargeback-guidelines/diners-discover-chargebacks | 910 | [[raw/adyen/docs/risk-management/chargeback-guidelines/diners-discover-chargebacks/2026-09-15]] |
| 27 | risk-management/run-ab-test-experiments | 891 | [[raw/adyen/docs/risk-management/run-ab-test-experiments/2026-09-15]] |
| 28 | online-payments/donations/testing | 879 | [[raw/adyen/docs/online-payments/donations/testing/2026-09-15]] |
| 29 | risk-management/shopper-dna | 868 | [[raw/adyen/docs/risk-management/shopper-dna/2026-09-15]] |
| 30 | risk-management/configure-your-risk-profile/post-auth-rules | 855 | [[raw/adyen/docs/risk-management/configure-your-risk-profile/post-auth-rules/2026-09-15]] |
| 31 | risk-management/chargeback-guidelines/unionpay-chargebacks | 817 | [[raw/adyen/docs/risk-management/chargeback-guidelines/unionpay-chargebacks/2026-09-15]] |
| 32 | risk-management/chargeback-guidelines/american-express-chargebacks | 716 | [[raw/adyen/docs/risk-management/chargeback-guidelines/american-express-chargebacks/2026-09-15]] |
| 33 | online-payments/payments-india-compliance-guide | 715 | [[raw/adyen/docs/online-payments/payments-india-compliance-guide/2026-09-15]] |
| 34 | risk-management/chargeback-guidelines/jcb-chargebacks | 698 | [[raw/adyen/docs/risk-management/chargeback-guidelines/jcb-chargebacks/2026-09-15]] |
| 35 | risk-management/chargeback-guidelines/mexicodomestic-chargebacks | 689 | [[raw/adyen/docs/risk-management/chargeback-guidelines/mexicodomestic-chargebacks/2026-09-15]] |
| 36 | risk-management/configure-your-risk-profile/risk-field-reference | 686 | [[raw/adyen/docs/risk-management/configure-your-risk-profile/risk-field-reference/2026-09-15]] |
| 37 | risk-management/chargeback-guidelines/billdesk-chargebacks | 685 | [[raw/adyen/docs/risk-management/chargeback-guidelines/billdesk-chargebacks/2026-09-15]] |
| 38 | risk-management/control-traffic | 677 | [[raw/adyen/docs/risk-management/control-traffic/2026-09-15]] |
| 39 | online-payments/reversal | 672 | [[raw/adyen/docs/online-payments/reversal/2026-09-15]] |
| 40 | risk-management/chargeback-guidelines/eftpos-chargebacks | 668 | [[raw/adyen/docs/risk-management/chargeback-guidelines/eftpos-chargebacks/2026-09-15]] |
| 41 | risk-management/chargeback-guidelines/sepa-chargebacks | 625 | [[raw/adyen/docs/risk-management/chargeback-guidelines/sepa-chargebacks/2026-09-15]] |
| 42 | risk-management/chargeback-guidelines/nyce-chargebacks | 552 | [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15]] |
| 43 | online-payments/online-payouts/payout-webhook | 539 | [[raw/adyen/docs/online-payments/online-payouts/payout-webhook/2026-09-15]] |
| 44 | risk-management/chargeback-guidelines/twint-chargebacks | 522 | [[raw/adyen/docs/risk-management/chargeback-guidelines/twint-chargebacks/2026-09-15]] |
| 45 | risk-management/chargeback-uploader | 476 | [[raw/adyen/docs/risk-management/chargeback-uploader/2026-09-15]] |
| 46 | risk-management/chargeback-guidelines/cash-app-pay-chargebacks | 433 | [[raw/adyen/docs/risk-management/chargeback-guidelines/cash-app-pay-chargebacks/2026-09-15]] |
| 47 | online-payments/online-payouts/payouts-to-a-bank-account | 394 | [[raw/adyen/docs/online-payments/online-payouts/payouts-to-a-bank-account/2026-09-15]] |
| 48 | online-payments/donations/terms-and-conditions | 363 | [[raw/adyen/docs/online-payments/donations/terms-and-conditions/2026-09-15]] |
| 49 | risk-management/skip-risk-rules | 281 | [[raw/adyen/docs/risk-management/skip-risk-rules/2026-09-15]] |
| 50 | risk-management/chargeback-guidelines/cartes-bancaires-chargebacks | 128 | [[raw/adyen/docs/risk-management/chargeback-guidelines/cartes-bancaires-chargebacks/2026-09-15]] |

Approval applied only to this manifest and provider authorization. Execution is complete; campaign state, independent reviews, promoted sources, concept updates and final validation are retained here. No C03 commit or push.
