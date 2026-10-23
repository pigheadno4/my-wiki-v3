---
title: "VX690 historical Wi-Fi setup"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-the-vx690-to-your-wireless-network"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-the-vx690-to-your-wireless-network/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx690, wifi, historical]
---

## Overview

This [[adyen]] guide, last modified **2021-12-28** and captured 2026-09-15 in the **terminal-deprecation** VX690 manual tree, describes configuring a VX690 payment terminal's Wi-Fi connection so it can communicate with Adyen's payments platform and the merchant's back-end systems. It belongs to [[adyen-payment-terminals]] and is historical model-specific setup guidance. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation schedule]] lists VX690 **“No more transactions” on 29 March 2024** (that source's raw line 35); a network setup flow is not proof of current terminal support, security compliance, successful boarding or payment processing.

## Key takeaways

- The procedure starts with a **fully charged, powered-on VX690** (raw line 20), then opens the Admin menu with **9 plus an image-only confirm key** (raw line 22). It requires an Admin PIN when boarded; the page expressly says **no Admin PIN is required if not yet boarded** and routes an unknown PIN to troubleshooting (raw lines 24–28). The image-only button should be read from the raw, not guessed from the empty image label.
- In the **scan** branch, select a network and enter its password; the guide says the terminal connects, makes the network default automatically, and then directs the operator to leave the network menu to begin boarding (raw lines 36–48). These are expected procedure descriptions, not observed outcomes on a particular terminal.
- In the **manual-add** branch, enter the SSID, select **WPA or WPA-2** authentication and **TKIP or CCMP** wireless-security options, then enter the password; the page says the terminal connects and makes that network default (raw lines 50–59). These are dated VX690 menu options, not current network-security recommendations or a claim about what a merchant's network policy accepts.
- Network configuration precedes the page's **begin boarding** instruction; it does not itself register the device, establish a durable connection or show payment authorization (raw lines 44–48).

## Detail locators

- Purpose and powered-device prerequisite: raw lines 14–20.
- Image-only Admin-menu key, conditional PIN and menu navigation: raw lines 22–34.
- Scan branch and expected default-network behavior: raw lines 36–48.
- Manual SSID, authentication/security choices and password: raw lines 50–59.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-the-vx690-to-your-wireless-network/2026-09-15|Full pinned VX690 Wi-Fi guide]]
