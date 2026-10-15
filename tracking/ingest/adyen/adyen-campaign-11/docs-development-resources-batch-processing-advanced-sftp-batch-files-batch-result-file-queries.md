# SFTP batch result-file common-record retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** What does this result-file reference establish after a successful ACK validation, and can it prove that a specific payment or modification succeeded?

**Expected route:** `[[adyen-index]]` → `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]]`; pinned raw `# Batch result file` lines 14–18 and common-record sections lines 20–70.

**Expected answer:** It describes common SFTP batch result file and block records. The page says a result file can be obtained two days after a successfully validated ACK. That validation is a file-level gate, not per-operation success. This page does not define transaction-specific line outcomes, PSP references, or final payment/refund/payout lifecycle status. Use the corresponding result-type source and any required later outcome evidence.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which fields identify the file and blocks, and how should an analyst avoid confusing them with a transaction PSP reference?

**Expected route:** Same source; raw `### File Header [FH]` lines 20–42, `### File Trailer [FT]` lines 44–51, `### Block Header [BH]` lines 53–61, and `### Block Trailer [BT]` lines 63–70. Type-specific raw navigation is under the source entry's `## Related raw API references`.

**Expected answer:** `FH` repeats request-header identity such as TEST/LIVE environment, account type/name, submission platform, file sequence number, SFTP upload API credential name, file type, and optional header `EchoData`. `FT` counts blocks; `BH` has sequential block number and optional request echo; `BT` counts line records. None of these common fields is a transaction PSP reference or a per-record result. The six listed file types point to separate detail guides; the displayed TEST fragment is an example, not proof of execution.
