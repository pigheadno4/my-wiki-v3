---
title: "SEPA Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, sepa, sepa-debit, eu, eur, iban, bank-debit, mandates, disputes]
---

## Definition

SEPA Direct Debit lets businesses in the SEPA region (and 40 global Stripe markets) pull funds from customers' EUR-denominated bank accounts via IBAN. API enum: `sepa_debit`. Business-initiated, delayed notification, reusable. Core scheme (not B2B) — supports both personal and business accounts.

**Currency**: EUR only. **Region**: EU customers (all EUR IBAN accounts in the SEPA zone).

## Limits

- Per transaction: 10,000 EUR
- New users: 10,000 EUR weekly (increases as volume grows)

## Settlement

| Settlement | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Standard | T+6 at 00:00 UTC | T+6 at 00:00 UTC | 10:30 CET |

**Payment timing**: submitted same day if before 10:30 CET cutoff, next business day otherwise. **5-business-day refusal window** after submission — most failures occur here. After refusal window, payment appears successful; rare post-window failures appear as disputes.

> Wait at least 6 business days before considering a SEPA payment as successful. Wait 7 days before refunding.

## Mandates

Collect customer name + IBAN; customer accepts mandate authorizing Stripe to debit on business's behalf. Mandate ID on `payment_method_details.sepa_debit.mandate` on Charge.

Customers can cancel at any time via merchant or bank. Stripe only learns of cancellation when a payment attempt fails → sets `inactive` + `mandate.updated` webhook.

If a multi-use mandate is associated with a disputed payment, it may be deactivated — check and re-collect if needed.

## Creditor ID

Default: Stripe Creditor ID. Creditor Name priority:

1. Business name / legal entity name
2. Custom statement descriptor
3. Default Stripe name

**Recommendations**:

- Configure a recognizable statement descriptor to reduce disputes
- EU-based businesses: use own Creditor ID (reduces disputes, improves UX) — configure on Payment Method Settings page
- Cannot change Creditor ID after live payments collected (contact support)

**Connect Creditor ID**:

| Charge type | Creditor ID from |
| --- | --- |
| Direct | Connected account |
| Destination | Platform |
| Separate charge + transfer | Platform |
| Destination (`on_behalf_of`) | Connected account |
| Separate charge + transfer (`on_behalf_of`) | Connected account |

## Debit Notification Emails

Required by SEPA rulebook before each debit. Stripe sends automatically (when using Stripe Creditor ID, always auto). Custom emails must include: last 4 digits of account, mandate reference (`sepa_debit[reference]`), amount, Creditor ID, your contact info.

Standard lead time: 14 days. Stripe mandate allows as close as 2 days in advance.

## Connect

Requires `sepa_debit_payments` capability on connected accounts.

## Failure Codes

12 failure codes: `refer_to_customer`, `insufficient_funds`, `debit_disputed`, `authorization_revoked`, `debit_not_authorized`, `account_closed`, `bank_account_restricted`, `debit_authorization_not_match`, `recipient_deceased`, `branch_does_not_exist`, `incorrect_account_holder_name`, `invalid_account_number`, `generic_could_not_process`.

## Disputes

- **Up to 8 weeks**: "no questions asked", automatically honored by bank
- **8 weeks to 13 months**: unauthorized debit only; Stripe provides mandate; bank may still rule for customer
- `charge.dispute.created` webhook; dispute fee varies by settlement currency
- **Final and uncontestable** — must resolve directly with customer

## Refunds

- Up to 180 days from original payment
- 3–4 business days to process; arrive within 5 business days
- Full and partial refunds supported; appear as credit (not labeled "refund") on bank statement
- **Wait 7 business days before refunding** (ensures refusal window closed)
- Risk of double-credit if customer disputes after refund
- New accounts: refunds may be temporarily disabled for up to 2-day fraud review

## Radar

Real-time ML fraud protection for SEPA, trained specifically for SEPA Direct Debit fraud patterns.

## Integration

**Checkout**: `payment_method_types: ['sepa_debit']`, `eur` currency. Optional `reference_prefix` (12 chars, not starting with `STRIPE`) → 24-char mandate reference. Optional `target_date` (3–15 days).

**Payment Element**: `stripe.confirmPayment({ elements, return_url })` — automatically collects IBAN + presents mandate. Webhooks: `payment_intent.processing` / `payment_intent.succeeded` / `payment_intent.payment_failed`. **Wait 6+ business days before considering payment successful.**

**Test IBANs**: 19 countries (AT, BE, HR, EE, FI, FR, DE, GI, IE, LI, LT, LU, NL, NO, PT, ES, SE, CH, GB), 8 tokens per country (`pm_success_{cc}`, `pm_successDelayed_{cc}`, `pm_failed_{cc}`, `pm_failedDelayed_{cc}`, `pm_disputed_{cc}`, `pm_exceedsWeeklyVolumeLimit_{cc}`, `pm_exceedsWeeklyTransactionLimit_{cc}`, `pm_insufficientFunds_{cc}`).

## SEPA Subscriptions

Two paths: Checkout (`payment_method_types=['sepa_debit']`, `mode='subscription'`) or Payment Element (`default_incomplete` + `save_default_payment_method='on_subscription'`).

**Delayed notification** — do NOT fulfill on `checkout.session.completed`. Wait for `checkout.session.async_payment_succeeded` or `invoice.paid`.

Checkout supports: setup fee, inline pricing, existing customer, trials, fixed/dynamic tax rates, coupons, promo codes.

## Sources

- [[source-stripe-sepa-debit]] — primary source: settlement, Creditor ID, mandates, failure codes, disputes, refunds, Radar
- [[source-stripe-sepa-accept-payment]] — integration guide: Checkout + Elements + iOS + Android, 19-country IBAN test table, reference_prefix, target_date
- [[source-stripe-sepa-set-up-payment]] — save for future: Checkout setup mode + SetupIntents (Elements/iOS/Android), same IBAN test table, reference_prefix
- [[source-stripe-subscriptions-sepa-debit]] — subscription guide: Checkout + Payment Element, delayed notification, 20+ country IBAN test tables (8 scenarios each)
- [[source-stripe-subscriptions-ideal]] — iDEAL→SEPA subscription: Checkout + Direct API, generated_sepa_debit retrieval, 6 email/PM test patterns
