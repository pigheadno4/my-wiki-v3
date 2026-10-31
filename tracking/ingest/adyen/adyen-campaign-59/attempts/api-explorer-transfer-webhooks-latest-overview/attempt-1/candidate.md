---
title: "Adyen Transfer webhooks v4 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfer-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/transfer-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, transfer-webhooks, platforms, api-explorer]
---

## Overview

This 2026-09-15-captured API Explorer overview is headed **Transfer webhooks v4**. It says Adyen sends webhooks about incoming and outgoing platform transfers and lists `balancePlatform.transfer.created` and `balancePlatform.transfer.updated` as POST event references. The `latest` URL is a captured route label; the page itself supplies the v4 heading. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- The overview proposes using transfer notifications for platform dashboards and tracking incoming funds. It does not define either event's payload fields, status lifecycle, transfer identifiers, failure/reversal handling, or a financial finality rule. Follow the two endpoint references for those contracts. See raw lines 7–17.
- No delivery order, retries, deduplication, authentication or signature rule appears in this 17-line overview. An event listing is not evidence that a transfer was booked or funds arrived. See raw lines 5–17.

## Detail locators

- Family/version and purpose: raw lines 5–9.
- Listed event references: raw lines 11–17.

## Related

- [[adyen-webhooks]]
- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]]

## Raw Sources

- [[raw/adyen/api-explorer/transfer-webhooks/latest/overview/2026-09-15|Transfer webhooks v4 overview, captured 2026-09-15]]
