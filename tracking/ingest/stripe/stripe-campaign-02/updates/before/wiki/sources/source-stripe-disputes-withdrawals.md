---
title: "Stripe — Dispute Withdrawals"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-withdrawals-2026.md"
tags: [stripe, disputes, chargebacks, withdrawal, friendly-fraud]
---

## Summary

Guide to handling cardholder dispute withdrawals: what they mean, strategy for pursuing them, evidence requirements, and late withdrawal behavior.

## Key Rules

- **Withdrawn ≠ won**: withdrawing doesn't guarantee a win — must still submit evidence or issuer may treat silence as acceptance of liability
- **Withdrawn disputes still count** against dispute rate; don't resolve faster; don't appear differently in Dashboard/API
- **Only chargebacks can be withdrawn**: EFWs and inquiries cannot be withdrawn (no financial impact on those)
- **Refunds blocked**: cannot refund a disputed charge until issuer decides in your favor — even if customer verbally agreed to withdraw

## Strategy by Dispute Type

| Situation | Recommended action |
| --- | --- |
| High likelihood of winning | Submit evidence directly, skip customer outreach |
| Low value dispute | Accept the dispute |
| Mid-range / relationship matters | Pursue withdrawal: contact customer → resolve → ask them to call issuer |

## Evidence Requirements

- **Always submit evidence** even if customer says they're withdrawing — many issuers treat no-evidence as liability acceptance
- Evidence is one-shot only — time submission carefully (wait for customer conversation, but don't miss deadline)
- Withdrawal confirmation from customer (bank email, screenshot) is helpful but not required

## Late Withdrawals

- All card networks allow withdrawal after response deadline, even after a lost dispute
- Not governed by network rules — outside the regular lifecycle
- Timeline to reflect in Stripe: weeks to months after cardholder contacts issuer

## Related Pages

- [[disputes]] — concept page (updated with withdrawal details)
- [[source-stripe-disputes-how-disputes-work]] — dispute lifecycle and timing
- [[source-stripe-disputes-responding]] — evidence submission

## Raw Sources

- [[stripe-disputes-withdrawals-2026]] — verbatim Stripe dispute withdrawals guide
