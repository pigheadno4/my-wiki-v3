# Adyen C65 API Explorer collection-first preparation

Status: **AWAITING EXACT COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared 2026-11-03 after C64 publication `ab427db2bf81e4f7715ed949fd80f6f37123953c`.

C64 ingested all 50 newly collected pages: Checkout 2 and Balance Platform 48. Current totals: **2,959 sources = 2,547 General Docs + 396 API Explorer + 16 GitHub**. All locally collected complete-body API Explorer pages are ingested. The only 27 unreferenced local raw pages are excluded title-only stubs, retried in C63 and still title-only. No repeated stub retries proposed here.

## Pinned catalog reconciliation

The official API Explorer catalog captured 2026-11-02 contains **670 distinct normalized documentation URLs** (623 operation references and 47 overview references). Exact-URL reconciliation on 2026-11-03 finds 423 local raw URLs: 396 with ingested raw and 27 excluded title-only stubs. **247 catalog URLs have no local raw**. All 423 local URLs occur in the pinned catalog. [Complete reconciliation](catalog-reconciliation.json) retains its SHA256 and all missing URLs.

This is reconciliation against an immutable captured catalog, not a refreshed upstream inventory or a claim about present page availability. No network requests or semantic reads of the proposed pages were made. Titles and paths identify navigation scope only.

## Exact next collection proposal

Propose **50 exact official Markdown URLs**: the remaining 29 Balance Platform references and the first 21 uncollected Legal Entity references in captured catalog order. Metadata scope includes resource rules and tokens, grants, mandates, devices and transfer limits, followed by legal entities, transfer instruments, business lines, documents, terms and one PCI-template reference. No behavior is inferred from these names. Every selected URL has a pinned catalog-line locator; the documented duplicated API Explorer prefix is collapsed, retaining official case and parenthesized parameters. Every raw directory and provisional source target is absent and all URLs/targets are unique. [Exact 50-target proposal](collection-proposal.json).

Approval authorizes documentation collection for these 50 URLs only. Stage each response, retain status/headers/body/hash and final URL, omit server-set cookies from published metadata, and classify substantive/failed/title-only results separately. Preserve substantive body bytes verbatim in new dated immutable raw snapshots. No whole-corpus refresh, code/rule/validator changes, General Docs, GitHub, stub retries, provider/account/security/device/payment operations, automatic ingestion or further publication. Endpoint action names describe documentation targets, not authorized API calls.

After all 50 selected URLs reach recorded outcomes, reconcile results and prepare an exact ingestion manifest only from recovered complete-body evidence: raw SHA256 pins, actual fixed query prompts, three distinct audit samples and explicit provider review authorization. Obtain separate ingestion approval per rules/psp-collection.md. Do not pad failed or incomplete results or waive body/schema presence. If all 50 collect successfully, 197 captured-catalog URLs would still lack raw; source counts rise only after approved ingestion.

C65 is **PREPARED ONLY / awaiting approval**. No runtime, dispatch, candidates, raw collection or canonical sources created. Publishing this proposal does not authorize execution.

