# Adyen C68 API Explorer collection-first preparation

Status: **AWAITING EXACT COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared 2026-11-07 after C67 publication `e117a5eaba9572ef70fa4d97a40023ff0539c2d1`.

C67 ingested all 50 Management pages. Current totals: **3,109 sources = 2,547 General Docs + 546 API Explorer + 16 GitHub**. All locally collected complete-body API Explorer pages are ingested. The only 27 unreferenced local raw pages are excluded title-only stubs, retried in C63 and still title-only. No repeated stub retries proposed here.

## Pinned catalog reconciliation

The official API Explorer catalog captured 2026-11-02 contains **670 distinct normalized documentation URLs** (623 operation references and 47 overview references). Exact-URL reconciliation on 2026-11-07 finds 573 local raw URLs: 546 with ingested raw and 27 excluded title-only stubs. **97 catalog URLs have no local raw**. All 573 local URLs occur in the pinned catalog. [Complete reconciliation](catalog-reconciliation.json) retains its SHA256 and all missing URLs.

This is reconciliation against an immutable captured catalog, not a refreshed upstream inventory or a claim about present page availability. No network requests or semantic reads of the proposed pages were made. Titles and paths identify navigation scope only.

## Exact next collection proposal

Propose **50 exact official Markdown URLs**: the next 50 uncollected Management references in captured catalog order. Metadata scope covers the next Management references. All navigation labels are listed below for inspection. No behavior is inferred from these names. Every selected URL has a pinned catalog-line locator; the documented duplicated API Explorer prefix is collapsed, retaining official case and parenthesized parameters. Every raw directory and provisional source target is absent and all URLs/targets are unique. [Exact 50-target proposal](collection-proposal.json).

Approval authorizes documentation collection for these 50 URLs only. Stage each response, retain status/headers/body/hash and final URL, omit server-set cookies from published metadata, and classify substantive/failed/title-only results separately. Preserve substantive body bytes verbatim in new dated immutable raw snapshots. No whole-corpus refresh, code/rule/validator changes, General Docs, GitHub, stub retries, provider/account/security/device/payment operations, automatic ingestion or further publication. Endpoint action names describe documentation targets, not authorized API calls.

After all 50 selected URLs reach recorded outcomes, reconcile results and prepare an exact ingestion manifest only from recovered complete-body evidence: raw SHA256 pins, actual fixed query prompts, three distinct audit samples and explicit provider review authorization. Obtain separate ingestion approval per rules/psp-collection.md. Do not pad failed or incomplete results or waive body/schema presence. If all 50 collect successfully, 47 captured-catalog URLs would still lack raw; source counts rise only after approved ingestion.

C68 is **PREPARED ONLY / awaiting approval**. No runtime, dispatch, candidates, raw collection or canonical sources created. Publishing this proposal does not authorize execution.

