---
title: "Braintree Credit Cards Standard Client-Side Implementation for iOS v7"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/credit-cards/client-side/ios/v7-2026-09-16.md"
tags: [braintree, credit-cards, ios, swift, card-fields, tokenization]
---

## Overview

This captured Braintree iOS v7 standard client-side guide describes adding the SwiftUI `CardFields` component to an iOS checkout so the client can collect and tokenize card number, expiration date and CVV input. The guide's completion path returns a payment-method nonce for the merchant app to send to its server; it does not make the client responsible for completing the transaction. This is a version-routed website snapshot for [[braintree]] and [[braintree-ios-sdk]], not evidence of current SDK support, merchant enablement, successful processing or parity with separately retained GitHub implementation evidence.

## Key takeaways

- Before using Card Fields, the guide requires the Braintree iOS SDK to be set up and a tokenization key or client token to be generated. The merchant supplies the surrounding checkout UI, including non-card fields and the pay button.
- `CardFields` is a SwiftUI component. A UIKit checkout can host it with `UIHostingController`; validity changes control the merchant-owned pay button and expose the submission closure.
- The completion closure receives either a nonce or an error. The nonce is an input to the merchant's server-side transaction flow, not proof that a transaction has been created or accepted.
- The guide directs merchants to test in sandbox before going live. Its placeholder authorization value, example form data and verification steps are examples from the captured page, not credentials, present availability guarantees or payment-execution evidence.

## Detail locators

- **Before you begin** — SDK setup, client authorization material and merchant-owned checkout elements.
- **Add your pay button** — disabled-button starting state and Swift example.
- **Initialize Card Fields and track form validity** — component initialization, validity callback, submit closure and authorization placeholder.
- **Host Card Fields in your view controller** — SwiftUI component hosting in UIKit.
- **Trigger submission from your pay button** — merchant-button submission call.
- **Handle the tokenization result** — nonce/error completion branches and server handoff.
- **Optional: Add supplemental card data** — `BTCard` example for non-card data merged into the tokenization request.
- **Test your integration** — sandbox-before-live direction and testing route.

## Related

- [[braintree-ios-sdk]] — native iOS SDK architecture and independently versioned implementation boundaries.
- [[braintree-payment-methods]] — provider-level payment-method and eligibility routing.
- [[source-braintree-client-sdk-setup-ios-v7]] — separate iOS v7 client-SDK setup snapshot.
- [[source-braintree-authorization-tokenization-key-ios-v7]] — separate iOS v7 tokenization-key authorization snapshot.
- [[source-braintree-payment-method-nonces]] — separate nonce-purpose and lifespan route.

## Related raw API references

The captured page links to advanced client-side tokenization, client authorization, server-side transaction creation and testing/go-live documentation. Those linked targets are navigation only here and were not used as behavioral evidence for this entry.

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/client-side/ios/v7-2026-09-16|Braintree Credit Cards Standard Client-Side Implementation — iOS v7 (captured 2026-09-16)]]
