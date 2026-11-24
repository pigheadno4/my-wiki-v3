---
title: "Stripe Dynamic Payment Methods"
type: concept
category: technology
tags: [stripe, dynamic-payment-methods, payment-element, checkout, ai-models, optimized-checkout, payment-method-rules, a-b-testing]
---

## Definition

Dynamic payment methods is the default Stripe integration model where payment method selection is managed from the Dashboard — no code changes needed to add or remove methods. Stripe uses AI to determine which eligible payment methods to display and in what order for each checkout session.

Works with: Payment Element, Checkout, Payment Links, Hosted Invoice Page.

## Migration from Manual (`payment_method_types`)

Remove `payment_method_types` from code:
- **Checkout**: just omit the parameter
- **Payment Element, API ≥ 2023-08-16**: omit `payment_method_types` (Stripe defaults to dynamic mode)
- **Payment Element, API < 2023-08-16**: replace with `automatic_payment_methods[enabled]=true`

## Excluding Payment Methods Per-Transaction

Use `excluded_payment_method_types` on PaymentIntent/SetupIntent/Checkout/Payment Element:

```js
stripe.paymentIntents.create({
  automatic_payment_methods: { enabled: true },
  excluded_payment_method_types: ['affirm', 'acss_debit'],
})
```

> **Exception**: Apple Pay, Google Pay, and Link must be excluded via the `wallets` hash parameter — using `excluded_payment_method_types` for these generates an error.

## Eligibility Criteria (6 Factors)

A payment method only appears if all 6 criteria are met:

1. **Dashboard enabled**: must be turned on per account
2. **Product support**: not all PMs available in all products (e.g., Bacs not in Mobile PE)
3. **Presentment currency**: most PMs support only a subset of Stripe's 135+ currencies
4. **Charge amount**: some PMs have min/max limits; final amount (incl. tax + discounts) is used
5. **API support**: `setup_future_usage` or `capture_method: manual` auto-filter incompatible PMs
6. **Customer's country**: most PMs are country-specific (e.g., BLIK Poland-only)

> Apple Pay and Google Pay use different eligibility criteria — see wallet-specific docs.

> With Connect direct charges or `on_behalf_of`, the connected account's settings determine available PMs.

## AI Models (Optimized Checkout Suite)

For each session, AI models determine payment method order and display using:
- 100+ on-session signals (real-time uptime, popularity among similar customers)
- Network signals (preferred PMs of similar businesses)
- Exploration-exploitation framework: proven strategies + continuous testing

Works alongside Dashboard rules and code-based logic.

## Dashboard Customization Features

| Feature | Purpose |
| --- | --- |
| [[stripe-payment-method-rules\|Payment method rules]] | Show/hide PMs based on amount or customer location |
| [[stripe-ab-testing-payment-methods\|A/B testing]] | Roll out PMs to a % of traffic; measure conversion impact |
| [[stripe-payment-method-configurations\|Payment method configurations]] | Different PM sets for different checkout scenarios |
| Embed PM settings component | Let connected account users manage their own PMs |

## Sources

- [[source-stripe-dynamic-payment-methods]] — primary: migration guide, exclusion API, eligibility criteria, AI models, customization features
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change: omit payment_method_types → Dashboard methods; allow_redirects: never option; Elements migration
