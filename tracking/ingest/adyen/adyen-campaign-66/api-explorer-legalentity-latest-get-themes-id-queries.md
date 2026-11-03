# Original query answers — api-explorer-legalentity-latest-get-themes-id

## Q1

For `GET /themes/{id}`, the 2026-11-03 capture describes a Legal Entity Management API v4 theme-detail retrieval, with the listed TEST server `https://kyc-test.adyen.com/lem/v4` (raw lines 5–18). The caller supplies the unique theme `id` as a required path string; this operation shows no query or body inputs (lines 20–25). A 200 response identifies the theme by `id` and requires `createdAt` and `properties`; `description` and `updatedAt` are optional (lines 27–39). The example's visual-property keys are illustrative (lines 106–128). Limits are Live 700 and Test 200 requests per 5 seconds, plus 5 failed requests per 10 seconds (lines 9–15). The page names no caller role, defaults, or idempotency option. [[source-adyen-api-explorer-legalentity-latest-get-themes-id]] — https://docs.adyen.com/api-explorer/legalentity/latest/get/themes/(id)

## Q2

A 200 means the theme-detail read succeeded and returns configuration fields (raw lines 27–39); it does not show creation of a link, onboarding review/approval/activation, legal-entity eligibility, payment, settlement, or bank receipt. The capture lists 401 authentication and 403 insufficient-permission errors, alongside 400, 422, and 500 errors (lines 42–104). It specifies no idempotency, deletion/update lifecycle, propagation timing, asynchronous decision, reversal, or conflict behavior for this GET. Its v4 TEST server and November 2026 snapshot do not prove current Live access or runtime outcome (lines 1–18). [[source-adyen-api-explorer-legalentity-latest-get-themes-id]] — https://docs.adyen.com/api-explorer/legalentity/latest/get/themes/(id)
