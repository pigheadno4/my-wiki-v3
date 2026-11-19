---
title: "Stripe: Accept an FPX Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/fpx/accept-a-payment
original_format: webpage
raw_files:
  - "stripe-fpx-accept-payment-2025.md"
tags: [stripe, fpx, malaysia, myr, checkout, elements, mobile, payouts]
---

## Summary

The May 3, 2026 detailed guide describes FPX Checkout and a legacy Elements `fpxBank` integration, with a short Mobile Payment Element pointer. FPX is a single-use MYR bank redirect for customers in Malaysia. The May Checkout and legacy Elements paths require a six-field post-payment confirmation page; the May guide also provides an 18-bank reference, test states and errors, and separate `fpx` balance guidance. The November 7, 2026 capture of the canonical URL is a variant-navigation index only; it links Checkout, Elements, and Mobile pages but does not restate or update their behavior.

## Key Details

### Checkout path (May 3, 2026)

- Checkout compatibility lists customer geography Malaysia, supported and presentment currency `myr`, payment mode yes, setup mode no, and subscription mode no. Sessions use one-time line items in one currency, with `fpx` in `payment_method_types`; the hosted example uses `success_url`, while the embedded example uses `return_url` and `ui_mode: "embedded_page"`.
- **Required confirmation page for this path:** after payment, display transaction date/time (`Charge.created`), amount (`Charge.amount`), seller order no. (`Charge.statement_descriptor`), FPX transaction ID (`Charge.payment_method_details[fpx][transaction_id]`), buyer bank (`Charge.payment_method_details[fpx][bank]`), and transaction status (`Charge.status`). The May Checkout guide says to get the Charge using the PaymentIntent ID from the Checkout Session.
- The May guide states a refund period up to 60 days and no dispute process. These are dated guide claims, not renewed by the November index.

### Elements path (legacy, May 3, 2026)

- Enable FPX in Dashboard Payment methods settings and accept FPX terms. This guide says the business must be based in Malaysia; it separately labels FPX support for Connect Custom accounts beta. These are merchant and account gates, distinct from the Checkout customer-geography condition.
- Create a server-side MYR PaymentIntent with `payment_method_types: ["fpx"]`. The legacy client flow mounts an `fpxBank` Element and calls `stripe.confirmFpxPayment(clientSecret, {payment_method: {fpx: fpxBank}, return_url})`. The guide marks this `fpxBank` feature legacy and unavailable in the latest Stripe.js; that warning does not establish that all Elements or FPX support ended.
- A bank redirect or return URL is not proof of payment. Test authentication success moves the PaymentIntent from `requires_action` to `succeeded`; failure moves it to `requires_payment_method`. Named offline-bank or processing confirmation errors leave it in `requires_confirmation`. Listen for server-side `payment_intent.succeeded` for fulfillment rather than depending on a client callback. A manual redirect path uses `requires_action` with `next_action.type: redirect_to_url`.
- The return URL can carry `payment_intent` and `payment_intent_client_secret` query parameters for a status lookup. `fpxBank.on('change', ...)` reports the selected bank `value`, `complete`, and `empty`.
- The May amount table says minimum RM2 and maximum RM30,000, but its `invalid_amount` row says greater than RM2 and less than RM30,000. The exact endpoint eligibility is unresolved in this capture. MYR is required.
- Test error banks: `test_offline_bank` → `offline_bank`; `test_processing_error` → `payment_method_processing_error_transient`. Other listed errors are `invalid_amount`, `invalid_bank`, `invalid_currency`, `missing_parameter`, and `payment_method_not_available`.
- The May legacy Elements guide calls FPX single-use, says it cannot be used for recurring or additional payments, and says it is not supported with Stripe Billing. This conflicts with the broader bank-redirects concept's `send_invoice` subscription statement; the November index does not resolve that difference.
- The May legacy path requires the FPX logo, buyer-bank selection using the bank reference, and FPX terms wording on its checkout page. Its post-authentication confirmation page requires the same six Charge fields listed above. The guide says Charge details can be obtained from `payment_intent.succeeded`; direct `PaymentIntent.charges.data` access is described only for API version 2022-08-01 or older.

### Mobile pointer (May 3, 2026)

- The short May mobile section repeats Dashboard FPX enablement, terms acceptance, and Malaysia-based business eligibility, then points to the Mobile Payment Element for Android, iOS, or React Native. It contains no complete native implementation steps. The November index has a Mobile variant link, but its variant body was not captured here.

### FPX balance and payouts (May 3, 2026)

- The May guide says FPX funds settle in a separate `fpx` balance and may produce a separate automatic payout from other funds. Connect platforms can specify `source_type: "fpx"` when creating a payout or transfer from that balance; inspect available and pending amounts by source type. A successful PaymentIntent alone does not prove funds are available or a payout occurred.

### 18-bank reference (May 3, 2026)

`affin_bank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2e`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-fpx]], [[stripe-bank-redirects]]

## Related raw API references

- [[raw/stripe-payments-fpx-accept-a-payment-2026-11-07|November 7, 2026 FPX variant index]] — navigation only; links Checkout, Elements, and Mobile variants; no variant behavior captured.

## Raw Sources

- [[raw/stripe-fpx-accept-payment-2025|May 3, 2026 detailed FPX guide]] — Checkout, legacy Elements, short Mobile pointer, bank reference, errors, and balance guidance.
