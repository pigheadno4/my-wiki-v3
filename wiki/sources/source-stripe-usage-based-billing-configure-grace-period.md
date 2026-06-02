---
title: "Stripe: Configure an Invoice Finalization Grace Period"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-configure-grace-period-2025.md"
tags: [stripe, billing, usage-based, invoicing, grace-period, finalization]
---

## Summary

Covers the invoice finalization grace period for usage-based billing: default behavior, how to configure it globally or per rule, and how usage timestamps interact with draft invoices.

## Key Details

**Default grace period**: 1 hour. Configurable up to **72 hours (3 days)**. Set via Dashboard → Invoice settings → Invoice finalization grace period. Do not exceed your service period length (e.g., no ≥24-hour grace on daily billing).

**Cycling vs threshold invoices**:
- **Cycling invoices** (end-of-period): include usage reported during the grace period.
- **Threshold invoices**: reflect only usage up to the creation moment — grace period doesn't apply.

**Rules system**: per-group grace period overrides with conditions:
- "Invoice is from a subscription cycle"
- "Has a metered price"
- Both (AND)

When multiple rules match an invoice, Stripe applies the most conservative (longest) grace period.

**First subscription invoice exception**: always finalizes immediately, regardless of configured rules.

**Draft invoice usage behavior**:
- Usage timestamp must be within the service period of the draft invoice.
- Usage timestamped after the draft invoice's creation time goes to the *next* invoice.
- Verify added usage via Dashboard → Meters page or Meters API.

## Raw Sources

- [[stripe-usage-based-billing-configure-grace-period-2025]] — verbatim webpage content (54 lines)
