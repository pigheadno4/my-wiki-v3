---
title: "Braintree Amex Express Checkout Profile Retrieval (iOS v7 Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/client-side/ios/v7-2026-09-16.md"
tags: [braintree, amex-express-checkout, ios, legacy, profile-data]
---

## Overview

This captured Braintree website page is routed as an iOS v7 client-side guide for legacy Amex Express Checkout. Its substantive body documents the payload returned when profile data is requested for a specified nonce, including missing-profile handling and the fields in the returned Amex Express Checkout card profile. The page says Amex Express Checkout was replaced by Visa Secure Remote Commerce (SRC), but its SRC direction is qualified as limited release for eligible merchants, subject to API change, and access-requested. This dated snapshot is not evidence of current support, merchant or customer eligibility, certificate state, exact iOS SDK behavior, profile-data availability, or a successful payment. See [[braintree]] and [[braintree-payment-methods]].

## Key takeaways

- When no profile data is found for the specified nonce, the page shows a payload with a `Profile not found` message and status `404`. It says this appears in the payload argument rather than the `err` argument because the error comes from American Express rather than directly from Braintree.
- The described profile object contains one `amexExpressCheckoutCards` array item. The field inventory includes cardholder details, physical-card suffix and expiry, an Amex Express Checkout card ID, billing address and other profile attributes; use the raw locators for the exact field names and examples.
- Starred fields are available only to merchants approved by American Express for their specific implementation, and caret-marked fields may be unavailable for some customers. The Amex Express Checkout expiration date may differ from the physical card's expiration date.
- Although the URL is an iOS v7 route, the captured body provides no iOS API call or setup procedure and labels its only code example `JavaScript`. Do not infer native iOS implementation details, certificate requirements, current package behavior, or payment execution from this page.
- The availability notice directs prior Amex Express Checkout users to SRC and says SRC was introduced in Android v2, iOS v4 and JavaScript v3. Those statements are historical page wording, not proof of current SRC support or a safe migration path.

## Detail locators

- **Replacement and access qualifications:** raw lines 17–18 (`AVAILABILITY`) contain the Amex-to-SRC direction, limited-release and eligible-merchant scope, API-change warning, SDK-family introduction versions and access-request route.
- **Missing-profile payload:** raw lines 20–33 show the `Profile not found` payload and explain the payload-argument versus `err`-argument distinction.
- **Profile-card fields and qualifications:** raw lines 36–56 list `amexExpressCheckoutCards`, the one-item cardinality, card/profile fields, Amex approval condition and per-customer availability marker.
- **Billing-address fields:** raw lines 57–69 list the captured billing-address field names and examples.

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/client-side/ios/v7-2026-09-16|Braintree Amex Express Checkout client-side iOS v7 route (captured 2026-09-16)]]
