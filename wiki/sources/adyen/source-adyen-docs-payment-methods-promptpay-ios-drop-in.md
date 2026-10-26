---
title: "PromptPay iOS Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/promptpay/ios-drop-in/2026-09-15.md"
tags: [adyen, promptpay, ios, drop-in, qr, thailand]
---

## Overview

This [[adyen]] guide describes adding PromptPay to an existing **iOS Drop-in** integration. It offers Sessions and Advanced prerequisite tabs, TH/THB method discovery, a client-to-merchant-server payment handoff, and Drop-in QR presentation. The shopper pays with an app from a participating bank. The guide points to `/payments/details` for a frontend result and an asynchronous webhook for the payment outcome. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-promptpay|PromptPay overview]]. This dated page does not establish current account eligibility or a completed transaction.

## Key takeaways

- **Setup and discovery:** The page calls for an existing iOS Drop-in integration using either Sessions or Advanced server-side flow and asks the merchant to contact Adyen Support for Customer Area setup. For `/paymentMethods`, it specifies `countryCode: TH`, `amount.currency: THB` and an `amount.value`; Drop-in uses country and currency to decide what to show. The page gives no Checkout API or iOS SDK minimum. The Sessions and Advanced requirement links contain unresolved encoded template expressions, so follow the prose and verify the intended base guide. See raw lines 21–47.
- **Client and server roles:** After shopper selection, Drop-in calls `didSubmit` with `data.paymentMethod`. The app passes that data to the merchant server, which sends `/payments`. The v72 TEST curl example uses `paymentMethod.type: promptpay`, THB amount, reference and merchant account; other language snippets carry their own API-library versions and are not iOS SDK pins. Drop-in then generates the QR code for the shopper. See raw lines 49–279.
- **Result boundary:** The guide says to use a `/payments/details` `resultCode` for the frontend and to receive the payment outcome asynchronously by webhook. Its table is labeled “resultCode values” but actually has `eventCode` and `success` columns for `AUTHORISATION`: `false` means failure and `true` means the shopper completed the payment. A generated QR or shopper scan alone does not prove authorization. The page gives no full `/payments/details` request procedure. See raw lines 279–292.
- **TEST and live:** The guide says to test with real payment details and small amounts, inspect the test Payment list, and contact Support to add PromptPay in the live Customer Area before accepting live payments. These are instructions, not proof of a test result, zero financial movement, or live approval. See raw lines 294–300.

> [!warning] Templated links and outcome label
> The Sessions and Advanced integration-type URLs contain percent-encoded `{{getParameter(...)}}` placeholders rather than resolved platform/integration values. Both setup rows say “add in your Customer Area” without naming the method in that sentence, although the page is titled PromptPay. The result section's “resultCode values” heading should not be treated as a `/payments/details` enum: the table beneath it is a webhook `AUTHORISATION`/`success` table. See raw lines 25–37 and 281–292.

## Detail locators

- iOS Drop-in identity, flow tabs and templated prerequisites: raw lines 15–37; TH/THB discovery: raw lines 39–47.
- `didSubmit` handoff, server request and sample API-library versions: raw lines 49–277; Drop-in QR statement: raw line 279.
- Frontend result/webhook distinction and Support TEST/live guidance: raw lines 281–300.

## Related

- [[adyen-ios-sdk]] — separately versioned native Drop-in context; this page specifies no SDK release.
- [[source-adyen-docs-payment-methods-promptpay]] — QR-only method overview and channel routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/ios-drop-in/2026-09-15|PromptPay iOS Drop-in, 2026-09-15 snapshot]]
