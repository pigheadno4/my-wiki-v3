---
title: "BLIK Android Drop-in earlier versions"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/blik/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, blik, android, drop-in, earlier-versions, redirect, online-payments]
---

## Overview

This 2026-09-15 snapshot is headed **BLIK Drop-in v4.x.x integration** and describes adding BLIK with code to an existing **Android Drop-in** flow. It hands the shopper to a redirect, receives return details, and calls `/payments/details` before displaying the result; an asynchronous webhook also reports the outcome. The historical v4 title and examples do not establish current SDK behavior or account eligibility. [[adyen]] [[adyen-android-sdk]] [[adyen-online-payments]]

## Key takeaways

- The requirements table says BLIK for Android needs Drop-in **v3.8.0 or later** and BLIK added in the **test** Customer Area. Its linked “Drop-in integration” URL nevertheless points to `platform=iOS` and `integration=Components` with an encoded target fragment. Use the named Android Drop-in scope and verify the appropriate base guide rather than treating that prerequisite URL as a resolved Android route. The page heading says v4.x.x, so the v3.8.0 minimum does not itself validate later-version behavior. See raw lines 15–26.
- To show BLIK, `/paymentMethods` uses `countryCode: PL`, `amount.currency: PLN` and a minor-unit amount. Android Drop-in returns `paymentComponentData.paymentMethod`, which the app passes to its server. The server's `/payments` prose asks for that payment method and a `returnURL` no longer than 1024 characters, obtained from `RedirectComponent.getReturnUrl(context)`. The code samples use `blik`/`blikCode` but omit the prose-listed `returnURL`; do not treat them as complete request templates. See raw lines 28–73 and 75–359.
- The illustrated `/payments` response is `RedirectShopper` with a `redirect` action for the client. The example action URL contains `redirectPayPal` despite `paymentMethodType: blik`, so it is not a reliable BLIK destination template. Redirecting or receiving this action does not prove payment success. See raw lines 361–387.
- After the shopper returns to the app, Drop-in supplies `actionComponentData`. The server posts `actionComponentData.details` to `/payments/details`; the response's `resultCode` and `pspReference` can inform the frontend. The page also says the outcome arrives asynchronously by webhook. Its result table treats `Pending` or `Received` as nonfinal, potentially lasting minutes or hours, with final outcome in an `AUTHORISATION` webhook. An `Authorised` row describes successful payment and claims funds in 2–3 days, but this snapshot is not evidence of settlement in any particular transaction. See raw lines 389–444.
- For TEST BLIK-with-code, the guide names code `999000`, BLIK guideline checks and end-to-end testing. Before accepting live BLIK, it says to add the method in the live Customer Area. It does not document a One Click tokenization flow on this page. See raw lines 446–456.

## Detail locators

- Historical v4 scope, requirements and mismatched prerequisite link: raw lines 15–26.
- PL/PLN discovery, Drop-in data handoff and server `/payments` request: raw lines 28–53.
- Payment-request language examples and missing `returnURL`: raw lines 54–359.
- Redirect action response and sample URL discrepancy: raw lines 361–387.
- Return/details call, result values, webhook and nonfinal outcomes: raw lines 389–444.
- TEST code and live Customer Area gate: raw lines 446–456.

## Related

- [[adyen-android-sdk]] — Android Drop-in architecture.
- [[adyen-online-payments]] — online payment and result-state context.
- [[source-adyen-docs-payment-methods-blik]] — BLIK method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/android-drop-in/earlier-versions/2026-09-15|BLIK Android Drop-in earlier versions, captured 2026-09-15]]
