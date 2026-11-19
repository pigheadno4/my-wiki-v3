---
title: "Stripe: Use iDEAL | Wero to Set Up Future SEPA Direct Debit Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ideal/set-up-payment"
raw_files:
  - "stripe-ideal-set-up-payment-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, sepa-debit, iban, setup-intents, mandates, ios, android, react-native]
---

## Summary

The detailed 2026-05-03 guide uses an iDEAL | Wero SetupIntent to collect a mandate and bank details for later SEPA Direct Debit. It describes an actual 0.01 EUR iDEAL payment: the customer authenticates, Stripe refunds the payment, and the customer's IBAN is stored in a generated SEPA Direct Debit PaymentMethod. This is a setup payment, not the later SEPA charge or a purchase payment. The 2026-11-07 capture at the same canonical URL is only a purpose sentence and a chooser for Checkout, Elements, iOS, Android, and React Native variants; it does not restate or supersede implementation behavior.

## Key Details

### Preconditions and customer identity (2026-05-03 guide)

- Activate SEPA Direct Debit in the Dashboard and comply with both iDEAL and SEPA Direct Debit terms (old raw lines 12-14).
- Associate the payment method with a customer-configured Account v2 or Customer v1 and use the corresponding `customer_account` or `customer` field throughout setup and later charging (old raw lines 24-34, 142-189).
- In this dated guide, Accounts v2 is generally available for Connect users but is public preview for other Stripe users, who need a preview version. Treat that as a May 2026 statement, not November-verified eligibility (old raw lines 26-34).

### Setup paths and mandate (2026-05-03 guide)

- Checkout creates a Session in `mode: "setup"` with `ideal` included in `payment_method_types` and the customer identity. Its examples include `["card", "ideal"]`; Stripe-hosted and embedded pages use different success/return URL fields (old raw lines 68-140).
- Elements creates a customer-associated SetupIntent and uses `stripe.confirmSetup` with a return URL (old raw lines 262-300, 433-531). The guide's Stripe.js dahlia example is dated, not a November-confirmed version (old raw lines 305-316).
- Native iOS, Android, and React Native variants create a customer-associated SetupIntent with `ideal` and confirm it on the client with `STPPaymentHandler.confirmSetupIntent`, `PaymentLauncher.confirm`, or `confirmSetupIntent`, respectively. Bank redirects and app return/deep-link handling matter in these clients (old raw lines 788-889, 1147-1237, 1469-1600, 1713-1773).
- The mobile variants explicitly tell the merchant to collect a SEPA mandate agreement, display standard authorization text shown in seven languages, and communicate the accepted terms in the form or by email. Do not extend that specific manual-display instruction to hosted Checkout or Payment Element solely from this guide (old raw lines 831-863, 1157-1189, 1531-1564).

### Later charge, events, and tests (2026-05-03 guide)

- After setup, retrieve the SetupIntent with `expand: ["latest_attempt"]` and obtain `latest_attempt.payment_method_details.generated_sepa_debit`. For a later charge, create a separate `sepa_debit` PaymentIntent with that PaymentMethod and the same Account v2 or Customer v1 identity (old raw lines 142-189, 538-586, 892-939).
- The old guide recommends handling `setup_intent.succeeded` asynchronously rather than relying on a client callback. A browser/app return or successful setup is not evidence that a later SEPA charge succeeded or settled (old raw lines 623-627).
- In test mode, authorization moves the SetupIntent from `requires_action` to `succeeded`; failed authentication moves it to `requires_payment_method`. The six example billing-email and six PaymentMethod-token patterns test a *later* SEPA PaymentIntent moving from `processing` to success or failure, including delayed outcomes, an immediate dispute after success, and insufficient funds. These are dated test cases, not live outcome guarantees (old raw lines 588-621, 942-975).

## Capture and evidence boundary

The 2026-11-07 raw at this canonical URL lists five variant links, without the variant bodies. The collection diff replaces the older long body with this navigation index. It establishes no substantive change to prerequisites, API behavior, SDK versions, mandate presentation, or outcomes. The linked November variants were not captured here; use the 2026-05-03 guide only as dated implementation evidence.

## Related

- [[stripe]] — Stripe company route.
- [[stripe-ideal]] — iDEAL | Wero concept and related Stripe source routes.
- [[stripe-sepa-debit]] — SEPA Direct Debit payment method used for subsequent charges.

## Raw Sources

- [[raw/stripe-ideal-set-up-payment-2025|2026-05-03 full iDEAL | Wero setup guide]] — factual implementation and test evidence; 1,777 lines.

## Related raw API references

- [[raw/stripe-payments-ideal-set-up-payment-2026-11-07|2026-11-07 canonical iDEAL | Wero variant index]] — navigation-only capture of Checkout, Elements, iOS, Android, and React Native links; no variant behavior inferred.
