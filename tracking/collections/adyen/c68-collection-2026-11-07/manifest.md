# Adyen C68 bounded API Explorer collection

Collection approved2026-11-07; collection completed. No ingestion or publication.

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
| c68-01 | GET /merchants/{merchantId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalSettings/2026-11-07.md` |
| c68-02 | GET /merchants/{merchantId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalLogos/2026-11-07.md` |
| c68-03 | PATCH /merchants/{merchantId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalSettings/2026-11-07.md` |
| c68-04 | PATCH /merchants/{merchantId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalLogos/2026-11-07.md` |
| c68-05 | GET /merchants/{merchantId}/stores/{reference}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalSettings/2026-11-07.md` |
| c68-06 | GET /merchants/{merchantId}/stores/{reference}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalLogos/2026-11-07.md` |
| c68-07 | PATCH /merchants/{merchantId}/stores/{reference}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalSettings/2026-11-07.md` |
| c68-08 | PATCH /merchants/{merchantId}/stores/{reference}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalLogos/2026-11-07.md` |
| c68-09 | GET /stores/{storeId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/stores/(storeId)/terminalLogos/2026-11-07.md` |
| c68-10 | PATCH /stores/{storeId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/stores/(storeId)/terminalLogos/2026-11-07.md` |
| c68-11 | GET /stores/{storeId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/stores/(storeId)/terminalSettings/2026-11-07.md` |
| c68-12 | PATCH /stores/{storeId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/stores/(storeId)/terminalSettings/2026-11-07.md` |
| c68-13 | GET /terminals/{terminalId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/terminals/(terminalId)/terminalSettings/2026-11-07.md` |
| c68-14 | GET /terminals/{terminalId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/terminals/(terminalId)/terminalLogos/2026-11-07.md` |
| c68-15 | PATCH /terminals/{terminalId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalSettings/2026-11-07.md` |
| c68-16 | PATCH /terminals/{terminalId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalLogos/2026-11-07.md` |
| c68-17 | GET /companies/{companyId}/androidApps | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/androidApps/2026-11-07.md` |
| c68-18 | GET /companies/{companyId}/androidCertificates | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/androidCertificates/2026-11-07.md` |
| c68-19 | GET /companies/{companyId}/androidApps/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/androidApps/(id)/2026-11-07.md` |
| c68-20 | POST /companies/{companyId}/androidApps | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/androidApps/2026-11-07.md` |
| c68-21 | POST /companies/{companyId}/androidCertificates | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/androidCertificates/2026-11-07.md` |
| c68-22 | PATCH /companies/{companyId}/androidApps/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/androidApps/(id)/2026-11-07.md` |
| c68-23 | POST /merchants/{merchantId}/splitConfigurations | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/2026-11-07.md` |
| c68-24 | POST /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md` |
| c68-25 | GET /merchants/{merchantId}/splitConfigurations | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/2026-11-07.md` |
| c68-26 | GET /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md` |
| c68-27 | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md` |
| c68-28 | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/2026-11-07.md` |
| c68-29 | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/splitLogic/(splitLogicId)/2026-11-07.md` |
| c68-30 | DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md` |
| c68-31 | DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/2026-11-07.md` |
| c68-32 | GET /companies/{companyId}/clientCertificates | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/clientCertificates/2026-11-07.md` |
| c68-33 | POST /companies/{companyId}/clientCertificates | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/clientCertificates/2026-11-07.md` |
| c68-34 | POST /companies/{companyId}/campaignManagement | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/2026-11-07.md` |
| c68-35 | GET /companies/{companyId}/campaignManagement/accountHolders/{accountHolderId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/campaignManagement/accountHolders/(accountHolderId)/2026-11-07.md` |
| c68-36 | DELETE /companies/{companyId}/campaignManagement/{donationCampaignId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/campaignManagement/(donationCampaignId)/2026-11-07.md` |
| c68-37 | PATCH /companies/{companyId}/campaignManagement/{donationCampaignId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/campaignManagement/(donationCampaignId)/2026-11-07.md` |
| c68-38 | POST /companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/(donationCampaignId)/status/(status)/2026-11-07.md` |
| c68-39 | POST /companies/{companyId}/nonprofits | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/nonprofits/2026-11-07.md` |
| c68-40 | GET /companies/{companyId}/terminalThemes | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/2026-11-07.md` |
| c68-41 | GET /companies/{companyId}/terminalThemes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/(id)/2026-11-07.md` |
| c68-42 | POST /companies/{companyId}/terminalThemes | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/2026-11-07.md` |
| c68-43 | POST /companies/{companyId}/terminalThemes/{id}/assets | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/2026-11-07.md` |
| c68-44 | POST /companies/{companyId}/terminalThemes/{id}/assets/replace | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/replace/2026-11-07.md` |
| c68-45 | DELETE /companies/{companyId}/terminalThemes/{id}/assets | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/assets/2026-11-07.md` |
| c68-46 | PATCH /companies/{companyId}/terminalThemes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalThemes/(id)/2026-11-07.md` |
| c68-47 | POST /companies/{companyId}/terminalThemes/{id}/apply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/apply/2026-11-07.md` |
| c68-48 | POST /companies/{companyId}/terminalThemes/unapply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/unapply/2026-11-07.md` |
| c68-49 | DELETE /companies/{companyId}/terminalThemes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/2026-11-07.md` |
| c68-50 | GET /merchants/{merchantId}/terminalThemes | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/2026-11-07.md` |

Full evidence: page-results.json, summary.json and responses/. Separate exact ingestion approval required.
