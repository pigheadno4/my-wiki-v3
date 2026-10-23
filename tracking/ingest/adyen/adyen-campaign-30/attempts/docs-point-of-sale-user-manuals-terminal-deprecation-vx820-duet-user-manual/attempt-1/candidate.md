---
title: "Adyen VX820 Duet historical user manual"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx820-duet, user-manual, historical]
---

## Overview

This [[adyen]] **VX820 Duet** manual hub was last modified 2021-03-25 and captured 2026-09-15 under the terminal-deprecation tree. It outlines physical setup of the VX820 payment terminal (PED) with the **Duet base station and built-in printer**, then routes to paper installation, device security inspection and boarding guides. The page says new terminals of this type cannot be ordered. Its quickstart language about getting a "new terminal" running is historical template wording, not a current ordering or processing claim. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] table names **VX820 and VX820 Duet** in one row with **29 March 2024** as "No more transactions"; it gives a distinct 31 March 2024 classic-library transaction cutoff. See [[adyen-payment-terminals]].

## Key takeaways

- The quickstart connects a power supply cable and the Duet base, uses the base's **ETH** port for Internet access, then links to paper-roll installation, device security inspection and terminal boarding. These are ordered setup topics, not evidence that a device passed inspection, joined a network, boarded or processed a payment. See raw lines 23–32.
- **Wrong cable/port combinations can severely damage the device**; the page gives an Ethernet cable in the RS232 port as an example. It says a POS-to-PED serial connection is technically possible, while Adyen strongly recommends Ethernet for speed and operating-system performance. The recommendation does not make serial physically impossible. See raw lines 34–36.
- An **exclamation mark in the terminal's top bar** means the terminal holds data it failed to synchronize with Adyen's payments platform because it lacked an outgoing Internet connection. This is the manual's historical indicator interpretation, not confirmation of transaction status, eventual synchronization or settlement. See raw line 38.
- The provided-component list distinguishes the **VX820 PED** from the **Duet printer base**, and also names a power supply, privacy shield, Ethernet dongle and one paper roll. See raw lines 40–47.

## Detail locators

- **Dated no-new-orders statement and deprecation link:** raw lines 15–19.
- **Power, ETH, paper, inspection and boarding quickstart:** raw lines 23–32.
- **Cable damage, serial/Ethernet preference and unsynchronized-data indicator:** raw lines 34–38.
- **PED, Duet base and other supplied components:** raw lines 40–47.

## Related

- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/2026-09-15|VX820 Duet manual hub — captured 2026-09-15]]
