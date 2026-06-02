---
title: "Stripe: Card Product Codes"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-card-product-codes-2025.md"
tags: [stripe, cards, product-codes, visa, mastercard, brand-product]
---

## Summary

Reference tables for Visa and Mastercard card product codes, accessible via the `brand_product` field on PaymentMethod and Charge objects.

## Key Details

**Field location**: `brand_product` within `card_present` hash on PaymentMethod; also in `payment_method_details.card_present` on Charge after PaymentIntent confirmation.

**Supported networks**: Visa and Mastercard only. May be `null` if not yet collected or network not supported.

**Visa**: 41 product codes (A=Traditional, C=Signature, G=Business, I=Infinite, K=Corporate, L=Electron, N=Platinum, S=Purchasing, V=V Pay, etc.)

**Mastercard**: 200+ product codes (MDS=Standard Debit, MDP=Platinum Debit, MCW=World, MWE=World Elite, MAB=World Elite Business, MCC=Credit mixed BIN, prepaid, B2B, Maestro, installments, etc.)

**Test cards**: 5 Mastercard cards with product codes MDS/MDP/MCW/MWE/MAB.

## Raw Sources

- [[stripe-card-product-codes-2025]] — verbatim webpage content (full Visa 41-row + Mastercard 200+-row reference tables, test cards)
