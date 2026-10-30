# Fixed retrieval checks — api-explorer-disputes-latest-post-retrieveapplicabledefensereasons

Canonical source: [[source-adyen-api-explorer-disputes-latest-post-retrieveapplicabledefensereasons]] — https://docs.adyen.com/api-explorer/Disputes/latest/post/retrieveApplicableDefenseReasons
Pinned capture: `raw/adyen/api-explorer/Disputes/latest/post/retrieveApplicableDefenseReasons/2026-09-15.md` (2026-09-15); Disputes API v30 TEST server. Read audit: contiguous numbered raw lines 1–100, 101–190; SHA-256 verified against trusted input.

## Q1: For `Disputes/latest/post/retrieveApplicableDefenseReasons`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?

`POST /retrieveApplicableDefenseReasons` returns applicable defense reasons for a specific dispute (raw lines 5–7). The v30 TEST request table requires `disputePspReference` assigned to that dispute and `merchantAccountCode` for its dispute transaction (lines 9–18). These identify the dispute and merchant, not a payment PSP reference or defense document. The sample body illustrates those two fields (lines 20–28).

## Q2: For `Disputes/latest/post/retrieveApplicableDefenseReasons`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 is request success. The required `disputeServiceResult.success` is a service-request flag; optional `defenseReasons` include document-type availability, requirement levels and a `satisfied` material-sufficiency flag (raw lines 29–46). `AlternativeRequired` needs Support enablement (line 41). Neither the illustrated reasons nor `success: true` prove defense submission, scheme acceptance or a won dispute (lines 113–190). Generic 400/401/403/422/500 error shapes appear at lines 49–111, with no error examples. The `latest` URL preserves the captured v30 TEST snapshot, not current live/latest availability (lines 1–2, 9–10).
