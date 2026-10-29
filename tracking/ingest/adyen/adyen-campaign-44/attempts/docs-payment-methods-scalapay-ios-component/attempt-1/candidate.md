---
title: "Scalapay iOS Redirect Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/scalapay/ios-component/2026-09-15.md"
tags: [adyen, scalapay, ios, components, redirect, sessions]
---

## Overview

This [[adyen|Adyen]] guide, fetched and last-modified on 2026-09-15, adds Scalapay to an existing iOS Components integration using Sessions or Advanced server flow. It gives method-specific request fields and versioned Component creation examples. It does not itself describe capture, refund, redirect-return outcome or tokenization mechanics. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-scalapay|Scalapay overview]] for the captured EUR redirect and feature matrix; this page does not prove current merchant eligibility or successful payment execution.

## Key takeaways

- Both flow tabs require an existing Components integration and Scalapay added in Customer Area. The page says activation defaults to standard pricing and instructs merchants to contact an account manager before activation to verify Enterprise-pricing eligibility if volume may qualify. That instruction concerns pricing eligibility, not a guarantee of method enablement.
- The `/sessions` table, called the default with Components v5.0.0+, marks `countryCode` and `shopperName.firstName`/`lastName` required. It lists IT, FR, PT and ES as shopper country codes. Billing address, delivery address and `lineItems` are listed without required marks. The `/payments` table for an additional use case has the same core field markings, plus optional airline outbound flight date or lodging check-in date; its prose says to provide either field in the same transaction. Follow the verified table for format details.
- The Advanced `/payments` example is TEST Checkout API v72 with `paymentMethod.type: scalapay_3x`, IT/EUR, shopper name and a `returnUrl` placeholder. The library examples list their own versions. These are examples for the named product/country, not evidence of support for every Scalapay offer or a completed authorization.
- For iOS Components v5.0.0+, the guide looks up `.other("scalapay_3x")`, creates an `InstantPaymentComponent`, sets the Session or merchant delegate based on flow, and calls `initiatePayment()`. The v4.x.x path uses `ScalapayPaymentMethod` and `ScalapayComponent`. It says there are no additional Scalapay-specific Component configuration steps.
- The guide points to Scalapay test scenarios, test payment status in Customer Area and a live Customer Area request before accepting live payments. It does not establish live approval. Its requirement links contain an unresolved `{{getParameter('platform')}}` placeholder encoded in the URL; use the explicit iOS Components route in the page's See also section or the existing iOS integration rather than treating those template links as verified iOS URLs.

## Detail locators

- Existing-flow prerequisites and activation/pricing qualification: pinned raw lines 15–39. The platform placeholder appears in requirement links at lines 29 and 36.
- `/sessions` field table and Components v5 default: lines 41–55. Advanced `/payments` fields, optional airline/lodging data and IT `scalapay_3x` example: lines 57–96; language examples: lines 98–428.
- iOS v5+ Sessions/Advanced `InstantPaymentComponent`, v4 `ScalapayComponent`, and no extra configuration: lines 430–485.
- Test and live instructions plus explicit iOS integration route: lines 487–500.

## Related

- [[adyen-online-payments]] — main provider integration concept
- [[source-adyen-docs-payment-methods-scalapay]] — captured method/country/currency and feature matrix

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/ios-component/2026-09-15|Scalapay iOS Redirect Component guide, fetched 2026-09-15]]
