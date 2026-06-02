---
title: "Stripe: Virtual Bank Account Numbers (VBANs)"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-bank-transfers-vban-2025.md"
tags: [stripe, bank-transfers, vban, virtual-bank-account, customer-balance, limits]
---

## Summary

Best practices and limits for VBANs. Covers the permanence of VBAN allocation, the three ways to trigger allocation, per-region daily and lifetime limits, and guidance on avoiding unnecessary VBAN creation.

## Key Details

**VBANs are permanent**: once allocated to a customer, funds sent to that VBAN always go to their cash balance — forever. Stripe reuses an existing VBAN if one matches the country and customer.

**VBAN allocation triggers**:
1. Confirming a PaymentIntent with `customer_balance` PM
2. Creating an Invoice with `customer_balance` PM
3. Calling the Funding Instructions API (proactive, no payment required)

**Best practices**: only allocate VBANs to customers likely to pay via bank transfer. Don't assign to inactive customers or include in registration flows.

**Per-region limits**:

| Region | Daily limit | Lifetime limit | Fee beyond |
| --- | --- | --- | --- |
| US | 10,000 | — | — |
| UK | 5,000 | — | — |
| EU | 5,000 | 50,000 | Yes (beyond 1,000 EU allocations) |
| JP | 1,000 | — | — |
| MX | 1,000 | — | — |

## Raw Sources

- [[stripe-bank-transfers-vban-2025]] — verbatim webpage content (36 lines)
