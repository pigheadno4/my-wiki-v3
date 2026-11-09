---
title: "Stripe — Collect Payment Details Before Creating an Intent (Deferred)"
type: source
date_ingested: 2026-11-09
canonical_url: "https://docs.stripe.com/payments/accept-a-payment-deferred"
original_format: webpage
raw_files:
  - "stripe-accept-payment-deferred-2026.md"
tags: [stripe, payment-element, deferred-intent, payment-intent, setup-intent, subscription, elements, dynamic-update]
---

## Summary

The 2026-05-11 retained guide describes rendering the Payment Element before creating an Intent, with separate web payment, setup, and subscription variants. The 2026-11-07 capture of the exact canonical URL is a variant index, not an implementation guide; its links do not reverify the old procedures or imply that an omitted detail was deprecated. Use the branch-specific dated evidence below, and verify the linked variant for current implementation details.

## Payment Mode Flow (2026-05-11 guide)

1. Initialize Elements with `mode: 'payment'`, `amount`, and `currency` so the Payment Element can display eligible methods.
2. Call `elements.submit()` to validate the form and collect wallet details before creating the Intent.
3. Create a PaymentIntent server-side using the matching amount, currency, and relevant customer identity; return its `client_secret`.
4. Call `stripe.confirmPayment({ elements, clientSecret, confirmParams: { return_url } })`; handle immediate errors and any redirect or further customer action.
5. Use the `payment_intent.succeeded` event for fulfillment rather than relying on a client callback, which can be lost or manipulated.

For changed prices such as a validated discount, update the displayed amount with `elements.update({ amount: newAmount })` and keep Elements options aligned with the Intent parameters. The old guide also covers optional CustomerSession saved-payment-method controls, layout options, and a ConfirmationToken alternative for a two-step checkout.

## Setup Mode Flow (2026-05-11 guide)

A setup flow collects a payment method for future use without an immediate charge. Initialize Elements with `mode: 'setup'` and `currency`; no amount is required. Attach the method to a Customer or customer-configured Account, create a SetupIntent server-side, and return its client secret. After `elements.submit()`, use `stripe.confirmSetup({ elements, clientSecret, confirmParams: { return_url } })`. A later off-session charge is a separate PaymentIntent using the saved method and customer identity; authentication can still be required or the attempt can fail.

## Subscription Mode Flow (2026-05-11 guide)

The retained guide also has a subscription branch. Initialize Elements with `mode: 'subscription'`, currency, and the amount charged immediately, which can be `0` for a trial. Configure invoice and Payment Element methods consistently. Create a Subscription server-side with a Price and a Customer or customer-configured Account; the example uses `payment_behavior: 'default_incomplete'`, saves the default method on the subscription, and expands both `latest_invoice.confirmation_secret` and `pending_setup_intent`.

For a subscription without an upfront payment, return `pending_setup_intent.client_secret` with type `setup`; otherwise return `latest_invoice.confirmation_secret.client_secret` with type `payment`. After `elements.submit()`, call `stripe.confirmSetup` or `stripe.confirmPayment` according to that returned type. Creating the Subscription or receiving a client secret does not itself establish a successful payment or provisioned access; the guide separately points to webhooks and subscription management.

## Identity and Integration Conditions (2026-05-11 guide)

The historical examples distinguish Customers v1 `customer` from Accounts v2 `customer_account`. The guide describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users, with a preview API version needed for preview participants; these are dated availability statements, not a current eligibility determination. Illustrative snippets, including malformed fragments, are not proof that an integration runs or that a charge succeeds.

The deferred path excludes BLIK and **pre-authorized debits using ACSS**; it does not state that all ACSS use is unavailable. With dynamic payment methods, client-side deferred-intent creation cannot use `customer_balance` because the PaymentIntent requires a Customer or customer-configured Account. For that method, the old guide calls for creating the PaymentIntent server-side with that identity and returning its `client_secret`. These are integration-path limits from the dated guide, not current method availability verified by the November index.

## Related Pages

- [[stripe-payment-intents]] — PaymentIntent concept and deferred pattern
- [[source-stripe-two-step-confirmation]] — ConfirmationToken variant

## Related raw API references

- [[stripe-payments-accept-a-payment-deferred-2026-11-07]] — 2026-11-07 navigation-only variant index for payment, setup, and subscription; not factual implementation provenance

## Raw Sources

- [[stripe-accept-payment-deferred-2026]] — retained 2026-05-11 deferred guide with payment, setup, and subscription branches (2490 lines)
