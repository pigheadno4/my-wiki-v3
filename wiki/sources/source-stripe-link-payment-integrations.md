---
title: "Stripe Docs — Link in different payment integrations"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
canonical_url: "https://docs.stripe.com/payments/link/link-payment-integrations"
original_format: webpage
raw_files:
  - "stripe-payments-link-link-payment-integrations-2026-11-07.md"
  - "stripe-link-payment-integrations-2025.md"
tags: [stripe, link, payment-method-types, card-integration, ic-plus, backup-payment, instant-bank-payments]
---

## Summary

The May 8 and November 7, 2026 guides describe two ways to integrate Link. Enable Link under **Wallets** in Payment methods settings and integrate it for the use case. Stripe then displays Link automatically for eligible transactions. Both routes can use credit, debit, and eligible non-card funding such as Instant Bank Payments and Klarna. Funding methods have their own eligibility and integration limits.

## Integration paths

| Path | May manual request | November manual request | PaymentMethod representation |
| --- | --- | --- | --- |
| **Standalone Link** (recommended) | Include `link` in `payment_method_types`, or use dynamic payment methods | Include `link` in `allowed_payment_method_types`, or use dynamic payment methods | `type=link` |
| **Card-specific Link** | Include `card` and omit `link` in `payment_method_types` | Include `card` and omit `link` in `allowed_payment_method_types` | `type=card`, `card.wallet.type=link` |

In each dated manual recipe, including `link` selects standalone Link even when the list also includes `card`. Card-specific integration exposes genuine brand and last-four details for actual credit or debit funding. The standalone PaymentMethod does not reveal the exact underlying instrument.

Standalone Link uses a single blended rate in the integration guide and excludes Interchange+ (IC+). November explicitly excludes extended authorization, incremental authorization, and overcapture. Stripe directs integrations affected by these limits to the card-specific route. These standalone exclusions leave feature availability and pricing entitlement on a particular card integration unresolved.

Only standalone Link offers backup payment selection. Link suggests a backup if the customer has multiple eligible saved payment sources. If the customer approves it and the first attempt fails, Link retries with that source. The card-specific route offers no backup selection at checkout.

## Request fields by API surface

- **PaymentIntent and SetupIntent.** The `2026-07-29.dahlia` changelog adds `allowed_payment_method_types`. It filters a requested list to compatible methods based on inputs such as currency, amount, and customer, then returns the subset in `payment_method_types`. Do not combine the allow list with `payment_method_types`, `excluded_payment_method_types`, `automatic_payment_methods`, or `payment_method_configuration`. On `2026-09-30.endive`, the removal changelog’s named PaymentIntent create, update, and confirm and SetupIntent create and update methods return HTTP 400 `payment_method_types_no_longer_supported` for writes to the old field. The response field remains computed and read-only. The same changelog’s Impact section separately names `2026-08-26.preview` for upgrade preparation. The captured documentation leaves a universal start version unresolved.
- **Hosted Checkout Session Create.** The November [[source-stripe-checkout-link|Checkout Link guide]] still says to include both `card` and `link` in `payment_method_types` and use a single currency across line items. Both hosted guides separately advise listing payment methods manually when collecting card details for future use via SetupIntent. Select the supported request field for the Intent endpoint and version in use. The separate `2026-09-30.endive` Checkout Sessions changelog says the old request field returns HTTP 400 on Session creation. It directs integrations to dynamic payment methods or `allowed_payment_method_types`, with compatible methods still reported in the response’s computed `payment_method_types`.
- **Stripe.js deferred Elements.** On Endive, `paymentMethodTypes` throws a client integration error when creating Elements without a PaymentIntent or SetupIntent or calling `elements.update()`. Use the client option `allowedPaymentMethodTypes` or Dashboard-managed dynamic methods.

Receiving a compatible subset does not itself establish that Link displays or that a payment succeeds. Wallets enablement, integration, and transaction eligibility still apply.

## Non-card funding in a card integration

For non-card funding such as Instant Bank Payments, Stripe uses the following fixed PaymentMethod values.

| Field | Fixed value |
| --- | --- |
| `type` | `card` |
| `card.brand` | `link` |
| `card.last4` | `0000` |
| `card.exp_month`, `card.exp_year` | `12`, `2040` |
| `card.funding` | `unknown` |
| `card.display_brand` | `other` |
| `card.networks.available` | `["link"]` |
| `card.checks` results | `null` |

Stripe recommends showing **Link** in the customer interface in place of these placeholder card details.

The separate November US [[source-stripe-link-payment-methods|Link funding-groups guide]] describes coarse Charge metadata. Read `payment_method_details.link.funding_source_group` for standalone Link or `payment_method_details.card.wallet.link.funding_source_group` for card-specific Link. A group can contain multiple methods, such as Pix and UPI. This reporting does not identify the exact funding instrument. The US guide separately applies Link Group fees under the Stripe Pricing Agreement regardless of eligibility for any particular funding method. Use that agreement to determine the applicable fees.

## Confirmation and settlement

Both integration captures describe immediate confirmation and settlement of successful payments to the Stripe balance on the card timeline. Payout to a bank account is a separate step. The November [[source-stripe-instant-bank-payments|Instant Bank Payments guide]] says authorized payments settle on the card timeline and covers bank-initiated ACH returns. Customer-initiated disputes with the bank are an exception and can debit the payment amount and dispute fee.

The November [[source-stripe-klarna-on-link|Klarna on Link guide]] limits eligible US use to Payment Links, hosted Checkout, and Payment Element. It describes a credit to the Stripe account for the purchase amount minus Stripe fees immediately after issuer authorization. That wording concerns the Stripe account credit.

## Related Pages

- [[stripe]] — payment provider
- [[stripe-link]] — Link integration paths and funding methods
- [[stripe-instant-bank-payments]] — non-card Link funding and dispute boundary

## Raw Sources

- [[raw/stripe-payments-link-link-payment-integrations-2026-11-07|2026-11-07 Link in different payment integrations]] — 93 lines
- [[raw/stripe-link-payment-integrations-2025|2026-05-08 Link in different payment integrations]] — verbatim webpage content, 87 lines

## Related raw API references

- [[raw/stripe-changelog-dahlia-2026-07-29-allowed-payment-method-types-parameter-2026-11-07|2026-11-07 Dahlia Intent allow-list changelog]] — compatible-subset and mutual-exclusion rules
- [[raw/stripe-changelog-endive-2026-09-30-removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents-2026-11-07|2026-11-07 Endive Intent request-field changelog]] — endpoint table, error, and preview upgrade note
- [[raw/stripe-changelog-endive-2026-09-30-remove-payment-method-types-checkout-sessions-2026-11-07|2026-11-07 Endive Checkout Session Create changelog]] — request and response properties
- [[raw/stripe-changelog-endive-2026-09-30-remove-elements-deferred-intent-payment-method-types-2026-11-07|2026-11-07 Endive Stripe.js changelog]] — deferred Elements client option
