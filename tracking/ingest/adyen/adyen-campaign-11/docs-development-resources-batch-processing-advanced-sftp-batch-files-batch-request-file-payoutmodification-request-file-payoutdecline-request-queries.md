# Fixed retrieval checks — Adyen SFTP PayoutDecline request

## Q1 — Purpose, scope, and non-inference

**Question:** What does the PayoutDecline request page define, and what must not be inferred from its example?

**Expected answer:** It defines the mandatory `SL` sub-line for a PayoutDecline input in an SFTP PayoutModification request. Its example shows a PayoutModification file header and PayoutDecline parent/sub-line records, but example values and the presence of a request do not prove a decline was processed, a payout state became final, or a result file was produced. The merchant reference in the example `L` line is separate from the original payout PSP reference in the `SL` record.

**Raw locators:** `Mandatory sub-lines`, lines 16–25; `Example`, lines 27–36.

**Canonical wiki route:** [[adyen-index]] → [[adyen-batch-processing]] → [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file-payoutdecline-request]].

## Q2 — Capability, prerequisites, and warnings

**Question:** What are the required PayoutDecline sub-line positions and permission condition, and where would an outcome be checked?

**Expected answer:** All four table fields are marked required: fixed `SL` in position 1, numeric sub-line number in position 2 (starting at 1 and increasing within the parent line), fixed `PayoutDecline` in position 3, and the numeric **original payout PSP reference** in position 4. Adyen says the user role needs permission to review/decline a payout. This request page gives no final outcome; the distinct PayoutModification result-file source is the route for reported status and references.

**Raw locators:** `Mandatory sub-lines`, table lines 20–25; role sentence, line 38.

**Canonical wiki route:** [[adyen-index]] → [[adyen-batch-processing]] → [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file-payoutdecline-request]] → its pinned [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutdecline-request/2026-09-15|raw snapshot]].
