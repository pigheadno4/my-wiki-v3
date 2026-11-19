---
title: "Stripe: GrabPay Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/grabpay"
raw_files:
  - "stripe-payments-grabpay-2026-11-07.md"
  - "stripe-grabpay-2025.md"
tags: [stripe, wallets, grabpay, singapore, malaysia, sgd, myr, redirect, otp, branding]
---

## Overview

[[stripe]] describes GrabPay as a single-use Southeast Asian stored-balance wallet. Customers authenticate a payment with a one-time password after a browser or webview redirect to GrabPay. The November capture labels access instant but provisional, payment confirmation immediate, and settlement on the standard payout schedule. Return to the business is an integration step, not proof of a successful PaymentIntent or settled funds. See [[stripe-wallets]]. [November raw lines 5-14, 110-122]

## Eligibility and capability

- The November page lists Singapore and Malaysia as both customer and Stripe-account business locations, with MYR and SGD presentment, domestic coverage and no cross-border support. It lists merchants and Connect platforms/marketplaces, B2B and B2C. This is documented scope, not confirmation that a particular account is enabled or a transaction will succeed. [November raw lines 16-33]
- GrabPay is single-use: recurring payments, Billing, PaymentIntents with `setup_future_usage`, SetupIntents and off-session payments are marked unsupported. The May page explicitly excluded Checkout subscription and setup modes; keep that as a dated restriction, not an inference from November omission. Manual, partial, multi- and overcapture, extended/incremental/decremental/re-authorizations are also marked unsupported. [May raw lines 30-48, 61-71; November raw lines 34-48, 91-105]
- The November matrix marks full-page Checkout, Payment Links, embedded form, Payment Element, in-app payments, Invoicing, Connect, Checkout Sessions and PaymentIntents supported. Express Checkout Element, Payment Method Messaging Element, Customer Portal, Radar, Terminal and Managed Payments are marked unsupported. The shorter May product list did not establish blanket non-support for omitted products. [May raw lines 61-71; November raw lines 81-105]

## Customer and payment states

The customer selects GrabPay and authenticates at GrabPay using an OTP in a browser or webview. The November guide says authentication must complete within 15 minutes **of inactivity**; three incorrect OTP attempts fail authentication. Return to the website or app uses the configured return URL, URL scheme or universal link, where the integration displays the PaymentIntent success or failure result. The May capture described a website redirect; it did not cover these app return paths or time limits. A configured return path and provisional access do not prove the PaymentIntent result. [May raw lines 8-10; November raw lines 110-122]

GrabPay authentication reduces fraud and unrecognized-transaction risk. Stripe describes no standard GrabPay dispute or chargeback process, and says a customer contacting GrabPay might be directed to the merchant for a full or partial refund. OTP does not establish that fraud, complaints or refunds are impossible. [May raw lines 100-102; November raw lines 75-79]

## Refund lifecycle

Full **and partial** refunds are supported in both captures; the prior source's claim that partial refunds were unnoted was incorrect even for May. The maximum submission window is 90 days from the original payment, subject to the merchant's return policy. Refunds are asynchronous and take up to five minutes to complete; the November page says they cannot be canceled after submission. They are separate credits, never reversals, returned by GrabPay to the original wallet balance or linked payment method. [May raw lines 50-52, 96-98; November raw lines 50-67]

Submission is not refund success or customer receipt. Track the Refund object's `status` in the Dashboard/API and `refund.updated` or `refund.failed` events; verify webhook signatures. A successful refund has `succeeded` status. If it `failed`, Stripe returns the amount to the Stripe balance and the business must refund the customer by another method. [May raw lines 96-98; November raw lines 69-73]

## Transaction identity and branding

Stripe sends GrabPay a descriptor from the merchant and payment descriptors, formatted `<merchant descriptor> - <payment descriptor>` when both are present or `STRIPE` when neither is set. GrabPay does not guarantee how it appears to the customer. For Connect direct charges, the descriptor comes from the connected account; for destination charges, it comes from the platform by default. The Charge ID and PaymentIntent ID are separate Stripe IDs. The GrabPay transaction ID is `latest_charge.payment_method_details.grabpay.transaction_id` after expanding or retrieving the PaymentIntent's latest Charge. [November raw lines 124-130]

Use GrabPay's linked brand guidelines when building a checkout page; its linked PDF and logo/button ZIP are navigation, whose current content was not reviewed here. Enable GrabPay in payment method settings for Stripe front-end products; a manually listed payment-method integration uses its separate configuration guide. The November pricing URL contains an `undefined` path segment and supports no fee inference. [May raw lines 104-106; November raw lines 15, 106-108, 132-138]

## Raw Sources

- [[raw/stripe-payments-grabpay-2026-11-07|2026-11-07 full GrabPay overview]] — 138 lines; capabilities, refund and OTP states, descriptor and transaction ID
- [[raw/stripe-grabpay-2025|2026-05-07 GrabPay overview]] — 106 lines; earlier redirect, Checkout restrictions, refund outcome and brand guidance
