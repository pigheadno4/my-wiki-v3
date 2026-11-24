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
- **Advanced Payment Element, API on or after 2023-08-16** omits `payment_method_types`.
- **Advanced Payment Element, API before 2023-08-16** replaces the explicit list with `automatic_payment_methods[enabled]=true`.

## Excluding Payment Methods Per-Transaction

Use `excluded_payment_method_types` on PaymentIntent/SetupIntent/Checkout/Payment Element:

```js
stripe.paymentIntents.create({
  automatic_payment_methods: { enabled: true },
  excluded_payment_method_types: ['affirm', 'acss_debit'],
})
```

> For the documented per-PaymentIntent exclusion flow, use the integration-specific `wallets` settings to control Apple Pay, Google Pay or Link. Passing those wallet types to `excluded_payment_method_types` in that flow generates an error.

## Payment method eligibility

The guides describe the following checks. Payment method configurations, amount or currency rules and A/B tests can also affect availability.

1. **Dashboard enabled**: must be turned on per account
2. **Product support** varies by method. The May and November dynamic guides cite Bacs as unavailable in Mobile Payment Element. The November support matrix marks mobile UI support and separately excludes Payment Element creation of Bacs SetupIntents. See [[source-stripe-dynamic-payment-methods]] for the dated discrepancy.
3. **Presentment currency**: most PMs support only a subset of Stripe's 135+ currencies
4. **Charge amount**: some PMs have min/max limits; final amount (incl. tax + discounts) is used
5. **API support** filters incompatible methods when `setup_future_usage` or `capture_method: manual` is set. The dynamic guides use TWINT as an example of a method without future setup. The November TWINT overview and support matrix list PaymentIntent future setup as supported, and the November matrix footnote limits supported TWINT future setup to `off_session`. The May saving guide shows one `off_session` request. See [[source-stripe-dynamic-payment-methods]] for the dated evidence.
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
| [[stripe-payment-method-rules\|Payment method rules]] | Set visibility by amount, country, or currency for eligible non-card methods. The November 2026 guide excludes wallets, Hosted Invoice Page, and subscription creation through the listed integrations. |
| [[stripe-ab-testing-payment-methods\|A/B testing]] | Roll out PMs to a % of traffic; measure conversion impact |
| [[stripe-payment-method-configurations\|Payment method configurations]] | Different PM sets for different checkout scenarios |
| Embed PM settings component | Let connected account users manage their own PMs |

## Sources

- [[source-stripe-dynamic-payment-methods]] covers the May and November 2026 guides for advanced migration, transaction exclusions, eligibility and ranking, including dated Bacs, TWINT and Swish qualifications.
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change: omit payment_method_types → Dashboard methods; allow_redirects: never option; Elements migration
