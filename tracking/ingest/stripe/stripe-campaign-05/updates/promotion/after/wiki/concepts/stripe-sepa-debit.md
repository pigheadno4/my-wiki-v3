---
title: "SEPA Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, sepa, sepa-debit, eu, eur, iban, bank-debit, mandates, disputes]
---

## Definition

SEPA Direct Debit lets businesses in the SEPA region (and 40 global Stripe markets) pull funds from customers' EUR-denominated bank accounts via IBAN. API enum: `sepa_debit`. Business-initiated, delayed notification, reusable. Core scheme (not B2B) — supports both personal and business accounts.

**Currency** is EUR only. The May and November 2026 method overviews label customer locations as EU and separately list 40 Stripe-account business locations. See [[source-stripe-sepa-debit]] for the list.

## Limits

- Per transaction: 10,000 EUR
- New users: 10,000 EUR weekly (increases as volume grows)

## Settlement

| Settlement | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Standard | T+6 at 00:00 UTC | T+6 at 00:00 UTC | 10:30 CET |

**Payment timing**: submitted same day if before 10:30 CET cutoff, next business day otherwise. **5-business-day refusal window** after submission — most failures occur here. After refusal window, payment appears successful; rare post-window failures appear as disputes.

> Both method overviews advise waiting at least six business days before considering a SEPA debit successful. See the dated refund advice below.

## Mandates

Collect the customer's name and IBAN and obtain mandate acceptance before debit. The November 2026 method overview adds billing `city`, `postal_code`, `line1` and `country` for payments from an IBAN outside the EEA. The Charge exposes the Mandate ID at `payment_method_details.sepa_debit.mandate`. See [[source-stripe-sepa-debit]].

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
- After collecting live SEPA debits, the Dashboard blocks changing the Creditor ID. Contact Stripe support for migration guidance.

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

Standard notice is at least 14 calendar days before payment creation. State any shorter timing in the mandate. The Stripe mandate quoted by both overviews allows notice up to two calendar days before a future payment, including at payment creation. See [[source-stripe-sepa-debit]].

## Connect

Enable SEPA Direct Debit on the platform and request `sepa_debit_payments` for connected accounts. The November 2026 guides require a new customer mandate per connected account for destination charges processed on its behalf. Obtain acceptance with a PaymentIntent or SetupIntent that names the connected account in `on_behalf_of`. The guides exclude cloning SEPA payment methods and mandates to connected accounts for destination charges. See [[source-stripe-sepa-debit]] and [[source-stripe-payment-method-connect-support]].

## Failure Codes

13 failure codes: `refer_to_customer`, `insufficient_funds`, `debit_disputed`, `authorization_revoked`, `debit_not_authorized`, `account_closed`, `bank_account_restricted`, `debit_authorization_not_match`, `recipient_deceased`, `branch_does_not_exist`, `incorrect_account_holder_name`, `invalid_account_number`, `generic_could_not_process`.

## Disputes

- **Up to 8 weeks**: "no questions asked", automatically honored by bank
- **8 weeks to 13 months**: unauthorized debit only; Stripe provides mandate; bank may still rule for customer
- `charge.dispute.created` webhook; dispute fee varies by settlement currency
- **Final and uncontestable** — must resolve directly with customer

## Refunds

- Up to 180 days from original payment
- 3–4 business days to process; arrive within 5 business days
- Full and partial refunds supported; appear as credit (not labeled "refund") on bank statement
- May 2026 recommends waiting at least seven business days. November 2026 recommends issuing the refund after the original payment fully settles, confirming processing with the buyer and sharing expected timing.
- Bank disputes can still proceed after a refund, with potential double credit. See [[source-stripe-sepa-debit]].
- New accounts: refunds may be temporarily disabled for up to 2-day fraud review

## Radar

Real-time ML fraud protection for SEPA, trained specifically for SEPA Direct Debit fraud patterns.

## Integration

**Checkout**. The May 3, 2026 acceptance guide documents EUR prices and dynamic or manual SEPA Direct Debit selection. See [[source-stripe-sepa-accept-payment]] for the optional mandate reference prefix of up to 12 characters and best-effort debit scheduling 3–15 days ahead.

**Payment Element**. The May 3, 2026 acceptance guide uses the Payment Element to collect IBAN and present the mandate. Stripe.js `confirmPayment` submits the existing PaymentIntent. Wait for `payment_intent.succeeded` before fulfilling. See [[source-stripe-sepa-accept-payment]] for processing and decline webhooks, and [[source-stripe-sepa-debit]] for the separate May product guide’s standard T+6 settlement and six-business-day timing guidance.

**Test IBANs**: 19 countries (AT, BE, HR, EE, FI, FR, DE, GI, IE, LI, LT, LU, NL, NO, PT, ES, SE, CH, GB), 8 tokens per country (`pm_success_{cc}`, `pm_successDelayed_{cc}`, `pm_failed_{cc}`, `pm_failedDelayed_{cc}`, `pm_disputed_{cc}`, `pm_exceedsWeeklyVolumeLimit_{cc}`, `pm_exceedsWeeklyTransactionLimit_{cc}`, `pm_insufficientFunds_{cc}`).

## SEPA Subscriptions

The May 2026 guide has a hosted Checkout subscription example (`payment_method_types=['sepa_debit']`, `mode='subscription'`) and an advanced web example (`default_incomplete` + `save_default_payment_method='on_subscription'`). The advanced page recommends a separate Payment Element build guide for new users, while its own mixed sample mounts a Payment Element and uses SEPA-specific `confirmSepaDebitPayment` or `confirmSepaDebitSetup` calls according to whether payment is due up front. The November 2026 unparameterized capture is only a variant index. [[source-stripe-subscriptions-sepa-debit]]

**Delayed notification (May 2026 guide)** — `checkout.session.completed` records debit authorization, not payment success. The guide uses later `checkout.session.async_payment_succeeded` or `invoice.paid` for fulfillment. Its example handles `invoice.paid` for an initial paid invoice as well as later paid periods, even if that event precedes `checkout.session.completed`. [[source-stripe-subscriptions-sepa-debit]]

Checkout supports: setup fee, inline pricing, existing customer, trials, fixed/dynamic tax rates, coupons, promo codes.

## Sources

- [[source-stripe-sepa-debit]] — May and November 2026 method overviews with IBAN and mandate requirements, Connect, timing, refunds, disputes and Billing retries.
- [[source-stripe-sepa-accept-payment]] — May 2026 acceptance guide for Checkout, web Elements and React Native. The November capture links the three variants.
- [[source-stripe-sepa-set-up-payment]] — May 2026 guide to Checkout setup mode, web Elements and React Native SetupIntents, mandate references and later-debit test cases. The November capture links the three variants.
- [[source-stripe-subscriptions-sepa-debit]] — May subscription guide: hosted Checkout and advanced web example, delayed notification, 19 country headings in each IBAN test table (8 scenarios each); November capture is a variant index
- [[source-stripe-subscriptions-ideal]] — 2026-05-13 iDEAL→SEPA subscription variants: hosted Checkout and Direct API setup with generated_sepa_debit retrieval; setup success differs from the later SEPA payment outcome. 2026-11-07 capture is a variant index only.
- [[source-stripe-ideal-save-during-payment]] — 2026-05-03 initial iDEAL payment to generated SEPA method and distinct later SEPA intent; mobile mandate examples and asynchronous outcome caveat. 2026-11-07 capture is variant navigation only.
