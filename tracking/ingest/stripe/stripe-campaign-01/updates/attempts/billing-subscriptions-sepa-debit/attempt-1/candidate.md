---
title: "Stripe Subscriptions — Set Up SEPA Direct Debit Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: https://docs.stripe.com/billing/subscriptions/sepa-debit
raw_files:
  - "stripe-subscriptions-sepa-debit-2026.md"
tags: [stripe, billing, subscriptions, sepa-debit, eur, europe, checkout, payment-element, delayed-notification]
---

## Summary

The May 13, 2026 guide documents two SEPA Direct Debit subscription examples: a hosted Checkout page and an advanced web integration. SEPA Direct Debit has delayed payment notification, so Checkout form completion alone is not a payment-success or fulfillment signal. Its two test tables each have **19 country headings** and eight scenarios per country. These are May test examples, not evidence of current account or bank eligibility.

The November 7, 2026 capture at the same unparameterized URL is only an index linking to a full hosted web variant and an advanced web/elements variant. It contains no current API, mandate, webhook, payment-state, or test-table instructions. Omission from this index does not establish removal of either May flow. The linked full variants were not captured in this job.

## Hosted Checkout example (May 2026)

The May example creates a Checkout Session with `payment_method_types: ['sepa_debit']`, at least one recurring Price, and `mode: 'subscription'`. It redirects the customer to the Session URL and supplies a `success_url`. The matched May guide labels this a full hosted page; it does **not** establish that Checkout is recommended over the advanced path.

```js
stripe.checkout.sessions.create({
  payment_method_types: ['sepa_debit'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

## Advanced integration example (May 2026)

The May advanced variant describes customer-configured Accounts v2 and Customers v1 branches. In that capture, Accounts v2 was generally available for Connect users and in public preview for other Stripe users, with preview-version qualification. Its server example creates a subscription using `payment_behavior: 'default_incomplete'`, `payment_settings.save_default_payment_method: 'on_subscription'`, and expands `latest_invoice.confirmation_secret` plus `pending_setup_intent`. It returns the invoice confirmation secret when payment is due up front, or the pending SetupIntent secret when no payment is collected up front.

The old page tells new users to follow a separate Payment Element subscription build guide, yet its own sample mounts a Payment Element and includes other Elements/IBAN code. It says the Payment Element displays the SEPA form and mandate acceptance and collects name, email, and IBAN. The confirmation instruction and sample select **`stripe.confirmSepaDebitPayment`** for an upfront payment or **`stripe.confirmSepaDebitSetup`** when no payment is collected up front. This mixed May example must not be collapsed into a single `stripe.confirmPayment` call or treated as a verified end-to-end execution.

## Delayed notification and paid invoices (May 2026)

Do not fulfill solely on `checkout.session.completed`: the May table describes it as customer authorization, with payment still pending. The table describes `checkout.session.async_payment_succeeded` as eventual success and `invoice.paid` as a successful customer payment; either can support fulfillment according to that guide. It describes `checkout.session.async_payment_failed` and `invoice.payment_failed` as failure paths requiring customer follow-up.

| Event | May guide's interpretation |
|---|---|
| `checkout.session.completed` | Debit authorized; wait for success or failure |
| `checkout.session.async_payment_succeeded` | Delayed payment succeeded; fulfill |
| `checkout.session.async_payment_failed` | Delayed payment failed; ask customer to retry |
| `invoice.paid` | Customer payment succeeded; fulfill and record paid period |
| `invoice.payment_failed` | Invoice payment failed; contact customer |

The May webhook example explicitly allows `invoice.paid` to arrive before `checkout.session.completed`, fulfills the purchase, and records that subscription period as paid. Thus `invoice.paid` is **not limited to renewals** in this guide. These are event-handling examples, not a guarantee that a specific debit settled or funds became available.

## Optional Checkout features (May 2026)

- Setup fee: one-time plus recurring `line_items`
- Inline pricing: `price_data` plus `product_data`
- Existing customer: `customer` or `customer_account` branches
- Trials: `subscription_data.trial_period_days`
- Fixed tax rates: `subscription_data.default_tax_rates`
- Dynamic tax rates: `line_items.dynamic_tax_rates` (not mixed with fixed rates in its example)
- Coupons: `discounts[{coupon}]`
- Customer-facing promotion codes: `allow_promotion_codes: true`

## Test IBANs (May 2026)

Each of the two May variant tables has **19 country headings**: AT, BE, HR, EE, FI, FR, DE, GI, IE, LI, LT, LU, NL, NO, PT, ES, SE, CH, GB. The tables do not contain SK or SI headings. They give eight test scenarios per country: success, delayed success, failure, delayed failure, dispute, weekly volume limit, weekly transaction limit, and insufficient funds. Token examples include `pm_success_de` and `pm_disputed_fr`. Read the full historical tables in the raw capture; test data is not a live availability guarantee.

The May advanced page also labels its optional `idealBank` path legacy and unavailable in the latest Stripe.js version as of that capture. One API Price example uses USD while nearby narrative examples use EUR, so example currency values must not be treated as a general SEPA eligibility rule.

## Related pages

- [[stripe-sepa-debit]] — concept page
- [[stripe-subscriptions]] — subscription concept page
- [[stripe]] — company page

## Related raw API references

- [[stripe-billing-subscriptions-sepa-debit-2026-11-07]] — November 7, 2026 unparameterized variant index only; linked variants not captured here

## Raw Sources

- [[stripe-subscriptions-sepa-debit-2026]] — May 13, 2026 full hosted and advanced variant capture
