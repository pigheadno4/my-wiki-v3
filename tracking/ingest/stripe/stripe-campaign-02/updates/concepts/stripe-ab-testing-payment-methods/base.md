---
title: "Stripe A/B Testing Payment Methods"
type: concept
category: technology
tags: [stripe, a-b-testing, dynamic-payment-methods, payment-element, checkout, conversion, experimentation]
---

## Definition

Stripe's A/B testing feature lets merchants test new payment methods with a percentage of buyers before rolling out to all customers. Dashboard-only (no API). Requires [[stripe-dynamic-payment-methods]] to be enabled.

**Supported integrations**: Payment Element Web (PaymentIntents API) or Checkout in payment mode.

## How It Works

1. Create experiment in Dashboard → select PMs, optional PM rules, set traffic % (1–99%)
2. Stripe randomizes sessions by UserAgent + IP + date; same buyer sees consistent treatment/control for a given day
3. Sessions aggregated daily to avoid double-counting
4. Monitor results in Dashboard; download raw data for additional analysis
5. End experiment → adopt treatment settings or revert to control

## Key Constraints

- **One experiment per configuration** at a time
- **Dashboard only** — no API management
- **Can't toggle PMs mid-experiment** — must end experiment to change PM settings
- **Auto-ends at 180 days** → reverts to control settings

## Experiment Setup

- **Default traffic split**: 50/50 (recommended); 80,000 sessions gives 80% power to detect 100 BPS change at 5% significance
- **Optional PM rules**: add filters (e.g., minimum amount, presentment currency) to control eligibility
- **BNPL experiments**: Stripe recommends installing the Payment Method Messaging Element alongside

## Statistical Methodology

- **Primary metric**: average revenue per session (total revenue ÷ total sessions, including non-converting)
- **Significance**: z-test at 5% level (95% confidence interval); results flagged when < 5% probability of being due to chance
- **Power calculation**: 80% power to detect 1% difference at 5% significance
- **Indicators**: green = significant increase, yellow = significant decrease, gray = insufficient sessions (< 80% of required)

## Result Metrics

| Metric | Description |
| --- | --- |
| Average revenue per session | **Primary metric** — total revenue ÷ total sessions (incl. non-converting) |
| Revenue at 100% sessions | Projected revenue if treatment offered to 100% of traffic |
| Gross revenue | Actual revenue (influenced by treatment/control split %) |
| Conversion rate | Sessions with purchase ÷ eligible sessions (treatment PMs eligible + UI rendered) |
| Average order value | Average purchase amount for converting sessions |

## Raw Data Export (16 dimensions)

Key fields: `experiment_session_id` (group by this to avoid double-counting), `is_treatment`, `converted`, `payment_method`, `is_eligible_session`, `control_payment_method_types`, `treatment_payment_method_types`, `rendered_payment_methods`, `visible_payment_methods`.

## Connect

- Available for platforms, **not** for individual connected accounts
- Selected treatment/control applies to all eligible connected accounts
- Connected account's own PM preference (if they turn a PM on/off) **overrides** platform experiment for that account
- Can opt out specific account IDs during experiment creation

## Supported PMs (35 total)

All major PMs supported. Connect unsupported: ACH, ACSS, BECS, Bacs, Alipay, FPX, Konbini, SEPA Debit, WeChat Pay.

## Sources

- [[source-stripe-a-b-testing-payment-methods]] — primary: setup flow, metrics, statistical methodology, raw data dimensions, Connect rules, 35 PM support table
