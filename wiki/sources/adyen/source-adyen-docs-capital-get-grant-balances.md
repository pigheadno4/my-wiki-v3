---
title: "Adyen Capital grant and grant-account details"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/get-grant-balances"
raw_files:
  - "adyen/docs/capital/get-grant-balances/2026-09-15.md"
tags: [adyen, capital, platforms, grants, balances, reporting]
---

## Overview

This Adyen Capital guide (last modified 2022-10-26, captured 2026-09-15) describes API reads for grant details after a grant has been created: list grants for an account holder, retrieve one grant, and retrieve the grant account that tracks platform grant balances and limits. The returned balance, renewal and status fields support display and repayment monitoring, but a dated documentation example is not a live debt amount, funding event, repayment completion or bank receipt.

## Key takeaways

- The stated prerequisites are a Capital-supporting Adyen for Platforms integration, Balance Platform API credentials with Capital Configuration and Grant Initiation roles, a user in a supported Capital country/region, Capital compliance preparation, a selected offer and signed ToS, and at least one disbursed grant. These are the guide's conditions for this read workflow, not evidence that any specific account has access or that a grant was actually disbursed.
- GET `/grants?counterpartyAccountHolderId=...` returns a `grants` array for the receiving **account holder**. Each grant object can identify the grant reference `id`, receiving `counterparty`, `grantAccountId`, selected `grantOfferId`, `balances` (principal, fee, total, currency), `status`, and renewal fields. `renewal.minimumAmount` appears only if `renewal.eligible=true`; `renewsGrantId` appears only if the grant was configured to renew a prior grant. Keep grant ID, grant-account ID, offer ID, account-holder ID and receiving balance-account ID distinct.
- GET `/grants/{grantId}` reads a particular grant with the same field families. The sample shows an `Active` grant with numeric principal/fee/total and a renewal minimum, but no as-of timestamp for its balance. Do not convert that sample into a current amount owed, derive an actual repayment transaction, or infer that renewal eligibility automatically gives a fresh offer. Its `status` is a string in the single-grant JSON whereas the list example uses a `status.code` object; retain that example discrepancy rather than normalizing an API schema from it.
- GET `/grantAccounts/{id}` returns the **grant account** ID, aggregate `balances` by currency and `limits` for maximum allowed total grants on that grant account. The guide's prose calls the path `id` a “query parameter” although its URL/curl place it in the path; use the route as written and avoid treating the example's negative limit values as a user-available cash balance or universal credit limit.
- Examples are separate, illustrative responses rather than a coherent ledger. In the list, grant 2 `renewsGrantId` points to grant 1; in the single-grant example, grant 1 points back to grant 2. This cycle and the status-shape mismatch require actual response identifiers and source records before joining grants or asserting final debt/outcome.

## Detail locators

- Opening and `## Requirements`: post-creation purpose, integration/API roles, country, offer/ToS and prior-disbursement prerequisites.
- `## Get all grants of an account holder`: account-holder query filter, grant/offer/account identities, balances/status and conditional renewal fields; list example.
- `## Get details of a specific grant`: grant-ID path, per-grant fields and example status/renewal discrepancy.
- `## Get details of your grant account`: grant-account route, aggregate balances and limits; “query parameter” prose versus path URL.
- `## See also`: navigation to lifecycle, disbursement and reconciliation guides.

## Related

- [[adyen-capital]] — main Capital concept.
- [[source-adyen-docs-capital-grant-lifecycle-and-status]] — separate lifecycle/status reference.
- [[source-adyen-docs-capital-reporting-and-reconciliation]] — separate repayment evidence and reconciliation route.
- [[adyen-platforms]] — platform/account-holder context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/get-grant-balances/2026-09-15|Adyen Capital get-grant-details guide (fetched 2026-09-15)]]
