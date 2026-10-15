---
title: "Adyen Batch Processing"
type: concept
category: technology
tags: [adyen, batch-processing, bulk-requests, customer-area, sftp]
---

> [!warning] Contradiction
> The batch overview says one transaction type for one merchant account per SFTP file. The SFTP guide says one request type per merchant account and mentions Support-enabled modifications for multiple merchant accounts, without defining whether the one-merchant-account-per-file layout changes. These dated statements remain unresolved; confirm the approved file composition with Adyen for that case. [[source-adyen-docs-development-resources-batch-processing]] [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]]

## Definition

Adyen's batch-processing overview presents input-file upload as a way to submit many payment or modification requests in bulk. It is a dated overview (2019 last-modified metadata, captured 2026-09-15), not an execution record or an account-eligibility determination. Adyen notes that file preparation often takes manual work and recommends API use for regular payments and modifications.

## Upload routes

- Customer Area accepts modification-only simple CSV files. The overview says modifications for different merchant accounts can share a file and the Customer Area helps fill missing fields and correct errors.
- SFTP covers the listed Authorisation, Modification, RefundWithData, Payout, PayoutModification, AccountUpdater and StoreToken request types. Its complex CSV has headers, footers, counters and multiline records. The overview limits each file to one transaction type for one merchant account and calls for SFTP setup and PGP encryption.

## Outcome boundary

This landing page does not define acknowledgment or per-record result-file states. File preparation, upload or transport is not proof that an individual authorization, capture retry, refund or payout succeeded. The refund and failed-capture examples do not establish whether a particular unresolved operation is safe to retry. Use the route-specific request, acknowledgment and result sources for those distinct questions.

## Sources

- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] — 2026-09-15 SFTP batch hub for Support-provisioned connection, SSH and PGP input/result protection, and file-rejection ACK routing; its multi-account-modification enablement is not reconciled with the parent one-merchant-per-file table.


- [[source-adyen-docs-development-resources-batch-processing-submit-modifications]] — 2026-09-15 Customer Area CSV modification guide for roles, multi-account enablement, 6,000-row and field rules, review/upload, and validation-versus-webhook outcome; opening operation list and table differ on `authoriseReferral`.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]] — 2026-09-15 Adyen Docs snapshot of batch ACK file validation status, error-line identity and next-submission-number caveat.


- [[source-adyen-docs-development-resources-batch-processing]] — 2026-09-15 webpage snapshot comparing Customer Area and SFTP batch routes, request types, file shapes and setup boundaries.

## Related

- [[adyen]]
