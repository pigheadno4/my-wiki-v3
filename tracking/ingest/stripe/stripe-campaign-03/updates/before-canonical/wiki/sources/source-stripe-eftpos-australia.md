---
title: "Stripe: eftpos Australia"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-eftpos-australia-2025.md"
tags: [stripe, eftpos, australia, local-card-network, least-cost-routing, debit, disclosure]
---

## Summary

eftpos Australia is the local debit card network for AU. >90% co-branded with Visa/MC. AUD only. No manual capture. Disclosure requirement for dual-network debit routing.

## Key Details

**Routing**: eftpos default for non-hold payments; hold/delayed capture → always Visa/MC. Detect via `charge.payment_method_details.card.network` = `"eftpos_au"`.

**eftpos-only cards**: in-person only (cannot be used online).

**Excluded MCCs**: 7 categories including massage parlors, financial institutions, foreign currency, stored value.

**Disclosure**: must inform customers dual-network cards may route through debit network regardless of displayed logo.

## Raw Sources

- [[stripe-eftpos-australia-2025]] — verbatim webpage content (properties, routing, MCCs, disclosure wording, JSON network example)
