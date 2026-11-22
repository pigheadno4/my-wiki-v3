---
title: "Stripe: France Titres-Restaurant (Meal Vouchers)"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-fr-meal-vouchers-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, benefits, siret, split-tender]
---

## Summary

Overview of Stripe's French meal vouchers (titres-restaurant) payment method (private preview). Covers issuers, CNTR approval requirements, SIRET provisioning, off-Stripe settlement model, no-refund/no-dispute constraints, balance cap, balance check API, and split tender orchestration.

## Key Details

**Status**: private preview. FR accounts only, CNTR regulatory approval required.

**Issuers**: Bimpli, Pluxee, Up Déjeuner, Swile (Swile via Mastercard — different integration rules).

**CNTR approval**: per-branch, not per-company. Only restaurants, grocers, canteens, food-serving businesses qualify.

**SIRET provisioning**: provide branch SIRET to Stripe before use (1–3 business days). Pass via `payment_details.benefit.fr_meal_voucher.siret` on each PaymentIntent.

**Settlement**: off-Stripe — issuers pay acceptors directly. Stripe deducts a processing fee as a negative BalanceTransaction.

**No refunds, no disputes** (Bimpli/Pluxee/Up Déjeuner). Use auth+capture+release for unfulfillable orders.

**Daily balance cap**: 25 EUR, resets midnight French local time.

**Identify**: `paymentMethod.card.benefits.programs = 'fr_meal_voucher'`; `.issuer` names the issuer.

**Check balance**: `GET /v1/payment_methods/:id/check_balance` — optional.

**Split tender**: Stripe doesn't support natively. Create separate PaymentIntents for meal-voucher portion vs ancillary/overage.

## Raw Sources

- [[stripe-fr-meal-vouchers-2025]] — verbatim webpage content (147 lines); fixed `_split tender_` → `*split tender*`
