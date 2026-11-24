---
title: "Stripe Terminal: Configure On-Reader Tips (Fleet)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-tipping-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, tipping]
---

## Summary

Fleet-level Configuration API for on-reader tipping. Set tipping options per currency via the Configuration object (same account→location hierarchy). Propagation: 10 minutes.

**3 tip types**: smart tips (dynamic), percentages, fixed amounts.

**API field**: `tipping: { usd: { percentages: [...], fixed_amounts: [...], smart_tip_threshold: ... } }` — keyed by currency code. `smart_tip_threshold` (in cents) determines when amounts vs percentages are shown.

For SDK-level tipping behavior and on-receipt tipping, see [[stripe-terminal-tipping]].

## Raw Sources

- [[stripe-terminal-tipping-config-2025]] — verbatim webpage content
