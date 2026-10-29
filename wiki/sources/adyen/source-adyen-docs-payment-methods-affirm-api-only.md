---
title: "Adyen Affirm API-only integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm/api-only"
raw_files:
  - "adyen/docs/payment-methods/affirm/api-only/2026-09-15.md"
tags: [adyen, affirm, bnpl, api-only, redirect, capture, refund]
---

## Overview

This 2026-09-15 Adyen guide adds Affirm to an existing API-only integration in which the merchant builds the payment form and makes server-side Checkout requests. It covers the `/payments` redirect, `/payments/details` result, later capture and refund/cancellation gates. It is documentation, not proof of current account enablement, shopper financing approval, authorisation, capture or live operation. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-affirm|the Affirm overview]].

## Key takeaways

- The prerequisite is an existing API-only integration and adding Affirm in the test Customer Area. The form section asks to collect first/last name, phone, email, billing and delivery addresses. From the server, send `/payments` with `paymentMethod.type=affirm` and the required shopper name, phone and email. `shopperReference` is optional with a three-character minimum if used. The `countryCode` requiredness cell is blank, but its prose requires it for Canada or the UK because omission defaults to US. `stateOrProvince` is required within Canadian/US addresses and optional for UK addresses; absent delivery address defaults to billing address.
- The introduction says to provide details of purchased items in the payment request, but the `/payments` table explicitly labels `lineItems` optional and recommends them to improve approval rates. Keep that prose/table tension visible; do not treat the introductory wording as a required-field declaration. The form section lists both addresses to collect, while the request table leaves their outer requiredness cells blank and specifies the delivery fallback.
- Inspect the `/payments` `action` for redirect information and send the shopper to its returned `action.url`; the shown `RedirectShopper` response is an example, not the only possible payment result. After the shopper returns to the website, POST `/payments/details` with the URL-decoded `redirectResult`; use its `resultCode` to present an outcome and retain `pspReference` as the transaction identifier. For mobile redirection, the guide recommends the device's default browser; its GET advice names SFSafariViewController/Chrome Custom Tabs in preference to WebViews. These are recommendations, not a claim that this API-only page is an iOS or Android SDK integration.
- `/payments/details` result guidance distinguishes `Authorised` (then capture after dispatch), `Cancelled`, `Refused`, and `Pending`. Pending is not final; wait for the AUTHORISATION webhook to learn the final result. The sample `Authorised` response does not prove any real transaction was authorised.
- Capture after goods are sent and within 28 days; capture starts the shopper's installment schedule, and the authorisation expires if the deadline is missed. For lesser fulfillment, this guide instructs capturing the authorised amount then refunding the difference. An uncaptured payment may be cancelled; after capture, returning funds requires a refund, with `amount` specified for a partial refund. The [[source-adyen-docs-payment-methods-affirm|Affirm overview]] instead marks partial and multiple-partial captures supported in its feature matrix; the precise applicability of that mark versus this guide's lesser-fulfillment instruction remains unresolved in these captures.
- The curl examples show test `/v68/payments` and `/v72/payments/details`; these are sample API versions, not stated global minimums. The Go example says library v10.4.0 while importing `/v9/` paths, so do not copy its version declaration and imports without checking the applicable library. Test credentials come from Affirm; live processing needs Affirm's live credentials after test review, a live Customer Area request, and provision of those credentials to Adyen.

## Detail locators

- Purpose, fulfillment dependency and prerequisites: pinned raw lines 15–31. Form fields: lines 33–46. `/payments` request table, including country/address/line-item qualifications: lines 48–62. Curl test v68 example: lines 64–126; SDK-language examples: lines 128–800. Go version/import mismatch: lines 481–490.
- `/payments` action and redirect example: pinned raw lines 802–816. Redirect recommendations, return and `/payments/details` request/response: lines 818–857; details curl uses v72 at line 835. Result presentation and Pending webhook gate: lines 859–870.
- Capture timing and lesser-amount refund instruction: pinned raw lines 872–876. Before/after capture cancellation/refund distinction and partial-refund amount: lines 878–886. Test/live credentials and Customer Area gate: lines 888–894. Cross-page partial-capture feature-matrix conflict: [[raw/adyen/docs/payment-methods/affirm/2026-09-15|Affirm overview raw]] lines 27–29 versus this guide line 876.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-affirm]] — method overview and financing/capability matrix

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/api-only/2026-09-15|Affirm API-only guide, captured 2026-09-15]]
