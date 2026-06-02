---
title: "Stripe — Pay-As-You-Go Abuse Evaluation"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-payg-abuse-2026.md"
tags: [stripe, radar, payg, usage-based, subscriptions, non-payment-abuse, payment-evaluation]
---

## Summary

Radar Payment Evaluation API signal for detecting intentional non-payment abuse on usage-based subscriptions. Run mid-billing cycle as a background job, not at checkout.

## Use Case

Post-paid / usage-based billing (e.g. bill at month-end). Evaluate subscriptions mid-cycle to detect customers likely to not pay their next invoice. Actions: manual review, early invoice, or limit access.

## API

`POST /v1/radar/payment_evaluations` with:
- `customer_presence=off_session`, `payment_type=recurring`
- Payment method, customer, expected invoice amount
- No Radar Session required
- `Stripe-Version: 2026-03-25.dahlia`

Key response field: **`signals.non_payment_abuse.risk_level`**

Note: `signals.fraudulent_payment` returns default values (-1.0) — ignore it. `recommended_action` is evaluation-level, not signal-level.

## Risk Levels

| Level | Action |
| --- | --- |
| `normal` / `low` | No action needed |
| `elevated` | Manual review or usage limits |
| `highest` | Pause usage or require prepayment |
| `not_assessed` / `unknown` | Not applicable |

## Key Behaviors

- **Fail-open**: 4xx/5xx doesn't affect billing flow — retry or proceed without signal
- **No outcome reporting required**
- Test card: `4000000000004954` / `pm_card_riskLevelHighest` → `highest`

## Related Pages

- [[stripe-radar]] — concept page (updated with PAYG abuse evaluation)
- [[source-stripe-radar-free-trial-abuse]] — free trial abuse (related upfunnel risk control)

## Raw Sources

- [[stripe-radar-payg-abuse-2026]] — verbatim PAYG abuse evaluation guide
