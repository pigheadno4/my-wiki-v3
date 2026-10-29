---
title: "PayBright Android Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paybright/android-drop-in/2026-09-15.md"
tags: [adyen, paybright, affirm, android, drop-in]
---

## Overview

This 2026-09-15 Adyen Docs guide describes PayBright in an **existing Advanced-flow Android Drop-in** integration. Drop-in renders the method, sends the shopper to PayBright and handles the app return. The opening says PayBright was acquired by Affirm and **Adyen will not accept new PayBright integrations**; later Customer Area/live-request instructions do not override that boundary. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- The guide assumes an Advanced-flow Android Drop-in integration and PayBright added in Customer Area. To display the method, `/paymentMethods` uses `countryCode: CA`, `amount.currency: CAD` and an amount value in minor units. This is this guide's method-display condition, not proof that a merchant is currently enabled. The Android client passes `paymentComponentData.paymentMethod` to the server.
- The server's `/payments` request uses the returned method plus shopper name, birth date, email, phone, country, billing/delivery addresses, purchased-item `lineItems` and a redirect `returnUrl` obtained using `RedirectComponent.getReturnUrl(context)`; `shopperLocale` is optional. PayBright uses shopper details for risk checks. The code examples use TEST endpoints and CA/CAD fixtures; the curl `/payments` sample is v68 and the later `/payments/details` sample is v72, without a stated general minimum API version.
- A `/payments` response can carry `resultCode: RedirectShopper` and an `action` of type `redirect`; the server passes that action to the Android client. On return, Drop-in supplies `actionComponentData.details`, which the server submits to `/payments/details`. Its result code can be `Authorised`, `Cancelled` or `Refused` for the shopper display. If the shopper does not return, use the `AUTHORISATION` webhook success flag to learn the outcome. `Authorised` is not capture or settlement evidence. The introduction says "website" in its redirect-result instruction, while the actual flow is Android app return.
- PayBright captures automatically by default after authorization and charges the shopper's first installment at capture. To capture after shipping or partially capture, configure delay or manual capture. Partial capture is unavailable when automatic capture is enabled in Customer Area. A single partial capture automatically cancels the unclaimed remainder; **multiple partial captures** require Support setup, keep that remainder available after the first capture and create a new invoice per capture. The `/capture` example includes `modificationAmount` and optional invoice-item data, but its currency fields are blank and must not be copied as valid request values.
- An uncaptured payment can be cancelled; a captured payment that must return funds is refunded. The partial-refund example uses `/payments/{paymentPspReference}/refunds` with `modificationAmount` and optional `openinvoicedata`; its currency fields are also blank. A request example does not prove modification success.
- The TEST section points to PayBright test details/status lookup and then says to submit a live Customer Area request. Read that under the explicit no-new-integrations notice; no current approval, exception or real-payment outcome follows from this page. Its `## See also` Android Drop-in link goes to a Sessions URL even though this guide's Requirements specify Advanced.

## Detail locators

- Acquisition/no-new-integrations notice, Android redirect and shopper/item overview: raw lines 19–27.
- Advanced-only prerequisite and Customer Area setup: `## Requirements`, lines 29–34.
- CA/CAD method display, client-to-server method transfer and `/payments` fields: `## Show PayBright in your payment form` and `## Make a payment`, lines 36–67. Versioned TEST request examples: lines 68–819.
- Returned redirect action, app return/details, shopper result codes and AUTHORISATION webhook fallback: lines 821–891.
- Automatic/delayed/partial capture, remainder cancellation and Support-gated multiple capture: `## Capture the payment`, lines 893–952. The partial capture sample has empty `modificationAmount.currency` and `openinvoicedata.*.currencyCode` values (lines 929–945).
- Cancel/refund split and partial-refund request: `## Refunds and cancellations`, lines 954–998. Its sample's currency values are blank at lines 984–991.
- Testing/live-request wording and inconsistent Sessions `See also` URL: lines 1000–1012; compare opening line 19 and Advanced requirement line 33.

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-payment-methods-paybright-web-component]] — separate Web Components guide; do not transfer Web-specific defaults to Android.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/android-drop-in/2026-09-15|2026-09-15 PayBright Android Drop-in guide and examples]]
