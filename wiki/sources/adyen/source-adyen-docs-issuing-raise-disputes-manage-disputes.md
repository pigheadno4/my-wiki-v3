---
title: "Adyen Issuing: manage a raised dispute"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/raise-disputes/manage-disputes"
raw_files:
  - "adyen/docs/issuing/raise-disputes/manage-disputes/2026-09-15.md"
tags: [adyen, issuing, disputes, lifecycle, api]
---

## Overview

This 2026-09-15 Issuing guide covers managing a **draft** raised dispute through the Balance Platform Transfers API: edit its information, add supporting attachments through a linked procedure, or change its status to **submitted** or **closed**. It defers general requirements and limitations to the parent Raise disputes guide. A returned status and updated webhook show a lifecycle change; this page does not establish a chargeback win or returned funds.

## Key takeaways

- For a draft, `PATCH /disputes/{id}` with changed fields; the whole dispute object need not be sent. The page groups patchable information under `duplicateInfo`, `fraudInfo` and `notDeliveredInfo`. It describes fraud `reportOnly=true` as a report with no further chargeback or fee-reversal action, default false. Conditional non-delivery fields include `agreedDeliveryLocation` when the delivery location was wrong and `didCardholderReturn` when delivery was late. Use the field tables for the remaining type-specific details.
- Set `status=submitted` by PATCH to submit a draft. A successful response includes the updated dispute object, and Adyen sends `balancePlatform.dispute.updated` with the submitted status. The example uses a TEST endpoint; submission does not itself show the card scheme's final decision.
- Only a draft can be closed when the platform no longer intends to submit it. Set `status=closed` by PATCH; after closure, it cannot be edited, submitted or reopened. A successful response and `balancePlatform.dispute.updated` show closed status, and the guide instructs the platform to notify the cardholder.
- The duplicate-info PATCH table calls `duplicateTransactionId` a boolean even while describing it as a transaction ID; the sibling duplicate-creation field table calls it a string. The close example sends one dispute ID in the PATCH path but shows a different ID in its webhook. Treat these samples as illustrations, not proof of a valid field type or correlated record.

## Detail locators

- `## Requirements`, `## Edit dispute information`: parent prerequisite link, draft-only scope, partial PATCH and type-specific field tables.
- `### Tab: duplicate`, `### Tab: fraud`, `### Tab: notDelivered`: type fields and conditional values; note the duplicate-ID type inconsistency.
- `## Submit a dispute`: `status=submitted` PATCH, TEST example and updated webhook.
- `## Close a dispute`: draft-only close, no reopening, PATCH and mismatched example IDs.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[adyen]] — provider context.
- [[source-adyen-docs-issuing-raise-disputes-duplicate]] — duplicate-creation field table for the transaction-ID type conflict.

## Related raw API references

- [[raw/adyen/docs/issuing/raise-disputes/2026-09-15|Raise disputes]] — parent guide for general requirements and lifecycle; navigation only for this entry.

## Raw Sources

- [[raw/adyen/docs/issuing/raise-disputes/manage-disputes/2026-09-15|Manage disputes guide (fetched 2026-09-15)]]
