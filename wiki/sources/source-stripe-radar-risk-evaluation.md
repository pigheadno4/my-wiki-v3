---
title: "Stripe — Radar Risk Evaluations"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-risk-evaluation-2026.md"
tags: [stripe, radar, risk-score, risk-level, fraud-detection, outcome, charge, paymentintent, setupintent]
---

## Summary

Complete reference for Radar risk levels, score thresholds, `Charge.outcome` API fields, Radar object support matrix, and feedback mechanism.

## Risk Score Thresholds (Radar for Fraud Teams)

Score range: 0–99. Default thresholds:
- ≥75 → high risk
- ≥65 → elevated risk
- <65 → normal risk

## Risk Levels and `Charge.outcome` Fields

| Level | `risk_level` | Default behavior | `outcome.type` | Example score |
| --- | --- | --- | --- | --- |
| High | `highest` | **Blocked** by default | `blocked` | 92 |
| Elevated | `elevated` | Allowed; auto-reviewed (Fraud Teams) | `manual_review` | 68 |
| Normal | `normal` | Allowed | `authorized` | 23 |
| Not evaluated | `not_assessed` | Allowed | `authorized` | — |
| Unknown | `unknown` | Allowed (error state) | `authorized` | — |

`risk_score` field available only with Radar for Fraud Teams.

`not_assessed` applies to: non-card/ACH/SEPA payments, pre-risk-level card payments, opted-out businesses.

## Radar API Object Support

| Object | 3DS | Allow/Block | Review |
| --- | --- | --- | --- |
| Charge | ✗ | ✓ | ✓ |
| PaymentIntent | ✓ | ✓ | ✓ |
| SetupIntent | ✓ | ✓ | ✗ |

Enable Radar for SetupIntents: Dashboard → Radar settings.

## Stripe Billing

Radar only **scores** the first payment of a recurring subscription; evaluates rules for all payments.

## Network Coverage

- 92% chance Stripe has seen the card before
- 82% chance Stripe has seen the SEPA account
- 71% chance Stripe has seen the ACH account

## Feedback to Improve Model

Report fraudulent payments: refund with `reason: 'fraudulent'` (API) or select Fraudulent in Dashboard. Adds email + card fingerprint to block lists. AI model learns from this feedback.

## Allow List

If a high-risk payment is legitimate: Dashboard → payment → **Add to allow list**. Does not retry payment. Prevents future blocks for that payment method or email.

## Related Pages

- [[stripe-radar]] — concept page (updated with risk levels + score thresholds)
- [[stripe-declines]] — `Charge.outcome` object for decline types
- [[source-stripe-radar-how-it-works]] — Radar overview

## Raw Sources

- [[stripe-radar-risk-evaluation-2026]] — verbatim Radar risk evaluations reference
