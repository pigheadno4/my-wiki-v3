---
title: "Stripe: Accept an FPX Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-fpx-accept-payment-2025.md"
tags: [stripe, fpx, malaysia, myr, checkout, elements, payouts]
---

## Summary

Integration guide for accepting FPX payments via Checkout and Elements (legacy). Key: mandatory confirmation page with 6 specific transaction fields; FPX funds settle in a separate `fpx` balance; 18-bank reference table; error codes and test banks.

## Key Details

### Checkout path

- `payment_method_types: ['fpx']`, `myr`, payment mode only
- **Mandatory confirmation page**: must display transaction date/time, amount, seller order no., FPX transaction ID (`payment_method_details[fpx][transaction_id]`), buyer bank name, transaction status — all from Charge object

### Elements path (Legacy)

- `fpxBank` element + `stripe.confirmFpxPayment()` + `return_url`
- Min RM2, max RM30,000 per transaction
- Test: select any bank → Pay (success); click "Fail test payment" (failure)
- Test error banks: `test_offline_bank` → `offline_bank`; `test_processing_error` → `payment_method_processing_error_transient`
- `fpxBank.on('change', ...)` → gets `value` (bank name), `complete`, `empty`

### FPX balance and payouts

- FPX funds settle in separate `fpx` balance — may produce 2 payouts per day
- Use `source_type: 'fpx'` when creating payouts/transfers from Connect platforms

### 18 supported banks

affin_bank, alliance_bank, ambank, bank_islam, bank_muamalat, bank_rakyat, bsn, cimb, hong_leong_bank, hsbc, kfh, maybank2e, maybank2u, ocbc, public_bank, rhb, standard_chartered, uob

### Error codes

`invalid_amount`, `invalid_bank`, `invalid_currency`, `missing_parameter`, `offline_bank`, `payment_method_not_available`, `payment_method_processing_error_transient`

## Raw Sources

- [[stripe-fpx-accept-payment-2025]] — verbatim webpage content (529 lines, Checkout + Elements legacy + Mobile section)
