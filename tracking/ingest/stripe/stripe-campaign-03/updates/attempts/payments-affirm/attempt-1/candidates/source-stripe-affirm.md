---
title: "Stripe: Affirm Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/affirm"
raw_files:
  - "stripe-payments-affirm-2026-11-07.md"
  - "stripe-affirm-2025.md"
tags: [stripe, bnpl, affirm, buy-now-pay-later, installments, connect, disputes]
---

## Summary

[[stripe]] describes Affirm as a single-use, domestic B2C buy now, pay later method. The customer chooses Affirm, is redirected to Affirm's site or installed mobile app, selects a repayment plan, and authorizes it within 12 hours; Affirm collects the installments. After payment acceptance, Stripe says it makes the order amount less fees available to the business upfront. The November capture separately labels access **instant provisional**, confirmation **immediate**, and settlement **up to T+2**. A redirect, plan choice, or return to the merchant site alone does not establish a succeeded PaymentIntent, merchant access, or settlement. See [[stripe-bnpl]].

## Geography and eligibility

- **2026-05-06 capture**: US and Canada customer and business locations, with USD or CAD presentment.
- **2026-11-07 capture**: US/CA remain listed; GB business and customer locations and GBP presentment are marked **private preview**, not general availability. The business and customer must be in the same country; cross-border transactions are excluded. The November account matrix permits merchant and platform/marketplace account types but excludes B2B.
- The November guide says an account might undergo review after activation and requires a publicly accessible website displaying customer-local-currency prices. Its MCC table distinguishes **prohibited** codes from **restricted** codes requiring additional account information. The older broad category list also names B2B services, home improvement, titled goods/auto loans, professional services, NFTs, and pre-orders; healthcare has additional requirements. Use the actual MCC and account review, not the category label alone, to assess a particular merchant.
- Dynamic payment methods on Payment Element or Checkout Session filter country by shipping-address country first, then geocoded client IP. With explicit `payment_method_types`, the integration must present Affirm only to eligible customers or use dynamic payment methods. Display or configuration does not prove a buyer's loan approval.

## Payment options and financing

- **US (November)**: Pay in 30, USD 35–50 in the payment-options table (the package table caps its row at USD 49.99); Pay in 4, USD 50–500; monthly installments, USD 100–30,000 and up to 36 months.
- **CA (November)**: Pay in 4, CAD 50–500; monthly installments, CAD 100–30,000.
- **GB private preview (November)**: Pay in 3, GBP 50–500; monthly installments, GBP 100–30,000. The Standard package table lists UK Pay in 3 rows, while Enhanced does not; do not infer an Enhanced UK Pay in 3 option from the overview.
- Standard is the default financing package; Enhanced adds listed 0% APR monthly tiers. Affirm sets term and cart ranges, which can change at its discretion, and rates can be 10–36% APR subject to eligibility. Businesses with Dashboard access can view or change packages, except connected accounts and platforms. The captures exclude platforms from **Pay in 30 and monthly 0% APR plans**; they list Pay in 4 as 0% APR, so the exclusion is not every 0% plan.

## Product and transaction boundaries

The November support matrix lists full-page Checkout, Payment Links, embedded form, Payment Element, Payment Method Messaging Element, in-app payments, Connect, Invoicing, Customer Portal, Terminal, Checkout Sessions, and PaymentIntents. It excludes Express Checkout Element, Billing, Managed Payments, Radar, SetupIntents, PaymentIntents with `setup_future_usage`, and off-session payments. The capabilities matrix says **no recurring payments**; Invoicing or Customer Portal checkmarks do not imply subscriptions. The May guide specifically excludes Checkout subscription/setup modes and subscription invoices.

Manual capture is listed, while partial, multi, and over-capture are excluded. Extended, flexible extended, incremental, decremental, and re-authorizations are also excluded in the November matrix. Full and partial refunds are supported; partial disputes are not.

## Refunds

Both captures permit submitting full or partial refunds within **120 days of the original payment** through Dashboard or Refunds API. The November guide says processing is asynchronous and takes up to two days; refunds cannot be canceled. Check the Refund object's `status` or Dashboard, and use final `refund.updated` or `refund.failed` events. A failed refund returns the amount to the Stripe balance and requires another customer-refund method. Submission or `pending` is not success.

The November guide says a refund cancels remaining scheduled payments and returns amounts the customer already paid, less interest paid. The May guide instead says Affirm **pauses** the customer plan after initiation. Preserve this as a dated wording difference rather than equating the downstream states. May alone also states multiple partial refunds are possible, processing fees are not credited back, and an active dispute blocks refund creation; these are May-dated details not revalidated by omission in November.

## Disputes and fraud

> [!warning] Dated dispute-timing conflict
> The May capture says customers have **no filing time limit**, Stripe withholds the disputed amount for resolution of up to **30 calendar days from creation**, and Affirm decides within **15 days of evidence submission**. The November capture instead says customers have **120 calendar days from purchase** to file and Affirm issues a decision within **60 calendar days of dispute creation**. The merchant evidence deadline is **15 calendar days from dispute opening/creation** in both. Use the November statement as the newer captured overview; keep the May terms visible as historical claims rather than treating the two timelines as compatible.

On a November-documented dispute, Stripe immediately withholds the disputed amount. Affirm can receive multiple disputes for one payment; each is an independent object requiring its own response and counted in metrics. Email, Dashboard, and `charge.dispute.created` notify the business. The Dashboard and Dispute `reason` and `evidence_due_by` fields identify reason and deadline. In Dashboard, **Needs response → Counter dispute** submits evidence or **Accept dispute** accepts loss; the Disputes API can submit evidence using Files API IDs. A merchant win returns the disputed amount to the Stripe balance; a customer win makes the balance charge permanent. These are documented outcomes, not a guarantee that submitted evidence wins.

The guide says customers authenticate in their Affirm account and Affirm covers losses from **customer fraud**. Stripe may ask the business on Affirm's behalf to stop or pause shipment before losses occur; comply promptly with that request. This is not a blanket protection for all dispute reasons.

## Connect and transaction identity

The **May guide** specifies direct charges, destination charges, and separate charges and transfers. Platforms must enable Affirm and request the connected account's `affirm_payments` capability; correct connected-account MCC matters, and charge type can affect the merchant name displayed at Affirm redirect and merchant-of-record identity. November's generic Connect checkmark does not independently renew those specific configuration claims.

The **November guide** says the customer's bank statement shows Affirm plus a merchant identifier derived from business information or the configured descriptor suffix. Set a custom descriptor on the PaymentIntent before confirmation if desired. After payment completion, expand `latest_charge` on the PaymentIntent; `latest_charge.payment_method_details.affirm.transaction_id` is the Affirm transaction ID for customer support. The identifier is post-completion data, not evidence that a redirect or browser return succeeded.

## Raw Sources

- [[raw/stripe-payments-affirm-2026-11-07|2026-11-07 Affirm overview]] — full newer page capture (426 lines).
- [[raw/stripe-affirm-2025|2026-05-06 Affirm overview]] — prior full page capture (242 lines); historical terms retained, including the original summary's italic-markup normalization and MP4 link note.
