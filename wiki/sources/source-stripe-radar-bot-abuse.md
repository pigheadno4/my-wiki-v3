---
title: "Stripe — Bot Abuse Prevention"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-bot-abuse-2026.md"
tags: [stripe, radar, bot, bot-score, abuse, checkout, sigma, rules]
---

## Summary

Radar assigns a bot score (0–99) to Stripe Checkout payments to detect bot-driven payment attempts. Not a fraud signal — use for anti-bot/anti-scripting policies.

## Bot Score

- Range: 0–99 (higher = more likely bot-made)
- Available only for **Stripe Checkout** payments
- High score ≠ fraudulent; bot may not be malicious — use to enforce anti-scripting policies

## Access

| Method | Detail |
| --- | --- |
| Dashboard | Payment details → Risk scores section |
| Sigma | `radar_abuse_prevention_attributes.bot_score` |
| Radar rules | Custom rule on `:bot_score:` with threshold |

## Related Pages

- [[stripe-radar]] — concept page (updated with bot abuse section)

## Raw Sources

- [[stripe-radar-bot-abuse-2026]] — verbatim bot abuse prevention guide
