---
title: "Stripe — Orchestration"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-orchestration-2026.md"
tags: [stripe, orchestration, multi-processor, routing, retries, payment-routing, private-preview]
---

## Summary

Private preview product enabling rule-based payment routing across multiple external processors. Stripe acts as the orchestration layer while third-party processors remain processor of record for routed payments.

## Features

1. **Multi-processor routing**: Route via PaymentIntents or auto-route from Billing, Checkout, Payment Links, Dashboard
2. **Retry on different processor**: Rules to automatically retry failed payments with alternative processors
3. **Performance monitoring**: Analyze payments performance across processors
4. **Post-transaction flows**: Refunds via Stripe Dashboard or API; third-party processors administer their own refunds
5. **Sandbox testing**: Test rules before activating in production

## Supported Products

Payments, Billing, Dashboard payments (card only).

## Not Supported

Non-card payments, Link, Capital, Connect, Terminal, Organizations, Radar (third-party routed payments), Sigma, disputes, settlement-related activity.

## Key Rule

Third-party processor remains processor of record — their payment processing fees and liability terms continue to apply.

## Related Pages

- [[stripe-orchestration]] — concept page
- [[stripe-vault-and-forward]] — complementary: forwards card data (PANs) to external processors (different use case)
- [[stripe-off-session-payments]] — multi-processor routing also available via Off-Session Payments API

## Raw Sources

- [[stripe-orchestration-2026]] — verbatim Orchestration overview (39 lines)
