---
title: "Stripe: Buy Now, Pay Later Overview"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-bnpl-overview-2025.md"
tags: [stripe, bnpl, buy-now-pay-later, klarna, affirm, afterpay, installments, payments]
---

## Summary

Overview and support matrices for Stripe's 11 BNPL payment methods. Covers product support (Connect, Checkout, Subscriptions, etc.), API support (PaymentIntents, SetupIntents, manual capture, setup_future_usage), and transaction details (customer countries, repayment options, limits).

## Key Details

**11 BNPL methods**: Affirm, Afterpay/Clearpay, Alma, Billie, Klarna, Kriya, Mondu, Scalapay, SeQura, Sunbit, Zip. Plus Meses sin intereses (Mexico installments).

**All require redirect**. All support PaymentIntents.

**Klarna standout**: only method with SetupIntents, Express Checkout Element, and broadest country coverage (22 countries including US, UK, EU, AU, NZ).

**setup_future_usage support**: Billie, Klarna, Kriya, Mondu, SeQura.

**No manual capture**: Sunbit, Zip.

**Affirm**: US + Canada; $50 min, $30k max; supports Terminal, Subscriptions, manual capture.

**Afterpay/Clearpay**: AU, CA, NZ, UK, US; $1 min, $4k max.

**Zip**: AU + US only; no manual capture, no setup_future_usage.

**Meses sin intereses**: Mexico credit card installments, 3–24 months, 100 MXN/month minimum.

## Raw Sources

- [[stripe-bnpl-overview-2025]] — verbatim webpage content (95 lines)
