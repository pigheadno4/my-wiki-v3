---
title: "Stripe: SEPA Direct Debit Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/sepa-debit"
raw_files:
  - "stripe-payments-sepa-debit-2026-11-07.md"
  - "stripe-sepa-debit-2025.md"
tags: [stripe, sepa, sepa-debit, eu, eur, iban, bank-debit, mandates, disputes, radar]
---

## Summary

SEPA Direct Debit on [[stripe]] is a reusable, business-initiated bank debit in EUR with delayed payment notification. The May 3 and November 7, 2026 overviews describe SEPA Core for personal and business accounts. The separate SEPA B2B scheme and manual capture are unsupported. Both list EU customer locations and 40 eligible Stripe-account business locations. Payments are limited to €10,000 each, with an additional €10,000 weekly limit for new users that can rise with volume (May lines 6–118, November lines 7–119).

## Activation and mandate

- Request access from Dashboard payment method settings and complete the additional identity verification. The overviews list Checkout, Elements, Payment Links, Subscriptions, Invoicing and Connect, and exclude Express Checkout Element (May lines 105–149, November lines 106–149).
- Collect the customer's name and IBAN and obtain their acceptance of a mandate before creating the debit. November adds billing `city`, `postal_code`, `line1` and `country` for payments with an IBAN outside the EEA. Find the Mandate ID at `payment_method_details.sepa_debit.mandate` on the Charge (May line 10, November line 11).
- The customer can cancel via the party they established the mandate with or their bank. Subsequent debits under that mandate are invalid. Stripe learns of external cancellation on a failed attempt, marks the mandate `inactive` and emits `mandate.updated`. A merchant can cancel an active mandate by detaching its payment method or Source. A dispute can also deactivate a multi-use mandate. Collect fresh acceptance before using a replacement mandate (May lines 216–224 and 274–288, November lines 222–230 and 280–294).

## Timing and failures

Both method overviews list standard success and Stripe balance availability at **T+6 at 00:00 UTC**. T is bank submission. Payments created on a business day before the **10:30 CET** cutoff generally submit that day. Payments created after the cutoff or on a non-business day are processed the next business day. The bank can refuse the debit during the five business days after submission. Most failures occur within six business days of initiation, and rare later failures can appear as disputes. The setup guide separately describes a later payment typically taking five business days to arrive in the account. Its wording differs from the method overviews' submission-based timing. Neither the Checkout flow illustration, the debit estimate nor Stripe balance availability verifies external bank payout (both overviews lines 121–130 and 152–162, May failure section lines 226–272, November lines 232–278; [[source-stripe-sepa-set-up-payment|May future-payment setup guide]], May raw lines 20–27).

`expected_debit_date` on the Charge and in `charge.updated`, `charge.succeeded` or `charge.failed` events is an estimate when determinable. On failure, Stripe removes the funds immediately from the Stripe balance. Read the Charge's `failure_code` and `failure_message`. The May and November tables each list **13** codes (May lines 260–272, November lines 266–278): `refer_to_customer`, `insufficient_funds`, `debit_disputed`, `authorization_revoked`, `debit_not_authorized`, `account_closed`, `bank_account_restricted`, `debit_authorization_not_match`, `recipient_deceased`, `branch_does_not_exist`, `incorrect_account_holder_name`, `invalid_account_number`, and `generic_could_not_process`.

## Debit notifications

Notify the customer for each debit. Stripe sends an email by default, and always sends it automatically when its Creditor ID is used. When custom notices are allowed, manage Stripe email in Dashboard settings or use `mandate.notification_method` with the Sources API. Use `payment_intent.processing` to trigger a custom debit-initiation email. Include the debtor account's last four digits, mandate reference `sepa_debit[reference]`, amount, SEPA Creditor ID and merchant contact information. Standard notice is at least 14 calendar days before payment creation. State any shorter timing in the mandate. The Stripe mandate described in both captures permits notice up to two calendar days ahead of future payments, including at payment creation. One notice can list several upcoming debits of the same amount with their dates (both captures lines 164–180).

