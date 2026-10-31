# Fixed queries — Account API POST /getAccountHolder

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-getaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/getAccountHolder

## Q1

For `Account/latest/post/getAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: The captured TEST Account API v6 `POST /getAccountHolder` retrieves Classic account-holder details. The request uses `accountCode` or `accountHolderCode`; each is conditional on the absence of the other. `showDetails` is optional and described as true when details should be returned. The response distinguishes the holder, its listed accounts, and optional balance-platform migration IDs. The page lists authentication and permission failures but no named role. Its extensive response schema includes creation/update descriptions that do not add input requirements for this retrieval request. See the full canonical source stem and URL above; pinned raw `raw/adyen/api-explorer/Account/latest/post/getAccountHolder/2026-09-15.md` lines 5–35, 38–45, 144–205, 441–464.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: A 200 says the request succeeded; a 202 says accepted while processing remains incomplete. Optional response fields can expose holder status/events, a separate aggregate payout gate, processing state, per-account status/schedules, KYC checks, a freshness timestamp and migration mappings. The schema alone proves no actual holder status, KYC approval, migrated holder, payout execution, processed payment, or bank receipt; `disabled=false` alone is not `allowPayout=true`. The page lists 400, 401, 403, 422 and 500 errors and only generic 400/403 response examples. Its server is TEST Account v6; this snapshot does not establish current live behavior. See the full canonical source stem and URL above; pinned raw lines 36–45, 144–230, 233–234, 339–425, 428–516.
