---
title: "Adyen Scalapay API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/api-only"
raw_files:
  - "adyen/docs/payment-methods/scalapay/api-only/2026-09-15.md"
tags: [adyen, scalapay, api-only, redirect, capture, refunds]
---

## Overview

This [[adyen]] guide describes adding Scalapay to an existing Web API-only integration with a merchant-built payment form and server-side Checkout API calls. The captured page is marked last modified 2019-09-06 and fetched 2026-09-15. It covers FR, IT, PT and ES in EUR, a redirect and return flow, result handling, capture and multiple partial capture. The separate [[source-adyen-docs-payment-methods-scalapay]] overview identifies Scalapay as buy now, pay later and marks recurring and chargebacks unsupported in its snapshot table. A generic tokenization link in this guide's See also section does not establish Scalapay recurring capability.

## Key takeaways

- **Setup and commercial gate:** The guide requires an existing API-only integration and adding Scalapay in test Customer Area (raw lines 21–26). It says activation defaults to standard pricing and asks merchants to contact their account manager before activation to verify Enterprise-pricing eligibility (raw line 28). For `/paymentMethods`, it specifies country code IT, FR, PT or ES and EUR (raw lines 30–37). The test setup, pricing note and method listing do not prove account enablement.
- **Payment request:** The guide's `/payments` table marks `paymentMethod.type: scalapay_3x`, `countryCode`, `returnUrl` (maximum 1024 characters), `shopperEmail` and `shopperName` as required; billing/delivery addresses and `lineItems` are unmarked optional fields in this table. Flight and lodging dates are optional, with the instruction to provide **either** `additionalData.airline.flight_date` or `additionalData.lodging.checkInDate` in one transaction (raw lines 39–54). The curl and language snippets omit `shopperEmail` despite the table's required mark (raw lines 58–413); do not use those examples alone as a complete request recipe. Examples use TEST v72 and various library versions.
- **Redirect and outcome:** The server `/payments` response supplies an `action` of type redirect with the URL to use; after shopper return, the guide sends URL-decoded `redirectResult` in `/payments/details` (raw lines 415–484). The page recommends system browser or mobile browser handling for app redirects (raw lines 431–439). `/payments/details` can return Authorised, Cancelled, Error, Pending/Received or Refused. Pending/Received means final result is unknown and requires an `AUTHORISATION` webhook; if the shopper never returns, the page also directs use of that webhook for outcome (raw lines 486–505). A redirect return or Pending is not capture or settlement.
- **Capture and release:** Depending on settings, capture may be manual or automatic, delayed or immediate. Manual or delayed automatic capture must occur within **7 days** of authorization, after which authorization expires. The guide says to confirm successful capture **before shipping** and to cancel if no capture is intended, releasing authorized balance (raw lines 507–515). Multiple partial captures need Support enablement; after enablement, they can be made up to the authorized amount. Any authorized remainder that will not be captured needs an explicit cancellation request, or settlement can wait up to seven days for Scalapay to release it (raw lines 517–525).
- **Refund reference and live gate:** With multiple partial captures enabled, Scalapay refunds require `capturePspReference`; the guide warns to ensure the integration can send it to avoid failed refund requests (raw line 527). Test scenarios use Scalapay test cards and test Customer Area, while live acceptance requires a separate live Customer Area request (raw lines 529–535). Those instructions do not establish a successful payment, capture, refund or current merchant eligibility.

## Detail locators

- API-only prerequisite, activation pricing and method discovery: pinned raw lines 15–37.
- Payment request field table, field conditions and TEST examples: pinned raw lines 39–413.
- Redirect action, return and result statuses: pinned raw lines 415–505.
- Capture, cancellation, multiple partial captures and refund reference: pinned raw lines 507–527.
- Test/live setup: pinned raw lines 529–535.

## Related

- [[adyen-online-payments]] — broader online API and webhook context.
- [[source-adyen-docs-payment-methods-scalapay]] — product scope and snapshot feature matrix, including recurring and chargeback marks.

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/api-only/2026-09-15|Scalapay API-only guide, captured 2026-09-15]]
