---
title: "Adyen Business Accounts: View transfer details"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/view-transfers-details"
raw_files:
  - "adyen/docs/business-accounts/view-transfers-details/2026-09-15.md"
tags: [adyen, business-accounts, transfers, retrieval, confirmation-letter]
---

## Overview

This 2019-modified, 2026-09-15-captured Business Accounts guide explains how a platform views third-party transfer lists and details in Customer Area or through the Transfers API. It describes initiation, Adyen authorization and booking against a balance account as distinct stages, and recommends transfer webhooks for recurring tracking and reconciliation. A transfer's API state or downloadable confirmation letter is not proof that the beneficiary bank received funds. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- The documented prerequisite is an Adyen for Platforms integration. API retrieval calls need the **TransferService Webservice Retrieve role**. In Customer Area, the **Balance platform base role** permits transfer viewing; separate roles govern confirmation-letter download and unmasked PII (raw lines 35–45, 770–778).
- For a list, use Customer Area **Balances > Transfers** with one balance platform at a time, or `GET /transfers`. The page labels `createdSince` and `createdUntil` required, specifies a period of less than six months between them, and says at least one unique identifier must be supplied. `balanceAccountId` and `accountHolderId` are listed identifiers; `limit` controls page size. The response has a `data` array and optional next/previous `_links` (raw lines 47–72, 253–258).
- For one transfer, search Customer Area by transfer ID or description, or call `GET /transfers/{id}` with the transfer ID in the path (raw lines 465–486). The detail response describes amount, incoming/outgoing `direction`, event history, internal `reference`, and current `status` such as `received`, `authorised` or `booked` (raw lines 632–640). The examples include both a third-party `bankTransfer` and an `internalTransfer`; do not conflate their counterparties or treat an example status as a real transfer result (raw lines 260–462, 642–752).
- A downloadable PDF transfer confirmation letter describes beneficiary and transfer details and confirms **Adyen sent an instruction to carry out the transfer**. It does not say the recipient bank received funds. The guide describes the download flow for booked bank transfers, the extra download role, and a separate **View bank transfers PII** role; without the latter, PII is masked (raw lines 754–795).
- The captured list-request example contradicts its own stated conditions: it says the range must be under six months and an identifier is required, but its narrative says May 2025 to May 2026, while its curl sample uses a May 2026 one-day range with no identifier (raw lines 66–84). Use the stated condition for retrieval planning and verify against current API documentation before relying on sample code. The list example also combines `reason: counterpartyAccountNotFound` with `status: booked` (raw lines 304–312); do not infer successful beneficiary receipt from `booked` alone.

## Detail locators

- Roles and Customer Area list filters: raw lines 35–58.
- List API parameters, date/identifier warning, test-environment library snippets and response pagination: raw lines 60–258.
- Illustrative bank and internal transfer list objects: raw lines 260–462; single-transfer lookup and example event/tracking fields: raw lines 465–752.
- Confirmation-letter fields, access roles, masking and download path: raw lines 754–795.

## Related

- [[adyen-business-accounts]] — product and resource scope.
- [[source-adyen-docs-platforms-transfer-transactions-track-webhooks]] — transfer lifecycle events.
- [[source-adyen-docs-business-accounts-manage-access]] — credential and Customer Area access.
- [[adyen-platform-internal-transfers]] — separate internal balance-account transfer concept.

## Raw Sources

- [[raw/adyen/docs/business-accounts/view-transfers-details/2026-09-15|Captured View transfer details guide]]
