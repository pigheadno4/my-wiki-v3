---
title: "Stripe — Free Trial Abuse Prevention"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-free-trial-abuse-2026.md"
tags: [stripe, radar, free-trial, abuse, subscriptions, risk-controls, checkout, sigma]
---

## Summary

Radar risk control that blocks high-risk free trial starts before customers gain product access. Predicts whether subscription payment will fail when trial ends.

## Common Abuse Patterns

- Prepaid or virtual cards
- Same card used across multiple accounts for repeated free trials

## How It Works

Radar evaluates payment method at trial start and predicts if subscription payment will fail when trial ends. If high risk → trial blocked before access granted.

## Setup

**Recommended (zero code changes)**:
- Checkout Sessions in `subscription` mode

**Also auto-detected**:
- `subscription_data.trial_period_days` or `trial_end` on Checkout Session
- 100% off coupons for trials

**Manual setup needed** (contact Stripe):
- SetupIntents API, PaymentIntents API, Subscriptions API — requires adding metadata

**Enable**: Dashboard → Risk controls → Free trial abuse. Backtesting data available before enabling.

## Monitoring

Dashboard → Risk controls page (blocked trial starts).

Sigma query:
```sql
SELECT * FROM rule_decisions
WHERE rule_id = 'block_if_high_free_trial_abuse_risk'
```

## Related Pages

- [[stripe-radar]] — concept page (updated with free trial abuse control)
- [[source-stripe-radar-how-it-works]] — Radar overview

## Raw Sources

- [[stripe-radar-free-trial-abuse-2026]] — verbatim free trial abuse prevention guide
