---
title: "Adyen VX675 historical standalone refund steps"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/perform-a-refund-vx675"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/perform-a-refund-vx675/2026-09-15.md"
tags: [adyen, point-of-sale, vx675, standalone, refunds, legacy]
---

## Overview

This [[adyen]] page, last modified in 2019 and captured 2026-09-15, gives a short VX675 **standalone-mode** refund initiation sequence. It says Adyen enables refund functionality **per device**, and it separately mentions a password to perform a standalone refund and a PIN in the numbered unlock step. These are distinct terms in the source; the page does not explain their relationship or provide either credential. See [[adyen-payment-terminals]] and [[adyen-standalone-terminals]].

The page sits in a deprecated-terminal manual. A separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] table lists VX675 with **29 March 2024** under “No more transactions” (that page's raw lines 32–34). The 2019 steps are historical; following them would not establish current device eligibility, an accepted refund, actual shopper-card credit or settlement.

## Key takeaways

- **Unsynchronized-data indicator:** The guide says an exclamation mark in the terminal's top bar means it holds data that failed to synchronize with Adyen's platform because there was no outgoing internet connection. This is a warning about pending data, not a documented refund result or an explicit refund-blocking rule in this page. See pinned raw line 19.
- **Enablement and credentials:** Refund functionality is described as enabled per device. The prose requires a password for a standalone refund, while the steps ask for a PIN to unlock the device; preserve both words and do not infer they are the same credential. See pinned raw lines 21–22 and 28–30.
- **Manual sequence:** Press the illustrated VX675 button plus **8** to open Special Payments, enter the device-unlock PIN, enter the refund amount and proceed as with a normal transaction. The raw image identifies the button; the page gives no completion screen, provider response, refund reference or posting evidence. See pinned raw lines 24–30.

## Detail locators

- Standalone-mode scope and data synchronization warning: pinned raw lines 15–19.
- Per-device enablement, password statement and Special Payments/PIN/amount steps: pinned raw lines 21–30.
- Button image: pinned raw line 28; identify it from the image rather than filename.

## Related

- [[adyen-payment-terminals]] — VX675 physical-device context.
- [[adyen-standalone-terminals]] — standalone transaction model, with current-model scope separately documented.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — historical VX675 transaction cutoff.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/perform-a-refund-vx675/2026-09-15|VX675 standalone refund page, captured 2026-09-15]]