| Item | Family | Catalog label | Exact Markdown URL |
| --- | --- | --- | --- |
| c65-01 | balanceplatform | GET /paymentInstrumentGroups/{id}/transactionRules | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/transactionRules.md` |
| c65-02 | balanceplatform | GET /transactionRules/{transactionRuleId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/transactionRules/(transactionRuleId).md` |
| c65-03 | balanceplatform | PATCH /transactionRules/{transactionRuleId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/transactionRules/(transactionRuleId).md` |
| c65-04 | balanceplatform | DELETE /transactionRules/{transactionRuleId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/transactionRules/(transactionRuleId).md` |
| c65-05 | balanceplatform | GET /networkTokens/{networkTokenId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/networkTokens/(networkTokenId).md` |
| c65-06 | balanceplatform | PATCH /networkTokens/{networkTokenId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/networkTokens/(networkTokenId).md` |
| c65-07 | balanceplatform | GET /grantAccounts/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/grantAccounts/(id).md` |
| c65-08 | balanceplatform | GET /grantOffers/{grantOfferId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/grantOffers/(grantOfferId).md` |
| c65-09 | balanceplatform | GET /cardorders/{id}/items | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/cardorders/(id)/items.md` |
| c65-10 | balanceplatform | GET /mandates/{mandateId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/mandates/(mandateId).md` |
| c65-11 | balanceplatform | PATCH /mandates/{mandateId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/mandates/(mandateId).md` |
| c65-12 | balanceplatform | POST /mandates/{mandateId}/cancel | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/mandates/(mandateId)/cancel.md` |
| c65-13 | balanceplatform | DELETE /scaDevices/{deviceId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/scaDevices/(deviceId).md` |
| c65-14 | balanceplatform | PATCH /scaDevices/{deviceId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/scaDevices/(deviceId).md` |
| c65-15 | balanceplatform | POST /scaDevices/{deviceId}/scaAssociations | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/scaDevices/(deviceId)/scaAssociations.md` |
| c65-16 | balanceplatform | POST /balanceAccounts/{id}/transferLimits | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits.md` |
| c65-17 | balanceplatform | POST /balanceAccounts/{id}/transferLimits/approve | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/approve.md` |
| c65-18 | balanceplatform | GET /balanceAccounts/{id}/transferLimits/current | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/current.md` |
| c65-19 | balanceplatform | GET /balanceAccounts/{id}/transferLimits | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits.md` |
| c65-20 | balanceplatform | GET /balanceAccounts/{id}/transferLimits/{transferLimitId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/(transferLimitId).md` |
| c65-21 | balanceplatform | DELETE /balanceAccounts/{id}/transferLimits/{transferLimitId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(id)/transferLimits/(transferLimitId).md` |
| c65-22 | balanceplatform | POST /balancePlatforms/{id}/transferLimits | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balancePlatforms/(id)/transferLimits.md` |
| c65-23 | balanceplatform | GET /balancePlatforms/{id}/transferLimits | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits.md` |
| c65-24 | balanceplatform | GET /balancePlatforms/{id}/transferLimits/{transferLimitId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/(transferLimitId).md` |
| c65-25 | balanceplatform | DELETE /balancePlatforms/{id}/transferLimits/{transferLimitId} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balancePlatforms/(id)/transferLimits/(transferLimitId).md` |
| c65-26 | balanceplatform | PATCH /registeredDevices/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/registeredDevices/(id).md` |
| c65-27 | balanceplatform | POST /registeredDevices/{deviceId}/associations | `https://docs.adyen.com/api-explorer/balanceplatform/latest/post/registeredDevices/(deviceId)/associations.md` |
| c65-28 | balanceplatform | PATCH /registeredDevices/{deviceId}/associations | `https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/registeredDevices/(deviceId)/associations.md` |
| c65-29 | balanceplatform | DELETE /registeredDevices/{id} | `https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/registeredDevices/(id).md` |
| c65-30 | legalentity | GET /legalEntities/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id).md` |
| c65-31 | legalentity | PATCH /legalEntities/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/patch/legalEntities/(id).md` |
| c65-32 | legalentity | GET /legalEntities/{id}/businessLines | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/businessLines.md` |
| c65-33 | legalentity | POST /legalEntities/{id}/checkVerificationErrors | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/checkVerificationErrors.md` |
| c65-34 | legalentity | POST /legalEntities/{id}/confirmDataReview | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/confirmDataReview.md` |
| c65-35 | legalentity | POST /legalEntities/{id}/requestPeriodicReview | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/requestPeriodicReview.md` |
| c65-36 | legalentity | GET /transferInstruments/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/transferInstruments/(id).md` |
| c65-37 | legalentity | PATCH /transferInstruments/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/patch/transferInstruments/(id).md` |
| c65-38 | legalentity | DELETE /transferInstruments/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/delete/transferInstruments/(id).md` |
| c65-39 | legalentity | GET /businessLines/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/businessLines/(id).md` |
| c65-40 | legalentity | DELETE /businessLines/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/delete/businessLines/(id).md` |
| c65-41 | legalentity | PATCH /businessLines/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/patch/businessLines/(id).md` |
| c65-42 | legalentity | GET /documents/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/documents/(id).md` |
| c65-43 | legalentity | PATCH /documents/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/patch/documents/(id).md` |
| c65-44 | legalentity | DELETE /documents/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/delete/documents/(id).md` |
| c65-45 | legalentity | POST /legalEntities/{id}/termsOfService | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/termsOfService.md` |
| c65-46 | legalentity | PATCH /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | `https://docs.adyen.com/api-explorer/legalentity/latest/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid).md` |
| c65-47 | legalentity | GET /legalEntities/{id}/termsOfServiceAcceptanceInfos | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceAcceptanceInfos.md` |
| c65-48 | legalentity | GET /legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/acceptedTermsOfServiceDocument/(termsofserviceacceptancereference).md` |
| c65-49 | legalentity | GET /legalEntities/{id}/termsOfServiceStatus | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceStatus.md` |
| c65-50 | legalentity | POST /legalEntities/{id}/pciQuestionnaires/generatePciTemplates | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/generatePciTemplates.md` |
