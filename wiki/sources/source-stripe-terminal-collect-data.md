---
title: "Stripe Terminal: Collect Swiped Data"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-collect-data-2025.md"
tags: [stripe, stripe-terminal, magstripe, gift-cards, collect-data, private-preview]
---

## Summary

Stripe Terminal can read non-PCI magstripe data (e.g. gift cards) using the reader's hardware magnetic stripe interface. This is a **private preview** feature requiring email access request.

## Key Details

**Access**: Private preview — email `terminal-collect-data@stripe.com` with use case, reader/integration type, magstripe data format, and provider (if third-party card).

**Supported readers**: S700/S710, WisePOS E, M2, Chipper 2X BT. **Not available offline.**

**Data format restrictions** (track 2 only):
- ISO/IEC-7813 track 2 sentinels: start `;`, end `?`, no separator character
- Numeric digits only
- Custom formats require approval from the Terminal team

**Integration flow**:
1. Call `collectData()` / `Terminal.collectData()` with `type: MAGSTRIPE`
2. SDK returns a tokenized `CollectedData` object with a `stripeId`
3. Server-side: `GET /v1/terminal/reader_collected_data/{id}` to retrieve cleartext track data

**Storage**: Stripe stores collected data for **24 hours only**.

**Legal disclaimer**: Stripe explicitly disclaims responsibility for authentication and authorization of collected data, and is not liable for illegal conduct or fraud by third parties.

**SDK availability**: iOS, Android, React Native (no server-driven, no JS SDK variants shown). Customer cancellation enabled by default on smart readers; disable with `customerCancellation: disableIfAvailable`.

## Raw Sources

- [[stripe-terminal-collect-data-2025]] — verbatim webpage content (iOS, Android, React Native)
