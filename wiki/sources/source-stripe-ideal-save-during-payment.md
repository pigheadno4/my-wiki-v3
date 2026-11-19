---
title: "Stripe: Save Bank Details During an iDEAL | Wero Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ideal/save-during-payment"
raw_files:
  - "stripe-ideal-save-during-payment-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, sepa-debit, iban, mandates, save-payment-method, ios, android, react-native]
---

## Overview

The 2026-05-03 guide describes saving a customer's IBAN from an initial iDEAL | Wero payment as a generated SEPA Direct Debit PaymentMethod for later payments. It covers Elements, iOS, Android and React Native. The 2026-11-07 capture at the canonical URL is a variant index with the same stated purpose; it contains no integration details. Its linked variants were not captured here, so the detailed flow below remains dated May evidence. See [[stripe]], [[stripe-ideal]], [[stripe-sepa-debit]] and [[stripe-saved-payment-methods]].

## Key details from the 2026-05-03 guide

- The guide says to activate SEPA Direct Debit in the Dashboard and comply with both iDEAL and SEPA Direct Debit terms before using this setup. Its server flow creates a Customer, then an initial EUR PaymentIntent with `payment_method_types: ["ideal"]`, that `customer`, and `setup_future_usage: "off_session"`. It says there is no minimum charge amount and iDEAL | Wero supports no other currency. These are historical instructions, not evidence of November account eligibility.
- The Elements variant uses the Payment Element and web `stripe.confirmPayment({elements, confirmParams: {return_url}})`. It describes collecting payment details and mandate acknowledgement, but does not print the seven-language standard authorization text in that web section. For live checkout it calls for HTTPS and Stripe.js loaded from js.stripe.com. See the old raw's Elements section and return-page status examples.
- The iOS, Android and React Native variants collect full name and email and explicitly direct the merchant to obtain a SEPA mandate agreement and display standard authorization text, shown in seven languages (de, en, es, fi, fr, it, nl); the text's business name must be replaced and terms communicated in the form or by email. These dated mobile examples use `STPPaymentHandler.shared().confirmPayment`, Android `stripe.confirmPayment(this, confirmParams)` (the captured Gradle sample pins `stripe-android:23.5.0`), and React Native `confirmPayment(clientSecret, {paymentMethodType: 'Ideal', ...})`, respectively. React Native's captured bank-return example uses a custom URL scheme and `handleURLCallback`. Do not apply a single web SDK call or mandate presentation snippet to every platform.
- After the initial iDEAL payment, the guide locates the generated SEPA method by retrieving that PaymentIntent with `expand: ["latest_charge"]` and reading `latest_charge.payment_method_details.ideal.generated_sepa_debit`. A later debit uses a distinct `sepa_debit` PaymentIntent with that PaymentMethod and `confirm: true`; its examples use `customer_account` for Accounts v2 or `customer` for Customers v1. The generated ID is a lookup from the relevant completed initial flow, not something established by creating or redirecting an intent.
- A bank redirect or `requires_action` response is not payment success. The web return page retrieves the initial PaymentIntent and distinguishes `succeeded`, `processing` and `requires_payment_method`. The later SEPA intent has its own asynchronous outcome. The guide advises listening for Stripe payment events instead of relying on a client callback for business actions.

## Test patterns in the 2026-05-03 guide

The old raw gives test-mode authorization/failure actions for the initial iDEAL intent and six generated SEPA email and PaymentMethod patterns for later-intent transitions: succeed, delayed success, fail, delayed failure, succeeded then disputed, and insufficient funds. These are test cases; neither confirming a later intent nor a test token proves a live debit succeeds. Exact emails, tokens and state descriptions are in the old raw's “Test your SEPA Direct Debit integration” sections.

## Detail locators

- Old raw lines 8-22: purpose, recommendation, SEPA activation and terms, Elements scope.
- Old raw lines 37-65: Customer and initial EUR iDEAL PaymentIntent with future usage.
- Old raw lines 138-212 and 288-319: web Payment Element setup and `stripe.confirmPayment`; lines 388-440: return-page status inspection.
- Old raw lines 505-590: generated method lookup and separate Accounts v2/Customers v1 later intent; lines 593-632: test states and event handling.
- Old raw lines 877-951, 1204-1305 and 1565-1661: iOS, Android and React Native billing details, mandate text and distinct confirmation calls; lines 1812-1872: React Native deep linking.

## Related raw API references

- [[raw/stripe-payments-ideal-save-during-payment-2026-11-07|2026-11-07 variant navigation index]] — routes to Elements, iOS, Android and React Native; the linked variants were not captured in this order, and this index supplies no behavioral update.

## Raw Sources

- [[raw/stripe-ideal-save-during-payment-2025|2026-05-03 full guide, Elements and mobile variants]] — dated factual authority for the flow and examples above.
