---
title: "Adyen Swish API-only integration"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/api-only"
raw_files:
  - "adyen/docs/payment-methods/swish/api-only/2026-09-15.md"
tags: [adyen, swish, api-only, qr, redirect, online-payments]
---

## Overview

This 2026-09-15 guide adds Swish to an existing Adyen Web Advanced API-only integration. It covers SE/SEK payment-method discovery, a merchant-rendered QR for desktop or app-redirect button for mobile, return handling, and webhook-based payment outcome. It is a dated integration guide, not current merchant enablement or transaction proof. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and discovery:** The page requires an existing API-only integration, handling of an additional QR action, and Swish added in Customer Area. To obtain Swish from `/paymentMethods`, specify `countryCode: SE` and `amount.currency: SEK`. The example response has `paymentMethod.type: swish`; this discovery example alone does not establish merchant eligibility. (raw lines 23–29, 55–94)
- **Payment and shopper handoff:** The payment form need not collect extra shopper information for Swish. The specific `/payments` section says no additional method parameters, while the payment step supplies `paymentMethod.type: swish` and a `returnUrl`. The response describes `action.qrCodeData` for a merchant-rendered QR and `action.url` for a mobile app redirect. The shopper has three minutes after payment initiation to complete it; showing a timer is recommended. Desktop/laptop uses QR, mobile uses the redirect button, and tablet can use either or both. Screen-size detection is recommended rather than required. (raw lines 31–62, 96–157)
- **Result boundary:** QR completion is reported by webhook. After a mobile shopper returns, submit URL-decoded `redirectResult` in `/payments/details` and use the response to show a shopper-facing result. The guide says to wait for an `AUTHORISATION` webhook for the payment outcome: `success: false` means failure and `success: true` means successful completion. `Pending` or `Received` means the order was received, with a later final `AUTHORISATION` webhook. Neither the sample `/payments` `Pending` nor the sample details `Authorised` alone proves a real transaction in this snapshot. (raw lines 139–165, 167–225)
- **Testing and live:** The page says a TEST Swish payment is authorised within 15 seconds and provides Merchant Swish Simulator refusal scenarios using `shopperStatement` error codes. Accepting live Swish requires a separate request in the live Customer Area. These are documentation instructions; no test or live payment was performed for this ingestion. (raw lines 227–233)
- **Source conflicts and examples:** The 'How it works' list says the payment request includes additional item information, but the dedicated `/payments` section says no additional parameters. The requirements table names `action.type: qr`, whereas the sample response shows `action.type: qrCode`. The `/paymentMethods` curl example has `-X POST` without a following continuation marker. The listed order-fulfillment step appears before the later webhook-outcome instruction; follow the result section's explicit `AUTHORISATION` success/failure decision for fulfillment. Verify exact API behavior against the base flow before implementing these inconsistent examples. (raw lines 27–45, 67–81, 96–98, 139–157, 208–225)

## Detail locators

- Requirements, shopper flow and payment form: raw lines 23–53.
- SE/SEK discovery and its curl example: raw lines 55–94.
- Request and QR/mobile action, including three-minute completion window: raw lines 96–165.
- Mobile return `/payments/details`, webhook and result codes: raw lines 167–225.
- TEST simulator and live Customer Area request: raw lines 227–233.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/api-only/2026-09-15|Adyen Swish API-only guide, 2026-09-15 snapshot]]
