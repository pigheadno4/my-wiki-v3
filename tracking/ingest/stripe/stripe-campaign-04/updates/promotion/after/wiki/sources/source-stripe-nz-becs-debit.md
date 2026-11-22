---
title: "Stripe: New Zealand BECS Direct Debit Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/nz-bank-account"
raw_files:
  - "stripe-payments-nz-bank-account-2026-11-07.md"
  - "stripe-nz-becs-debit-2025.md"
tags: [stripe, nz-becs, becs, new-zealand, nzd, bank-debit, mandates, disputes]
---

## Summary

The May 3 and November 7, 2026 overviews describe a reusable, business-initiated, delayed NZD bank debit for New Zealand bank accounts. The payment method is `nz_bank_account`. A customer's Direct Debit Authority (DDA) authorizes Stripe to make debits. Submission, final payment outcome, and funds availability are distinct.

## Eligibility and limits

The November overview describes domestic NZD payments for New Zealand customers and New Zealand Stripe accounts, including merchants and Connect platforms or marketplaces, for B2B or B2C. Access requires approval. Request access in Payment methods settings and complete the additional identity checks when prompted. Prohibited merchant category codes (MCCs) are ineligible. A business with a restricted MCC may qualify and must provide additional information when creating the account. The separate list of prohibited or restricted business categories is at lines 309–324.

The minimum is **NZD 0.50** and the scheme maximum is **NZD 999,999,999.99**. The default per-transaction account limit and initial weekly volume limit are **NZD 10,000 each**. Both applicable account limits apply. They can differ with approval or increases. See November lines 18–69 for category and limit details.

## Product support and off-session scope

The May overview listed Connect, Checkout, Payment Links, Subscriptions, Invoicing, and Elements generally. The November overview specifies:

| Area | Listed support in November |
| --- | --- |
| Checkout UI | Full page (recommended), Payment Links, embedded form, and Payment Element. Express Checkout Element, Payment Method Messaging Element, and in-app payments are excluded. |
| Products | Billing, Invoicing, Customer Portal, and Connect. Managed Payments, Radar, and Terminal are excluded. |
| APIs and capabilities | Checkout Sessions (recommended), PaymentIntents, PaymentIntents with `setup_future_usage`, SetupIntents, and recurring payments. The API grid marks off-session payments unsupported. |
| Authorization and capture | Extended, flexible extended, incremental and decremental authorizations and reauthorizations are excluded. Manual, partial, multi-, and over-capture are excluded. |

The November [[source-stripe-nz-becs-accept-payment|acceptance guide]] sets `setup_future_usage=off_session` when creating the initial PaymentIntent. After that Intent succeeds, the generated PaymentMethod attaches to the object representing the customer. In the November [[source-stripe-nz-becs-set-up-payment|setup guide]], a successful SetupIntent creates a new PaymentMethod attached to that object. Both guides show later server requests to create an NZD PaymentIntent using the saved PaymentMethod, with `confirm=true` and `off_session=true`, for either a customer-configured Accounts v2 Account or a Customers v1 Customer. Both May integration guides have earlier Customers v1 examples. The November examples and the overview's **Off-session payments unsupported** cell leave product scope and account eligibility unresolved. Saving a method or sending a request does not establish a successful debit or off-session availability.

## Debit submission, outcome, and settlement

| Dated statement | Time and reference point |
| --- | --- |
| May overview result notification | Up to two business days after initiating the debit. |
| Both overviews' standard settlement table | T+2 business days after submission at 00:00 UTC for payment success and availability in the Stripe balance. The cutoff is 18:20 Pacific/Auckland. |
| November acceptance guide result notification | Within three business days after Stripe submits the debit, for PaymentIntent success or failure. |

Both overviews say payments are generally submitted the day they are created, with next-business-day handling when created after cutoff or on a non-business day. The November checkout flow confirms submission for processing first. Wait for success or failure as a separate outcome. See the acceptance guide's `payment_intent.processing`, `payment_intent.succeeded`, and `payment_intent.payment_failed` routes. A Charge's `payment_method_details.expected_debit_date` is an estimate. It can appear in the API and Charge update, success, and failure events when Stripe can determine it.

