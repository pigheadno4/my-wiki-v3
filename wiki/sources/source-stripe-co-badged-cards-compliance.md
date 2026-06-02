---
title: "Stripe: Co-badged Cards Compliance"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-co-badged-cards-compliance-2025.md"
tags: [stripe, co-badged, cartes-bancaires, girocard, eu-regulation, elements, terminal]
---

## Summary

EU Regulation 2015/751 compliance guide for co-badged cards. Stripe-hosted UIs auto-display network selector. Connect requires `onBehalfOf`. Mobile needs SDK minimums.

## Key Details

**Scope**: EEA businesses processing Cartes Bancaires (online EUR) + France/Germany in-person.

**Integration per UI**:
- Checkout/Payment Links: automatic
- Web Payment Element: automatic; Connect needs `onBehalfOf`; `defaultValues.card.network` for default
- Web Card Element: needs `hideIcon: false`; `preferredNetwork` for default; incompatible with Sources
- Payment Request Button / Express Checkout Element: automatic; Connect needs `onBehalfOf`
- Mobile (Payment Sheet, Payment Element, Customer Sheet, Card Element): automatic; `preferredNetworks` for default; iOS 23.22.1+/Android 20.37.4+; Connect needs `onBehalfOf` in IntentConfiguration
- Terminal (WisePad 3, S700/S710): automatic; Tap to Pay on iPhone needs manual `requested_priority`

**Test cards**: 4000002500001001 (CB/Visa), 5555552500001001 (CB/MC); tokens; PM IDs.

## Raw Sources

- [[stripe-co-badged-cards-compliance-2025]] — verbatim webpage content (7 CDN images downloaded; all integration guides with JS/Swift/Kotlin code)
