---
title: "AU BECS Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, au-becs, becs, australia, aud, bank-debit, mandates, disputes]
---

## Definition

Australia BECS Direct Debit lets AU businesses pull funds from customers' Australian bank accounts. API enum: `au_becs_debit`. Business-initiated, delayed notification, reusable. Disputes are final and uncontestable.

**Currency**: AUD only. **Country**: AU customers; AU business accounts only.

## Limits

- Per transaction: 10,000 AUD (new users)
- Per week: 10,000 AUD (new users)
- Contact Stripe support for higher limits

## Settlement

| Settlement | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Standard | T+2 at 00:00 UTC | T+2 at 00:00 UTC | 18:30 Australia/Melbourne |

Funds debited from customer at T+0; settlement confirmation takes 2 business days.

`expected_debit_date` available on `payment_method_details` for Charges (estimated, not guaranteed).

## Mandates (DDR)

Called Direct Debit Requests (DDRs). Require: account holder name, BSB number, account number, mandate Service Agreement acceptance.

Customers can cancel at any time via bank or merchant. Cancellation invalidates future debits — must collect new DDR.

Mandate event: `mandate.updated` fires when mandate is canceled or permanently failed → `status` becomes `inactive`.

## Debit Notification Emails

BECS scheme advises (not mandatory) notifying customers:

1. When mandate is established
2. Before each debit

Stripe sends automatically. Pre-debit email sent day before account is debited. Custom emails: turn off Stripe emails, trigger on `payment_intent.processing`. Suggested 14-day lead time (not mandatory).

Custom email should include: last 4 digits of bank account, amount, contact info, planned debit date.

## Disputes

- **7-year** dispute window, "no questions asked"
- **Final and uncontestable** — must resolve directly with customer
- Stripe sends `charge.dispute.created` + `charge.dispute.closed` simultaneously
- Risk of double-credit if refund issued while dispute in flight

## Refunds

- Max 90 days from original payment
- 3–5 business days to process
- Full and partial refunds supported
- Labeled as credit (not refund) on bank statement

## Statement Descriptors

Two fields on customer's bank statement:

- **Merchant name**: from Stripe account statement descriptor; override with `statement_descriptor` on PaymentIntent
- **Lodgement reference**: first 9 alphanumeric chars of descriptor + unique ID (e.g., `RocketRid_AB1234CD`)

Connect `on_behalf_of` changes descriptor source to connected account.

## Product Support

Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements (not Express Checkout Element).

## Billing Retries

Private preview. Auto-retry for insufficient funds on subscription or one-off invoices.

## Integration

**Checkout**: `payment_method_types: ['au_becs_debit']`, `aud` currency required. Supports payment/setup/subscription modes. Optional `target_date` (3–15 days, best-effort).

**iOS**: `STPAUBECSFormView` collects name/email/BSB/account + displays BECS Terms. Confirm with `STPPaymentHandler.confirmPayment`. Share mandate URL after confirmation.

**Android**: `AUBECSDirectDebitWidget` + `stripe.confirmAuBecsDebitPayment()`.

**Test BSB `000000`**: 10 test accounts covering success, delayed success, closed account, no account, refer-to-customer, debit-not-authorized, dispute, weekly/transaction limit.

## Subscription integration

Flow: SetupIntent (`au_becs_debit`) → `auBankAccount` Element → `confirmAuBecsDebitSetup()` → share mandate URL → create Customer with PM as default → create subscription.

**Critical: BECS payments are never automatically retried**, even if a retry schedule is configured.

After `SetupIntent.succeeded`: must share mandate URL, business name, payment schedule, DDR link with customer. Mandate URL at `Mandate.payment_method_details.au_becs_debit.url`.

## Sources

- [[source-stripe-au-becs-debit]] — primary source: settlement, mandates, disputes, refunds, debit notifications, statement descriptors
- [[source-stripe-au-becs-accept-payment]] — integration guide: Checkout + Elements + iOS + Android, 10 test accounts, target_date
- [[source-stripe-au-becs-set-up-payment]] — save for future: SetupIntent (Elements + iOS + Android), AuBankAccountElement, DDR mandate requirements, off-session charging
- [[source-stripe-subscriptions-becs-debit]] — subscription setup: no-retry rule, mandatory mandate sharing, SetupIntents flow, billing_cycle_anchor + trial_end
