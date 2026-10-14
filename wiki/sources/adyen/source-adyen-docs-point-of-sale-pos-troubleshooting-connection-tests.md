---
title: "Adyen payment-terminal connection tests"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/pos-troubleshooting/connection-tests"
raw_files:
  - "adyen/docs/point-of-sale/pos-troubleshooting/connection-tests/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, diagnostics, terminal-api, connectivity]
---

## Overview

Adyen's terminal-run connection-test guide, captured 2026-09-15, explains **PSP connection**, **Terminal API**, local-communications TLS information and four-URL **Endpoints** diagnostics for non-legacy physical payment terminals. Its stated scope includes standalone terminals and Terminal API integrations with a POS system; some checks apply only to local or cloud communications. This routes through [[adyen-payment-terminals]] with [[adyen-terminal-api]] for the integrated transport boundary. A successful test shows the checked connection at that time, not payment authorization, settlement or continued availability.

## Key takeaways

- On the terminal, check the Wi-Fi icon when Wi-Fi is used and the cloud icon for cloud Terminal API integrations, then open **Settings > Diagnostics** for PSP connection, Terminal API and Endpoints. Non-Android terminals on the **old menu structure** instead use **Admin > Network > Diagnostics**. Android terminals show **Successful** or **Failed**; old-menu non-Android terminals use green checks/red crosses. A failed step also marks all subsequent steps failed, so diagnose the first failing step rather than interpreting every later cross as a separate cause.
- **PSP connection** tests the terminal's path to Adyen's payments platform: DNS lookup, network connection, TLS negotiation, outbound writing and inbound receiving. Lookup failure points to DNS; connection or data failures point to network/router/firewall issues for the merchant network team. A TLS negotiation failure may involve inspection by a security gateway or another issue; the guide says to wait for inspection, recommends bypassing inspection of Adyen domains, and says to contact Adyen immediately for the other problem. The special first-connection case allows a red **Receiving data** cross to be ignored only when the **overall PSP result is No Error**.
- **Terminal API** checks whether the API is enabled and, for cloud, whether WebSockets are enabled and connected. The guide gives Customer Area device-setting routes for enabling Terminal API and WebSockets. For integrated terminals using **local** communications, ignore WebSocket test results. The TLS version, cipher and POS-to-terminal URL fields in this diagnostic are **local-communications TLS information**; they do not apply to cloud-integrated or standalone terminals.
- **Endpoints** tests the terminal's Sync URL (refunds/cancellations), Config URL (configuration), PAL URL (requests) and Firmware URL (software), and shows the terminal's MTU. Failures in lookup, connection, writing or receiving are network checks. For an Endpoints **Negotiating** failure, the guide names changed certificates or possible compromise and directs immediate Adyen contact; do not treat it as a routine safe retry. These tests describe terminal connectivity, not a payment result.

## Detail locators

- Raw `# Run connection tests from the terminal` and `## Requirements` (lines 15–39): tested links, standalone versus Terminal API scope, non-legacy hardware and local/cloud limits. This snapshot does not identify a specific model or current installed software version.
- Raw `## Run diagnostic connection tests from a terminal` (lines 41–64): menu paths, status presentation and failed-step cascade. The menu variation is qualified by Android versus non-Android **old menu structure**, not all non-Android terminals.
- Raw `## PSP connection test` (lines 66–80): five network/TLS stages, escalation, and first-connection **No Error** exception for Receiving data.
- Raw `## Terminal API test` and `## Local communications TLS test` (lines 82–104): cloud WebSocket versus local distinction, configuration route and local-only TLS fields.
- Raw `## Endpoints test` (lines 106–129): four URL purposes, MTU, per-URL checks and urgent Negotiating warning. `## See also` (lines 131–135) provides navigation to separate diagnosis, network and certificate pages; these links alone do not establish their details.

## Related

- [[adyen-payment-terminals]] — physical-terminal operations and model manuals.
- [[adyen-terminal-api]] — local/cloud POS messaging and outcome boundary.
- [[adyen-terminal-management]] — Customer Area device settings and fleet administration.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/pos-troubleshooting/connection-tests/2026-09-15|Terminal connection tests, fetched 2026-09-15]]
