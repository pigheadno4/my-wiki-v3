---
title: "Stripe Instant Bank Payments"
type: concept
category: technology
tags: [stripe, instant-bank-payments, link, ach, bank-debit, us-only, recurring, guaranteed-settlement]
---

## Definition

Instant Bank Payments (IBP) let US customers pay with their bank account through [[stripe-link]], with instant payment confirmation, 2-day settlement, and protection from bank-initiated ACH returns. Auto-enabled when Link is turned on; subject to eligibility.

**US only, USD only.**

## IBP vs ACH Direct Debit

| Property | Instant Bank Payments | ACH Direct Debit |
| --- | --- | --- |
| Confirmation | Instant | T+4 business days |
| Settlement | 2 days (card parity) | T+4 to T+7 |
| Bank-initiated returns | Stripe guarantees payment | Funds reversed |
| Transaction limit | < $5,000 (default) | No specific limit |
| Checkout experience | Link accelerated checkout | Standard flow |

> Use ACH Direct Debit for businesses that don't immediately fulfill goods/services and can wait up to 4 business days for confirmation.

## Key Properties

- **Currency**: USD; **Customer location**: US only
- **Settlement**: 2-day (same as cards); Stripe **guarantees** settlement vs bank-initiated ACH returns
- **Customer-initiated disputes**: Stripe debits your balance + dispute fee (same process as card disputes)
- **Recurring/off-session**: Yes — no re-auth after first Link authentication
- **Manual capture**: Yes; **Connect**: Yes; **Refunds**: Yes / partial Yes

## Eligibility

IBP appears only when all met:
- US business with Stripe usage history (onboarding criteria)
- Transaction amount < $5,000 (dynamic risk threshold)
- ACH Direct Debit is NOT also enabled for this transaction

**Supported integrations**: Checkout, Payment Links, Hosted Invoice Page, Payment Element, Mobile Payment Element.

## ACH Direct Debit Interaction Rule

IBP and ACH cannot appear together. ACH always takes precedence:

- **Explicit**: if `us_bank_account` in `payment_method_types` → IBP never shown
- **Dynamic PMs**: any ACH-eligible transaction → IBP suppressed

**Workaround**: use [[stripe-payment-method-rules]] to restrict ACH eligibility; transactions that don't meet ACH criteria but are IBP-eligible will show IBP instead.

## Stripe-Funded Cash Back Promotions

Stripe may offer consumer cash back/credits to drive IBP adoption:
- **No merchant cost** — Stripe funds fully; merchant receives full transaction amount
- Promotional amount deposited to customer's bank within 7 business days
- Configurable in Link settings Dashboard

## Testing

**Success scenarios**: Success, Disputed, Blocked, Bank (Non-OAuth — any credentials work; special keywords: `options`/`mfa`/`confirm_mfa`/`security_question`/`error`/`incorrect`), Bank (OAuth)

**Failure scenarios**: Down (Scheduled), Down (Unscheduled), Down (Error)

## Sources

- [[source-stripe-instant-bank-payments]] — primary: settlement guarantee, ACH comparison, eligibility, ACH priority rule, cash back promotions, testing
