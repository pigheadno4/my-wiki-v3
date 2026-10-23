---
title: "Adyen VX690 historical transaction-totals print and reset"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/print-shift-and-end-of-day-reports-vx690"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/print-shift-and-end-of-day-reports-vx690/2026-09-15.md"
tags: [adyen, point-of-sale, vx690, totals, reports, legacy]
---

## Overview

This [[adyen]] VX690 manual page, last modified in 2019 and captured 2026-09-15, describes printing a terminal summary of **total amounts processed since the last counter reset**. Although the path mentions shift and end-of-day reports and the steps call the printout “day totals,” the page defines the counting window by the last reset, not by a calendar day or shift. See [[adyen-payment-terminals]]; this local terminal summary is distinct from [[adyen-reporting]] financial reports.

The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] schedule lists VX690 with **29 March 2024** under “No more transactions” (that page's raw lines 32–35). Printing a historical terminal total is not proof of current device support, particular payment authorization, reconciliation, settlement, payout or bank receipt.

## Key takeaways

- **PIN-gated print path:** The guide uses an illustrated VX690 key with **9**, then the Admin-menu PIN, **4. Totals** and **2. Print totals**. The raw page's Print totals line has malformed markup; use the pinned line and button image for exact interface identification rather than guessing from the image filename. Unknown Admin PINs route to POS Troubleshooting/Support. See pinned raw lines 25–33.
- **Reset changes the next summary's window:** The page first advises resetting counters after printing **if** periodic summary reports are wanted. Its numbered sequence then expressly says to press **Yes** to reset the counter after printing. Do not collapse the conditional advice into an always-required precondition or omit the explicit reset action; it changes the since-last-reset basis for later local totals. The page does not say that resetting changes prior payments or settlement records. See pinned raw lines 17–23 and 31.
- **Report scope:** The page describes an overview of total amounts processed since the last reset; it does not supply transaction-level, settlement or payout fields. See pinned raw lines 15–19.

## Detail locators

- Summary definition and counting window: pinned raw lines 15–19.
- Conditional periodic-report advice: pinned raw line 23.
- Illustrated key, Admin PIN, Totals/Print totals menu labels, reset prompt and PIN-help route: pinned raw lines 25–33.

## Related

- [[adyen-payment-terminals]] — VX690 physical-device context.
- [[adyen-reporting]] — separate provider reporting and reconciliation scope.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — later VX690 transaction cutoff.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/print-shift-and-end-of-day-reports-vx690/2026-09-15|VX690 transaction-totals print guide, captured 2026-09-15]]
