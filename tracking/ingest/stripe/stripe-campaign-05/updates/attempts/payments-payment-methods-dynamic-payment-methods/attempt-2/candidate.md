---
title: "Stripe Docs — Dynamic payment methods"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods
raw_files:
  - "stripe-payments-payment-methods-dynamic-payment-methods-2026-11-07.md"
  - "stripe-dynamic-payment-methods-2025.md"
tags: [stripe, dynamic-payment-methods, payment-element, checkout, ai-models, optimized-checkout, automatic-payment-methods]
---

## Summary

The May 8 and November 7, 2026 guides describe dynamic payment methods as part of the default [[stripe]] integration. Merchants manage most payment methods in the Dashboard. Stripe selects and orders eligible methods for each customer or checkout session across Payment Element, Checkout, Payment Links and the hosted invoice page.

## Integration and transaction exclusions

- To migrate manually configured Checkout or advanced Payment Element, remove `payment_method_types`. For advanced Payment Element with an API version before August 16, 2023, replace the explicit list with `automatic_payment_methods[enabled]=true`. The November capture corrects the May cURL continuation around the currency and automatic-payment-method arguments. See [[source-stripe-automatic-payment-methods]] for the separate API-version context.
- For Connect direct charges and charges using `on_behalf_of`, the connected account's settings determine available methods. May links to the dynamic payment methods migration page for platforms. November points to managing payment methods for connected accounts. The target change establishes a navigation update.
- The exclusion field `excluded_payment_method_types` is listed for PaymentIntents, SetupIntents, Checkout and Payment Element. The May Node example and equivalent November cURL example use enabled automatic methods and exclude `affirm` and `acss_debit` on one PaymentIntent, even if enabled in the Dashboard.
- For the particular PaymentIntent exclusion flow, use the integration-specific `wallets` settings to control Apple Pay, Google Pay or Link. Passing those wallet types to `excluded_payment_method_types` in this flow produces an error (May lines 87–108, November lines 89–105).

## Eligibility, customization and order

Eligibility depends on Dashboard enablement and Stripe account location, product, currency, final amount including discounts and tax, API compatibility, and the customer's country. Incompatible methods can be filtered by settings such as `setup_future_usage` or `capture_method: manual`. Apple Pay and Google Pay use separate criteria.

[[stripe-payment-method-configurations|Payment method configurations]], [[stripe-payment-method-rules|display rules]] such as amount and currency conditions, and [[stripe-ab-testing-payment-methods|A/B tests]] can also affect availability. The guides also describe embedding the payment method settings component for connected-account users. The Optimized Checkout Suite uses more than 100 on-session signals and broader network signals to select and order eligible methods alongside Dashboard rules and code-based logic. Stripe describes using an exploration-exploitation approach to refine ordering. Eligibility, checkout display and payment completion are distinct.

## Dated differences between product examples and support tables

- **Bacs Direct Debit.** Both dynamic guides give Bacs as a Mobile Payment Element exclusion example (May lines 110–114, November lines 107–111). The November support matrix marks the mobile UI supported. A separate footnote excludes creating Bacs SetupIntents with Payment Element and directs readers to Checkout setup mode. The documents differ on mobile UI support, apart from the SetupIntent constraint. [[raw/stripe-payments-payment-methods-payment-method-support-2026-11-07|November support matrix, lines 86–97]]
- **TWINT.** Both dynamic guides give TWINT as an example of a method without future setup (May lines 132–136, November lines 129–133). The November TWINT method page and the November support matrix list PaymentIntent future setup as supported. The matrix limits supported methods outside the listed card and bank-debit exceptions to `off_session`, which the May TWINT saving example uses. [[raw/stripe-payments-twint-2026-11-07|November TWINT overview, lines 231–236]] · [[raw/stripe-payments-payment-methods-payment-method-support-2026-11-07|November support matrix, lines 320–323 and 339–343]] · [[raw/stripe-twint-save-during-payment-2025|May TWINT saving guide, lines 400–419]]
- **Swish.** Both dynamic guides cite Swish for no recurring payments (May lines 110–114, November lines 107–111). The November support matrix excludes Checkout subscription/setup modes and lists a Subscriptions cell with the `send_invoice` qualification. November's Swish method overview excludes Billing, Invoicing and `setup_future_usage`. The Subscriptions cell is a dated table label for the `send_invoice` collection method. Automatic recurring collection remains unsupported in the two dynamic guides. [[raw/stripe-payments-payment-methods-payment-method-support-2026-11-07|November support matrix, lines 154–165]] · [[raw/stripe-payments-swish-2026-11-07|November Swish overview, lines 155–182]]

## Related Pages

- [[stripe-dynamic-payment-methods]] — durable concept
- [[stripe-payment-methods]] — payment methods overview
- [[source-stripe-automatic-payment-methods]] — August 2023 API change context
- [[source-stripe-payment-method-support]] — product and API support matrices
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-payment-methods-dynamic-payment-methods-2026-11-07|Dynamic payment methods, captured 2026-11-07]] — full guide (153 lines), cURL exclusion example and updated Connect navigation.
- [[raw/stripe-dynamic-payment-methods-2025|Dynamic payment methods, captured 2026-05-08]] — full guide (156 lines), with the historical Node exclusion example and Connect route.
