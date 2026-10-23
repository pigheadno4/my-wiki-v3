---
title: "Adyen e315 user manual (historical overview)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, e315, terminal-deprecation, user-manual]
---

## Overview

This [[adyen]] e315 manual overview, last modified 2021-03-25 and captured 2026-09-15, is a historical entry point under terminal deprecation. It explicitly says new e315 terminals cannot be ordered. Route model-specific physical-device material through [[adyen-payment-terminals]]; the linked child guides own their procedures.

## Key takeaways

- The quickstart sequence is **charge → device security inspection → network connection using the iOS device's connection → board the terminal** (pinned raw lines 23–28). The security inspection is part of the sequence, not an optional cosmetic check. The page links to separate inspection and boarding guides for detail.
- The page says completing these steps makes the reader “ready to process payments” (line 30). Read that as historical quickstart wording, not proof of current device support, merchant enablement, successful authorization or settlement—especially alongside the explicit no-new-orders notice (line 19).
- Supplied components are an e315 payment terminal and USB-to-Micro-USB cable; the page names Adyen POS App or the merchant's own POS app as integration routes (lines 32–37). It supplies no installation, app-version, security-certification or payment-test result.

## Related

- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — historical deprecation overview.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-inspect-device-security-e315]] — separate security-inspection guide.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-board-the-terminal-e315]] — separate boarding guide.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/2026-09-15|Adyen Docs snapshot: e315 user manual (2026-09-15)]]
