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
| Default presentment threshold | May 2026 under 5,000 USD; November under 7,500 USD; dynamic risk threshold | No specific limit |
| Checkout experience | Link accelerated checkout | Standard flow |

> Use ACH Direct Debit for businesses that don't immediately fulfill goods/services and can wait up to 4 business days for confirmation.

## Key Properties

- **Currency**: USD; **Customer location**: US only
- **Settlement**: 2-day (same as cards); Stripe **guarantees** settlement vs bank-initiated ACH returns
- **Customer-initiated disputes**: Stripe debits your balance + dispute fee (same process as card disputes)
- **Recurring/off-session**: After the customer authenticates and completes their first Link transaction, the guides describe future use of the saved account without reauthentication.
- **Manual capture**: Yes; **Connect**: Yes; **Refunds**: Yes / partial Yes

## Eligibility

Stripe applies dynamic risk and onboarding criteria for each session. The examples include US business with Stripe usage history, an amount below the applicable risk cutoff, and ACH Direct Debit not being enabled for the transaction.

**Supported integrations (May 8 and November 7, 2026 dedicated guides)**: Checkout, Payment Links, hosted invoice page, Payment Element and Mobile Payment Element. The May 2 bank-debits overview lists mobile support for its combined Instant Bank Payments-or-ACH row. The November 7 bank-debits overview lists that combined row as unsupported. The row leaves specific method and client changes unresolved. See [[source-stripe-instant-bank-payments]] and [[source-stripe-bank-debits]].

## ACH Direct Debit Interaction Rule

ACH Direct Debit takes precedence for the same transaction. May names `us_bank_account` in `payment_method_types` on Checkout Session, PaymentIntent and SetupIntent. The November dedicated guide uses `allowed_payment_method_types` on PaymentIntent and SetupIntent, while retaining `payment_method_types` for Checkout Session. The separate Endive changelogs reject the writable field on `2026-09-30.endive` Checkout Session Create and affected Intent requests. Endive Checkout allowlist precedence remains unverified.

Dynamic ACH eligibility suppresses Instant Bank Payments. [[stripe-payment-method-rules|Restricting ACH by a rule]] can leave Instant Bank Payments available only for transactions that separately qualify. The sibling Link guide's `link` or `card` route selection and resulting PaymentMethod response types describe a separate choice. See [[source-stripe-instant-bank-payments]].

## Stripe-Funded Cash Back Promotions

Stripe may offer consumer cash back/credits to drive IBP adoption:
- **No merchant cost** — Stripe funds fully; merchant receives full transaction amount
- Promotional amount deposited to customer's bank within 7 business days
- Configurable in Link settings Dashboard

## Testing

**Success scenarios**: Success, Disputed, Blocked, Bank (Non-OAuth — any credentials work; special keywords: `options`/`mfa`/`confirm_mfa`/`security_question`/`error`/`incorrect`), Bank (OAuth)

**Failure scenarios**: Down (Scheduled), Down (Unscheduled), Down (Error)

## Sources

- [[source-stripe-instant-bank-payments]] — May and November 2026 guides to eligible presentment, settlement and dispute scope, dated ACH precedence, the mobile listing conflict, cash back and testing.
- [[source-stripe-link-payment-integrations]] — Standalone and card-specific Link representations, non-card placeholders and general Stripe-balance timing alongside the Instant Bank Payments dispute exception.
