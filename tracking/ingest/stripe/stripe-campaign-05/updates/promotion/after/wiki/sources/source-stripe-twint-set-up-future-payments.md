---
title: "Stripe: Set Up Future TWINT Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/twint/set-up-future-payments"
raw_files:
  - "stripe-twint-set-up-future-payments-2025.md"
tags: [stripe, twint, switzerland, chf, recurring, setup-intents, save-payment-method]
---

## Summary

The May 3, 2026 guide shows how to save a TWINT payment method for later off-session use without charging upfront. It covers Checkout setup mode, Elements and Direct API. Saving as part of an active payment is documented separately in [[source-stripe-twint-save-during-payment]].

The May examples associate the method with a customer-configured Accounts v2 Account (`customer_account`) or Customers v1 Customer (`customer`). The guide describes Accounts v2 as generally available for Connect users and in public preview for others, with a preview API version required for enrolled users.

## May setup paths

- **Checkout.** Create a Checkout Session in `setup` mode for TWINT and the customer's ID. Direct the customer to the Session URL to authorize. Retrieve the SetupIntent from `checkout.session.completed` or retrieve the Session server-side with `setup_intent` expanded using the Session ID from the `success_url` template. The SetupIntent exposes the PaymentMethod ID. These are retrieval paths. Verify mandate authorization independently of browser return.
- **Elements.** Create a TWINT SetupIntent server-side for the customer and supply its client secret to the Payment Element. Use `stripe.confirmSetup` with `return_url` to send the customer to TWINT authorization and return them to the merchant.
- **Direct API.** Create a TWINT SetupIntent server-side for the customer. The recommended Stripe.js path uses `stripe.confirmTwintSetup` with the client secret and `return_url`. The optional merchant-server path confirms at creation with `confirm=true`, TWINT payment method data, a `return_url` and online mandate acceptance data including IP address and user agent. While the SetupIntent is in `requires_action`, redirect the customer to `next_action.redirect_to_url.url` to authorize at TWINT. Stripe then returns the customer to the supplied URL.

Across all three paths, confirm mandate authorization through SetupIntent state or events. May describes `setup_intent.succeeded` with status `succeeded` after authorization and instructs the merchant to store the PaymentMethod ID for reuse. Unsuccessful authorization emits `setup_intent.setup_failed` with status `requires_payment_method`. Browser return alone is insufficient.

## Charging later

For a later charge, create and confirm a separate CHF PaymentIntent with the customer identity and saved TWINT PaymentMethod. Set `off_session=true` when the customer is absent. The May guide waives `return_url` when reusing TWINT previously set up via a SetupIntent or a PaymentIntent with `setup_future_usage`. Setup status does not establish the later charge outcome.

## Testing

- The May test-key instructions distinguish approving versus declining the setup mandate on the redirect page.
- The Direct API test-key section sets `payment_method_data.billing_details.email` when confirming the SetupIntent to simulate a later saved charge. The `decline@` pattern produces `payment_method_provider_decline`, and the `revoke@` pattern produces `payment_intent_mandate_revoked`.
- The May simulation table labels the later failure `payment_intent.failed` (lines 1193–1198). The separate May save-during-payment capture uses `payment_intent.payment_failed` for failure to authorize during the initial payment (line 1135), while its own later-charge simulation table also uses `payment_intent.failed` (lines 1217–1222). The simulation spelling is dated documentation and does not establish a production webhook contract. SetupIntent mandate failure is a separate event.

## Detail locators

| Topic | May raw lines |
| --- | --- |
| Checkout setup and retrieval | 33–216 |
| Elements SetupIntent and confirmation | 324–400, 613–742 |
| Direct API confirmation and redirect | 845–928, 1021–1111 |
| Later charge and return URL exception | 250–288, 776–814, 1145–1183 |
| Direct API test fixtures | 1185–1198 |

## Related

- [[stripe-twint]] — TWINT concept and integration routes
- [[source-stripe-twint-save-during-payment]] — Separate active-payment save flow and May event terminology
- [[source-stripe-subscriptions-twint]] — Separate subscription integration guide
- [[stripe]] — Stripe company page

## Related raw API references

- [[raw/stripe-payments-twint-set-up-future-payments-2026-11-07|November 7, 2026 variant selector]] — Navigation for Checkout, Elements and Direct API.

## Raw Sources

- [[raw/stripe-twint-set-up-future-payments-2025|May 3, 2026 full setup guide]] — 1,198 lines covering the three setup paths.
