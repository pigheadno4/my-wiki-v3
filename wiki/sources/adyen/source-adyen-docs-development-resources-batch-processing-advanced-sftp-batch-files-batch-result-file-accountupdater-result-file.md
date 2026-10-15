---
title: "Adyen Account Updater batch result file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/accountupdater-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/accountupdater-result-file/2026-09-15.md"
tags: [adyen, account-updater, batch-processing, sftp, result-file, pgp]
---

## Overview

This dated Adyen reference defines the Account Updater **batch result file**: encryption/PAN conditions, the request-level `L` line, and the corresponding result `SL` sub-line. It covers scheduled batch, automatic, and real-time Account Updater result variants; those variants are not the same flow. The raw page was last modified 2020-07-14 and captured 2026-09-15. See [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The result file is encrypted **only if all three stated conditions hold**: the request file was encrypted, a company-account PGP key with Purpose `AccountUpdater` is registered, and the result file contains a card number. The page says an unencrypted result file contains no PAN. Parsing or validation errors instead use the separately linked validation-error result structure. This page gives no basis to treat an unencrypted result as containing a card number.
- An `L` record carries metadata for its corresponding `SL` record: merchant account, requested type (`ScheduleAccountUpdater`, `AccountUpdaterAutoUpdate`, or `AccountUpdaterRealtime`), merchant reference, and a `Scheduled`/`Error`/`Success` status and `EchoData` where applicable. The line status and `EchoData` fields do **not** apply to the real-time type. `L` `Success` is not a successful card-detail change or charge.
- The `SL` type distinguishes scheduled batch (`AccountUpdaterResult`), automatic/API (`AccountUpdaterAutoUpdateResult`), and real-time authorization (`AccountUpdaterRealtimeResult`). For non-real-time results, `Submitted` means the record was submitted to and processed by the scheme; `Not Submitted` means it was not. This submission field is blank for the real-time type. Field 4 describes a PSP reference for the listed `L` request types but also describes a merchant reference for `AccountUpdaterResult`; the scheduled-batch overlap is unresolved in the page. Do not assume one identifier for every variant.
- The `SL` action result groups are `NoChange`, `CloseAccount`, `PANChanged`, `CardExpiryChanged`, `ContactCardAccountHolder`, and `Error`; the detailed subvalues are in the raw field table. `NoChange` and `Error` are excluded for the real-time `L` type. `ContactCardAccountHolder` is Visa-only and says the customer requested that the issuer withhold updated details, even though card information changed. It is a disclosure/result state, not proof of a new consent grant.
- The processed date is when Adyen processed the scheme file. A new alias is populated only for changed PAN or expiry. Field 11 is an internal/implementation refusal reason on `Not Submitted` batch/automatic results, but an acquirer response code for real-time results. These Account Updater and response-code fields are not proof of successful authorization, capture, or settlement. The sample `TEST` file at raw lines 135–154 illustrates result rows, not production outcomes or a universal field fill pattern.

## Detail locators

- Lines 14–28: conditional encryption, no-PAN alternative, validation-error structure.
- `## AccountUpdater line`, lines 30–55: `L` record metadata, request variants, status and EchoData real-time exclusions.
- `## AccountUpdater sub-line`, lines 57–77: `SL` types, field-4 identifier ambiguity, submitted/not-submitted condition.
- Sub-line field 6, lines 78–123: detailed action subvalues, variant exclusions, Visa contact-cardholder withholding.
- Sub-line fields 7–12, lines 124–133: processed date, alias/expiry, refusal-reason variant, PAN conditions.
- Lines 135–154: illustrative `TEST` result file.

## Related

- [[adyen-batch-processing]] — batch-file route and reciprocal source link.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — common outer result-file records; distinct from this Account Updater `L`/`SL` schema.
- [[source-adyen-docs-online-payments-account-updater-batch-account-updater]] — separate Batch Account Updater request and follow-up guide.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/accountupdater-result-file/2026-09-15|Account Updater result-file reference, captured 2026-09-15]]
