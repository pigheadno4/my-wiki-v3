# Adyen C68 collected API Explorer ingestion selection

Status: **COMPLETE — all 50 sources approved and validated**. Prepared 2026-11-07.

Approved collection completed for all50 exact URLs: **50 HTTP200 substantive Markdown pages**, no failed, title-only or mismatched documents. Families: **Management50**. Every response body is preserved byte-for-byte after collection metadata in a new dated2026-11-07 raw file. All prior Adyen raw/wiki hashes are unchanged; concurrent unrelated PayPal work is recorded separately. These title/body/byte checks are collection screening, not full semantic reads. [Collection manifest](../../../collections/adyen/c68-collection-2026-11-07/manifest.md), [summary](../../../collections/adyen/c68-collection-2026-11-07/summary.json). Original proposal retained in [collection-selection-review.md](collection-selection-review.md).

Exact proposed ingestion: **50 source units**, **100 fixed answers**, **three predetermined distinct full-read audits**. All hashes, URL/target uniqueness, absent canonical targets and unreferenced pins verified. Size: **121,812 whitespace words, 12,326 raw lines, 798,258 bytes**. Source generation begins only after separate exact ingestion approval.

Current baseline **3,109 = 2,547 General Docs +546 API Explorer +16 GitHub**. Successful ingestion of all50 gives **3,159 = 2,547 General Docs +596 API Explorer +16 GitHub**. API Explorer now has623 local raw pages:546 ingested substantive pages,50 newly collected and27 excluded title-only stubs. Unreferenced local raw would decline77→27 after successful ingestion. The captured670-URL catalog has **47 URLs still without local raw**; the27 stub exclusions remain separate. This is captured-catalog coverage, not a current upstream completeness claim.

[Proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers/different high initial reviewers, full numbered reads of every schema/example,3–5locatedquotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [100 original fixed prompts](proposed-queries.md) require actual independently checked answers. Full raw reads apply to every captured schema, authentication/security qualification and example, including minimal references.

Fixed coordinator audit jobs: `api-explorer-management-latest-get-merchants-merchantid-terminallogos`, `api-explorer-management-latest-patch-terminals-terminalid-terminalsettings`, `api-explorer-management-latest-get-companies-companyid-androidapps`. Material partial/fail expands to all50. No ingestion runtime, dispatch, canonical wiki source generation, commit or push. Await separate exact C68 ingestion approval.

| # | Family | Operation | Words | Raw lines |
| --- | --- | --- | ---: | ---: |
| 1 | Management | GET /merchants/{merchantId}/terminalSettings | 5,037 | 400 |
| 2 | Management | GET /merchants/{merchantId}/terminalLogos | 1,357 | 158 |
| 3 | Management | PATCH /merchants/{merchantId}/terminalSettings | 9,035 | 753 |
| 4 | Management | PATCH /merchants/{merchantId}/terminalLogos | 1,432 | 187 |
| 5 | Management | GET /merchants/{merchantId}/stores/{reference}/terminalSettings | 5,043 | 399 |
| 6 | Management | GET /merchants/{merchantId}/stores/{reference}/terminalLogos | 1,365 | 159 |
| 7 | Management | PATCH /merchants/{merchantId}/stores/{reference}/terminalSettings | 9,097 | 787 |
| 8 | Management | PATCH /merchants/{merchantId}/stores/{reference}/terminalLogos | 1,447 | 188 |
| 9 | Management | GET /stores/{storeId}/terminalLogos | 1,334 | 154 |
| 10 | Management | PATCH /stores/{storeId}/terminalLogos | 1,417 | 183 |
| 11 | Management | GET /stores/{storeId}/terminalSettings | 5,056 | 420 |
| 12 | Management | PATCH /stores/{storeId}/terminalSettings | 9,079 | 788 |
| 13 | Management | GET /terminals/{terminalId}/terminalSettings | 5,052 | 428 |
| 14 | Management | GET /terminals/{terminalId}/terminalLogos | 1,258 | 147 |
| 15 | Management | PATCH /terminals/{terminalId}/terminalSettings | 9,111 | 814 |
| 16 | Management | PATCH /terminals/{terminalId}/terminalLogos | 1,325 | 176 |
| 17 | Management | GET /companies/{companyId}/androidApps | 1,663 | 190 |
| 18 | Management | GET /companies/{companyId}/androidCertificates | 1,507 | 185 |
| 19 | Management | GET /companies/{companyId}/androidApps/{id} | 1,497 | 147 |
| 20 | Management | POST /companies/{companyId}/androidApps | 1,241 | 135 |
| 21 | Management | POST /companies/{companyId}/androidCertificates | 1,201 | 133 |
| 22 | Management | PATCH /companies/{companyId}/androidApps/{id} | 1,244 | 135 |
| 23 | Management | POST /merchants/{merchantId}/splitConfigurations | 3,592 | 262 |
| 24 | Management | POST /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | 3,658 | 285 |
| 25 | Management | GET /merchants/{merchantId}/splitConfigurations | 1,882 | 239 |
| 26 | Management | GET /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | 2,461 | 224 |
| 27 | Management | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | 2,507 | 238 |
| 28 | Management | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | 2,759 | 246 |
| 29 | Management | PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId} | 3,237 | 274 |
| 30 | Management | DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | 2,353 | 164 |
| 31 | Management | DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | 2,357 | 165 |
| 32 | Management | GET /companies/{companyId}/clientCertificates | 1,054 | 135 |
| 33 | Management | POST /companies/{companyId}/clientCertificates | 1,679 | 194 |
| 34 | Management | POST /companies/{companyId}/campaignManagement | 2,743 | 205 |
| 35 | Management | GET /companies/{companyId}/campaignManagement/accountHolders/{accountHolderId} | 2,362 | 200 |
| 36 | Management | DELETE /companies/{companyId}/campaignManagement/{donationCampaignId} | 1,329 | 141 |
| 37 | Management | PATCH /companies/{companyId}/campaignManagement/{donationCampaignId} | 2,308 | 193 |
| 38 | Management | POST /companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status} | 2,222 | 182 |
| 39 | Management | POST /companies/{companyId}/nonprofits | 1,887 | 184 |
| 40 | Management | GET /companies/{companyId}/terminalThemes | 548 | 174 |
| 41 | Management | GET /companies/{companyId}/terminalThemes/{id} | 502 | 147 |
| 42 | Management | POST /companies/{companyId}/terminalThemes | 548 | 192 |
| 43 | Management | POST /companies/{companyId}/terminalThemes/{id}/assets | 874 | 210 |
| 44 | Management | POST /companies/{companyId}/terminalThemes/{id}/assets/replace | 885 | 213 |
| 45 | Management | DELETE /companies/{companyId}/terminalThemes/{id}/assets | 457 | 129 |
| 46 | Management | PATCH /companies/{companyId}/terminalThemes/{id} | 463 | 171 |
| 47 | Management | POST /companies/{companyId}/terminalThemes/{id}/apply | 246 | 97 |
| 48 | Management | POST /companies/{companyId}/terminalThemes/unapply | 287 | 109 |
| 49 | Management | DELETE /companies/{companyId}/terminalThemes/{id} | 271 | 113 |
| 50 | Management | GET /merchants/{merchantId}/terminalThemes | 543 | 174 |

User approved exact C68 ingestion on2026-11-07 after50hash/count checks. Historical preparation statements above retain their pre-approval meaning. No commit/push.

C68 closed: 3159 total sources; 596 API Explorer sources. Remaining 27 API raw pages are excluded title-only stubs. No commit/push.
