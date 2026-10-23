---
title: "MX925 terminal boarding (historical guide)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/mx925-user-manual/board-the-terminal-mx925"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/mx925-user-manual/board-the-terminal-mx925/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, mx925, boarding, historical]
---

## Overview

This [[adyen]] MX925 boarding guide was last modified in **2019** and captured on 2026-09-15. It describes historical Customer Area and Adyen POS App routes for registering and configuring that physical payment terminal. It sits under terminal deprecation and is **not current MX925 payment-processing guidance**: the separately captured [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo/Verix deprecation schedule]] lists **29 March 2024** as the MX925 “No more transactions” date. See [[adyen-payment-terminals]].

## Key takeaways

- The stated prerequisites are successful internet connection and device security inspection before boarding (raw line 21). The page does not specify the inspection checklist; it links to the MX925 quick-start guide. Do not treat connectivity alone as a passed inspection.
- In the historical Customer Area route, the operator logs in, switches to the intended merchant account, uses the Point-of-Sale widget to register terminal type, serial number and merchant account, retrieves a one-time password, then enters it on the terminal. The device may reboot more than once and receive merchant configuration (raw lines 25–46). These are merchant-account-scoped administrative actions, not evidence that a device is currently eligible or boarded.
- In the historical POS App route, the operator first obtains the terminal IP address. Android instructions require API credential details and adding that IP; the app identifies the terminal, synchronizes and verifies configuration before a restart/update (raw lines 48–68). The Android UI prompts a Bluetooth-or-Wi-Fi choice, but the instructions here use the IP address; the page does not establish a Bluetooth pairing procedure. The iOS route accepts hostname or IP, shows “Not Boarded,” then offers “Board device” and a restart/configuration update (raw lines 70–81).
- The guide points custom systems to legacy Java Native Interface, COM, C, iOS and Android library-integration guides and points boarding issues to POS Troubleshooting (raw lines 83–93). Those linked procedures are navigation, not evidence of current library support.
- This 2019 guide says processing can begin after configuration in its historical flow (raw lines 43–46, 67–81). The later deprecation schedule supersedes any inference of present-day MX925 transaction availability; neither this guide nor a successful configuration step proves payment authorization or settlement.

## Detail locators

- Internet and inspection prerequisite: raw lines 19–21.
- Customer Area merchant-account, serial-number and one-time-password route: raw lines 25–46.
- POS App Android and iOS boarding routes: raw lines 48–81.
- Custom-library and troubleshooting navigation: raw lines 83–93.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[adyen-terminal-management]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/mx925-user-manual/board-the-terminal-mx925/2026-09-15|Full pinned MX925 boarding guide]]