---
title: "AccountUpdater request file | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/accountupdater-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/accountupdater-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, account-updater, card-data]
---

## Overview

This Adyen SFTP `AccountUpdater` **request-file format** guide (last-modified metadata 2019-10-21; collected 2026-09-15) defines a per-transaction `L` metadata record and two alternative `SL` request types: `AccountUpdaterRecurring` and `AccountUpdaterSingle`. It is field-level input guidance under [[adyen-batch-processing]], not an Account Updater result file or evidence of a changed card, stored credential, or payment outcome.

## Key takeaways

- The `L` table requires record identity and sequence, `MerchantAccount`, merchant account name, fixed `AccountUpdater` processing type, and a merchant reference for the transaction. `EchoData` is optional, returned unchanged when populated, and not used by Adyen for processing. The table says `ValidationError` in the processing-type column instead calls for a separately linked **batch result-file** structure; it is not described as another request type. See raw lines 18–30.
- `AccountUpdaterRecurring` is presented for when shopper payment details are unavailable. Its mandatory `SL` table requires a shopper reference plus field 5: a card alias if card details are not stored, or a stored recurring detail reference or `LATEST` if they are stored. The shopper reference identifies the shopper; the `L` merchant reference identifies a transaction. The example's email-shaped shopper reference is an example, not an email-format requirement. See raw lines 32–70.
- `AccountUpdaterSingle` is presented when card details are at least partly available. Its mandatory `SL` requires card number or alias, expiry month/year, and cardholder name. Field 7 is optional in the table but explicitly says to leave CVC blank; Maestro UK start month/year and one-digit issue number are optional. The page permits live card numbers in a batch file **only if the file is PGP-encrypted before submission**. See raw lines 72–105.
- `L` numbering is sequential within a block and `SL` numbering is sequential within its parent `L`. The request examples include common FH/BH/BT/FT wrappers, whose full schema and account/file-scope qualifications belong to the common request-file and SFTP guides. An ACK, result-file Account Updater status, and any later card or financial result are separate from this input format.

## Detail locators

- **`L` fields, requiredness, merchant reference and optional echo:** raw lines 18–30.
- **Recurring identity and reference selection, with illustrative example:** raw lines 32–70.
- **Single card-data condition, PGP requirement, field requiredness and example:** raw lines 72–105.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[adyen-tokenization]] — related stored-card lifecycle, not this file format
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common file/block format
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-accountupdater-result-file]] — result-file status schema
- [[source-adyen-docs-online-payments-account-updater-batch-account-updater]] — broader Batch Account Updater workflow

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/accountupdater-request-file/2026-09-15|Adyen AccountUpdater request file — collected 2026-09-15]]
