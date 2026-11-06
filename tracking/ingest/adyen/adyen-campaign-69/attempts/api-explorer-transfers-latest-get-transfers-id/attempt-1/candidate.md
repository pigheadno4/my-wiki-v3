---
title: "Transfers API: get a transfer by ID"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/get/transfers/(id)"
raw_files:
  - "adyen/api-explorer/transfers/latest/get/transfers/(id)/2026-11-07.md"
tags: [adyen, transfers, platforms, api-explorer]
---

## Overview

This 2026-11-07 Transfers API `latest` v4 TEST reference for `GET /transfers/{id}` returns details of the transfer identified by required path `id`. The captured server is `https://balanceplatform-api-test.adyen.com/btl/v4`. The page does not specify a caller role. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- A 200 response requires `amount` (currency and value in minor units), `category`, and `status`. The ID and many associated account, counterparty, payment-instrument, event, review, tracing, tracking, and transaction-rule fields are optional in the response schema. Category includes bank, card, grants, interest, internal, issuedCard, platformPayment, and topUp.
- Status examples distinguish `received` (outgoing request created), `refused` (Adyen rejected the request), `authorised` (funds reserved), `booked` (funds deducted from the user's balance account), `failed` (counterparty bank rejection), and `returned` (counterparty bank return). A booked readback is not proof of beneficiary bank receipt.
- Optional `events` describes events leading to current status; accounting, tracing, and tracking are distinct event types. `transactionId` is sent only for accounting events where the balance changes. Optional `review` can show approvals required or SCA status; it does not make approval universal. If an execution date is set, the reference says status remains `received` and reason `pending` until that date.
- The 200 JSON example illustrates one booked internal transfer with accounting mutations and sequence number 3. Its sample IDs, balances, dates, and event progression are illustrative rather than universal.

## Detail locators

- Path, required response fields, category and counterparty identities: pinned raw lines 5–64.
- Events, conditional fields, execution date, status, review and transaction rules: pinned raw lines 65–171.
- 401, 403, 422 and 500 problem schemas: pinned raw lines 174–271.
- Booked internal-transfer example: pinned raw lines 273–363.

## Related

- [[adyen-platforms]] — platform transfer context.
- [[source-adyen-api-explorer-transfers-latest-overview]] — Transfers API v4 overview.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/get/transfers/(id)/2026-11-07|Transfer detail API Explorer snapshot]]