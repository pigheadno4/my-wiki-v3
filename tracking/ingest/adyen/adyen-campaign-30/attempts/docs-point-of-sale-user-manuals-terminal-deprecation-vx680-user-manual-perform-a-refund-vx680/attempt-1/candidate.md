---
title: "Adyen VX680 historical standalone refund procedure"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/perform-a-refund-vx680"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/perform-a-refund-vx680/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx680, standalone, refunds, historical]
---

## Overview

This [[adyen]] **VX680** page was last modified 2019-05-20 and captured 2026-09-15 under the terminal-deprecation manual tree. It describes **starting a refund when that terminal is in standalone mode**. Adyen says refund functionality is enabled **per device** for security and that a password is required; the step list separately instructs entering a **PIN code** to unlock the device. The page does not identify whether these labels refer to the same credential. The procedure does not prove that any device is enabled, a refund was accepted, or funds reached a shopper. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] lists VX680 with a historical **29 March 2024** "No more transactions" date. See [[adyen-payment-terminals]].

## Key takeaways

- The procedure is scoped to a **VX680 in standalone mode**. The stated prerequisites are per-device refund enablement and a password. The numbered steps use an **illustrated key plus 8** to open Special Payments, request a PIN code to unlock the device, then say to enter the refund amount and proceed as in a normal transaction. The image-only key must be read from the pinned raw; this page does not provide a textual key name or a result screen. See raw lines 15–17 and 21–30.
- A top-bar **exclamation** means the terminal holds data that failed to synchronize with Adyen's payments platform because it lacked an outgoing Internet connection. The indicator is a failure boundary, not a claim that refund funds were sent or later reconciled. See raw line 19.
- The page says a shopper may return previously purchased goods and the operator might start a refund to pay back the corresponding amount to the shopper's card. That is a scenario and intended action, not confirmation that a particular refund was authorized, completed or credited. See raw lines 21–22.

## Detail locators

- **Standalone mode scope and unsynchronized-data indicator:** raw lines 15–19.
- **Return scenario, per-device enablement and password statement:** raw lines 21–22.
- **Image-only key plus 8, PIN unlock and amount-entry steps:** raw lines 24–30.

## Related

- [[adyen-payment-terminals]]
- [[adyen-standalone-terminals]] — broader solution context; its 2026-09-15 overview has a different dated model list.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/perform-a-refund-vx680/2026-09-15|VX680 standalone refund page — captured 2026-09-15]]
