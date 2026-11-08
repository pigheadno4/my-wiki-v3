---
title: "Stripe Subscriptions — Set Up PayPal Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/paypal"
raw_files:
  - "stripe-subscriptions-paypal-2026.md"
tags: [stripe, billing, subscriptions, paypal, checkout, setup-intents, mandate, billing-agreement]
---

## Summary

Stripe's May 2026 PayPal subscription guide describes two paths: Stripe-hosted Checkout and a Direct API flow using a SetupIntent and PayPal billing agreement. The 2026-11-07 capture of the canonical URL is a 14-line variant index linking those two paths, with no operational instructions. It does not establish changed behavior, current availability, or current account eligibility.

## Important prerequisites (May 2026 guide)

- **Stripe-hosted Checkout:** Stripe said recurring payments were automatically enabled for most users when PayPal was activated, but regional restrictions or PayPal policy might require manual Dashboard enablement.
- **Direct API:** The guide instructed merchants to enable PayPal recurring payments in the Dashboard and check business-location eligibility. These are path-specific statements in the May capture, not a verified current account state.

## Path 1: Stripe-hosted Checkout (May 2026 guide)

Create a server-side Checkout Session with `payment_method_types: ['paypal']`, `mode: 'subscription'`, at least one recurring Price in `line_items`, and a `success_url`; redirect the buyer to the returned Session URL. The guide also permits one-time line items alongside recurring ones and says the buyer receives receipts from Stripe and PayPal.

```js
stripe.checkout.sessions.create({
  payment_method_types: ['paypal'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

A visit to `success_url` alone does not prove payment: someone can visit it without paying, and a buyer can close the tab before redirect. Use the Dashboard, webhooks, or another post-payment mechanism before fulfillment. The May guide illustrates a `checkout.session.completed` webhook.

The hosted variant also documents a one-time setup fee on the initial invoice, inline pricing, existing customers, email prefill, trials, fixed or dynamic tax rates, coupons, and promotion codes. See the historical raw for the specific parameters and conditions.

## Path 2: Direct API and SetupIntent (May 2026 guide)

1. Create or retrieve a customer-configured Account v2 or Customer v1 to represent the buyer; these are distinct Stripe object paths.
2. On the server, create a SetupIntent for that object with `payment_method_types: ['paypal']` and `payment_method_data.type: 'paypal'`.
3. On the client, use `stripe.confirmPayPalSetup(clientSecret, { return_url, mandate_data })`. The buyer is redirected to PayPal to approve a billing agreement, then back to the site.
4. Confirm authorization using `setup_intent.succeeded`; `setup_intent.setup_failed` indicates failed setup and `mandate.updated` can signal revocation. Setup authorization is separate from successful subscription payment.
5. The guide's main server-side subscription-create examples pass the customer object ID, the saved `default_payment_method`, a Price, and `off_session: true`. A successful initial payment is described as moving the Subscription to `active`; failed payments follow configured collection settings.

### `off_session` qualification

The May guide says to specify `off_session=true` when updating a subscription so a new payment does not require another PayPal redirect. Its main initial-create examples include `off_session: true`, but its optional billing-anchor and trial create examples omit both that field and `default_payment_method`. The 2026-11-07 index has no contract text to resolve this tension.

> [!warning] Contradiction
> The May guide's main Direct API create examples include `off_session: true`, while its optional create examples omit it. Treat the main examples and update instruction as dated guidance; do not infer an unconditional requirement for every create from this capture.

## PaymentMethod and Mandate identities (May 2026 guide)

After PayPal setup, the guide places the payer ID and Billing Agreement ID on the resulting Mandate under `payment_method_details`. It also places the buyer email and payer ID on `PaymentMethod.paypal`. Its following field table describes `payer_email`, `payer_id`, and `billing_agreement_id` without assigning all three to one object.

## Removing a saved PayPal payment method (May 2026 guide)

The guide says `paymentMethods.detach(id)` revokes the Stripe Mandate and calls the PayPal API to cancel the associated PayPal billing agreement. This is consequential historical behavior, not a verified action on a particular account.

## Optional Direct API examples (May 2026 guide)

The guide illustrates `billing_cycle_anchor` for a manual cycle and `trial_end` for a trial, including a combined trial and billing anchor. The optional snippets omit fields used in its main subscription-create examples, so they should not be treated as complete proof of requiredness or operational validity.

## Related pages

- [[stripe-paypal]] — Stripe PayPal integration concept
- [[stripe-subscriptions]] — Stripe subscriptions concept
- [[paypal-subscriptions]] — PayPal-native Subscriptions API, distinct from Stripe's PayPal integration
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-paypal-2026-11-07|2026-11-07 variant index]] — navigation only; links to [Stripe-hosted page](https://docs.stripe.com/billing/subscriptions/paypal.md?payments-ui-type=stripe-hosted) and [Direct API](https://docs.stripe.com/billing/subscriptions/paypal.md?payments-ui-type=direct-api); variant bodies were not captured here

## Raw Sources

- [[raw/stripe-subscriptions-paypal-2026|May 2026 PayPal subscription guide]] — historical Stripe-hosted and Direct API variant content (994 lines)
