---
title: "Adyen e355 LED colors (historical manual)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/understand-the-led-colors-e355"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/understand-the-led-colors-e355/2026-09-15.md"
tags: [adyen, point-of-sale, e355, terminal-deprecation, led, battery]
---

## Overview

This [[adyen]] e355 manual page is a model-specific **LED-status lookup table**, last modified 2021-02-01 and captured 2026-09-15 under terminal deprecation. It belongs with [[adyen-payment-terminals]]. It does not establish current e355 transaction support, device safety, connectivity, payment success or battery remediation steps.

## Key takeaways

- Green blinking every 4 seconds denotes **Sleep**; continuously lit green denotes **Normal Operation** in this table.
- Red at **1 Hz, 50% duty cycle** is **Battery Low**, with the listed 3.7 V condition. Red at **4 Hz, 50% duty cycle** is **Battery Extremely Low**, with the listed 3.6 V condition. These are historical table labels and conditions, not measured voltage or present battery-health proof for a particular device.
- Orange at **1 Hz, 50% duty cycle** denotes **Battery Charging**; continuously lit orange denotes **Charging Timer Fault**. An LED being off is explicitly listed for an e355 charging on a **gang charger**; do not treat darkness alone as evidence that the device is powered off, healthy or safe.
- The page provides no troubleshooting, service, replacement or payment-flow procedure. Use the exact model/context and the historical deprecation route before operational interpretation.

## Detail locators

- Purpose: pinned raw lines 14–16.
- Complete LED behavior/status table: pinned raw lines 20–28.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/understand-the-led-colors-e355/2026-09-15|Adyen Docs snapshot: Understand the LED colors - e355 (2026-09-15)]]
