# Fixed retrieval checks — PayoutConfirm batch request

## Q1 — What is this page for, what is its scope, and what should not be inferred?

This 2026-09-15 Adyen page defines the mandatory `PayoutConfirm` `SL` sub-line in an SFTP PayoutModification request, with an illustrative enclosing file. It identifies the original payout to be confirmed; it does not show a successful confirmation, final original-payout state, bank settlement, or a merchant user's actual permission. Route: `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file-payoutconfirm-request]]` → `[[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutconfirm-request/2026-09-15]]`; raw lines 14–38. Canonical page: https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutconfirm-request.

## Q2 — What fields and prerequisite matter, and how are references distinguished?

All four `SL` fields are required: `SL`, parent-local sequential sub-line number, `PayoutConfirm`, and original payout PSP reference (raw lines 20–25). In the example, the separate parent `L` row carries a merchant reference; do not substitute it for the original payout PSP reference in `SL` field 4 (raw lines 29–36). The page requires a role permitted to review/decline a payout but does not name the role (line 38). Use the parent PayoutModification request source for `L` schema and the result source for later processing status; request submission alone does not establish a financial outcome. Follow the same concept→source→raw route.
