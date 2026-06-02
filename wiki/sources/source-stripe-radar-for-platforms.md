---
title: "Stripe — Radar for Platforms"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-for-platforms-2026.md"
tags: [stripe, radar, connect, platforms, connected-accounts, risk, reserves, identity-verification]
---

## Summary

Radar for Platforms extends Radar to Connect platforms: transaction risk + connected account risk scoring, investigation tools, identity verification requests, and account actions (reject/reserves).

## Connected Account Risk Scores

| Level | Score | Probability of platform loss |
| --- | --- | --- |
| `highest` | ≥90 | >90% |
| `elevated` | 50–89 | 50–89% |

Scores update on every new event (transaction, business info change). Indicators explain the risk level.

## API Signals (Private Preview)

- Account fraud signal — fraudulent activity (misrepresentation, unauthorized transactions)
- Account insolvency signal — financial distress indicators
- Fraudulent website signal — deceptive websites

## Rules

**Transaction rules**: Request 3DS, Allow, Block, Review (same as other Radar tiers).

**Connected account rules**: Raise review OR Pause payouts + raise review.

## Investigation Tools (Risk Tab)

- Agent-generated risk indicators (suspicious network connections, business info mismatches, location mismatches)
- Risk metrics: time-series of payments/disputes/declines/refunds, dispute/refund/failure rates
- Risk history with note-taking

## Identity Verification Request

Request gov ID + selfie → set enforcement (pause payouts or payouts+payments) → set deadline (time or volume limit) → send remediation link.

## Actions on Connected Accounts

- Pause payments, pause payouts
- Reject (with reason code — 7 options: fraud_card_casher, fraud_card_tester, fraud_no_intent_to_fulfill, fraud_other, credit, terms_of_service, other)
- Set reserves
- Dismiss review (timed — re-evaluates later)

> Rejection is hard to reverse — requires Stripe Support to un-reject.

## Platform Payment Controls

| Mode | Behavior |
| --- | --- |
| Platform only | Platform rules apply to all payments incl. direct charges; connected accounts can't manage Radar |
| Both | Platform rules run first; connected accounts can also set their own rules |

## Permissions

Connect Risk Analyst role required to view/act on risk reviews. Risk Analysts receive email notifications for `elevated`/`highest` accounts; Admins can opt in.

## Related Pages

- [[stripe-radar]] — concept page (updated with Platforms section)
- [[source-stripe-radar-how-it-works]] — Radar tiers overview

## Raw Sources

- [[stripe-radar-for-platforms-2026]] — verbatim Radar for Platforms guide
