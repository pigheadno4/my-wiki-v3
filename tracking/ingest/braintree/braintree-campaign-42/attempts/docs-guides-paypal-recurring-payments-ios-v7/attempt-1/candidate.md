---
title: "Braintree PayPal Recurring Payments for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/recurring-payments/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/recurring-payments/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios, recurring-payments, billing-agreements, vault]
---

## Overview

This collected [[braintree]] webpage is the iOS v7-routed guide to creating a PayPal recurring Billing Agreement through Braintree and later using its Payment Token for merchant-initiated payments. It describes the client request and the later Braintree server handoff; it is not a direct PayPal Orders or Vault API guide. Use [[paypal-braintree-integration]] for the provider boundary and [[braintree-ios-sdk]] for independently retained exact-version implementation evidence.

> [!warning] Snapshot, SDK and environment boundary
> This is a 2026-09-16 website snapshot at an iOS v7 URL, while its availability notice says client-side recurring payments are available for iOS v6+. The page does not name a sandbox or production environment, prove current SDK behavior or merchant eligibility, or demonstrate successful Billing Agreement creation or a later payment.

## Key takeaways

- The guide describes PayPal recurring payments as a two-stage Billing Without Purchase Checkout flow: the buyer first approves a Billing Agreement and the merchant stores the returned Payment Token against the customer; later merchant-initiated payments use that token. This is a Braintree PayPal flow, not proof of direct PayPal API behavior.
- At Billing Agreement creation, the recurring indicator is supplied through Braintree `plan_type`; for subsequent transactions, the page assigns the indicator to `transaction_source`. The exact Subscription, Recurring, Unscheduled and Installment mappings remain in the raw tables because first-versus-subsequent values are material and the captured rendering joins some field names and values.
- `plan_metadata` supplies buyer-facing recurring-plan information on PayPal's checkout review page. The page says to pass it during Billing Agreement creation, not during later merchant-initiated payment requests. Passing `plan_type` without metadata still triggers a generic recurring checkout, while passing neither produces non-recurring checkout UX and is not recommended for recurring transactions.
- Merchants must classify transactions as prepaid or postpaid and contact their Account Manager to enable PREPAID or POSTPAID as the recurring-billing default. The snapshot does not establish that this configuration is enabled for any merchant.
- The Swift section constructs `BTPayPalRecurringBillingDetails` and supplies it to `BTPayPalVaultRequest` with a recurring plan type. Its pricing, cycle and amount values are examples, not universal requirements.
- For collecting a payment and Billing Agreement consent in one checkout, the guide routes to Checkout with Vault and identifies `BTPayPalCheckoutRequest` with `requestBillingAgreement = true`. Its later-payment section separately routes through Vaulted Payments and Payment Method: Create before payment creation; those linked documents remain separate authorities.

## Detail locators

- Client-side availability notice and comparison with vaulted payments: raw lines 17-25.
- Recurring-payment categories and RBA type dimensions: raw lines 30-53.
- Two-stage Billing Agreement creation and later Payment Token use: raw lines 55-59.
- Recurring indicator purpose and the `plan_type` / `transaction_source` boundary: raw lines 62-85.
- Buyer-facing RBA Plan Information, creation-only `plan_metadata`, and the three metadata choices: raw lines 88-105.
- Optional plan name and warning against generic, SKU or internal-ID content: raw lines 110-140.
- Required prepaid/postpaid classification and Account Manager enablement: raw lines 143-145.
- Swift `BTPayPalVaultRequest` construction and example recurring-billing fields: raw lines 148-187.
- Checkout with Vault alternative and later-payment server-route navigation: raw lines 190-202.
- Subsequent-transaction RBA mappings: raw lines 200-209; consult the raw because the captured table contains joined tokens.

## Related raw API references

The following links are navigation preserved from the fully read page; their targets were not used as behavioral evidence for this entry.

- [Checkout with Vault for iOS v7](https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-vault/ios/v7/)
- [Vaulted Payments for JavaScript v3](https://developer.paypal.com/braintree/docs/guides/paypal/vault/javascript/v3/)
- [Payment Method: Create for Ruby](https://developer.paypal.com/braintree/docs/reference/request/payment-method/create/ruby)

## Related

- [[braintree]] - provider and collected-source catalog.
- [[paypal-braintree-integration]] - main Braintree-to-PayPal client, nonce/token and merchant-server boundary.
- [[braintree-ios-sdk]] - separately retained exact-SHA native SDK evidence; this website snapshot does not replace it.
- [[braintree-recurring-billing]] - separate Braintree subscription-plan product route, not ownership of this PayPal Billing Agreement flow.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/recurring-payments/ios/v7-2026-09-16|Braintree PayPal Recurring Payments for iOS v7 snapshot (2026-09-16)]]
