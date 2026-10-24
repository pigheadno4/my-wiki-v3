---
title: "PayNow iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paynow/ios-drop-in/2026-09-15.md"
tags: [adyen, paynow, ios, drop-in, qr-code]
---

## Overview

Adyen's 2026-09-15 PayNow iOS Drop-in page lists method-specific additions to an existing iOS Drop-in integration for Sessions and Advanced server-side flows. It is a setup guide, not evidence that a shopper scanned a QR code, a bank transfer completed, or a merchant is currently eligible. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing iOS Drop-in Sessions integration using Checkout API v68 or later and PayNow added in Customer Area. The page says no extra PayNow-specific `/sessions` parameters or Drop-in configuration are needed. It does not give a PayNow-specific QR callback or final-state procedure for Sessions; follow the linked base guide. [Raw lines 25–46]
- **Advanced:** Requires an existing iOS Drop-in Advanced integration, handling its additional `action.type: qrCode`, and PayNow added in Customer Area. The page says no extra PayNow-specific configuration or ordinary `/payments` parameters are needed. It does not define QR expiry, request-success semantics, or a final webhook here. [Raw lines 60–82]
- **Live and test warning:** Before live acceptance, contact Adyen Support to add PayNow in the live Customer Area. The page describes small-amount “penny” testing in the **live** Customer Area with a real banking app scanning a test QR, with payment status checked in the live payment list. It recommends against testing payments in the test Customer Area because test-environment bank transfers cannot be reversed and funds are deducted from the bank account. These are financial-operation warnings, not evidence that any payment was performed. [Raw lines 48–58, 84–94]

## Detail locators

- No country/currency table, iOS Drop-in SDK version, QR expiry interval, recurring-token path, or capture/refund behavior is stated on this page. Use the linked base integration and payment-status sources before making claims about those steps.
- The Checkout API v68+ requirement is in the Sessions branch; the Advanced branch does not state that version gate here. [Raw lines 33, 68–70]

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/ios-drop-in/2026-09-15|PayNow iOS Drop-in (2026-09-15)]]
