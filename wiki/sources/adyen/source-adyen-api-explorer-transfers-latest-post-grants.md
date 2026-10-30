---
title: "Adyen Transfers API v4: POST /grants"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/post/grants"
raw_files:
  - "adyen/api-explorer/transfers/latest/post/grants/2026-09-15.md"
tags: [adyen, transfers-api, capital, grants, api-reference]
---

## Overview

This 2026-09-15-captured Transfers API v4 test-server reference defines `POST /grants` to request payout of a selected [[adyen-capital|Adyen Capital]] grant offer. The grant account, selected offer, receiving counterparty, and returned grant reference are distinct identities. A successful request response is not evidence that the grant was accepted, disbursed, booked, received, or repaid.

## Key takeaways

- The request property table requires `grantAccountId` and `grantOfferId`. An optional `counterparty` object can identify a receiving account holder's balance account or that account holder's legal entity transfer instrument; its two child IDs are each marked optional, with no choice/exclusivity rule stated here. The table does not separately state whole-body requiredness.
- `Idempotency-Key` is an optional header with a 64-character maximum; a UUID is recommended. This page gives no retry or deduplication semantics.
- The 200 response identifies the grant reference (`id`), grant account and selected offer, reports `status` among `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed`, and `Revoked`, and includes balances. Optional amount, fee, counterparty and repayment objects may appear. The repayment description covers daily deduction from incoming net volume in basis points and an optional 30-day threshold; `maximumDays` applies only when `contractType` is `loan`, although this request table does not define `contractType`. The example is `Pending`, so a 200 response alone does not prove payout completion.
- Error categories are 400, 401, 403, 404, 422 and 500. The 404 description says a *payment* was not found, an object-name mismatch with this grant request; do not infer which grant object was missing. The page names no specific permission role, offer-acceptance step, transfer webhook or final funding state.

## Detail locators

- Purpose, test v4 server, optional idempotency header and request fields: raw lines 5–27. Request example: lines 29–40.
- Response identifiers, amounts, balances, repayment and status: raw `### 200 Success`, lines 43–75. Pending example: lines 197–232.
- Error schemas and 404 wording: raw lines 78–195.

## Related

- [[adyen-capital]] — financing offer and grant context.
- [[adyen-api-access]] — general credentials; this endpoint reference states only 401/403 classes.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/post/grants/2026-09-15|POST /grants captured 2026-09-15]]
