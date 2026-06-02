---
title: "Stripe: Accept Titres-Restaurant Payments with Connect"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-fr-meal-vouchers-connect-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, connect, charges, platform]
---

## Summary

Connect integration guide for French meal vouchers. Covers supported/unsupported charge types, direct vs platform charge paths, how to identify meal vouchers via ConfirmationToken or PaymentMethod, and fee collection via transfers.

## Key Details

**Supported charge types**:

| Type | Support |
| --- | --- |
| Platform charges | ✓ |
| Direct charges | ✓ (via `Stripe-Account` header) |
| Destination charges | ❌ (funds settle outside Stripe) |
| Separate charges + transfers | ❌ (funds settle outside Stripe) |

**Direct charges**: add `Stripe-Account: CONNECTED_ACCOUNT_ID` header; rest of integration same as standard.

**Platform charges**: create PaymentIntent on platform account. Omit `transfer_data`, `application_fee_amount`, `transfer_group`. Pass SIRET in `payment_details[benefit][fr_meal_voucher][siret]`.

**Identify meal voucher before creating PaymentIntent**:
- Via **SetupIntent** → check `paymentMethod.card.benefits.programs = 'fr_meal_voucher'`
- Via **ConfirmationToken** → check `confirmationToken.payment_method_preview.card.benefits`

**Fee collection**: after capture, create `v1/transfers` from connected account to platform. Refund fees via transfer reversal (not payment refund — meal vouchers don't support those).

**Flow of funds**: issuer settles directly with connected account outside Stripe; platform collects fee via `v1/transfers`.

**SIRET provisioned on**: the merchant of record.

## Raw Sources

- [[stripe-fr-meal-vouchers-connect-2025]] — verbatim webpage content (218 lines); fixed 3× `_italic_` → `*italic*`
