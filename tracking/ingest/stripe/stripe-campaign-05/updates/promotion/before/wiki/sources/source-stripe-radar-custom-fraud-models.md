---
title: "Stripe — Custom Fraud Models"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-custom-fraud-models-2026.md"
tags: [stripe, radar, custom-fraud-model, metadata, machine-learning, fraud-detection]
---

## Summary

Custom fraud models extend Radar's global model with business-specific metadata signals. Trained per merchant, no integration changes after setup.

## Benefits

- Catch fraud that looks normal globally but anomalous for your traffic
- Approve transactions that look risky globally but are typical for your business
- Improve precision/recall (fewer false positives)

## Requirements

- Structured metadata on PaymentIntent objects
- Sufficient payment volume (evaluated at onboarding)

## How It Works

1. Attach metadata to payments via `PaymentIntent.metadata` (no extra code needed)
2. Stripe trains custom model on your traffic + global signals
3. Custom risk score deployed — no integration changes
4. Model retrains as business evolves

## High-Impact Metadata Types

| Signal | Examples |
| --- | --- |
| User signals | Account age, verification status, VIP flag |
| Behavioral | Session duration, time from login to checkout, interaction frequency |
| Product context | Product category, item value tier, shipping method |
| Risk indicators | Internal risk scores, usage-to-payment ratios |

## Related Pages

- [[stripe-radar]] — concept page (updated with custom fraud models)
- [[source-stripe-radar-optimize-risk-factors]] — risk factor data quality

## Raw Sources

- [[stripe-radar-custom-fraud-models-2026]] — verbatim custom fraud models overview
