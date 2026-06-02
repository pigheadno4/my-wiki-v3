---
title: "Stripe Terminal: Place Hardware Orders"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-order-and-return-readers-2025.md"
tags: [stripe, stripe-terminal, hardware, fleet, orders, returns, api, shipping]
---

## Summary

Complete guide for ordering, tracking, and returning Terminal readers via Dashboard or Hardware Orders API (preview).

## Key Details

**Ordering**: Dashboard (Terminal → Shop) or Hardware Orders API (preview; requires Account Manager + monthly invoice billing). Up to 10,000 units per order. Volume discounts via sales.

**Order statuses**: Pending (cancelable ≥30 min) → Ready to ship (no longer cancelable) → Shipped → Delivered. Also: Canceled, Undeliverable.

**Shipping**: physical addresses only; standard/express/priority by country; signature required above thresholds (500 USD US, 400 EUR most EU); freight auto-selected for large orders; Connect platforms can ship to connected account addresses.

**Self-service returns** (33 countries including US/CA/GB/AU/EU): 30-day window, original packaging, first-return shipping fee refund only, ≤10 day credit card refund, flow in Dashboard.

**Permissions**: Support Specialist and View Only cannot place/cancel orders; View Only cannot initiate self-service returns.

**Hardware Orders API**: beta header `Stripe-Version: 2026-04-22.dahlia;terminal_hardware_orders_beta=v5`. SKUs are country-specific; query dynamically (can become unavailable). Preview endpoint validates without creating. 6 webhook events. v5 is current (v1–v3 deprecated).

## Raw Sources

- [[stripe-terminal-order-and-return-readers-2025]] — verbatim webpage content (includes shipping table for 37 countries, API changelog v1–v5)
