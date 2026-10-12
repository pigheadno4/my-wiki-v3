# Adyen C02 selection and execution plan

Status: COMPLETED — exact scope approved on 2026-10-12 and validated locally on 2026-10-13.

> **For agentic workers:** Use the existing coordinator-controlled workflow and rules/ingest-roles.md; no new framework.

**Goal:** 50 previously unreferenced General Docs retrieval sources.

**Architecture:** Ten shared rolling child slots; Sol medium workers and independent Sol high first reviewers; coordinator-only repository writes.

**Tech Stack:** Existing filesystem campaign artifacts and validators.

**Spec:** CLAUDE.md, rules/ingest.md, rules/psp/adyen.md, dispatch-contract.md.

## Scope and review focus

Modern online-payment follow-ups, risk/disputes, payouts, donations, account upkeep, access/compliance and testing. Five topic overview routes first, then larger pages earlier. Classic integrations and pages over 10,000 metadata words are deferred for scheduling only, not assigned raw_reference. API Explorer/GitHub excluded. Metadata selection is not semantic reading or a low-risk verdict.

Retain actor/flow/version/environment, consequential warnings, irreversible actions and snapshot conflicts. Do not silently reconcile field names or certificate/algorithm examples. Use valid concept category enums. Default concepts to reciprocal retrieval routes, avoid routine schema replication.

## Execution steps

- [x] Pin latest local snapshots; verify 50 unique jobs/URLs/targets, hashes and absence from factual raw_files.
- [x] Obtain exact manifest/provider authorization approval.
- [x] Initialize existing runtime; full per-page raw read and 3–5 exact located quotes.
- [x] Independent first full review; max3attempts; bounded unchanged-hash retries targeted.
- [x] Promote approved concepts then sources serially; aggregate catalogs/count/log once.
- [x] Two fixed queries/page (scope/notinfer; purpose/warnings/detail retrieval), 100 total; bounded correction review. Three fixed exemplar IDs in manifest.
- [x] One structural close and typed validation; record timestamps and interruption-aware timing. Commit/push separately approved.

## Pinned list

Total metadata words: 142383.

