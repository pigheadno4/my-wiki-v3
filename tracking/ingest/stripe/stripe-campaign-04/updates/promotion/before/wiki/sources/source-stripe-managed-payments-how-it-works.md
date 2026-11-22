---
title: "How Managed Payments Works"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-how-it-works-2025.md"
tags: [stripe, managed-payments, merchant-of-record, link, adaptive-pricing, payment-methods, transaction-support, data-deletion]
---

## Summary

Full operational details of Managed Payments: customer flow, Link as customer-facing MoR, subscription email rules, payment method availability, refund tax handling, 48-hour support response rule, and data deletion.

## What Stripe Handles (MoR Responsibilities)

| Area | Details |
| --- | --- |
| Tax compliance | 80+ countries; auto calculate/collect/file/remit |
| Checkout optimizations | Link + Adaptive Pricing enabled by default |
| Transaction emails | Sent from Link (not your Dashboard settings) |
| Order/transaction support | Link support handles; seller escalated within 48h |
| Fraud prevention | AI + Radar; Stripe manages rules and blocklists |
| Dispute management | Smart Disputes auto-submits evidence |

## Link as Customer-Facing MoR

- Customers see **"Sold through Link"** as the merchant
- Statement descriptor: `LINK.COM* [Your statement descriptor]`
- Receipts, invoices, refund notifications sent **from Link** — your Dashboard receipt settings don't apply
- Customers manage orders (history, cancel/update subscriptions, update PM, billing address) via [link.com](https://link.com)

## Key Operational Rules

### 48-Hour Support Response
If Stripe escalates a support issue and you don't respond within **48 hours**, Stripe may issue a refund without your approval.
> Keep support email current in Dashboard → Settings → Business details.

### Refund Tax Handling
Refund = full amount including tax to customer. But in certain jurisdictions, Stripe retains and remits the original sales tax → your account balance is reduced by that tax amount.

### Subscription Renewal Email Schedule (Mandatory Regardless of Dashboard Setting)
- **AU/UK**: 6-month + 12-month anniversary
- **All others**: 12-month anniversary or as required by local law
- **Monthly-or-less frequent**: 30 days before renewal (or local law requirement)
- **More frequent than monthly**: 7 days before renewal

### Data Deletion
When a customer requests deletion, Stripe:
- Cancels their Managed Payments subscriptions
- Deletes data from: v2 Account, Customer, PaymentMethod, Invoice, PaymentIntent, Subscription, Charge objects in your Stripe account
- Sends you an email notification

## Payment Method Availability

| Method | Buyer countries | One-time | Recurring | Local currency required | Adaptive Pricing |
| --- | --- | --- | --- | --- | --- |
| Cards | Global | ✓ | ✓ | No | ✓ |
| Apple Pay | Global | ✓ | ✓ | No | ✓ |
| Google Pay | Global | ✓ | ✓ | No | ✓ |
| Link | Global | ✓ | ✓ | No | ✓ |
| Klarna | Global | ✓ (one-time only¹) | ✗ | Yes | ✗ |
| Cash App Pay | US | ✓ | ✓ | Yes | ✗ |
| Cash App Afterpay | US | ✓ | ✗ | Yes | ✗ |
| Korean cards/Kakao/Naver Pay | South Korea | ✓ | ✓ | Yes | ✓ |
| Samsung Pay/PAYCO | South Korea | ✓ | ✗ | Yes | ✓ |
| UPI | India | ✓ | ✓ | Yes | ✗ |
| Pix | Brazil | ✓ | ✓ (no daily²) | Yes | ✗ |
| Bancontact | Belgium | ✓ | ✓ | Yes | ✓ |

¹ Klarna one-time only for Managed Payments; recurring Klarna available outside Managed Payments.
² Pix doesn't support daily subscriptions.

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[source-stripe-managed-payments-tax-compliance]] — tax coverage details
- [[source-stripe-managed-payments-eligibility]] — eligibility and tax codes

## Raw Sources

- [[stripe-managed-payments-how-it-works-2025]] — verbatim guide (~133 lines, 1 image)
