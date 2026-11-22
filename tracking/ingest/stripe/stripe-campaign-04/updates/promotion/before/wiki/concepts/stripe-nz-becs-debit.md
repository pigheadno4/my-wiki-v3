---
title: "NZ BECS Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, nz-becs, becs, new-zealand, nzd, bank-debit, mandates, disputes]
---

## Definition

New Zealand BECS Direct Debit lets NZ businesses pull funds from customers' New Zealand bank accounts. API enum: `nz_bank_account`. Business-initiated, delayed notification, reusable. Disputes limited to 9 months (DDA authorization disputes) or 120 days (notification disputes).

**Currency**: NZD only. **Country**: NZ customers; NZ business accounts only.

## Settlement

| Settlement | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Standard | T+2 at 00:00 UTC | T+2 at 00:00 UTC | 18:20 Pacific/Auckland |

`expected_debit_date` available on `payment_method_details` for Charges (estimated, not guaranteed).

## Mandates (DDA)

Called Direct Debit Authorities (DDAs). Require: account holder name, email, bank account number + NZ BECS Direct Debit Service T&C agreement.

Customers can cancel at any time via bank or merchant. Cancellation invalidates future debits — must collect new DDA.

Mandate event: `mandate.updated` fires when canceled or permanently failed → `status` becomes `inactive`.

## Mandate and Debit Notification Emails

Mandatory emails (cannot be turned off without Stripe support involvement):

1. **Mandate confirmation** (within 5 days of mandate establishment): date, Stripe NZ Limited (auth code 3143978) statement, link to NZ Direct Debit Service T&Cs, bank name/account number/account name, signatory name if different, your contact info (address, email, phone).

2. **Pre-debit notification** (day of every PaymentIntent confirmation): payment amount, Stripe NZ Limited debit statement, debit date, bank statement label warning, your contact info.

## Disputes

- **9 months** from first payment: if customer isn't satisfied the DDA authorizes the debit
- **120 days** from payment: if pre-debit notification wasn't sent, or amount/date differs from notification
- `charge.dispute.created` event fired; Stripe immediately removes funds
- Risk of double-credit if refund issued while dispute in flight

## Refunds

- Max 90 days from original payment
- 3–5 business days to process
- Full and partial refunds supported
- Labeled as credit (not refund) on bank statement

## Product Support

Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements (full product support, no ECE restriction mentioned).

## Billing Retries

Private preview. Auto-retry for insufficient funds on subscription or one-off invoices.

## Key Differences from AU BECS

| | NZ BECS | AU BECS |
| --- | --- | --- |
| Mandate name | DDA (Direct Debit Authority) | DDR (Direct Debit Request) |
| Currency | NZD | AUD |
| Dispute window | 9 months / 120 days | 7 years |
| Pre-debit email | Day of debit | Day before debit |
| Email opt-out | Via Stripe support only | Self-serve |

## Integration

**Payment Element** automatically collects name, email, bank account number, and presents NZ BECS Direct Debit Service T&C for DDA agreement — no separate mandate UI needed.

**PaymentIntent flow**: `payment_method_types: ['nz_bank_account']`, `currency: 'nzd'` → `stripe.confirmPayment({ elements, redirect: 'if_required' })` → returns `processing` → await `payment_intent.succeeded` webhook.

**Target date**: `payment_method_options.nz_bank_account.target_date`, 3–15 days, best-effort. Can cancel PaymentIntent up to 3 business days before target.

**Test accounts** (bank `11`, branch `0000`): 6 test account/suffix combinations. Tokens: `pm_nzBankAccount_success`, `pm_nzBankAccount_insufficientFunds`, `pm_nzBankAccount_referToCustomer`, `pm_nzBankAccount_noAccount`, `pm_nzBankAccount_debitNotAuthorized`, `pm_nzBankAccount_processing`.

## Sources

- [[source-stripe-nz-becs-debit]] — primary source: settlement, mandates, DDA emails, disputes, refunds
- [[source-stripe-nz-becs-accept-payment]] — integration guide: PaymentIntent + Payment Element, DDA mandate text, off-session charging, 6 test accounts, target_date
- [[source-stripe-nz-becs-set-up-payment]] — save for future: SetupIntent + Payment Element, DDA mandate, off-session charging
- [[source-stripe-nz-becs-migrate-from-processor]] — processor migration: 3-step notification requirements, SetupIntent with offline DDA acceptance, billing_details required
