---
title: "Adyen VX690 Bluetooth base-station LED states (historical)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-a-vx690-to-a-base-station-with-bluetooth/understand-the-bluetooth-base-station-led-colors"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-a-vx690-to-a-base-station-with-bluetooth/understand-the-bluetooth-base-station-led-colors/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx690, bluetooth, led, deprecation]
---

## Overview

This 2021-modified, 2026-09-15-captured [[adyen]] page maps **VX690 Bluetooth base-station LED behavior** to four historical status labels: powering on, discover mode, pairing and connected. It is an indicator reference within the deprecated VX690 manual, not a network diagnostic or payment result. The separately captured [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation table]] lists VX690 under **29 March 2024 "No more transactions"**. See [[adyen-payment-terminals]].

## Key takeaways

- **Powering on:** All three LEDs—green, orange and blue—light up; the green LED blinks for roughly 10 seconds and then stays on. The table labels this pattern **Powering on**. See pinned raw line 22.
- **Blue LED states:** Slow blinking means **Discover mode enabled**; quick blinking means **Pairing**; steady blue means **Connected** in this base-station table. Preserve the blink rate distinction. See pinned raw lines 23–25.
- **Scope:** The table supplies expected LED labels only. A solid blue LED is not evidence here of terminal boarding, Adyen-platform connectivity, security certification or a successful transaction. The page gives no troubleshooting procedure for an unexpected LED pattern.

## Detail locators

- Page identity and indicator-table context: pinned raw lines 14–20.
- Green/orange/blue power-on sequence: pinned raw line 22.
- Slow/quick/steady blue states: pinned raw lines 23–25.

## Related

- [[adyen-payment-terminals]] — physical-terminal model context.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-connect-a-vx690-to-a-base-station-with-bluetooth]] — separate base-pairing procedure and local connection-status check.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate dated eVo transaction cutoff.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-a-vx690-to-a-base-station-with-bluetooth/understand-the-bluetooth-base-station-led-colors/2026-09-15|VX690 Bluetooth base LED table, captured 2026-09-15]]
