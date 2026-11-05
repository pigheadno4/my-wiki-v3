# Adyen C67 collected API Explorer ingestion selection

Status: **PREPARED ONLY — awaiting exact ingestion approval**. Prepared 2026-11-05.

Approved collection completed for all50 exact URLs: **50 HTTP200 substantive Markdown pages**, no failed, title-only or mismatched documents. Families: **Management50**. Every response body is preserved byte-for-byte after collection metadata in a new dated2026-11-05 raw file. All prior Adyen raw/wiki hashes are unchanged; concurrent unrelated PayPal work is recorded separately. These title/body/byte checks are collection screening, not full semantic reads. [Collection manifest](../../../collections/adyen/c67-collection-2026-11-05/manifest.md), [summary](../../../collections/adyen/c67-collection-2026-11-05/summary.json). Original proposal retained in [collection-selection-review.md](collection-selection-review.md).

Exact proposed ingestion: **50 source units**, **100 fixed answers**, **three predetermined distinct full-read audits**. All hashes, URL/target uniqueness, absent canonical targets and unreferenced pins verified. Size: **132,706 whitespace words, 12,782 raw lines, 853,262 bytes**. Source generation begins only after separate exact ingestion approval.

Current baseline **3,059 = 2,547 General Docs +496 API Explorer +16 GitHub**. Successful ingestion of all50 gives **3,109 = 2,547 General Docs +546 API Explorer +16 GitHub**. API Explorer now has573 local raw pages:496 ingested substantive pages,50 newly collected and27 excluded title-only stubs. Unreferenced local raw would decline77→27 after successful ingestion. The captured670-URL catalog has **97 URLs still without local raw**; the27 stub exclusions remain separate. This is captured-catalog coverage, not a current upstream completeness claim.

[Proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers/different high initial reviewers, full numbered reads of every schema/example,3–5locatedquotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [100 original fixed prompts](proposed-queries.md) require actual independently checked answers. Full raw reads apply to every captured schema, authentication/security qualification and example, including minimal references.

Fixed coordinator audit jobs: `api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-allowedorigins`, `api-explorer-management-latest-post-merchants-merchantid-paymentmethodsettings`, `api-explorer-management-latest-get-companies-companyid-terminalmodels`. Material partial/fail expands to all50. No ingestion runtime, dispatch, canonical wiki source generation, commit or push. Await separate exact C67 ingestion approval.

| # | Family | Operation | Words | Raw lines |
| --- | --- | --- | ---: | ---: |
| 1 | Management | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | 1,385 | 174 |
| 2 | Management | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | 1,306 | 158 |
| 3 | Management | DELETE /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | 1,215 | 128 |
| 4 | Management | POST /companies/{companyId}/webhooks | 2,770 | 317 |
| 5 | Management | GET /companies/{companyId}/webhooks | 2,411 | 305 |
| 6 | Management | GET /companies/{companyId}/webhooks/{webhookId} | 2,183 | 272 |
| 7 | Management | PATCH /companies/{companyId}/webhooks/{webhookId} | 2,712 | 300 |
| 8 | Management | DELETE /companies/{companyId}/webhooks/{webhookId} | 1,184 | 127 |
| 9 | Management | POST /companies/{companyId}/webhooks/{webhookId}/generateHmac | 1,254 | 143 |
| 10 | Management | POST /companies/{companyId}/webhooks/{webhookId}/test | 2,137 | 250 |
| 11 | Management | POST /merchants/{merchantId}/webhooks | 2,662 | 311 |
| 12 | Management | GET /merchants/{merchantId}/webhooks | 2,455 | 310 |
| 13 | Management | GET /merchants/{merchantId}/webhooks/{webhookId} | 2,197 | 275 |
| 14 | Management | PATCH /merchants/{merchantId}/webhooks/{webhookId} | 2,616 | 301 |
| 15 | Management | DELETE /merchants/{merchantId}/webhooks/{webhookId} | 1,184 | 127 |
| 16 | Management | POST /merchants/{merchantId}/webhooks/{webhookId}/generateHmac | 1,263 | 147 |
| 17 | Management | POST /merchants/{merchantId}/webhooks/{webhookId}/test | 1,991 | 227 |
| 18 | Management | POST /merchants/{merchantId}/paymentMethodSettings | 14,231 | 608 |
| 19 | Management | GET /merchants/{merchantId}/paymentMethodSettings | 4,231 | 328 |
| 20 | Management | GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | 7,431 | 349 |
| 21 | Management | PATCH /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | 12,260 | 495 |
| 22 | Management | POST /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | 1,473 | 162 |
| 23 | Management | GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | 1,243 | 136 |
| 24 | Management | POST /terminals/{terminalId}/reassign | 1,350 | 153 |
| 25 | Management | GET /companies/{companyId}/terminalActions | 1,506 | 173 |
| 26 | Management | GET /companies/{companyId}/terminalActions/{actionId} | 1,375 | 160 |
| 27 | Management | GET /companies/{companyId}/terminalModels | 1,563 | 302 |
| 28 | Management | GET /companies/{companyId}/terminalProducts | 1,547 | 216 |
| 29 | Management | GET /companies/{companyId}/billingEntities | 1,571 | 190 |
| 30 | Management | GET /companies/{companyId}/shippingLocations | 1,674 | 205 |
| 31 | Management | POST /companies/{companyId}/shippingLocations | 1,868 | 216 |
| 32 | Management | POST /companies/{companyId}/terminalOrders | 2,281 | 265 |
| 33 | Management | GET /companies/{companyId}/terminalOrders | 1,869 | 260 |
| 34 | Management | GET /companies/{companyId}/terminalOrders/{orderId} | 2,042 | 229 |
| 35 | Management | PATCH /companies/{companyId}/terminalOrders/{orderId} | 2,346 | 278 |
| 36 | Management | POST /companies/{companyId}/terminalOrders/{orderId}/cancel | 2,069 | 229 |
| 37 | Management | GET /merchants/{merchantId}/terminalModels | 1,577 | 305 |
| 38 | Management | GET /merchants/{merchantId}/terminalProducts | 1,563 | 220 |
| 39 | Management | GET /merchants/{merchantId}/billingEntities | 1,555 | 182 |
| 40 | Management | GET /merchants/{merchantId}/shippingLocations | 1,648 | 193 |
| 41 | Management | POST /merchants/{merchantId}/shippingLocations | 1,885 | 220 |
| 42 | Management | POST /merchants/{merchantId}/terminalOrders | 2,305 | 270 |
| 43 | Management | GET /merchants/{merchantId}/terminalOrders | 1,886 | 270 |
| 44 | Management | GET /merchants/{merchantId}/terminalOrders/{orderId} | 2,063 | 234 |
| 45 | Management | PATCH /merchants/{merchantId}/terminalOrders/{orderId} | 2,366 | 282 |
| 46 | Management | POST /merchants/{merchantId}/terminalOrders/{orderId}/cancel | 2,090 | 234 |
| 47 | Management | GET /companies/{companyId}/terminalSettings | 5,063 | 420 |
| 48 | Management | GET /companies/{companyId}/terminalLogos | 1,342 | 155 |
| 49 | Management | PATCH /companies/{companyId}/terminalSettings | 9,087 | 788 |
| 50 | Management | PATCH /companies/{companyId}/terminalLogos | 1,421 | 183 |