| Item | Family | Catalog label | Exact Markdown URL |
| --- | --- | --- | --- |
| c68-01 | Management | GET /merchants/{merchantId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalSettings.md` |
| c68-02 | Management | GET /merchants/{merchantId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalLogos.md` |
| c68-03 | Management | PATCH /merchants/{merchantId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalSettings.md` |
| c68-04 | Management | PATCH /merchants/{merchantId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalLogos.md` |
| c68-05 | Management | GET /merchants/{merchantId}/stores/{reference}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalSettings.md` |
| c68-06 | Management | GET /merchants/{merchantId}/stores/{reference}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalLogos.md` |
| c68-07 | Management | PATCH /merchants/{merchantId}/stores/{reference}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalSettings.md` |
| c68-08 | Management | PATCH /merchants/{merchantId}/stores/{reference}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalLogos.md` |
| c68-09 | Management | GET /stores/{storeId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/get/stores/(storeId)/terminalLogos.md` |
| c68-10 | Management | PATCH /stores/{storeId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/patch/stores/(storeId)/terminalLogos.md` |
| c68-11 | Management | GET /stores/{storeId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/stores/(storeId)/terminalSettings.md` |
| c68-12 | Management | PATCH /stores/{storeId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/patch/stores/(storeId)/terminalSettings.md` |
| c68-13 | Management | GET /terminals/{terminalId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/terminals/(terminalId)/terminalSettings.md` |
| c68-14 | Management | GET /terminals/{terminalId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/get/terminals/(terminalId)/terminalLogos.md` |
| c68-15 | Management | PATCH /terminals/{terminalId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalSettings.md` |
| c68-16 | Management | PATCH /terminals/{terminalId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalLogos.md` |
| c68-17 | Management | GET /companies/{companyId}/androidApps | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/androidApps.md` |
| c68-18 | Management | GET /companies/{companyId}/androidCertificates | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/androidCertificates.md` |
| c68-19 | Management | GET /companies/{companyId}/androidApps/{id} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/androidApps/(id).md` |
| c68-20 | Management | POST /companies/{companyId}/androidApps | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/androidApps.md` |
| c68-21 | Management | POST /companies/{companyId}/androidCertificates | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/androidCertificates.md` |
| c68-22 | Management | PATCH /companies/{companyId}/androidApps/{id} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/androidApps/(id).md` |
| c68-23 | Management | POST /merchants/{merchantId}/splitConfigurations | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations.md` |
| c68-24 | Management | POST /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/(splitConfigurationId).md` |
| c68-25 | Management | GET /merchants/{merchantId}/splitConfigurations | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations.md` |
| c68-26 | Management | GET /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/(splitConfigurationId).md` |
| c68-27 | Management | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId).md` |
| c68-28 | Management | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId).md` |
| c68-29 | Management | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/splitLogic/(splitLogicId).md` |
| c68-30 | Management | DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId).md` |
| c68-31 | Management | DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId).md` |
| c68-32 | Management | GET /companies/{companyId}/clientCertificates | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/clientCertificates.md` |
| c68-33 | Management | POST /companies/{companyId}/clientCertificates | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/clientCertificates.md` |
| c68-34 | Management | POST /companies/{companyId}/campaignManagement | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement.md` |
| c68-35 | Management | GET /companies/{companyId}/campaignManagement/accountHolders/{accountHolderId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/campaignManagement/accountHolders/(accountHolderId).md` |
| c68-36 | Management | DELETE /companies/{companyId}/campaignManagement/{donationCampaignId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/campaignManagement/(donationCampaignId).md` |
| c68-37 | Management | PATCH /companies/{companyId}/campaignManagement/{donationCampaignId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/campaignManagement/(donationCampaignId).md` |
| c68-38 | Management | POST /companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status} | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/(donationCampaignId)/status/(status).md` |
| c68-39 | Management | POST /companies/{companyId}/nonprofits | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/nonprofits.md` |
| c68-40 | Management | GET /companies/{companyId}/terminalThemes | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes.md` |
| c68-41 | Management | GET /companies/{companyId}/terminalThemes/{id} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/(id).md` |
| c68-42 | Management | POST /companies/{companyId}/terminalThemes | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes.md` |
| c68-43 | Management | POST /companies/{companyId}/terminalThemes/{id}/assets | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets.md` |
| c68-44 | Management | POST /companies/{companyId}/terminalThemes/{id}/assets/replace | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/replace.md` |
| c68-45 | Management | DELETE /companies/{companyId}/terminalThemes/{id}/assets | `https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/assets.md` |
| c68-46 | Management | PATCH /companies/{companyId}/terminalThemes/{id} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalThemes/(id).md` |
| c68-47 | Management | POST /companies/{companyId}/terminalThemes/{id}/apply | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/apply.md` |
| c68-48 | Management | POST /companies/{companyId}/terminalThemes/unapply | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/unapply.md` |
| c68-49 | Management | DELETE /companies/{companyId}/terminalThemes/{id} | `https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id).md` |
| c68-50 | Management | GET /merchants/{merchantId}/terminalThemes | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes.md` |
