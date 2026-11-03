# Adyen C66 API Explorer collection-first preparation

Status: **AWAITING EXACT COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared 2026-11-03 after C65 publication `7c15ef604868cf04a9af6d8fc7449fa3d096494a`.

C65 ingested all 50 pages: Balance Platform 29 and Legal Entity 21. Current totals: **3,009 sources = 2,547 General Docs + 446 API Explorer + 16 GitHub**. All locally collected complete-body API Explorer pages are ingested. The only 27 unreferenced local raw pages are excluded title-only stubs, retried in C63 and still title-only. No repeated stub retries proposed here.

## Pinned catalog reconciliation

The official API Explorer catalog captured 2026-11-02 contains **670 distinct normalized documentation URLs** (623 operation references and 47 overview references). Exact-URL reconciliation on 2026-11-03 finds 473 local raw URLs: 446 with ingested raw and 27 excluded title-only stubs. **197 catalog URLs have no local raw**. All 473 local URLs occur in the pinned catalog. [Complete reconciliation](catalog-reconciliation.json) retains its SHA256 and all missing URLs.

This is reconciliation against an immutable captured catalog, not a refreshed upstream inventory or a claim about present page availability. No network requests or semantic reads of the proposed pages were made. Titles and paths identify navigation scope only.

## Exact next collection proposal

Propose **50 exact official Markdown URLs**: the remaining 8 Legal Entity references and the first 42 uncollected Management references in captured catalog order. Metadata scope spans the remaining Legal Entity references and the next Management references. All navigation labels are listed below for inspection. No behavior is inferred from these names. Every selected URL has a pinned catalog-line locator; the documented duplicated API Explorer prefix is collapsed, retaining official case and parenthesized parameters. Every raw directory and provisional source target is absent and all URLs/targets are unique. [Exact 50-target proposal](collection-proposal.json).

Approval authorizes documentation collection for these 50 URLs only. Stage each response, retain status/headers/body/hash and final URL, omit server-set cookies from published metadata, and classify substantive/failed/title-only results separately. Preserve substantive body bytes verbatim in new dated immutable raw snapshots. No whole-corpus refresh, code/rule/validator changes, General Docs, GitHub, stub retries, provider/account/security/device/payment operations, automatic ingestion or further publication. Endpoint action names describe documentation targets, not authorized API calls.

After all 50 selected URLs reach recorded outcomes, reconcile results and prepare an exact ingestion manifest only from recovered complete-body evidence: raw SHA256 pins, actual fixed query prompts, three distinct audit samples and explicit provider review authorization. Obtain separate ingestion approval per rules/psp-collection.md. Do not pad failed or incomplete results or waive body/schema presence. If all 50 collect successfully, 147 captured-catalog URLs would still lack raw; source counts rise only after approved ingestion.

C66 is **PREPARED ONLY / awaiting approval**. No runtime, dispatch, candidates, raw collection or canonical sources created. Publishing this proposal does not authorize execution.

| Item | Family | Catalog label | Exact Markdown URL |
| --- | --- | --- | --- |
| c66-01 | legalentity | POST /legalEntities/{id}/pciQuestionnaires/signPciTemplates | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signPciTemplates.md` |
| c66-02 | legalentity | GET /legalEntities/{id}/pciQuestionnaires | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires.md` |
| c66-03 | legalentity | GET /legalEntities/{id}/pciQuestionnaires/{pciid} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/(pciid).md` |
| c66-04 | legalentity | POST /legalEntities/{id}/pciQuestionnaires/signingRequired | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signingRequired.md` |
| c66-05 | legalentity | POST /legalEntities/{id}/setTaxElectronicDeliveryConsent | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/setTaxElectronicDeliveryConsent.md` |
| c66-06 | legalentity | POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/checkTaxElectronicDeliveryConsent.md` |
| c66-07 | legalentity | POST /legalEntities/{id}/onboardingLinks | `https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/onboardingLinks.md` |
| c66-08 | legalentity | GET /themes/{id} | `https://docs.adyen.com/api-explorer/legalentity/latest/get/themes/(id).md` |
| c66-09 | Management | GET /companies/{companyId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId).md` |
| c66-10 | Management | GET /companies/{companyId}/merchants | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/merchants.md` |
| c66-11 | Management | POST /merchants/{merchantId}/activate | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/activate.md` |
| c66-12 | Management | GET /merchants/{merchantId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId).md` |
| c66-13 | Management | GET /merchants/{merchantId}/stores | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores.md` |
| c66-14 | Management | POST /merchants/{merchantId}/stores | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/stores.md` |
| c66-15 | Management | GET /merchants/{merchantId}/stores/{storeId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(storeId).md` |
| c66-16 | Management | PATCH /merchants/{merchantId}/stores/{storeId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId).md` |
| c66-17 | Management | GET /stores/{storeId} | `https://docs.adyen.com/api-explorer/Management/latest/get/stores/(storeId).md` |
| c66-18 | Management | PATCH /stores/{storeId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/stores/(storeId).md` |
| c66-19 | Management | POST /merchants/{merchantId}/payoutSettings | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/payoutSettings.md` |
| c66-20 | Management | PATCH /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId).md` |
| c66-21 | Management | GET /merchants/{merchantId}/payoutSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings.md` |
| c66-22 | Management | GET /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/(payoutSettingsId).md` |
| c66-23 | Management | DELETE /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/payoutSettings/(payoutSettingsId).md` |
| c66-24 | Management | GET /companies/{companyId}/users | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/users.md` |
| c66-25 | Management | POST /companies/{companyId}/users | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/users.md` |
| c66-26 | Management | GET /companies/{companyId}/users/{userId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/users/(userId).md` |
| c66-27 | Management | PATCH /companies/{companyId}/users/{userId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/users/(userId).md` |
| c66-28 | Management | GET /merchants/{merchantId}/users | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/users.md` |
| c66-29 | Management | POST /merchants/{merchantId}/users | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/users.md` |
| c66-30 | Management | GET /merchants/{merchantId}/users/{userId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/users/(userId).md` |
| c66-31 | Management | PATCH /merchants/{merchantId}/users/{userId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/users/(userId).md` |
| c66-32 | Management | GET /me/allowedOrigins/{originId} | `https://docs.adyen.com/api-explorer/Management/latest/get/me/allowedOrigins/(originId).md` |
| c66-33 | Management | DELETE /me/allowedOrigins/{originId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/me/allowedOrigins/(originId).md` |
| c66-34 | Management | GET /companies/{companyId}/apiCredentials | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials.md` |
| c66-35 | Management | POST /companies/{companyId}/apiCredentials | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials.md` |
| c66-36 | Management | GET /companies/{companyId}/apiCredentials/{apiCredentialId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId).md` |
| c66-37 | Management | PATCH /companies/{companyId}/apiCredentials/{apiCredentialId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/apiCredentials/(apiCredentialId).md` |
| c66-38 | Management | GET /merchants/{merchantId}/apiCredentials | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials.md` |
| c66-39 | Management | POST /merchants/{merchantId}/apiCredentials | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials.md` |
| c66-40 | Management | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId).md` |
| c66-41 | Management | PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/apiCredentials/(apiCredentialId).md` |
| c66-42 | Management | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateApiKey.md` |
| c66-43 | Management | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateApiKey.md` |
| c66-44 | Management | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateClientKey.md` |
| c66-45 | Management | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateClientKey.md` |
| c66-46 | Management | GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins.md` |
| c66-47 | Management | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins.md` |
| c66-48 | Management | GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId).md` |
| c66-49 | Management | DELETE /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId).md` |
| c66-50 | Management | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins.md` |
