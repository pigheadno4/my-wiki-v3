---
title: "List company webhooks | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/webhooks"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/webhooks/2026-11-05.md"
tags: [adyen, management-api, webhooks, company-account]
---

## Overview

`GET /companies/{companyId}/webhooks` lists webhook configurations for the specified company account in the captured Management API reference. The captured server is `https://management-test.adyen.com/v3`; `companyId` is the required company-account identifier. The API credential needs either **Management API—Webhooks read** or **Management API—Webhooks read and write**. This read operation does not create, activate, test, deliver, or delete a webhook. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- Optional `pageSize` defaults to 10 and has maximum 100; optional `pageNumber` selects a page. The 200 body includes `itemsTotal`, `pagesTotal`, optional pagination `_links`, and optional `data` array of configurations.
- A listed configuration can identify its `id`, `type`, `url`, `communicationFormat`, `active`, `hasError`, account reference and account-scope links. The schema marks `active`, `type`, `url`, and `communicationFormat` required **within each configuration object**; `data` itself is optional. A company link is present only for company-level webhooks, and a merchant link only for merchant-level webhooks.
- `active: true` is required to receive account-related events, while `hasError: true` points to troubleshooting through the test endpoint. A returned configuration, active flag, or test link does not establish actual event delivery, payment outcome, account eligibility, or compliance.
- Company-level merchant inclusion depends on `filterMerchantAccountType`: `allAccounts` includes all merchant accounts without a list; `includeAccounts` or `excludeAccounts` requires `filterMerchantAccounts`. These are response-field descriptions, not request inputs for this GET operation.

> [!warning] Captured version mismatch
> The captured server list specifies Management API **v3 test**, but the illustrative 200 response uses `management-test.adyen.com/v1` links. Do not use those example links as proof that this operation's captured server is v1 or that a live endpoint was documented here.

## Detail locators

- Raw lines 5–30: purpose, credential roles, test server, required path identifier and pagination inputs.
- Raw lines 34–84: 200 response schema, including optional parent objects versus required nested fields, configuration identity, active/error flags, certificate/security settings, event filters, webhook type and endpoint URL.
- Raw lines 87–184: 400, 401, 403, 422 and 500 error responses; 401 means authentication required, 403 insufficient permissions, and 422 request validation error.
- Raw lines 186–304: one illustrative 200 response, including v1 example links and sample configuration values. Example values do not define defaults beyond the field descriptions.

## Related

- [[adyen-webhooks]] — webhook concepts and configuration context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/webhooks/2026-11-05|GET company webhooks, captured 2026-11-05]]