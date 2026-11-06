---
title: "Adyen Management API: get terminal settings"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/terminals/(terminalId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/terminals/(terminalId)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-management, terminal-settings]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `GET /terminals/{terminalId}/terminalSettings` on the v3 test server. It returns settings configured for the payment terminal identified by required path `terminalId`. It is a settings read, not a terminal action or payment operation. See [[adyen-terminal-management]].

## Key takeaways

- The API credential needs either `Management API—Terminal settings read` or `Management API—Terminal settings read and write`. Sensitive terminal settings additionally require `Management API—Terminal settings Advanced read and write`. Live requests are subject to rate limits.
- A `200` response says the request succeeded. The response table marks its top-level settings groups optional, including receipts, connectivity, payment, refunds, offline processing, hardware, and Wi-Fi. Nested required cells, such as surcharge configuration and Wi-Fi profile fields, do not make their optional parents mandatory.
- Material setting qualifications in the response schema include terminal-level, cellular-model-only SIM status; a contactless-currency change that requires contacting Adyen for a compliance check first; full merchant liability for losses from fraudulent or duplicate unreferenced refunds; and the store-and-forward trio of `maxAmount`, `maxPayments`, and `supportedCardTypes` that must be configured locally or inherited. These are configuration descriptions, not evidence that a particular terminal is online, has applied changes, or can process payments.

## Detail locators

- `## Parameters` → `### Path parameters`: required terminal ID; no query or request body is listed.
- `## Responses` → `200 Success` response table: optional groups and detailed field semantics, limits, defaults, and conditional notes. Inspect `connectivity`, `hardware`, `payment`, `refunds`, `storeAndForward`, `surcharge`, and `wifiProfiles` as relevant.
- `## Responses` → `400`, `401`, `403`, `422`, and `500` error tables.
- `## Response examples` → `200 Success`: illustrative settings only; it does not establish that all groups are always returned or describe live device state.

## Related

- [[adyen]]
- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/terminals/(terminalId)/terminalSettings/2026-11-07|Management API terminal settings GET, captured 2026-11-07]]
