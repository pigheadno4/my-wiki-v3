---
title: "PromptPay iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/promptpay/ios-component/2026-09-15.md"
tags: [adyen, promptpay, ios, components, qr, thailand]
---

## Overview

This [[adyen]] page describes adding PromptPay to an existing iOS Components integration. It gives Sessions and Advanced prerequisite tabs, method discovery for TH/THB/iOS, a `PromptPayComponent` setup example, and a merchant-server `/payments` request that returns a QR action. A `Pending` response and the shopper's QR scan are not final authorization; the page points to a later webhook for the payment outcome. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-promptpay|PromptPay overview]]. The dated guide does not establish current merchant eligibility or completed payment execution.

## Key takeaways

- **Prerequisites and discovery:** The page calls for an existing iOS Components integration in either Sessions or Advanced flow and says to contact Adyen Support to add PromptPay in Customer Area. For `/paymentMethods`, it specifies `countryCode: TH`, `amount.currency: THB`, and `channel: iOS`; it then decodes the response and selects method type `promptpay`. This is discovery guidance, not proof a specific account will receive that method. The page does not state a Checkout API or iOS SDK minimum. See raw lines 21–55.
- **Client and server roles:** The iOS sample creates an `APIContext` with a client key and TEST environment, then initializes `PromptPayComponent` and sets its delegate and payment amount. When `didSubmit` supplies `data.paymentMethod`, the app passes it to the merchant server, which sends `/payments` with the method type. API key and merchant account appear in server-side examples, not as app configuration. The many API-library snippets are examples with their own stated versions; none pins the iOS SDK to that version. See raw lines 57–92 and 94–310.
- **QR and outcome:** The sample `/payments` response has `resultCode: Pending` and `action.type: qrCode`, with a QR image `url` and `qrCodeData`. The guide tells the integrator to render the QR using the action; the shopper scans it or uploads a screenshot to a bank app. For display after follow-up, it mentions a `/payments/details` `resultCode`; the asynchronous `AUTHORISATION` webhook is the stated outcome signal, with `success: false` for failure and `true` for successful completion. The guide does not supply a full `/payments/details` request procedure. See raw lines 312–353.
- **TEST and live setup:** It instructs testing with real payment details and small amounts, checking test payment status in Customer Area, and contacting Support to add PromptPay in the live Customer Area before live acceptance. These instructions do not prove a test succeeded, that no real funds could move, or that live access was granted. See raw lines 355–361.

> [!warning] UI and sample discrepancies
> The introduction says the Component collects the shopper's selected bank, but the later discovery, Component, `/payments` and QR sections show no bank-selection field or issuer value; do not invent one from the introductory sentence. The Swift sample embeds `<strong>THB</strong>` inside the `currencyCode` string and sets 1000 minor units while the server examples use 10000; it is not copy-ready. The prose says to pass `data.paymentMethod` to `paymentMethod.type`, while the sample server request simply uses `type: promptpay`; preserve the client/server boundary and verify the actual payload. See raw lines 19, 43–55, 74–92 and 96–110. The guide's QR-rendering step does not by itself prove how the native Component displays that action.

## Detail locators

- Sessions/Advanced requirements and Support setup: raw lines 21–37; TH/THB/iOS discovery and client-key/environment setup: raw lines 39–82.
- Server request and language-specific sample versions: raw lines 84–310; QR response/render and webhook outcome: raw lines 312–353.
- TEST and live gates: raw lines 355–361. The URL to iOS 5.0.0 environment docs in raw line 62 is a reference link, not an explicit SDK minimum.

## Related

- [[adyen-ios-sdk]] — independently versioned native iOS integration context.
- [[source-adyen-docs-payment-methods-promptpay]] — QR-only method overview and channel routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/ios-component/2026-09-15|PromptPay iOS Component, 2026-09-15 snapshot]]
