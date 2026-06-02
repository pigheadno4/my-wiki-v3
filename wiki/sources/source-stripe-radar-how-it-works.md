---
title: "Stripe — How Radar Works"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-how-it-works-2026.md"
tags: [stripe, radar, fraud, fraud-detection, rules-engine, risk, block-list, allow-list, 3ds]
---

## Summary

Overview of Stripe Radar's three product tiers, pricing model, supported payment methods, and six core features for real-time fraud protection.

## Product Tiers

| Tier | Target | Key capability |
| --- | --- | --- |
| Stripe Radar | All merchants | AI fraud detection, no dev time |
| Radar for Fraud Teams | High-volume / complex | Custom rules, risk insights, analytics |
| Radar for Platforms | Connect platforms | Transaction + account risk |

## Pricing

- Fee per evaluated transaction (all attempt types: successful, declined, blocked, flagged)
- **Stripe Billing exception**: only billed for first transaction of a recurring series (not subsequent)
- Radar for Platforms: additional connected account fee

## Supported Payment Methods

- Cards
- Wallets (card-backed only)
- ACH Direct Debit
- SEPA Direct Debit
- (Preview) Other payment methods

**Not screened**: SetupIntents for non-card payment methods.

## Core Features

| Feature | Description |
| --- | --- |
| AI fraud detection | Real-time risk scoring; enable risk controls to auto-block elevated/high-risk payments |
| Custom rules engine | Business-specific fraud rules; automatic responses to risk levels |
| Risk insights | Factors driving risk on each payment; suspicious pattern detection |
| 3DS integration | Trigger 3D Secure for high-risk card transactions via rules |
| Block/allow lists | Manage by user, email, IP, metadata, payment method |
| Real-time monitoring | View and respond to fraud as it happens |

## Related Pages

- [[stripe-radar]] — concept page
- [[stripe-declines]] — how Radar blocking appears in Charge.outcome
- [[stripe-3d-secure]] — 3DS triggered by Radar rules

## Raw Sources

- [[stripe-radar-how-it-works-2026]] — verbatim Stripe Radar overview
