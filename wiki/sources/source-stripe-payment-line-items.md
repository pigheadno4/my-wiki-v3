---
title: "Stripe — Payment Line Items"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-line-items"
raw_files:
  - "stripe-payments-payment-line-items-2026-11-07.md"
  - "stripe-payment-line-items-2026.md"
tags: [stripe, payment-line-items, l2-l3, interchange, commercial-cards, klarna, paypal, payment-intents]
---

## Summary

The May 11 and November 7, 2026 guides describe adding transaction metadata to PaymentIntents through `amount_details` and `payment_details`. It helps customers reconcile purchases. Eligible commercial cards on IC+ pricing can qualify for interchange savings. Klarna and PayPal use line-item data in underwriting, which can improve approvals.

## Geographic and network scope

- The card program covers US domestic transactions with US merchants and US-issued cards (excluding US territories), and intra-EU transactions with EU merchants and EU-issued cards. Stripe lists Visa, Mastercard and American Express, with a direct agreement required for AmEx savings. The guides list up to 200 line items and say AmEx receives only the first four.
- Klarna is described as a global payment method and PayPal as available to customers across locations. Business-location eligibility is defined in the individual payment-method guides.
- The November guide says **US Visa Level 2 ended in April 2026**, with Visa savings available through **Product 3 CEDP**. Its retained Visa Level 2 column is context for the former program. Mastercard Level 2 remains separately documented.
- November lists Visa Product 3 for Purchasing, Corporate and Business cards, versus Mastercard Level 3 for Purchasing and Corporate cards. It retains Business, Purchasing and Corporate in the Level 2 column. May used generic card-type rows for Level 2 and Level 3/Product 3.
- November revises Visa exclusion codes, extends Mastercard’s `3000–3299` exclusion range to `3000–3350` for L2 and L3, and lists separate Product 3 exclusions for federal-government-issued Visa GSA T&E Corporate and Purchasing cards at specified MCCs. Read the dated network tables for the exact codes and sales-tax requirements. The industry-to-MCC examples are a separate lookup.

## Minimum fields and validation

- **Payment Intents API, Level 2.** Send transaction tax in `amount_details[tax][total_tax_amount]` and the order reference in `payment_details[order_reference]` for the documented Level 2 program.
- **Payment Intents API, Level 3/Product 3.** Include order reference and per-item product name, unit cost, quantity, product code and unit of measure. November explicitly permits transaction-level tax or per-item tax for L3, although the per-item field row still labels tax required. The field notes prohibit combining those two placements. May’s minimum-field table names per-item tax, but its request examples already show how to pass transaction-level tax. Report actual sales tax, including zero when none was collected.
- **Checkout Sessions API.** Checkout populates Level 2 tax and order reference from line items. Its documented Level 3 inputs are Checkout line-item quantity, price unit amount and product, and product name and unit label. These are Checkout fields.
- **Validation versus eligibility.** Network MCC and tax requirements affect savings eligibility without causing a corresponding Stripe API rejection. Stripe returns HTTP 400 for an arithmetic mismatch by default. Set `amount_details.enforce_arithmetic_validation: false` per request to proceed with an `amount_details.error` when arithmetic fails. Stripe withholds mismatched card line-item data from the networks, removing L2/L3 qualification. Payment status and any realized savings are separate outcomes.

## PaymentIntent operations and field limits

- Send line items during confirmation with automatic or manual capture. If omitted at confirmation, supply them at a supported capture. PayPal does not support setting line items at capture. For an ordinary separate capture, already supplied line items persist. If a capture updates them, match the updated data to the capture amount. Multicapture has separate field continuity rules in the [[source-stripe-payment-line-items-flexible|flexible guide]].
- Expand `amount_details.line_items` to include line items in API responses. A create response can remain `requires_payment_method`. A sample return URL gives a destination and does not confirm payment completion.
- Per-item tax appears in actual examples as `amount_details[line_items][index][tax][total_tax_amount]`. Use one tax placement per request and one discount placement per request. The field table sometimes uses singular `line_item` as shorthand for an indexed item.
- Product names allow up to 1,024 characters (card transmission truncates to 26 alphanumeric characters, PayPal to 127). Product code and alphanumeric unit of measure allow up to 12 characters. Order reference is truncated to 25 alphanumeric characters for cards and 255 for Klarna, where it is visible to the customer. Card-only customer reference is truncated to 25 alphanumeric characters before network transmission.

## Payment-method-specific fields

Pass supported method-specific fields under each PaymentIntent item at `amount_details[line_items][index][payment_method_options][method]`. Different methods’ fields may coexist in a request when supported, independent of which method confirms it.

- **Card.** `commodity_code` is at most 12 alphanumeric characters, without spaces.
- **Klarna.** `product_url` and `image_url` allow up to 4,096 characters. `reference` is customer-visible, while `subscription_reference` is for select recurring integrations. Each reference allows up to 255 characters. Klarna derives the item amount as `(unit_cost × quantity) − discount_amount + tax.total_tax_amount`; the example still supplies a PaymentIntent `amount`.
- **PayPal.** `description` allows up to 127 characters. `category` is `digital_goods`, `physical_goods`, or `donation`. `sold_by` identifies the connected Stripe account selling the item. Leave it blank outside that role.
- **Industry metadata.** Both guides say card and PayPal line items cannot accompany travel-industry metadata. They separately document Klarna Extra Merchant Data as private preview.

## Flexible payment scenarios

The May cards row excludes partial and decrement authorization. The November cards compatibility row uses broader wording and the guide names surcharge, multicapture, overcapture, incremental, decremental and partial authorization. The [[source-stripe-payment-line-items-flexible|companion guide]] documents conditional manual partial authorization and capture-time reconciliation, and does not include a decrement procedure. Its multicapture guidance excludes Klarna and PayPal. See the companion for scenario-specific prerequisites.

## Detail locators

- November lines 19–53 and May lines 18–49 cover card, region, and network eligibility, including the dated Visa and Mastercard MCC tables. November lines 683–713 and May lines 789–822 are the separate industry-to-MCC lookup.
- November lines 55–128 and May lines 51–126 cover minimum fields, the separate Checkout structure, and conditional validation. November lines 417–451 and May lines 511–547 show the full indexed PaymentIntent line-item and method nesting.
- November lines 290–407 and May lines 324–501 cover confirmation and capture. November lines 612–620 and May lines 706–714 cover arithmetic validation and network eligibility.

## Related Pages

- [[stripe|Stripe]]
- [[stripe-payment-line-items]] — payment line items concept
- [[stripe-payment-intents]] — Payment Intents API concept
- [[source-stripe-payment-line-items-flexible]] — scenario implementation guide

## Raw Sources

- [[raw/stripe-payments-payment-line-items-2026-11-07|November 7, 2026 payment line items guide]] — full capture (717 lines).
- [[raw/stripe-payment-line-items-2026|May 11, 2026 payment line items guide]] — full capture (826 lines).
