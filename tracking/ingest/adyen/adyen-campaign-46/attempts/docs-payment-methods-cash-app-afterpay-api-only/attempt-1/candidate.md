---
title: "Cash App Afterpay API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/api-only"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/api-only/2026-09-15.md"
tags: [adyen, cash-app-afterpay, api-only, web, redirect, buy-now-pay-later]
---

## Overview

This 2026-09-15 capture of Adyen's Cash App Afterpay API-only guide describes adding the method to an existing API-only integration and building a custom checkout form. The core flow makes a server-side `/payments` request, redirects the shopper using the returned action, then checks `/payments/details` after return. It also covers result webhooks, capture/refund behavior, discounts, and test/live setup. It is a source snapshot, not proof of current merchant eligibility or a completed live transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Start with an existing API-only integration and add Cash App Afterpay in **test Customer Area** (raw lines 21–26). If using `/paymentMethods` for availability, the page specifies US `countryCode` and USD `amount.currency`; this is the US Cash App Afterpay route, and the example's `afterpaytouch_US` API type is part of that route (raw lines 28–35, 45–75).
- Collect full name, email, billing address, and delivery address for Cash App Afterpay risk checks (raw lines 39–43). The server-side `/payments` instruction includes `paymentMethod`, shopperName, shopperEmail, both addresses, and lineItems; it marks telephoneNumber optional. The example also includes shopperReference, countryCode, amount, reference, merchantAccount, and a website returnUrl; use the raw request at lines 45–123 for exact fields and sample values. Do not infer a universal schema requirement from a sample field alone.
- Check the `/payments` response `action`, then redirect to its `action.url`; the example has `resultCode: RedirectShopper` and `type: redirect`. After the shopper returns to the website, send the URL-decoded `redirectResult` in `/payments/details`; use its resultCode for shopper messaging and note the pspReference. The page's GET/browser advice at raw lines 534–542 is explicitly for app/mobile cases and is not a Web-only requirement (raw lines 518–573).
- A `Pending` or `Received` result is not final: it may take minutes or hours, and the guide says to wait for the AUTHORISATION webhook. If the shopper does not return, use webhook outcome; AUTHORISATION `false` means failure and `true` means successful completion according to the page. `Authorised`, `Cancelled`, and `Refused` have separate shopper actions (raw lines 575–593).
- Capture depends on merchant-account configuration: automatic after authorization or manual. Delayed capture needs a capture delay or manual capture; partial capture requires manual capture. Capture within **13 days** after authorization, or Cash App Afterpay cancels and refunds the first installment. Test authorizations expire in **one day**, so test manual capture must occur within that day (raw lines 595–603).
- For manual capture, amount.value specifies the full or partial amount and lineItems is optional. An unclaimed remainder after partial capture is automatically cancelled unless the account is enabled for multiple partial captures; Support must set up that capability, and each capture creates a new invoice. Cancel before capture; refund after capture, full or partial with optional lineItems (raw lines 605–625).
- The discount prose says “1 USD on Item #2,” while the example applies -100 minor units with quantity 2 and totals USD 8.00. That is arithmetically consistent with USD 1 **per unit** but ambiguous as a discount on the whole line. The sample also lacks a comma between the Item #2 and Discount objects, so it is not copy-ready JSON (raw lines 627–661).

## Detail locators

- Scope, setup, US/USD discovery and risk data: raw `## Requirements` lines 21–26 and `## Build your payment form for Cash App Afterpay` lines 28–43.
- Server request and response examples: raw `## Make a payment` lines 45–532; curl example lines 63–123, SDK variants lines 125–515, redirect-action response lines 518–532.
- Redirect, finality and shopper messaging: raw `## Handle the redirect` lines 534–573 and `## Present the payment result` lines 575–593.
- Capture, refunds and caveat: raw `## Capture the payment` lines 595–614, `## Refunds and cancellations` lines 616–625, and `## Discounts` lines 627–661.
- Test/live gate: raw `## Test and go live` lines 663–681 describes an Afterpay sandbox shopper account with US selected; accepting live Cash App Afterpay payments requires a request in live Customer Area.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-afterpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/api-only/2026-09-15|Cash App Afterpay API-only guide, captured 2026-09-15]]
