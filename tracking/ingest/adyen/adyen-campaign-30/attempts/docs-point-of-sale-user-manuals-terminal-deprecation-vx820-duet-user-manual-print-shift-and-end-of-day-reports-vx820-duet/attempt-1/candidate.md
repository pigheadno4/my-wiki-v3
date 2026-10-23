---
title: "Adyen VX820 Duet terminal-local totals printout (historical guide)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/print-shift-and-end-of-day-reports-vx820-duet"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/print-shift-and-end-of-day-reports-vx820-duet/2026-09-15.md"
tags: [adyen, point-of-sale, vx820-duet, payment-terminals, local-totals, terminal-deprecation]
---

## Overview

This [[adyen]] VX820 Duet manual page, titled “Print a summary of transaction totals,” describes printing the terminal's summary of amounts processed since its last counter reset. Although the URL mentions shift and end-of-day reports, the captured page describes this local totals procedure; it does not define a shift period, settlement batch or financial reconciliation report. It was last modified 2020-05-01 and captured 2026-09-15 under terminal deprecation. See [[adyen-payment-terminals]].

## Key takeaways

- The guide says that if a summary is printed periodically, reset the counters after printing. Its numbered sequence then instructs the operator to press **Yes** to reset the counter after the day-totals print. Preserve both wordings: the page does not explain a no-reset branch or say that all printing necessarily resets counters. Resetting changes the local since-last-reset reporting window. See raw lines 17–31.
- The route uses an image-only key followed by `+ 9`, an Admin-menu PIN, `4. Totals`, and `2. Print totals`; the image-only key must be taken from the raw, not assigned a guessed label. If the Admin PIN is unknown, the page directs the operator to its troubleshooting section and Support Team. See raw lines 27–33.
- A terminal-local amount summary and counter reset are not evidence that all payments settled, that funds reached a bank account, or that a merchant's books reconcile. The related [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] overview lists VX820 Duet “No more transactions” on **29 March 2024** (that overview's raw lines 32–35); this old print procedure is not current transaction-support proof.

## Detail locators

- Summary scope since last reset: raw lines 15–19.
- Conditional periodic-print advice and numbered print/reset instructions: raw lines 21–31, `### Steps`.
- Unknown Admin PIN route: raw lines 28 and 33.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — historical model cutoff and migration overview.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/print-shift-and-end-of-day-reports-vx820-duet/2026-09-15|Print a summary of transaction totals - VX820 duet, 2026-09-15 capture]]
