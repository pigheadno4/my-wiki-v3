---
title: "Braintree PayPal Checkout with Vault - iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-vault/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/checkout-with-vault/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios-v7, checkout-with-vault, billing-agreements]
---

## Overview

This 2026-09-16 Braintree website snapshot documents PayPal Checkout with Vault for iOS v7. It describes a single checkout session that charges the customer while requesting Billing Agreement consent so the PayPal account can be vaulted for later merchant-initiated payments. It is Braintree-hosted guidance for the [[braintree]] iOS route, not direct PayPal API documentation.

The page is a version-family guide, not evidence for an exact `braintree-ios` package release, current merchant or buyer eligibility, account enablement, runtime behavior, or a completed payment or vault operation. See [[braintree-ios-sdk]] for the provider-owned native SDK route and separately retained exact-release boundaries.

## Key takeaways

- The guide distinguishes Checkout with Vault from Recurring Payments: its documented purpose is an immediate charge plus storage for future use, whereas the linked Recurring Payments flow uses Billing Without Purchase and performs no transaction at signup.
- The iOS request is a `BTPayPalCheckoutRequest` with `requestBillingAgreement` set to `true`; the parameter defaults to `false`, and the page says the customer is prompted to consent during checkout.
- `billingAgreementDescription` is optional. `recurringBillingDetails` and `recurringBillingPlanType` are also optional when checkout begins a recurring arrangement; their presence is request metadata, not proof that recurring charging is scheduled or enabled.
- The parameter table says `amountBreakdown` is optional but does not accept `discountTotal`, `handlingTotal`, `insuranceTotal`, or `shippingDiscount` when `recurringBillingDetails` is supplied. The displayed Swift values are examples, not guaranteed production results or universal field requirements.

## Detail locators

- Flow identity, immediate-charge-plus-vault purpose, and distinction from Billing Without Purchase: `### Overview`, raw lines 17-21.
- Required Checkout-with-Vault request switch and minimal Swift construction: `### Integration` and the first `### Swift` block, raw lines 24-35.
- Optional billing-agreement description and recurring-arrangement fields: paragraph before the second `### Swift` block, raw line 36; illustrative construction at raw lines 39-84.
- Parameter types, defaults, consent behavior, and the recurring-details `amountBreakdown` exclusion: `### Parameters`, raw lines 86-94.

## Related

- [[braintree-ios-sdk]] - native iOS SDK retrieval hub with PayPal, nonce-handoff and exact-release boundaries
- [[source-braintree-docs-guides-paypal-recurring-payments-ios-v7]] - separate iOS v7 Recurring Payments route referenced by this page
- [[source-braintree-docs-guides-paypal-checkout-with-paypal-ios-v7]] - separate iOS v7 one-time PayPal checkout route

## Raw Sources

- [[raw/braintree/docs/guides/paypal/checkout-with-vault/ios/v7-2026-09-16|Braintree PayPal Checkout with Vault - iOS v7]] - fully read 2026-09-16 website snapshot
