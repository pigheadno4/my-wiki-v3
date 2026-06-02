---
title: "Stripe: Billing Credits (Overview)"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-credits-overview-2025.md"
tags: [stripe, billing, usage-based, credits, credit-grants, invoicing]
---

## Summary

Conceptual reference for the Billing Credits feature (Public preview). Covers use cases, prohibited uses, credit grant states, eligibility rules, application priority, ledger vs available balance, unused grant limit, and void/credit note behavior.

## Key Details

**Use cases**: prepayment (paid credits) and promotional (free, often with expiry).

**Prohibited uses**: gift cards, stored value for non-subscription spending, third-party payments, digital wallet linking.

**Credit grant states**:

| State | Description |
| --- | --- |
| Pending | `available_balance` not yet usable |
| Granted | Eligible based on `effective_at`; effective immediately if not set |
| Depleted | Balance fully used |
| Expired | Reached `expires_at` or manually expired |
| Voided | Never applied to any invoice; can't be applied to future invoices |

**Eligibility** — credit applies to invoice if all 4 true:
1. Invoice `period_end` ≥ grant `effective_at`
2. Invoice `period_end` < grant `expires_at` (if set)
3. Grant has available balance at finalization
4. Grant currency matches invoice currency

**Cannot apply to**: one-off invoices, one-time setup items, licensed-price line items, metered-price items using legacy Usage Records.

**Application order**: after discounts, before taxes and `invoice_credit_balance`.

**Priority when multiple grants match** (highest to lowest):
1. Priority number (lower = higher priority)
2. Earlier `expires_at`
3. `promotional` category before `paid`
4. Earlier `effective_at`
5. Earlier `created`

**Finalization-only**: credits on preview/draft invoices may change if another invoice finalizes first. No finalization order guarantee across subscriptions.

**Ledger vs available balance**:
- Ledger: immutable append-only; reflects all recorded transactions
- Available: ledger minus expired/unrecorded transactions
- Unused grant limit uses **ledger balance** — a grant with zero available but positive ledger still counts

**Unused grant limit**: max **100 per customer**. Grant stops counting when depleted, expired, or voided.

**Void & credit note behavior**:
- Voiding an invoice reinstates credits to the grant (immediately expired if grant is past expiry)
- Issuing a Credit Note does NOT reinstate credits — must create a new grant

## Raw Sources

- [[stripe-usage-based-billing-credits-overview-2025]] — reformatted from plain-text paste (user request); all content preserved (107 lines original)
