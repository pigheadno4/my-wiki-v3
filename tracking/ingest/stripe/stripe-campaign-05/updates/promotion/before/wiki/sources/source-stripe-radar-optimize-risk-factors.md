---
title: "Stripe — Optimize Radar Risk Factors"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-optimize-risk-factors-2026.md"
tags: [stripe, radar, fraud, risk-factors, stripe-js, customer-object, radar-sessions, advanced-risk-factors]
---

## Summary

How to maximize Radar effectiveness by providing the right data. Quantified impact of each risk factor type and integration tier ranking.

## Risk Factor Impact (Estimated Model Improvement)

| Data | Improvement |
| --- | --- |
| Advanced risk factors (device signals via Stripe.js/SDKs/Radar Sessions) | **+36%** |
| IP address | **+12%** |
| Customer email | **+11%** |
| Customer name | **+3%** |
| Billing address | **+1%** |

## Three Risk Factor Types

| Type | What it is | How to send |
| --- | --- | --- |
| Advanced | Device characteristics, browser signals, activity indicators | Stripe.js, mobile SDKs, or Radar Sessions |
| Customer | Email, name, billing address | Customer object in API |
| Client | IP address, user-agent, checkout URL | PaymentIntent object |

## Integration Completeness Ranking (Best → Worst)

1. Payment Links (Recommended)
2. Checkout (Recommended)
3. Elements + customer risk factors (Recommended)
4. Direct API + Radar Sessions + customer risk factors
5. Direct API + client + customer risk factors
6. Direct API + client risk factors only
7. Direct API + customer risk factors only
8. Direct API with no additional risk factors

## Best Practices

- **Stripe.js on every page** (not just checkout) — captures browsing behavior signals
- **Customer object**: attach email, name, billing address, shipping address; store multiple payment methods; Stripe tracks cross-payment-method fraud history
- **Radar Sessions**: for direct API integrations not using Stripe.js or SDKs
- **SetupIntents**: Radar doesn't scan by default — enable "Use Radar on payment methods saved for future use" in Radar settings
- **Privacy policy**: disclose that Stripe collects device/behavior data for fraud detection

## Related Pages

- [[stripe-radar]] — concept page (updated with risk factor impact table)
- [[source-stripe-radar-how-it-works]] — Radar overview

## Raw Sources

- [[stripe-radar-optimize-risk-factors-2026]] — verbatim Radar risk factor optimization guide
