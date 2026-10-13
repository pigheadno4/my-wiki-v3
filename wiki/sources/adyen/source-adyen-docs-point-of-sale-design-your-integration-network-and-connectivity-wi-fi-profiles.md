---
title: "Adyen Wi-Fi Profiles for Payment Terminals"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/wi-fi-profiles"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/wi-fi-profiles/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, wifi, terminal-management, management-api]
---

## Overview

This Adyen Docs guide explains how a Wi-Fi-capable Adyen payment terminal obtains network settings from a local or remote Wi-Fi profile. It covers Terminal API and standalone POS solutions, remote setup in the Customer Area or through Management API terminal settings, terminal loading and verification, and certificate/network maintenance. This is a 2026-09-15 webpage snapshot with a 2020-10-28 `last_modified` field; its API code snippets name separate, older language-library versions and use TEST endpoints or clients. They are examples of this guide, not current GitHub SDK contracts or evidence of deployed connectivity.

## Key takeaways

- Local profiles are managed on the terminal and support WPA/WPA2 Personal; Enterprise EAP-PEAP and EAP-TLS require a centrally managed remote profile. Remote profiles also support Personal PSK. Match the profile and company, merchant, store or terminal setting level to the actual network and account structure.
- For Customer Area setup, the guide covers Personal PSK and Enterprise EAP-PEAP/EAP-TLS. Enterprise profiles require the relevant RADIUS CA certificate; EAP-TLS also needs a terminal client certificate and key, and its Customer Area creation option is available on demand through the Adyen account manager. Android terminal fields have model/OS qualifications: `Hidden SSID` is mandatory for Android terminals in the guide, while `Domain Suffix` applies to Android 11 or higher for Enterprise profiles.
- API automation uses the **Management API**, with the `Management API—Terminal Advanced settings read and write` role, to GET or PATCH `/terminalSettings` at company, merchant, store or terminal level. These are sensitive settings because they affect Terminal API communication. Before removing settings, inspect what the next higher level will supply through inheritance. The guide says an outdated profile can be removed, but does not spell out a deletion request; do not infer deletion semantics from its create/update PATCH examples.
- A terminal needs temporary internet access before first boarding to retrieve its remote profile; boarded terminals receive changes through automatic maintenance or a manual **Config > Update**. The on-terminal **Network > Wi-Fi > Added** field distinguishes `via CA` from `local on device`. Profile nodes with different credentials or certificates can share an SSID; the terminal tries them in turn and reuses the last successful node on its next connection.
- Expired Enterprise certificates prevent Wi-Fi connection. The guide offers Customer Area expiry lookup and optional email reminders, and warns that unsuitable cryptographic protocols can block EAP-PEAP/EAP-TLS terminals from connecting to process transactions. Treat its listed cryptographic parameters as source-specific guidance to verify before applying; do not silently rewrite the raw's RSA key-size wording.

## Detail locators

- `## Requirements` and `## Wi-Fi network and profile types` — integration/hardware prerequisites, Personal versus Enterprise support, local/remote distinction, profile types and account/store scope.
- `## Set up Wi-Fi profiles in the Customer Area` — tab-specific Personal PSK, EAP-PEAP and EAP-TLS setup; certificate formats, Android fields, preferred band, Create then Save.
- `## Set up Wi-Fi profiles using API calls` — Management API role, inheritance warning, four `/terminalSettings` levels, `wifiProfiles` settings/profile tables, Base64 certificate objects and TEST code examples. The examples list Java 25.0.0, PHP 17.4.0, .NET 14.3.0, Node 16.2.0, Go 9.2.0, Python 12.2.0 and Ruby 9.2.0; use their exact tab before copying a snippet.
- `## Load profiles on the terminal` — temporary first-use connection, boarding, maintenance/manual update and on-device verification.
- `## Manage changes using multiple-node Wi-Fi profiles`, `## Know when certificates expire`, `## Security recommendations` — staged same-SSID changes, expiry reminders and connection-blocking security conditions.

## Related

- Company: [[adyen]]
- POS message/API boundary: [[adyen-terminal-api]] — Terminal API carries POS messages; this guide's remote Wi-Fi administration uses Management API.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/wi-fi-profiles/2026-09-15|2026-09-15 Adyen Wi-Fi profiles guide snapshot]]