## Creditor ID and Connect

- The default is Stripe's Creditor ID. Creditor Name checks business or legal entity name, then custom statement descriptor, then Stripe default name. For Connect, the first two prefer the connected account's respective field when available, then the platform's. Stripe recommends a recognizable descriptor and suggests an own Creditor ID for EU businesses. After collecting live SEPA debits, the Dashboard blocks changing the Creditor ID. Contact Stripe support for migration guidance (May lines 186–202, November lines 192–208).
- Enable SEPA Direct Debit on the platform and request `sepa_debit_payments` for the connected accounts. The charge-type table assigns Creditor ID to the connected account for direct charges and for destination or separate charges and transfers with `on_behalf_of`. Without that flag the two latter paths use the platform (May lines 182–214, November lines 182–220).
- November requires a mandate for each connected account for destination charges processed `on_behalf_of`, where the connected account is merchant of record. It prohibits cloning the SEPA PaymentMethod and mandate to connected accounts for destination charges. Collect a new mandate authorization from the customer through a new PaymentIntent or SetupIntent with `on_behalf_of` set to that connected account (November lines 186–190).

## Disputes and refunds

- A buyer can dispute through their bank without giving a reason for eight weeks after the debit. After that and up to 13 months, only unauthorized debits qualify. Stripe can supply the accepted mandate to the bank on request, and the bank can still refund the buyer. The disputes are final without appeal. Stripe emits `charge.dispute.created` and deducts the amount and a fee that varies with default settlement currency. Check for multi-use mandate deactivation (May lines 274–288, November lines 280–296).
- Both captures allow full or partial refunds within 180 days. Refunds have no fee, and the original processing fees remain nonrefundable. The guides describe typical processing in 3–4 business days and arrival within five business days. The bank statement shows a credit referencing the original descriptor. New-account refunds can be restricted while Stripe reviews the account, typically up to two business days (May lines 290–304, November lines 298–320).
- **Dated refund advice.** May recommends a trusted and verified customer, confirming processing with them and waiting at least seven business days. It also advises immediate outreach for an accidental debit. November advises waiting until the original payment fully settles, confirming the refund is being processed and explaining the expected timing. A bank dispute can still proceed after a refund and produce a double credit. The seven-day advice does not establish protection against that outcome (May lines 302–322, November lines 296 and 310–320).

## Radar, Billing retries and business restrictions

May says Radar might default to on for Radar users. November says it is on by default for supported payment methods. Both describe real-time fraud evaluation trained for SEPA Direct Debit. May labels Direct Debit Billing retries private preview. November describes enablement for recurring subscription invoices, one-off invoices or both, with up to two automatic retries for insufficient funds within 30 days of the original attempt and no debit failure fees on Stripe-initiated automatic retries. November omits the preview label and does not state general availability (May lines 324–332, November lines 322–334).

The November method overview adds SEPA-specific prohibited or restricted business categories alongside Stripe's general policy. Examples include cannabis businesses excluding cannabidiol (CBD), payment facilitators processing for sub-merchants, peer-to-peer money transfers and weapons or firearms. The overview does not assign a separate prohibition or restriction status to each listed item. See its full list at November lines 336–351.

## Related Pages

- [[stripe-sepa-debit]] — durable SEPA Direct Debit concept
- [[source-stripe-sepa-accept-payment]] — separate acceptance implementation
- [[source-stripe-sepa-set-up-payment]] — separate future-payment setup guide
- [[source-stripe-subscriptions-sepa-debit]] — separate subscription integration

## Raw Sources

- [[raw/stripe-payments-sepa-debit-2026-11-07|SEPA Direct Debit overview, captured 2026-11-07]] — full method eligibility, Connect, refund and retry guidance.
- [[raw/stripe-sepa-debit-2025|SEPA Direct Debit overview, captured 2026-05-03]] — full dated overview reusing three generic flow SVGs from `raw/assets/stripe-acss-debit-*.svg`.
