---
title: "Stripe: Deposit Mode Stablecoin Payments"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-crypto-deposit-mode-2025.md"
tags: [stripe, stablecoin, crypto, usdc, deposit-mode, payment-intents, machine-payments]
---

## Summary

API-only crypto payment flow returning deposit addresses per network. Customer sends stablecoins directly on-chain; Stripe auto-captures after settlement. Requires separate access request (machine-payments@stripe.com) and API version `2026-03-04.preview`.

## Key Details

**3 networks** (USDC only): Tempo, Base, Solana. US businesses only.

**Flow**: confirm PaymentIntent → `requires_action` (deposit addresses returned) → customer sends → `processing` → `succeeded`.

**Critical**: token amount must match exactly. USDC uses 6 decimal places vs USD's 2 (e.g., 1.01 USD = 1.010000 USDC). Any mismatch → cannot auto-match or return funds.

**Failure modes**: wrong network/token, funds after expiration, any amount mismatch.

**Refunds**: returned to original sending wallet. Warn if exchange/omnibus wallet.

**Testing**: `simulate_crypto_deposit` test helper; `testsuccess`/`testfailed` hash values.

**API**: `payment_method_types: ['crypto']`, `payment_method_options.crypto.mode: 'deposit'`, `deposit_options.networks: [...]`, `confirm: true`.

## Raw Sources

- [[stripe-crypto-deposit-mode-2025]] — verbatim webpage content (node block, JSON response, curl test helper, network support table)
