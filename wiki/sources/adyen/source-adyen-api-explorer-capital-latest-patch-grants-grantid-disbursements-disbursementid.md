---
title: "Adyen Capital API v1: update disbursement repayment configuration"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/patch/grants/(grantId)/disbursements/(disbursementId)"
raw_files:
  - "adyen/api-explorer/capital/latest/patch/grants/(grantId)/disbursements/(disbursementId)/2026-11-07.md"
tags: [adyen, capital, grants, disbursements, repayment]
---

## Overview

This captured Capital API v1 PATCH reference updates a grant disbursement's repayment percentage in basis points. The capture conflicts on the deduction base: its operation description says the user's net income, while its request and response `basisPoints` rows say incoming net volume. `grantId` names the grant reference and `disbursementId` names the disbursement; both path IDs are required. [[adyen]] [[adyen-capital]]

## Key takeaways

> [!warning] Contradiction
> The operation description says the deduction is from the user's net income (raw line 7), while the request and response `basisPoints` descriptions say incoming net volume (raw lines 30 and 62). This capture does not resolve which base applies.

- The request schema marks the `repayment` object optional and both nested `basisPoints` and `updateDescription` optional. It states no range, default, or minimum required field; the operation's stated purpose is to update the repayment percentage.
- `200` returns a disbursement record with required account-holder and balance-account IDs, amount, balances, fee, grant and disbursement IDs, and repayment object. `fundsCollections` is optional and describes accounts for repayment-related transfers; it is not a receipt for a transfer.
- The captured bases are Capital `/capital/v1` test and live. Listed failures are `404` entity not found and `422` validation error. A successful configuration update does not itself establish a new grant, disbursement, booked repayment, completed debt, or bank receipt.

## Detail locators

- Purpose, servers, required path IDs and optional request-body fields: raw lines 5–31.
- `200` disbursement response fields, including monetary minor units and optional funds collections: raw lines 33–63. Error schemas: raw lines 66–101.

## Related

- [[adyen-capital]] — Capital grant, disbursement and repayment context.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/patch/grants/(grantId)/disbursements/(disbursementId)/2026-11-07|Capital API v1 disbursement repayment PATCH reference]]
