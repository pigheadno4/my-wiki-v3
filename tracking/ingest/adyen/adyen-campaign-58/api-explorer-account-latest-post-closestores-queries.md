# Fixed-query audit: api-explorer-account-latest-post-closestores

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-closestores.md` — https://docs.adyen.com/api-explorer/Account/latest/post/closeStores
Pinned evidence: `raw/adyen/api-explorer/Account/latest/post/closeStores/2026-09-15.md` (SHA-256 `101765c44e283bb2c8486b83348e7d818960fa17ebc1922f0358f3addca2cd4a`).

## Q1

For `Account/latest/post/closeStores`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The API page calls `POST /closeStores` an operation to close stores associated with an account holder (raw lines 5–7). Its server is Account v6 TEST (lines 9–10). The request body table requires `accountHolderCode`, the account holder's code, and `stores`, an array of store strings (lines 14–18). The 401 and 403 descriptions identify authentication and sufficient permissions as access gates (lines 52–66). The page states no other request-body conditions, prerequisites, or store eligibility rules. Retrieve `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-closestores.md` at https://docs.adyen.com/api-explorer/Account/latest/post/closeStores.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the request succeeded and lists optional `invalidFields`, request `pspReference`, and `resultCode` fields (raw lines 20–36). The page also lists 400, 401, 403, 422, and 500 descriptions and optional error-body fields (lines 39–101); the 400/403 JSON examples are illustrative (lines 103–127). The captured reference does not define result-code values, closure propagation timing, idempotency, reversal, later approval/verification, or any financial outcome. The listed server is TEST Account v6 (lines 9–10), and this is a 2026-09-15 raw capture (line 2), so it does not prove current live availability or an executed closure. Retrieve `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-closestores.md` at https://docs.adyen.com/api-explorer/Account/latest/post/closeStores.
