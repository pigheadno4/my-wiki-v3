# Adyen C65 collected API Explorer ingestion selection

Status: **PREPARED ONLY — awaiting exact ingestion approval**. Prepared 2026-11-03.

Approved collection completed for all50 exact URLs: **50 HTTP200 substantive Markdown pages**, no failed, title-only or mismatched documents. Families: **Balance Platform29 + Legal Entity21**. Every response body is preserved byte-for-byte after collection metadata in a new dated2026-11-03 raw file. All prior Adyen raw/wiki hashes are unchanged; concurrent unrelated PayPal work is recorded separately. These title/body/byte checks are collection screening, not full semantic reads. The 515-byte periodic-review reference contains a server, required path ID and 204 response; it is substantive, not a title-only stub. [Collection manifest](../../../collections/adyen/c65-collection-2026-11-03/manifest.md), [summary](../../../collections/adyen/c65-collection-2026-11-03/summary.json). Original proposal retained in [collection-selection-review.md](collection-selection-review.md).

Exact proposed ingestion: **50 source units**, **100 fixed answers**, **three predetermined distinct full-read audits**. All hashes, URL/target uniqueness, absent canonical targets and unreferenced pins verified. Size: **93,304 whitespace words, 9,214 raw lines, 592,191 bytes**. Source generation begins only after separate exact ingestion approval.

Current baseline **2,959 = 2,547 General Docs +396 API Explorer +16 GitHub**. Successful ingestion of all50 gives **3,009 = 2,547 General Docs +446 API Explorer +16 GitHub**. API Explorer now has473 local raw pages:396 ingested substantive pages,50 newly collected and27 excluded title-only stubs. Unreferenced local raw would decline77→27 after successful ingestion. The captured670-URL catalog has **197 URLs still without local raw**; the27 stub exclusions remain separate. This is captured-catalog coverage, not a current upstream completeness claim.

[Proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers/different high initial reviewers, full numbered reads of every schema/example,3–5locatedquotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [100 original fixed prompts](proposed-queries.md) require actual independently checked answers. Full raw reads apply equally to the largest Legal Entity schema and minimal 204 references.

Fixed coordinator audit jobs: `api-explorer-balanceplatform-latest-get-transactionrules-transactionruleid`, `api-explorer-legalentity-latest-patch-legalentities-id`, `api-explorer-legalentity-latest-get-documents-id`. Material partial/fail expands to all50. No ingestion runtime, dispatch, canonical wiki source generation, commit or push. Await separate exact C65 ingestion approval.

| # | Family | Operation | Words | Raw lines |
| --- | --- | --- | ---: | ---: |
| 1 | balanceplatform | GET /paymentInstrumentGroups/{id}/transactionRules | 3,288 | 317 |
| 2 | balanceplatform | GET /transactionRules/{transactionRuleId} | 3,198 | 279 |
| 3 | balanceplatform | PATCH /transactionRules/{transactionRuleId} | 6,974 | 469 |
| 4 | balanceplatform | DELETE /transactionRules/{transactionRuleId} | 4,122 | 332 |
| 5 | balanceplatform | GET /networkTokens/{networkTokenId} | 1,395 | 177 |
| 6 | balanceplatform | PATCH /networkTokens/{networkTokenId} | 1,097 | 164 |
| 7 | balanceplatform | GET /grantAccounts/{id} | 1,476 | 206 |
| 8 | balanceplatform | GET /grantOffers/{grantOfferId} | 1,637 | 214 |
| 9 | balanceplatform | GET /cardorders/{id}/items | 1,482 | 209 |
| 10 | balanceplatform | GET /mandates/{mandateId} | 1,312 | 133 |
| 11 | balanceplatform | PATCH /mandates/{mandateId} | 1,090 | 123 |
| 12 | balanceplatform | POST /mandates/{mandateId}/cancel | 1,058 | 117 |
| 13 | balanceplatform | DELETE /scaDevices/{deviceId} | 1,262 | 136 |
| 14 | balanceplatform | PATCH /scaDevices/{deviceId} | 1,458 | 173 |
| 15 | balanceplatform | POST /scaDevices/{deviceId}/scaAssociations | 1,569 | 184 |
| 16 | balanceplatform | POST /balanceAccounts/{id}/transferLimits | 1,762 | 161 |
| 17 | balanceplatform | POST /balanceAccounts/{id}/transferLimits/approve | 761 | 102 |
| 18 | balanceplatform | GET /balanceAccounts/{id}/transferLimits/current | 1,188 | 114 |
| 19 | balanceplatform | GET /balanceAccounts/{id}/transferLimits | 1,280 | 132 |
| 20 | balanceplatform | GET /balanceAccounts/{id}/transferLimits/{transferLimitId} | 1,054 | 103 |
| 21 | balanceplatform | DELETE /balanceAccounts/{id}/transferLimits/{transferLimitId} | 498 | 61 |
| 22 | balanceplatform | POST /balancePlatforms/{id}/transferLimits | 1,526 | 136 |
| 23 | balanceplatform | GET /balancePlatforms/{id}/transferLimits | 1,280 | 132 |
| 24 | balanceplatform | GET /balancePlatforms/{id}/transferLimits/{transferLimitId} | 1,054 | 103 |
| 25 | balanceplatform | DELETE /balancePlatforms/{id}/transferLimits/{transferLimitId} | 498 | 61 |
| 26 | balanceplatform | PATCH /registeredDevices/{id} | 1,475 | 205 |
| 27 | balanceplatform | POST /registeredDevices/{deviceId}/associations | 1,427 | 203 |
| 28 | balanceplatform | PATCH /registeredDevices/{deviceId}/associations | 1,530 | 209 |
| 29 | balanceplatform | DELETE /registeredDevices/{id} | 1,344 | 197 |
| 30 | legalentity | GET /legalEntities/{id} | 8,626 | 454 |
| 31 | legalentity | PATCH /legalEntities/{id} | 15,468 | 893 |
| 32 | legalentity | GET /legalEntities/{id}/businessLines | 1,484 | 173 |
| 33 | legalentity | POST /legalEntities/{id}/checkVerificationErrors | 1,152 | 296 |
| 34 | legalentity | POST /legalEntities/{id}/confirmDataReview | 633 | 111 |
| 35 | legalentity | POST /legalEntities/{id}/requestPeriodicReview | 88 | 22 |
| 36 | legalentity | GET /transferInstruments/{id} | 1,322 | 157 |
| 37 | legalentity | PATCH /transferInstruments/{id} | 1,527 | 190 |
| 38 | legalentity | DELETE /transferInstruments/{id} | 566 | 95 |
| 39 | legalentity | GET /businessLines/{id} | 1,723 | 168 |
| 40 | legalentity | DELETE /businessLines/{id} | 599 | 97 |
| 41 | legalentity | PATCH /businessLines/{id} | 2,532 | 212 |
| 42 | legalentity | GET /documents/{id} | 1,257 | 153 |
| 43 | legalentity | PATCH /documents/{id} | 1,901 | 191 |
| 44 | legalentity | DELETE /documents/{id} | 563 | 95 |
| 45 | legalentity | POST /legalEntities/{id}/termsOfService | 907 | 138 |
| 46 | legalentity | PATCH /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | 920 | 136 |
| 47 | legalentity | GET /legalEntities/{id}/termsOfServiceAcceptanceInfos | 797 | 125 |
| 48 | legalentity | GET /legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference} | 722 | 110 |
| 49 | legalentity | GET /legalEntities/{id}/termsOfServiceStatus | 651 | 113 |
| 50 | legalentity | POST /legalEntities/{id}/pciQuestionnaires/generatePciTemplates | 771 | 133 |
