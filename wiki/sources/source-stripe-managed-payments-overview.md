---
title: "Managed Payments — Overview"
type: source
date_ingested: 2026-04-23
original_format: notes
raw_files:
  - "stripe-managed-payments-overview-2025.md"
tags: [stripe, managed-payments, merchant-of-record, tax-compliance, digital-goods, saas, fraud, disputes]
---

## Summary

Landing page overview for Stripe Managed Payments — Stripe's merchant of record (MoR) solution for selling digital products globally. Stripe assumes legal responsibility for indirect tax compliance, fraud, disputes, and transaction-level support.

## What It Is

Managed Payments = **Stripe as merchant of record** for digital product sales (SaaS, software, digital content/downloads). Stripe handles:

- **Indirect tax compliance**: sales tax, VAT, GST in 80+ countries
- **Fraud prevention**
- **Dispute management**
- **Transaction-level customer support**

## Comparison: Managed Payments vs Other Stripe Products

| Feature | Managed Payments | Other Stripe products |
| --- | --- | --- |
| Merchant of record | Stripe | Your business |
| Indirect tax compliance | ✓ (80+ countries) | Available with Stripe Tax |
| Checkout page | Checkout, Payment Links | Checkout, Elements, Invoice, Payment Links |
| Subscriptions | Available with Billing | Available with Billing |
| Fraud protection | | Radar |
| Dispute response | | Payments |
| Transaction-level support | ✓ | ✗ |
| Platform support | ✗ | Connect |

## Integration Paths

- Build a new Checkout integration with Managed Payments enabled
- Update existing Checkout integration
- Create Payment Links with Managed Payments
- Accept mobile app payments

## Unsupported Integrations

- Stripe Connect (platforms/marketplaces)
- Embeddable web components / advanced integrations (Elements)
- Invoice items on Customer object attached to Managed Payments subscription
- One-off invoices outside billing period
- Creating subscriptions outside Checkout or Payment Links
- Third-party tax integrations

## Related Pages

- [[stripe-managed-payments]] — concept page

## Raw Sources

- [[stripe-managed-payments-overview-2025]] — verbatim overview page (reformatted from pasted navigation page)
