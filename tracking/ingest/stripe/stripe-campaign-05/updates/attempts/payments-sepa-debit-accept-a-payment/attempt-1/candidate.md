---
title: "Stripe: Accept a SEPA Direct Debit Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/sepa-debit/accept-a-payment"
raw_files:
  - "stripe-sepa-accept-payment-2025.md"
tags: [stripe, sepa, sepa-debit, eu, eur, iban, checkout, elements, react-native, mandates, test-ibans]
---

## Overview

The May 3, 2026 guide documents SEPA Direct Debit acceptance through Checkout, web Elements and React Native. It covers EUR pricing, customer IBAN and mandate acknowledgement, delayed payment outcomes, optional mandate-reference prefixes and scheduled debits. The November 7, 2026 capture links to the three variants.

## Checkout

The May Checkout guide documents payment, setup and subscription modes. All line-item Prices must use EUR. Dynamic payment methods can select relevant methods automatically, or merchants can manually include `sepa_debit` in the captured `payment_method_types` examples. The Checkout introduction describes funds typically arriving in five business days. For standard settlement measured from submission and the separate six-business-day guidance, see [[source-stripe-sepa-debit]].

## Web Elements and React Native

In the May examples, the merchant’s server creates an EUR PaymentIntent and the customer supplies an IBAN and acknowledges the mandate. The May Elements guide recommends Stripe’s prebuilt Checkout page to collect mandates when processing with the Stripe Creditor ID.

On web, the Payment Element collects bank details and presents the mandate. Stripe.js `confirmPayment` submits the existing PaymentIntent using its client secret. In React Native, the merchant collects the IBAN, presents the mandate terms and submits using the React Native SDK’s `confirmPayment`. The React Native guide requires `addressCountry` and `addressLine1` in `billingDetails` for certain IBAN country codes, including GB and CH. See the May guide’s React Native **Submit the payment to Stripe** section for the full list.

Stripe moves a successfully submitted PaymentIntent from `requires_confirmation` to `processing`. The May guide uses `payment_intent.processing` to wait, `payment_intent.succeeded` to fulfill, and `payment_intent.payment_failed` to request a different method. For reuse, the guide specifies `setup_future_usage: off_session`. In the web Elements flow, Stripe attaches the PaymentMethod at `processing` to the customer-configured Account passed as `customer_account` (Accounts v2) or the Customer passed as `customer` (Customers v1), regardless of the eventual debit result.

## Mandate references, scheduled debits and servicing

- **Reference prefix**. Optional `payment_method_options.sepa_debit.mandate_options.reference_prefix` accepts up to 12 characters. It must start with a digit or uppercase letter. The remaining characters may be uppercase letters, digits, spaces, or `.`, `/`, `&`, `-` and `_`. The prefix cannot start with `STRIPE`. A valid prefix produces a 24-character reference.
- **Target debit date**. The May Checkout and Elements sections describe a best-effort `target_date` 3–15 days ahead. A non-business day or a date fewer than three business days ahead defers the debit to the next available business day. The Elements section says a PaymentIntent created with a target date can be canceled up to three business days before that date.
- **Refunds and disputes**. The May Checkout section summarizes refunds up to 180 days after payment and customer disputes through the bank up to 13 months after payment, with no appeal. See [[source-stripe-sepa-debit]] for the product guide’s dispute-window qualifications.

## Test IBANs

The May Checkout and Elements tables each cover 19 test-country headings with eight scenarios per heading. They cover success, delayed success, failure, delayed failure, a dispute following success, weekly payment-volume or transaction limits, and insufficient funds. Test fixtures establish test coverage. The exact IBANs, token names and failure codes are in the May capture’s **Test IBANs** sections.

## Related

- [[stripe-sepa-debit]] — Stripe SEPA Direct Debit concept
- [[source-stripe-sepa-debit]] — payment method, settlement and dispute reference
- [[source-stripe-sepa-set-up-payment]] — save a payment method for future use
- [[source-stripe-subscriptions-sepa-debit]] — subscriptions
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-sepa-accept-payment-2025|May 3, 2026 SEPA Direct Debit acceptance guide]] — Checkout, web Elements and React Native, including test fixtures and configuration.

## Related raw API references

- [[raw/stripe-payments-sepa-debit-accept-a-payment-2026-11-07|November 7, 2026 acceptance variant index]] — navigation to Checkout, Elements and React Native.
