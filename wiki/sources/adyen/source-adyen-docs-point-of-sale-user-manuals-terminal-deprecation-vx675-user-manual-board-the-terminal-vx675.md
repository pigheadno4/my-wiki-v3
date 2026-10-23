---
title: "Adyen VX675 historical terminal boarding guide"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/board-the-terminal-vx675"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/board-the-terminal-vx675/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx675, boarding, historical]
---

## Overview

This [[adyen]] VX675 guide, last modified 2019-05-14 and captured 2026-09-15 under terminal deprecation, describes registering the terminal with Adyen through the historical POS App or Customer Area; it also points custom integrations to classic-library guides. It belongs with [[adyen-payment-terminals]]. Its after-configuration statement that payments can begin is historical procedure wording: the later [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] table lists VX675 "No more transactions" on **29 March 2024**. Neither the old screens nor this snapshot establishes present support, successful boarding, authorization or settlement.

## Key takeaways

- **Precondition:** connect the VX675 to the internet and perform a device security inspection before boarding. The guide then shows a PIN-gated Admin menu path to Network → Wi-Fi → TCP/IP settings for noting the terminal IP address. The opening key is image-only in the raw, so use its image locator rather than inferring a key label. See raw lines 18–32.
- **Integrated POS App route:** Android asks for API credential details, offers a Bluetooth/Wi-Fi selection, and then instructs entering the terminal IP and selecting Add Device. iOS asks for hostname or IP, displays a "Not Boarded" listing, then offers Board Device. Both routes describe boarding, restart and subsequent merchant-configuration update as expected steps; these are not observed outcomes. The iOS menu icon is image-only. See raw lines 34–57.
- **Other routes:** the custom-system section links Java Native Interface, Windows COM, C, iOS and Android classic-library guides, without providing their procedures. The Customer Area standalone section uses the Merchant account Point of Sale widget and Register Terminal, requests serial number and API credential, then a shown one-time password entered on the powered-on terminal; it says the terminal may reboot more than once. Another standalone paragraph says to use the POS App once for initial registration/configuration, then continue without that app or integrations. These are distinct described paths, not proof either was completed. See raw lines 59–94.
- **Later cutoff:** the related deprecation page lists VX675 among PTS PCI 3 eVo terminals with "No more transactions" on 29 March 2024. It separately says classic-library transactions would no longer be possible after 31 March 2024. Do not use this older boarding guide's payment-ready wording or library links as current enablement guidance. See [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] and its raw lines 32–35, 50–54.

## Detail locators

- Security/network prerequisite and pictured Admin key: raw lines 18–32.
- POS App Android and iOS steps, status and update wording: raw lines 34–57.
- Classic-library navigation: raw lines 59–67.
- Customer Area and POS App standalone variants: raw lines 69–94.

## Related

- [[adyen-payment-terminals]]
- [[adyen-terminal-management]]
- [[adyen-standalone-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/board-the-terminal-vx675/2026-09-15|VX675 boarding guide — collected 2026-09-15]]
