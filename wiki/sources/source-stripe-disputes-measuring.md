---
title: "Stripe — Measuring Disputes"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-measuring-2026.md"
tags: [stripe, disputes, dispute-rate, dispute-activity, monitoring, radar, early-fraud-warnings]
---

## Summary

Two distinct dispute metrics in Stripe, their purposes, thresholds, and how EFWs factor into network monitoring programs.

## Two Metrics

| Metric | Calculation | Used for |
| --- | --- | --- |
| Dispute activity | Disputes by **dispute date** ÷ payments in same period | Card network monitoring programs |
| Dispute rate | Disputes by **charge date** ÷ payments | Fraud analysis; identifying problematic sales patterns |

**Example**: 1,000 payments in a week, 10 disputes received (only 3 from that week's payments):
- Dispute activity = 10/1,000 = **1%**
- Dispute rate = 3/1,000 = **0.3%**

**Dashboard locations**:
- Dispute activity: Dashboard → Analytics section
- Dispute rate: Dashboard → Radar for Fraud Teams page

## Thresholds and Monitoring

- **Industry standard**: >0.75% dispute activity = excessive
- Sudden spike or steep upward trend can trigger monitoring programs **before** reaching 0.75%
- All disputes (won or lost) count toward dispute rate
- Dispute rate mutable for dates <120 days old (new disputes still arriving)

## Predicted Dispute Activity

Stripe AI models predict future excessive dispute activity risk and alert proactively. Cannot predict which specific payments will be disputed.

## EFWs and VAMP

Early fraud warnings (EFWs) from Visa, Mastercard, and JCB are counted as a metric by networks — not just informational. Visa counts EFWs toward identification in the **VAMP monitoring program** (in addition to formal disputes).

## Related Pages

- [[disputes]] — concept page (updated with measuring metrics)
- [[stripe-high-risk-merchant-lists]] — MATCH/VMSS thresholds
- [[source-stripe-disputes-how-disputes-work]] — EFW details

## Raw Sources

- [[stripe-disputes-measuring-2026]] — verbatim Stripe measuring disputes page (3 chart images)
