---
title: "Stripe Docs — Instant Bank Payments"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-instant-bank-payments-2025.md"
tags: [stripe, instant-bank-payments, link, ach, bank-debit, us-only, recurring, guaranteed-settlement, cash-back]
---

## Summary

Comprehensive overview of Instant Bank Payments — Link's US bank account payment option that delivers instant confirmation, 2-day settlement, and guaranteed settlement vs bank-initiated ACH returns.

## Key Facts

- **US only, USD only**; auto-enabled with Link; subject to eligibility
- **Settlement**: 2-day (card parity); Stripe guarantees vs bank-initiated returns; customer-initiated disputes still debit balance + fee
- **Default transaction limit**: < $5,000 (dynamic risk threshold)
- **Recurring/off-session**: Yes; **Manual capture**: Yes; **Connect**: Yes
- **Supported integrations**: Checkout, Payment Links, Hosted Invoice Page, Payment Element, Mobile Payment Element

## ACH Interaction Rule

IBP and ACH Direct Debit cannot coexist. ACH always wins:
- Explicit `us_bank_account` in `payment_method_types` → IBP never shown
- Dynamic PMs: ACH-eligible transaction → IBP suppressed
- Workaround: use PM rules to restrict ACH eligibility; non-ACH transactions show IBP

## Stripe-Funded Promotions

Cash back/credits funded entirely by Stripe; merchant receives full amount; promotional amount deposited to customer within 7 business days; configurable in Link settings.

## Testing

- **Success**: authorized payment
- **Disputed**: authorized then customer-initiated dispute
- **Blocked**: payment declined by risk
- **Non-OAuth Bank**: any credentials work; keywords `options`/`mfa`/`confirm_mfa`/`security_question`/`error`/`incorrect`
- **OAuth Bank**: test OAuth popup
- **Failure modes**: Down (Scheduled), Down (Unscheduled), Down (Error)

## CDN Assets (9 screenshots)

- `raw/assets/stripe-ibp-bank-tab.png` — bank selection tab (93 KB)
- `raw/assets/stripe-ibp-consent.png` — Link agreement page (78 KB)
- `raw/assets/stripe-ibp-sign-up.png` — Link sign-up (64 KB)
- `raw/assets/stripe-ibp-oauth.png` — bank OAuth login (132 KB)
- `raw/assets/stripe-ibp-success.png` — success page (29 KB)
- `raw/assets/stripe-ibp-returning.png` — returning customer welcome back (77 KB)
- `raw/assets/stripe-ibp-otp.png` — 2FA code entry (55 KB)
- `raw/assets/stripe-ibp-saved.png` — saved account selection (73 KB)
- `raw/assets/stripe-ibp-settlement-timing.png` — 2-day settlement diagram (13 KB)

## Related Pages

- [[stripe-instant-bank-payments]] — concept page
- [[stripe-link]] — Link concept page (IBP is Link-exclusive)
- [[source-stripe-ach-direct-debit]] — ACH Direct Debit (competing method)
- [[stripe-payment-method-rules]] — PM rules (workaround for ACH/IBP conflict)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-instant-bank-payments-2025]] — verbatim webpage content (185 lines)
