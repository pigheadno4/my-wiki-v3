---
title: "Braintree Amex Express Checkout Client-Side Implementation (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/client-side/android/v5-2026-09-16.md"
tags: [braintree, amex-express-checkout, android, client-side, legacy, profile-data]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is routed as the Android v5 client-side implementation page for legacy Amex Express Checkout. Its retained body documents the response when profile data is not found for a specified nonce and the shape and qualifications of a returned Amex Express Checkout cardmember profile. The captured body does not document Android client setup, checkout-button or brand presentation, nonce creation or tokenization, or a server transaction action, so the route must not be used as evidence for those procedures or for successful payment processing.

The page says Amex Express Checkout was replaced by Visa Secure Remote Commerce (SRC) and directs prior users to integrate with SRC. It simultaneously qualifies SRC as a limited release for eligible merchants, says the API is subject to change, names Android v2, iOS v4 and JavaScript v3 as its introducing Client SDK generations, and directs readers to request access. This stored statement does not prove current Amex or SRC availability, merchant eligibility, account enablement, SDK behavior or a safe migration path; [[braintree-payment-methods]] preserves the separate unresolved SRC support-status conflict.

## Key takeaways

- When no profile data is found for the specified nonce, the page shows a payload with status `404`, message `Profile not found` and an empty `fieldErrors` array. It says this American Express-originated condition appears in the payload argument rather than the direct error argument. The rendered example is labeled JavaScript even though the URL and slug route the page as Android v5, so it is not evidence of an Android SDK call or callback contract.
- A returned profile has one `amexExpressCheckoutCards` array containing one Amex Express Checkout card item. The profile and billing-address fields, descriptions and examples belong in the raw tables rather than being reconstructed here.
- Fields marked with an asterisk are available only to merchants approved by American Express for the specific implementation, while caret-marked profile and billing-address fields may be unavailable for some customers. These qualifications do not prove approval or data availability for any merchant or customer.

> [!warning] Snapshot and lifecycle boundary
> A specified nonce is an input to the retained profile-result description, but this captured body does not show how the nonce is created, tokenized, sent to a server or used for a transaction. Neither the page route nor the profile payload proves a current account configuration, SDK capability, checkout, authorization, settlement or funding outcome.

## Detail locators

- Replacement-by-SRC direction, limited-release eligibility, API-change warning, named Client SDK generations and access-request route: `# Client-Side Implementation > AVAILABILITY`, raw lines 17-18.
- Missing-profile payload example and American Express-versus-Braintree error-channel explanation: raw lines 24-39.
- Single-item `amexExpressCheckoutCards` profile description and field table: `### Profile payload`, raw lines 44-68.
- Billing-address field table and customer-availability qualification: `### Billing address fields`, raw lines 71-83.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/client-side/android/v5-2026-09-16|Braintree Amex Express Checkout client-side implementation (Android v5)]] - complete collected snapshot for replacement and SRC availability qualifications, missing-profile response semantics, and profile-field availability conditions
