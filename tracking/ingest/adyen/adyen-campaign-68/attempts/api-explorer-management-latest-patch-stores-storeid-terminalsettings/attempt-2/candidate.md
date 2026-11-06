---
title: "Adyen Management API: Update store terminal settings"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/stores/(storeId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/stores/(storeId)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, terminal-management, terminal-settings]
---

## Overview

This 2026-11-07-captured Management API `latest` reference lists a TEST `/v3` server for `PATCH /stores/{storeId}/terminalSettings`. It updates settings for the store identified by required path `storeId`; individual-terminal values can override store values. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Changing or resetting a parameter requires the **full containing object**. To restore a value inherited from a higher level, supply an empty value or omit that parameter within its containing object. Objects absent from the request are not updated.
- The caller's API credential requires **Management API—Terminal settings read and write**; sensitive settings additionally require **Management API—Terminal settings Advanced read and write**. Live requests have rate limits.
- Request-body setting groups are listed as optional in the table, with required nested fields where applicable. The shared `connectivity.simcardStatus` field is an endpoint-scope exception: it can be updated or received only at individual-terminal level, and only on models supporting cellular connectivity (raw lines 42 and 300). For store-and-forward, `maxAmount`, `maxPayments`, and `supportedCardTypes` must be configured in this request or inherited. In Wi-Fi profiles, `hiddenSsid` is table-optional but the prose says it is mandatory for Android terminals. The raw table also gives Wi-Fi profile field conditions and supported values.
- Enabling DCC carries receipt and terms-of-use responsibilities; unreferenced refunds carry fraud or duplicate-loss liability. Contact Adyen before the first `payment.contactlessCurrency` update so compliance requirements can be checked. Consult the raw fields for model, currency, image, amount, and default-hour limits.
- `200` reports request success and a settings representation with optional fields. It does not prove that a device has applied the configuration, that a payment occurred, or that Live eligibility or compliance has been established. The reference also lists `400`, `401`, `403`, `422`, and `500` errors.

> [!warning] Contradiction
> The Wi-Fi table describes `eapIntermediateCert` as for `eap: tls` (raw lines 186, 444), while the PEAP request and `200` response examples include that field (lines 217–220, 641–644). The examples do not settle the accepted condition.

## Detail locators

- Store scope, update/reset semantics, roles, Live notice and TEST server: raw lines 5–33.
- Request setting groups and constraints: raw lines 36–196; Wi-Fi request examples: lines 198–288.
- `200` response schema: raw lines 289–454; errors: lines 457–554; response examples: lines 556–787.

## Related

- [[adyen-terminal-management]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/stores/(storeId)/terminalSettings/2026-11-07|PATCH store terminal settings, captured 2026-11-07]]
