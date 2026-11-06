---
title: "Update one payment terminal's settings (Adyen Management API)"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-settings]
---

## Overview

This 2026-11-07 capture of Adyen Management API `latest` documents `PATCH /terminals/{terminalId}/terminalSettings` for settings on the uniquely identified payment terminal. The listed server is Test `/v3`; Live requests have rate limits. The API credential needs `Management API—Terminal settings read and write`, plus `Management API—Terminal settings Advanced read and write` for sensitive settings.

## Key takeaways

- `terminalId` is the required path parameter. The request-body table marks its top-level settings objects optional, but included objects follow explicit replacement/reset rules: include the full containing object to change a parameter; to restore inheritance from a higher level, include that full object and give the parameter an empty value or omit it. Objects absent from the request are not updated. The raw does not specify a request-wide idempotency key.
- The body spans receipts, connectivity, DCC, gratuities, hardware, kiosk mode, localization, MOTO, Terminal API (`nexo`), offline processing, passcodes, payment, refunds, standalone, store-and-forward, surcharge, Wi-Fi profiles and other terminal settings. Consult the raw for field types, nested requirements, values, limits and model constraints. In particular, `wifiProfiles.profiles` has required nested fields, and `hiddenSsid` is table-optional but described as mandatory for Android terminals. Store-and-forward `maxAmount`, `maxPayments` and `supportedCardTypes` must be configured in the request or inherited from a higher level.
- Material qualifications: enabling DCC carries receipt/terms compliance responsibility; Adyen says to contact it before the first contactless-currency update for a compliance check; unreferenced refunds create full liability for fraudulent or duplicate losses, with limit/delay recommended. `moto.maxAmount` needs `standalone.currencyCode`, but the text cautions against enabling standalone outside a standalone solution. Cellular `simcardStatus` is terminal-level and model-limited, and `ACTIVATED` does not by itself enable cellular networking on the device.
- A `200` response has a terminal-settings schema with optional fields. It records API success, not proof that the device has applied every setting, passed a compliance check, become payment-ready, or processed a payment. The reference lists `400`, `401`, `403`, `422` and `500` errors.

> [!warning] Contradiction
> The Wi-Fi field description says `eapIntermediateCert` is for EAP TLS, but the PEAP request and `200` response examples include it in a PEAP profile. The capture does not establish whether PEAP accepts that field; treat the examples as illustrative rather than a validation rule.

## Detail locators

- Raw lines 5–36: update/reset rules, credential roles, Live rate limits, Test server and terminal ID.
- Raw lines 36–196: request schema, nested required fields, defaults, units, limits and consequential conditions.
- Raw lines 198–288: PEAP/PSK and TLS request examples; compare `eapIntermediateCert` at lines 186 and 217.
- Raw lines 289–454: `200` response schema; lines 457–554: error responses.
- Raw lines 556–813: two illustrative `200` settings responses, including the PEAP field at line 644.

## Related

- [[adyen]]
- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalSettings/2026-11-07|PATCH terminal-specific settings, 2026-11-07 capture]]
