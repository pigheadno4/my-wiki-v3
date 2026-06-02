---
title: "Stripe Terminal: Monitor Readers"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-monitor-readers-2025.md"
tags: [stripe, stripe-terminal, fleet, monitoring, dashboard, reader-events]
---

## Summary

Monitor Terminal reader health, connectivity, and event history via the Stripe Dashboard. Smart readers have richer monitoring than mobile readers.

## Key Details

**Readers list**: filter and export all registered readers. Connection state (online/offline) is smart readers only. Connect direct charges: must log in as connected account to see its readers.

**Smart reader details**: connection state, battery, P2PE status, last active, software version, recent payments summary. Connectivity: Ethernet (MAC, IP), WiFi (MAC, IP, SSID, frequency, signal strength), Bluetooth (MAC).

**Reader events** (public preview): 30-day event log, events take several minutes to appear. Event types:

| Event | Sub-type | Notes |
| --- | --- | --- |
| General | Device powered on | Includes restart reason; "unknown" common on software < 2.33 |
| Network connectivity | Network connected/disconnected | Includes connection type; WiFi includes SSID |
| Update operation | Update install succeeded | Includes software + version |
| Update operation | Updates deferred | User action or low battery |
| Update operation | Update install failed | Retried in reboot window; manual retry = reboot (check battery) |

**Mobile reader details**: no connection state; reader type, ID, registration, location, last active, software version.

## Raw Sources

- [[stripe-terminal-monitor-readers-2025]] — verbatim webpage content
