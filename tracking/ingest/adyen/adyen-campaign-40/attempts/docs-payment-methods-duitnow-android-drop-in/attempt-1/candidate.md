---
title: "DuitNow Android Drop-in integration"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/duitnow/android-drop-in/2026-09-15.md"
tags: [adyen, duitnow, android, drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen page explains method-specific additions for DuitNow in an **existing Android Drop-in** integration. It separates Sessions and Advanced server-side flows, but does not document an end-to-end payment or result sequence. Both branches point to adding DuitNow in Customer Area before integration; the live section separately requires Support to add DuitNow in the live Customer Area. [[adyen]] [[adyen-android-sdk]] [[adyen-online-payments]]

## Key takeaways

- The **Sessions** prerequisite is an existing Android Drop-in Sessions integration. Its `/sessions` request needs no additional DuitNow fields, and Drop-in needs no additional DuitNow configuration. See raw lines 21–30, 39–43 and 49–53.
- The **Advanced** prerequisite is an existing Android Drop-in Advanced integration. Its `/payments` request likewise needs no additional DuitNow fields, and Drop-in needs no additional DuitNow configuration. These are method-specific additions to the base flow, not an assertion that a full payment request has no fields. See raw lines 32–37, 45–47 and 55–57.
- Testing guidance calls for real payment details and small amounts, followed by a test Customer Area payment-list check. Before accepting live DuitNow, the page says to contact Support to add it in the **live** Customer Area. These instructions do not establish current availability, account enablement or an executed test/live result. See raw lines 59–65.
- The page does not state an Android SDK or Checkout API minimum, a DuitNow response/action shape, QR handling, webhook transition or settlement outcome. Its links to base Android Drop-in guides and general webhook/API references are navigation, not evidence of those DuitNow-specific behaviors. See raw lines 21–71.

## Detail locators

- Sessions and Advanced prerequisites and Customer Area setup: raw lines 21–37.
- Method-specific `/sessions` and `/payments` additions: raw lines 39–47.
- Method-specific Drop-in configuration: raw lines 49–57.
- Test and live setup instructions: raw lines 59–65.

## Related

- [[adyen-android-sdk]] — base Android Drop-in architecture.
- [[adyen-online-payments]] — online payment-method context.
- [[source-adyen-docs-payment-methods-duitnow]] — DuitNow method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/android-drop-in/2026-09-15|DuitNow Android Drop-in, captured 2026-09-15]]
