---
title: "Stripe Terminal: Collect Tapped Data for NFC Instruments"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-collect-nfc-data-2025.md"
tags: [stripe, stripe-terminal, nfc, collect-data, private-preview, offline]
---

## Summary

Stripe Terminal can read the NFC UID from non-payment NFC instruments (cards, wristbands) using the reader's contactless interface. This is a **private preview** feature in the same access program as magstripe collect-data.

## Key Details

**Access**: Private preview — email `terminal-collect-data@stripe.com` with use case, Terminal device, and integration type.

**Supported readers**: S700/S710, M2 only. **Not** WisePOS E or Chipper2X.

**Available offline** (unlike magstripe collect-data).

**Cannot be used for card payments** — a hard warning in the docs. Use the standard Terminal payment flow for payment collection.

**Integration**:
- Call `collectData()` with `type: NFC_UID` (`.nfcUid` on iOS)
- SDK returns `CollectedData` object with `nfcUid` field directly — no server-side retrieval step needed (unlike magstripe)
- iOS/Android/React Native only (no server-driven variant)

**Customer cancellation**: enabled by default on smart readers; disable with `customerCancellation: disableIfAvailable`.

## Raw Sources

- [[stripe-terminal-collect-nfc-data-2025]] — verbatim webpage content (iOS, Android, React Native)
