---
title: "Managed Payments Changelog"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-changelog-2026.md"
tags: [stripe, managed-payments, merchant-of-record, changelog, timeline]
---

## Summary

Chronological changelog for Managed Payments. Key milestones: general availability (April 2026, 39 countries), one-time payments (Sep 2025), in-app payments (Sep 2025), Adaptive Pricing (Feb 2026), Radar support (Aug 2025).

## Timeline

### April 22, 2026 — General Availability

- **39 countries** (Australia added)
- Payment Links support added
- Invoice Items + Subscription Items with eligible categories now supported
- Business name now shown on invoices (previously only "Sold through Link")
- Trial subscription confirmation email added
- Additional tax codes eligible

### February 9, 2026

- 15 payment methods supported
- Subscription schedules support
- Free trials without collecting payment method: `payment_method_collection: 'if_required'`; customer gets email with hosted form before trial ends
- Adaptive Pricing for one-time + subscription payments
- `hosted_invoice_url` returned in Invoice objects
- One-off invoices outside billing period explicitly blocked

### November 11, 2025

- New Dashboard Settings page: status, usage metrics, Tax settings

### October 7, 2025

- `saved_payment_method_options` parameter available

### September 22, 2025

- **One-time payments** supported (`mode: 'payment'`)
- **In-app payments** (`origin_context: 'mobile_app'`)
- **Link account no longer required** — guests can checkout; receipt email contains URL to link transaction to Link account; phone number no longer required
- 21 new tax codes added (video games, audio works, AV works, artwork, website advertising, bundles)

### August 22, 2025

- `customer_update[address]` and `customer_update[name]` removed — Managed Payments always collects and updates customer name + billing address (needed for tax calculation)
- Website Information Services tax codes added (`txcd_10701400`, `txcd_10701401`)

### August 15, 2025

- **Radar for Fraud Teams** supported — custom fraud rules (country blocking, 3DS forcing) apply on top of Managed Payments default fraud prevention

### August 13, 2025

- Refunded sales tax clarification: Stripe only retains original tax where required (not all refunded transactions); Payment breakdown shows refunded tax amount

## Key Feature Rollout Dates

| Feature | Date |
| --- | --- |
| GA (39 countries incl. Australia) | 2026-04-22 |
| Payment Links | 2026-04-22 |
| Subscription schedules | 2026-02-09 |
| Free trials without PM | 2026-02-09 |
| Adaptive Pricing | 2026-02-09 |
| One-time payments | 2025-09-22 |
| In-app payments | 2025-09-22 |
| Link account no longer required | 2025-09-22 |
| Radar for Fraud Teams | 2025-08-15 |

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[source-stripe-managed-payments-overview]] — overview

## Raw Sources

- [[stripe-managed-payments-changelog-2026]] — verbatim changelog (~138 lines, 1 image)
