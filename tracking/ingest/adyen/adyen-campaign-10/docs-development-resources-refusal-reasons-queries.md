# Refusal reasons retrieval checks

## Q1 — Purpose, scope, and inference limit

**Query:** What does Adyen's refusal-reasons page explain, and what should a merchant not infer from HTTP `200 OK` or a test refusal trigger?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-development-resources-refusal-reasons.md` → pinned raw `raw/adyen/docs/development-resources/refusal-reasons/2026-09-15.md`, lines 19–27 and 29–34. It is an online payment authorization refusal-code catalog. HTTP `200 OK` confirms request submission and Adyen processing, not payment or modification execution. Test trigger values are for Adyen's test environment; they do not establish live issuer behavior, payment authorization, capture, settlement, or a particular transaction's outcome. Do not expose detailed refusal reasons to shoppers (line 27).

## Q2 — Central capability, prerequisites, warnings

**Query:** Where are refusal fields found, how should `refusalReasonCode` be interpreted, and when does the page permit retry?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-development-resources-refusal-reasons.md` → pinned raw lines 23–25, 29–34, 49–53, 55–107. Scope is an online-payments integration; the Standard webhook carries refusal reasons without an additional webhook subscription (lines 29–34). In unsuccessful payment or modification responses, `resultCode`, `refusalReason`, and `refusalReasonCode` describe the issue; capture/refund refusal fields also occur in `CAPTURE_FAILED` and `REFUND_FAILED` webhook `additionalData` (line 25). Code `0` with `Authorised` must be ignored (line 61). Retry advice is row-specific: code `38` requires 3D Secure after an exemption decline, code `40` calls for a different payment method, codes `41`–`42` state their own paths, and code `46` is an excessive-retry block (lines 101–106). Do not infer a blanket retry permission or final outcome from a refusal label.
