---
title: "Adyen Management API: Get a terminal logo"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/terminals/(terminalId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/get/terminals/(terminalId)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-logos]
---

## Overview

This 2026-11-07 capture of the Management API `latest` `GET /terminals/{terminalId}/terminalLogos` reference lists the TEST `https://management-test.adyen.com/v3` server. It returns the logo configured for the payment terminal identified by required path parameter `terminalId`. If present, the image is Base64 encoded and must be decoded to obtain the file. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The API credential needs Management API—Terminal settings read or read and write. Live requests are subject to rate limits.
- A `200` means the request succeeded; response field `data` is optional. A returned encoded image is configuration readback, not evidence that the image has appeared on the terminal, that the device is ready, or that a payment has occurred.
- The captured reference specifies 400, 401, 403, 422 and 500 error responses. It does not document an update, reset, activation or payment transition for this GET.

## Detail locators

- Purpose, credential roles, Live rate limit, TEST server and required terminal ID: raw lines 5–26.
- `200` response and optional `data`: raw lines 28–36. Error schemas: raw lines 39–136. Illustrative Base64 response: raw lines 138–147.

## Related

- [[adyen-terminal-management]] — terminal fleet configuration and settings.
- [[adyen-payment-terminals]] — terminal devices and deployment context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/terminals/(terminalId)/terminalLogos/2026-11-07|Pinned terminal logo GET reference (2026-11-07)]]
