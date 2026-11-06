---
title: "Adyen Management API v3: get company terminal settings"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalSettings/2026-11-05.md"
tags: [adyen, management-api, terminal-management, terminal-settings]
---

## Overview

This 2026-11-05-captured Management API reference describes `GET /companies/{companyId}/terminalSettings`, a read of settings configured for the company account. These settings apply to its terminals unless overridden at merchant, store or individual-terminal level. The listed server is `https://management-test.adyen.com/v3`. The calling credential needs **Management API—Terminal settings read** or **Management API—Terminal settings read and write**; the reference additionally requires **Management API—Terminal settings Advanced read and write** for sensitive terminal settings. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The required string path parameter `companyId` identifies the company account. This GET reference specifies no query parameters or request body. Live requests are subject to rate limits, with no numeric limit stated here.
- A `200` reports configured terminal-settings fields, all optional at the top level in the response table. Their categories include receipts, connectivity, DCC, gratuities, hardware, kiosk/localization, MOTO, Terminal API (`nexo`), offline processing, passcodes, pay-at-table, payments, refunds, standalone mode, store-and-forward, surcharge, Tap to Pay, instructions, timeouts and Wi-Fi profiles. Optional parents do not make every nested property required; within optional `surcharge.configurations` entries, `brand` and `currencies` are marked required, and within optional Wi-Fi `profiles` entries, `authType`, `bssType`, `ssid` and `wsec` are marked required.
- Important scope and safety qualifications in the response field descriptions: `connectivity.simcardStatus` is terminal-level only for cellular-capable models; DCC enablement carries receipt/terms responsibility; a first `payment.contactlessCurrency` change requires contacting Adyen for a compliance check; unreferenced refunds create liability for fraudulent or duplicate losses. The `storeAndForward` description says `maxAmount`, `maxPayments` and `supportedCardTypes` must be configured in a request or inherited from a higher level; that is not a requirement to include them in this GET response.
- Tipping has at most four predefined options, or three plus a custom-tip option. `hardware.resetTotalsHour` and `restartHour` default to 06:00 in the terminal's timezone with a 0–23 range. Other limits and units, including MOTO/offline amounts, receipt logo, encryption-key passphrase, Wi-Fi and kiosk constraints, remain in the raw response table.
- The reference lists `400`, `401`, `403`, `422` and `500` failures. This GET readback does not change settings, prove lower-level effective values or on-device application, establish payment readiness, or execute any example receipt/refund/offline transaction. Example passcodes, network credentials and URLs are illustrative values.

## Detail locators

- Raw opening paragraphs, `## Servers` and `## Parameters > ### Path parameters`: scope, roles, rate-limit notice, TEST host and company ID.
- Raw `## Responses > ### 200 Success`, lines 39–88: receipt, connectivity, DCC, gratuity, hardware, kiosk and `nexo` settings; terminal-only SIM status and encryption-key constraints.
- Same response table, lines 89–155: offline, passcodes, pay-at-table, currency/compliance, receipts, refunds, standalone and store-and-forward conditions.
- Same response table, lines 156–196: surcharge nested required fields, Tap to Pay, timeouts and Wi-Fi profile constraints.
- Raw error sections, lines 199–296: HTTP failure classes and problem fields.
- Raw `## Response examples > ### 200 Success`, lines 298–419: illustrative settings payload, not a universal default or effective device state.

## Related

- [[adyen-terminal-management]] — terminal configuration and lifecycle boundaries.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-configure-terminals-api]] — separate guide for inheritance, updates and timing.
- [[source-adyen-api-explorer-managementnotification-latest-post-terminalsettings-modified]] — separate modification notification.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalSettings/2026-11-05|GET company terminal settings, captured 2026-11-05]]