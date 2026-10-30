# C56 fixed query answers — Disputes POST /supplyDefenseDocument

Source: `source-adyen-api-explorer-disputes-latest-post-supplydefensedocument` — https://docs.adyen.com/api-explorer/Disputes/latest/post/supplyDefenseDocument
Pinned raw: `raw/adyen/api-explorer/Disputes/latest/post/supplyDefenseDocument/2026-09-15.md` (fully read contiguous numbered lines 1–65 and 66–128; SHA-256 `3dcf09daf17995e539b57bec65f645ea8f3096371af02df87837020e2a1ae915`).

## Q1: For `Disputes/latest/post/supplyDefenseDocument`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?

`POST /supplyDefenseDocument` supplies document evidence for a **specific dispute** under Disputes Service **v30 test**, not a payment or Checkout request (raw lines 5–10). The request-body table marks `defenseDocuments`, `disputePspReference`, and `merchantAccountCode` required, and each document's `content`, `contentType`, and `defenseDocumentTypeCode` required (lines 14–22). The sole example uses PDF and `DefenseMaterial`, which does not establish universal format, size, code, or dispute-specific eligibility (lines 24–39). This reference does not itself state account role or scheme deadline; the broader Disputes API guide is a separate route for those prerequisites.

## Q2: For `Disputes/latest/post/supplyDefenseDocument`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP `200` establishes request success at the API layer; `disputeServiceResult.success` indicates whether this **supply request** succeeded, and an optional `errorMessage` may accompany it. The one example shows `success: true` (raw lines 40–50, 117–128). This does not submit a final defense, prove evidence reached or was accepted by an issuer, or establish a dispute win; the separate workflow guide places final submission at `/defendDispute`. HTTP `400`, `401`, `403`, `422`, and `500` error body schemas are listed without examples, and their generic payment `pspReference` field is distinct from the dispute selector `disputePspReference` (lines 53–115 versus 21). The captured `latest` route shows only a v30 test server and no live outcome (lines 1–10).
