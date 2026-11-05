# Adyen C67 bounded API Explorer collection

Collection approved2026-11-05; collection completed. No ingestion or publication.

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
| c67-01 | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-05.md` |
| c67-02 | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-05.md` |
| c67-03 | DELETE /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-05.md` |
| c67-04 | POST /companies/{companyId}/webhooks | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/2026-11-05.md` |
| c67-05 | GET /companies/{companyId}/webhooks | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/webhooks/2026-11-05.md` |
| c67-06 | GET /companies/{companyId}/webhooks/{webhookId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/webhooks/(webhookId)/2026-11-05.md` |
| c67-07 | PATCH /companies/{companyId}/webhooks/{webhookId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/webhooks/(webhookId)/2026-11-05.md` |
| c67-08 | DELETE /companies/{companyId}/webhooks/{webhookId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/webhooks/(webhookId)/2026-11-05.md` |
| c67-09 | POST /companies/{companyId}/webhooks/{webhookId}/generateHmac | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/generateHmac/2026-11-05.md` |
| c67-10 | POST /companies/{companyId}/webhooks/{webhookId}/test | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/test/2026-11-05.md` |
| c67-11 | POST /merchants/{merchantId}/webhooks | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/2026-11-05.md` |
| c67-12 | GET /merchants/{merchantId}/webhooks | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/2026-11-05.md` |
| c67-13 | GET /merchants/{merchantId}/webhooks/{webhookId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05.md` |
| c67-14 | PATCH /merchants/{merchantId}/webhooks/{webhookId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05.md` |
| c67-15 | DELETE /merchants/{merchantId}/webhooks/{webhookId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05.md` |
| c67-16 | POST /merchants/{merchantId}/webhooks/{webhookId}/generateHmac | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/generateHmac/2026-11-05.md` |
| c67-17 | POST /merchants/{merchantId}/webhooks/{webhookId}/test | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/test/2026-11-05.md` |
| c67-18 | POST /merchants/{merchantId}/paymentMethodSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/2026-11-05.md` |
| c67-19 | GET /merchants/{merchantId}/paymentMethodSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/2026-11-05.md` |
| c67-20 | GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/2026-11-05.md` |
| c67-21 | PATCH /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/2026-11-05.md` |
| c67-22 | POST /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/addApplePayDomains/2026-11-05.md` |
| c67-23 | GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/getApplePayDomains/2026-11-05.md` |
| c67-24 | POST /terminals/{terminalId}/reassign | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/reassign/2026-11-05.md` |
| c67-25 | GET /companies/{companyId}/terminalActions | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/2026-11-05.md` |
| c67-26 | GET /companies/{companyId}/terminalActions/{actionId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/(actionId)/2026-11-05.md` |
| c67-27 | GET /companies/{companyId}/terminalModels | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalModels/2026-11-05.md` |
| c67-28 | GET /companies/{companyId}/terminalProducts | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalProducts/2026-11-05.md` |
| c67-29 | GET /companies/{companyId}/billingEntities | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/billingEntities/2026-11-05.md` |
| c67-30 | GET /companies/{companyId}/shippingLocations | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/shippingLocations/2026-11-05.md` |
| c67-31 | POST /companies/{companyId}/shippingLocations | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/shippingLocations/2026-11-05.md` |
| c67-32 | POST /companies/{companyId}/terminalOrders | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/2026-11-05.md` |
| c67-33 | GET /companies/{companyId}/terminalOrders | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/2026-11-05.md` |
| c67-34 | GET /companies/{companyId}/terminalOrders/{orderId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/(orderId)/2026-11-05.md` |
| c67-35 | PATCH /companies/{companyId}/terminalOrders/{orderId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalOrders/(orderId)/2026-11-05.md` |
| c67-36 | POST /companies/{companyId}/terminalOrders/{orderId}/cancel | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/(orderId)/cancel/2026-11-05.md` |
| c67-37 | GET /merchants/{merchantId}/terminalModels | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalModels/2026-11-05.md` |
| c67-38 | GET /merchants/{merchantId}/terminalProducts | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalProducts/2026-11-05.md` |
| c67-39 | GET /merchants/{merchantId}/billingEntities | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/billingEntities/2026-11-05.md` |
| c67-40 | GET /merchants/{merchantId}/shippingLocations | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/shippingLocations/2026-11-05.md` |
| c67-41 | POST /merchants/{merchantId}/shippingLocations | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/shippingLocations/2026-11-05.md` |
| c67-42 | POST /merchants/{merchantId}/terminalOrders | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/2026-11-05.md` |
| c67-43 | GET /merchants/{merchantId}/terminalOrders | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/2026-11-05.md` |
| c67-44 | GET /merchants/{merchantId}/terminalOrders/{orderId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/(orderId)/2026-11-05.md` |
| c67-45 | PATCH /merchants/{merchantId}/terminalOrders/{orderId} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalOrders/(orderId)/2026-11-05.md` |
| c67-46 | POST /merchants/{merchantId}/terminalOrders/{orderId}/cancel | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/(orderId)/cancel/2026-11-05.md` |
| c67-47 | GET /companies/{companyId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalSettings/2026-11-05.md` |
| c67-48 | GET /companies/{companyId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalLogos/2026-11-05.md` |
| c67-49 | PATCH /companies/{companyId}/terminalSettings | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalSettings/2026-11-05.md` |
| c67-50 | PATCH /companies/{companyId}/terminalLogos | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalLogos/2026-11-05.md` |

Full evidence: page-results.json, summary.json and responses/. Separate exact ingestion approval required.
