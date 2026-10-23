---
title: "VX675 historical transaction-totals print and reset"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/print-shift-and-end-of-day-reports-vx675"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/print-shift-and-end-of-day-reports-vx675/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx675, totals, historical]
---

## Overview

This [[adyen]] **VX675** guide, last modified **2019-05-10** and captured 2026-09-15 under terminal deprecation, describes printing a terminal summary of **total amounts processed since the last reset**, followed by an optional counter reset for periodic reporting. Although its URL says shift/end-of-day and the steps call these “day totals,” the described window is **reset-based**, so it is not necessarily a calendar-day, shift, settlement-batch or bank-reconciliation report. This device-local procedure belongs to [[adyen-payment-terminals]], with [[adyen-reporting]] providing separate reporting context. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation schedule]] lists VX675 **“No more transactions” on 29 March 2024** (its raw line 34).

## Key takeaways

- The terminal can print totals **since the last reset** (raw lines 17–19). The page gives no transaction-level rows, timezone or reconciliation fields and no evidence of capture, settlement or bank receipt.
- Access uses an **image-only VX675 key plus 9**, then the **Admin menu PIN**; if it is unknown, the page points to POS troubleshooting and Adyen Support (raw lines 27–28, 33). The image-only key should be read from the raw illustration, not guessed from its empty image label.
- The steps select **4. Totals** and **2. Print totals** (raw lines 29–30). The pinned raw has garbled HTML/Markdown around the “Print totals” line, so the exact menu rendering should be checked on the historical device/source rather than reconstructed from the malformed text.
- **After printing**, the guide says to press **Yes** to **reset the counter** (raw line 31). That reset changes the period for later summaries; printing and resetting are distinct actions. The page advises resetting after printing if a periodic summary is desired (raw line 23). It does not state that reset cancels transactions or alters Adyen settlement.

## Detail locators

- Reset-based total-amount scope: raw lines 15–19.
- Periodic report/reset advice: raw lines 21–25.
- Image-only shortcut, PIN and totals menu: raw lines 27–30.
- Post-print **Yes** counter reset and missing-PIN Support route: raw lines 31–33.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[adyen-reporting]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/print-shift-and-end-of-day-reports-vx675/2026-09-15|Full pinned VX675 totals guide]]
