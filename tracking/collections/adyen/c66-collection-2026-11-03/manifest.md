# Adyen C66 bounded API Explorer collection

Collection approved2026-11-03; collection completed. No ingestion or publication.

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
| c66-01 | POST /legalEntities/{id}/pciQuestionnaires/signPciTemplates | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signPciTemplates/2026-11-03.md` |
| c66-02 | GET /legalEntities/{id}/pciQuestionnaires | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/2026-11-03.md` |
| c66-03 | GET /legalEntities/{id}/pciQuestionnaires/{pciid} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/(pciid)/2026-11-03.md` |
| c66-04 | POST /legalEntities/{id}/pciQuestionnaires/signingRequired | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signingRequired/2026-11-03.md` |
| c66-05 | POST /legalEntities/{id}/setTaxElectronicDeliveryConsent | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/setTaxElectronicDeliveryConsent/2026-11-03.md` |
| c66-06 | POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/checkTaxElectronicDeliveryConsent/2026-11-03.md` |
| c66-07 | POST /legalEntities/{id}/onboardingLinks | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/onboardingLinks/2026-11-03.md` |
| c66-08 | GET /themes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/legalentity/latest/get/themes/(id)/2026-11-03.md` |
| c66-09 | GET /companies/{companyId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/2026-11-03.md` |
| c66-10 | GET /companies/{companyId}/merchants | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/merchants/2026-11-03.md` |
| c66-11 | POST /merchants/{merchantId}/activate | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/activate/2026-11-03.md` |
| c66-12 | GET /merchants/{merchantId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/2026-11-03.md` |
| c66-13 | GET /merchants/{merchantId}/stores | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/2026-11-03.md` |
| c66-14 | POST /merchants/{merchantId}/stores | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/stores/2026-11-03.md` |
| c66-15 | GET /merchants/{merchantId}/stores/{storeId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(storeId)/2026-11-03.md` |
| c66-16 | PATCH /merchants/{merchantId}/stores/{storeId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId)/2026-11-03.md` |
| c66-17 | GET /stores/{storeId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/stores/(storeId)/2026-11-03.md` |
| c66-18 | PATCH /stores/{storeId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/stores/(storeId)/2026-11-03.md` |
| c66-19 | POST /merchants/{merchantId}/payoutSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/payoutSettings/2026-11-03.md` |
| c66-20 | PATCH /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03.md` |
| c66-21 | GET /merchants/{merchantId}/payoutSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/2026-11-03.md` |
| c66-22 | GET /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03.md` |
| c66-23 | DELETE /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03.md` |
| c66-24 | GET /companies/{companyId}/users | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/users/2026-11-03.md` |
| c66-25 | POST /companies/{companyId}/users | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/users/2026-11-03.md` |
| c66-26 | GET /companies/{companyId}/users/{userId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/users/(userId)/2026-11-03.md` |
| c66-27 | PATCH /companies/{companyId}/users/{userId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/users/(userId)/2026-11-03.md` |
| c66-28 | GET /merchants/{merchantId}/users | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/users/2026-11-03.md` |
| c66-29 | POST /merchants/{merchantId}/users | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/users/2026-11-03.md` |
| c66-30 | GET /merchants/{merchantId}/users/{userId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/users/(userId)/2026-11-03.md` |
| c66-31 | PATCH /merchants/{merchantId}/users/{userId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/users/(userId)/2026-11-03.md` |
| c66-32 | GET /me/allowedOrigins/{originId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/me/allowedOrigins/(originId)/2026-11-03.md` |
| c66-33 | DELETE /me/allowedOrigins/{originId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/me/allowedOrigins/(originId)/2026-11-03.md` |
| c66-34 | GET /companies/{companyId}/apiCredentials | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/2026-11-03.md` |
| c66-35 | POST /companies/{companyId}/apiCredentials | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/2026-11-03.md` |
| c66-36 | GET /companies/{companyId}/apiCredentials/{apiCredentialId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/2026-11-03.md` |
| c66-37 | PATCH /companies/{companyId}/apiCredentials/{apiCredentialId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/apiCredentials/(apiCredentialId)/2026-11-03.md` |
| c66-38 | GET /merchants/{merchantId}/apiCredentials | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/2026-11-03.md` |
| c66-39 | POST /merchants/{merchantId}/apiCredentials | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/2026-11-03.md` |
| c66-40 | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/2026-11-03.md` |
| c66-41 | PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/apiCredentials/(apiCredentialId)/2026-11-03.md` |
| c66-42 | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateApiKey/2026-11-03.md` |
| c66-43 | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateApiKey/2026-11-03.md` |
| c66-44 | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateClientKey/2026-11-03.md` |
| c66-45 | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateClientKey/2026-11-03.md` |
| c66-46 | GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03.md` |
| c66-47 | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03.md` |
| c66-48 | GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-03.md` |
| c66-49 | DELETE /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-03.md` |
| c66-50 | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03.md` |

Full evidence: page-results.json, summary.json and responses/. Separate exact ingestion approval required.
