---
title: "Adyen VX680 terminal-local totals printout (historical guide)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/print-shift-and-end-of-day-reports-vx680"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/print-shift-and-end-of-day-reports-vx680/2026-09-15.md"
tags: [adyen, point-of-sale, vx680, payment-terminals, local-totals, terminal-deprecation]
---

## Overview

This [[adyen]] VX680 manual page, titled “Print a summary of transaction totals,” describes a terminal-local printout of total amounts processed since the last counter reset. Although its URL mentions shift and end-of-day reports, the captured text gives this local totals procedure; it does not define a shift period, settlement batch or financial reconciliation report. It was last modified 2020-05-01 and captured 2026-09-15 under terminal deprecation. See [[adyen-payment-terminals]].

## Key takeaways

- For periodic summary reports, the guide advises resetting counters after printing. Its numbered day-totals sequence then says to press **Yes** after printing to reset the counter. Preserve that difference: the page does not explain a no-reset branch or state that every print automatically resets counters. The reset changes the local since-last-reset reporting window. See raw lines 17–31.
- The procedure shows the pictured key + `9`, then an Admin-menu PIN, `4. Totals`, and `2. Print totals`. Do not infer a textual name for the pictured key. For an unknown Admin PIN, the page routes to POS troubleshooting and its Support Team. See raw lines 27–33.
- This local terminal summary is not proof that the listed payments settled, that money reached a bank account, or that accounting has been reconciled. The related [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] overview lists VX680 “No more transactions” on **29 March 2024** (that overview's raw lines 32–35); this old procedure does not establish present device support or payment processing.

## Detail locators

- Summary scope since last reset: raw lines 15–19.
- Conditional periodic-print advice and numbered print/reset sequence: raw lines 21–31, `### Steps`.
- Unknown Admin PIN route: raw lines 28 and 33.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — historical model cutoff and migration overview.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/print-shift-and-end-of-day-reports-vx680/2026-09-15|Print a summary of transaction totals - VX680, 2026-09-15 capture]]
