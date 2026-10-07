---
title: "Braintree PayPal Pay Later Offers for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/pay-later-offers/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/pay-later-offers/android/v5-2026-09-16.md"
tags: [braintree, paypal, pay-later, android, sdk-v5]
---

## Overview

This 2026-09-16 Braintree website snapshot is the Android v5-routed guide to presenting PayPal Pay Later offers from a PayPal checkout request. It describes country-dependent financing offers, says merchants are paid up front, and routes the Android client action through `PayPalCheckoutRequest`; it does not establish current offer availability, merchant or buyer eligibility, exact SDK-package support, or a completed payment.

## Key takeaways

- Set `shouldOfferPayLater = true` on `PayPalCheckoutRequest` to display Pay Later offers after PayPal login to eligible customers. This is a presentation request, not a guarantee that a particular offer appears or that a payment succeeds.
- Offer products, purchase ranges, term lengths, interest or APR treatment, and credit or regulatory qualifications vary by customer country. The page also says Pay Later is included with PayPal Checkout at no additional cost unless the merchant is in the US.
- Consumer and merchant eligibility are separate: consumers in the listed countries may be eligible across most integrations, while merchant eligibility depends on merchant location and integration. The guide directs merchants to the PayPal overview and their PayPal account manager or Braintree contact route for details.
- The captured prerequisite says to complete a PayPal client-side integration, but its link points to the JavaScript v3 route even though this page is routed as Android v5. Treat that mismatch as unresolved navigation, not evidence that JavaScript setup applies to this Android request.
- Additional Pay Later messaging was unavailable in this snapshot. The page says merchants should not create extra content, wording, marketing, or other material encouraging use, and warns that PayPal may act under the User Agreement.

## Detail locators

- Offer identity, merchant up-front payment, and the US cost exception: `# Pay Later Offers`, line 16.
- Country-specific products, transaction ranges, terms, APR or interest treatment, and regulatory or credit qualifications: country table, lines 18-28.
- Consumer-versus-merchant availability and the location/integration condition: `AVAILABILITY`, lines 30-32.
- Captured prerequisite and its JavaScript v3 destination: `## Before you get started`, lines 37-42.
- Android request flag and Kotlin example: `## Offer Pay Later`, lines 44-53.
- Additional-messaging prohibition and User Agreement warning: `IMPORTANT`, lines 55-57.

## Related

- Company: [[braintree]]
- Concept: [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/pay-later-offers/android/v5-2026-09-16|Braintree PayPal Pay Later Offers — Android v5 (2026-09-16)]]
