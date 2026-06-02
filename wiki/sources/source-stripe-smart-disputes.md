---
title: "Stripe — Smart Disputes"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-smart-disputes-2026.md"
tags: [stripe, disputes, smart-disputes, ai, evidence, automation]
---

## Summary

Smart Disputes automates evidence collection and submission for eligible card disputes using an AI rules engine. Fee is charged only on wins.

## How It Works

1. Eligible dispute received → Stripe notifies via email + Dashboard
2. AI rules engine extracts evidence from Stripe internal data, transaction data, cardholder data
3. Evidence tailored to dispute reason code
4. Auto-submitted just before dispute deadline (if merchant takes no action)

**Merchant can override**: counter manually or accept before deadline. Auto-submit can be disabled at Dashboard → Dispute settings.

## Eligibility Factors

Dispute reason code, payment method, evidence availability, evidence relevance, cost.

## Pricing

**Fee only on wins** — no Smart Disputes fee on lost disputes. See [Stripe pricing](https://stripe.com/pricing).

## Key Constraints

- Merchant responsible for accuracy/completeness of transaction data used in evidence
- Not a replacement for professional dispute advice — review each dispute individually
- No integration required (built into Stripe)

## Related Pages

- [[disputes]] — concept page (updated with Smart Disputes fee model)
- [[source-stripe-disputes-prevention]] — dispute prevention overview (Smart Disputes mentioned)

## Raw Sources

- [[stripe-disputes-smart-disputes-2026]] — verbatim Smart Disputes overview (4 images)
