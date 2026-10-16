# Adyen C14 selection and execution plan

Status: **COMPLETE — execution approved and validated**.
Prepared 2026-10-16 after C13 commit `a8b6d16dafbab9bd6499b09ff75f3c48caaa0589` was pushed; exact remote main verification is recorded in preflight-validation.json.

50 previously unreferenced English General Docs snapshots: **22 remaining eligible plugin guides** (Cegid 6, Microsoft Dynamics 1, Mirakl 8, Salesforce OMS 7), **16 industry/market guides**, **8 partner/OAuth guides**, **2 reporting guides**, and **2 payments/financial-products orientation pages**.

Four connector/partner orientation pages first; remaining pages largest-first. Total **47,470 metadata words**, including schemas/examples; each page below 10,000 metadata words. Metadata selection is not semantic approval or current availability.

Baseline **664 = 650 website + 14 GitHub summaries**. Audit existing Adyen account structure, API access, IAM, webhooks, tokenization, capture/refund, payouts, POS, reporting, Salesforce and generic OAuth concepts through indexes first. New connector/partner concepts require genuine gaps and independent approval before source promotion. No new payment architecture or live operational choice is preselected.

Localized Japanese SCTA/PSA page is explicitly excluded even though its metadata says en; the title and content are Japanese. Its separate English canonical page is selected. Oversized plugin release notes, all other product families, API Explorer and GitHub remain deferred. No raw collection, connector installation, OAuth authorization/token requests, account/seller/admin changes, financial operations, legal refresh or raw_reference reclassification.

Ten shared rolling child slots with gpt-6-sol medium workers and different high independent first reviewers; repository-read-only delegates and coordinator-only writes, no worktrees. One full pinned raw per source, 3–5 exact located quotes, full initial independent review, at most three attempts and bounded corrections. [Exact proposed provider authorization](dispatch-contract.md). Concept-before-source promotion; aggregate company/catalog/log/count once at close; 100 fixed locator-backed answers and three coordinator full-read exemplars; exhaustive structural and touched typed validation. No framework/code/rule/schema/validator changes.

## Fixed exemplars

- `docs-plugins-mirakl`.
- `docs-plugins-cegid-retail-y2-set-up-the-plugin`.
- `docs-partners-oauth-integration`.

## Preparation checks

- [x] C13 complete, committed and pushed; exact remote SHA verified.
- [x] 50 unique jobs/URLs/latest pins/absent targets and factual ownership.
- [x] 50 hashes, English metadata/title check, localized exception exclusion, size and review/routing configuration checked.
- [x] Three distinct fixed exemplars in exact manifest.
- [x] Explicit approval before execution.

## Exact selection

