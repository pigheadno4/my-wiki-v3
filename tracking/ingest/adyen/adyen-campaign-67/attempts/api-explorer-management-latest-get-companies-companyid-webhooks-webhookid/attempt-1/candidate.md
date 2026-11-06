---
title: "Get a company webhook | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/webhooks/(webhookId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/webhooks/(webhookId)/2026-11-05.md"
tags: [adyen, management-api, webhooks, company-accounts]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, describes `GET /companies/{companyId}/webhooks/{webhookId}`: read the configuration of one webhook identified by its company-account and webhook path IDs. The listed server is TEST `https://management-test.adyen.com/v3`. The calling API credential needs either `Management API—Webhooks read` or `Management API—Webhooks read and write`. See [[adyen-webhooks]] for the notification context and [[adyen-api-access]] for credential scope.

## Key takeaways

- Both path parameters are required strings: `companyId` identifies the company account; `webhookId` identifies the webhook configuration. The captured reference specifies no query parameters or request body. [Raw: lines 18–24]
- A `200` means the GET request succeeded and returns configuration. Required top-level response fields are `active`, `communicationFormat`, `type`, and `url`. The optional `_links` parent contains required `generateHmac`, `self`, and `testWebhook` children when present; `company` and `merchant` links are optional and scope-qualified. These links identify separate operations, not effects of this GET. [Raw: lines 28–44, 49, 55, 66–67]
- `active: true` is required by the field description to receive webhooks about account events, but readback alone does not prove actual delivery, HMAC generation, endpoint testing, authentication success, payment authorization, or any financial outcome. Optional `hasError` flags configuration trouble; `true` points to the separate testing endpoint. `hasPassword` and `hmacKeyCheckValue` describe protection/key identity without revealing delivery success. [Raw: lines 49, 60–63]
- Optional settings cover SSL certificate acceptance (each listed acceptance flag defaults to `false`), format (`soap`, `http`, `json`), `type`, destination URL, credentials, additional Standard-webhook fields, and company-level merchant filtering. `filterMerchantAccounts` is conditionally required for `includeAccounts` or `excludeAccounts`, and unnecessary for `allAccounts`; this is prose conditionality within the response table, not a required GET input. `HTTP` encryption protocol is Test-only; unspecified protocol defaults to TLSv1.2 according to the field description. [Raw: lines 45–68]
- The reference lists `400` request, `401` authentication, `403` permission, `422` validation, and `500` server errors, with problem-detail fields in each response schema. [Raw: lines 71–168]

> [!warning] Contradiction
> The listed TEST server is `/v3`, but the `200` example's `self`, `company`, `generateHmac`, and `testWebhook` URLs all use `/v1`. The example does not settle the current resource-link version or a Live route. [Raw: lines 15–16, 257–269]

## Detail locators

- Purpose, caller role, TEST server and required path IDs: pinned raw lines 5–24.
- `200` response fields and conditional/default descriptions: pinned raw lines 28–68.
- Failure categories and exact error-field requiredness: pinned raw lines 71–168.
- Illustrative `200` payload and conflicting `/v1` links: pinned raw lines 170–271. Example values do not establish defaults or account-specific settings.
- This read-only capture specifies no idempotency behavior, mutation, deletion/reversal, propagation timing, review, approval or activation transition. Its `latest` label and snapshot do not prove current availability, eligibility, compliance or financial results.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/webhooks/(webhookId)/2026-11-05|Management API webhook GET — captured 2026-11-05]]