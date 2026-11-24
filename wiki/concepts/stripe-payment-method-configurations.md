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

In Dashboard Payment methods settings, create and name the configuration. A new Dashboard configuration starts with all payment methods disabled. Set the configuration status to **Active**, save it, then enable the desired methods. Stripe filters the enabled methods for the payment’s currency and location and ranks the eligible methods.

## Use a Configuration at Checkout

Choose the configuration ID when using dynamic selection without an explicit `payment_method_types` list.

- **Server** uses `payment_method_configuration` for PaymentIntent creation or for Checkout Session creation without a Payment Element.
- **Deferred clients** use `paymentMethodConfiguration` on the Web Payment Element and `paymentMethodConfigurationId` in the iOS and Android PaymentSheet intent configuration.

## Dated Checkout wallet guidance

The May 2026 Checkout section describes Apple Pay as enabled by default and Google Pay as disabled by default. It describes Google Pay filtering for automatic tax without a shipping address and says Stripe-hosted Checkout needs no integration changes. The November guide gives general Checkout support for both wallets and links to testing. Current defaults and the automatic-tax filtering behavior remain unresolved from that newer wording.

## Configs vs `excluded_payment_method_types`

| Use | When |
| --- | --- |
| Multiple PMCs | Broad categories (one-time vs subscriptions); consistent offerings across similar transactions |
| `excluded_payment_method_types` | Per-transaction fine-grained control; impractical to implement with configs |

Configurations can be combined with `excluded_payment_method_types`. To control Apple Pay, Google Pay or Link for a transaction, use the integration-specific `wallets` parameters.

## Sources

- [[source-stripe-payment-method-configurations]] covers the May and November 2026 guides for Dashboard activation, server and deferred client configuration, dated Checkout wallet wording and transaction-level exclusions.
