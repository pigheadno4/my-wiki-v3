---
title: "Stripe — Fraud Alerts"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-fraud-alerts-2026.md"
tags: [stripe, radar, fraud-alerts, monitoring, attack-detection]
---

## Summary

Stripe auto-detects unusual fraud patterns and notifies via email + Dashboard bell. Fraud Teams users get additional action options (Smart Refunds, controls, rules).

## Trigger

Significant shift in Radar risk score distribution → email + Dashboard bell notification → dedicated fraud alert investigation page.

## Alert Investigation Page Shows

- Risk trend charts (current period vs prior weeks)
- List of elevated-risk payments
- Volume and count of potentially fraudulent payments

## Actions by Tier

| Tier | Available actions |
| --- | --- |
| Radar | Review elevated payments; verify attack; upgrade to Fraud Teams |
| Radar for Fraud Teams | + Smart Refunds recommendations; enable fraud controls; adjust Radar rules |

## Best Practices

Act quickly → verify pattern vs business activity → look for common attributes (billing address/IP/card BIN) → take preventive action → monitor results.

## Related Pages

- [[stripe-radar]] — concept page (updated with fraud alerts)
- [[source-stripe-radar-risk-settings]] — fraud controls to enable
- [[source-stripe-radar-reviews]] — Smart Refunds (recommended refunds)

## Raw Sources

- [[stripe-radar-fraud-alerts-2026]] — verbatim fraud alerts guide
