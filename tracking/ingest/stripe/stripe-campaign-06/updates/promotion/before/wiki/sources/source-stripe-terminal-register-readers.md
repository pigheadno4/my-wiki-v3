---
title: "Stripe Terminal: Register Readers"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-register-readers-2025.md"
tags: [stripe, stripe-terminal, registration, fleet, readers, locations]
---

## Summary

Readers must be registered to a location before accepting payments. Any user with write permissions can register. Smart readers have 3 registration methods; mobile readers register at SDK connect time.

## Smart Reader Registration Methods

**1. Registration code (pairing code)**: requires physical access to the reader. Pairing code appears on-screen on first unbox; regenerate via admin settings if needed. Register via Dashboard or API (`stripe.terminal.readers.create({ registration_code, label, location })`).

**2. Serial number**: remote registration — no physical reader needed. Up to **10 readers at a time**. Only works for readers ordered by the account (platforms: order must be by the platform or the sub-account). Serial number found on box, back of reader, or Hardware Orders page.

**3. Order number**: register from Hardware Orders page (overflow menu → Register) or registration flow. Only works for orders placed by the account or its sub-accounts. Supports batch registration with sequential naming (e.g. "Test reader 1", "Test reader 2").

## Mobile Reader Registration

Register M2, Chipper 2X BT, WisePad 3 at SDK connect time by passing `locationId` in `BluetoothConnectionConfiguration`. Can reuse `reader.locationId` from a previously discovered reader to register to the last-used location.

## Raw Sources

- [[stripe-terminal-register-readers-2025]] — verbatim webpage content (Dashboard flows + Node/Swift/Kotlin/React Native code samples)
