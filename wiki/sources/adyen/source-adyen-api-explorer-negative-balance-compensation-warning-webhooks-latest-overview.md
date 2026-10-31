---
title: "Adyen negative balance compensation warning webhooks v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/negative-balance-compensation-warning-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, negative-balance]
---

## Overview

This 2026-09-15-captured API Explorer overview is titled **Negative balance compensation warning v1**. Adyen says it sends webhooks about balance accounts whose balance has been negative for at least 20 days. It lists one incoming POST event, `balancePlatform.negativeBalanceCompensationWarning.scheduled`, for scheduled compensation. The overview is a warning and endpoint route, not an event payload schema or proof that compensation has occurred. See [[adyen]], [[adyen-webhooks]], and [[adyen-platforms]].

## Key takeaways

- The overview says that if funds are not transferred to the affected balance account to cover its negative balance before the scheduled compensation date, a transfer is made from the platform's liable balance account on that date. The warning therefore describes a future conditional transfer, not a transfer already made when the warning arrives.
- The page names the warning family as v1 and has a `latest` path. It lists the scheduled-warning event but gives no request-body fields, amount or currency, exact compensation date, webhook acceptance response, or delivery and signature details. Consult the event-specific reference for its payload; this overview alone cannot establish the affected account identity for a particular notification or actual transfer outcome.

## Detail locators

- Family/version title and negative-balance trigger plus conditional liable-account transfer: pinned raw lines 5–7.
- Sole listed POST event: pinned raw lines 9–14.

## Related

- [[adyen-webhooks]] — general incoming webhook context.
- [[adyen-platforms]] — balance accounts and liable-account context.
- [[source-adyen-api-explorer-negative-balance-compensation-warning-webhooks-latest-post-balanceplatform-negativebalancecompensationwarning-scheduled]] — event-specific scheduled-warning reference.

## Raw Sources

- [[raw/adyen/api-explorer/negative-balance-compensation-warning-webhooks/latest/overview/2026-09-15|Negative balance compensation warning v1 overview, captured 2026-09-15]]
