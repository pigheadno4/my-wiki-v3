# Fixed retrieval checks — PayoutModification request file

## Q1 — What is this page for, what is its scope, and what should not be inferred?

This 2026-09-15 Adyen page specifies the common `L` row for an SFTP PayoutModification **request** file and says operation-specific `SL` count/types vary. It is not a payout-modification result file, a status for the original payout, or evidence of bank settlement. Retrieve through `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file]]` → `[[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/2026-09-15]]`; raw lines 14–33. Canonical page: https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file.

## Q2 — What fields and choices are required, and what outcome warning matters?

The `L` row requires fields 1–6: record identifier, sequential block-local line number, `MerchantAccount` and account name, `PayoutConfirm` or `PayoutDecline` processing type, and a merchant reference for the transaction (raw lines 20–28). Field 7 echo is optional; sub-line schema depends on the selected action and is not supplied here (lines 29–33). A `ValidationError` mention routes to a separate **result-file** error format (line 27). Neither action label nor merchant reference proves original payout status or final funds transfer; obtain result status and the distinct original-payout PSP reference from the separate PayoutModification result source via the same concept route.
