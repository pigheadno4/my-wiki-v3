---
title: "Braintree PayPal Pay Later Offers for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/pay-later-offers/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/pay-later-offers/ios/v7-2026-09-16.md"
tags: [braintree, paypal, pay-later, ios, checkout]
---

## Overview

This collected [[braintree]] webpage is the iOS v7-routed guide to requesting PayPal Pay Later offers during Braintree PayPal checkout. It directs the merchant to construct `BTPayPalCheckoutRequest` with `offerPayLater: true`; the page says this displays Pay Later offers to eligible customers after they have logged into PayPal. Use [[paypal-braintree-integration]] for the Braintree-to-PayPal boundary and [[braintree-ios-sdk]] for separately retained exact-version implementation evidence.

> [!warning] Snapshot, eligibility and execution boundary
> This is a 2026-09-16 website snapshot at an iOS v7 URL. It does not establish current offer terms, current SDK behavior, merchant enablement, buyer or cart eligibility, approval, tokenization, authorization, capture, settlement or funding. Merchant eligibility differs by merchant location and integration, and the page conditions display on an eligible customer after PayPal login.

## Key takeaways

- The page characterizes Pay Later as country-dependent short-term interest-free payments, longer-term monthly installments and other financing options, with merchants paid up front. Its country table contains snapshot-specific offer names, amount ranges, schedules and legal or credit qualifications; use the raw locator rather than transferring one country's terms to another or treating them as current.
- To offer Pay Later in this iOS v7-routed checkout, the page sets `offerPayLater: true` when creating `BTPayPalCheckoutRequest`. This requests display of offers to eligible customers after PayPal login; it is not a promise that an offer will appear or that a payment will complete.
- The prerequisite bullet links to a PayPal client-side integration at a JavaScript v3 URL even though this page is routed as iOS v7. Preserve that link as captured navigation; do not treat it as an iOS setup procedure or infer cross-SDK equivalence.
- At snapshot time, the page says additional messaging is unavailable and prohibits merchant-created content, wording, marketing or other material intended to encourage use of Pay Later.

> [!warning] Messaging restriction
> Do not turn the checkout request into permission to create Pay Later promotional messaging. The page separately says additional messaging is unavailable at that time and warns against merchant-created promotional material.

## Detail locators

- Pay Later identity, merchant-up-front statement and customer-country offer table: `# Pay Later Offers`, raw lines 16-24.
- Consumer availability and merchant location/integration qualification: `AVAILABILITY`, raw lines 27-28.
- Support-article navigation and the captured JavaScript v3 client-side prerequisite link: `## Before you get started`, raw lines 31-35.
- `BTPayPalCheckoutRequest` construction, `offerPayLater: true` and eligible-customer-after-login condition: `## Offer Pay Later`, raw lines 38-47.
- Additional-messaging unavailability and merchant-created-material prohibition: `## Offer Pay Later > IMPORTANT`, raw lines 49-50.

## Related raw API references

The following links are navigation preserved from the fully read page; their targets were not used as behavioral evidence for this entry.

- [PayPal Pay Later offers support article](https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal-pay-later-offers)
- [PayPal client-side integration for JavaScript v3](https://developer.paypal.com/braintree/docs/guides/paypal/client-side/javascript/v3/)

## Related

- [[braintree]] - provider and collected-source catalog.
- [[paypal-braintree-integration]] - main Braintree-to-PayPal checkout and server-processing boundary.
- [[braintree-ios-sdk]] - separately retained exact-SHA native SDK evidence; this website snapshot does not replace it.
- [[paypal-pay-later]] - broader product concept; country terms and other integration surfaces remain separately qualified.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/pay-later-offers/ios/v7-2026-09-16|Braintree PayPal Pay Later Offers for iOS v7 snapshot (2026-09-16)]]
