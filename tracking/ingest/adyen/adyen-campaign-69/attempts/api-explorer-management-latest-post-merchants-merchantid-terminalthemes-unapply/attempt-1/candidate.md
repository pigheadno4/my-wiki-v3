---
title: "Adyen merchant terminal theme unapply"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/unapply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/unapply/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, terminal-management]
---

## Overview

Captured Management API v3 TEST `POST /merchants/{merchantId}/terminalThemes/unapply` reference for resetting a merchant account's terminal-theme assignment. Android terminals under the merchant then use a company-level custom theme, or Adyen's default if none is applied at company level. Store or individual-terminal custom themes continue to override that fallback. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- This unapply operation does not change or delete the theme itself. If no custom theme is applied at merchant level, the request still returns `200 OK` without error.
- The required path value `merchantId` identifies the merchant account. The API credential needs `Management API - Terminal themes read and write`. The captured server is `https://management-test.adyen.com/v3`; this page does not list a live server, request body, query parameters, default, limit or idempotency rule.
- `200 OK` confirms the request response, not when each Android terminal displays its effective theme. The success example contains `{"status":"success"}`, but no response-field schema is given. This configuration operation is not device-state, payment, compliance, or financial-outcome proof.
- Documented failures are 401 Unauthorized, 403 Forbidden, 404 Not Found, and 500 Internal Server Error. Example error bodies and codes are in the raw; the 403/404 example details distinguish access from account lookup only as illustrated.

## Detail locators

- Reset, fallback, lower-level overrides, no deletion, and no-op success: raw lines 5–11.
- Required role, TEST v3 server and merchant path ID: raw lines 13–25.
- Response statuses: raw lines 27–46; illustrative success and error bodies: raw lines 48–109.

## Related

- [[adyen-terminal-management]] — terminal administration and theme sources.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/unapply/2026-11-07|Merchant terminal theme unapply, captured 2026-11-07]]
