---
title: "Adyen Docs: Auto Rescue"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/auto-rescue"
raw_files:
  - "adyen/docs/online-payments/auto-rescue/2026-09-15.md"
tags: [adyen, online-payments, auto-rescue, retries, recurring-payments]
---

## Overview

This [[adyen]] Auto Rescue overview describes automatic later retry attempts for shopper-not-present payments that Adyen judges may succeed after an initial failure. It covers refused card transactions and, in its explanatory text, charged-back SEPA direct debit transactions, with subscription renewals as an example. Adyen schedules qualifying attempts at times it selects within a rescue window; the page does not promise that an attempted rescue will succeed.

## Key takeaways

- The distinction between a potentially recoverable failure, such as insufficient funds, and a permanent decline, such as a closed account, drives whether a later attempt may be worthwhile. Adyen says Auto Rescue selects payments with a chance of succeeding; several attempts may be needed within the rescue window.
- Webhooks are a prerequisite. The page says they report retry results, whether another attempt is scheduled, and the end of rescue; an optional payment link can be sent to the shopper after unsuccessful rescue if enabled.
- The overview calls the SEPA direct debit case "charged back," but its SEPA navigation says "refused." Retain that terminology difference when choosing the transaction-specific guide; this overview alone does not resolve it.

## Detail locators

- **Opening explanation**, raw lines 17–23 — supported shopper-not-present examples, refusal versus chargeback, recoverable and permanent examples, scheduling, and rescue window.
- **Requirements**, raw lines 27–34 — webhook setup and the reported process details, including the optional post-failure payment link.
- **Choose transaction type**, raw lines 36–48 — links to the card and SEPA guides and the SEPA navigation wording.

## Related

- [[adyen-online-payments]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/auto-rescue/2026-09-15|Adyen Auto Rescue documentation snapshot (2026-09-15)]]
