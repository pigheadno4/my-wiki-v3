# Fixed retrieval checks: Customer Area batch modifications

## Q1 — Purpose and scope

**Query:** What does this Adyen Customer Area batch guide let a merchant submit, and what does `COMPLETED` or a green result not prove?

**Expected answer:** It documents CSV upload of payment modifications through Customer Area, with capture, cancel, refund and cancel-or-refund in the opening list. The field table additionally names `authoriseReferral`, an unresolved scope difference. A processed/COMPLETED batch and green row indicate file/row handling and validation; the row's modification can still fail during processing and must be checked via its later webhook. Neither upload nor a green row proves money movement, capture, refund or cancellation success.

**Raw locators:** `# Submit modifications in your Customer Area`, lines 15–24; `## Upload modifications`, lines 77–110; `## Check the result`, lines 112–122. **Canonical retrieval route:** [[source-adyen-docs-development-resources-batch-processing-submit-modifications]] → [[raw/adyen/docs/development-resources/batch-processing/submit-modifications/2026-09-15|pinned raw]].

## Q2 — Roles, columns, amounts and outcome checks

**Query:** What prerequisites and CSV rules matter, and how do account and amount fields behave?

**Expected answer:** The user needs Merchant submit batch modifications and Merchant manage payments roles. Multiple merchant accounts require Support enablement; webhooks are needed for outcome updates. The UTF-8 CSV has no header, one record per line, same fields across records, no empty fields and at most 6,000 rows. PSP reference of the payment is required. Omitted merchant account defaults to the uploading account; Customer Area can fill missing modification, amount or currency, but the chosen value applies to all rows. Amount is in minor units; for `cancelOrRefund` the page says the full amount is refunded regardless of the supplied amount. After Review Batch fixes and final Upload, inspect individual result messages and later webhooks; validation success is not processing success. The sample rows with trailing commas appear inconsistent with the stated no-empty-fields rule, so do not copy them blindly.

**Raw locators:** `## Requirements`, lines 26–35; `## Create an input file`, lines 37–75; `## Upload modifications`, lines 77–110; `## Check the result`, lines 112–122. **Canonical retrieval route:** [[source-adyen-docs-development-resources-batch-processing-submit-modifications]] → [[raw/adyen/docs/development-resources/batch-processing/submit-modifications/2026-09-15|pinned raw]].
