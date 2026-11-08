---
title: "Stripe Subscriptions — Set Up Revolut Pay Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/revolut-pay"
raw_files:
  - "stripe-subscriptions-revolut-pay-2026.md"
tags: [stripe, billing, subscriptions, revolut-pay, setup-intents, payment-intents, checkout, mandate]
---

## Summary

The May 13, 2026 full guide documents three Revolut Pay subscription paths: SetupIntents API, direct Subscriptions API plus PaymentIntent confirmation, and a Stripe-hosted Checkout page. The November 7 capture at this canonical URL is only an index linking those three variants. Its linked variant pages were not read in this update, so the index does not verify their current parameters, states, or eligibility, and the missing detail does not establish deprecation. The 15 GBP monthly price in the May guide is an example, not a universal currency rule.

## May 2026: SetupIntents API path

The guide's server-side SetupIntent creation example sets `confirm=true`, `usage=off_session`, Revolut Pay payment-method fields, `mandate_data[customer_acceptance]` with online acceptance fields, and a `return_url`. It says to pass the returned `client_secret` to Stripe.js on the client to redirect the buyer to Revolut Pay and authorize the mandate. That passage does not explicitly report a `succeeded` SetupIntent status.

```bash
# Abbreviated May SetupIntent creation example
curl /v1/setup_intents \
  -d confirm=true \
  -d usage=off_session \
  -d "payment_method_data[type]=revolut_pay" \
  -d "payment_method_types[]=revolut_pay" \
  -d "mandate_data[customer_acceptance][type]=online" \
  --data-urlencode "return_url=..."
```

The May server-side subscription-create sample uses the SetupIntent response's PaymentMethod ID as `default_payment_method` and includes `off_session=true` on that subscription-create request. The guide says the Dashboard shows Active after successful payment. The sample's `off_session=true` belongs to this SetupIntents path; it is not a statement that every path explicitly passes the same field.

## May 2026: Direct Subscriptions API path

The guide creates a subscription with `payment_behavior=default_incomplete` and `payment_settings.save_default_payment_method=on_subscription`, expanding `latest_invoice.payments` and `latest_invoice.confirmation_secret`. It passes the confirmation secret to the frontend and obtains a PaymentIntent ID from invoice payments. Its server-side confirmation example uses `payment_method_data[type]=revolut_pay`, `mandate_data` fields including `accepted_at`, and `return_url`.

> [!warning] Contradiction
> In the May direct-confirm section, the prose says to set `payment_method_types` to Revolut Pay, but the shown cURL request instead sets `payment_method_data[type]=revolut_pay`. The provided capture does not validate a runnable request or resolve that discrepancy.

The guide says a `requires_action` PaymentIntent requires customer authentication. **After successful payment**, the subscription becomes active and saves the method as default. Authentication alone is not the stated activation condition.

## May 2026: Stripe-hosted Checkout path

The May server-side Checkout example creates a Session with `mode=subscription`, a recurring price, and `payment_method_types` containing card and Revolut Pay, then redirects the customer to the returned Session URL. The example does not explicitly include `mandate_data`, `return_url`, or `off_session=true`; their absence in this sample does not prove they are forbidden or describe defaults. The guide says the customer authorizes future use of the Revolut account through Checkout.

## Request and outcome boundaries

The May examples put `mandate_data` and `return_url` on the SetupIntent-create and direct PaymentIntent-confirm requests; they are not shown as universal fields for all three paths. The SetupIntent example's `usage=off_session` and SetupIntents-path subscription example's `off_session=true` remain request-specific. The May testing paragraph describes a **successful test case** in which a PaymentIntent moves from `requires_action` to `succeeded`; it does not report a SetupIntent status or prove a live initial or recurring payment. Neither capture proves an individual merchant's eligibility, completed mandate, charge, or settlement.

## Related pages

- [[stripe-revolut-pay]] — Revolut Pay concept
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-revolut-pay-2026-11-07|November 7 variant index]] — navigation only; links to SetupIntents API, Subscriptions API, and Stripe-hosted page variants, whose target contents were not read here

## Raw Sources

- [[raw/stripe-subscriptions-revolut-pay-2026|May 13 full guide]] — dated three-path examples and request prose
