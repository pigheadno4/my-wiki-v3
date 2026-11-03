# Adyen C67 API Explorer collection-first preparation

Status: **AWAITING EXACT COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared 2026-11-03 after C66 publication `1d4dd3923c953aa0a25671cea9c06d38810e2cfd`.

C66 ingested all 50 pages: Legal Entity 8 and Management 42. Current totals: **3,059 sources = 2,547 General Docs + 496 API Explorer + 16 GitHub**. All locally collected complete-body API Explorer pages are ingested. The only 27 unreferenced local raw pages are excluded title-only stubs, retried in C63 and still title-only. No repeated stub retries proposed here.

## Pinned catalog reconciliation

The official API Explorer catalog captured 2026-11-02 contains **670 distinct normalized documentation URLs** (623 operation references and 47 overview references). Exact-URL reconciliation on 2026-11-03 finds 523 local raw URLs: 496 with ingested raw and 27 excluded title-only stubs. **147 catalog URLs have no local raw**. All 523 local URLs occur in the pinned catalog. [Complete reconciliation](catalog-reconciliation.json) retains its SHA256 and all missing URLs.

This is reconciliation against an immutable captured catalog, not a refreshed upstream inventory or a claim about present page availability. No network requests or semantic reads of the proposed pages were made. Titles and paths identify navigation scope only.

## Exact next collection proposal

Propose **50 exact official Markdown URLs**: the next 50 uncollected Management references in captured catalog order. Metadata scope covers the next Management references. All navigation labels are listed below for inspection. No behavior is inferred from these names. Every selected URL has a pinned catalog-line locator; the documented duplicated API Explorer prefix is collapsed, retaining official case and parenthesized parameters. Every raw directory and provisional source target is absent and all URLs/targets are unique. [Exact 50-target proposal](collection-proposal.json).

Approval authorizes documentation collection for these 50 URLs only. Stage each response, retain status/headers/body/hash and final URL, omit server-set cookies from published metadata, and classify substantive/failed/title-only results separately. Preserve substantive body bytes verbatim in new dated immutable raw snapshots. No whole-corpus refresh, code/rule/validator changes, General Docs, GitHub, stub retries, provider/account/security/device/payment operations, automatic ingestion or further publication. Endpoint action names describe documentation targets, not authorized API calls.

After all 50 selected URLs reach recorded outcomes, reconcile results and prepare an exact ingestion manifest only from recovered complete-body evidence: raw SHA256 pins, actual fixed query prompts, three distinct audit samples and explicit provider review authorization. Obtain separate ingestion approval per rules/psp-collection.md. Do not pad failed or incomplete results or waive body/schema presence. If all 50 collect successfully, 97 captured-catalog URLs would still lack raw; source counts rise only after approved ingestion.

C67 is **PREPARED ONLY / awaiting approval**. No runtime, dispatch, candidates, raw collection or canonical sources created. Publishing this proposal does not authorize execution.

