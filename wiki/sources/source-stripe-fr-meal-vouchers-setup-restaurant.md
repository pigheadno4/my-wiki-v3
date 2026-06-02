---
title: "Stripe: Set Up a Restaurant for Titres-Restaurant Payments"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-fr-meal-vouchers-setup-restaurant-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, siret, onboarding, connect]
---

## Summary

Step-by-step guide for onboarding a restaurant to accept French meal vouchers via Stripe Dashboard. Covers SIRET provisioning, postal code matching requirement, status validation, Connect provisioning, and test SIRETs.

## Key Details

**Prerequisites**: CNTR license + issuer contracts before starting.

**SIRET onboarding** (Dashboard → French meal vouchers SIRETs → Add SIRET):
- Provide SIRET, postal code, and store name — all must match CNTR record
- Takes **1–2 business days** to validate
- **SIRET and name are immutable** after creation

**Status**: check per-issuer status on the SIRETs page. `Requires Action` means postal code mismatch — fix via Update Details.

**Postal code mismatch fix**: Dashboard → SIRETs page → click restaurant → Update Details → enter correct postal code → **1–2 business days** to re-validate.

**Connect provisioning**: Connected Accounts → select account → Payment methods → French Meal Voucher Conecs → Configure SIRETs.

**API onboarding**: preview only — contact fr-meal-voucher-beta@stripe.com.

**Test SIRETs**:

| SIRET | Postal code | Scenario |
| --- | --- | --- |
| `42424242424242` | `42424` | Valid onboarded restaurant |
| `11111111111111` | `11111` | Awaiting onboarding outcome |
| `42424242424242` | Any other | Postal code mismatch |

## Raw Sources

- [[stripe-fr-meal-vouchers-setup-restaurant-2025]] — verbatim webpage content (91 lines)
