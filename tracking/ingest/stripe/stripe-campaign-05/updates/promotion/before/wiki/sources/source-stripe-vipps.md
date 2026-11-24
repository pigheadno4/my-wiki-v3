---
title: "Stripe: Vipps Payments"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-vipps-2025.md"
tags: [stripe, wallets, vipps, norway, nok, card-wallet, private-preview, connect, disputes, refunds]
---

## Summary

Overview of Vipps, a Norway-only card wallet in private preview on Stripe. Vipps processes payments as underlying Visa/Mastercard card transactions. Covers payment flow, Connect, disputes, refunds, fees, and restrictions.

## Key Details

**Norway customers only**, NOK only. Card wallet — customers authenticate via Vipps app push notification after entering phone number.

**Private preview**: requires `vipps_preview=v1` header on all API requests.

**Underlying card transaction**: Stripe receives card data from Vipps and processes as Visa/Mastercard. Invisible to merchant integration. Immediate notification of success/failure.

**29 European business countries** (includes NO, plus 28 other EU/EEA countries).

**No recurring payments.**

**Manual capture**: Yes.

## Product Support

Connect (Direct, Destination, Separate charges), Checkout (not subscription/setup mode), Payment Links (API-created only), Elements (not Express Checkout Element).

## Disputes

Same process as card payments — customers dispute directly with card issuer. Evidence submission via standard Stripe dispute flow.

## Refunds

Full and partial. Multiple partial refunds allowed up to original charge amount. No time limit stated.

## Fees

Three components per successful transaction:
1. **Stripe card processing fees** — deducted from transaction (identical to standard card)
2. **Applicable taxes** — deducted from transaction
3. **Vipps per-transaction fee** — **billed daily** (not deducted from individual transaction; deducted from Stripe balance once per day)

Standard payout schedule applies.

## Connect

Capability: `vipps_payments`. All three charge types supported (Direct, Destination, Separate charges and transfers). Connected account name displayed to customers in checkout and Vipps app.

## Limitations

**BankAxept not supported** — BankAxept-branded cards processed on Visa/Mastercard networks instead.

## Prohibited Categories

8 categories: cryptocurrencies (restricted), stock trade, gambling, betting, bonds, money transfers, debt collection, MLM/pyramid schemes.

## Raw Sources

- [[stripe-vipps-2025]] — verbatim overview page (171 lines); 1 CDN video downloaded
