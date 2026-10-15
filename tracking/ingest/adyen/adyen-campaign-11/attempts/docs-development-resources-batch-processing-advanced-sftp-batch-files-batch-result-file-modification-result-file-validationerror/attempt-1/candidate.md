---
title: "Batch result file with validation errors | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file-validationerror"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file-validationerror/2026-09-15.md"
tags: [adyen, batch-processing, sftp, validation-error, result-file]
---

## Overview

This Adyen SFTP **batch result-file validation-error schema** (last modified 2019-10-25; captured 2026-09-15) defines an `L` error row and `ValidationErrorResult` `SL` detail when parsing or validation of a request entry fails. Although its URL sits under `modification-result-file`, the page states that successful lines and validation-error lines can occur within the same batch result file and includes an Account Updater example. It is not a blanket declaration that the entire file or every transaction failed. [[adyen-batch-processing]]

## Key takeaways

- The `L` row uses `MerchantAccount`, a merchant account name, fixed `ParseOrValidationError` processing type and fixed `ValidationError` status. Its merchant-reference field is returned when an optional merchant reference was included in the corresponding request; examples also show `N/A`. `EchoData` is an echo field, not data Adyen uses to process the payment. See raw lines 18–31.
- The `SL` row uses fixed `ValidationErrorResult`, requires field 4 to be empty, and puts the error description in field 5. Examples include invalid amount, a missing original `pspReference` for a modification, and invalid merchant account in an Account Updater request. The phrase about a missing PSP reference is an error description, not a PSP reference returned by this schema. See raw lines 33–66.
- This entry-level validation status is distinct from a batch acknowledgment's file-validation result and from the successful result schema for a given request type. It cannot by itself establish other entries' status, a payment's financial outcome, or whether retrying the request is safe. Use the affected request/result sources and existing operation state before deciding an action.

## Detail locators

- **Scope and mixed success/error qualification:** raw lines 14–16.
- **`L` account, optional echoed merchant reference and fixed error markers:** raw lines 18–31.
- **`SL` fixed type, empty field 4 and error text/examples:** raw lines 33–66.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]] — batch acknowledgment and file-validation stage
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — common result-file structure
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]] — modification-result schema distinct from this validation-error entry

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file-validationerror/2026-09-15|Adyen batch validation-error result file — collected 2026-09-15]]