| Order | Documentation path | Words | Raw |
| --- | --- | ---: | --- |
| 1 | risk-management | 907 | [[raw/adyen/docs/risk-management/2026-09-15]] |
| 2 | online-payments/online-payouts | 885 | [[raw/adyen/docs/online-payments/online-payouts/2026-09-15]] |
| 3 | online-payments/donations | 1501 | [[raw/adyen/docs/online-payments/donations/2026-09-15]] |
| 4 | online-payments/auto-rescue | 279 | [[raw/adyen/docs/online-payments/auto-rescue/2026-09-15]] |
| 5 | online-payments/account-updater | 451 | [[raw/adyen/docs/online-payments/account-updater/2026-09-15]] |
| 6 | online-payments/online-payouts/instant-payouts | 8725 | [[raw/adyen/docs/online-payments/online-payouts/instant-payouts/2026-09-15]] |
| 7 | development-resources/error-codes | 7809 | [[raw/adyen/docs/development-resources/error-codes/2026-09-15]] |
| 8 | online-payments/3d-secure/api-reference | 5940 | [[raw/adyen/docs/online-payments/3d-secure/api-reference/2026-09-15]] |
| 9 | development-resources/test-cards-and-credentials/alternative-payment-method-credentials | 5429 | [[raw/adyen/docs/development-resources/test-cards-and-credentials/alternative-payment-method-credentials/2026-09-15]] |
| 10 | online-payments/online-payouts/payouts-to-bank-accounts-and-wallets | 4631 | [[raw/adyen/docs/online-payments/online-payouts/payouts-to-bank-accounts-and-wallets/2026-09-15]] |
| 11 | online-payments/donations/integration-options/advanced-flow | 4582 | [[raw/adyen/docs/online-payments/donations/integration-options/advanced-flow/2026-09-15]] |
| 12 | development-resources/pci-dss-compliance-guide | 4570 | [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/2026-09-15]] |
| 13 | risk-management/disputes-api/disputes-api-reference | 4535 | [[raw/adyen/docs/risk-management/disputes-api/disputes-api-reference/2026-09-15]] |
| 14 | online-payments/3d-secure/redirect-3ds2/web-component | 4355 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/web-component/2026-09-15]] |
| 15 | online-payments/tokenization/forward-payment-details | 3749 | [[raw/adyen/docs/online-payments/tokenization/forward-payment-details/2026-09-15]] |
| 16 | development-resources/paymentmethodvariant | 3600 | [[raw/adyen/docs/development-resources/paymentmethodvariant/2026-09-15]] |
| 17 | risk-management/dispute-and-fraud-monitoring | 3567 | [[raw/adyen/docs/risk-management/dispute-and-fraud-monitoring/2026-09-15]] |
| 18 | online-payments/3d-secure/redirect-3ds2/android-drop-in | 3296 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/android-drop-in/2026-09-15]] |
| 19 | online-payments/3d-secure/redirect-3ds2/ios-drop-in | 3216 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/ios-drop-in/2026-09-15]] |
| 20 | online-payments/3d-secure/redirect-3ds2/ios-component | 3066 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/ios-component/2026-09-15]] |
| 21 | online-payments/3d-secure/redirect-3ds2/android-component/earlier-versions | 3063 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/android-component/earlier-versions/2026-09-15]] |
| 22 | online-payments/auto-rescue/cards | 3001 | [[raw/adyen/docs/online-payments/auto-rescue/cards/2026-09-15]] |
| 23 | online-payments/auto-rescue/sepa | 2955 | [[raw/adyen/docs/online-payments/auto-rescue/sepa/2026-09-15]] |
| 24 | online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v3 | 2893 | [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v3/2026-09-15]] |
| 25 | risk-management/chargeback-guidelines/ach-chargebacks | 2866 | [[raw/adyen/docs/risk-management/chargeback-guidelines/ach-chargebacks/2026-09-15]] |
| 26 | development-resources/migrating-payment-data/import-payment-details-for-recurring-payments | 2651 | [[raw/adyen/docs/development-resources/migrating-payment-data/import-payment-details-for-recurring-payments/2026-09-15]] |
| 27 | risk-management/dynamic-3d-secure | 2573 | [[raw/adyen/docs/risk-management/dynamic-3d-secure/2026-09-15]] |
| 28 | risk-management/disputes-api/dispute-notifications | 2495 | [[raw/adyen/docs/risk-management/disputes-api/dispute-notifications/2026-09-15]] |
| 29 | risk-management/understanding-disputes/dispute-process-and-flow | 2482 | [[raw/adyen/docs/risk-management/understanding-disputes/dispute-process-and-flow/2026-09-15]] |
| 30 | online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v4 | 2415 | [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v4/2026-09-15]] |
| 31 | online-payments/upgrade-your-integration/upgrade-to-web-v6 | 2353 | [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/2026-09-15]] |
| 32 | development-resources/test-cards-and-credentials/test-card-numbers | 2350 | [[raw/adyen/docs/development-resources/test-cards-and-credentials/test-card-numbers/2026-09-15]] |
| 33 | risk-management/disputes-api | 2346 | [[raw/adyen/docs/risk-management/disputes-api/2026-09-15]] |
| 34 | risk-management/avs-checks | 2253 | [[raw/adyen/docs/risk-management/avs-checks/2026-09-15]] |
| 35 | online-payments/donations/integration-options/sessions-flow | 2214 | [[raw/adyen/docs/online-payments/donations/integration-options/sessions-flow/2026-09-15]] |
| 36 | development-resources/surcharge-compliance | 2212 | [[raw/adyen/docs/development-resources/surcharge-compliance/2026-09-15]] |
| 37 | risk-management/case-management | 2135 | [[raw/adyen/docs/risk-management/case-management/2026-09-15]] |
| 38 | online-payments/3d-secure/redirect-3ds2/android-component | 2117 | [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/android-component/2026-09-15]] |
| 39 | development-resources/pci-dss-compliance-guide/script-security | 2014 | [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/script-security/2026-09-15]] |
| 40 | online-payments/account-updater/real-time-account-updater | 2012 | [[raw/adyen/docs/online-payments/account-updater/real-time-account-updater/2026-09-15]] |
| 41 | risk-management/chargeback-guidelines/paypal-chargebacks | 1945 | [[raw/adyen/docs/risk-management/chargeback-guidelines/paypal-chargebacks/2026-09-15]] |
| 42 | risk-management/chargeback-guidelines/visa-chargebacks | 1935 | [[raw/adyen/docs/risk-management/chargeback-guidelines/visa-chargebacks/2026-09-15]] |
| 43 | development-resources/mtls | 1932 | [[raw/adyen/docs/development-resources/mtls/2026-09-15]] |
| 44 | online-payments/upgrade-your-integration | 1924 | [[raw/adyen/docs/online-payments/upgrade-your-integration/2026-09-15]] |
| 45 | risk-management/handle-risk-rule-notifications | 1923 | [[raw/adyen/docs/risk-management/handle-risk-rule-notifications/2026-09-15]] |
| 46 | risk-management/disputes-api/test-applicable-dispute-reasons | 1783 | [[raw/adyen/docs/risk-management/disputes-api/test-applicable-dispute-reasons/2026-09-15]] |
| 47 | development-resources/libraries | 1673 | [[raw/adyen/docs/development-resources/libraries/2026-09-15]] |
| 48 | development-resources/currency-codes | 1647 | [[raw/adyen/docs/development-resources/currency-codes/2026-09-15]] |
| 49 | development-resources/testing/3d-secure-2-authentication | 1568 | [[raw/adyen/docs/development-resources/testing/3d-secure-2-authentication/2026-09-15]] |
| 50 | development-resources/security/incidents | 1560 | [[raw/adyen/docs/development-resources/security/incidents/2026-09-15]] |
