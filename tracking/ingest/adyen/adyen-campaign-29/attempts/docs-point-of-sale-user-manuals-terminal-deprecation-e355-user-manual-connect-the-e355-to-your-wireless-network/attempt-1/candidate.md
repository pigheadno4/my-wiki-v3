---
title: "Adyen e355 historical Wi-Fi setup"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/connect-the-e355-to-your-wireless-network"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/connect-the-e355-to-your-wireless-network/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e355, wifi, historical]
---

## Overview

This [[adyen]] e355 wireless-network procedure was last modified **2019-05-27** and captured 2026-09-15 under the **terminal-deprecation** manual tree. It describes connecting the physical terminal to Wi-Fi before boarding so it can communicate with Adyen and merchant back-end systems. Its listed Wi-Fi security choices and menu state are historical device instructions, not a present-day network-security recommendation or proof of a working connection, boarding, supported e355 transactions or PCI compliance. See [[adyen-payment-terminals]] and [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]].

## Key takeaways

- Open the e355 Admin menu with the confirm-key image plus **9**, then enter the Admin PIN; the guide says no PIN is required **if the terminal is not yet boarded**. It gives a troubleshooting link for an unknown PIN and `*`/`#` scrolling controls. This does not establish the PIN state of a particular device. See raw lines 19–28.
- Follow Network → Wi-Fi → Networks and either **scan** or **manually add** a network. In the scan branch, choose the network, enter its wireless password, and the guide says the device connects and sets it as default; it then instructs leaving the menu to begin boarding. The described connection is an expected UI result, not a connectivity diagnostic or successful platform registration. See raw lines 29–47.
- In the manual-add branch, enter SSID, choose authentication `WPA` or `WPA-2`, choose wireless-security `TKIP` or `CCMP`, then enter the password. The page says this sets the network as default. These are the **2019 e355 menu options**; do not infer they meet current merchant security policy or that other standards are supported/unsupported now. See raw lines 49–58.
- The source contains a malformed HTML-entity rendering, `Pres&#x73;**&#xA0;1.**`, at the Network step. Treat it as the page's displayed **1. Network** menu instruction, not a literal button sequence. See raw line 29.

## Detail locators

- **Admin menu/PIN and not-yet-boarded exception:** raw lines 19–28.
- **Scan/connect/default-network branch and boarding transition:** raw lines 29–47.
- **Manual SSID/authentication/security/password branch:** raw lines 49–58.

## Related

- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/connect-the-e355-to-your-wireless-network/2026-09-15|e355 Wi-Fi setup — collected 2026-09-15]]
