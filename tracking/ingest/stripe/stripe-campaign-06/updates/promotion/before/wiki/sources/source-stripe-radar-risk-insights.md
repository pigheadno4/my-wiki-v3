---
title: "Stripe — Radar Risk Insights"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-risk-insights-2026.md"
tags: [stripe, radar, risk-insights, fraud-factors, related-payments, fraud-teams]
---

## Summary

Risk insights (Fraud Teams only) exposes the risk factors that drive Radar's AI score for each payment. Includes fraud factor numbers, top fraud factors, customer signals, geography, and related payments network.

## Key Features

### Fraud Factor Numbers
Per-risk-factor multiplier vs Stripe average. 3.5x = 3.5× more likely fraudulent than average. High-risk payments have some factors >1; low-risk have factors <1. Hover for network distribution data.

### Top Fraud Factors
Flags which specific factors are most suspicious. Note: Radar can still correctly identify fraud even when no single factor looks suspicious (complex pattern detection across hundreds of factors).

### Customer Signals
- Name/email match
- Email authorization rate on Stripe network (low rate = suspicious — prior declines suggest past fraud attempts)
- Geography: billing, shipping, IP address locations

### Related Payments
Other payments to your business sharing customer ID, IP, or card number. Helps identify:
- Card testing: many cards sharing one IP
- Trial abuse: many accounts sharing one card

## Constraints
- Available for **up to 6 months** of transaction history
- **Not available in sandbox**
- Requires email, IP, shipping address in integration for full data

## Related Pages

- [[stripe-radar]] — concept page (updated with risk insights)
- [[source-stripe-radar-reviews]] — review queue (risk insights shown in detailed view)
- [[source-stripe-radar-optimize-risk-factors]] — how to provide the data risk insights needs

## Raw Sources

- [[stripe-radar-risk-insights-2026]] — verbatim risk insights guide (5 screenshots)
