---
title: "Stripe Terminal: Configure Reboot Time Window"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-reboot-time-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, reboot]
---

## Summary

Smart readers reboot every 24h at midnight by default. Configure a custom reboot window via the Configuration object to avoid business-hours disruptions. Reboots are staggered randomly within the window.

**Timezone**: uses the reader's registered location's local time, not the management account's timezone.

**API**: `configurations.create/update({ reboot_window: { start_hour: 0-23, end_hour: 0-23 } })`

**Crossing midnight**: `start_hour < end_hour` = same day; `start_hour > end_hour` = crosses midnight (e.g. 15–3 = 3pm to 3am).

**Propagation**: 10 minutes. If reader already rebooted today, takes effect next cycle.

## Raw Sources

- [[stripe-terminal-reboot-time-2025]] — verbatim webpage content
