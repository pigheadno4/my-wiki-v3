---
title: "Stripe Terminal: JavaScript SDK API Reference"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-js-sdk-reference-2025.md"
tags: [stripe, stripe-terminal, javascript, sdk, api-reference]
---

## Summary

Complete API reference for the Stripe Terminal JavaScript SDK. 29 methods covering the full payment lifecycle, plus error codes and changelog.

## Method Groups

**Lifecycle**: `StripeTerminal.create()` (options: `onFetchConnectionToken`, `onUnexpectedReaderDisconnect`, `onConnectionStatusChange`, `onPaymentStatusChange`, `readerBehavior`), `clearCachedCredentials()`

**Reader connection**: `discoverReaders()`, `connectReader()` (`fail_if_in_use` option), `disconnectReader()`, `getConnectionStatus()`, `getPaymentStatus()`

**Payment collection**: `collectPaymentMethod()` (config_override: `skip_tipping`, `tipping.eligible_amount`, `update_payment_intent`, `enable_customer_cancellation`, `allow_redisplay`, `moto`), `cancelCollectPaymentMethod()`, `processPayment()` (config_override: `return_url`), `cancelProcessPayment()`

**Save payment methods**: `collectSetupIntentPaymentMethod()`, `cancelCollectSetupIntentPaymentMethod()`, `confirmSetupIntent()`, `cancelConfirmSetupIntent()`, `readReusableCard()`, `cancelReadReusableCard()`

**Reader display**: `setReaderDisplay()`, `clearReaderDisplay()`

**Refunds**: `collectRefundPaymentMethod()` (Connect: `refund_application_fee`, `reverse_transfer`), `cancelCollectRefundPaymentMethod()`, `processRefund()`, `cancelProcessRefund()`

**Collect inputs**: `collectInputs()`, `cancelCollectInputs()`

**Printing** (V660p only): `print()` (takes `HTMLCanvasElement`)

**Simulator**: `setSimulatorConfiguration()`, `getSimulatorConfiguration()`

## Error Codes

17 error codes including: `no_established_connection`, `canceled`, `network_error`, `network_timeout`, `already_connected`, `failed_fetch_connection_token`, `discovery_too_many_readers`, `command_already_in_progress`, and 7 printer-specific codes (`printer_busy`, `printer_paperjam`, `printer_cover_open`, `printer_out_of_paper`, `printer_absent`, `printer_unavailable`, `printer_error`).

## Changelog Highlights

- 2025-10-30: Surcharge consent collection in `processPayment`
- 2025-10-06: `print()` method (V660p, preview)
- 2025-06-02: `cancelProcessPayment`, `cancelConfirmSetupIntent`, `cancelProcessRefund` added; simulated reader supports input collection

## Raw Sources

- [[stripe-terminal-js-sdk-reference-2025]] — verbatim webpage content
