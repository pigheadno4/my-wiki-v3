---
title: "Adyen Managed Risk webhook — blocked balance released"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.balance.block.released"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.balance.block.released/2026-09-15.md"
tags: [adyen, managed-risk, webhooks, balance-platform]
---

## Overview

This 2026-09-15 API Explorer `latest` snapshot defines the incoming `balancePlatform.managedRisk.balance.block.released` webhook. Adyen sends it when previously blocked funds are released, making them available. It concerns Managed Risk blocked funds associated with a balance account; the webhook is not a merchant release API operation or a payout result. See [[adyen]], [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- The request table requires top-level `data`, `environment` (`test` or `live`) and `type`; `timestamp` is optional and means when the event was queued. Within `data`, `accountHolder`, `amount` and `balanceAccount` are required objects. The released `amount` has required ISO currency and integer value in minor units. The account-holder and balance-account resource IDs and references are optional properties of their required parent objects.
- Optional `balancePlatform` identifies the balance platform; optional `batchReference` identifies the released batch. `blockedBalanceBefore` and `blockedBalanceAfter` are optional amount objects, each with required currency and minor-unit value if present. `creationDate` is when the event was triggered, while `valueDate` is when the amount was released; both are optional and the page gives ISO 8601 extended-format examples.
- The sample's released amount has currency `EUR` and numeric value `25000` in minor units (EUR 250); it also shows negative blocked-balance values before and after. It illustrates one event and does not define a universal sign convention, payout, bank receipt or settlement result.
- The response section shows `200 Success` and says to respond with any `2xx` HTTP status code to accept the webhook. That receiver acknowledgement is distinct from the release event.

## Detail locators

- Event identity and purpose: raw lines 5–7. Full request schema, including optional resource identifiers, amount units and distinct dates: raw lines 9–38.
- Test-environment JSON example with account holder, balance account, released amount, batch reference and blocked-balance snapshots: raw lines 40–77. Receiver response: raw lines 78–86.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — balance-platform context.
- [[adyen-webhooks]] — incoming webhook and acknowledgement context.

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.balance.block.released/2026-09-15|Adyen Managed Risk balance block released webhook, captured 2026-09-15]]
