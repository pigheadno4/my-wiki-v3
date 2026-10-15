---
title: "Adyen SFTP payout result file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/payout-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/payout-result-file/2026-09-15.md"
tags: [adyen, batch-processing, payout, result-file, store-token]
---

## Overview

This 2019-last-modified Adyen SFTP reference defines `L` line records and `PayoutResult`/`StoreTokenResult` `SL` sub-lines in a **Payout result file**. It points parsing or validation errors to a separate result-file structure. The page was captured 2026-09-15. Its literal statuses and sample are file-level/result-code evidence, not proof that a destination bank or recipient received funds. See [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The `L` table gives merchant account, merchant reference, processing type `Payout`, status `Received`, `Success` or `Error`, and optional `EchoData`. It does not define a full payout lifecycle or guarantee that `Success` is final bank credit. The sample also shows an `L` row with processing type `StoreToken`, although the table lists only `Payout`; preserve this table/example mismatch.
- A `PayoutResult` `SL` holds a field-4 PSP reference described literally as **“this modification”**, plus a result code if available. If the original payout request also executed `StoreToken`, fields 6 and 7 instead identify the **stored token's PSP reference** and its result code. The page does **not** define an original-payment-authorisation PSP reference in this `PayoutResult` schema; do not substitute the conditional token PSP reference for one.
- A separate `StoreTokenResult` `SL` has a field-4 PSP reference also described as “this modification” and a result code if available. This distinct sub-line records a StoreToken operation result, not a beneficiary payout result.
- The `TEST` example shows a `Payout` `L` status of `Received`, a `PayoutResult` code `[payout-submit-received]`, and a conditional StoreToken result of `Success`; it also shows a separate `StoreToken` `L`/`SL` with `Success`. Token success and payout submission receipt do not show final bank or card payout. Amount, recipient and bank-posting fields are not specified in these `L`/`SL` tables; use separate request and outcome evidence for those questions.

## Detail locators

- Lines 14–16: payout result page and validation-error file route.
- `## Payout line`, lines 18–33: `L` merchant/reference/type/status and EchoData.
- `### PayoutResult`, lines 37–49: payout-result PSP reference, optional result code, conditional stored-token reference/result code.
- `### StoreTokenResult`, lines 51–61: separate token-operation sub-line.
- Lines 63–72: `TEST` example with payout `Received`, conditional StoreToken `Success`, and example `StoreToken` `L` mismatch.

## Related

- [[adyen-batch-processing]] — batch-file flow and reciprocal source route.
- [[adyen-payouts]] — separate payout product/lifecycle context, not imported into this SFTP schema.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payout-request-file-payout-request]] — separately scoped payout request fields.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — common outer result-file records.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/payout-result-file/2026-09-15|Payout result-file reference, captured 2026-09-15]]
