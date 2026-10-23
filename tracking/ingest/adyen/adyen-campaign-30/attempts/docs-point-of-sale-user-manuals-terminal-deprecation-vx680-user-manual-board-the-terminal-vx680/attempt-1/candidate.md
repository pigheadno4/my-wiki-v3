---
title: "Board the terminal - VX680 (historical guide)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/board-the-terminal-vx680"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/board-the-terminal-vx680/2026-09-15.md"
tags: [adyen, point-of-sale, vx680, boarding, terminal-deprecation, historical]
---

## Overview

This [[adyen]] VX680 boarding guide was last modified 2019-05-14 and captured 2026-09-15 under the deprecated-terminal manuals. It describes registering a physical VX680 with Adyen through integrated POS App or library paths, or through Customer Area or a one-time POS App setup for standalone use. See [[adyen-payment-terminals]] and [[adyen-standalone-terminals]]. It is a historical procedure, not evidence of current VX680 support or a completed boarding or payment.

## Key takeaways

- The guide says to connect the device to the internet and perform a device security inspection **before** boarding; it points to the VX680 quick start guide for those preparations. See raw lines 18–20.
- For the integrated POS App path, the manual uses a PIN-gated Admin menu to find the terminal IP address, then describes Android API-credential entry and device selection by IP address, or iOS device selection by hostname/IP and an explicit **Board Device** action. It says the terminal restarts and updates merchant configuration after boarding begins. These are described steps, not observed success. See raw lines 24–57. The Android instructions mention a Bluetooth-or-Wi-Fi prompt but give an IP-address entry next; the download/install line is incomplete, so the raw is not a reliable app-install reference.
- For the Customer Area standalone path, the manual describes merchant-account **Point of Sale** widget registration using terminal serial number and an API credential, followed by a one-time password entered on the powered-on terminal; it warns that the terminal may reboot more than once. See raw lines 69–88. Its separate Adyen Application standalone path says to use the POS App once to register and configure standalone mode, then operate without the App or integrations. See raw lines 90–92.
- The manual says payments can begin once the latest merchant configuration has applied (raw lines 43–44, 56–57, 87–88). That older readiness statement is limited by the linked [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation schedule]], which lists VX680 **“No more transactions” on March 29, 2024** (deprecation raw lines 32–35). Neither statement establishes current device eligibility, actual configuration, authorization, or settlement.

## Detail locators

- **Precheck and illustrated Admin-menu/IP-address sequence:** raw lines 18–32. The key symbol in step 1 is image-only/malformed in this capture; consult the raw and image rather than guessing its label.
- **Android POS App entry, credential, device selection, synchronization and restart:** raw lines 34–44.
- **iOS POS App hostname/IP, Not Boarded state, Board Device and restart:** raw lines 46–57; the menu icon is image-only.
- **Custom integrated libraries:** raw lines 59–67 are links to separate Java Native Interface, Windows COM, C, iOS and Android guides, not procedures in this page.
- **Customer Area and POS App standalone alternatives:** raw lines 69–92.

## Related

- [[adyen-payment-terminals]]
- [[adyen-terminal-management]]
- [[adyen-standalone-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/board-the-terminal-vx680/2026-09-15|VX680 boarding guide — collected 2026-09-15]]
