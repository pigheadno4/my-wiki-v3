---
title: "Update a Checkout Integration to Use Managed Payments"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/managed-payments/update-checkout"
raw_files:
  - "stripe-payments-managed-payments-update-checkout-2026-11-07.md"
  - "stripe-managed-payments-update-checkout-2025.md"
tags: [stripe, managed-payments, checkout, migration, unsupported-parameters, subscriptions, one-time-payments]
---

## Summary

Stripe’s November 7, 2026 migration guide covers enabling [[stripe-managed-payments]] on an existing hosted or embedded [[stripe-checkout]] integration. [[stripe]] describes its merchant-of-record solution as handling indirect tax compliance in more than 80 countries, fraud prevention, dispute management, and transaction-level customer support. [[stripe-link|Link]] acts as merchant of record at checkout and provides subscription management and transaction support on the Link website. The tax coverage and the April 22, 2026 general-availability milestone for businesses in 39 countries measure different things. See November guide lines 9-15 and 194-200 and the [[source-stripe-managed-payments-changelog|Managed Payments changelog]].

## Steps to Migrate

1. Enable Managed Payments in the Stripe Dashboard. The existing hosted or embedded integration must create Checkout Sessions in `payment` or `subscription` mode and use API version `2025-03-31.basil` or later. Only new subscriptions purchased through a Managed Payments Checkout Session are eligible. For a new integration, see [[source-stripe-managed-payments-setup]].
2. Verify [[source-stripe-managed-payments-eligibility|product eligibility]] and set an eligible tax code on each digital product in the Dashboard or via API. For inline products, set `line_items[].price_data.product_data.tax_code`; see the November guide’s “Configure your products for Managed Payments” at lines 20-72.
3. Set `managed_payments[enabled]=true` in the server’s Checkout Session creation request and remove the fields listed for the applicable mode. The November guide gives separate subscription and one-time examples and removal tables at lines 74-148.

## November 7, 2026 — Fields, Identities and Payment Outcomes

The November subscription and one-time tables still document removals for Adaptive Pricing, tax, payment-method selection, customer update, shipping, Connect, and post-sale actions. Managed Payments covers digital products, so it does not collect shipping information, and it does not support Connect. Follow the exact subscription table (lines 106-124) or one-time table (lines 126-148). Stripe controls available methods using dynamic payment methods.

Managed Payments requires the customer’s name and a valid billing address to calculate sales tax. Remove `customer_update[name]` and `customer_update[address]`. If you supply an existing `customer_account` or `customer` ID at Session creation, Managed Payments updates the referenced Account or Customer with any changes to those details (lines 116-117 and 136-137). After successful payment, the guide says the Session references the Customer and either a successful PaymentIntent or an active Subscription (line 15). Session creation or a checkout redirect alone gives no evidence of either outcome. See the setup guide for post-payment webhooks and delayed-payment outcomes.

A subscription purchased through Managed Payments authorizes Managed Payments to charge that payment method. Obtain appropriate customer consent before using it for transactions outside Managed Payments (November lines 173-175 and April lines 244-246).

The November one-time table omits `payment_intent_data.setup_future_usage` and `payment_method_options.{payment_method}.setup_future_usage`. The September 3, 2026 [[source-stripe-managed-payments-changelog|Managed Payments changelog]] explicitly documents the two named parameters for Managed Payments Checkout Session creation, with payment-method scope on the nested parameter. November also omits top-level `payment_method_options` from the subscription removal table. That omission leaves general subscription options unresolved, and the September entry supplies technical support only for the fields it names. The consent requirement still applies.

## Checkout UI and Returns

The migration guide covers hosted and embedded Checkout pages. The Managed Payments overview separately excludes payment flows using Elements-style embeddable components and advanced integrations. April’s `ui=embedded-form` and November’s `ui=embedded-page` are documentation query parameters. The API transition comes from the separate `2026-03-25.dahlia` changelog, which replaces Checkout Session `ui_mode` values `hosted`, `embedded`, and `custom` with `hosted_page`, `embedded_page`, and `elements`, and adds the distinct `form` value.

The November Checkout Session create reference defaults to `hosted_page`. For `embedded_page` or `elements`, it disallows `success_url` and requires `return_url` when redirect-based payment methods are enabled. The migration samples omit `ui_mode` and set `success_url` (November lines 49-100). Use the mode-specific create contract for an embedded migration. The API changelog identifies an API version boundary. It leaves the version of the migration examples and Managed Payments eligibility for other UI modes unstated.

## April 23, 2026 — Historical Migration Guide

The April capture included a standalone Dashboard Terms-of-Service acceptance step, explicitly said every product in the purchase needed to be eligible, and used “during this preview” for the new-subscriptions-only rule. November still requires enablement, eligible products and eligible tax codes, and retains the restriction to new subscriptions without the preview wording. Its omissions leave the status of the standalone Terms step and mixed-cart eligibility unconfirmed.

- April subscriptions table (lines 168-189) included `payment_method_options` among the fields to remove.
- April one-time table (lines 191-217) included `payment_intent_data.setup_future_usage` and `payment_method_options.{payment_method}.setup_future_usage` among the fields to remove. The November guide and scoped September changelog above document the later status of these two fields.
- April uses Node.js examples and November uses cURL, both with the same minimum API version. The updated sample language, step numbering and clearer test headings are presentation changes.

## Testing and Price Tax Behavior

The guides describe varying billing addresses to test tax calculations and reviewing transaction details in the Dashboard. Sandbox purchases have no automatic receipt email. The Dashboard can send a receipt manually for preview. Sandbox purchases do not appear in the Link app. The guide uses a repeat Checkout Session to test Link account checkout and a live-mode Session for testing the app’s order-management tools. See April lines 219-271 and November lines 150-200.

Prices can set inclusive or exclusive `tax_behavior`. Without a price override, the documented default adds tax on top. Change the default through **Include tax in prices** in Dashboard Tax settings. See April lines 273-279 and November lines 202-208.

## Related Pages

- [[stripe-managed-payments]] — product concept, integration paths and limitations.
- [[stripe-checkout]] — Checkout UI and Session outcome context.
- [[source-stripe-managed-payments-setup]] — new Checkout integration guide and post-payment event handling.
- [[source-stripe-managed-payments-overview]] — Merchant of Record responsibilities and unsupported integrations.
- [[source-stripe-managed-payments-eligibility]] — product criteria and eligible tax codes.
- [[source-stripe-managed-payments-changelog]] — dated feature and API changes.

## Raw Sources

- [[raw/stripe-payments-managed-payments-update-checkout-2026-11-07|Stripe’s November 7, 2026 Managed Payments Checkout migration guide]]
- [[raw/stripe-managed-payments-update-checkout-2025|Stripe’s April 23, 2026 Managed Payments Checkout migration guide]]

## Related raw API references

- [[raw/stripe-changelog-dahlia-2026-03-25-updates-available-checkout-session-ui-modes-2026-11-07|March 25, 2026 Dahlia Checkout Session UI mode changelog]] — November 7, 2026 capture, lines 5-28.
- [[raw/stripe-api-checkout-sessions-create-2026-11-07|Checkout Session create reference]] — November 7, 2026 capture, lines 476-477, 512-513 and 518-531.
