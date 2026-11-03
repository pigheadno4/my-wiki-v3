# Adyen C65 bounded API Explorer collection

Collection approved2026-11-03; collection completed. No ingestion or publication.

- status: COLLECTION_COMPLETE_AWAITING_INGESTION_APPROVAL
- selected: 50
- outcomes: {'new_complete_body_raw': 50}
- complete_body_pages: 50
- http_200: 50
- new_raw_sha256_verified: 50
- response_bytes_preserved: 50
- existing_adyen_raw_and_wiki_unchanged: True
- concurrent_unrelated_wiki_changes: ['wiki/paypal-log.md', 'wiki/paypal-index.md', 'wiki/log.md', 'wiki/companies/paypal.md']
- original_title_only_stubs_still_excluded: 27
- runtime_initialized: False
- ingestion_executed: False
- publication_executed: False

Body presence and identity screens are mechanical, not full semantic source reads. Every selected URL has a terminal outcome; per-attempt status/headers/body/hash retained. Server-set cookies omitted. Every accepted response body is byte-exact after collection metadata; prior accepted raw/wiki untouched.

| Item | Catalog operation | Outcome | New raw |
| --- | --- | --- | --- |
| c65-01 | GET /paymentInstrumentGroups/{id}/transactionRules | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/transactionRules/2026-11-03.md` |
| c65-02 | GET /transactionRules/{transactionRuleId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/transactionRules/(transactionRuleId)/2026-11-03.md` |
| c65-03 | PATCH /transactionRules/{transactionRuleId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/transactionRules/(transactionRuleId)/2026-11-03.md` |
| c65-04 | DELETE /transactionRules/{transactionRuleId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/transactionRules/(transactionRuleId)/2026-11-03.md` |
| c65-05 | GET /networkTokens/{networkTokenId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/networkTokens/(networkTokenId)/2026-11-03.md` |
| c65-06 | PATCH /networkTokens/{networkTokenId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/networkTokens/(networkTokenId)/2026-11-03.md` |
| c65-07 | GET /grantAccounts/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/grantAccounts/(id)/2026-11-03.md` |
| c65-08 | GET /grantOffers/{grantOfferId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/grantOffers/(grantOfferId)/2026-11-03.md` |
| c65-09 | GET /cardorders/{id}/items | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/cardorders/(id)/items/2026-11-03.md` |
| c65-10 | GET /mandates/{mandateId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/mandates/(mandateId)/2026-11-03.md` |
| c65-11 | PATCH /mandates/{mandateId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/mandates/(mandateId)/2026-11-03.md` |
| c65-12 | POST /mandates/{mandateId}/cancel | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/mandates/(mandateId)/cancel/2026-11-03.md` |
| c65-13 | DELETE /scaDevices/{deviceId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/scaDevices/(deviceId)/2026-11-03.md` |
| c65-14 | PATCH /scaDevices/{deviceId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/scaDevices/(deviceId)/2026-11-03.md` |
| c65-15 | POST /scaDevices/{deviceId}/scaAssociations | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/scaDevices/(deviceId)/scaAssociations/2026-11-03.md` |
| c65-16 | POST /balanceAccounts/{id}/transferLimits | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/2026-11-03.md` |
| c65-17 | POST /balanceAccounts/{id}/transferLimits/approve | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/approve/2026-11-03.md` |
| c65-18 | GET /balanceAccounts/{id}/transferLimits/current | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/current/2026-11-03.md` |
| c65-19 | GET /balanceAccounts/{id}/transferLimits | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/2026-11-03.md` |
| c65-20 | GET /balanceAccounts/{id}/transferLimits/{transferLimitId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/(transferLimitId)/2026-11-03.md` |
| c65-21 | DELETE /balanceAccounts/{id}/transferLimits/{transferLimitId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(id)/transferLimits/(transferLimitId)/2026-11-03.md` |
| c65-22 | POST /balancePlatforms/{id}/transferLimits | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/balancePlatforms/(id)/transferLimits/2026-11-03.md` |
| c65-23 | GET /balancePlatforms/{id}/transferLimits | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/2026-11-03.md` |
| c65-24 | GET /balancePlatforms/{id}/transferLimits/{transferLimitId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/(transferLimitId)/2026-11-03.md` |
| c65-25 | DELETE /balancePlatforms/{id}/transferLimits/{transferLimitId} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/balancePlatforms/(id)/transferLimits/(transferLimitId)/2026-11-03.md` |
| c65-26 | PATCH /registeredDevices/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/registeredDevices/(id)/2026-11-03.md` |
| c65-27 | POST /registeredDevices/{deviceId}/associations | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/post/registeredDevices/(deviceId)/associations/2026-11-03.md` |
| c65-28 | PATCH /registeredDevices/{deviceId}/associations | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/patch/registeredDevices/(deviceId)/associations/2026-11-03.md` |
| c65-29 | DELETE /registeredDevices/{id} | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform/latest/delete/registeredDevices/(id)/2026-11-03.md` |
| c65-30 | GET /legalEntities/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/2026-11-03.md` |
| c65-31 | PATCH /legalEntities/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/patch/legalEntities/(id)/2026-11-03.md` |
| c65-32 | GET /legalEntities/{id}/businessLines | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/businessLines/2026-11-03.md` |
| c65-33 | POST /legalEntities/{id}/checkVerificationErrors | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/checkVerificationErrors/2026-11-03.md` |
| c65-34 | POST /legalEntities/{id}/confirmDataReview | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/confirmDataReview/2026-11-03.md` |
| c65-35 | POST /legalEntities/{id}/requestPeriodicReview | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/requestPeriodicReview/2026-11-03.md` |
| c65-36 | GET /transferInstruments/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/transferInstruments/(id)/2026-11-03.md` |
| c65-37 | PATCH /transferInstruments/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/patch/transferInstruments/(id)/2026-11-03.md` |
| c65-38 | DELETE /transferInstruments/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/delete/transferInstruments/(id)/2026-11-03.md` |
| c65-39 | GET /businessLines/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/businessLines/(id)/2026-11-03.md` |
| c65-40 | DELETE /businessLines/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/delete/businessLines/(id)/2026-11-03.md` |
| c65-41 | PATCH /businessLines/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/patch/businessLines/(id)/2026-11-03.md` |
| c65-42 | GET /documents/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/documents/(id)/2026-11-03.md` |
| c65-43 | PATCH /documents/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/patch/documents/(id)/2026-11-03.md` |
| c65-44 | DELETE /documents/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/delete/documents/(id)/2026-11-03.md` |
| c65-45 | POST /legalEntities/{id}/termsOfService | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/termsOfService/2026-11-03.md` |
| c65-46 | PATCH /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid)/2026-11-03.md` |
| c65-47 | GET /legalEntities/{id}/termsOfServiceAcceptanceInfos | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceAcceptanceInfos/2026-11-03.md` |
| c65-48 | GET /legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/acceptedTermsOfServiceDocument/(termsofserviceacceptancereference)/2026-11-03.md` |
| c65-49 | GET /legalEntities/{id}/termsOfServiceStatus | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceStatus/2026-11-03.md` |
| c65-50 | POST /legalEntities/{id}/pciQuestionnaires/generatePciTemplates | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/generatePciTemplates/2026-11-03.md` |

Full evidence: page-results.json, summary.json and responses-network-enabled/ (successful captures); responses/ retains initial sandbox DNS failures. Separate exact ingestion approval required.
