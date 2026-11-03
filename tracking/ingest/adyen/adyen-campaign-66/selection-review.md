# Adyen C66 collected API Explorer ingestion selection

Status: **PREPARED ONLY — awaiting exact ingestion approval**. Prepared 2026-11-03.

Approved collection completed for all50 exact URLs: **50 HTTP200 substantive Markdown pages**, no failed, title-only or mismatched documents. Families: **Legal Entity8 + Management42**. Every response body is preserved byte-for-byte after collection metadata in a new dated2026-11-03 raw file. All prior Adyen raw/wiki hashes are unchanged; any unrelated concurrent changes are recorded separately. These title/body/byte checks are collection screening, not full semantic reads. [Collection manifest](../../../collections/adyen/c66-collection-2026-11-03/manifest.md), [summary](../../../collections/adyen/c66-collection-2026-11-03/summary.json). Original proposal retained in [collection-selection-review.md](collection-selection-review.md).

Exact proposed ingestion: **50 source units**, **100 fixed answers**, **three predetermined distinct full-read audits**. All hashes, URL/target uniqueness, absent canonical targets and unreferenced pins verified. Size: **78,831 whitespace words, 9,602 raw lines, 498,723 bytes**. Source generation begins only after separate exact ingestion approval.

Current baseline **3,009 = 2,547 General Docs +446 API Explorer +16 GitHub**. Successful ingestion of all50 gives **3,059 = 2,547 General Docs +496 API Explorer +16 GitHub**. API Explorer now has523 local raw pages:446 ingested substantive pages,50 newly collected and27 excluded title-only stubs. Unreferenced local raw would decline77→27 after successful ingestion. The captured670-URL catalog has **147 URLs still without local raw**; the27 stub exclusions remain separate. This is captured-catalog coverage, not a current upstream completeness claim.

[Proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers/different high initial reviewers, full numbered reads of every schema/example,3–5locatedquotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [100 original fixed prompts](proposed-queries.md) require actual independently checked answers. Full raw reads apply to every captured schema, authentication/security qualification and example, including minimal references.

Fixed coordinator audit jobs: `api-explorer-management-latest-get-companies-companyid`, `api-explorer-management-latest-patch-merchants-merchantid-stores-storeid`, `api-explorer-legalentity-latest-get-legalentities-id-pciquestionnaires-pciid`. Material partial/fail expands to all50. No ingestion runtime, dispatch, canonical wiki source generation, commit or push. Await separate exact C66 ingestion approval.

| # | Family | Operation | Words | Raw lines |
| --- | --- | --- | ---: | ---: |
| 1 | legalentity | POST /legalEntities/{id}/pciQuestionnaires/signPciTemplates | 697 | 134 |
| 2 | legalentity | GET /legalEntities/{id}/pciQuestionnaires | 683 | 125 |
| 3 | legalentity | GET /legalEntities/{id}/pciQuestionnaires/{pciid} | 682 | 118 |
| 4 | legalentity | POST /legalEntities/{id}/pciQuestionnaires/signingRequired | 677 | 106 |
| 5 | legalentity | POST /legalEntities/{id}/setTaxElectronicDeliveryConsent | 625 | 101 |
| 6 | legalentity | POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent | 617 | 100 |
| 7 | legalentity | POST /legalEntities/{id}/onboardingLinks | 1,387 | 147 |
| 8 | legalentity | GET /themes/{id} | 687 | 128 |
| 9 | Management | GET /companies/{companyId} | 1,585 | 180 |
| 10 | Management | GET /companies/{companyId}/merchants | 2,455 | 434 |
| 11 | Management | POST /merchants/{merchantId}/activate | 1,278 | 140 |
| 12 | Management | GET /merchants/{merchantId} | 1,852 | 190 |
| 13 | Management | GET /merchants/{merchantId}/stores | 2,347 | 260 |
| 14 | Management | POST /merchants/{merchantId}/stores | 2,780 | 250 |
| 15 | Management | GET /merchants/{merchantId}/stores/{storeId} | 2,066 | 200 |
| 16 | Management | PATCH /merchants/{merchantId}/stores/{storeId} | 2,817 | 324 |
| 17 | Management | GET /stores/{storeId} | 2,038 | 196 |
| 18 | Management | PATCH /stores/{storeId} | 2,729 | 289 |
| 19 | Management | POST /merchants/{merchantId}/payoutSettings | 1,747 | 153 |
| 20 | Management | PATCH /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | 1,607 | 150 |
| 21 | Management | GET /merchants/{merchantId}/payoutSettings | 1,566 | 144 |
| 22 | Management | GET /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | 1,551 | 144 |
| 23 | Management | DELETE /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | 1,208 | 129 |
| 24 | Management | GET /companies/{companyId}/users | 1,648 | 166 |
| 25 | Management | POST /companies/{companyId}/users | 1,753 | 254 |
| 26 | Management | GET /companies/{companyId}/users/{userId} | 1,414 | 146 |
| 27 | Management | PATCH /companies/{companyId}/users/{userId} | 1,604 | 161 |
| 28 | Management | GET /merchants/{merchantId}/users | 1,642 | 169 |
| 29 | Management | POST /merchants/{merchantId}/users | 1,704 | 240 |
| 30 | Management | GET /merchants/{merchantId}/users/{userId} | 1,407 | 149 |
| 31 | Management | PATCH /merchants/{merchantId}/users/{userId} | 1,583 | 163 |
| 32 | Management | GET /me/allowedOrigins/{originId} | 1,248 | 134 |
| 33 | Management | DELETE /me/allowedOrigins/{originId} | 1,174 | 125 |
| 34 | Management | GET /companies/{companyId}/apiCredentials | 2,505 | 522 |
| 35 | Management | POST /companies/{companyId}/apiCredentials | 2,001 | 251 |
| 36 | Management | GET /companies/{companyId}/apiCredentials/{apiCredentialId} | 1,801 | 216 |
| 37 | Management | PATCH /companies/{companyId}/apiCredentials/{apiCredentialId} | 2,000 | 225 |
| 38 | Management | GET /merchants/{merchantId}/apiCredentials | 2,627 | 549 |
| 39 | Management | POST /merchants/{merchantId}/apiCredentials | 1,950 | 243 |
| 40 | Management | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId} | 1,731 | 196 |
| 41 | Management | PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId} | 1,897 | 226 |
| 42 | Management | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey | 1,227 | 132 |
| 43 | Management | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | 1,242 | 136 |
| 44 | Management | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey | 1,230 | 132 |
| 45 | Management | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey | 1,245 | 136 |
| 46 | Management | GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | 1,312 | 166 |
| 47 | Management | POST /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | 1,372 | 171 |
| 48 | Management | GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | 1,291 | 154 |
| 49 | Management | DELETE /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | 1,215 | 128 |
| 50 | Management | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | 1,327 | 170 |
