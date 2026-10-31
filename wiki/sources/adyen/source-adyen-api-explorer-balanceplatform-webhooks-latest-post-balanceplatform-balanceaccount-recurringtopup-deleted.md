---
title: "Balance Platform recurring top-up deleted webhook | Adyen API Explorer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.deleted"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.deleted/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, recurring-top-ups]
---

## Overview

This captured Adyen Balance Platform webhook POST reference describes the incoming `balancePlatform.balanceAccount.recurringTopUp.deleted` event sent when a recurring top-up is successfully deleted from a balance account. It is a configuration deletion event, not a merchant deletion request or evidence that a top-up transfer was funded or booked. The path says `latest`; the captured page does not resolve a numbered webhook API version. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- The request body marks `data`, `environment`, and `type` required. Inside `data`, `accountId` and `webhookTopUpConfiguration` are required; inside that configuration, `counterparty`, `description`, `id`, `status`, `topUpAmount`, and `trigger` are required. `balancePlatform`, `creationDate`, top-level `data.id`, `timestamp`, configuration `mandate`, and `referenceForBeneficiary` are optional in the table. These are table-level field requirements; the page does not specify required child fields within the required object fields. [Raw: Request body, lines 11–30]
- `accountId` identifies the balance account; the nested configuration `id` identifies the recurring top-up configuration. The `status` field describes `active` and `inactive` configurations, `topUpAmount` may be fixed or target, and `trigger` may be schedule or minimum balance threshold. The example's `status: active` appears in a deletion event; read it as example payload content, not proof the deleted configuration remains active. [Raw: Request body, lines 15–27; request example, lines 34–71]
- `environment` can be `test` or `live`. The example includes a fixed EUR amount, a weekly schedule and EUR threshold, a transfer-instrument counterparty, a beneficiary reference, and a mandate; those sample values are not universal requirements or evidence of a particular debit. The response section says any `2xx` accepts the webhook; this acknowledgement does not prove transfer execution or financial finality. [Raw: lines 28–30, 34–81]

## Detail locators

- Event purpose and deletion trigger: opening statement, lines 5–7.
- Full payload field table, requiredness and status/amount/trigger descriptions: Request body, lines 11–30.
- Illustrative envelope and configuration, including `active` status: Request examples, lines 32–72.
- Receiver response and `2xx` acknowledgement: Responses, lines 73–92.

## Related

- [[adyen-webhooks]] — incoming event and acknowledgement context.
- [[adyen-platforms]] — balance-account top-up context; the existing scheduled-top-up sweep guide describes a separate configuration surface and should not be equated to this recurring-top-up event.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.deleted/2026-09-15|Adyen Balance Platform recurring top-up deleted webhook — captured 2026-09-15]]
