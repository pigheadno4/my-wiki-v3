---
title: "Stripe: Accept an Australia BECS Direct Debit Payment"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-au-becs-accept-payment-2025.md"
tags: [stripe, au-becs, becs, australia, aud, checkout, elements, ios, android, payment-intents]
---

## Summary

Multi-platform integration guide for accepting AU BECS Direct Debit payments: Checkout (hosted/embedded), Checkout Sessions API (Elements), iOS (STPAUBECSFormView), and Android. Covers test accounts, target date, and failure codes.

## Key Details

### Checkout path

- `payment_method_types: ['au_becs_debit']` (or include alongside `'card'`)
- All line items must use `aud` currency
- Supports payment, setup, and subscription modes
- Optional `target_date`: 3–15 days out, best-effort, delayed to next business day if weekend/holiday

### Checkout Sessions API (Elements)

- Create Checkout Session with `ui_mode: 'elements'`, `return_url`
- TypeScript server: `session.client_secret` → pass to client
- Client: `initCheckoutElementsSdk({clientSecret})` → `checkout.loadActions()` → `createPaymentElement()` + `actions.confirm()`
- Email required: `actions.updateEmail(email)` or pass `customer_email` at session creation

### iOS (STPAUBECSFormView)

- `STPAUBECSFormView` collects name, email, BSB, account number + shows BECS Terms
- Delegate `auBECSDebitForm(_:didChangeToStateComplete:)` to enable Pay button
- Create PaymentIntent server-side: `currency: 'aud'`, `payment_method_types: ['au_becs_debit']`, optional `setup_future_usage: 'off_session'`
- Client: `STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self)` — handles mandate presentation
- After confirmation: share mandate URL from `Mandate.payment_method_details.au_becs_debit.url`

### Android

- `AUBECSDirectDebitWidget` collects bank details + displays mandate
- Create PaymentIntent server-side; confirm with `stripe.confirmAuBecsDebitPayment()`

### Test accounts (BSB `000000`)

| Account | Token | Behavior |
| --- | --- | --- |
| `000123456` | `pm_auBecsDebit_success` | Succeeds immediately |
| `900123456` | `pm_auBecsDebit_successDelayed` | Succeeds after 3 min |
| `111111113` | `pm_auBecsDebit_accountClosed` | Fails; mandate → inactive |
| `111111116` | `pm_auBecsDebit_noAccount` | Fails; mandate → inactive |
| `222222227` | `pm_auBecsDebit_referToCustomer` | Fails; mandate stays active |
| `922222227` | `pm_auBecsDebit_referToCustomerDelayed` | Fails after 3 min; mandate stays active |
| `333333335` | `pm_auBecsDebit_debitNotAuthorized` | Fails; mandate → inactive |
| `666666660` | `pm_auBecsDebit_dispute` | Succeeds then dispute |
| `343434343` | `pm_auBecsDebit_exceedsWeeklyLimit` | Fails: `charge_exceeds_source_limit` |
| `121212121` | `pm_auBecsDebit_exceedsTransactionLimit` | Fails: `charge_exceeds_transaction_limit` |

## Raw Sources

- [[stripe-au-becs-accept-payment-2025]] — verbatim webpage content (Checkout + Elements + iOS + Android sections)
