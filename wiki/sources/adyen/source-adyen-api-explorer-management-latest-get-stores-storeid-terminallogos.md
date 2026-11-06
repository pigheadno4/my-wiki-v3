---
title: "Get a store terminal logo by model"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/stores/(storeId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/get/stores/(storeId)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-logo]
---

## Overview

This 2026-11-07 snapshot of the [[adyen]] Management API `latest` GET reference lists the v3 test server for reading the logo configured for a terminal model at a store. The caller supplies the store's unique `storeId` as a path parameter and a required terminal `model` query parameter. The API credential needs either Terminal settings read or Terminal settings read and write. Live requests are subject to rate limits.

## Key takeaways

- A successful `200` describes a logo response whose `data` field is **optional** and, when present, is a Base64-encoded image string that must be decoded to obtain the file.
- The store-model logo applies to terminals of that model under the store unless an individual terminal has a different configured logo. Reading this configuration does not establish that an individual terminal displays it or has processed a payment.
- This captured reference lists a test server at `https://management-test.adyen.com/v3`; the Live rate-limit notice is not a Live base URL or evidence of current account access.

## Detail locators

- Purpose, override scope, roles and Live rate-limit notice: raw lines 5–17.
- Server, required `storeId` and required `model` (including the captured model list): raw lines 19–33.
- `200` response and optional `data`: raw lines 35–43; illustrative response: lines 145–154.
- Error descriptions and schemas: `400` lines 46–63, `401` lines 66–83, `403` lines 86–103, `422` lines 106–123, `500` lines 126–143.

## Related

- [[adyen-terminal-management]] — terminal fleet configuration and API boundary.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/stores/(storeId)/terminalLogos/2026-11-07|GET store terminal logo reference (2026-11-07)]]
