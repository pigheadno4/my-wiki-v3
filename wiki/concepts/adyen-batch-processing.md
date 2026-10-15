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

- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file-payoutdecline-request]] — 2026-09-15 SFTP PayoutDecline request `SL` schema with original payout PSP reference and review/decline role requirement; no result or finality claim.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file-payoutconfirm-request]] — 2026-09-15 SFTP PayoutConfirm mandatory `SL` field reference, original-payout PSP-reference position and review/decline-permission prerequisite.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-cancelorrefund-request]] — 2026-09-15 SFTP Modification/CancelOrRefund request `SL` schema for original payment PSP reference and partial-cancellation prohibition; action selection and outcome are not defined.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-cancel-request]] — 2019-modified SFTP Cancel request `SL` schema requiring the original-payment PSP reference and excluding partial cancellation modifications (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-refund-request]] — 2026-09-15 SFTP Modification/Refund request sub-line schema for original payment PSP reference and amount/exponent/currency; no refund-result or partial-eligibility rule.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-capture-request]] — 2019-modified SFTP Capture request `SL` schema for original-payment PSP reference and amount/exponent/currency, with optional airline-data route and outcome boundary (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file]] — 2026-09-15 SFTP Authorisation request parent `L` line fields and method-dependent `SL` scope; request structure only, with ValidationError result-format routing.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file]] — 2026-09-15 SFTP Modification request `L` field and five action-type schema, optional merchant reference, and variable operation-specific sub-line route.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file]] — 2026-09-15 SFTP PayoutModification request `L` schema for required `PayoutConfirm`/`PayoutDecline` action and merchant reference, with variable sub-lines and separate result routing.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-refundwithdata-request-file]] — 2026-09-15 parent RefundWithData SFTP request-file `L` metadata schema, merchant-reference options, and one-child-sub-line navigation; its ValidationError result wording appears in a request table.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-storetoken-request-file]] — 2026-09-15 SFTP StoreToken parent `L` request-line fields and child sub-line navigation, separate from validation and token/payout outcomes.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payout-request-file]] — SFTP Payout request parent `L` record for merchant account, processing type, merchant reference and optional echo; sub-line details are absent from this page (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file-validationerror]] — 2019-modified, 2026-09-15-captured per-entry `ParseOrValidationError`/`ValidationErrorResult` result schema; successful and invalid entries can coexist in one file.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-authorisationreferral-request]] — 2026-09-15 SFTP AuthoriseReferral Modification request format for MOTO referral, original payment PSP reference and authCode; its mandatory-sub-line sentence conflicts by saying bank-transfer authorisation.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-payout-result-file]] — 2019-modified SFTP Payout `L`/`SL` result schema with conditional StoreToken references, `Received` example and no final-bank-outcome proof (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-file-naming-and-structure]] — 2020-modified SFTP batch request/result/ACK filename patterns, platform-scoped sequence and CSV structure reference; FH field-9 requiredness conflicts with the common request-file table, and ACK-generation wording needs the dedicated ACK guide (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-payoutmodification-result-file]] — 2026-09-15 SFTP PayoutModification result `L`/`ModificationResult` schema for confirm/decline status, distinct modification and original-payout PSP references, and validation-error routing.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-refundwithdata-result-file]] — 2019-modified RefundWithData SFTP `L`/`SL` result schema, original-payment PSP reference, literal statuses and `Received` example; no amount or final-refund proof (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-authorisation-result-file]] — 2019-modified, 2026-09-15-captured SFTP Authorisation result `L` statuses and `PaymentResult` PSP/reference/code/reason schema, with separate ValidationError route.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-accountupdater-request-file]] — 2019-modified, 2026-09-15-captured SFTP AccountUpdater input schema for merchant-referenced `L`, Recurring shopper/token references, Single card/expiry fields, and live-PAN PGP condition.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]] — 2019-modified SFTP Modification `L`/`SL` result schema with action/status, separate modification and original-authorisation PSP references, and validation-error boundary (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-ach-direct-debit]] — 2019-modified bank-transfer/ACH DD SFTP authorisation-request sub-line schema for amount/exponent, bank account and addresses, with table/example conflicts (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-capture-request-capture-with-airline-data]] — SFTP Modification/Capture airline-data sub-line guide with conditional leg and passenger records and example-only capture reference context (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-a-recurring-payment]] — SFTP recurring Authorisation sub-line format for amount/exponent/shopper, stored-detail selection and interaction type, with inconsistent optional order-reference example (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-an-iban-payment]] — 2026-09-15 SFTP batch IBAN Authorisation request sub-line schema for bank transfer/SEPA Direct Debit, including required IBAN country/account fields, optional records, and a card-example mismatch.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payout-request-file-payout-request]] — 2026-09-15 SFTP batch payout request sub-line schema for payout details, recurring type and card/bank/IBAN destination, with permission and example/table discrepancies.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-with-airline-data]] — 2026-09-15 SFTP airline-data `SL` field reference for authorisation requests, including conditional leg/passenger records, optional merchant order reference, and example-versus-table discrepancies.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-a-card-payment]] — 2026-09-15 SFTP batch card Authorisation request sub-line schema for mandatory PGP-protected PaymentDetails/Card records and conditional fields; examples have counter/record-line inconsistencies.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-accountupdater-result-file]] — 2020-modified Account Updater result-file `L`/`SL` schema for batch, automatic and real-time variants, conditional PAN/PGP, and result-versus-payment boundaries (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-storetoken-request-file-storetoken-request-for-payout]] — 2019-modified payout-oriented StoreToken batch sub-line and field reference, including mandatory shopper/recurring/instrument records and permission warning (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-refundwithdata-request-file-refundwithdata-request]] — 2026-09-15 snapshot of the RefundWithData SFTP request sub-line schema, with field/value requiredness, Card/IBAN paths, and unresolved authorization wording and example/table conflicts; no financial outcome semantics.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — SFTP batch result common `FH`/`FT`/`BH`/`BT` file and block records after successful ACK validation, with type-specific results routed separately (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — 2026-09-15 SFTP batch request-file reference for common FH/BH/BT/FT fields, identifiers, requiredness and counters; its merchant-versus-company header wording and the existing multi-account qualification remain unresolved.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] — 2026-09-15 SFTP batch hub for Support-provisioned connection, SSH and PGP input/result protection, and file-rejection ACK routing; its multi-account-modification enablement is not reconciled with the parent one-merchant-per-file table.


- [[source-adyen-docs-development-resources-batch-processing-submit-modifications]] — 2026-09-15 Customer Area CSV modification guide for roles, multi-account enablement, 6,000-row and field rules, review/upload, and validation-versus-webhook outcome; opening operation list and table differ on `authoriseReferral`.


- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]] — 2026-09-15 Adyen Docs snapshot of batch ACK file validation status, error-line identity and next-submission-number caveat.


- [[source-adyen-docs-development-resources-batch-processing]] — 2026-09-15 webpage snapshot comparing Customer Area and SFTP batch routes, request types, file shapes and setup boundaries.

## Related

- [[adyen]]