| # | Path | Metadata words | Raw |
| --- | --- | ---: | --- |
| 1 | plugins/mirakl | 488 | [[raw/adyen/docs/plugins/mirakl/2026-09-15]] |
| 2 | plugins/salesforce-order-management-system | 548 | [[raw/adyen/docs/plugins/salesforce-order-management-system/2026-09-15]] |
| 3 | plugins/cegid-retail-y2 | 657 | [[raw/adyen/docs/plugins/cegid-retail-y2/2026-09-15]] |
| 4 | partners | 437 | [[raw/adyen/docs/partners/2026-09-15]] |
| 5 | plugins/cegid-retail-y2/set-up-the-plugin | 3462 | [[raw/adyen/docs/plugins/cegid-retail-y2/set-up-the-plugin/2026-09-15]] |
| 6 | plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup | 3044 | [[raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup/2026-09-15]] |
| 7 | partners/uplift-enablement | 2535 | [[raw/adyen/docs/partners/uplift-enablement/2026-09-15]] |
| 8 | plugins/microsoft-dynamics | 2295 | [[raw/adyen/docs/plugins/microsoft-dynamics/2026-09-15]] |
| 9 | partners/oauth/integration | 1966 | [[raw/adyen/docs/partners/oauth/integration/2026-09-15]] |
| 10 | partners/integration-checklist | 1794 | [[raw/adyen/docs/partners/integration-checklist/2026-09-15]] |
| 11 | plugins/salesforce-order-management-system/set-up-oobo | 1784 | [[raw/adyen/docs/plugins/salesforce-order-management-system/set-up-oobo/2026-09-15]] |
| 12 | plugins/mirakl/set-up-the-connector | 1405 | [[raw/adyen/docs/plugins/mirakl/set-up-the-connector/2026-09-15]] |
| 13 | plugins/cegid-retail-y2/tap-to-pay | 1342 | [[raw/adyen/docs/plugins/cegid-retail-y2/tap-to-pay/2026-09-15]] |
| 14 | plugins/salesforce-order-management-system/upgrade | 1320 | [[raw/adyen/docs/plugins/salesforce-order-management-system/upgrade/2026-09-15]] |
| 15 | industries/markets/japan/credit-card-security-guidelines-compliance-guide | 1286 | [[raw/adyen/docs/industries/markets/japan/credit-card-security-guidelines-compliance-guide/2026-09-15]] |
| 16 | plugins/cegid-retail-y2/troubleshooting | 1285 | [[raw/adyen/docs/plugins/cegid-retail-y2/troubleshooting/2026-09-15]] |
| 17 | industries/peak-season/refunds | 1263 | [[raw/adyen/docs/industries/peak-season/refunds/2026-09-15]] |
| 18 | industries/peak-season/in-person-payments | 1216 | [[raw/adyen/docs/industries/peak-season/in-person-payments/2026-09-15]] |
| 19 | industries/markets/japan/scta-and-psa | 1184 | [[raw/adyen/docs/industries/markets/japan/scta-and-psa/2026-09-15]] |
| 20 | plugins/salesforce-order-management-system/install-and-set-up-the-package | 1079 | [[raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/2026-09-15]] |
| 21 | plugins/mirakl/set-up-payment-flows | 1054 | [[raw/adyen/docs/plugins/mirakl/set-up-payment-flows/2026-09-15]] |
| 22 | industries/peak-season | 1002 | [[raw/adyen/docs/industries/peak-season/2026-09-15]] |
| 23 | industries/major-sports-event | 939 | [[raw/adyen/docs/industries/major-sports-event/2026-09-15]] |
| 24 | partners/application-information | 902 | [[raw/adyen/docs/partners/application-information/2026-09-15]] |
| 25 | industries/markets/india | 888 | [[raw/adyen/docs/industries/markets/india/2026-09-15]] |
| 26 | partners/oauth/scopes | 886 | [[raw/adyen/docs/partners/oauth/scopes/2026-09-15]] |
| 27 | industries/peak-season/risk-and-disputes | 884 | [[raw/adyen/docs/industries/peak-season/risk-and-disputes/2026-09-15]] |
| 28 | plugins/salesforce-order-management-system/authorization-reversal | 876 | [[raw/adyen/docs/plugins/salesforce-order-management-system/authorization-reversal/2026-09-15]] |
| 29 | plugins/cegid-retail-y2/giftcards | 854 | [[raw/adyen/docs/plugins/cegid-retail-y2/giftcards/2026-09-15]] |
| 30 | industries/peak-season/status-and-help | 828 | [[raw/adyen/docs/industries/peak-season/status-and-help/2026-09-15]] |
| 31 | reporting/your-payment-terminals | 780 | [[raw/adyen/docs/reporting/your-payment-terminals/2026-09-15]] |
| 32 | plugins/mirakl/onboard-sellers | 753 | [[raw/adyen/docs/plugins/mirakl/onboard-sellers/2026-09-15]] |
| 33 | industries/peak-season/online-payments | 747 | [[raw/adyen/docs/industries/peak-season/online-payments/2026-09-15]] |
| 34 | plugins/mirakl/test-and-go-live | 646 | [[raw/adyen/docs/plugins/mirakl/test-and-go-live/2026-09-15]] |
| 35 | industries/peak-season/afp | 558 | [[raw/adyen/docs/industries/peak-season/afp/2026-09-15]] |
| 36 | plugins/mirakl/reconciliation-and-invoices | 535 | [[raw/adyen/docs/plugins/mirakl/reconciliation-and-invoices/2026-09-15]] |
| 37 | plugins/cegid-retail-y2/pay-by-link | 522 | [[raw/adyen/docs/plugins/cegid-retail-y2/pay-by-link/2026-09-15]] |
| 38 | industries/peak-season/giving | 471 | [[raw/adyen/docs/industries/peak-season/giving/2026-09-15]] |
| 39 | plugins/mirakl/payouts | 384 | [[raw/adyen/docs/plugins/mirakl/payouts/2026-09-15]] |
| 40 | partners/oauth | 359 | [[raw/adyen/docs/partners/oauth/2026-09-15]] |
| 41 | payments | 318 | [[raw/adyen/docs/payments/2026-09-15]] |
| 42 | partners/oauth/installed-oauth-apps | 309 | [[raw/adyen/docs/partners/oauth/installed-oauth-apps/2026-09-15]] |
| 43 | industries | 270 | [[raw/adyen/docs/industries/2026-09-15]] |
| 44 | financial-products | 264 | [[raw/adyen/docs/financial-products/2026-09-15]] |
| 45 | plugins/mirakl/troubleshooting | 252 | [[raw/adyen/docs/plugins/mirakl/troubleshooting/2026-09-15]] |
| 46 | industries/markets/japan | 198 | [[raw/adyen/docs/industries/markets/japan/2026-09-15]] |
| 47 | reporting/platform-reports | 165 | [[raw/adyen/docs/reporting/platform-reports/2026-09-15]] |
| 48 | plugins/salesforce-order-management-system/order-status-lifecycle | 161 | [[raw/adyen/docs/plugins/salesforce-order-management-system/order-status-lifecycle/2026-09-15]] |
| 49 | industries/markets | 152 | [[raw/adyen/docs/industries/markets/2026-09-15]] |
| 50 | industries/feature-packs | 123 | [[raw/adyen/docs/industries/feature-packs/2026-09-15]] |

Preparation does not execute C14. No runtime campaign, workers, reviews, source or concept edits created for C14. These preparation artifacts remain uncommitted.
