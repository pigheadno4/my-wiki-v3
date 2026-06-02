---
title: "Stripe Terminal: Configure Offline Mode"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-offline-mode-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, offline]
---

## Summary

Enable or disable offline mode via the Configuration object (same account→location hierarchy as other configurations). Propagation: 10 minutes.

**API**: `configurations.create/update({ offline: { enabled: true } })`

See [[source-stripe-terminal-offline-payments]] and [[source-stripe-terminal-offline-collect-card-payments]] for offline payment behavior and integration details.

## Raw Sources

- [[stripe-terminal-offline-mode-config-2025]] — verbatim webpage content
