# A2A issuer API overview retrieval checks

## Q1 — Who uses this API, and what payment actions does its overview list?

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-business-accounts.md` → `[[source-adyen-api-explorer-a2aissuer-api-latest-overview]]` ([canonical URL](https://docs.adyen.com/api-explorer/a2aissuer-api/latest/overview)). The pinned raw identifies A2A payments API v1 as an issuer-side API for direct payments by users with Adyen Business accounts (lines 5–7). It lists detail retrieval, SCA confirmation and cancellation of pending transactions (lines 9–15), plus three iDEAL profile routes and three payment routes (lines 48–58). It does not define merchant checkout behavior or demonstrate a completed payment.

## Q2 — What access and environment boundaries apply to the catalog?

Route: `[[source-adyen-api-explorer-a2aissuer-api-latest-overview]]` ([canonical URL](https://docs.adyen.com/api-explorer/a2aissuer-api/latest/overview)) → pinned raw lines 17–46. Requests use an API key via `X-API-Key` (lines 17–26); the credential needs `Role for A2A Issuer payments - API`, with Adyen-contact setup (lines 28–34). Live use calls for a key from the live Customer Area (lines 36–38). Test and live `/a2aissuer-api/v1` bases are separate (lines 40–46). These requirements and route listings do not prove current role assignment, user SCA or funds movement.
