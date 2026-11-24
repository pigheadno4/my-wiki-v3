---
title: "Stripe — Pay-As-You-Go Abuse Evaluation"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/pay-as-you-go-abuse"
raw_files:
  - "stripe-radar-pay-as-you-go-abuse-2026-11-07.md"
  - "stripe-radar-payg-abuse-2026.md"
tags: [stripe, radar, payg, usage-based, subscriptions, non-payment-abuse, payment-evaluation]
---

## Summary

[[stripe|Stripe]] [[stripe-radar|Radar]] documents a signal for intentional non-payment on post-paid or usage-based subscription invoices. The merchant server simulates an upcoming invoice payment outside checkout. Stripe returns `signals.non_payment_abuse.risk_level`, and the merchant chooses whether to review, invoice early, request prepayment or limit or pause usage. The May 2026 guide documents Payment Evaluation for this use case. The November guide documents Billing Evaluation in preview.

## When to Evaluate

- **Signup or card save before usage** — The November guide routes this stage to [[source-stripe-radar-free-trial-abuse|free-trial abuse prevention]] because there is no accrued usage or invoice amount for the non-payment abuse signal.
- **Mid-cycle** — Send the actual or estimated accrued usage amount. The guide recommends reevaluating as usage accrues with the latest projected amount, which is more useful when close to the final invoice amount.
- **Subsequent cycles** — Evaluate before each recurring invoice finalizes using the upcoming invoice amount, and again as usage accrues. The guide lists merchant actions such as flagging a renewal for manual review or requiring a credit top-up before further usage.

## Billing Evaluation Preview — 2026-11-07

The November guide's Customers v1 and Accounts v2 examples call `POST /v1/radar/billing_evaluations` with `Stripe-Version: 2026-10-28.preview`. They show `payment_details.currency` alongside the expected invoice amount and tokenized card PaymentMethod.

Each request uses exactly one customer field: `customer_details.customer` for a Customer ID, `customer_details.customer_account` for a customer-configured Account ID, or `customer_details.data` for inline attributes when the customer has neither a Customer nor an Account representation. The referenced Customer or Account must have an email address. For inline attributes, supply `data.email`. A missing email returns HTTP `400`.

The example returns a `radar.billing_evaluation` object. Within `signals`, the guide documents only `non_payment_abuse`, which contains `risk_level` and `evaluated_at`. The example's `livemode` value illustrates the response.

The separate [2026-09-30 Endive preview changelog](https://docs.stripe.com/changelog/endive/2026-09-30/adds-billing-evaluations-for-assessing-non-payment-abuse-risk) describes Radar Pro scope for usage-based or post-paid billing, optional client device metadata, and unavailable retrieval or listing for its `2026-09-30.preview` version.

## Payment Evaluation — 2026-05-10

The May guide shows `POST /v1/radar/payment_evaluations` with `Stripe-Version: 2026-03-25.dahlia`, a Customer ID, payment method and expected invoice amount. Its `money_movement_details` example specifies card, `customer_presence=off_session` and `payment_type=recurring`. The May guide says a Radar Session is unnecessary for this use case, so `client_device_metadata_details` is optional.

Its example `radar.payment_evaluation` response includes default `signals.fraudulent_payment` values such as a `-1.0` score, plus an evaluation-level `recommended_action` that reflects the overall evaluation. The May guide uses `signals.non_payment_abuse.risk_level` for merchant decisions and explicitly says this use case requires no outcome or event reporting.

> [!warning] Dated contract scope
> Use the inputs and response fields from the relevant guide. November's different endpoint and response leave continued signal support on the May endpoint and billing-evaluation outcome reporting unresolved.

## Risk Levels and Shared Behavior

| Level | Documented meaning or suggested action |
| --- | --- |
| `normal` / `low` | Low risk. No action required. |
| `elevated` | Consider manual review or usage limits. |
| `highest` | Consider pausing usage or requiring prepayment. |
| `not_assessed` | Stripe did not assess the signal. |
| `unknown` | Risk level unknown. |

- **Stripe Billing** — Both guides retrieve the subscription or Customer default payment method and the upcoming invoice's `amount_due`.
- **Fail-open** — In both guides, a Stripe `4xx` or `5xx` leaves the subscription or billing flow unaffected. The merchant can retry or continue without the signal.
- **Sandbox** — May names `pm_card_riskLevelHighest` and test card `4000000000004954` for `highest`. November lists `pm_card_radarBlock` and `pm_card_riskLevelHighest` for `highest`, plus `pm_card_riskLevelElevated` for `elevated`. It documents `not_assessed` for other test cards, including general fraud-testing fixtures. See the November **Sandbox behavior** tables for card numbers.

## Related Pages

- [[stripe-radar]] — Radar concept and adjacent risk controls
- [[source-stripe-radar-free-trial-abuse]] — separate risk control at signup or card save

## Raw Sources

- [[raw/stripe-radar-pay-as-you-go-abuse-2026-11-07|2026-11-07 Stripe pay-as-you-go abuse evaluation guide]] — full capture with Billing Evaluation, lifecycle guidance and sandbox fixtures
- [[raw/stripe-radar-payg-abuse-2026|2026-05-10 Stripe pay-as-you-go abuse evaluation guide]] — full earlier capture with Payment Evaluation and outcome reporting scope
