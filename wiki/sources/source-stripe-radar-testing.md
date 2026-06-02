---
title: "Stripe — Testing Stripe Radar"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-testing-2026.md"
tags: [stripe, radar, testing, sandbox, test-cards, risk-level, backtesting]
---

## Summary

Test cards/tokens/PaymentMethods for specific Radar risk levels, and rule backtesting framework for evaluating rule impact before enabling.

## Test Cards by Risk Level

| Risk level | Card | Token | PaymentMethod | Notes |
| --- | --- | --- | --- | --- |
| `highest` (rules apply) | `4000000000004954` | `tok_riskLevelHighest` | `pm_card_riskLevelHighest` | Blocked only if block rule is enabled |
| `highest` (always blocked) | `4100000000000019` | `tok_chargeDeclinedFraudulent` | `pm_card_chargeDeclinedFraudulent` | Blocked regardless of rules |
| `elevated` | `4000000000009235` | `tok_riskLevelElevated` | `pm_card_riskLevelElevated` | Placed in review by default |

## Rule Backtesting

Before enabling, rule testing searches last 6 months of live mode historical payments. Shows:
- Disputes and EFWs
- Refunded payments
- Blocked and failed payments
- Succeeded payments
- **Overrides** (for allow rules): previously blocked payments that would now be allowed

## When to Implement Each Rule Type

| Rule type | Implement if… |
| --- | --- |
| Block | Matches fraud/EFW/refund payments at acceptable false-positive cost; or blocks high-failure payments hurting auth rates |
| Review | Matches fraud/EFW/refund payments for closer human inspection |
| Request 3DS | Matches fraud payments at acceptable false-positive cost (3DS doesn't guarantee challenge) |
| Allow | Matches previously-blocked payments with high confidence they're legitimate; few Overrides |

## Related Pages

- [[stripe-radar]] — concept page (updated with test cards)
- [[source-stripe-radar-rules]] — rule creation and testing workflow

## Raw Sources

- [[stripe-radar-testing-2026]] — verbatim Radar testing guide (+ backtesting screenshot)
