---
title: "Stripe Docs — Payment method support"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payment-method-support-2025.md"
tags: [stripe, payment-methods, integration-matrix, product-support, api-support, bnpl, wallets, bank-debits]
---

## Summary

Comprehensive reference page covering country/currency support, product support matrices, and API support for all Stripe payment methods. Primary reference for "does PM X work with product Y?" questions.

## Country / Currency Table (36 Payment Methods)

Key entries with notable constraints:

- **Stablecoin payments**: USD, US business location only, worldwide customers
- **Zip**: AUD/USD, AU/US — invite only
- **Pix**: BRL; BR (invite only) + US business locations; BR customers
- **Pay by Bank**: GBP, GB only
- **Alma**: EUR, FR only
- **Konbini**: JPY, JP only
- **PayNow**: SGD, SG only
- **PromptPay**: THB, TH only
- **FPX**: MYR, MY only

## Product Support Highlights

### BNPL methods not covered in individual sources yet
Billie, Kriya, Mondu, Scalapay, SeQura, Sunbit — all support Connect, Checkout (payment mode only), Payment Links, Payment Element; none support subscriptions, invoicing, ECE, or Terminal.

### Notable constraints
- **BLIK**: Checkout requires payment mode; no Subscriptions/Invoicing
- **TWINT**: Checkout requires payment mode; no Subscriptions/Invoicing
- **Bancontact / EPS / FPX / P24**: Subscriptions/Invoicing use `send_invoice` only
- **iDEAL/Wero**: Subscriptions only in subscription mode; no `charge_automatically`; single-use (customer authenticates each payment)
- **Bank transfers**: Checkout payment mode only; no Payment Links/ECE/Mobile PE
- **Pre-authorized debit (ACSS)**: Checkout payment mode only; no Payment Links; PE has deferred setup limitations
- **Affirm**: Only BNPL in Terminal
- **Klarna**: Only BNPL in Express Checkout Element (no `setup_future_usage` saving)
- **Afterpay**: Invoicing private preview only

## API Support Table

The API support section shows per-PM support for:
- `setup_future_usage` (on_session vs off_session vs neither)
- `return_url` requirement
- Webhook availability

Cards and bank debits support both `on_session` and `off_session`. Most other PMs only support `off_session` or neither.

## Related Pages

- [[stripe-payment-methods]] — payment methods concept page
- [[source-stripe-payment-methods-overview]] — primary overview source
- [[source-stripe-bank-debits]] — bank debits detail
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-method-support-2025]] — verbatim webpage content (344 lines)
