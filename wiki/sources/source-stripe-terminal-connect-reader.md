---
title: "Stripe Terminal: Connect to a Reader (All Platforms)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-connect-reader-2025.md"
tags: [stripe, terminal, in-person, connection, bluetooth, usb, internet, tap-to-pay, simulated-reader, reader-updates]
---

## Stripe Terminal: Connect to a Reader (All Platforms)

Comprehensive connection guide covering all reader types × all SDKs: Simulated, Bluetooth, USB, Internet/LAN, and Tap to Pay.

## Key Takeaways

### Simulated reader registration codes (server-driven, sandbox only)

| Code | Creates |
| --- | --- |
| `simulated-wpe` | Simulated WisePOS E |
| `simulated-s700` | Simulated Stripe S700 |
| `simulated-s710` | Simulated Stripe S710 |

### Bluetooth connection rules

- **Don't pair through device Settings** — doing so makes the reader unavailable to your app
- **Mobile readers require no Dashboard/API registration** — associate with `locationId` at connection time via `BluetoothConnectionConfiguration`
- **Don't cache reader objects** — always use the most recent discovery results; stale objects cause connection failures
- **Standby mode**: do NOT call `disconnectReader` to save power — the reader handles power management in standby

### WisePad 3 Bluetooth pairing (Nov 2025 change)

Numeric comparison pairing now required for new device pairings and re-pairings:
1. Verify 6-digit code matches on both WisePad 3 and POS device
2. Select **Confirm** on WisePad 3
3. Select **Pair** on POS device

Only applies when pairing with a **new** POS device, or re-pairing with a "forgotten" device.

### USB connections

**Android only** — iOS uses Bluetooth instead.

### Auto-reconnect

- Enabled by default (`autoReconnectOnUnexpectedDisconnect: true`)
- To disable: set flag to `false` and handle disconnect callbacks manually
- **Auto-reconnect on app start is NOT automatic** — must implement manually:
  1. Store reader serial number persistently when connected
  2. On launch, call `discoverReaders` to find the saved reader
  3. Connect to the matching reader if found

### Reader reboot

M2 and WisePad 3 auto-reboot after **24 hours** of operation. Can force a reboot via `rebootReader` API (disconnects reader; auto-reconnect resumes if enabled).

### Reader updates

- **Required updates**: install automatically on connection; reader unusable until complete; **battery must be >50%**; can be cancelled (fails connection)
- **Optional updates**: reported via `didReportAvailableUpdate`; deferred until `requiredAt` date; install via `installAvailableUpdate`
- If required update fails but reader runs recent software (within 30 days) AND iOS SDK ≥ 3.5.0: connection still succeeds; update retried next connection

### Internet/LAN connection (smart readers)

Smart readers (WisePOS E, S700/S710, Verifone) connect via internet or LAN. Server-driven uses internet; SDK uses LAN (same-network required).

### Handoff mode (S700/S710 Apps on Devices)

Special connection mode for Apps on Devices deployments where your app runs on the smart reader itself.

### Tap to Pay on iPad (TTPOI)

Requires a dedicated account linking flow. See raw file for details.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-connect-reader-2025]] — verbatim reader connection guide (3792 lines; all platforms × all reader types)
