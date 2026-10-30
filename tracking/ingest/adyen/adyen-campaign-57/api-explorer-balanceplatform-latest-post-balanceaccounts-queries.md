# Fixed query check — api-explorer-balanceplatform-latest-post-balanceaccounts

Pinned source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts
Pinned raw: `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/2026-09-15.md` (SHA-256 `23d051cf8b7455f77c9aa33c14fe68a26a85ac9f5cd347c362e2619d33a32181`).

## Q1
For `balanceplatform/latest/post/balanceAccounts`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** It documents TEST Balance Platform API v2 `POST /balanceAccounts`, creating a balance account that holds an associated account holder's funds (raw lines 5–10). Only `accountHolderId` is marked required in the request body; other top-level fields are optional (14–25). `defaultCurrencyCode` defaults to EUR and cannot change after creation (18). The optional settlement delay requires Custom Sales Day Payout enablement and permits 1–20 business days or null (21–23); this is conditional on using the field. Description/reference lengths, metadata update deletion semantics and time-zone default are documented at 19–25. The 403 heading reports insufficient permissions but does not name a role (135–136). The created balance-account `id` is separate from the associated account-holder ID (74, 84).

## Q2
What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** The 200 is labeled request success and returns a required balance-account `id` plus associated `accountHolderId`; `status` is optional and described as active by default (68–92). Balance amounts are optional response data; zero-value examples are illustrative (75–81, 194–279). Documented errors are 400, 401, 403, 422 and 500 (95–192). The 422 and 500 generic examples discuss payment-instrument operations, so they cannot support balance-account-specific status rules (320–346). The page gives no deletion, verification/approval, propagation or fund-settlement result from account creation. A `latest` path with TEST `/bcl/v2` in a 2026-09-15 capture does not establish current LIVE eligibility or completed money movement (1–10).
