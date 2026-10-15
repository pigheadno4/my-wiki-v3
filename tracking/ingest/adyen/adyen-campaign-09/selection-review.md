# Adyen C09 selection and execution plan

Status: **COMPLETE — execution approved and validated**.
Prepared 2026-10-14 after C08 commit `8b9f033b4a0612cc6ba13921f79b44de6915f3db` was pushed; exact remote main verification is recorded in preflight-validation.json.

50 previously unreferenced English General Docs snapshots: all **14 remaining unified-commerce guides**, **35 classic-integration guides excluding 3D Secure 1 branches**, and **PCI-DSS compliance**. Four orientation pages first; remaining jobs largest-first. Total **83,602 metadata words**, including code/navigation. Metadata selection is not semantic approval or current availability.

Baseline **414 = 400 website + 14 GitHub summaries**. Audit existing unified-commerce, Terminal API, tokenization, refunds, 3D Secure and API-access concepts before source creation. No new concepts preselected. Explicitly distinguish classic versus modern Checkout, authentication versus authorization, merchant order/fulfillment versus financial transitions, and queued modifications versus final outcomes.

3D Secure 1 branches, deprecated terminal manuals, oversized pages, remaining online/risk deferrals, platforms/issuing/payment-method guides outside this exact selection, API Explorer and GitHub are excluded. No collection/refresh or raw_reference reclassification. Preserve original C08 evidence and concept scope.

Existing ten shared rolling child slots with gpt-6-sol medium workers and different high independent first reviewers; repository-read-only delegates and coordinator-only writes, no worktrees. One pinned raw per source, full reads, 3–5 verified quotes, full independent initial review, at most three attempts and bounded corrections. [Exact provider authorization](dispatch-contract.md). Aggregate catalog/count/log once at close; 100 fixed locator-backed answers, three full-read exemplars, exhaustive structural and touched typed validation. No framework/code/rule/schema/validator changes. Use unique full-job-ID handoff filenames and exact literal concept headings; requested replacements must replace rather than append competing definitions.

## Fixed exemplars

- `docs-unified-commerce-pay-by-link`.
- `docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-authentication-only-integration`.
- `docs-unified-commerce-retail-use-cases-click-and-collect-c-and-c-add-return`.

## Preparation checks

- [x] C08 complete, committed and pushed; remote SHA verified.
- [x] 50 unique jobs/URLs/latest pins/absent targets and factual ownership.
- [x] 50 hashes, English metadata and size checked.
- [x] Three distinct fixed exemplars in exact manifest.
- [x] Explicit approval before execution.

## Exact selection

