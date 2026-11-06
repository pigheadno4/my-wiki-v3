---
title: "Adyen Management API: Test a company webhook"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/test"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/test/2026-11-05.md"
tags: [adyen, management-api, webhooks, testing]
---

## Overview

The captured Management API company webhook test endpoint, `POST /companies/{companyId}/webhooks/{webhookId}/test`, sends sample notifications to check a configured webhook. The pinned reference lists only the TEST server `https://management-test.adyen.com/v3`. The API credential needs the Management API—Webhooks read and write role. `companyId` identifies the company account; `webhookId` identifies its webhook configuration. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The request body fields are optional at the top level. `merchantIds` can select at most 20 configured merchant accounts. Without it, Adyen says it sends samples to all configured merchant accounts, while also limiting sending to a maximum of 20; for a configuration above 20, specify a subset.
- `types` selects supported event codes by webhook type. Four test notifications are sent per chosen event code, covering success and failure in hard-coded EUR and GBP. For `CUSTOM`, `notification` is required and only the specified custom notification is sent. Its optional `amount` object has required `currency` and minor-unit integer `value` when supplied.
- A 200 response has optional `data` results, one per test webhook sent. Each result has required `status` (`success` for a 2xx response from your server, otherwise `failed`); optional merchant ID, sent body, response code, response time in milliseconds, and explanatory output aid troubleshooting.
- This tests notification delivery and the receiving server's HTTP response. A successful test does not establish a real authorization, capture, settlement, webhook delivery guarantee, or production setup. The response examples are sample data, not live payment evidence.

## Detail locators

- Purpose, sample limit and test semantics: raw lines 5–17.
- TEST server, path IDs, request fields, supported `types` by webhook type and conditional custom fields: raw lines 19–45.
- Request examples: raw lines 47–83. Response schema and success rule: raw lines 84–98. Client and server error schemas: raw lines 101–198. Response examples: raw lines 200–249.
- The pinned reference lists 400, 401, 403, 422 and 500 errors; it does not document an idempotency key, lifecycle change, asynchronous approval, activation, or financial outcome for this endpoint.

## Related

- [[adyen-webhooks]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/test/2026-11-05|Adyen Management API company webhook test, captured 2026-11-05]]