## Mandates and customer emails

Checkout and Payment Element collect the account holder name, email, bank account details, and agreement to the NZ BECS Direct Debit Service Terms and Conditions. If using other collection, display the terms and confirm acceptance. For a mandate created by SetupIntent, read `SetupIntent.mandate` and retrieve it via `GET /v1/mandates/{id}`. The Dashboard also displays mandate details.

Customers can cancel via their bank or the merchant. Detach the PaymentMethod to inactivate the mandate in Stripe, and establish a new DDA before further authorized debits. `mandate.updated` can signal inactivation when the customer cancels or after a permanent debit failure.

- **Mandate confirmation.** The May overview says within five days of establishing the mandate. The May acceptance and setup samples say five business days after the customer's DDA confirmation. The November overview and both November samples say five days. The November overview describes Stripe's default immediate email after mandate collection, including successful PaymentIntent confirmation or SetupIntent success when used to collect the mandate. The email includes mandate date, Stripe New Zealand Limited's authorization code 3143978 and role, applicable terms, bank and account details, any distinct authorized signatory, and merchant contact information.
- **Debit notification.** The May overview says on the day of each debit. November says **no later than the day of each debit**. Both distinguish Stripe's default immediate send after every successful PaymentIntent confirmation. The email contains the amount, debit date, Stripe New Zealand Limited debit and statement notices, and merchant contact details. Contact Stripe Support to disable Stripe emails and send custom notices.

## Disputes and refunds

- **Disputes.** A customer can dispute whether the DDA authorizes a debit for up to nine months from the first payment. Missing or mismatched notice permits a dispute for up to 120 days from the individual payment. November limits disputes to the full payment amount. `charge.dispute.created` identifies dispute creation. Stripe immediately removes funds if the customer's bank rules for the customer and requests their return.
- **Refunds.** Both overviews describe full or partial refunds within 90 days of the original payment, typically processed in three to five business days, and warn that a concurrent bank dispute can result in a double credit. A refund appears as a bank statement credit referencing the original descriptor.
- **Dated refund states.** May says a refund requested before payment completion begins when the PaymentIntent reaches `succeeded`, and is marked canceled if the payment fails and the Intent enters `requires_payment_method`. November says a refund request before debit submission cancels the payment. After submission, the refund remains pending until payment succeeds and is marked failed if the payment fails. Retrieve the Refund to check its status. The two descriptions give distinct scopes and status wording.

## Billing retries and statement descriptors

The May guide labeled automatic insufficient-funds retries private preview. November documents configurable automatic retries for payments that fail due to insufficient funds on recurring subscription invoices, one-off invoices, or both. Stripe can retry an eligible failure once, no more than 30 days after the original attempt. Stripe charges no debit failure fee for attempts it initiates automatically. The capture leaves the feature's general availability undetermined.

The November descriptor rules use the payment-level descriptor before the account-level default, use the first 12 characters, and fall back to the business name and then Stripe. For Connect direct charges, use the connected account's default. For destination charges and separate charges and transfers, use the platform's default even with `on_behalf_of`. The actual statement may instead say “Stripe New Zealand Limited.”

## Related Pages

- [[stripe]] — payment provider
- [[stripe-nz-becs-debit]] — NZ BECS Direct Debit concept and dated integration scopes
- [[source-stripe-nz-becs-migrate-from-processor]] — separate route for migrating existing mandates

## Raw Sources

- [[raw/stripe-payments-nz-bank-account-2026-11-07|2026-11-07 NZ BECS Direct Debit overview]]
- [[raw/stripe-nz-becs-debit-2025|2026-05-03 NZ BECS Direct Debit overview]] — reuses three flow illustrations from `raw/assets/stripe-acss-debit-*.svg`
