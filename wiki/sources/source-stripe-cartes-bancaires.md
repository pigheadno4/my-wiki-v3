---
title: "Stripe: Cartes Bancaires (CB)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-cartes-bancaires-2025.md"
tags: [stripe, cartes-bancaires, france, local-card-network, co-badged, disputes]
---

## Summary

Cartes Bancaires is France's local card network. >95% co-badged with Visa/MC. EUR only. 41 business countries. 0 EUR dispute fee; cannot contest disputes.

## Key Details

**Co-badging**: EEA businesses must offer network choice; Stripe auto-retries on Visa/MC if CB declines.

**Non-France enablement**: must process one CB payment first.

**Disputes**: fewer reasons → lower rate; cannot contest; 0 EUR fee; CB may withdraw → `won`.

**Product support**: Connect/Checkout/Payment Links/Subscriptions/Invoicing/Elements (not Express Checkout)/Terminal (France needs regional config).

## Raw Sources

- [[stripe-cartes-bancaires-2025]] — verbatim webpage content
