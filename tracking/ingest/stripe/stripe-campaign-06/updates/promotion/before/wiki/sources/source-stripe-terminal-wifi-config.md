---
title: "Stripe Terminal: Configure the WiFi Network"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-wifi-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, wifi, network]
---

## Summary

Remotely push WiFi credentials to smart readers via the Configuration object. Reader must first connect to a local WiFi to fetch the remote config. Configured network appears automatically on reader without user input.

## Key Details

**Supported security types**: WPA/WPA2 Personal (PSK), WPA/WPA2 Enterprise (EAP-PEAP), WPA/WPA2 Enterprise (EAP-TLS).

**No credential validation**: Stripe doesn't check credentials — incorrect password or expired EAP-TLS certificate causes silent connection failure.

**EAP-TLS**: upload certificates and private key via Files API first (`terminal_wifi_certificate` for client/CA certs, `terminal_wifi_private_key` for private key; PEM format required).

**Propagation**: new readers show prompt on registration; existing registered readers: up to 10 minutes.

**API**: `wifi: { type: 'personal_psk', personal_psk: { ssid, password } }` (type varies by security type).

## Raw Sources

- [[stripe-terminal-wifi-config-2025]] — verbatim webpage content (Dashboard flows + Node.js API samples)
