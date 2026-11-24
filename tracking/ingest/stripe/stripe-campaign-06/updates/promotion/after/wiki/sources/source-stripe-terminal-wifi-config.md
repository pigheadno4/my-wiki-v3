---
title: "Stripe Terminal: Configure the WiFi Network"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/wifi"
raw_files:
  - "stripe-terminal-wifi-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, wifi, network]
---

## Summary

The 2026-05-01 [[stripe]] Terminal guide describes remote WiFi configuration for smart readers. A reader first connects to local WiFi to fetch the remote configuration. The configured network then appears in the reader’s settings. The device user selects it and the reader connects without requiring them to enter additional information. The 2026-11-07 capture states the remote configuration purpose and links to separate Dashboard and API variants.

## Key Details

The 2026-05-01 guide documents the following behavior.

**Supported security types**. WPA/WPA2 Personal (PSK), WPA/WPA2 Enterprise (EAP-PEAP) and WPA/WPA2 Enterprise (EAP-TLS).

**Credential validation and updates**. Stripe pushes profile changes to the reader, which stays connected if the credentials are valid. Stripe does not validate credentials when the profile is configured. An incorrect password, expired EAP-TLS certificate or other invalid credential prevents the reader from connecting. The guide does not specify what feedback appears on the reader.

**Dashboard**. Operators select the security type, enter credentials and apply changes from the location details or manage locations page, using the local or inherited configuration controls as applicable.

**Reader registration**. Newly registered readers prompt the user to connect to the configured network. On readers that are already registered, the network may take up to 10 minutes to appear in network settings.

**API**. Create or update a Configuration object with the WiFi type and its corresponding field. The Personal PSK examples use `wifi: { type: 'personal_psk', personal_psk: { ssid, password } }`.

**EAP-TLS**. First upload PEM files to the Files API and use the resulting file IDs in the configuration. Choose `terminal_wifi_certificate` for client and CA certificates and `terminal_wifi_private_key` for the private key.

## Related

- [[stripe-terminal-hardware-orders]] — Terminal fleet configuration and reader registration

## Raw Sources

- [[raw/stripe-terminal-wifi-config-2025|Stripe Terminal WiFi configuration guide captured 2026-05-01]] — Dashboard flows and Node.js API examples

## Related raw API references

- [[raw/stripe-terminal-fleet-wifi-2026-11-07|Stripe Terminal WiFi configuration Dashboard and API index captured 2026-11-07]]
