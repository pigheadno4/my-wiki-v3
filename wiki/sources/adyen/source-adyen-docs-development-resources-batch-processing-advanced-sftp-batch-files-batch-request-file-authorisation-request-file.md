---
title: "Adyen SFTP authorisation request file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, authorisation]
---

## Overview

This Adyen webpage snapshot describes the parent `L` line for an SFTP batch **Authorisation request file**. The line carries metadata for its corresponding `SL` sub-lines. The source is a request-format reference, not evidence of an authorised payment. See [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The parent line identifies its record as fixed `L`, assigns a numeric line number that starts at 1 and increments within its batch-file block, and requires fixed `MerchantAccount` as account type followed by the merchant account name.
- It requires fixed `Authorisation` as the processing type and a merchant reference unique to a specific transaction. That merchant reference is not identified here as an Adyen PSP reference.
- Optional `EchoData` can carry up to 80 characters. Adyen says it returns the content exactly in the result file and does not use that data.
- The page says the number and type of `SL` sub-lines depend on the payment method. It does not specify card fields or other method-specific sub-line schemas on this parent page. Its field-5 description also redirects a `ValidationError` column to the batch result-file ValidationError structure; that is a result-format distinction, not a successful authorisation.

## Detail locators

- `Authorisation line` and fields 1–7: pinned raw, lines 16–28. The table marks fields 1–6 required and field 7 optional.
- `Authorisation sub-lines`: pinned raw, lines 30–32. Consult the method-specific child reference for the applicable `SL` record schema.

## Related

- [[adyen-batch-processing]] — batch file routes and outcome boundary.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-a-card-payment]] — card-specific child sub-line reference.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-a-recurring-payment]] — recurring-payment child sub-line reference.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/2026-09-15|Authorisation request file, fetched 2026-09-15]]
