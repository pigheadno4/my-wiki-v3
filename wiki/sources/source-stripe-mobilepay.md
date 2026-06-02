---
title: "Stripe: MobilePay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-mobilepay-2025.md"
tags: [stripe, wallets, mobilepay, denmark, finland, dkk, eur, card-wallet, 3ds, manual-capture, dankort, fees]
---

## Summary

Overview of Stripe's MobilePay integration — Denmark and Finland card wallet. Underlying card transaction processed invisibly. Manual capture supported. 3DS occurs 1–7% of transactions (invisible, handled by MobilePay). Dankort not supported. Extra fees: per-transaction + 35 DKK/month for Denmark businesses.

## Key Details

**API enum**: `mobilepay`. Denmark and Finland customers. DKK, EUR, NOK, SEK. 30 European merchant countries.

**Card wallet**: underlying Visa/Mastercard transaction processed invisibly. Two flows: mobile redirect or desktop phone + push notification.

**Manual capture**: Yes. **Disputes**: Yes (same as card disputes). Full and partial refunds. Multiple partials allowed.

**Card retries**: customer can retry with different card in-app before failure → may result in success.

**3D Secure**: 1–7% of transactions require step-up (Finland Mastercard highest at ~7%). Handled invisibly. **Liability shift only if 3DS occurred** — merchant cannot enforce 3DS. 

**Dankort not supported** — processed on Visa/Mastercard instead.

**Fees**: Stripe processing fees + MobilePay per-transaction fee (billed daily) + **35 DKK/month membership fee** (Denmark businesses only). MobilePay fees billed as separate line on monthly tax invoice.

**Prohibited categories** (8): cryptocurrencies, stock trade, gambling, betting, bonds, money transfers, debt collection, MLM/pyramid schemes.

**Branding**: merchant icon from Branding settings shown in MobilePay app. 250×250px recommended.

## Raw Sources

- [[stripe-mobilepay-2025]] — verbatim webpage content (217 lines); fixed `*card authentication*` ×1, `*3D Secure challenge*` ×1, `*3D Secure authentication*` ×1; 1 PNG downloaded, 2 CloudFront .mp4 not downloaded
