# SFTP payout request parent-line retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Does this page define payout destination sub-lines or prove a payout was accepted, approved, or sent?

**Expected route:** `[[adyen-index]]` → `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payout-request-file]]`; pinned raw `# Payout request file` lines 14–18, line table lines 20–29, and `## Payout sub-lines` lines 31–33.

**Expected answer:** The pinned page defines the parent `L` request line and stops just after the sub-line heading. It does not supply destination, amount, bank/card details, result record, webhook, or financial-success evidence. The separate child payout-request raw route in the source entry is navigation for those missing fields and was not read as evidence for this entry.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which fields identify the parent payout line and merchant account, and how do merchant reference, EchoData, and ValidationError differ?

**Expected route:** Same source; raw `## Payout lines` lines 16–29.

**Expected answer:** Required fields are fixed `L`, a sequential line number within the block, fixed `MerchantAccount`, the merchant account name, `Payout` processing type, and merchant reference. `MerchantAccount` is the transaction's account type, not a user permission. The merchant reference is a transaction identifier; the page oddly describes retain-or-replace options with modification-request wording, which does not establish a PSP-reference mapping. Optional `EchoData` is returned unchanged but unused by Adyen, up to 80 characters. `ValidationError` points to a distinct result-file structure, not successful payout execution.
