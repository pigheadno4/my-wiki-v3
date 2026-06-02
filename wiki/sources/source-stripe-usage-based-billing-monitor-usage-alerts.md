---
title: "Stripe: Monitor Usage with Alerts"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-monitor-usage-alerts-2025.md"
tags: [stripe, billing, usage-based, meters, alerts, thresholds, monitoring]
---

## Summary

Hub page for UBB monitoring. Introduces two mechanisms — usage alerts (notify on meter threshold) and billing thresholds (trigger invoice on spend) — with key limitations for each. Links to detailed setup pages.

## Key Details

**Two monitoring mechanisms**:
- **Usage alerts** — notify when a customer exceeds a meter usage threshold. Use cases: email users, deprovision access, upsell sales team notification.
- **Billing thresholds** — trigger an invoice when a customer reaches a spend amount.

**Usage alert limits**:
- Max **25 alerts** per meter+customer combination
- Evaluation includes usage reported before the alert was created (retroactive)

**Billing threshold constraints**:
- Not applicable to trial subscriptions
- Not evaluated in last **24 hours** before subscription ends
- Monetary threshold must exceed sum of flat rates on usage-based items
- Monetary threshold value excludes taxes but **includes discounts and billing credits**
- One monetary threshold per subscription; one usage threshold per subscription item
- Per-package tiered pricing not supported
- Invoiced amount may slightly exceed threshold (not triggered at exact moment)

## Raw Sources

- [[stripe-usage-based-billing-monitor-usage-alerts-2025]] — verbatim webpage content (38 lines, hub page)
