---
title: "Stripe Terminal: Collect Swiped Data"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/collect-data"
raw_files:
  - "stripe-terminal-collect-data-2025.md"
tags: [stripe, stripe-terminal, magstripe, gift-cards, collect-data, private-preview]
---

## Summary

The 2026-05-01 [[stripe]] Terminal guide describes a private preview for collecting non-PCI magstripe data, such as gift-card data, through reader hardware. The 2026-11-07 capture repeats the non-PCI purpose and indexes iOS, Android and React Native. The linked variant bodies are outside the November capture. The operational details below come from the May guide.

## Key Details

**Private preview access in May**. The guide directs merchants to email `terminal-collect-data@stripe.com` with the use case, device and integration type, magstripe format, and the provider if using third-party cards.

**Reader and offline scope in May**. The guide lists Stripe Reader S700/S710, BBPOS WisePOS E, Stripe M2 and BBPOS Chipper2X BT. It states that collection is unavailable offline.

**Data format**. The May guide specifies non-PCI numeric track-2 data with the ISO/IEC 7813 start sentinel `;`, the end sentinel `?`, and no separator. For formats outside the documented list, it directs merchants to contact the Terminal team with the card format and BIN ranges.

**Integration flow in May**.

1. The merchant’s POS uses the Terminal SDK’s `collectData` with its magstripe configuration, and the customer swipes the card.
2. The SDK returns a token representing the data or an error if the swipe fails. The iOS and React Native examples read the token from `stripeId`.
3. The merchant’s authenticated backend uses the token to retrieve cleartext non-PCI track data through `GET /v1/terminal/reader_collected_data/{id}`, for example to redeem a gift card. The May guide says Stripe stores the collected data for 24 hours.

**Customer cancellation in May**. The iOS and Android sections describe default customer cancellation on supported readers and a smart-reader opt-out using the platform’s `customerCancellation` setting. The React Native example also sets `customerCancellation: 'disableIfAvailable'`.

**Stripe responsibility**. The May guide says Stripe neither authenticates collected data nor authorizes transactions using that data. Stripe disclaims responsibility for those activities and liability for related third-party illegal conduct or fraud.

## Related

- [[stripe-terminal]] — Terminal devices and integration overview

## Raw Sources

- [[raw/stripe-terminal-collect-data-2025|Stripe Terminal collect swiped data guide captured 2026-05-01]] — iOS, Android, and React Native implementation sections

## Related raw API references

- [[raw/stripe-terminal-features-collect-data-2026-11-07|Stripe Terminal collect swiped data SDK variant index captured 2026-11-07]]
