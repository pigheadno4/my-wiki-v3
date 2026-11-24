---
title: "Stripe: PayTo Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payto"
raw_files:
  - "stripe-payments-payto-2026-11-07.md"
  - "stripe-payto-2025.md"
tags: [stripe, real-time-payments, payto, australia, aud, mandates, recurring, billing, connect, disputes]
---

## Overview

PayTo (`payto`) is a real-time Australian payment method for one-time and recurring AUD payments. The November 7, 2026 overview specifies domestic coverage, Australian businesses and customers, and approval for eligible merchants and Connect platforms or marketplaces serving B2B or B2C. Request access in Payment methods settings and complete additional identity verification before accepting payments. Stripe can review an account after activation. The November **Account eligibility** and **Verification requirements** sections list the qualifications and seven prohibited merchant category codes.

A customer gives a PayID or their BSB and bank account number. Their bank typically sends a push notification or email to request mandate authorization. The customer authenticates and approves via mobile or online banking. Both dated overviews say Stripe typically reports the final payment status within 60 seconds after authorization. Confirm actual payment success from that result. Settlement follows the standard payout schedule.

## Transaction and bank limits

The November method minimum is AUD 0.50. The default per-transaction account limit is AUD 10,000. Approved accounts may accept up to the AUD 100,000 method maximum. The customer's bank can also apply its own mandate limits.

Both dated bank tables list 43 institutions. ANZ, CBA, Westpac and Macquarie reject mandates over AUD 25,000 and mandates with no maximum amount. Westpac separately declines ad hoc payments over AUD 1,000 for high-risk merchants. CBA may require call-center approval for high-risk mandates. PayTo tends to perform best with recurring payments and payments under AUD 1,000, with performance varying by bank, account type and payment frequency. Business bank account coverage is lower than individual-account coverage. See the dated raw tables for bank-specific details.

## Mandates

The customer authorizes the required mandate through their bank. The November overview says merchants need no separate legal mandate text for this method. Stripe automatically configures a one-off mandate for a fixed payment amount, `adhoc` cadence and one payment, starting at confirmation with no end date. Merchants can override the inferred `purpose` with a valid value.

For recurring collection, use the least permissive terms under `payment_method_options.payto.mandate_options`. The documented fields are `amount`, `amount_type`, `payment_schedule`, `purpose`, `start_date`, `end_date` and `payments_per_period`. A `fixed` mandate requires an amount the charge must equal. The default `maximum` allows charges at or below the stated amount. Set a ceiling because several banks reject mandates without one. The recurring cadence defaults to `adhoc`, the end date defaults to none, and the default is one payment per period except for an ad hoc cadence, where the default is no count limit. See the November **Mandate options** table for field-specific detail.

Retrieve the Mandate and inspect `payment_method_details.payto`. Detaching the PaymentMethod cancels the mandate. Customers can also revoke it using mobile banking or by contacting their bank.

## Refunds and disputes

Request full or partial refunds in the Dashboard or Refunds API within two years of the original payment. Multiple partial refunds can total up to the original payment. Customers typically receive funds in minutes, but some banks take several days. For payments made with PayID, `payment_method.billing_details.name` must match the bank-account name. A mismatch can cause the refund to fail. Check the refund in the Dashboard or retrieve the Refund and inspect its status.

The November profile supports full disputes only. Stripe deducts the disputed amount and associated fee from the Stripe balance and sends `charge.dispute.created` and `charge.dispute.closed`. Verify event signatures. PayTo disputes are final, with no merchant evidence or appeal path. If a customer agrees to return the funds after resolving the dispute with the merchant, the customer must make a new payment.

## Product support and off-session qualification

The May 6, 2026 guide documents Checkout Sessions, Payment Element or Direct API acceptance, Billing and Payment Links. In November, the PayTo profile lists full-page or embedded Checkout, Payment Links, Payment Element, Billing, Invoicing, Customer Portal, Radar and Connect. It marks Express Checkout Element, Payment Method Messaging Element, in-app payments, Managed Payments and Terminal unsupported. It marks manual, partial, multi- and over-capture unsupported. Enable PayTo in Payment methods settings for automatic front-end selection, or follow the separate acceptance guide when manually listing methods.

The November PayTo profile lists recurring payments, SetupIntents and Payment Intents with `setup_future_usage` as supported, with Off-session payments marked unsupported. The separate November [[source-stripe-payment-method-support|payment method support matrix]] lists PayTo future usage as supported. Its footnote says non-card and non-bank-debit methods that support `setup_future_usage` support `off_session` only. These dated entries leave the concrete off-session flow and Billing `charge_automatically` unresolved. Mandate authorization and the Billing product label alone establish neither outcome.

## Connect and reconciliation

May lists direct charges, destination charges, and separate charges and transfers. Both overviews direct platforms to request the connected account's `payto_payments` capability through the Capabilities API for Express or non-Stripe-hosted dashboards.

In November, the customer’s bank statement includes the business name and payment reference. Text, order and truncation depend on the bank. For destination charges, the statement uses the platform identity if `on_behalf_of` is omitted and the connected account identity if it is set. Stripe provides no separate PayTo network transaction ID.

## Related

- [[stripe-real-time-payments]] — Stripe real-time payment methods and dated product comparisons
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-payto-2026-11-07|November 7, 2026 PayTo product overview]] — full capture, including eligibility, limits, bank directory, refunds, mandates and Connect statement details.
- [[raw/stripe-payto-2025|May 6, 2026 PayTo product overview]] — earlier merchant, bank, transaction and Connect documentation.

## Related raw API references

- [[raw/stripe-payments-payto-accept-a-payment-2026-11-07|November 7, 2026 PayTo acceptance index]] — navigation to Checkout, Elements and Direct API.
- [[raw/stripe-payments-payto-save-during-payment-2026-11-07|November 7, 2026 PayTo pay and save index]] — navigation to Checkout, Elements and Direct API.
- [[raw/stripe-payments-payto-set-up-payment-2026-11-07|November 7, 2026 PayTo setup index]] — navigation to Checkout, Elements and Direct API.
