---
title: "Stripe — Risk Settings and Risk Controls"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-risk-settings-2026.md"
tags: [stripe, radar, risk-settings, risk-controls, fraud, adaptive-3ds, fraudulent-dispute, early-fraud-warning, risk-score]
---

## Summary

Three preset risk settings automatically tune blocking thresholds across four risk controls. Five Radar scores underlie these controls, with the legacy risk score being deprecated.

## Risk Settings (3 presets)

| Setting | Priority |
| --- | --- |
| Maximize protection | Block payments likely to result in EFWs |
| Balance risk and revenue | Default middle ground |
| Maximize revenue | Block only high-risk payments |

Estimated impact shown as Fraud saved + Payments accepted, based on 4 months of data.

**Migration** (from March 1, 2026): Radar for Fraud Teams moving to risk settings from legacy risk score thresholds. Selecting a risk setting disables the `Block if :risk_level: = 'highest' default` rule.

**Manual mode**: When Fraud Teams user sets a custom Fraudulent dispute threshold that doesn't match a preset.

## Risk Controls (4)

| Control | Signal used | Notes |
| --- | --- | --- |
| Fraudulent dispute | `fraudulent_dispute_score` | Backtest available (Fraud Teams); custom threshold available |
| Early fraud warning | `early_fraud_warning_score` | Maximize protection setting only; recommended if in VAMP |
| Adaptive 3DS | ML model | Liability shift on authenticated payments; SCA compliance overrides disable |
| Fraudulent non-card payments | Stripe risk attributes | Auto-enabled by default; covers LPMs |

Custom rules are never overridden by risk settings or controls.

## Radar Scores (5)

| Score | Range | Applies to | Rule attribute | Status |
| --- | --- | --- | --- | --- |
| Fraudulent dispute score | 0–99 | Cards, ACH, SEPA | `:fraudulent_dispute_score:` | Active |
| Early fraud warning score | 0–99 | Cards only | `:early_fraud_warning_score:` | Active |
| Bot score | 0–99 | Checkout only | `:bot_score:` | Private preview |
| Risk score | 0–99 | Cards, ACH, SEPA | `:risk_score:` | **Deprecated** |
| Overall risk level | Normal/Elevated/Highest | — | `:risk_level:` | Active (max of other scores) |

Overall risk level = max(fraudulent_dispute_score, EFW_score, risk_score) — separate from `:risk_level:` rules attribute.

## Related Pages

- [[stripe-radar]] — concept page (updated with risk settings and scores)
- [[source-stripe-radar-risk-evaluation]] — risk level outcomes on Charge.outcome
- [[stripe-3d-secure]] — 3DS adaptive authentication

## Raw Sources

- [[stripe-radar-risk-settings-2026]] — verbatim risk settings and controls reference
