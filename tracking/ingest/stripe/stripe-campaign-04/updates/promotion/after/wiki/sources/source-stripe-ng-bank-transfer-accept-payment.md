---
title: "Stripe Docs — Accept a payment through local bank transfers in Nigeria"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment"
raw_files:
  - "stripe-ng-bank-transfer-accept-payment-2025.md"
tags: [stripe, nigeria, naira, bank-transfer, ng-bank-transfer, merchant-of-record, payment-intents, checkout]
---

## Summary

The May 8, 2026 guide covers Checkout and Direct API for Nigerian customers paying via local Naira bank transfer (`ng_bank_transfer`). Stripe directs the customer to its local merchant-of-record service provider's checkout to authenticate and authorize, then sends the customer back to the merchant site. This bank-transfer method is separate from Naira cards (`ng_card`) and the Nigerian partner is the merchant of record for this route. In the separate [[stripe-managed-payments|Stripe Managed Payments]] product Stripe is the merchant of record.

The November 7, 2026 acceptance capture links the Checkout and Direct API variants. Their detailed bodies are outside the capture, so the integration mechanics below are dated to May.

## May 8, 2026 Checkout

The Checkout compatibility section lists US business locations, NGN presentment and line-item prices, and 500–100,000,000 NGN per transaction. Payment mode is supported, with setup and subscription modes excluded. The guide offers dynamic Checkout method selection or manual configuration that lists `ng_bank_transfer` in the Session's historical `payment_method_types` parameter. The hosted example sets `success_url`. The full embedded example sets `ui_mode: embedded_page` and `return_url`. For testing, the guide says to select **Nigerian payment methods** in Checkout and click **Pay**.

## May 8, 2026 Direct API

1. Use a Stripe account and create a PaymentIntent on the server. The May instructions list the amount, `ngn` and `ng_bank_transfer` in `payment_method_types`. The Node.js creation example additionally shows `payment_method_data.type: 'ng_bank_transfer'`.
2. Pass the Intent's client secret to the browser. The May sample uses Dahlia Stripe.js initialized with a publishable key. The browser calls `stripe.confirmPayment` with the client secret, `payment_method_data.type: 'ng_bank_transfer'` and `return_url` to initiate the partner redirect.
3. The May browser snippet destructures `error` and branches on it, then tries to read `result.error.message` without a `result` binding in the shown code. The November index leaves the Direct API code and its error handling unverified.
4. The redirect back includes the `payment_intent` and `payment_intent_client_secret` query parameters. Use those identifiers to verify PaymentIntent status before displaying the outcome. The May test-key flow moves from `requires_action` to `succeeded` after test authentication, or to `requires_payment_method` after **Fail test payment**.
5. For order confirmation or shipping, act after verifying successful payment independently of the browser return. The May guide points to `payment_intent.succeeded` and the Dashboard, a webhook or a partner integration for handling completion.

## API version and country access

- **Endive request fields.** The separate [Checkout Sessions changelog](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions) and [PaymentIntents changelog](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents) identify `2026-09-30.endive` endpoints that reject writable `payment_method_types` on Checkout Session create and PaymentIntent create, update and confirm. The PaymentIntent changelog's Impact text separately names `2026-08-26.preview`; its REST table and endpoint links specify Endive. The changelogs point to dynamic methods with optional `allowed_payment_method_types` or `excluded_payment_method_types`. An allowed list filters incompatible methods and the computed `payment_method_types` remains readable on the response. These general endpoint rules leave the current Nigerian bank-transfer variants and account eligibility unverified.
- **Recurring and access.** The separate [[source-stripe-nigeria-payment-methods|Nigeria method overview]] said recurring bank transfer was “Coming soon” in May. The November matrix lists one-time Yes and recurring No, separately from the Naira card row. The November overview adds a preview invite request. A request, Dashboard setting or partner redirect leaves approval and live payment outcomes unverified.

## Related Pages

- [[stripe-nigeria-payment-methods]] — concept and dated country routes
- [[source-stripe-nigeria-payment-methods]] — country overview, scope and access, disputes, refunds and VAT
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-ng-bank-transfer-accept-payment-2025|May 8, 2026 full Naira bank transfer acceptance guide]] — verbatim webpage content, 294 lines. Checkout selection, compatibility and examples at lines 8–101. Direct API server setup at 103–151, browser setup and return at 220–272, test and completion outcomes at 274–294.

## Related raw API references

- [[raw/stripe-payments-ng-bank-transfer-accept-a-payment-2026-11-07|Naira bank transfer acceptance variant index]] — November 7, 2026 navigation to Checkout and Direct API (lines 7–12).
