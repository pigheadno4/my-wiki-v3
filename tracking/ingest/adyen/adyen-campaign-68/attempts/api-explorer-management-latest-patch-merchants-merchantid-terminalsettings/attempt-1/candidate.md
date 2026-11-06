---
title: "Adyen Management API: Update merchant terminal settings"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-settings]
---

## Overview

This 2026-11-07 capture of the Management API `latest` reference documents `PATCH /merchants/{merchantId}/terminalSettings` on the shown TEST v3 server (`https://management-test.adyen.com/v3`). It updates settings for the merchant account identified by required path `merchantId`. Settings apply to its terminals unless a store or terminal has a lower-level override. This is a configuration endpoint, not a [[adyen-terminal-api]] payment request. [[adyen]] · [[adyen-terminal-management]]

## Key takeaways

- To change a parameter, send its **full containing object**, including other parameters to retain. To restore an inherited higher-level value, send that full object with the parameter empty or omitted. Omitted objects are not updated. This is not a field-by-field patch.
- The API credential needs **Management API—Terminal settings read and write**; sensitive settings additionally need **Management API—Terminal settings Advanced read and write**. Live requests are subject to rate limits, without a numeric limit specified here.
- The request table marks top-level settings objects optional. Nested requirements apply when their containing structures are used: `surcharge.configurations[]` marks `brand` and `currencies` required; `wifiProfiles.profiles[]` marks `authType`, `bssType`, `ssid`, and `wsec` required. The `storeAndForward` prose requires `maxAmount`, `maxPayments`, and `supportedCardTypes` to be configured in the request or inherited from a higher level. `kioskAppOnStartup` must be in `allowedAppsInKioskMode`.
- Material feature cautions: enabling DCC carries receipt-requirement and terms responsibilities; contact Adyen before the first `payment.contactlessCurrency` update for a compliance check; enabling unreferenced refunds carries liability for fraudulent or duplicate refunds, with a recommended limit and delay. `connectivity.simcardStatus` can be updated or received only at terminal level on cellular-capable models, despite its appearance in this shared schema. The MOTO maximum-amount description points to `standalone.currencyCode` and cautions against enabling standalone outside a standalone solution.
- `200` says the request succeeded and describes a settings representation whose fields are optional; `204` has no additional content. Neither response establishes that a terminal has applied settings, accepted a payment, or settled funds. The captured reference lists `400`, `401`, `403`, `422`, and `500` errors. It states no idempotency, deletion, reversal, review, or activation contract for this PATCH.

## Detail locators

- Endpoint, inheritance, full-object/reset semantics, roles, live limit and server: raw lines 5–27.
- Path and request schema: raw lines 29–197. Defaults, units and bounds include `hardware.resetTotalsHour`/`restartHour` default 06:00 terminal time with 0–23 bounds (lines 54–57), gratuity options capped at four or three plus custom (49–53), and store-and-forward amounts in minor units (146–156). Wi-Fi profile types and conditional EAP fields are at 173–197.
- Illustrative PEAP/PSK and TLS request examples: raw lines 199–289. Response schemas, status and errors: lines 290–559. Illustrative `200` response examples: lines 561–752. Example values do not establish guaranteed returned fields or applied device state.

## Related

- [[adyen]] · [[adyen-terminal-management]] · [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalSettings/2026-11-07|2026-11-07 captured merchant terminal-settings PATCH reference]]
