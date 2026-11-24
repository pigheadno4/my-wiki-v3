---
title: "Stripe Docs — Payment method configurations"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/payment-method-configurations
raw_files:
  - "stripe-payments-payment-method-configurations-2026-11-07.md"
  - "stripe-payment-method-configurations-2025.md"
tags: [stripe, payment-method-configurations, dynamic-payment-methods, payment-element, checkout, connect, pmc]
---

## Summary

The May 8 and November 7, 2026 guides cover named payment method configurations for different checkout scenarios. Both require dynamic payment methods with Payment Element or Checkout. A merchant or platform can use different enabled sets by product, by one-time versus subscription checkout, or to offer connected accounts extra methods for a different subscription fee. The merchant or platform selects a configuration and Stripe filters its enabled methods by payment location, currency and applicable restrictions, then ranks eligible methods to optimize conversion.

## Create and enable a configuration

- The account starts with **Default Config**. Create additional named configurations in Dashboard Payment methods settings or with the Payment Method Configurations API.
- A newly created Dashboard configuration starts with all methods disabled. Set the configuration status to **Active**, save it, and turn on the desired methods. Configuration status and method enablement are separate settings. The November guide links to the Dashboard **Payment methods review** page, where merchants can review a transaction ID or enter amount and currency.
- API creation accepts a Dashboard-readable `name` and optional named method fields. Both captures use `affirm` and `klarna` with `display_preference.preference` set to `on`. May uses Node's `stripe.paymentMethodConfigurations.create()`. November shows cURL against `/v1/payment_method_configurations`.

## Apply a configuration

Copy the configuration's `pmc_...` ID from the Dashboard. The examples use dynamic selection without an explicit `payment_method_types` list. The separate November Payment Method Configurations API overview states that boundary explicitly. ([[raw/stripe-api-payment-method-configurations-2026-11-07|November API overview, line 25]])

- **Deferred Web Payment Element** uses `paymentMethodConfiguration` in its client options.
- **Deferred iOS and Android PaymentSheet** use `paymentMethodConfigurationId` in the intent configuration.
- **Server creation** uses `payment_method_configuration` on a PaymentIntent or on a Checkout Session without a Payment Element. The PaymentIntent examples explicitly enable `automatic_payment_methods`. Both captures state that the latest API version described there enables it by default. The May server examples use Node and the November examples use cURL for these same fields.

For Connect account selection, the separate November API overview describes direct configurations for payments created on the merchant or platform’s own Stripe account and child configurations for payments on connected accounts using direct charges or `on_behalf_of`. Dashboard-managed parent configurations set defaults and control connected-account overrides. See that overview for charge-type scope. ([[raw/stripe-api-payment-method-configurations-2026-11-07|November API overview, lines 27–33]])

## Checkout wallet guidance

The May Checkout section gives Apple Pay enabled and Google Pay disabled as defaults. It says Stripe filters Google Pay if automatic tax is enabled without collecting a shipping address, and specifies that Stripe-hosted Checkout pages need no integration changes to enable either wallet. It says Stripe handles those wallet payments the same way as other card payments. These are dated Checkout statements. Newly created Dashboard configurations start with methods disabled as described above (May lines 148–154 and 29–46).

The November section says Checkout supports Apple Pay and Google Pay with no integration changes and links to the Checkout Sessions wallet test variant. Its wording omits the May defaults and the automatic-tax condition. The canonical wallet testing index lists separate testing variants. This leaves current defaults, filtering and rendering unresolved for a particular account or integration (November lines 127–132). [[raw/stripe-testing-wallets-2026-11-07|November wallet testing index, lines 5–16]]

## Configurations and transaction-level exclusions

Use configurations for broad categories of transactions and `excluded_payment_method_types` for fine-grained exclusions on PaymentIntents, SetupIntents, Checkout and Payment Element. A configuration and a per-transaction exclusion can be used together. The combined-use sentence in both captures shows the stray spelling `excluded_payment_methods_types`. The surrounding passages and the separate dynamic-payment-methods request example use `excluded_payment_method_types`.

Use the integration-specific `wallets` parameters to control Apple Pay, Google Pay or Link for one transaction. The exclusion field is for other supported methods (May lines 177–194, November lines 149–166). See [[source-stripe-dynamic-payment-methods]] and its November exclusion example. [[raw/stripe-payments-payment-methods-dynamic-payment-methods-2026-11-07|November dynamic payment methods, lines 89–105]]

## CDN Assets

- `raw/assets/stripe-payment-method-configurations.png` is the May Dashboard UI screenshot (168 KB). The November capture references a CDN image.

## Related Pages

- [[stripe-payment-method-configurations]]
- [[stripe-dynamic-payment-methods]]
- [[stripe-payment-method-rules]]
- [[stripe]]

## Raw Sources

- [[raw/stripe-payments-payment-method-configurations-2026-11-07|Payment method configurations, captured 2026-11-07]] — full guide (166 lines) with cURL examples and Checkout wallet testing navigation.
- [[raw/stripe-payment-method-configurations-2025|Payment method configurations, captured 2026-05-08]] — full guide (194 lines) with Node examples and dated Checkout wallet defaults and filtering.
