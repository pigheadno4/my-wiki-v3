---
title: "VX675 historical Quick Info and terminal identifiers"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/view-terminal-information-vx675"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/view-terminal-information-vx675/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx675, device-info, historical]
---

## Overview

This [[adyen]] **VX675** page, last modified **2019-04-18** and captured 2026-09-15 under terminal deprecation, describes using the terminal's **Quick Info** menu to view network and device identifiers. It is historical model-specific guidance within [[adyen-payment-terminals]]. Displayed identifiers are not a diagnostic result, verified network connection, boarding or payment outcome. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation schedule]] lists VX675 **“No more transactions” on 29 March 2024** (its raw line 34).

## Key takeaways

- The page instructs pressing a **pictured, unlabeled key together with 5** to open Quick Info (raw lines 19–23). Its image filename is not evidence of a physical button name. The raw line has malformed HTML entities around “at the same time,” so consult the raw rather than inventing further access steps; this page does not mention an Admin PIN step.
- The display lists an **IP address, terminal ID and software version** (raw lines 25–29). These are displayed fields; the page gives no live network test or validation of any particular terminal's status.
- A **QR code** encodes IP address, MAC address, network name, store name, merchant account name and terminal ID (raw line 30). The guide says these values are encoded; it does not say that the QR code authenticates a device or grants account access.
- The page is an information lookup, not a current support or transaction-processing procedure.

## Detail locators

- Quick Info purpose: raw lines 15–19.
- Image-only key plus 5 shortcut and malformed markup: raw lines 21–23.
- Displayed fields: raw lines 25–29.
- QR-encoded network, store, merchant and terminal identifiers: raw line 30.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/view-terminal-information-vx675/2026-09-15|Full pinned VX675 device-info guide]]
