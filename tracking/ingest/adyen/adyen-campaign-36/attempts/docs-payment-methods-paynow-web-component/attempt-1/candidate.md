---
title: "PayNow Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/web-component"
raw_files:
  - "adyen/docs/payment-methods/paynow/web-component/2026-09-15.md"
tags: [adyen, paynow, web-components, qr-code, singapore, online-payments]
---

## Overview

This 2026-09-15 guide adds PayNow to an existing Adyen Web Components integration. It has distinct Sessions and Advanced server-side flow instructions and describes QR-code handling and live enablement. It does not show an observed payment result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** requires an existing Sessions Web Components integration, Checkout API v68 or later, and PayNow added in Customer Area. The page says no PayNow-specific `/sessions` request parameters are needed. Import `PayNow` from `@adyen/adyen-web`, configure the Component, and initialize/mount the `PayNow` class. The Sessions configuration table marks `countdownTime` required and defines it as minutes after the QR code loads during which the shopper must complete payment; `5` is an example, not a stated default or universal expiry. (raw lines 25–87)
- **Advanced flow:** requires an existing Advanced Web Components integration, handling an additional `action.type: qrCode`, and PayNow added in Customer Area. It also imports and initializes `PayNow`; the page says no PayNow-specific `/payments` parameters are needed. The Sessions-only `countdownTime` table is not repeated in this Advanced section, so its applicability there is not established by this page. (raw lines 99–141)
- **Live and test boundary:** for either flow, the page says to contact Adyen Support to add PayNow in the *live* Customer Area before accepting live payments. It describes penny testing there with a real banking app and checking status in the live Customer Area. It recommends against testing PayNow payments in the test Customer Area because test-environment bank transfers cannot be reversed and funds will be deducted from the bank account. These are source statements about financial effects, not authorization to run a live or test payment. (raw lines 89–97, 143–151)
- **Outcome limit:** Component setup, QR-code display, scan, and status-check instructions do not establish that a particular bank transfer was authorized, captured or settled. This method-specific page gives no payment-success callback or webhook sequence. (raw lines 25–151)

## Detail locators

- Sessions prerequisites and no extra session parameters: raw lines 29–41.
- Sessions import, `countdownTime` and initialization: raw lines 43–87.
- Advanced `qrCode` action, import, initialization and no extra payment parameters: raw lines 99–141.
- Live enablement, status location and test bank-transfer warning: raw lines 89–97 and 143–151.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/web-component/2026-09-15|Adyen PayNow Web Component guide, 2026-09-15 snapshot]]
