---
title: "Adyen Capital API: get a grant disbursement"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)/2026-11-07.md"
tags: [adyen, capital, grants, disbursements, api-explorer]
---

## Overview

This 2026-11-07-captured Capital API v1 reference retrieves details of the disbursement identified by `disbursementId` under a grant identified by `grantId`. The Test and Live base URLs use `/capital/v1`. The returned record describes a grant disbursement and repayment configuration; it is not a bank-receipt or debt-completion record. [[adyen]] [[adyen-capital]]

## Key takeaways

- Both path parameters are required and distinct: `grantId` is the grant reference ID; `disbursementId` is the disbursement ID. This GET reference specifies no query parameters or request body.
- The `200` response requires `accountHolderId` and `balanceAccountId` for the recipients, `grantId` and disbursement `id`, an `amount` with currency and minor-unit value, `balances` with fee/principal/total, a `fee.amount`, and `repayment` with basis points and `updateDescription`. The `balances.total` description says it is principal plus fee. These are response fields, not a separate bank transfer or collection confirmation.
- `fundsCollections` is optional. If supplied, its account identification and funds-collection type are optional; the listed types are `UnscheduledRepayment` and `Revocation`. A configured repayment basis-point percentage or collection account information does not prove a repayment occurred.
- The page lists `404` entity-not-found and `422` request-validation errors. It gives no status field for the disbursement and no bank-receipt, settlement, or completed-repayment field.

## Detail locators

- Purpose, Test/Live Capital v1 servers and required path IDs: [[raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)/2026-11-07#L5|raw lines 5–23]].
- Required response identifiers, amounts, balances, fees and optional collections: [[raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)/2026-11-07#L25|raw lines 25–52]].
- Repayment basis points and `404`/`422` error schemas: [[raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)/2026-11-07#L53|raw lines 53–93]].

## Related

- [[adyen-capital]] — grant, disbursement and repayment evidence boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)/2026-11-07|Adyen grant disbursement GET reference capture, 2026-11-07]]
