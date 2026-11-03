# Adyen C64 API Explorer collection-first preparation

Status: **AWAITING EXACT COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared2026-11-02 after C63 ingestion publication `10b70b9c47d5affe9d086aaa0008ae1d678619ad`.

C63 ingested all10 recovered Checkout pages. Current totals: **2,909 sources = 2,547 General Docs + 346 API Explorer + 16 GitHub**. Every locally collected complete-body API Explorer page is now ingested; the only27 unreferenced local raw pages are the explicitly excluded title-only stubs, retried in C63 and still title-only. No repeated stub retries proposed here.

## Catalog reconciliation reveals additional collection work

The official API Explorer catalog captured2026-11-02 contains **670 distinct normalized documentation URLs**. Exact-URL reconciliation with373 local raw pages yields346 catalog URLs with ingested raw,27 catalog URLs with excluded title-only raw, and **297 catalog URLs without local raw**. All373 local raw URLs are present in the captured catalog. The catalog includes623 operation references and47 overview references. See [complete reconciliation](catalog-reconciliation.json), including the captured catalog SHA256 and all missing URLs.

The earlier “no complete-body raw remains” result described the local ingestion queue, not upstream documentation completeness. This broader catalog comparison identifies collection gaps; it does not establish why each gap exists or current page availability. No network requests or semantic source reads were made for this preparation.

## Exact next collection proposal

Propose **50 exact official Markdown URLs**: both uncollected Checkout references and the first48 uncollected Balance Platform references in captured catalog order. This gives a bounded resource-focused round rather than collecting all297. All50 URLs are directly located in the catalog with its documented duplicate-prefix fixup logged; parenthesized path parameters and official URL case remain intact. Every raw directory and provisional source target is absent; URLs/targets are unique. Names identify navigation scope only, with no behavior inferred from metadata. [Exact50-target proposal](collection-proposal.json).

Approval of this packet authorizes collection of these50 documentation URLs only. Stage responses, retain status/headers/body/hash and final URL, omit server-set cookies from publication metadata, and classify complete-body/failed/title-only results separately. Store substantive responses verbatim with collection metadata in new dated immutable raw. No whole-corpus refresh, code/rule/validator changes, General Docs or GitHub scope, existing stub retries, provider/account/security/device/payment operations, automatic ingestion, commit or push. No body-presence waiver.

After every selected URL has a recorded outcome, reconcile results and prepare an exact ingestion manifest only from recovered complete-body evidence, with raw SHA256, actual fixed query prompts, three distinct audit samples and the explicit provider review authorization. Seek separate ingestion approval under rules/psp-collection.md. Do not pad failed or incomplete results. Successful collection of all50 would provide up to50 new source units; counts are not raised by collection alone.

This C64 proposal is prepared only. Publishing this proposal does not authorize collection or ingestion. No runtime, dispatch, candidates, raw collection or canonical source pages created.

| Item | Family | Catalog label | Exact Markdown URL |
| --- | --- | --- | --- |
| c64-01 | Checkout | POST /verifyShopperTaxIdentification | `https://docs.adyen.com/api-explorer/Checkout/latest/post/verifyShopperTaxIdentification.md` |
| c64-02 | Checkout | POST /calculateTax | `https://docs.adyen.com/api-explorer/Checkout/latest/post/calculateTax.md` |
| c64-03 | balanceplatform | GET /balancePlatforms/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id).md` |
| c64-04 | balanceplatform | GET /balancePlatforms/{id}/accountHolders | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/accountHolders.md` |
| c64-05 | balanceplatform | GET /balancePlatforms/{id}/transactionRules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transactionRules.md` |
| c64-06 | balanceplatform | PATCH /accountHolders/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/accountHolders/(id).md` |
| c64-07 | balanceplatform | GET /accountHolders/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id).md` |
| c64-08 | balanceplatform | GET /accountHolders/{id}/balanceAccounts | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/balanceAccounts.md` |
| c64-09 | balanceplatform | GET /accountHolders/{id}/taxForms | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxForms.md` |
| c64-10 | balanceplatform | GET /accountHolders/{id}/taxFormSummary | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary.md` |
| c64-11 | balanceplatform | GET /accountHolders/{id}/transactionRules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/transactionRules.md` |
| c64-12 | balanceplatform | PATCH /balanceAccounts/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(id).md` |
| c64-13 | balanceplatform | GET /balanceAccounts/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id).md` |
| c64-14 | balanceplatform | GET /balanceAccounts/{id}/paymentInstruments | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/paymentInstruments.md` |
| c64-15 | balanceplatform | GET /balanceAccounts/{id}/transactionRules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transactionRules.md` |
| c64-16 | balanceplatform | POST /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings.md` |
| c64-17 | balanceplatform | PATCH /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId).md` |
| c64-18 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId).md` |
| c64-19 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings.md` |
| c64-20 | balanceplatform | DELETE /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId).md` |
| c64-21 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/payoutSchedules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules.md` |
| c64-22 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/payoutSchedules/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/(id).md` |
| c64-23 | balanceplatform | POST /balanceAccounts/{balanceAccountId}/payoutSchedules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/payoutSchedules.md` |
| c64-24 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/payoutSchedules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules.md` |
| c64-25 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id).md` |
| c64-26 | balanceplatform | PATCH /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/payoutSchedules/(id).md` |
| c64-27 | balanceplatform | DELETE /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/payoutSchedules/(id).md` |
| c64-28 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/executions.md` |
| c64-29 | balanceplatform | POST /balanceAccounts/{balanceAccountId}/sweeps | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/sweeps.md` |
| c64-30 | balanceplatform | PATCH /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/sweeps/(sweepId).md` |
| c64-31 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/sweeps | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps.md` |
| c64-32 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId).md` |
| c64-33 | balanceplatform | DELETE /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/sweeps/(sweepId).md` |
| c64-34 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}/executions | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/executions.md` |
| c64-35 | balanceplatform | POST /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers.md` |
| c64-36 | balanceplatform | GET /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers.md` |
| c64-37 | balanceplatform | PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers.md` |
| c64-38 | balanceplatform | DELETE /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers.md` |
| c64-39 | balanceplatform | POST /balanceAccounts/{balanceAccountId}/recurringTopUps | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/recurringTopUps.md` |
| c64-40 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/recurringTopUps | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/recurringTopUps.md` |
| c64-41 | balanceplatform | PATCH /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId).md` |
| c64-42 | balanceplatform | DELETE /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId).md` |
| c64-43 | balanceplatform | PATCH /paymentInstruments/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/(id).md` |
| c64-44 | balanceplatform | GET /paymentInstruments/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id).md` |
| c64-45 | balanceplatform | GET /paymentInstruments/{id}/reveal | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/reveal.md` |
| c64-46 | balanceplatform | GET /paymentInstruments/{id}/networkTokens | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokens.md` |
| c64-47 | balanceplatform | GET /paymentInstruments/{id}/transactionRules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/transactionRules.md` |
| c64-48 | balanceplatform | GET /paymentInstruments/{id}/networkTokenActivationData | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokenActivationData.md` |
| c64-49 | balanceplatform | POST /paymentInstruments/{id}/networkTokenActivationData | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments/(id)/networkTokenActivationData.md` |
| c64-50 | balanceplatform | GET /paymentInstrumentGroups/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id).md` |

User approved this exact50-target collection on2026-11-02. Collectionactive; ingestion and publication not authorized. Earlier statements describe preparation-time state.
