---
title: "Adyen Management API: Get store terminal settings"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-settings, stores]
---

## Overview

This captured Management API `latest` reference documents `GET /merchants/{merchantId}/stores/{reference}/terminalSettings` on the listed TEST `https://management-test.adyen.com/v3` server. It reads settings configured for the store identified by merchant-account ID and store reference. Those settings apply to terminals under the store unless an individual terminal has different values. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Both `merchantId` and `reference` are required path parameters; the latter is the store reference. The API credential needs Terminal settings read or read and write. Reading sensitive settings additionally needs Terminal settings Advanced read and write.
- Live requests are subject to rate limits. A `200` means the read succeeded and may include the optional settings groups; `204` means successful processing with no additional content. Neither response proves that a physical terminal has applied a setting, can transact, or that a payment succeeded.
- Consequential field qualifications include DCC receipt obligations when enabled, the liability warning for unreferenced refunds, a prior Adyen compliance check before first changing contactless currency, and the requirement for store-and-forward `maxAmount`, `maxPayments`, and `supportedCardTypes` to be configured locally or inherited. These are settings descriptions in the response schema, not proof of current eligibility or payment behavior.

## Detail locators

- Endpoint purpose, roles, Live rate-limit notice, TEST server and required path IDs: raw lines 5–30.
- Optional response groups and nested fields, including receipt, connectivity, gratuities, offline, payment, refund, surcharge, store-and-forward, Wi-Fi and terminal instructions: raw lines 37–197. Nested `surcharge.configurations` entries mark `brand` and `currencies` required; Wi-Fi profile entries mark `authType`, `bssType`, `ssid`, and `wsec` required, while their parent response groups remain optional.
- `200`/`204` and 400, 401, 403, 422 and 500 response definitions: raw lines 32–35 and 200–301. The illustrative `200` response is at lines 303–398.

## Related

- [[adyen-terminal-management]] — terminal fleet configuration and scope.
- [[adyen-pos-store-management]] — store identity and administration.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalSettings/2026-11-07|Pinned Management API store terminal settings GET (2026-11-07)]]
