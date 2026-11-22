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
| Standard (May and November 2026) | T+2 business days after submission at 00:00 UTC | T+2 business days after submission at 00:00 UTC | 18:20 Pacific/Auckland |

The Charge's `payment_method_details.expected_debit_date` estimates when funds may be debited. The May overview separately describes up to two business days from initiation to receive a payment result. The November [[source-stripe-nz-becs-accept-payment|acceptance guide]] says the PaymentIntent success or failure notification comes within three business days after submission. Submission confirmation indicates processing.

## Mandates (DDA)

Called Direct Debit Authorities (DDAs). Require: account holder name, email, bank account number + NZ BECS Direct Debit Service T&C agreement.

Customers can cancel at any time via bank or merchant. Cancellation invalidates future debits — must collect new DDA.

Mandate event: `mandate.updated` fires when canceled or permanently failed → `status` becomes `inactive`.

## Mandate and Debit Notification Emails

Mandatory emails (cannot be turned off without Stripe support involvement):

1. **Mandate confirmation.** Both method overviews say within five days of mandate establishment. The May acceptance and setup samples say five business days. Their November versions say five days. For setup-based collection, Stripe’s November default sends immediately after a successful SetupIntent. Include the date, the Stripe NZ Limited statement and authorization code 3143978, a link to the NZ Direct Debit Service Terms and Conditions, the bank name, account number and account name, the signatory name if different, and merchant address, email and phone. See [[source-stripe-nz-becs-accept-payment]] and [[source-stripe-nz-becs-set-up-payment]].

2. **Debit notification.** The May method overview says to notify on each debit day, and November says no later than the debit day. Under Stripe’s separate November default, it sends the notice immediately after successful PaymentIntent confirmation. Include the amount, Stripe NZ Limited debit statement, debit date, bank statement label notice and your contact information. Contact Stripe Support to disable Stripe’s emails and send custom notices.

## Disputes

- **9 months from the first payment** for a dispute about whether the DDA authorizes the debit.
- **120 days from the individual payment** for missing or mismatched notice.
- The November overview limits disputes to the full amount. `charge.dispute.created` marks creation. Stripe removes funds immediately when the customer's bank rules for the customer and requests the return.
- A refund issued while a dispute is in flight can cause a double credit.

## Refunds

- Max 90 days from original payment
- 3–5 business days to process
- Full and partial refunds supported
- Labeled as credit (not refund) on bank statement

## Product Support

The May overview lists Connect, Checkout, Payment Links, Subscriptions, Invoicing, and Elements generally. The November grid lists the full page, embedded form, Payment Links, and Payment Element. It excludes Express Checkout Element, Payment Method Messaging Element, and in-app payments. See [[source-stripe-nz-becs-debit]] for the dated products, APIs, and off-session conflict.

## Billing Retries

The May 2026 overview labeled the insufficient-funds retry feature private preview. The November guide documents configurable automatic retries for payments that fail due to insufficient funds on recurring subscription invoices, one-off invoices, or both. Stripe can retry an eligible failure once, no more than 30 days after the original attempt. Stripe charges no debit failure fee for its automatic retries. General availability remains undetermined.

## Key Differences from AU BECS

| | NZ BECS | AU BECS |
| --- | --- | --- |
| Mandate name | DDA (Direct Debit Authority) | DDR (Direct Debit Request) |
| Currency | NZD | AUD |
| Dispute window | 9 months / 120 days | 7 years |
| Pre-debit email | No later than the day of the debit (November 2026 NZ overview) | Day before debit |
| Email opt-out | Via Stripe support only | Self-serve |

## Integration

**Payment Element** automatically collects name, email, bank account number, and presents NZ BECS Direct Debit Service T&C for DDA agreement — no separate mandate UI needed.

**PaymentIntent flow.** The May 2026 guide uses `payment_method_types: ['nz_bank_account']` on NZD PaymentIntents. The November guide enables NZ bank account in Dashboard and shows `automatic_payment_methods[enabled]=true` with `customer_account` or `customer`. A successful client submission enters `processing`; fulfill after verified success. The Endive changelog identifies HTTP 400 (`payment_method_types_no_longer_supported`) for writing the old field on `2026-09-30.endive` PaymentIntent Create. The computed response field remains readable. See [[source-stripe-nz-becs-accept-payment]] for the API version and compatibility-filter guidance.

**Off-session scope.** The November acceptance guide illustrates `off_session=true` for both customer identities. The November [[source-stripe-nz-becs-debit|method overview]] marks off-session payments unsupported while listing `setup_future_usage` and SetupIntents as supported. Eligibility remains unresolved. Apply the same qualification when consulting [[source-stripe-nz-becs-set-up-payment]].

**Target date**: `payment_method_options.nz_bank_account.target_date`, 3–15 days ahead, best effort. A non-business date or fewer than three business days of lead time rolls to the next available business day. Cancel up to three business days before the configured date. The November guide tracks the Charge estimate `payment_method_details.expected_debit_date` through `charge.updated`; the Intent moves from `processing` to `succeeded` on bank settlement or `requires_payment_method` on bank rejection.

**Test accounts** (bank `11`, branch `0000`): 6 test account/suffix combinations. Tokens: `pm_nzBankAccount_success`, `pm_nzBankAccount_insufficientFunds`, `pm_nzBankAccount_referToCustomer`, `pm_nzBankAccount_noAccount`, `pm_nzBankAccount_debitNotAuthorized`, `pm_nzBankAccount_processing`.

## Sources

- [[source-stripe-nz-becs-debit]] — May and November 2026 overview of approval, account limits, submission-relative settlement, notices, disputes, and refunds. November's off-session Unsupported cell conflicts with dated acceptance and setup examples, and the May overview's five-day mandate wording differs from the May samples' five business days.
- [[source-stripe-nz-becs-accept-payment]] — May and November 2026 PaymentIntent and Payment Element guides covering explicit and dynamic setup, Endive Create, DDA notices, target dates and sandbox tests. November describes measuring result notification from submission. Its later `off_session=true` examples conflict with the same-date overview’s Unsupported cell. May’s mandate sample says five business days and November’s says five days.
- [[source-stripe-nz-becs-set-up-payment]] — May and November 2026 guides for SetupIntent, Payment Element, and DDA. The November Accounts v2 and Customers v1 examples show a later NZD PaymentIntent with `off_session=true`, while the same-date [[source-stripe-nz-becs-debit|method overview]] marks off-session payments unsupported and lists recurring, SetupIntents, and PaymentIntents with `setup_future_usage` as supported. The conflict leaves route and account eligibility unresolved.
- [[source-stripe-nz-becs-migrate-from-processor]] — May and November 2026 migration guides covering original DDA retention, pre-migration and separate successful-import, per-debit and merchant first-success notices, and offline SetupIntent confirmation.
