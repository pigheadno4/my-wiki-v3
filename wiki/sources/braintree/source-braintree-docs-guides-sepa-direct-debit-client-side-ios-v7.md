---
title: "Braintree SEPA Direct Debit Client-Side Implementation (iOS v7)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/client-side/ios/v7-2026-09-16.md"
tags: [braintree, sepa, direct-debit, ios, client-sdk, tokenization]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is the iOS v7-routed client-side implementation guide for SEPA Direct Debit. It covers collecting the required bank-account and customer information, invoking the iOS SEPA flow to create and display a mandate and tokenize the payment method, and handing the resulting nonce to the merchant server.

The page limits the method to eligible merchants using a custom client-side integration, states an iOS v5.11+ SDK-family availability floor, excludes Drop-in, and directs qualifying merchants to request enablement for their Sandbox or Production account.

## Key takeaways

- The setup section names the `Braintree/SEPADirectDebit` CocoaPods module and the `BraintreeSEPADirectDebit` framework for Swift Package Manager or Carthage. It does not identify an exact package version.
- The required inputs are the account holder name and IBAN plus a billing address and the merchant-system customer ID; exact field names remain at the raw locator.
- The page constructs `BTSEPADirectDebitClient` and `BTSEPADirectDebitRequest`, then calls `tokenize(_:completion:)`. The page says this method launches the flow, creates and displays a mandate, and tokenizes the payment method.
- The Swift example uses `.oneOff` as its mandate type and sends the nonce to the server only in the successful client callback; the example does not establish a universal mandate type or a successful server-side payment outcome.

> [!warning] Scope boundary
> This is a captured iOS v7 documentation route whose availability notice separately names iOS v5.11+; it is not exact-package or current product-support evidence. Custom-client eligibility, Drop-in exclusion, account enablement, and Sandbox-versus-Production scope remain distinct, and client tokenization or nonce handoff does not establish mandate acceptance, server processing, debit success, settlement or funding.

## Detail locators

- Eligible-merchant, custom-client, platform/SDK-family, Drop-in and account-enablement conditions: `# Client-Side Implementation > AVAILABILITY`, raw lines 17-20.
- CocoaPods, Swift Package Manager and Carthage setup names: `## Set up your iOS Client > Get the SDK`, raw lines 25-45.
- Required bank-account and customer information: `### Collect information`, raw lines 46-54.
- Client/request construction and the mandate-display/tokenization action: `### Invoking the SEPA Direct Debit flow`, raw lines 57-59.
- Client authorization, request fields, `.oneOff` example, nonce callback and server handoff: Swift example at raw lines 60-101.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- SEPA lifecycle and mandate overview: [[source-braintree-docs-guides-sepa-direct-debit-overview]]
- Other platform routes: [[source-braintree-docs-guides-sepa-direct-debit-client-side-android-v5]] and [[source-braintree-docs-guides-sepa-direct-debit-client-side-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/client-side/ios/v7-2026-09-16|Braintree SEPA Direct Debit client-side implementation for iOS v7]] - complete collected page covering availability, SDK setup, required inputs, mandate display, tokenization and nonce handoff
