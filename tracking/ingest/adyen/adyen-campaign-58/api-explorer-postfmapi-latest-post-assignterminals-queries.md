# Fixed-query audit: api-explorer-postfmapi-latest-post-assignterminals

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-post-assignterminals.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/post/assignTerminals
Pinned evidence: `raw/adyen/api-explorer/postfmapi/latest/post/assignTerminals/2026-09-15.md`, SHA-256 `adeceb0a4e71a38700378ab99b5eb056b2225f435b020d9fd89c2a7db8bf5910`.

## Q1

For `postfmapi/latest/post/assignTerminals`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: This deprecated POS Terminal Management API v1 TEST endpoint assigns/reassigns terminal IDs to merchant accounts or stores, or unassigns them to company inventory (raw lines 5–12). `companyAccount` and array `terminals` are required; only these two are specified for return to company inventory (lines 16–23). Optional `merchantAccount` identifies the merchant, and `store` a store code. `merchantInventory` is required for merchant-account assignment and prohibited for store assignment; `true` puts devices in merchant inventory where they cannot be boarded, whereas `false` makes an in-store assignment described as ready for boarding/payment processing (line 21). Three request examples are lines 25–59. The page lists 401 authentication and 403 insufficient permissions without a named role (lines 84–107). It says the v1 API was deprecated January 1, 2025 with support ending April 1, 2025, directing automation to the separate Management API (line 9). Route: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-post-assignterminals.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/post/assignTerminals; raw locators `## Parameters > ### Request body`, `## Request examples`.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: The 200 body has required per-terminal `results`: `Done` assigned, `AssignmentScheduled` asynchronous, `RemoveConfigScheduled` previously boarded terminal awaiting synchronization, and `Error` per-terminal failure (raw lines 60–68). All three 200 examples happen to show `RemoveConfigScheduled` (lines 135–164). Listed errors are 400, 401, 403, 422 and 500, with illustrative JSON examples (lines 71–212). A 200 or in-store assignment description does not prove every requested device has synchronized, boarded, received configuration, become operational, or processed a payment. The page documents v1 TEST and expressly points to separate Management API automation (lines 9–12); it does not establish current live support or a Management API request contract. Route: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-post-assignterminals.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/post/assignTerminals; raw locators `## Responses`, `## Response examples`.
