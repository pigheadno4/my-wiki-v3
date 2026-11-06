---
title: "Adyen Management API v3: get a merchant webhook configuration"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/(webhookId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05.md"
tags: [adyen, management-api, webhooks, configuration]
---

## Overview

This 2026-11-05-captured Management API reference documents `GET /merchants/{merchantId}/webhooks/{webhookId}`, which reads the path-identified webhook configuration for a merchant account. The caller's API credential needs either `Management API—Webhooks read` or `Management API—Webhooks read and write`. The only listed server is TEST `https://management-test.adyen.com/v3`; this capture does not establish a Live endpoint or current account access. A configuration readback does not prove webhook delivery, event receipt, payment authorization, or settlement. [[adyen]] [[adyen-webhooks]]

> [!warning] Contradiction
> The reference lists a TEST `/v3` server, but the 200 response example's `self`, `generateHmac`, `merchant`, and `testWebhook` links all use `/v1`. The example does not resolve which action-link version should be used.

## Key takeaways

- Required string path parameters are `merchantId`, the merchant account ID, and `webhookId`, the webhook configuration ID. No query parameters or request body are listed (raw lines 18–24).
- HTTP 200 returns the configuration schema. Required response fields include `active`, `communicationFormat`, `type`, and public `url`; within optional `_links`, `generateHmac`, `self`, and `testWebhook` are marked required. The account-level `company` and `merchant` links are optional and qualified by webhook level (raw lines 28–44, 49, 55, 66–67).
- `active: true` is required to receive webhooks about account events, but its readback does not demonstrate successful delivery. Optional `hasError` flags configuration problems; optional `hmacKeyCheckValue` identifies the configured key by checksum, not its secret (raw lines 49, 60–63).
- The response schema describes certificate-acceptance flags defaulting to `false`; `encryptionProtocol` allows `HTTP` only in Test and otherwise defaults to `TLSv1.2` when unspecified. For company-level filtering, `filterMerchantAccounts` is required when `filterMerchantAccountType` is `includeAccounts` or `excludeAccounts`, but not for `allAccounts` (raw lines 45–47, 57–59). These are schema descriptions, not an assertion that every field appears in a given response.
- The reference also lists HTTP 204 with no additional content and 400, 401, 403, 422, and 500 errors. A 204 has no configuration readback (raw lines 71–172).

## Detail locators

- Purpose, role and TEST server: raw lines 5–16; path IDs: lines 18–24.
- Complete 200 response field schema, including additional settings, protocol, filters, types, URL and optional IDs: raw lines 28–68.
- 204 and error-body schemas: raw lines 71–172.
- Illustrative 200 response and v1 action links: raw lines 174–275. Example values do not establish defaults or Live behavior.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05|Management API GET merchant webhook configuration, captured 2026-11-05]]
