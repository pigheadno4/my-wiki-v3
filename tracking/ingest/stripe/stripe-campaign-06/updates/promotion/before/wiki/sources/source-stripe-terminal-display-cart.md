---
title: "Stripe Terminal: Display Cart Details"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-display-cart-2025.md"
tags: [stripe, stripe-terminal, reader-display, cart, pre-dip, checkout]
---

## Summary

Stripe Terminal smart readers (Verifone P400, WisePOS E, S700/S710) can display line items and totals during checkout via the `setReaderDisplay` API. The display is purely informational — amounts shown do not control what is charged.

## Set the Reader Display

Call `setReaderDisplay` before processing payment, passing a `cart` object with `line_items`, `currency`, `tax`, and `total`. Available on all SDKs (iOS, Android, React Native, JavaScript, server-driven).

**Important**: The amounts in `setReaderDisplay` are display-only. The application must calculate tax and total independently (can use Stripe Tax API). The total shown on the reader does not control the charge amount.

To reset the reader to the splash screen:
- iOS/Android/React Native: call `clearReaderDisplay`
- Server-driven: call the `cancel_action` endpoint

## Pre-Dip (US only)

Pre-dip (also called pre-tap or pre-swipe) lets customers present a card before the transaction amount is finalized. Supported on Verifone P400, WisePOS E, S700/S710.

- Call `setReaderDisplay` to prepare the reader for pre-dipping.
- Customer can present their card at any point after that call.
- Multiple `setReaderDisplay` calls can update the display without invalidating an existing pre-dip.
- Stripe does not emit events when a pre-dip occurs — process the transaction normally with a PaymentIntent.
- Pre-dip disabled (non-US): reader shows subtotal and line items only, no card capture.

## Raw Sources

- [[stripe-terminal-display-cart-2025]] — verbatim webpage content
