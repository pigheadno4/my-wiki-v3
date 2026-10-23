---
title: "e355 Bluetooth payment path (historical guide)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e355, bluetooth, historical]
---

## Overview

This [[adyen]] e355 Pin Entry Device guide was last modified in **2019** and captured 2026-09-15 under terminal-deprecation manuals. It is a short navigation and compatibility page for a Bluetooth-connected POS App path: clean up pairing, pair the mobile device, reboard if needed, and start a transaction. It is not a payment result or present-day support claim; see [[adyen-payment-terminals]] and the later [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo/Verix deprecation schedule]], which lists **29 March 2024** as the e355 “No more transactions” date.

## Key takeaways

- The page recommends a clean Bluetooth configuration and removal of unnecessary paired devices, with a link to a separate unpairing procedure (raw lines 19–21). This is advice in this guide, not a blanket requirement to unpair every device.
- Its listed flow links to e355/mobile-device pairing, removing configuration and reboarding, and starting a transaction (raw lines 23–29). The document labels this “3 steps” yet the first linked item is named “Step 2” and the last “Step 3”; the separate clean-configuration link appears above the list. Follow the child guides for procedures rather than inferring missing steps from these labels.
- The POS App and e355 should use the same serial communication protocol version. The page calls version **2** current at its 2019 modification time. With a mismatch, Bluetooth pairing can succeed while boarding and transaction start fail, leaving the app in initialization (raw line 31). Pairing alone therefore does not establish a usable payment connection.
- The page gives no card-present interaction, authorization response, capture, settlement or observed transaction outcome. Its “Start a transaction” item is a link to another guide (raw line 29), and neither it nor historical successful pairing overrides later device deprecation.

## Detail locators

- Clean Bluetooth configuration advice and linked unpairing guide: raw lines 19–21.
- Linked pair, reboard and transaction-start stages: raw lines 23–29.
- Same-protocol requirement, historical version number and mismatch failure: raw line 31.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-step-2-pair-the-e355-with-a-mobile-device]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/2026-09-15|Full pinned e355 Bluetooth guide]]