| Item | Family | Catalog label | Exact Markdown URL |
| --- | --- | --- | --- |
| c67-01 | Management | POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins.md` |
| c67-02 | Management | GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId).md` |
| c67-03 | Management | DELETE /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId).md` |
| c67-04 | Management | POST /companies/{companyId}/webhooks | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/webhooks.md` |
| c67-05 | Management | GET /companies/{companyId}/webhooks | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/webhooks.md` |
| c67-06 | Management | GET /companies/{companyId}/webhooks/{webhookId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/webhooks/(webhookId).md` |
| c67-07 | Management | PATCH /companies/{companyId}/webhooks/{webhookId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/webhooks/(webhookId).md` |
| c67-08 | Management | DELETE /companies/{companyId}/webhooks/{webhookId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/webhooks/(webhookId).md` |
| c67-09 | Management | POST /companies/{companyId}/webhooks/{webhookId}/generateHmac | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/generateHmac.md` |
| c67-10 | Management | POST /companies/{companyId}/webhooks/{webhookId}/test | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/test.md` |
| c67-11 | Management | POST /merchants/{merchantId}/webhooks | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks.md` |
| c67-12 | Management | GET /merchants/{merchantId}/webhooks | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks.md` |
| c67-13 | Management | GET /merchants/{merchantId}/webhooks/{webhookId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/(webhookId).md` |
| c67-14 | Management | PATCH /merchants/{merchantId}/webhooks/{webhookId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/webhooks/(webhookId).md` |
| c67-15 | Management | DELETE /merchants/{merchantId}/webhooks/{webhookId} | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/webhooks/(webhookId).md` |
| c67-16 | Management | POST /merchants/{merchantId}/webhooks/{webhookId}/generateHmac | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/generateHmac.md` |
| c67-17 | Management | POST /merchants/{merchantId}/webhooks/{webhookId}/test | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/test.md` |
| c67-18 | Management | POST /merchants/{merchantId}/paymentMethodSettings | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings.md` |
| c67-19 | Management | GET /merchants/{merchantId}/paymentMethodSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings.md` |
| c67-20 | Management | GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId).md` |
| c67-21 | Management | PATCH /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId).md` |
| c67-22 | Management | POST /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/addApplePayDomains.md` |
| c67-23 | Management | GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/getApplePayDomains.md` |
| c67-24 | Management | POST /terminals/{terminalId}/reassign | `https://docs.adyen.com/api-explorer/Management/latest/post/terminals/(terminalId)/reassign.md` |
| c67-25 | Management | GET /companies/{companyId}/terminalActions | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalActions.md` |
| c67-26 | Management | GET /companies/{companyId}/terminalActions/{actionId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/(actionId).md` |
| c67-27 | Management | GET /companies/{companyId}/terminalModels | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalModels.md` |
| c67-28 | Management | GET /companies/{companyId}/terminalProducts | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalProducts.md` |
| c67-29 | Management | GET /companies/{companyId}/billingEntities | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/billingEntities.md` |
| c67-30 | Management | GET /companies/{companyId}/shippingLocations | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/shippingLocations.md` |
| c67-31 | Management | POST /companies/{companyId}/shippingLocations | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/shippingLocations.md` |
| c67-32 | Management | POST /companies/{companyId}/terminalOrders | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders.md` |
| c67-33 | Management | GET /companies/{companyId}/terminalOrders | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders.md` |
| c67-34 | Management | GET /companies/{companyId}/terminalOrders/{orderId} | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/(orderId).md` |
| c67-35 | Management | PATCH /companies/{companyId}/terminalOrders/{orderId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalOrders/(orderId).md` |
| c67-36 | Management | POST /companies/{companyId}/terminalOrders/{orderId}/cancel | `https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/(orderId)/cancel.md` |
| c67-37 | Management | GET /merchants/{merchantId}/terminalModels | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalModels.md` |
| c67-38 | Management | GET /merchants/{merchantId}/terminalProducts | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalProducts.md` |
| c67-39 | Management | GET /merchants/{merchantId}/billingEntities | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/billingEntities.md` |
| c67-40 | Management | GET /merchants/{merchantId}/shippingLocations | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/shippingLocations.md` |
| c67-41 | Management | POST /merchants/{merchantId}/shippingLocations | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/shippingLocations.md` |
| c67-42 | Management | POST /merchants/{merchantId}/terminalOrders | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders.md` |
| c67-43 | Management | GET /merchants/{merchantId}/terminalOrders | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders.md` |
| c67-44 | Management | GET /merchants/{merchantId}/terminalOrders/{orderId} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/(orderId).md` |
| c67-45 | Management | PATCH /merchants/{merchantId}/terminalOrders/{orderId} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalOrders/(orderId).md` |
| c67-46 | Management | POST /merchants/{merchantId}/terminalOrders/{orderId}/cancel | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/(orderId)/cancel.md` |
| c67-47 | Management | GET /companies/{companyId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalSettings.md` |
| c67-48 | Management | GET /companies/{companyId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalLogos.md` |
| c67-49 | Management | PATCH /companies/{companyId}/terminalSettings | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalSettings.md` |
| c67-50 | Management | PATCH /companies/{companyId}/terminalLogos | `https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalLogos.md` |
