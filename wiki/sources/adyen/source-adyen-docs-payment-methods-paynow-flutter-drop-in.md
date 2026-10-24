---
title: "Adyen PayNow Flutter Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paynow/flutter-drop-in/2026-09-15.md"
tags: [adyen, paynow, flutter, drop-in, qr-code, bank-payment]
---

## Overview

This [[adyen]] page gives **PayNow-specific additions** to an existing **Flutter Drop-in** integration under separate **Sessions** and **Advanced** server-side flows. It describes an **Advanced `qrCode` action** and unusually consequential **real-funds testing warnings**. It is not a complete QR lifecycle or result-handling guide; showing or scanning a QR code and checking a list does not prove payment authorization, bank transfer finality or merchant enablement. [[adyen-online-payments]]

## Key takeaways

- **Sessions base path:** The Sessions section requires an existing Flutter Drop-in Sessions integration, **Checkout API v68 or later**, and Support contact to add PayNow in Customer Area. Its integration-type hyperlink mistakenly points to an **Advanced** guide despite the Sessions heading and prose. It says no PayNow-specific extra /sessions parameters or configuration. It does not state an action type in this section. See raw lines 23–47.
- **Advanced base path:** The Advanced section requires an existing Flutter Drop-in Advanced integration and handling an additional **`action.type: qrCode`** action. Its action-handling link targets an anchor named “handle-the-redirect,” despite the QR action. Setup here says to add PayNow in Customer Area, while a separate live instruction still says to contact Support. The page says no extra PayNow configuration or parameters for the ordinary /payments request. No Advanced-flow API minimum is stated in prose. See raw lines 59–81 and 83–91.
- **Live setup and money movement:** Both sections say Support must add PayNow in **live Customer Area** before live acceptance. The page describes small-amount “penny” tests in **live** Customer Area using a **real banking app** to scan a test QR and points to live payment-list status. It expressly recommends **against** testing in **test Customer Area**: bank transfers in the test environment cannot be reversed and funds will be deducted from the bank account. This is a source warning, not an instruction to conduct a transfer. The text does not document a refund/reversal path or final status webhook. See raw lines 49–57 and 83–91.

## Detail locators

- Sessions requirements and no-extra-base-parameter statements: raw lines 23–47.
- Sessions live setup and real-funds warning: raw lines 49–57.
- Advanced qrCode, setup and base-request scope: raw lines 59–81.
- Repeated live setup and real-funds warning: raw lines 83–91.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/flutter-drop-in/2026-09-15|Adyen PayNow Flutter Drop-in snapshot]]