| # | Path | Metadata words | Raw |
| --- | --- | ---: | --- |
| 1 | unified-commerce/pay-by-link | 685 | [[raw/adyen/docs/unified-commerce/pay-by-link/2026-09-15]] |
| 2 | online-payments/classic-integrations | 137 | [[raw/adyen/docs/online-payments/classic-integrations/2026-09-15]] |
| 3 | online-payments/classic-integrations/classic-api-integration | 610 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/2026-09-15]] |
| 4 | online-payments/classic-integrations/modify-payments | 238 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/2026-09-15]] |
| 5 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration | 6547 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration/2026-09-15]] |
| 6 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration | 6115 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/2026-09-15]] |
| 7 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2 | 5826 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2/2026-09-15]] |
| 8 | unified-commerce/retail-use-cases/endless-aisle/e-a-store-pickup | 5487 | [[raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/e-a-store-pickup/2026-09-15]] |
| 9 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/android-sdk-integration | 4988 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/android-sdk-integration/2026-09-15]] |
| 10 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/ios-sdk-integration | 4814 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/ios-sdk-integration/2026-09-15]] |
| 11 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions | 4647 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15]] |
| 12 | online-payments/classic-integrations/modify-payments/adjust-authorisation | 3670 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/adjust-authorisation/2026-09-15]] |
| 13 | unified-commerce/retail-use-cases/endless-aisle/e-a-ship-home | 3055 | [[raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/e-a-ship-home/2026-09-15]] |
| 14 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata | 2670 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata/2026-09-15]] |
| 15 | unified-commerce/retail-use-cases/click-and-collect/c-and-c-add-return | 2440 | [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-add-return/2026-09-15]] |
| 16 | unified-commerce/retail-use-cases/click-and-collect/c-and-c-try-then-buy | 2436 | [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-try-then-buy/2026-09-15]] |
| 17 | unified-commerce/retail-use-cases/click-and-collect/c-and-c-assistant-pickup | 2315 | [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-assistant-pickup/2026-09-15]] |
| 18 | online-payments/classic-integrations/modify-payments/refund | 2053 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15]] |
| 19 | unified-commerce/pay-by-link/create-payment-links/customer-area | 1816 | [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/customer-area/2026-09-15]] |
| 20 | online-payments/classic-integrations/modify-payments/capture | 1803 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/capture/2026-09-15]] |
| 21 | online-payments/classic-integrations/classic-api-integration/classic-pix | 1396 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-pix/2026-09-15]] |
| 22 | online-payments/classic-integrations/classic-api-integration/tokenization/store-payment-details | 1307 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/store-payment-details/2026-09-15]] |
| 23 | online-payments/classic-integrations/classic-api-integration/tokenization/authorise-a-recurring-payment | 1249 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-a-recurring-payment/2026-09-15]] |
| 24 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication | 1245 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/2026-09-15]] |
| 25 | online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details | 1231 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15]] |
| 26 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2 | 1153 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/2026-09-15]] |
| 27 | online-payments/classic-integrations/classic-api-integration/client-side-encryption | 1042 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/2026-09-15]] |
| 28 | online-payments/classic-integrations/classic-api-integration/tokenization/capture-a-recurring-payment | 983 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/capture-a-recurring-payment/2026-09-15]] |
| 29 | unified-commerce/pay-by-link/supported-payment-methods | 976 | [[raw/adyen/docs/unified-commerce/pay-by-link/supported-payment-methods/2026-09-15]] |
| 30 | online-payments/classic-integrations/classic-api-integration/tokenization/retrieve-stored-details | 915 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/retrieve-stored-details/2026-09-15]] |
| 31 | online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library | 853 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library/2026-09-15]] |
| 32 | online-payments/classic-integrations/modify-payments/cancel | 828 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/cancel/2026-09-15]] |
| 33 | online-payments/classic-integrations/modify-payments/capture/failure-reasons | 787 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/capture/failure-reasons/2026-09-15]] |
| 34 | unified-commerce/pay-by-link/settings | 696 | [[raw/adyen/docs/unified-commerce/pay-by-link/settings/2026-09-15]] |
| 35 | unified-commerce/retail-use-cases/mixed-baskets-accounts | 687 | [[raw/adyen/docs/unified-commerce/retail-use-cases/mixed-baskets-accounts/2026-09-15]] |
| 36 | online-payments/classic-integrations/modify-payments/cancel-or-refund | 661 | [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/cancel-or-refund/2026-09-15]] |
| 37 | unified-commerce/pay-by-link/create-payment-links | 590 | [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/2026-09-15]] |
| 38 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only | 554 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15]] |
| 39 | online-payments/classic-integrations/classic-api-integration/classic-gift-cards | 536 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-gift-cards/2026-09-15]] |
| 40 | online-payments/classic-integrations/classic-api-integration/tokenization | 530 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/2026-09-15]] |
| 41 | unified-commerce/pay-by-link/ios-app | 493 | [[raw/adyen/docs/unified-commerce/pay-by-link/ios-app/2026-09-15]] |
| 42 | online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details | 428 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details/2026-09-15]] |
| 43 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses | 353 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses/2026-09-15]] |
| 44 | online-payments/classic-integrations/classic-api-integration/classic-google-pay | 352 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-google-pay/2026-09-15]] |
| 45 | online-payments/pci-dss-compliance | 335 | [[raw/adyen/docs/online-payments/pci-dss-compliance/2026-09-15]] |
| 46 | online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party | 242 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party/2026-09-15]] |
| 47 | online-payments/classic-integrations/classic-api-integration/client-side-encryption/cse-library-public-key-location-and-token | 228 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/cse-library-public-key-location-and-token/2026-09-15]] |
| 48 | unified-commerce/retail-use-cases/click-and-collect | 206 | [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/2026-09-15]] |
| 49 | unified-commerce/retail-use-cases/endless-aisle | 203 | [[raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/2026-09-15]] |
| 50 | online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows | 191 | [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/2026-09-15]] |

User approval activated this exact campaign. All 50 sources are promoted, reviews and closure checks retained. No commit or push.
