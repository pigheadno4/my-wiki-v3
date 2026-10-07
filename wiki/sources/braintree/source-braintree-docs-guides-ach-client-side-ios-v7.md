---
title: "Braintree ACH Client-Side Implementation (iOS v7 Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/ach/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/ach/client-side/ios/v7-2026-09-16.md"
tags: [braintree, ach, direct-debit, ios, javascript-v3, client-sdk, certificates]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is routed and titled as an iOS v7 client-side ACH Direct Debit page, but its substantive ACH statement limits availability to eligible merchants using the JavaScript v3 SDK. The captured body provides no iOS ACH setup or client action. See [[braintree-payment-methods]] for the provider-wide payment-method context and [[braintree-ios-sdk]] for separately versioned native iOS evidence.

## Key takeaways

- The route and page heading identify a client-side iOS v7 document, while the only ACH availability sentence points to JavaScript v3. Do not infer an iOS ACH integration flow from the route alone.
- The page carries a cross-mobile warning that Braintree Mobile iOS and Android SDK SSL certificates were set to expire on March 30, 2026. It directs merchants to iOS SDK 6.17.0+ and Android SDK 4.45.0+ or 5.0.0+, and says older published app versions must be decommissioned or force-upgraded by that date to avoid all customer traffic failing. The captured separator before `Android` is malformed as `&gt;Android`; consult the raw line rather than treating the formatting as an operator.
- The certificate notice is historical snapshot wording, not proof of the current certificate state, current SDK support, or the behavior of any exact package release.

## Material boundaries

- The captured body does not document iOS bank-account collection, tokenization, verification, nonce handoff, server processing, transaction creation, settlement or funding. Follow dedicated, applicable authorities before implementing an ACH flow.
- Merchant eligibility is asserted but not established for a particular account. This website snapshot is not account-enablement, runtime, successful-payment or current-support proof.
- The iOS v7 route is not exact-version GitHub implementation or release-history evidence, and the JavaScript v3 availability statement must not be generalized to a native iOS capability.

## Detail locators

- iOS v7 route identity: raw frontmatter `slug`, line 7; page heading, line 14.
- Eligible-merchant and JavaScript v3 availability statement: `**AVAILABILITY**`, raw lines 17-18.
- Cross-mobile certificate deadline, version directions, malformed `&gt;Android` separator and traffic-failure warning: `**IMPORTANT**`, raw lines 21-22.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[braintree-ios-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/ach/client-side/ios/v7-2026-09-16|Braintree ACH client-side iOS v7 route (captured 2026-09-16)]]
