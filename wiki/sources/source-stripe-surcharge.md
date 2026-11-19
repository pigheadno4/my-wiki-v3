---
title: "Stripe — Collect Surcharges"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/cards/surcharge
original_format: webpage
raw_files:
  - "stripe-payments-cards-surcharge-2026-11-07.md"
  - "stripe-surcharge-2026.md"
tags: [stripe, surcharge, payment-intent, compliance, refunds, multicapture, preview]
---

## Summary

The public-preview PaymentIntent surcharge guide describes how merchants, and connected accounts on platforms that set and collect payment fees, can offset some card acceptance costs. It requires API version `2026-03-25.preview` via a public-preview SDK or a Stripe-Version request header. An available API response or Stripe technical maximum is not legal permission, a recommended amount, or proof that a surcharge was collected. The merchant remains responsible for jurisdiction and card-network requirements.

## Availability and dated table difference

The November 7, 2026 table lists United States credit cards up to 3%, Canada credit cards up to 2.4%, and New Zealand all cards up to 4%. It also names Visa, Mastercard, Amex, Discover, Eftpos, Diners, Interac, JCB, Maestro, and Unionpay as available networks. The network list does not mean every network, card product, or merchant is eligible in every listed country.

The May 11, 2026 table additionally listed Australia, all cards, 4%. Australia is absent from the November table. This is a dated documentation difference; the captures alone do not establish current Australian legal or account-specific availability or prohibition.

## PaymentIntent availability and validation

With an attached payment method, sending `amount_details[surcharge][amount]` or `amount_details[surcharge][enforce_validation]` returns `surcharge.status` (`available` or `unavailable`) and, when technical validation is enabled, `surcharge.maximum_amount`. The maximum is Stripe's technical limit for the selected payment method, not a suggested surcharge or a legal/network cap. Compare a compliant calculation with that returned maximum to avoid technical errors.

| `enforce_validation` | Stripe technical behavior |
| --- | --- |
| `enabled` | Enforce technical maximum and return `maximum_amount`. |
| `disabled` | Do not enforce that technical maximum or return `maximum_amount`; funding-type and regional availability restrictions, and applicable law and network limits, remain. |
| `automatic` | Default technical maximum enforcement when no explicit value is sent. |

The guide allows explicit enablement or disablement at PaymentIntent create, update, or confirm. Once explicitly set either way, `surcharge.enforce_validation` cannot be modified.

## Amount, lifecycle, and capture

The top-level PaymentIntent `amount` must include subtotal plus surcharge; Stripe does not add `amount_details[surcharge][amount]` to it. For a $10 subtotal and $0.20 surcharge, set top-level `amount: 1020` and surcharge `amount: 20`. The November guide applies this at create, confirm, or capture. Its sample responses show `requires_confirmation` before confirmation and `requires_capture` after a confirmation request; neither is a captured payment or settlement outcome.

At capture, a surcharge set at confirmation can only be reduced, never increased. For multicapture, each capture can specify a surcharge, but their sum cannot exceed the surcharge confirmed. Incremental Authorization cannot increase the surcharge, even if the authorized amount increases; surcharging is unavailable when autocapturing with partial authorizations.

## Compliance, refunds, and receipts

The guide frames listed compliance duties as obligations that may apply by region and card type. Calculate within applicable law, card-network and cost-of-acceptance limits; notify the acquirer or card network **if required** by the jurisdiction or network; surcharge consistently where required; disclose the amount and total before purchase; show surcharge separately on the receipt; and allow cancellation or another payment method after disclosure. Stripe says the merchant bears responsibility for fines, penalties, and losses from noncompliance. These are documented guidance, not a determination for a specific transaction.

The merchant must implement surcharge-return logic for refunds. The guide says card-network rules and certain laws and regulations require the full surcharge on a full refund and a prorated amount on a partial refund; its example refunds $60.90 for $60 of a $100 order with a $1.50 surcharge. Stripe prebuilt receipts automatically display the surcharge; custom receipts must show it separately. The applied amount is visible at `PaymentIntent.amount_details.surcharge.amount`, and Sigma has `payment_intents.amount_details_surcharge_amount`.

## Preview migration and example scope

Both dated captures distinguish private-preview `amount_surcharge`, automatic top-level amount increment, always-on validation, update/confirm-only use, and `payment_method_options` response fields from public-preview `amount_details[surcharge]`, merchant-specified total-inclusive amount, configurable technical validation, create/update/confirm/capture support, and `amount_details` response fields. These are version contexts, not contradictory instructions for the same API version.

The May examples use the Node public-preview SDK; November examples use curl with explicit `Stripe-Version: 2026-03-25.preview` headers and an illustrative `return_url` on confirm. The sample change does not establish a universal new `return_url` requirement or remove a path-wide `payment_method_types` requirement.

## Related

- Company: [[stripe]]
- Concept: [[stripe-surcharge]]
- Related concepts: [[stripe-refunds]], [[stripe-payment-intents]]

## Raw Sources

- [[raw/stripe-payments-cards-surcharge-2026-11-07|November 7, 2026 surcharge guide]] — full captured page with US/Canada/New Zealand table and curl examples.
- [[raw/stripe-surcharge-2026|May 11, 2026 surcharge guide]] — full captured page with Australia row and Node examples.
