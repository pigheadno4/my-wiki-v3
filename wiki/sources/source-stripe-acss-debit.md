---
title: "Stripe: Canadian Pre-Authorized Debit Payments (ACSS)"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/acss-debit"
raw_files:
  - "stripe-payments-acss-debit-2026-11-07.md"
  - "stripe-acss-debit-2025.md"
tags: [stripe, acss, acss-debit, canada, cad, bank-debit, mandates, pad, disputes, refunds, connect]
---

## Summary

Stripe's Canadian pre-authorized debit (PAD/ACSS) guide covers CA/US business accounts taking bank debits from customers with Canadian accounts, in CAD or USD. A mandate defining the debit schedule or terms and bank verification are required; confirmation is delayed, and payments can fail or be disputed after initiation. The November 2026 capture adds eligibility review, conditional limits, detailed refunds/disputes, Connect mandates, retry bounds, and event-specific asynchronous outcomes. These are dated documentation statements, not verification of any merchant's eligibility, configured limits, or a live debit. See [[stripe-acss-debit]] and [[stripe]]. [May capture](../../raw/stripe-acss-debit-2025.md#L8-L16), [November capture](../../raw/stripe-payments-acss-debit-2026-11-07.md#L9-L38).

## Eligibility, limits, and capabilities

The November guide lists CA and US merchant/Connect platform locations, Canadian customer bank accounts, CAD/USD presentment, and provisional access subject to possible post-activation review. It states a 0.50 minimum in the applicable currency and a **default maximum of 999,999.99** without enabled increased large-charge limits. Only if Stripe enables an increased limit does the absolute two-decimal-currency hard cap reach 9,999,999.99; merchant or platform Risk limits can lower the effective cap. The source does not establish any account's eligibility or limit. Most Canadian accounts hold CAD; a CAD/USD account-currency mismatch can cause a delayed failure, so the guide recommends CAD unless USD debit support is known. [May geography/currency](../../raw/stripe-acss-debit-2025.md#L20-L26), [May risk](../../raw/stripe-acss-debit-2025.md#L218-L224); [November eligibility](../../raw/stripe-payments-acss-debit-2026-11-07.md#L22-L43), [November limits/currency](../../raw/stripe-payments-acss-debit-2026-11-07.md#L44-L52).

The November capability matrix supports recurring payments, full and partial refunds, and full disputes, while excluding manual, partial, multi-, and over-capture and partial disputes. Product limitations say Checkout supports PAD in payment/setup modes, not subscription mode; Payment Element needs an existing PaymentIntent, not a deferred-intent or Elements-with-Checkout-Sessions path; Express Checkout Element and iOS/Android Payment Sheet do not support PAD. Billing, Invoicing, and Connect are listed separately from Checkout subscription mode. The product matrix marks off-session payments unsupported, while both captures document interval mandates and invoice/subscription reuse; keep that matrix label in its product/integration context, rather than treating it as erasure of those documented mandate paths. [May products](../../raw/stripe-acss-debit-2025.md#L67-L76), [May mandate reuse](../../raw/stripe-acss-debit-2025.md#L133-L166); [November capability matrix](../../raw/stripe-payments-acss-debit-2026-11-07.md#L54-L78), [November product matrix/limitations](../../raw/stripe-payments-acss-debit-2026-11-07.md#L200-L242).

## Mandates and notifications

A PAD mandate records bank details and a payment schedule: `interval` for specified dates or defined triggers, `sporadic` for irregular debits requiring express customer authorization at payment time, or `combined`. It also identifies `personal` or `business` transaction type. `default_for: ['invoice', 'subscription']` enables the documented invoice/subscription payment-method reuse without a new mandate. Canceling a mandate invalidates future debit requests; a new mandate is needed for further payments. Stripe starts the first debit immediately after acceptance. [May mandate/schedule](../../raw/stripe-acss-debit-2025.md#L123-L166), [November mandate/schedule](../../raw/stripe-payments-acss-debit-2026-11-07.md#L137-L177).

Payments Canada notification guidance in both captures requires mandate confirmation **within five calendar days of acceptance** and debit notification **each time a debit is made**. Stripe sends these emails by default. If the merchant sends custom notifications, it must support mandate confirmation, every-debit notification, and applicable microdeposit reminders together. The guide uses `charge.pending` to trigger a custom debit-notification email, with webhook signature verification; that pending event does **not** establish final debit success. Neither capture supports a blanket before-each-charge delivery deadline for the debit email. [May notification](../../raw/stripe-acss-debit-2025.md#L168-L188), [November notification](../../raw/stripe-payments-acss-debit-2026-11-07.md#L179-L198).

## Delayed outcome and settlement

The November flow moves from bank-detail collection and verification (instant or microdeposits, typically 1–2 business days and verification within 10 days), through mandate acceptance, to a submitted/processing state. Final success or failure can take up to five business days. For PaymentIntents, `payment_intent.processing` means submitted and waiting, while `payment_intent.succeeded` or `payment_intent.payment_failed` report outcomes. For Checkout, `checkout.session.completed` means **session completion only**; `checkout.session.async_payment_succeeded` and `checkout.session.async_payment_failed` report delayed payment outcomes. A browser page or pending state must not be treated as final payment success. [May delay](../../raw/stripe-acss-debit-2025.md#L14-L16), [November customer flow/events](../../raw/stripe-payments-acss-debit-2026-11-07.md#L278-L313).

Standard timing in both captures is **T+4 at 21:00 UTC** for payment success and **T+5 at 00:00 UTC** for funds to become available in the Stripe balance, with a **17:00 US/Eastern cutoff**. T counts business days **after submission**, which can differ from creation. `expected_debit_date` on Charge payment-method details is an estimate, not a guaranteed bank debit date; Stripe-balance availability does not prove a customer-bank receipt. Rare late bank failure after a PaymentIntent reached `succeeded` can create a failure-reason dispute and fee; even the status event is not a guarantee against later reversal. [May timing](../../raw/stripe-acss-debit-2025.md#L111-L121), [May late failure](../../raw/stripe-acss-debit-2025.md#L200-L216); [November late failure](../../raw/stripe-payments-acss-debit-2026-11-07.md#L131-L135), [November timing](../../raw/stripe-payments-acss-debit-2026-11-07.md#L266-L276).

## Refunds and disputes

A full or partial PAD refund must be submitted within 180 days of the original payment and typically takes three business days to process. The November guide says a refund cannot be canceled. If submitted while the Charge is pending, it starts only after Charge success; a failed Charge cancels that pending refund. Refunds are separate bank credits rather than payment reversals, can appear under the original descriptor rather than a refund label, and may fail (`refund.updated` or `refund.failed` and Refund status). A refund does not prevent a bank dispute; concurrent refund and dispute can create a duplicate customer credit. [May refunds](../../raw/stripe-acss-debit-2025.md#L226-L236), [November refunds](../../raw/stripe-payments-acss-debit-2026-11-07.md#L70-L105).

Personal-account PAD disputes may be filed up to **90 calendar days** after debit; business-account disputes up to **10 business days**. There is no inquiry phase and no evidence submission or merchant appeal; the bank's decision is final, and Stripe does not refund the dispute fee. The November guide says `charge.dispute.created` arrives when a customer files and `charge.dispute.closed` when the dispute closes. The May sentence grouped both events at creation but did not establish simultaneous delivery; the older source's simultaneous claim is therefore removed. Stripe deducts disputed funds and fee when the bank creates a dispute. [May dispute](../../raw/stripe-acss-debit-2025.md#L190-L198), [November dispute](../../raw/stripe-payments-acss-debit-2026-11-07.md#L107-L129).

## Connect, retries, and identifiers

For Connect PAD integration, the November guide says enable PAD on the platform and request `acss_debit_payments` for connected accounts. For destination charges with `on_behalf_of`, the connected account is merchant of record, so collect a separate mandate for each such connected account; do not clone PAD methods or mandates across accounts. Descriptor ownership also depends on charge type: direct and `on_behalf_of` examples use the connected account, while ordinary destination and separate-charge-and-transfer examples use the platform. This does not prove a particular connected account has capability enabled. [May Connect](../../raw/stripe-acss-debit-2025.md#L255-L267), [November Connect](../../raw/stripe-payments-acss-debit-2026-11-07.md#L248-L256), [November descriptors](../../raw/stripe-payments-acss-debit-2026-11-07.md#L315-L336).

The May heading labeled Billing Retries **private preview**. November omits a release-phase label but describes Direct Debit retries for failed PAD payments caused by insufficient funds: at most one Stripe-initiated automatic retry within 30 days of the original attempt, with no debit failure fee for that automatic retry. The omission does not establish general availability or account enablement. Custom Radar PAD settings are separately labeled private preview in November. [May retries](../../raw/stripe-acss-debit-2025.md#L269-L271), [November retries](../../raw/stripe-payments-acss-debit-2026-11-07.md#L258-L264), [November Radar](../../raw/stripe-payments-acss-debit-2026-11-07.md#L244-L246).

The descriptor uses the first 15 alphanumeric characters on bank statements and may be dynamically set on a PaymentIntent; banks can format it differently. The November guide identifies a **PAD mandate ID**, not an ACSS network transaction ID: in the Stripe account owning the PaymentIntent, expand `latest_charge` and read `latest_charge.payment_method_details.acss_debit.mandate`. Use the debit date/amount, bank last four, descriptor, and mandate ID for matching or support. The May raw retains three local flow-diagram SVG references. [May descriptor/assets](../../raw/stripe-acss-debit-2025.md#L78-L88), [May descriptor](../../raw/stripe-acss-debit-2025.md#L238-L267); [November identifier](../../raw/stripe-payments-acss-debit-2026-11-07.md#L315-L340).

## Related Pages

- [[stripe-acss-debit]] — ACSS/PAD concept
- [[source-stripe-acss-accept-payment]] — separate acceptance integration guide
- [[source-stripe-acss-set-up-payment]] — separate save-for-future integration guide
- [[source-stripe-subscriptions-acss-debit]] — separate subscription guide
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-payments-acss-debit-2026-11-07|November 7, 2026 Canadian PAD guide]] — full webpage content (346 lines)
- [[raw/stripe-acss-debit-2025|May 2, 2026 Canadian PAD guide]] — historical webpage content (271 lines; three local flow diagrams)
