# Adyen C64 bounded API Explorer collection

Collection approved2026-11-02; collection completed. No ingestion or publication.

- status: COLLECTION_COMPLETE_AWAITING_INGESTION_APPROVAL
- selected: 50
- outcomes: {'new_complete_body_raw': 50}
- complete_body_pages: 50
- http_200: 50
- new_raw_sha256_verified: 50
- response_bytes_preserved: 50
- existing_adyen_raw_and_wiki_unchanged: True
- concurrent_unrelated_wiki_changes: []
- original_title_only_stubs_still_excluded: 27
- runtime_initialized: False
- ingestion_executed: False
- publication_executed: False

Body presence and identity screens are mechanical, not full semantic source reads. Every selected URL has a terminal outcome; per-attempt status/headers/body/hash retained. Server-set cookies omitted. Every accepted response body is byte-exact after collection metadata; prior accepted raw/wiki untouched.

| Item | Catalog operation | Outcome | New raw |
| --- | --- | --- | --- |
| c64-01 | POST /verifyShopperTaxIdentification | new_complete_body_raw | `raw/adyen/api-explorer/Checkout/latest/post/verifyShopperTaxIdentification/2026-11-02.md` |
| c64-02 | POST /calculateTax | new_complete_body_raw | `raw/adyen/api-explorer/Checkout/latest/post/calculateTax/2026-11-02.md` |
| c64-03 | GET /balancePlatforms/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/2026-11-02.md` |
| c64-04 | GET /balancePlatforms/{id}/accountHolders | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/accountHolders/2026-11-02.md` |
| c64-05 | GET /balancePlatforms/{id}/transactionRules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transactionRules/2026-11-02.md` |
| c64-06 | PATCH /accountHolders/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/accountHolders/(id)/2026-11-02.md` |
| c64-07 | GET /accountHolders/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/2026-11-02.md` |
| c64-08 | GET /accountHolders/{id}/balanceAccounts | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/balanceAccounts/2026-11-02.md` |
| c64-09 | GET /accountHolders/{id}/taxForms | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxForms/2026-11-02.md` |
| c64-10 | GET /accountHolders/{id}/taxFormSummary | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary/2026-11-02.md` |
| c64-11 | GET /accountHolders/{id}/transactionRules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/transactionRules/2026-11-02.md` |
| c64-12 | PATCH /balanceAccounts/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(id)/2026-11-02.md` |
| c64-13 | GET /balanceAccounts/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/2026-11-02.md` |
| c64-14 | GET /balanceAccounts/{id}/paymentInstruments | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/paymentInstruments/2026-11-02.md` |
| c64-15 | GET /balanceAccounts/{id}/transactionRules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transactionRules/2026-11-02.md` |
| c64-16 | POST /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/2026-11-02.md` |
| c64-17 | PATCH /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02.md` |
| c64-18 | GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02.md` |
| c64-19 | GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/2026-11-02.md` |
| c64-20 | DELETE /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02.md` |
| c64-21 | GET /balancePlatforms/{balancePlatformId}/payoutSchedules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/2026-11-02.md` |
| c64-22 | GET /balancePlatforms/{balancePlatformId}/payoutSchedules/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/(id)/2026-11-02.md` |
| c64-23 | POST /balanceAccounts/{balanceAccountId}/payoutSchedules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/payoutSchedules/2026-11-02.md` |
| c64-24 | GET /balanceAccounts/{balanceAccountId}/payoutSchedules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/2026-11-02.md` |
| c64-25 | GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02.md` |
| c64-26 | PATCH /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02.md` |
| c64-27 | DELETE /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02.md` |
| c64-28 | GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/executions/2026-11-02.md` |
| c64-29 | POST /balanceAccounts/{balanceAccountId}/sweeps | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/sweeps/2026-11-02.md` |
| c64-30 | PATCH /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02.md` |
| c64-31 | GET /balanceAccounts/{balanceAccountId}/sweeps | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/2026-11-02.md` |
| c64-32 | GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02.md` |
| c64-33 | DELETE /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02.md` |
| c64-34 | GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}/executions | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/executions/2026-11-02.md` |
| c64-35 | POST /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md` |
| c64-36 | GET /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md` |
| c64-37 | PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md` |
| c64-38 | DELETE /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md` |
| c64-39 | POST /balanceAccounts/{balanceAccountId}/recurringTopUps | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/recurringTopUps/2026-11-02.md` |
| c64-40 | GET /balanceAccounts/{balanceAccountId}/recurringTopUps | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/recurringTopUps/2026-11-02.md` |
| c64-41 | PATCH /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)/2026-11-02.md` |
| c64-42 | DELETE /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)/2026-11-02.md` |
| c64-43 | PATCH /paymentInstruments/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/paymentInstruments/(id)/2026-11-02.md` |
| c64-44 | GET /paymentInstruments/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/2026-11-02.md` |
| c64-45 | GET /paymentInstruments/{id}/reveal | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/reveal/2026-11-02.md` |
| c64-46 | GET /paymentInstruments/{id}/networkTokens | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokens/2026-11-02.md` |
| c64-47 | GET /paymentInstruments/{id}/transactionRules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/transactionRules/2026-11-02.md` |
| c64-48 | GET /paymentInstruments/{id}/networkTokenActivationData | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokenActivationData/2026-11-02.md` |
| c64-49 | POST /paymentInstruments/{id}/networkTokenActivationData | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/(id)/networkTokenActivationData/2026-11-02.md` |
| c64-50 | GET /paymentInstrumentGroups/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/2026-11-02.md` |

Full evidence: page-results.json, summary.json and responses/. Separate exact ingestion approval required.
