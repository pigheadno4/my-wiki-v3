---
title: "Adyen Management API: update store terminal settings"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, terminal-settings, point-of-sale]
---

## Overview

This captured Management API `PATCH /merchants/{merchantId}/stores/{reference}/terminalSettings` reference updates terminal settings for a store. The settings apply to its terminals except where an individual terminal has different values. It identifies the merchant account by `merchantId` and store by its `reference`; the listed server is the TEST `/v3` endpoint. This is configuration, not a payment request. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Include the full object containing a parameter to change it. An omitted object is not updated. To restore an inherited value from a higher level, include its full containing object and set that parameter empty or omit it. This is a store-level update subject to terminal-level overrides.
- The API credential needs `Management API—Terminal settings read and write`; sensitive settings additionally need `Management API—Terminal settings Advanced read and write`. Live requests are subject to rate limits.
- The request body table marks top-level settings objects optional. Nested `Yes` fields are required within their relevant objects, such as surcharge configuration `brand` and `currencies`, and Wi-Fi profile `authType`, `bssType`, `ssid`, and `wsec`. The store-and-forward `maxAmount`, `maxPayments`, and `supportedCardTypes` must be configured in the request or inherited from a higher level.
- Important operational cautions in the schema: contact Adyen before first changing `payment.contactlessCurrency` for a compliance check; enabling DCC carries receipt and terms obligations; unreferenced refunds carry fraud and duplicate-loss liability. The SIM status setting can be updated and received only at supported terminal level, despite its presence in this shared schema.
- `200` returns a terminal-settings body with optional fields; `204` succeeds without additional content. Neither response alone proves the configuration is effective on a particular device, that a transaction succeeded, or current live eligibility. The captured page lists 400, 401, 403, 422, and 500 errors.

## Detail locators

- Raw lines 5–34: purpose, inheritance/change semantics, roles, live rate-limit note, TEST server, and path parameters.
- Raw lines 37–197: request body fields, conditional requirements, defaults, limits, units, and cautions; lines 199–286: Wi-Fi request examples.
- Raw lines 287–452: 200 response schema; lines 455–556: 204 and error responses; lines 558–786: illustrative 200 responses.

## Related

- [[adyen]]
- [[adyen-terminal-management]]
- [[adyen-pos-store-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalSettings/2026-11-07|Captured Management API PATCH store terminal settings reference]]
