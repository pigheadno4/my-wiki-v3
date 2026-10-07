---
title: "Braintree PayPal Checkout with Vault (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-vault/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/checkout-with-vault/android/v5-2026-09-16.md"
tags: [braintree, paypal, checkout-with-vault, android-v5, billing-agreements]
---

## Overview

This collected Android v5-routed [[braintree]] website guide describes PayPal Checkout with Vault: one standard PayPal checkout that both collects an immediate payment and creates a Billing Agreement so the PayPal account can be used for future merchant-initiated payments. It distinguishes this combined flow from the separate Recurring Payments flow, whose Billing Without Purchase checkout has no transaction at signup.

This is a 2026-09-16 website snapshot for the Android v5 documentation family. It does not identify an exact SDK artifact version or establish current package support, merchant or buyer eligibility, account enablement, runtime behavior, successful Billing Agreement creation, payment execution, settlement, or funding.

## Key takeaways

- The documented enabling action is to construct `PayPalCheckoutRequest` with `shouldRequestBillingAgreement = true`; the parameter table says the default is `false` and that enabling it prompts the customer to consent to a Billing Agreement during checkout.
- `billingAgreementDescription` is optional and supplies a custom customer-facing Billing Agreement description. If the checkout begins a recurring arrangement, the page also permits optional `recurringBillingDetails` and `recurringBillingPlanType`; the example values are illustrative, not universal requirements.
- The parameter table notes that `discountTotal`, `handlingTotal`, `insuranceTotal`, and `shippingDiscount` are not accepted in `amountBreakdown` when `recurringBillingDetails` is passed. Keep the exact optional types, defaults, example construction, and restriction at the raw locators.

> [!warning] Request and outcome boundary
> The captured page documents request construction and the customer-consent purpose. It does not show the authorization return, tokenization, server transaction, storage/association step, or any later merchant-initiated charge. Do not infer those stages or a successful payment from `shouldRequestBillingAgreement = true`.

## Detail locators

- Combined immediate-payment and Billing Agreement purpose, future merchant-initiated use, and distinction from Billing Without Purchase Checkout: `### Overview`, raw lines 17-21.
- Enabling action: `### Integration`, raw lines 24-26.
- Minimal Kotlin request example: first `### Kotlin` block, raw lines 29-36.
- Optional Billing Agreement description and recurring-arrangement fields: paragraph and second `### Kotlin` block, raw lines 37-87.
- Parameter types, defaults, consent description, and the `amountBreakdown` exclusions when recurring details are supplied: `### Parameters`, raw lines 89-97.

## Related

- Company: [[braintree]]
- Main SDK concept: [[braintree-android-sdk]]
- Vault concept: [[paypal-vault]]

## Related raw API references

- [[raw/braintree/docs/guides/paypal/recurring-payments/android/v5-2026-09-16|Braintree PayPal Recurring Payments - Android v5]] - unread navigation-only route for the separate Billing Without Purchase flow; no sibling behavior is inferred here
- [[raw/braintree/docs/guides/paypal/checkout-with-paypal/android/v5-2026-09-16|Braintree PayPal One-time Payments - Android v5]] - unread navigation-only route for ordinary one-time checkout; no sibling behavior is inferred here

## Raw Sources

- [[raw/braintree/docs/guides/paypal/checkout-with-vault/android/v5-2026-09-16|Braintree PayPal Checkout with Vault - Android v5]] - fully read pinned website snapshot covering the combined checkout-and-Billing-Agreement purpose, Android request flag, optional recurring fields, and parameter restrictions
