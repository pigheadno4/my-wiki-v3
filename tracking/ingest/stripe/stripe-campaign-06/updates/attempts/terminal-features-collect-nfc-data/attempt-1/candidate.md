---
title: "Stripe Terminal: Collect Tapped Data for NFC Instruments"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/collect-nfc-data"
raw_files:
  - "stripe-terminal-collect-nfc-data-2025.md"
tags: [stripe, stripe-terminal, nfc, collect-data, private-preview, offline]
---

## Summary

The 2026-05-01 [[stripe]] Terminal guide documents Collect data private-preview support for reading the unique identifier (UID) of a non-payment NFC instrument, such as a card or wristband, through the reader’s contactless interface. The 2026-11-07 capture states the reader-hardware purpose and indexes the iOS, Android and React Native variants. The implementation details below come from the May guide.

## Key Details

**Private preview access in May**. Request access by emailing `terminal-collect-data@stripe.com` with the use case, Terminal device and integration type.

**Reader and offline scope in May**. The guide lists Stripe Reader S700/S710 and Stripe M2 and documents offline collection.

> **Card-payment restriction.** NFC UID collection cannot collect card payments. Use the standard Terminal payment flow for payments. [Collect card payments with Terminal](https://docs.stripe.com/terminal/payments/collect-card-payment.md).

**Integration in May**. The merchant’s POS initiates collection through the Terminal SDK using `collectData()` with NFC UID configured as `.nfcUid` on iOS or `NFC_UID` on Android and React Native. The customer taps the NFC instrument. The SDK returns a collected-data object containing `nfcUid`, or an error if the read fails. The UID returns to the app in the collection result. The separate swiped-data guide documents a token followed by backend retrieval.

**Customer cancellation in May**. The iOS and Android sections describe default cancellation on supported readers and a smart-reader opt-out in `customerCancellation`. The iOS spelling is `.disableIfAvailable`, and Android uses `DISABLE_IF_AVAILABLE`. The React Native example sets `customerCancellation: 'disableIfAvailable'`.

## Related

- [[stripe-terminal]] — Terminal devices and integration overview
- [[source-stripe-terminal-collect-data]] — non-PCI magstripe capture with server retrieval

## Raw Sources

- [[raw/stripe-terminal-collect-nfc-data-2025|Stripe Terminal collect NFC tapped data guide captured 2026-05-01]] — iOS, Android, and React Native implementation sections

## Related raw API references

- [[raw/stripe-terminal-features-collect-nfc-data-2026-11-07|Stripe Terminal collect NFC tapped data SDK variant index captured 2026-11-07]]
