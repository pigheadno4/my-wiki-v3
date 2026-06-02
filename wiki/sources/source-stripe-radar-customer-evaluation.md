---
title: "Stripe — Multi-Account and Account Sharing Abuse Evaluation"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-customer-evaluation-2026.md"
tags: [stripe, radar, customer-evaluation, multi-accounting, account-sharing, fraud, registration, login, upfunnel]
---

## Summary

Customer Evaluation API provides upfunnel fraud signals at registration and login — before any payment is collected. Detects multi-accounting and account sharing abuse.

## Two Abuse Signals

| Signal | Event type | Detects |
| --- | --- | --- |
| `multi_accounting` | `registration` | Same actor registering multiple accounts |
| `account_sharing` | `login` | Same account used from multiple locations simultaneously |

## Score and Risk Level

Score 0–100. Risk levels same as payment evaluation:

| Risk level | Score | Action |
| --- | --- | --- |
| `highest` | 75–100 | Block or require additional verification |
| `elevated` | 65–74 | Apply friction or review |
| `normal` | 0–64 | No additional action |

## API Flow

1. Client: `stripe.createRadarSession()` → get Radar Session token
2. Server: `POST /v1/radar/customer_evaluations` with `event_type`, `customer`, `radar_session`
3. Stripe returns signal + score + risk_level
4. Report outcome: `POST .../report` with `registration_success|failed` or `login_success|failed`
5. At payment time: use **same Customer ID** (required to connect registration/login/payment history)

**Preview API**: requires `Stripe-Version: 2026-03-04.preview` header.

## Critical Constraint

The `customer` parameter at payment time must match the Customer ID used in `CustomerEvaluation`. This connects all signals across the customer lifecycle.

## Related Pages

- [[stripe-radar]] — concept page (updated with Customer Evaluation API)
- [[source-stripe-radar-sessions]] — Radar Sessions (prerequisite for Customer Evaluation)

## Raw Sources

- [[stripe-radar-customer-evaluation-2026]] — verbatim Customer Evaluation API guide
