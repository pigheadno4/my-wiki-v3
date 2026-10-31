---
title: "Grant updated webhook | Adyen Capital webhooks"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.updated"
raw_files:
  - "adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.updated/2026-09-15.md"
tags: [adyen, capital, grants, webhooks]
---

## Overview

This captured `POST balancePlatform.grants.updated` Capital webhook reference says [[adyen]] sends information about a grant after that grant is updated. It gives financing disbursement to a user and user repayment as examples of when the notification can arrive. It is an incoming grant-lifecycle event contract, not a merchant grant-update request; the captured `latest` URL does not establish the current version. [[adyen-capital]] [[adyen-webhooks]]

## Key takeaways

- The request-body table marks `balances` and its `currency`, `fee`, `principal` and `total` fields required. It describes `total` as fee plus principal and identifies these as grant amounts, not a payment or bank-transfer receipt. The table also requires `grantAccountId`, `grantOfferId`, grant-reference `id`, and `status` with a required `code`.
- `counterparty` is optional; its account-holder, balance-account and transfer-instrument IDs are optional fields described as possible disbursement recipients/resources. A reported recipient identifier alone does not prove delivery to that destination.
- Status codes listed are `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed`, `Revoked`, `Requested`, `Reviewing`, `Approved`, `Rejected`, and `Cancelled`. Optional `status.actions` carry required `actionCode` and `resolved` fields within each action. The reference does not provide a transition graph or say that every listed state follows the same funding or repayment path.
- The response section says any `2xx` accepts the webhook. This is a receiver acknowledgment, separate from grant status and any disbursement, booked transfer, repayment or bank receipt. The captured page has no example payload or delivery, ordering, retry, deduplication or signature contract.

## Detail locators

- Event purpose and illustrative triggers: raw lines 5–9.
- Required balance, grant and status fields: raw lines 11–20 and 25–32.
- Optional counterparty resource identifiers: raw lines 21–24.
- Acknowledgment response: raw lines 34–42.

## Related

- [[adyen]] — provider.
- [[adyen-capital]] — grant lifecycle and financing context.
- [[adyen-webhooks]] — general webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.updated/2026-09-15|Captured balancePlatform.grants.updated reference]]
