---
title: "Adyen e355 view device info (historical manual)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/view-terminal-information-e355"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/view-terminal-information-e355/2026-09-15.md"
tags: [adyen, point-of-sale, e355, terminal-deprecation, device-information]
---

## Overview

This [[adyen]] e355 guide, last modified 2019-04-23 and captured 2026-09-15 under terminal deprecation, shows how to view the device's information screen. It is a historical model-specific lookup in [[adyen-payment-terminals]], not a current support or terminal-health check.

## Key takeaways

- The documented access action is to press the **illustrated button and 5 at the same time** (pinned raw line 21). The raw text embeds an image for the button and contains HTML entities; consult that exact line/image before applying the gesture. This page states no role, PIN or passcode prerequisite.
- The display then shows the terminal's IP address, terminal ID and software version. Its QR code encodes IP and MAC addresses, network name, store name, merchant account name and terminal ID (lines 23–28). Treat the QR data as device/network/account identifiers when sharing it.
- A displayed version or identifier is inventory information. This page does not demonstrate network reachability, boarding status, security state, current e355 availability or any authorized/settled payment.

## Detail locators

- Purpose and simultaneous-button instruction: pinned raw lines 15–21.
- Displayed fields and QR contents: pinned raw lines 23–28.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/view-terminal-information-e355/2026-09-15|Adyen Docs snapshot: View device info - e355 (2026-09-15)]]
