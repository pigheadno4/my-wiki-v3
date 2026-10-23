---
title: "Adyen VX690 standalone refund procedure (historical)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/perform-a-refund-vx690"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/perform-a-refund-vx690/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx690, standalone, refunds, deprecation]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] VX690 manual page describes starting a card refund **when the terminal is in standalone mode**. It says Adyen enables refunds per device for security and requires a password for a standalone refund; its steps separately say to enter a PIN to unlock the device. This is a historical menu procedure, not a completed refund or current VX690 eligibility: the separately captured [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation table]] lists VX690 under **29 March 2024 "No more transactions"**. See [[adyen-payment-terminals]].

## Key takeaways

- **Scope and access:** The shopper-return example describes starting a refund to the shopper's card. Refund functionality must be enabled on the specific device, and the page calls for a password. The listed procedure uses an illustrated terminal key + `8` to open Special Payments, then a PIN to unlock the device, followed by entry of the refund amount and continuation like a normal transaction. Do not infer that the password and device PIN are the same credential; the page does not explain their relationship. See pinned raw lines 15–17 and 21–30. The key is pictured in the raw; its label should not be guessed from the image filename.
- **Unsynchronized-data warning:** An exclamation mark at the terminal's top bar means, according to this guide, that data failed to synchronize with Adyen's payments platform because the terminal lacked an outgoing internet connection. That warning does not identify the status of any particular refund. See pinned raw line 19.
- **Outcome boundary:** Entering an amount and following normal-transaction steps is only the described start of a historical refund flow. This page gives no final response, confirmation, funds-return or settlement evidence, and the separate model cutoff limits any present-day payment inference.

## Detail locators

- Standalone scope and exclamation-mark meaning: pinned raw lines 15–19.
- Return/refund framing and per-device enablement/password statement: pinned raw lines 21–22.
- Special Payments key illustration, unlock PIN and amount steps: pinned raw lines 24–30.

## Related

- [[adyen-payment-terminals]] — VX690 physical-terminal and model context.
- [[adyen-standalone-terminals]] — separate current standalone-solution context, whose dated model list does not include VX690.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate dated eVo terminal cutoff.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/perform-a-refund-vx690/2026-09-15|VX690 standalone refund guide, captured 2026-09-15]]
