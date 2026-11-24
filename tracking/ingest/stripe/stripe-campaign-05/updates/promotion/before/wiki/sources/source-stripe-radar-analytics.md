---
title: "Stripe — Radar Analytics Center"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-analytics-2026.md"
tags: [stripe, radar, analytics, fraud, disputes, benchmarks, monitoring-programs, sigma]
---

## Summary

Radar analytics center in the Dashboard: fraud/dispute/block rate charts with peer benchmarks, rule match breakdowns, and legacy overview. 24-hour data delay.

## New Analytics Center (Default)

**Rate charts**: Fraud, Disputes, Blocks — each with benchmark comparison icon vs comparable Stripe businesses.

**Configurable data set**:
- Calculate by transaction volume vs payment count
- Calculate fraud rates by fraud arrival date vs payment date
- De-duplicate retries per payment intent
- Include SetupIntents

**Fraud panel**: disputes vs EFWs breakdown; worst-case fraud rate AI estimate toggle (disabled if low volume or using fraud arrival date mode).

**Rule matches**: totals + detail by Blocked (top rules), 3DS (outcomes), Allow (legitimate/disputed/refunded), Review (in review/approved/rejected/failed/disputed).

**Monitoring programs**: tracks rates vs card network thresholds; shows current status.

## Legacy Overview

- **Overview Chart**: 3DS → Screened by Radar → Disputed flow
- **Benchmarks**: Block rate, fraudulent dispute rate, estimated false positive rate vs regional + similar businesses
- **Fraud prevention**: attempted payments, blocked (high-risk vs rules), block rate; false positive rate estimate
- **Fraudulent disputes chart**: partial rate (solid) + projected maximum (dashed, 120-day window)
- **Disputes section**: disputes received by type; win rate
- **Manual reviews**: sent to review + outcomes (approved/refunded/disputed)

## Data Details

- 24-hour delay; computed daily at midnight UTC
- New view defaults to prior 30 days; legacy defaults to 6 months
- Each chart has CSV download + View in Sigma link
- Benchmarks: ≥dozens of businesses per cohort; each business gets 1 vote (opt-out available)

## Related Pages

- [[stripe-radar]] — concept page (updated with analytics section)
- [[stripe-dispute-monitoring-programs]] — monitoring program thresholds
- [[source-stripe-disputes-measuring]] — dispute activity vs rate

## Raw Sources

- [[stripe-radar-analytics-2026]] — verbatim Radar analytics center guide (299 lines, 8 screenshots)
