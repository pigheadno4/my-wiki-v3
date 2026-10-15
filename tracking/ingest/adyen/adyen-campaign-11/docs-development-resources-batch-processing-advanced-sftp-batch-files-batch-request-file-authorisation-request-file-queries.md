# Fixed retrieval checks — Adyen Authorisation request parent file

## Q1 — Purpose, scope, and non-inference

**Question:** What does this Authorisation request file page define, and what should a reader avoid inferring about card details or payment outcome?

**Expected answer:** It defines the SFTP batch Authorisation request's parent `L` record, whose metadata applies to corresponding `SL` records. The child sub-line number and types vary by payment method, so this page does not supply a complete card-payment schema. A request-line format does not establish that Adyen processed or authorised any particular payment, and the merchant reference in field 6 is not described as a PSP reference.

**Raw locators:** `Authorisation line`, lines 16–28, especially 18 and 27; `Authorisation sub-lines`, lines 30–32.

**Canonical wiki route:** [[adyen-index]] → [[adyen-batch-processing]] → [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file]].

## Q2 — Central fields, prerequisites, and warnings

**Question:** Which parent-line fields and conditions are documented, and how should ValidationError and EchoData be read?

**Expected answer:** Fields 1–6 are marked required: fixed `L` record type, sequential numeric `L` line number within its batch-file block starting at 1, fixed `MerchantAccount` account type, merchant account name, fixed `Authorisation` processing type, and transaction-specific merchant reference. Field 7 `EchoData` is optional, at most 80 characters, returned unchanged in a result file, and not used by Adyen. The field-5 description says that a `ValidationError` column means the file instead follows the linked batch result-file ValidationError structure; this is no proof of successful authorisation. The number and type of sub-lines depend on the payment method and must be resolved in its child reference.

**Raw locators:** `Authorisation line`, table lines 20–28; `Authorisation sub-lines`, lines 30–32.

**Canonical wiki route:** [[adyen-index]] → [[adyen-batch-processing]] → [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file]] → its pinned [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/2026-09-15|raw snapshot]].
