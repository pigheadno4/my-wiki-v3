---
title: "Stripe Terminal: Configure Cellular Network"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-cellular-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, cellular, s710]
---

## Summary

Enable cellular connectivity on the Stripe Reader S710 via the Configuration object. Cellular is a WiFi fallback — device uses cellular only when WiFi is unavailable. Disabled by default per location.

## Key Details

**S710 only** — no other readers support cellular configuration.

**Billing**: monthly cellular usage fee applies if cellular was enabled at any point during the calendar month.

**API**: `cellular: { enabled: true }` on the Configuration object. Enable per location; register reader to that location to activate.

## Raw Sources

- [[stripe-terminal-cellular-config-2025]] — verbatim webpage content
