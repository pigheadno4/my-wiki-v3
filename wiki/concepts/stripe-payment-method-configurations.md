---
title: "Stripe Payment Method Configurations"
type: concept
category: technology
tags: [stripe, payment-method-configurations, dynamic-payment-methods, payment-element, checkout, connect, pmc]
---

## Definition

Payment method configurations (PMCs) let merchants create named sets of payment methods for different checkout scenarios. Each configuration gets a `pmc_...` ID. Part of the [[stripe-dynamic-payment-methods]] customization suite.

**Requires**: dynamic payment methods + Payment Element or Checkout.

**Default**: every account starts with "Default Config". Additional configs can be created via Dashboard or API.

## Use Cases

- Different PM sets for one-time purchases vs subscriptions
- Different PMs per product category
- (Connect) Offer connected accounts additional PMs for a different subscription fee

## Create a Configuration

### API

```js
stripe.paymentMethodConfigurations.create({
  name: 'MyConfig',
  affirm: { display_preference: { preference: 'on' } },
  klarna: { display_preference: { preference: 'on' } },
})
```

### Dashboard

Payment methods settings → Payment configurations → overflow menu → Create a configuration → name → Save. All PMs initially disabled by default.

## Use a Configuration at Checkout

Pass `payment_method_configuration: 'pmc_234'` on:
- **PaymentIntent**: `stripe.paymentIntents.create({ ..., payment_method_configuration: 'pmc_123' })`
- **Checkout session**: `stripe.checkout.sessions.create({ ..., payment_method_configuration: 'pmc_234' })`
- **Payment Element** (deferred intent): `{ mode: 'payment', paymentMethodConfiguration: 'pmc_234' }` (Web); `paymentMethodConfigurationId: "pmc_234"` (iOS/Android)

## Apple Pay / Google Pay Defaults

- Apple Pay: **enabled by default**
- Google Pay: **disabled by default**; also filtered when automatic tax enabled without shipping address collection

## Configs vs `excluded_payment_method_types`

| Use | When |
| --- | --- |
| Multiple PMCs | Broad categories (one-time vs subscriptions); consistent offerings across similar transactions |
| `excluded_payment_method_types` | Per-transaction fine-grained control; impractical to implement with configs |

Both can be combined. Apple Pay, Google Pay, and Link cannot be excluded via `excluded_payment_method_types` — use `wallets` hash instead.

## Sources

- [[source-stripe-payment-method-configurations]] — primary: create/manage configs, integration code (Web/iOS/Android), Apple Pay/Google Pay defaults, config vs exclusion decision rule
