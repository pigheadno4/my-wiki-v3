---
title: "Adyen VX820 historical terminal boarding"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx820-user-manual/board-the-terminal-vx820"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-user-manual/board-the-terminal-vx820/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx820, boarding, historical]
---

## Overview

This 2019-modified [[adyen]] guide records how the **VX820 non-Duet** terminal was boarded to register it with Adyen's payments platform using the historical Adyen POS App or linked classic-library integrations. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation schedule]] lists VX820 and VX820 Duet with **29 March 2024** as “No more transactions” (schedule raw line 34), and classic-library transactions ending after **31 March 2024** (schedule raw line 52). The guide's post-boarding “begin processing payments” wording is historical and does not establish current boarding support or transaction capability. [[adyen-payment-terminals]]

## Key takeaways

- The guide says to board **only after** a successful internet connection and device-security inspection. Its VX820 admin-menu path uses the pictured key plus **9**, an Admin PIN, **Network → Ethernet → TCP/IP settings**, and noting the terminal IP address before POS App setup. The pictured key is not textually identified, and the guide does not supply an Admin PIN. See raw lines 18–32.
- The Android POS App path says to enter API-credential details, select **Payment device**, enter the terminal IP and tap **Add Device**. The page says the app then identifies the terminal, synchronizes with Adyen, verifies configuration, and the terminal restarts and updates merchant configuration. This is the page's expected sequence, not evidence that a specific device successfully boarded or processed a payment. See raw lines 34–44.
- The iOS POS App path instead selects the payment-device menu, adds a hostname or IP, shows the device as **Not Boarded**, then offers **Board device** and a restart/configuration update. The guide does not show the Android API-credential entry as an iOS step. See raw lines 46–57.
- The “library integrations” section only links Java Native Interface, Windows COM, C, iOS and Android integration guides for custom systems. Those links are not instructions or proof of a working library route; the independently read eVo schedule says classic-library transactions were to end after 31 March 2024. See raw lines 59–69 and deprecation schedule raw lines 50–54.
- This page belongs to the **VX820 user-manual** route and does not document the separate VX820 Duet base/printer model. The parent VX820 hub states new units of this type cannot be ordered, while this child page's older boarding wording remains preserved as historical documentation. See the parent [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual]] and the deprecation schedule, not a current-support inference.

## Detail locators

- Internet/security prerequisites and Admin-menu/IP lookup: raw lines 18–32.
- Android and iOS app boarding paths: raw lines 34–57.
- Custom-system library navigation and POS Troubleshooting route: raw lines 59–69.

## Related

- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-user-manual/board-the-terminal-vx820/2026-09-15|VX820 boarding manual snapshot]]
