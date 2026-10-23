---
title: "Clean e355 Bluetooth pairings (deprecated-terminal guide)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-1-clean-the-bluetooth-configuration"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-1-clean-the-bluetooth-configuration/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e355, bluetooth, historical]
---

## Overview

This 2026-09-15-captured [[adyen]] e355 page under terminal-deprecation manuals describes removing Bluetooth pairings before the historical e355/mobile-device flow. It addresses the terminal's paired-device list within [[adyen-payment-terminals]], not merchant configuration, boarding, Bluetooth protocol compatibility or a completed payment. The separately captured [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo/Verix deprecation schedule]] lists **29 March 2024** as the e355 “No more transactions” date; the page's 2026 modification timestamp does not establish restored transaction support.

## Key takeaways

- The opening advice says to remove other paired devices **unless they are necessary** (raw line 16). Its final numbered step instead says to repeat until **all devices are removed** (raw line 35). Preserve this internal tension; the source does not explain how to decide which necessary pairings to keep.
- On the e355, the historical menu route opens Admin, then Network → Bluetooth → Paired devices. The source's confirm-button label is malformed HTML at step 5, so the pinned raw preserves the exact icon reference rather than a clear text button name (raw lines 20–29).
- The operator chooses a device and presses `1. Unpair`; **unpairing is only possible while that device is disconnected** (raw lines 31–33). Removing a pairing is a device-side Bluetooth change and may require pairing again later. The page does not say it deletes merchant configuration, credentials or transaction records.
- These steps do not test a POS App connection or show boarding or payment outcome. The companion Bluetooth overview separately warns that pairing can succeed while mismatched serial protocol versions prevent boarding and transaction start.

## Detail locators

- Conditional clean-pairing advice: raw line 16.
- Admin → Network → Bluetooth → Paired devices path and malformed icon: raw lines 20–29.
- Unpair condition and all-devices endpoint: raw lines 31–35.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-1-clean-the-bluetooth-configuration/2026-09-15|Full pinned e355 Bluetooth cleanup guide]]