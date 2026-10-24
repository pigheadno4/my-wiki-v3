---
title: "PayNow iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/ios-component"
raw_files:
  - "adyen/docs/payment-methods/paynow/ios-component/2026-09-15.md"
tags: [adyen, paynow, ios, components, qr-code]
---

## Overview

Adyen's 2026-09-15 PayNow iOS Component page gives method-specific additions for existing iOS Components Sessions and Advanced flows. It initializes an `InstantPaymentComponent` for method type `paynow`; the Advanced branch explicitly handles a QR-code action. This page does not prove a bank transfer, payment authorization, or current account eligibility. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing iOS Components Sessions integration, Checkout API v68 or later, and PayNow added in Customer Area. No extra PayNow-specific `/sessions` parameters or Component configuration are specified. The Swift example checks that `.other("paynow")` exists in the session's methods before showing the Component, sets `session` as delegate, then initiates payment. [Raw lines 25–69]
- **Advanced:** Requires an existing iOS Components Advanced integration and handling the additional `action.type: qrCode`; PayNow must be added in Customer Area. No extra PayNow-specific configuration or ordinary `/payments` parameters are specified. The example uses `InstantPaymentComponent` with the calling object as delegate. Its **Advanced Components** prerequisite label links to a **Drop-in** URL; the separately linked action and payment steps point to Components. Preserve that source inconsistency rather than treating Drop-in as the required integration. [Raw lines 81–124]
- **Live and testing warning:** Before live acceptance, contact Adyen Support to add PayNow in the live Customer Area. The page describes small-amount “penny” testing in the **live** Customer Area using a real banking app to scan a test QR and checking status in the live payment list. It recommends against test Customer Area payment testing because test-environment bank transfers cannot be reversed and funds are deducted from the bank account. A scan or Component callback alone is no payment-status proof. [Raw lines 71–79, 126–134]

## Detail locators

- The Sessions and Advanced Swift examples differ in delegate assignment: `component.delegate = session` versus `component.delegate = self`; raw lines 57–69 and 107–118. These are flow-specific snippets, not a stated iOS SDK version requirement.
- The page itself gives no country/currency table, QR expiry period, recurring-token route, or final result-code/webhook semantics. Follow the relevant base integration and payment-status evidence for those behaviors.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/ios-component/2026-09-15|PayNow iOS Component (2026-09-15)]]
