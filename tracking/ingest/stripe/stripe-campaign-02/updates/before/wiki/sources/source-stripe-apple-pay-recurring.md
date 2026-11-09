---
title: "Stripe: Manage Recurring Payments on Apple Pay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-apple-pay-recurring-2025.md"
tags: [stripe, wallets, apple-pay, recurring, dpan, mpan, cryptogram, cit, mit, setup-intent, off-session]
---

## Summary

Technical guide for improving Apple Pay recurring payment authorization rates. Checkout/Elements handle this automatically — guide targets API integrations. Root cause of failures: cryptogram expiration. Key pattern: consume cryptogram via SetupIntent CIT immediately after capture.

## Key Details

**Checkout and Elements are automatic** — this guide applies to direct API integrations only.

**DPAN vs MPAN**:
- DPAN: device-tied; deactivates if user switches to new device with same card
- MPAN (merchant token): persists across devices; preferred for recurring

**Cryptogram expiration = root cause of recurring failures**: each DPAN/MPAN includes a one-time expiring cryptogram. CIT must consume it immediately. If CIT fails → all subsequent MITs on that card also fail.

**Correct pattern**: Save DPAN/MPAN → immediately trigger CIT via SetupIntent (0 USD validation) → use saved payment method for future off-session MITs.

**Free trial pattern**: use Stripe Subscriptions (auto-creates SetupIntent + 0 USD validation as CIT). Never delay CIT to after trial end — cryptogram expires.

**Legacy Tokens API**: strongly deprecated for recurring Apple Pay — Tokens API doesn't trigger authorization in time. Migrate to PaymentIntents/SetupIntents.

**Off-session restriction**: Apple Pay terms **forbid** `usage=on_session` with saved payment method — if customer is present, must authorize new cryptogram.

**Incremental authorizations**: only supported when increasing amount before capture.

## Raw Sources

- [[stripe-apple-pay-recurring-2025]] — verbatim webpage content (91 lines); no italic fixes needed
