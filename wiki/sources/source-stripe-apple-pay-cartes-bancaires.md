---
title: "Stripe: Cartes Bancaires with Apple Pay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-apple-pay-cartes-bancaires-2025.md"
tags: [stripe, wallets, apple-pay, cartes-bancaires, france, eur, ios, web]
---

## Summary

Guide for enabling Cartes Bancaires within Apple Pay. EUR only. iOS requires one line of SDK config; web is automatic via supported Elements. Connect platforms must verify connected account supports Cartes Bancaires when using on_behalf_of.

## Key Details

**EUR only** — Stripe only supports EUR for Cartes Bancaires with Apple Pay.

**iOS**: `StripeAPI.additionalEnabledApplePayNetworks = [.cartesBancaires]`. Only add if transaction is EUR and merchant supports Cartes Bancaires. Check connected account eligibility via Capabilities API.

**Web**: automatic — Payment Element, Express Checkout Element, Checkout, and Payment Request Button all support it automatically. No extra code.

**Connect platforms (web)**: if using `on_behalf_of`, set `OnBehalfOf` on Elements object to match the intent's `on_behalf_of` account.

**Test**: real Cartes Bancaires card from Apple Pay participating bank required (same test limitation as all Apple Pay).

## Raw Sources

- [[stripe-apple-pay-cartes-bancaires-2025]] — verbatim webpage content (77 lines); no italic fixes needed
