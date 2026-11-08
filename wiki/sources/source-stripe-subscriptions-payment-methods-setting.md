---
title: "Stripe Subscriptions — Set Payment Method Types Per Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: https://docs.stripe.com/billing/subscriptions/payment-methods-setting
raw_files:
  - "stripe-billing-subscriptions-payment-methods-setting-2026-11-07.md"
  - "stripe-subscriptions-payment-methods-setting-2026.md"
tags: [stripe, billing, subscriptions, payment-methods, payment-settings, payment-update-link]
---

## Summary

Stripe's November 7, 2026 guide explains that subscription `payment_settings.payment_method_types` limits the **types allowed** to pay subscription invoices; it does not select a single saved default payment method. The May 13, 2026 capture also documented subscription updates, payment-update links, and save-default controls. Details omitted from the November capture remain dated May evidence, not evidence of removal or current availability.

## Allowed types and collection method (November 2026)

- With `send_invoice`, customers choose among eligible types on the Hosted Invoice Page; some types support only this collection method.
- With `charge_automatically`, Stripe attempts collection without first presenting a payment-method selector. The configured types constrain the invoice PaymentIntent. An invoice payment or recovery flow later offers eligible types.
- Account activation, recurring-payment and product support, currency, amount, country, and collection method constrain eligibility. Ineligible types cannot pay the invoice or appear in customer-facing payment flows.

## Type selection and default method

By default, Stripe derives allowed types for a subscription-generated invoice from the account's Invoice default payment method configuration, attempts to include the **type** of the applicable saved default method, and filters by invoice eligibility. Explicit subscription `payment_settings.payment_method_types` takes precedence over the default invoice type configuration for that subscription and is passed to its SetupIntent and invoices.

**Pitfall:** If the subscription has an applicable default payment method, include that method's **type** in an explicit `payment_method_types` list. Otherwise, the default method cannot pay the subscription invoices. Type inclusion is distinct from selecting which saved method Stripe attempts. The May capture separately says a subscription `default_payment_method` or legacy `default_source` can prioritize an individual method; it also says the account's Invoice default type configuration takes precedence over the older customer `default_source` setting. These older method-priority statements are dated May evidence, not a three-step priority ladder for allowed types.

## Configure the subscription

The November Dashboard example creates a subscription that emails a manual invoice: Subscriptions → Create subscription → choose customer → Payment: **Email invoice the customer to pay manually** → Payment methods: **Manage** → select and save allowed types.

Its API example creates a subscription using an existing customer and recurring price, with `payment_settings[payment_method_types]` entries such as `card` and `link`. A restricted key needs `subscription_write` permission. This is a create example, not evidence that updating is unavailable or that a payment succeeded.

The May capture separately showed an update example:

```js
stripe.subscriptions.update(subId, {
  payment_settings: {
    payment_method_types: ['card', 'customer_balance']
  }
})
```

## Save a payment method as a default (May 2026 only)

The May guide said that either enabling **Save customer payment information** in Dashboard Invoice settings or setting Subscription `payment_settings.save_default_payment_method` can make a method used to pay an invoice “the new default.” That sentence did not identify the destination object for each control. The November payment-method-types guide does not discuss saving a paid method as default. Do not assume that both controls change the subscription's default from these captures alone.

## Payment update links (May 2026 only)

The May Dashboard guide described single-use links for customers to update the payment method on an automatically billed subscription. It said links are available for `active`, `past_due`, or `trialing` subscriptions, require a card, allow one update, and expire after 30 days if unused. The link updates only its associated subscription's method, not the customer's default payment method. These link restrictions are separate from the save-default settings above; the November guide is silent on current link availability.

## Ineligible types and possible errors

If an explicitly configured type is ineligible, Stripe **might** return an error when creating or updating the subscription or finalizing an invoice, according to the November guide. The May guide also discussed possible creation and payment-time/finalization errors. Neither capture establishes a successful account-specific payment attempt.

For payment-method-specific options, see `payment_settings.payment_method_options`.

## Related pages

- [[stripe-subscriptions-invoices]] — invoice collection and payment-method settings
- [[source-stripe-billing-collection-method]] — collection methods
- [[stripe-subscriptions]] — subscription concepts
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-subscriptions-payment-methods-setting-2026-11-07]] — November 7, 2026 Stripe docs capture
- [[stripe-subscriptions-payment-methods-setting-2026]] — May 13, 2026 Stripe docs capture
