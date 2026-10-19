# Adyen C21 selection and execution plan

Status: **COMPLETE — execution approved and validated**.
Prepared 2026-10-18 after C20 commit `3d755a993b19decfb54acf084b506fcf64b276a5` was pushed and exact remote main verified.

50 previously unreferenced English General Docs snapshots, **98,808 metadata words**. Focus: Issuing account/resource/access foundations, onboarding, verification/KYC and error references, card creation/management, payment/authorization lifecycle and transaction rules, plus 3DS/Authentication SDK introduction and installation (50). First three foundation routes precede remaining largest-first jobs. Selection uses metadata only; no source facts or architecture are pre-approved.

Baseline **1014 = 1000 website + 14 GitHub**. Audit existing Adyen Issuing, financial products, Platforms, account structure, verification, card, authorization, 3DS and authentication concepts through indexes first. Reuse the Issuing concept; add a dedicated concept only for a genuine product/topic gap. New concepts require genuine gaps and independent approval before source promotion.

Ten shared rolling child slots, gpt-6-sol medium workers and different high independent first reviewers; repo-read-only delegates, coordinator-only serial writes. Full pinned raw per job, 3–5 quotes, independent full initial review, maximum three attempts, bounded corrections. Concept-before-source promotion; aggregates once at close; 100 fixed locator-backed answers, three fixed coordinator full-read exemplars, exhaustive hashes/links/counts and touched typed validation. [Exact proposed authorization](dispatch-contract.md).

No raw collection, live provider/payout/transfer/top-up/report/admin/account operations, code/rule/schema/validator changes or disposition reclassification. Unselected pages remain deferred; no raw_reference reclassification. Issuing funding/top-ups, balances, reports, disputes, card-data/PIN, tokens/wallets, other components and OOB authentication/device implementation guides, Classic Platforms, API Explorer, GitHub, localized pages and oversized references remain deferred. The 15,876-word required-KYC-information page is not selected.

## Fixed exemplars

- `docs-issuing-integration-checklist`
- `docs-issuing-manage-account-holders`
- `docs-issuing-create-cards`

## Preparation checks

- [x] C20 complete, committed and pushed; exact remote SHA verified.
- [x] 50 unique jobs, canonical URLs, latest pins and absent source targets.
- [x] 50 unreferenced hashes, English metadata/title and size checks.
- [x] Review/routing schema and three distinct exemplars verified.
- [x] Explicit approval before execution.

## Exact selection

| # | Path | Metadata words |
| --- | --- | ---: |
| 1 | https://docs.adyen.com/issuing/integration-checklist | 3631 |
| 2 | https://docs.adyen.com/issuing/account-structure-resources | 677 |
| 3 | https://docs.adyen.com/issuing/account-structure-resources/issuing-embedded | 1092 |
| 4 | https://docs.adyen.com/issuing/manage-account-holders | 6543 |
| 5 | https://docs.adyen.com/issuing/test-verification-errors | 6157 |
| 6 | https://docs.adyen.com/issuing/verification-requirements/data-formats-per-country | 5548 |
| 7 | https://docs.adyen.com/issuing/verification-requirements/document-requirements | 5263 |
| 8 | https://docs.adyen.com/issuing/authorisation/transaction-rules/create-and-manage | 4805 |
| 9 | https://docs.adyen.com/issuing/kyc-verification-codes/sub-errors | 4718 |
| 10 | https://docs.adyen.com/issuing/manage-legal-entities | 3861 |
| 11 | https://docs.adyen.com/issuing/create-cards | 3503 |
| 12 | https://docs.adyen.com/issuing/onboard-users/components | 3066 |
| 13 | https://docs.adyen.com/issuing/kyc-verification-codes/general-verification-errors | 2929 |
| 14 | https://docs.adyen.com/issuing/onboard-users/terms-of-service | 2907 |
| 15 | https://docs.adyen.com/issuing/manage-cards | 2731 |
| 16 | https://docs.adyen.com/issuing/3d-secure/password-otp | 2671 |
| 17 | https://docs.adyen.com/issuing/authorisation/transaction-rules | 2623 |
| 18 | https://docs.adyen.com/issuing/payment-stages/check-details-payment | 2439 |
| 19 | https://docs.adyen.com/issuing/kyc-verification-codes/remediating-actions | 2353 |
| 20 | https://docs.adyen.com/issuing/verification-requirements | 2255 |
| 21 | https://docs.adyen.com/issuing/onboard-users | 2029 |
| 22 | https://docs.adyen.com/issuing/onboard-users/customize-hosted-onboarding | 2015 |
| 23 | https://docs.adyen.com/issuing/validation-checks | 1886 |
| 24 | https://docs.adyen.com/issuing/kyc-insights | 1830 |
| 25 | https://docs.adyen.com/issuing/authorisation/transaction-rules/view-available-limits | 1619 |
| 26 | https://docs.adyen.com/issuing/verification-overview/capabilities | 1602 |
| 27 | https://docs.adyen.com/issuing/manage-access/api-credentials-web-service | 1540 |
| 28 | https://docs.adyen.com/issuing/manage-balance-accounts | 1494 |
| 29 | https://docs.adyen.com/issuing/payment-stages | 1440 |
| 30 | https://docs.adyen.com/issuing/authorisation/transaction-rules/examples | 1264 |
| 31 | https://docs.adyen.com/issuing/authorisation/relayed-authorisation | 1236 |
| 32 | https://docs.adyen.com/issuing/verification-requirements/reference-additional-products | 1181 |
| 33 | https://docs.adyen.com/issuing/verification-overview | 1177 |
| 34 | https://docs.adyen.com/issuing/account-holder-status | 962 |
| 35 | https://docs.adyen.com/issuing/authorisation/scheme-advice | 923 |
| 36 | https://docs.adyen.com/issuing/account-structure-resources/issuing-enterprise | 857 |
| 37 | https://docs.adyen.com/issuing/kyc-verification-codes | 775 |
| 38 | https://docs.adyen.com/issuing/payment-stages/authorisation-holds | 735 |
| 39 | https://docs.adyen.com/issuing/authorisation | 729 |
| 40 | https://docs.adyen.com/issuing/3d-secure | 685 |
| 41 | https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/install-sdk-mobile | 528 |
| 42 | https://docs.adyen.com/issuing/3d-secure/troubleshooting | 513 |
| 43 | https://docs.adyen.com/issuing/manage-access/webservice-roles | 459 |
| 44 | https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk | 322 |
| 45 | https://docs.adyen.com/issuing/manage-liable-accounts | 267 |
| 46 | https://docs.adyen.com/issuing/manage-access | 246 |
| 47 | https://docs.adyen.com/issuing/account-structure-resources/legal-entity-management | 241 |
| 48 | https://docs.adyen.com/issuing/onboard-users/onboarding-steps | 170 |
| 49 | https://docs.adyen.com/issuing/verification-requirements/reference-additional-products/industry-codes | 168 |
| 50 | https://docs.adyen.com/issuing/verification-requirements/reference-additional-products/brand-specific-industry-codes | 143 |

User approval activated this exact campaign. All 50 sources are promoted, reviews and closure checks retained. No commit or push.
